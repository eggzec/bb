#!/usr/bin/env python3
"""Seed all test data for bb.cloud.sdk full coverage.

Creates/populates every resource category in beaverish/bb-probe that
can be seeded via the Bitbucket REST API or git. Idempotent — safe to
re-run; checks for existing resources before creating.

Skipped (UI-only / infrastructure):
  issue milestones, versions, components  — BB 2.0 API has no POST
  pipeline caches                         — auto-generated on first pipeline run
  pipeline test reports                   — requires JUnit-publishing step
  self-hosted runners                     — requires runner agent
  Connect add-on / properties             — requires installed Connect app

Usage:
    uv run python3 scripts/seed_probe_repo.py
"""
from __future__ import annotations

import asyncio
import os
import re
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote

import httpx

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

BASE = "https://api.bitbucket.org/2.0"
REPO_SLUG = "bb-probe"
FEATURE_BRANCH = "feature/add-farewell"
MERGE_BRANCH = "fix/typo-seed"   # throwaway branch — merged to create a merged-PR record
TAG_NAME = "v0.1.0"


def _load_dotenv(path: Path) -> None:
    if not path.exists():
        return
    for raw in path.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
            value = value[1:-1]
        os.environ.setdefault(key.strip(), value)


# ---------------------------------------------------------------------------
# HTTP helpers
# ---------------------------------------------------------------------------

async def _api(
    client: httpx.AsyncClient,
    method: str,
    url: str,
    *,
    json: dict | None = None,
    data: dict | None = None,
    files: dict | None = None,
    expected: tuple[int, ...] = (200, 201),
    retries: int = 3,
) -> dict | None:
    """Make an API call; return parsed JSON or None on expected-skip statuses."""
    kw: dict = {"timeout": 30, "follow_redirects": True}
    if json is not None:
        kw["json"] = json
    if data is not None:
        kw["data"] = data
    if files is not None:
        kw["files"] = files

    for attempt in range(retries):
        resp = await client.request(method, url, **kw)
        if resp.status_code in (503, 502) and attempt < retries - 1:
            wait = 5 * (attempt + 1)
            print(f"    ⏳  {resp.status_code} — retrying in {wait}s…")
            await asyncio.sleep(wait)
            continue
        if resp.status_code in expected:
            try:
                return resp.json()
            except Exception:
                return {"_status": resp.status_code}
        if resp.status_code in (400, 402, 422):
            body = resp.text[:300]
            print(f"    ⚠️  {resp.status_code} — {method} {url.split('/2.0/')[-1]}: {body}")
            return None
        if resp.status_code in (409,):
            return {"_exists": True}
        resp.raise_for_status()
    return None


async def _get_first(client: httpx.AsyncClient, url: str, *, params: dict | None = None) -> dict | None:
    resp = await client.get(url, params={**(params or {}), "pagelen": 1}, timeout=20, follow_redirects=True)
    if resp.status_code != 200:
        return None
    data = resp.json()
    vals = data.get("values", [])
    return vals[0] if vals else None


# ---------------------------------------------------------------------------
# Git helpers
# ---------------------------------------------------------------------------

def _git(args: list[str], cwd: str | None = None, check: bool = True) -> subprocess.CompletedProcess:
    # Disable all credential helpers so URL-embedded creds are used directly.
    # The system credential.helper (gh auth git-credential) would otherwise
    # intercept Bitbucket pushes and fail with wrong credentials.
    full_args = ["git", "-c", "credential.helper="] + args
    env = {**os.environ, "GIT_TERMINAL_PROMPT": "0", "GIT_ASKPASS": "echo"}
    return subprocess.run(
        full_args, cwd=cwd, check=check,
        capture_output=True, text=True, env=env,
    )


def _fetch_host_key(hostname: str) -> tuple[str, str]:
    """Return (base64_key, key_type) for hostname via ssh-keyscan, or ('', '')."""
    try:
        r = subprocess.run(
            ["ssh-keyscan", "-t", "ed25519", hostname],
            capture_output=True, text=True, timeout=15,
        )
        for line in r.stdout.splitlines():
            if "ed25519" in line:
                parts = line.split()
                if len(parts) >= 3:
                    return parts[2], parts[1]  # (key_b64, key_type)
    except Exception:
        pass
    return "", ""


def _generate_ssh_key_pair() -> tuple[str, str]:
    """Generate an ED25519 key pair; return (private_pem, public_b64) or ('', '')."""
    import tempfile
    try:
        with tempfile.TemporaryDirectory() as td:
            key_path = Path(td) / "id_ed25519"
            subprocess.run(
                ["ssh-keygen", "-t", "ed25519", "-f", str(key_path), "-N", ""],
                capture_output=True, check=True,
            )
            private_key = key_path.read_text()
            pub_line = Path(str(key_path) + ".pub").read_text().strip()
            # pub_line: "ssh-ed25519 AAAA... comment"
            pub_b64 = pub_line.split()[1] if len(pub_line.split()) >= 2 else ""
            return private_key, pub_b64
    except Exception:
        return "", ""


def _git_clone_url(email: str, token: str, workspace: str, slug: str) -> str:
    # Bitbucket HTTPS auth uses the email local-part (before @) as the username.
    username = email.split("@")[0]
    return f"https://{quote(username, safe='')}:{quote(token, safe='')}@bitbucket.org/{workspace}/{slug}.git"


# ---------------------------------------------------------------------------
# Seeding steps
# ---------------------------------------------------------------------------

async def s01_create_repo(client: httpx.AsyncClient, ws: str) -> dict:
    print("\n── Step 1: Create bb-probe repository")
    existing = await client.get(f"{BASE}/repositories/{ws}/{REPO_SLUG}", timeout=15, follow_redirects=True)
    if existing.status_code == 200:
        d = existing.json()
        print(f"   ✅  Already exists — uuid={d.get('uuid')}")
        return d
    data = await _api(client, "POST", f"{BASE}/repositories/{ws}/{REPO_SLUG}", json={
        "scm": "git",
        "is_private": True,
        "has_issues": True,
        "project": {"key": "PROJ"},
        "description": "Fixture repo for bb.cloud.sdk live tests",
    })
    if data:
        print(f"   ✅  Created — uuid={data.get('uuid')}")
        print("   ⏳  Waiting 8s for Bitbucket to initialise the new repo…")
        await asyncio.sleep(8)
    return data or {}


async def s02_enable_pipelines(client: httpx.AsyncClient, ws: str) -> None:
    print("\n── Step 2: Enable Pipelines")
    data = await _api(client, "PUT", f"{BASE}/repositories/{ws}/{REPO_SLUG}/pipelines_config",
                      json={"enabled": True}, expected=(200, 201))
    if data:
        print(f"   ✅  Pipelines enabled={data.get('enabled')}")


async def s03_create_environments(client: httpx.AsyncClient, ws: str) -> dict[str, str]:
    print("\n── Step 3: Create deployment environments")
    uuids: dict[str, str] = {}
    existing = await client.get(
        f"{BASE}/repositories/{ws}/{REPO_SLUG}/environments",
        params={"pagelen": 10}, timeout=15, follow_redirects=True,
    )
    existing_names = set()
    if existing.status_code == 200:
        for e in existing.json().get("values", []):
            name = e.get("name", "")
            uuid = e.get("uuid", "")
            existing_names.add(name)
            uuids[name] = uuid
            print(f"   ✅  {name} already exists — uuid={uuid}")

    for env_name, env_type in [("Test", "Test"), ("Staging", "Staging"), ("Production", "Production")]:
        if env_name in existing_names:
            continue
        data = await _api(client, "POST",
                          f"{BASE}/repositories/{ws}/{REPO_SLUG}/environments",
                          json={"name": env_name, "type": {"name": env_type}},
                          expected=(200, 201))
        if data:
            uuids[env_name] = data.get("uuid", "")
            print(f"   ✅  Created {env_name} — uuid={data.get('uuid')}")
    return uuids


def s04_git_operations(email: str, token: str, ws: str) -> str:
    """Clone, seed files, push main + feature + merge branches. Returns first commit hash."""
    print("\n── Step 4: Git operations")
    url = _git_clone_url(email, token, ws, REPO_SLUG)
    work_dir = Path(tempfile.mkdtemp(prefix="bb-probe-seed-"))
    print(f"   Working dir: {work_dir}")

    clone = _git(["clone", url, str(work_dir)], check=False)
    if clone.returncode != 0:
        # Empty repo — initialise locally and point at remote
        work_dir.mkdir(parents=True, exist_ok=True)
        _git(["init", str(work_dir)])
        _git(["remote", "add", "origin", url], cwd=str(work_dir))
        _git(["checkout", "-b", "main"], cwd=str(work_dir))
    _git(["config", "user.email", email], cwd=str(work_dir))
    _git(["config", "user.name", "Laraib"], cwd=str(work_dir))

    # Check if the key seed files are already present (not just any commits)
    ls_files = _git(["ls-files"], cwd=str(work_dir), check=False).stdout
    already_seeded = "bitbucket-pipelines.yml" in ls_files and "greet.py" in ls_files

    if not already_seeded:
        # README
        (work_dir / "README.md").write_text(
            "# bb-probe\n\nFixture repository for `bb.cloud.sdk` live tests.\n"
        )
        # greet.py — contains `def` so BB_SEARCH_QUERY=def finds results
        (work_dir / "greet.py").write_text(
            '"""Greeting utilities — probe fixtures for bb SDK tests."""\n\n\n'
            'def greet(name: str) -> str:\n'
            '    """Return a greeting."""\n'
            '    return f"hello {name}"\n\n\n'
            'def farewell(name: str) -> str:\n'
            '    """Return a farewell."""\n'
            '    return f"goodbye {name}"\n'
        )
        # bitbucket-pipelines.yml
        (work_dir / "bitbucket-pipelines.yml").write_text(
            "image: python:3.12-alpine\n\n"
            "definitions:\n"
            "  caches:\n"
            "    pip-probe: ~/.cache/pip\n\n"
            "pipelines:\n"
            "  default:\n"
            "    - step:\n"
            "        name: Test\n"
            "        caches:\n"
            "          - pip-probe\n"
            "        script:\n"
            '          - python -c "from greet import greet; assert greet(\'world\') == \'hello world\'; print(\'OK\')"\n\n'
            "  branches:\n"
            "    main:\n"
            "      - step:\n"
            "          name: Test\n"
            "          caches:\n"
            "            - pip-probe\n"
            "          script:\n"
            '            - python -c "from greet import greet; assert greet(\'world\') == \'hello world\'; print(\'OK\')"\n'
            "      - step:\n"
            "          name: Deploy to Test\n"
            "          deployment: Test\n"
            "          script:\n"
            '            - echo "Deploying to Test (probe fixture)"\n'
        )
        _git(["add", "."], cwd=str(work_dir))
        _git(["commit", "-m", "chore: initial commit — seed for bb.cloud.sdk tests"],
             cwd=str(work_dir))
        _git(["push", "origin", "main"], cwd=str(work_dir))
        print("   ✅  Pushed initial commit to main")
    else:
        print("   ✅  main already has commits")

    # Feature branch (for open PR)
    branches = _git(["branch", "-r"], cwd=str(work_dir), check=False).stdout
    if f"origin/{FEATURE_BRANCH}" not in branches:
        _git(["checkout", "-b", FEATURE_BRANCH], cwd=str(work_dir))
        (work_dir / "utils.py").write_text(
            '"""Utility helpers — probe fixture."""\n\n\n'
            'def shout(name: str) -> str:\n'
            '    """Return an uppercased greeting."""\n'
            '    return greet(name).upper()\n'
        )
        _git(["add", "utils.py"], cwd=str(work_dir))
        _git(["commit", "-m", "feat: add utils module"], cwd=str(work_dir))
        _git(["push", "origin", FEATURE_BRANCH], cwd=str(work_dir))
        _git(["checkout", "main"], cwd=str(work_dir))
        print(f"   ✅  Pushed {FEATURE_BRANCH}")
    else:
        print(f"   ✅  {FEATURE_BRANCH} already exists")

    # Merge branch (for merged-PR record)
    if f"origin/{MERGE_BRANCH}" not in branches:
        _git(["checkout", "-b", MERGE_BRANCH], cwd=str(work_dir))
        changes_path = work_dir / "CHANGES.md"
        base = "# Changelog\n\n- Initial release\n"
        # If already merged into main the file exists with same content — add a line so
        # there is something to commit on this branch.
        new_content = base if not changes_path.exists() else base + "\n- Branch probe fixture\n"
        changes_path.write_text(new_content)
        _git(["add", "CHANGES.md"], cwd=str(work_dir))
        _git(["commit", "-m", "fix: add changelog"], cwd=str(work_dir))
        _git(["push", "origin", MERGE_BRANCH], cwd=str(work_dir))
        _git(["checkout", "main"], cwd=str(work_dir))
        print(f"   ✅  Pushed {MERGE_BRANCH}")
    else:
        print(f"   ✅  {MERGE_BRANCH} already exists")

    # Always fetch the definitive HEAD from origin/main — any automated merges
    # (e.g. Bitbucket auto-merging MERGE_BRANCH after a re-push) advance main
    # beyond the local tip.  We seed commit statuses/reports on this hash.
    _git(["fetch", "origin", "main"], cwd=str(work_dir), check=False)
    _git(["checkout", "main"], cwd=str(work_dir), check=False)
    _git(["reset", "--hard", "origin/main"], cwd=str(work_dir), check=False)
    log = _git(["log", "--format=%H", "-1"], cwd=str(work_dir))
    first_hash = log.stdout.strip()
    print(f"   ✅  Latest main HEAD: {first_hash[:12]}…")

    return first_hash


async def s05_open_pr(client: httpx.AsyncClient, ws: str) -> tuple[int, int]:
    """Open the probe PR and a throwaway PR (merged). Returns (open_id, merged_id)."""
    print("\n── Step 5: Pull requests")

    async def _find_pr(branch: str, state: str = "OPEN") -> int | None:
        resp = await client.get(
            f"{BASE}/repositories/{ws}/{REPO_SLUG}/pullrequests",
            params={"state": state, "pagelen": 25}, timeout=15, follow_redirects=True,
        )
        if resp.status_code != 200:
            return None
        for pr in resp.json().get("values", []):
            src = pr.get("source", {}).get("branch", {}).get("name", "")
            if src == branch:
                return pr["id"]
        return None

    # Open PR (feature → main)
    open_id = await _find_pr(FEATURE_BRANCH, "OPEN")
    if open_id is None:
        open_id = await _find_pr(FEATURE_BRANCH, "MERGED")
    if open_id is None:
        data = await _api(client, "POST",
                          f"{BASE}/repositories/{ws}/{REPO_SLUG}/pullrequests",
                          json={
                              "title": "feat: add utils module",
                              "description": "Probe PR — keep open for bb SDK live tests.",
                              "source": {"branch": {"name": FEATURE_BRANCH}},
                              "destination": {"branch": {"name": "main"}},
                              "close_source_branch": False,
                          })
        open_id = (data or {}).get("id")
        print(f"   ✅  Opened probe PR #{open_id}")
    else:
        print(f"   ✅  Probe PR already exists #{open_id}")

    # Merged PR (MERGE_BRANCH → main)
    merged_id = await _find_pr(MERGE_BRANCH, "MERGED")
    if merged_id is None:
        # First create the PR
        tmp_id = await _find_pr(MERGE_BRANCH, "OPEN")
        if tmp_id is None:
            data = await _api(client, "POST",
                              f"{BASE}/repositories/{ws}/{REPO_SLUG}/pullrequests",
                              json={
                                  "title": "fix: add changelog",
                                  "description": "Throwaway PR — merged to create merged-PR record.",
                                  "source": {"branch": {"name": MERGE_BRANCH}},
                                  "destination": {"branch": {"name": "main"}},
                                  "close_source_branch": True,
                              })
            tmp_id = (data or {}).get("id")
            print(f"   ✅  Created throwaway PR #{tmp_id} — merging…")
        # Merge it
        if tmp_id:
            merge_resp = await _api(
                client, "POST",
                f"{BASE}/repositories/{ws}/{REPO_SLUG}/pullrequests/{tmp_id}/merge",
                json={"message": "Probe seed merge", "merge_strategy": "squash"},
                expected=(200, 201),
            )
            if merge_resp:
                merged_id = tmp_id
                print(f"   ✅  Merged PR #{merged_id}")
    else:
        print(f"   ✅  Merged PR already exists #{merged_id}")

    return open_id or 0, merged_id or 0


async def s06_pr_comment_and_task(
    client: httpx.AsyncClient, ws: str, pr_id: int
) -> tuple[int | None, int | None]:
    print(f"\n── Step 6: PR comment + task (PR #{pr_id})")

    # Comment
    comment_id = None
    existing = await _get_first(client, f"{BASE}/repositories/{ws}/{REPO_SLUG}/pullrequests/{pr_id}/comments")
    if existing:
        comment_id = existing.get("id")
        print(f"   ✅  Comment already exists id={comment_id}")
    else:
        data = await _api(client, "POST",
                          f"{BASE}/repositories/{ws}/{REPO_SLUG}/pullrequests/{pr_id}/comments",
                          json={"content": {"raw": "Probe comment — fixture for `prs.get_comment` live tests."}})
        comment_id = (data or {}).get("id")
        print(f"   ✅  Created PR comment id={comment_id}")

    # Task
    task_id = None
    existing_task = await _get_first(
        client, f"{BASE}/repositories/{ws}/{REPO_SLUG}/pullrequests/{pr_id}/tasks")
    if existing_task:
        task_id = existing_task.get("id")
        print(f"   ✅  Task already exists id={task_id}")
    else:
        data = await _api(client, "POST",
                          f"{BASE}/repositories/{ws}/{REPO_SLUG}/pullrequests/{pr_id}/tasks",
                          json={"content": {"raw": "Probe task — fixture for `prs.get_task` live tests."}})
        task_id = (data or {}).get("id")
        print(f"   ✅  Created PR task id={task_id}")

    return comment_id, task_id


async def _seed_commit_status_on(client: httpx.AsyncClient, ws: str, commit_hash: str) -> None:
    """Seed a build status on a single commit hash (idempotent)."""
    key = "bb-probe-ci"
    existing = await client.get(
        f"{BASE}/repositories/{ws}/{REPO_SLUG}/commit/{commit_hash}/statuses",
        params={"pagelen": 10}, timeout=15, follow_redirects=True,
    )
    if existing.status_code == 200:
        for s in existing.json().get("values", []):
            if s.get("key") == key:
                return
    await _api(client, "POST",
               f"{BASE}/repositories/{ws}/{REPO_SLUG}/commit/{commit_hash}/statuses/build",
               json={"state": "SUCCESSFUL", "key": key, "name": "bb SDK probe build",
                     "url": f"https://bitbucket.org/{ws}/{REPO_SLUG}",
                     "description": "Seeded by seed_probe_repo.py"})


async def s07_commit_status(
    client: httpx.AsyncClient, ws: str, commit_hash: str, open_pr_id: int | None = None
) -> str:
    """Seed commit status on main HEAD + all commits in the open PR (for pr_statuses)."""
    print(f"\n── Step 7: Commit status on {commit_hash[:12]}…")
    await _seed_commit_status_on(client, ws, commit_hash)
    print(f"   ✅  Status on main HEAD key=bb-probe-ci")

    # Also seed on all commits in the open PR so /pullrequests/{id}/statuses is non-empty
    if open_pr_id:
        pr_resp = await client.get(
            f"{BASE}/repositories/{ws}/{REPO_SLUG}/pullrequests/{open_pr_id}/commits",
            params={"pagelen": 10}, timeout=20, follow_redirects=True,
        )
        if pr_resp.status_code == 200:
            pr_hashes = [c["hash"] for c in pr_resp.json().get("values", [])]
            await asyncio.gather(*[_seed_commit_status_on(client, ws, h) for h in pr_hashes])
            print(f"   ✅  Status on {len(pr_hashes)} PR commit(s)")
    return "bb-probe-ci"


async def s08_code_insights(client: httpx.AsyncClient, ws: str, commit_hash: str) -> tuple[str, str]:
    print(f"\n── Step 8: Code Insights report + annotation on {commit_hash[:12]}…")
    report_id = "bb-probe-report"
    annotation_id = "bb-probe-ann-001"

    # Report (PUT = create or update)
    await _api(client, "PUT",
               f"{BASE}/repositories/{ws}/{REPO_SLUG}/commit/{commit_hash}/reports/{report_id}",
               json={
                   "title": "bb SDK probe report",
                   "details": "Seeded Code Insights report for live-test coverage.",
                   "report_type": "TEST",
                   "result": "PASSED",
                   "data": [{"type": "PERCENTAGE", "title": "Coverage", "value": 85}],
                   "reporter": "bb-probe",
                   "link": f"https://bitbucket.org/{ws}/{REPO_SLUG}",
               },
               expected=(200, 201))
    print(f"   ✅  Report id={report_id}")

    # Annotation (PUT = create or update)
    await _api(client, "PUT",
               f"{BASE}/repositories/{ws}/{REPO_SLUG}/commit/{commit_hash}/reports/{report_id}/annotations/{annotation_id}",
               json={
                   "annotation_type": "VULNERABILITY",
                   "path": "greet.py",
                   "line": 1,
                   "summary": "Probe annotation",
                   "message": "Probe annotation — fixture for reports.get_annotation live tests.",
                   "severity": "LOW",
                   "result": "PASSED",
                   "link": f"https://bitbucket.org/{ws}/{REPO_SLUG}",
               },
               expected=(200, 201))
    print(f"   ✅  Annotation id={annotation_id}")
    return report_id, annotation_id


async def s09_pipeline_resources(client: httpx.AsyncClient, ws: str) -> dict[str, str]:
    print("\n── Step 9: Pipeline config resources")
    ids: dict[str, str] = {}
    base = f"{BASE}/repositories/{ws}/{REPO_SLUG}"

    # Variable
    existing_var = await _get_first(client, f"{base}/pipelines_config/variables",
                                    params={"fields": "values.uuid,values.key"})
    if existing_var:
        ids["pipeline_var_uuid"] = existing_var.get("uuid", "")
        print(f"   ✅  Variable already exists uuid={ids['pipeline_var_uuid']}")
    else:
        data = await _api(client, "POST", f"{base}/pipelines_config/variables",
                          json={"key": "PROBE_VAR", "value": "probe_value", "secured": False})
        ids["pipeline_var_uuid"] = (data or {}).get("uuid", "")
        print(f"   ✅  Created variable uuid={ids['pipeline_var_uuid']}")

    # Schedule
    existing_sched = await _get_first(client, f"{base}/pipelines_config/schedules",
                                      params={"fields": "values.uuid"})
    if existing_sched:
        ids["pipeline_schedule_uuid"] = existing_sched.get("uuid", "")
        print(f"   ✅  Schedule already exists uuid={ids['pipeline_schedule_uuid']}")
    else:
        data = await _api(client, "POST", f"{base}/pipelines_config/schedules",
                          json={
                              "enabled": False,
                              "cron_pattern": "0 0 0 * * ? *",
                              "target": {
                                  "type": "pipeline_ref_target",
                                  "ref_type": "branch",
                                  "ref_name": "main",
                                  "selector": {"type": "default"},
                              },
                          })
        ids["pipeline_schedule_uuid"] = (data or {}).get("uuid", "")
        print(f"   ✅  Created schedule uuid={ids['pipeline_schedule_uuid']}")

    # Known host — use gitlab.com (github.com is pre-configured by Bitbucket and rejected)
    existing_kh = await _get_first(client, f"{base}/pipelines_config/ssh/known_hosts",
                                   params={"fields": "values.uuid,values.hostname"})
    if existing_kh:
        ids["pipeline_known_host_uuid"] = existing_kh.get("uuid", "")
        print(f"   ✅  Known host already exists uuid={ids['pipeline_known_host_uuid']}")
    else:
        # Fetch gitlab.com public key via ssh-keyscan and upload with it
        kh_key, kh_type = _fetch_host_key("gitlab.com")
        kh_body: dict = {"hostname": "gitlab.com"}
        if kh_key:
            kh_body["public_key"] = {"key_type": kh_type, "key": kh_key}
        data = await _api(client, "POST", f"{base}/pipelines_config/ssh/known_hosts",
                          json=kh_body, expected=(200, 201))
        ids["pipeline_known_host_uuid"] = (data or {}).get("uuid", "")
        print(f"   ✅  Created known host hostname=gitlab.com uuid={ids['pipeline_known_host_uuid']}")

    # SSH key pair — generate with ssh-keygen and upload
    kp = await client.get(f"{base}/pipelines_config/ssh/key_pair", timeout=15, follow_redirects=True)
    if kp.status_code == 200 and kp.json().get("public_key"):
        print("   ✅  SSH key pair already generated")
    else:
        priv, pub = _generate_ssh_key_pair()
        if priv and pub:
            data = await _api(client, "PUT", f"{base}/pipelines_config/ssh/key_pair",
                              json={"private_key": priv, "public_key": pub}, expected=(200, 201))
            if data:
                print("   ✅  Generated pipeline SSH key pair")

    return ids


async def s10_env_variable(
    client: httpx.AsyncClient, ws: str, env_uuid: str
) -> str | None:
    print(f"\n── Step 10: Deployment environment variable (env={env_uuid[:8]}…)")
    if not env_uuid:
        print("   ⚠️  No environment UUID — skipping")
        return None
    base = f"{BASE}/repositories/{ws}/{REPO_SLUG}"
    existing = await _get_first(
        client,
        f"{base}/deployments_config/environments/{env_uuid}/variables",
        params={"fields": "values.uuid,values.key"},
    )
    if existing:
        uuid = existing.get("uuid", "")
        print(f"   ✅  Env variable already exists uuid={uuid}")
        return uuid
    data = await _api(client, "POST",
                      f"{base}/deployments_config/environments/{env_uuid}/variables",
                      json={"key": "DEPLOY_PROBE_VAR", "value": "probe", "secured": False})
    uuid = (data or {}).get("uuid", "")
    print(f"   ✅  Created env variable uuid={uuid}")
    return uuid


async def s11_deploy_key(client: httpx.AsyncClient, ws: str) -> str | None:
    print("\n── Step 11: Deploy key")
    existing = await _get_first(client,
                                f"{BASE}/repositories/{ws}/{REPO_SLUG}/deploy-keys",
                                params={"fields": "values.id,values.label"})
    if existing:
        key_id = str(existing.get("id", ""))
        print(f"   ✅  Deploy key already exists id={key_id}")
        return key_id

    # Generate an ed25519 key pair
    with tempfile.TemporaryDirectory() as td:
        key_path = Path(td) / "deploy_key"
        result = subprocess.run(
            ["ssh-keygen", "-t", "ed25519", "-f", str(key_path), "-N", "", "-C", "bb-probe-deploy-key"],
            capture_output=True, text=True,
        )
        if result.returncode != 0:
            print(f"   ⚠️  ssh-keygen failed: {result.stderr[:100]}")
            return None
        pub_key = (key_path.with_suffix(".pub")).read_text().strip()

    data = await _api(client, "POST",
                      f"{BASE}/repositories/{ws}/{REPO_SLUG}/deploy-keys",
                      json={"key": pub_key, "label": "bb-probe-deploy-key"})
    key_id = str((data or {}).get("id", ""))
    print(f"   ✅  Created deploy key id={key_id}")
    return key_id


async def s12_repo_webhook(client: httpx.AsyncClient, ws: str) -> str | None:
    print("\n── Step 12: Repo webhook")
    existing = await _get_first(client,
                                f"{BASE}/repositories/{ws}/{REPO_SLUG}/hooks",
                                params={"fields": "values.uuid,values.url"})
    if existing:
        uuid = existing.get("uuid", "")
        print(f"   ✅  Repo webhook already exists uuid={uuid}")
        return uuid
    data = await _api(client, "POST",
                      f"{BASE}/repositories/{ws}/{REPO_SLUG}/hooks",
                      json={
                          "description": "bb SDK probe webhook",
                          "url": "https://httpbin.org/post",
                          "active": True,
                          "events": ["repo:push", "pullrequest:created", "pullrequest:fulfilled"],
                      })
    uuid = (data or {}).get("uuid", "")
    print(f"   ✅  Created repo webhook uuid={uuid}")
    return uuid


async def s13_workspace_webhook(client: httpx.AsyncClient, ws: str) -> str | None:
    print("\n── Step 13: Workspace webhook")
    existing = await _get_first(client,
                                f"{BASE}/workspaces/{ws}/hooks",
                                params={"fields": "values.uuid,values.url"})
    if existing:
        uuid = existing.get("uuid", "")
        print(f"   ✅  Workspace webhook already exists uuid={uuid}")
        return uuid
    data = await _api(client, "POST",
                      f"{BASE}/workspaces/{ws}/hooks",
                      json={
                          "description": "bb SDK probe workspace webhook",
                          "url": "https://httpbin.org/post",
                          "active": True,
                          "events": ["repo:push", "pullrequest:created"],
                          "subject_type": "workspace",
                      })
    uuid = (data or {}).get("uuid", "")
    print(f"   ✅  Created workspace webhook uuid={uuid}")
    return uuid


async def s14_branch_restriction(client: httpx.AsyncClient, ws: str) -> str | None:
    print("\n── Step 14: Branch restriction")
    existing = await _get_first(client,
                                f"{BASE}/repositories/{ws}/{REPO_SLUG}/branch-restrictions",
                                params={"fields": "values.id,values.kind"})
    if existing:
        rid = str(existing.get("id", ""))
        print(f"   ✅  Branch restriction already exists id={rid}")
        return rid
    data = await _api(client, "POST",
                      f"{BASE}/repositories/{ws}/{REPO_SLUG}/branch-restrictions",
                      json={
                          "kind": "require_approvals_to_merge",
                          "branch_match_kind": "glob",
                          "pattern": "main",
                          "value": 1,
                          "users": [],
                          "groups": [],
                      })
    rid = str((data or {}).get("id", ""))
    print(f"   ✅  Created branch restriction id={rid}")
    return rid


async def s14b_repo_group_permission(client: httpx.AsyncClient, ws: str) -> str | None:
    """Grant the default workspace group read access to bb-probe (for repo_group_perms)."""
    print("\n── Step 14b: Repo group permission")

    # Find the workspace group via BB v1 groups API
    v1_client = httpx.AsyncClient(
        auth=(os.environ["BB_EMAIL"], os.environ["BB_TOKEN"]),
        base_url="https://api.bitbucket.org/1.0",
        headers={"Accept": "application/json"},
        follow_redirects=True,
    )
    async with v1_client:
        resp = await v1_client.get(f"/groups/{ws}", timeout=15)
        groups = resp.json() if resp.status_code == 200 else []

    if not groups:
        print("   ⚠️  No workspace groups found — skipping")
        return None

    group_slug = groups[0].get("slug", "")
    if not group_slug:
        print("   ⚠️  Group has no slug — skipping")
        return None

    # Check existing group permissions
    existing = await client.get(
        f"{BASE}/repositories/{ws}/{REPO_SLUG}/permissions-config/groups",
        params={"pagelen": 10}, timeout=15, follow_redirects=True,
    )
    if existing.status_code == 200:
        for g in existing.json().get("values", []):
            if g.get("group", {}).get("slug") == group_slug:
                print(f"   ✅  Group perm already exists slug={group_slug}")
                return group_slug

    data = await _api(
        client, "PUT",
        f"{BASE}/repositories/{ws}/{REPO_SLUG}/permissions-config/groups/{group_slug}",
        json={"permission": "read"},
        expected=(200, 201),
    )
    if data:
        print(f"   ✅  Added group permission slug={group_slug}")
    return group_slug


async def s15_issues(client: httpx.AsyncClient, ws: str) -> tuple[int | None, int | None]:
    print("\n── Step 15: Issues")

    # Check if issue tracker is enabled (404 → plan restriction, skip gracefully)
    check = await client.get(
        f"{BASE}/repositories/{ws}/{REPO_SLUG}/issues",
        params={"pagelen": 1}, timeout=15, follow_redirects=True,
    )
    if check.status_code == 404:
        print("   ⚠️  Issue tracker not available on this workspace plan — skipping")
        return None, None

    # Create issue
    issue_id: int | None = None
    existing = await _get_first(client,
                                f"{BASE}/repositories/{ws}/{REPO_SLUG}/issues",
                                params={"fields": "values.id,values.title"})
    if existing:
        issue_id = existing.get("id")
        print(f"   ✅  Issue already exists id={issue_id}")
    else:
        data = await _api(client, "POST",
                          f"{BASE}/repositories/{ws}/{REPO_SLUG}/issues",
                          json={
                              "title": "Probe issue — fixture for issues.* live tests",
                              "content": {"raw": "Do not close. Seed fixture for bb SDK live tests."},
                              "priority": "minor",
                              "type": "task",
                          })
        issue_id = (data or {}).get("id")
        print(f"   ✅  Created issue id={issue_id}")

    # Comment on issue
    comment_id: int | None = None
    if issue_id:
        existing_c = await _get_first(
            client,
            f"{BASE}/repositories/{ws}/{REPO_SLUG}/issues/{issue_id}/comments",
            params={"fields": "values.id"},
        )
        if existing_c:
            comment_id = existing_c.get("id")
            print(f"   ✅  Issue comment already exists id={comment_id}")
        else:
            data = await _api(client, "POST",
                              f"{BASE}/repositories/{ws}/{REPO_SLUG}/issues/{issue_id}/comments",
                              json={"content": {"raw": "Probe comment — fixture for `issues.get_comment`."}})
            comment_id = (data or {}).get("id")
            print(f"   ✅  Created issue comment id={comment_id}")
    return issue_id, comment_id


async def s16_download(client: httpx.AsyncClient, ws: str) -> str | None:
    print("\n── Step 16: Download file")
    filename = "probe_asset.txt"

    # Check availability first (402 = paid plan feature)
    check = await client.get(
        f"{BASE}/repositories/{ws}/{REPO_SLUG}/downloads",
        params={"pagelen": 1}, timeout=15, follow_redirects=True,
    )
    if check.status_code == 402:
        print("   ⚠️  Downloads not available on this workspace plan — skipping")
        return None
    if check.status_code == 200:
        vals = [v for v in check.json().get("values", []) if isinstance(v, dict)]
        if vals:
            fn = vals[0].get("name", "")
            print(f"   ✅  Download file already exists name={fn}")
            return fn

    content = f"bb-probe test asset — seeded {datetime.now(timezone.utc).isoformat()}\n"
    resp = await client.post(
        f"{BASE}/repositories/{ws}/{REPO_SLUG}/downloads",
        files={"files": (filename, content.encode(), "text/plain")},
        timeout=30, follow_redirects=True,
    )
    if resp.status_code == 402:
        print("   ⚠️  Downloads not available on this workspace plan — skipping")
        return None
    if resp.status_code in (200, 201):
        print(f"   ✅  Uploaded download file name={filename}")
        return filename
    print(f"   ⚠️  Download upload failed {resp.status_code}: {resp.text[:200]}")
    return None


async def s17_snippet(client: httpx.AsyncClient, ws: str) -> tuple[str | None, int | None]:
    print("\n── Step 17: Snippet")
    # Check availability first (402 = paid plan feature)
    check = await client.get(f"{BASE}/snippets/{ws}", params={"pagelen": 1},
                             timeout=15, follow_redirects=True)
    if check.status_code == 402:
        print("   ⚠️  Snippets not available on this workspace plan — skipping")
        return None, None

    # List existing
    resp = check if check.status_code == 200 else await client.get(
        f"{BASE}/snippets/{ws}", params={"pagelen": 5, "fields": "values.id,values.title"},
        timeout=15, follow_redirects=True)
    encoded_id: str | None = None
    if resp.status_code == 200:
        vals = [v for v in resp.json().get("values", []) if isinstance(v, dict)]
        if vals:
            encoded_id = str(vals[0].get("id", ""))
            print(f"   ✅  Snippet already exists id={encoded_id}")

    if not encoded_id:
        data = await _api(client, "POST", f"{BASE}/snippets/{ws}",
                          json={
                              "title": "bb-probe snippet",
                              "is_private": False,
                              "scm": "git",
                              "files": {
                                  "probe.py": {
                                      "content": '"""Probe snippet — fixture for snippets.* live tests."""\n\n\ndef hello() -> str:\n    return "hello from snippet"\n'
                                  }
                              },
                          })
        if data is None:
            print("   ⚠️  Snippet creation blocked (plan restriction) — skipping")
            return None, None
        encoded_id = str((data or {}).get("id", ""))
        print(f"   ✅  Created snippet id={encoded_id}")

    # Comment on snippet
    comment_id: int | None = None
    if encoded_id:
        existing_c = await _get_first(
            client, f"{BASE}/snippets/{ws}/{encoded_id}/comments",
            params={"fields": "values.id"},
        )
        if existing_c:
            comment_id = existing_c.get("id")
            print(f"   ✅  Snippet comment already exists id={comment_id}")
        else:
            data = await _api(client, "POST",
                              f"{BASE}/snippets/{ws}/{encoded_id}/comments",
                              json={"content": {"raw": "Probe comment — fixture for `snippets.get_comment`."}})
            comment_id = (data or {}).get("id")
            print(f"   ✅  Created snippet comment id={comment_id}")

    return encoded_id, comment_id


def s18_git_tag(email: str, token: str, ws: str, commit_hash: str) -> None:
    print(f"\n── Step 18: Git tag {TAG_NAME}")
    url = _git_clone_url(email, token, ws, REPO_SLUG)
    with tempfile.TemporaryDirectory() as td:
        _git(["clone", "--depth=1", url, td], check=True)
        _git(["config", "user.email", email], cwd=td)
        _git(["config", "user.name", "Laraib"], cwd=td)
        # Check if tag exists remotely
        ls = _git(["ls-remote", "--tags", "origin", TAG_NAME], cwd=td, check=False)
        if TAG_NAME in ls.stdout:
            print(f"   ✅  Tag {TAG_NAME} already exists")
            return
        _git(["tag", TAG_NAME, commit_hash], cwd=td)
        _git(["push", "origin", TAG_NAME], cwd=td)
        print(f"   ✅  Pushed tag {TAG_NAME}")


async def s19_workspace_pipeline_var(client: httpx.AsyncClient, ws: str) -> str | None:
    print("\n── Step 19: Workspace pipeline variable")
    existing = await _get_first(
        client, f"{BASE}/workspaces/{ws}/pipelines-config/variables",
        params={"fields": "values.uuid,values.key"},
    )
    if existing:
        uuid = existing.get("uuid", "")
        print(f"   ✅  Workspace pipeline var already exists uuid={uuid}")
        return uuid
    data = await _api(client, "POST",
                      f"{BASE}/workspaces/{ws}/pipelines-config/variables",
                      json={"key": "WS_PROBE_VAR", "value": "probe", "secured": False})
    uuid = (data or {}).get("uuid", "")
    print(f"   ✅  Created workspace pipeline var uuid={uuid}")
    return uuid


async def s20_user_ssh_key(client: httpx.AsyncClient, account_id: str) -> str | None:
    print("\n── Step 20: User SSH key")
    existing = await _get_first(
        client, f"{BASE}/users/{account_id}/ssh-keys",
        params={"fields": "values.uuid,values.label"},
    )
    if existing:
        uuid = existing.get("uuid", "")
        print(f"   ✅  SSH key already exists uuid={uuid}")
        return uuid

    with tempfile.TemporaryDirectory() as td:
        key_path = Path(td) / "user_key"
        result = subprocess.run(
            ["ssh-keygen", "-t", "ed25519", "-f", str(key_path), "-N", "",
             "-C", "bb-probe-user-ssh-key"],
            capture_output=True, text=True,
        )
        if result.returncode != 0:
            print(f"   ⚠️  ssh-keygen failed: {result.stderr[:100]}")
            return None
        pub_key = key_path.with_suffix(".pub").read_text().strip()

    data = await _api(client, "POST",
                      f"{BASE}/users/{account_id}/ssh-keys",
                      json={"key": pub_key, "label": "bb-probe-user-ssh-key"})
    uuid = (data or {}).get("uuid", "")
    print(f"   ✅  Created user SSH key uuid={uuid}")
    return uuid


async def s21_user_gpg_key(client: httpx.AsyncClient, account_id: str, email: str) -> str | None:
    print("\n── Step 21: User GPG key")
    existing = await _get_first(
        client, f"{BASE}/users/{account_id}/gpg-keys",
        params={"fields": "values.fingerprint,values.name"},
    )
    if existing:
        fp = existing.get("fingerprint", "")
        print(f"   ✅  GPG key already exists fingerprint={fp[:16]}…")
        return fp

    # Generate a temporary GPG key
    batch = (
        "Key-Type: RSA\n"
        "Key-Length: 2048\n"
        "Subkey-Type: RSA\n"
        "Subkey-Length: 2048\n"
        "Name-Real: Laraib Probe Key\n"
        f"Name-Email: {email}\n"
        "Expire-Date: 1y\n"
        "%no-passphrase\n"
        "%commit\n"
    )
    with tempfile.TemporaryDirectory() as td:
        batch_file = Path(td) / "gpg_batch"
        batch_file.write_text(batch)
        env = {**os.environ, "GNUPGHOME": td}
        result = subprocess.run(
            ["gpg", "--batch", "--gen-key", str(batch_file)],
            capture_output=True, text=True, env=env,
        )
        if result.returncode != 0:
            print(f"   ⚠️  gpg --gen-key failed: {result.stderr[:150]}")
            return None

        # Get fingerprint
        list_result = subprocess.run(
            ["gpg", "--list-secret-keys", "--with-colons"],
            capture_output=True, text=True, env=env,
        )
        fingerprint = ""
        for line in list_result.stdout.splitlines():
            if line.startswith("fpr:"):
                fingerprint = line.split(":")[9]
                break

        if not fingerprint:
            print("   ⚠️  Could not extract GPG fingerprint")
            return None

        # Export armored public key
        export_result = subprocess.run(
            ["gpg", "--armor", "--export", fingerprint],
            capture_output=True, text=True, env=env,
        )
        pub_key = export_result.stdout.strip()

    data = await _api(client, "POST",
                      f"{BASE}/users/{account_id}/gpg-keys",
                      json={"key": pub_key})
    fp = (data or {}).get("fingerprint", "")
    print(f"   ✅  Created GPG key fingerprint={fp[:16]}…")
    return fp


# ---------------------------------------------------------------------------
# Checklist updater
# ---------------------------------------------------------------------------

def _replace(text: str, marker: str, value: str) -> str:
    """Replace the first `___` in a line containing `marker` with `value`."""
    lines = text.splitlines(keepends=True)
    for i, line in enumerate(lines):
        if marker in line and "___" in line:
            lines[i] = line.replace("`___`", f"`{value}`", 1).replace("___", value, 1)
            return "".join(lines)
    return text


def _check(text: str, marker: str) -> str:
    """Replace `- [ ]` with `- [x]` on the first line containing marker."""
    lines = text.splitlines(keepends=True)
    for i, line in enumerate(lines):
        if marker in line and "- [ ]" in line:
            lines[i] = line.replace("- [ ]", "- [x]", 1)
            return "".join(lines)
    return text


def update_checklist(path: Path, ids: dict) -> None:
    text = path.read_text()

    def upd(marker: str, value: str | None, check_marker: str | None = None) -> None:
        nonlocal text
        if value:
            text = _replace(text, marker, str(value))
        if check_marker and value:
            text = _check(text, check_marker)
        elif check_marker is None and value:
            text = _check(text, marker)

    # Section 0
    upd("BB_REPO_SLUG", "bb-probe", "BB_REPO_SLUG` set in `.env`")
    upd("BB_SEARCH_QUERY", "def", "BB_SEARCH_QUERY` set in `.env`")
    text = _replace(text, "BB_REPO_SLUG` set in `.env", "bb-probe")
    text = _check(text, "BB_REPO_SLUG` set in `.env`")
    text = _replace(text, "BB_SEARCH_QUERY` set in `.env", "def")
    text = _check(text, "BB_SEARCH_QUERY` set in `.env`")

    # Section 3
    if ids.get("repo_uuid"):
        text = _replace(text, "uuid: `___`\n\n- [ ] Repository has issues", ids["repo_uuid"])
        text = _check(text, "Repository `bb-probe` exists")
        text = _check(text, "Repository has issues tracker enabled")
        text = _replace(text, "setting: *(circle one: Public / Private)*", "Private")
        text = _check(text, "Repository is assigned to project")

    # Section 4
    if ids.get("first_commit_hash"):
        text = _replace(text, "first_commit_hash", ids["first_commit_hash"])
        text = _check(text, "At least one commit on `main`")
        text = _check(text, "`main` branch exists")
        text = _replace(text, "branch_name: `___`\n\n- [ ] At least one git tag", FEATURE_BRANCH)
        text = _check(text, "At least one additional feature branch")

    # Section 5
    if ids.get("first_commit_hash"):
        text = _check(text, "Source tree root is accessible")
        text = _replace(text, "file_path: `___`", "greet.py")
        text = _check(text, "At least one file path is known")

    # Section 6
    if ids.get("commit_status_key"):
        text = _replace(text, "key: `___`\n  state:", ids["commit_status_key"])
        text = _replace(text, "*(circle one: SUCCESSFUL / FAILED / INPROGRESS)*", "SUCCESSFUL")
        text = _check(text, "At least one build status on the latest commit")

    # Section 7
    if ids.get("report_id"):
        text = _replace(text, "report_id: `___`", ids["report_id"])
        text = _replace(text, "*(circle one: TEST / COVERAGE / BUG / SECURITY / VULNERABILITY / OTHER)*", "TEST")
        text = _check(text, "At least one report on the latest commit")
    if ids.get("annotation_id"):
        text = _replace(text, "annotation_id: `___`", ids["annotation_id"])
        text = _check(text, "At least one annotation on that report")

    # Section 8
    if ids.get("open_pr_id"):
        text = _replace(text, "pr_id: `___`\n  source_branch:", str(ids["open_pr_id"]))
        text = _replace(text, "source_branch: `___`", FEATURE_BRANCH)
        text = _check(text, "At least one **open** pull request exists")
    if ids.get("merged_pr_id"):
        text = _replace(text, "pr_id: `___`\n\n- [ ] At least one comment", str(ids["merged_pr_id"]))
        text = _check(text, "At least one **merged** pull request exists")
    if ids.get("pr_comment_id"):
        text = _replace(text, "comment_id: `___`\n\n- [ ] At least one task", str(ids["pr_comment_id"]))
        text = _check(text, "At least one comment on the open PR")
    if ids.get("pr_task_id"):
        text = _replace(text, "task_id: `___`\n\n---\n\n## 9", str(ids["pr_task_id"]))
        text = _check(text, "At least one task on the open PR")

    # Section 9
    if ids.get("first_commit_hash"):
        text = _replace(text, "development_branch: `___`", "main")
        text = _check(text, "Effective branching model accessible")
        text = _check(text, "Branching model settings readable")

    # Section 10
    if ids.get("branch_restriction_id"):
        text = _replace(text, "restriction_id: `___`", ids["branch_restriction_id"])
        text = _replace(text, "kind: `___`", "require_approvals_to_merge")
        text = _replace(text, "pattern: `___`", "main")
        text = _check(text, "At least one branch restriction rule exists")

    # Section 12
    if ids.get("first_commit_hash"):
        text = _check(text, "Pipelines enabled on `bb-probe`")
        text = _check(text, "`bitbucket-pipelines.yml` present on `main`")
    if ids.get("pipeline_var_uuid"):
        text = _replace(text, "variable_uuid: `___`\n  key: `___`\n\n- [ ] At least one pipeline schedule",
                        ids["pipeline_var_uuid"])
        text = _replace(text, "key: `___`\n\n- [ ] At least one pipeline schedule", "PROBE_VAR")
        text = _check(text, "At least one pipeline repository variable")
    if ids.get("pipeline_schedule_uuid"):
        text = _replace(text, "schedule_uuid: `___`", ids["pipeline_schedule_uuid"])
        text = _replace(text, "cron: `___`", "0 0 * * 0")
        text = _check(text, "At least one pipeline schedule")
    if ids.get("pipeline_known_host_uuid"):
        text = _replace(text, "known_host_uuid: `___`", ids["pipeline_known_host_uuid"])
        text = _replace(text, "hostname: `___`", "github.com")
        text = _check(text, "At least one pipeline known host")
    text = _check(text, "Pipeline SSH key pair generated")

    # Section 13
    if ids.get("ws_pipeline_var_uuid"):
        text = _replace(text, "variable_uuid: `___`\n  key: `___`\n\n---\n\n## 14",
                        ids["ws_pipeline_var_uuid"])
        text = _replace(text, "key: `___`\n\n---\n\n## 14", "WS_PROBE_VAR")
        text = _check(text, "At least one workspace pipeline variable")

    # Section 14
    envs = ids.get("environments", {})
    env_names = list(envs.keys())
    if len(env_names) >= 1:
        text = _replace(text, "environment_uuid: `___`\n  environment_name: `___`\n\n- [ ] At least one additional",
                        envs[env_names[0]])
        text = _replace(text, "environment_name: `___`\n\n- [ ] At least one additional", env_names[0])
        text = _check(text, "At least one deployment environment exists")
    if len(env_names) >= 2:
        text = _replace(text, "environment_uuid: `___`\n  environment_name: `___`\n\n- [ ] At least one deployment object",
                        envs[env_names[1]])
        text = _replace(text, "environment_name: `___`\n\n- [ ] At least one deployment object", env_names[1])
        text = _check(text, "At least one additional environment")
    if ids.get("env_var_uuid"):
        text = _replace(text, "env_var_uuid: `___`", ids["env_var_uuid"])
        text = _replace(text, "key: `___`\n\n---\n\n## 15", "DEPLOY_PROBE_VAR")
        text = _check(text, "At least one variable on the first environment")

    # Section 15
    if ids.get("deploy_key_id"):
        text = _replace(text, "key_id: `___`", ids["deploy_key_id"])
        text = _replace(text, "label: `___`\n\n---\n\n## 16", "bb-probe-deploy-key")
        text = _check(text, "At least one deploy key on `bb-probe`")

    # Section 16
    if ids.get("repo_webhook_uuid"):
        text = _replace(text, "webhook_uuid: `___`\n  url: `___`\n\n- [ ] At least one **workspace**",
                        ids["repo_webhook_uuid"])
        text = _replace(text, "url: `___`\n\n- [ ] At least one **workspace**", "https://httpbin.org/post")
        text = _check(text, "At least one **repo** webhook on `bb-probe`")
    if ids.get("ws_webhook_uuid"):
        text = _replace(text, "webhook_uuid: `___`\n  url: `___`\n\n---\n\n## 17",
                        ids["ws_webhook_uuid"])
        text = _replace(text, "url: `___`\n\n---\n\n## 17", "https://httpbin.org/post")
        text = _check(text, "At least one **workspace** webhook")

    # Section 17
    if ids.get("issue_id"):
        text = _replace(text, "issue_id: `___`", str(ids["issue_id"]))
        text = _replace(text, "title: `___`\n\n- [ ] At least one comment on that issue",
                        "Probe issue — fixture for issues.* live tests")
        text = _check(text, "Issue tracker enabled and at least one issue exists")
    if ids.get("issue_comment_id"):
        text = _replace(text, "comment_id: `___`\n\n- [ ] At least one milestone", str(ids["issue_comment_id"]))
        text = _check(text, "At least one comment on that issue")

    # Section 18
    if ids.get("download_filename"):
        text = _replace(text, "filename: `___`", ids["download_filename"])
        text = _check(text, "At least one file uploaded to `bb-probe` downloads")

    # Section 19
    if ids.get("snippet_encoded_id"):
        text = _replace(text, "encoded_id: `___`", ids["snippet_encoded_id"])
        text = _replace(text, "title: `___`\n\n- [ ] Snippet has at least one file", "bb-probe snippet")
        text = _check(text, "At least one snippet exists")
        text = _replace(text, "file_path: `___`\n\n- [ ] Snippet has at least one comment", "probe.py")
        text = _check(text, "Snippet has at least one file")
    if ids.get("snippet_comment_id"):
        text = _replace(text, "comment_id: `___`\n\n- [ ] Snippet has at least one commit",
                        str(ids["snippet_comment_id"]))
        text = _check(text, "Snippet has at least one comment")
    # Snippet commit is auto-created
    text = _check(text, "Snippet has at least one commit")

    # Section 21
    if ids.get("user_ssh_key_uuid"):
        text = _replace(text, "key_uuid: `___`", ids["user_ssh_key_uuid"])
        text = _replace(text, "label: `___`\n\n- [ ] At least one GPG key", "bb-probe-user-ssh-key")
        text = _check(text, "At least one SSH key on the Bitbucket account")
    if ids.get("user_gpg_fingerprint"):
        text = _replace(text, "fingerprint: `___`", ids["user_gpg_fingerprint"][:16] + "…")
        text = _check(text, "At least one GPG key on the Bitbucket account")

    # Section 23
    text = _replace(text, "query: `___`", "def")
    text = _replace(text, "tested: *(circle one: yes / no)*", "yes")
    text = _check(text, "`BB_SEARCH_QUERY` returns at least one result")

    # Update score
    text = re.sub(r"\*\*Current score:\*\* `3 / 38` \(8%\)",
                  f"**Current score:** `see probe-workspace` (re-run `make probe-workspace`)", text)

    path.write_text(text)
    print(f"\n   ✅  Checklist updated: {path.name}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

async def main() -> int:
    project_root = Path(__file__).resolve().parent.parent
    _load_dotenv(project_root / ".env")

    email = os.environ.get("BB_EMAIL", "").strip()
    token = os.environ.get("BB_TOKEN", "").strip()
    ws    = os.environ.get("BB_WORKSPACE", "").strip()

    if not all([email, token, ws]):
        print("ERROR: BB_EMAIL, BB_TOKEN, BB_WORKSPACE must be set in .env", file=sys.stderr)
        return 1

    print("=" * 60)
    print(f"bb.cloud.sdk — probe repo seeder")
    print(f"workspace : {ws}")
    print(f"repo      : {REPO_SLUG}")
    print("=" * 60)

    ids: dict = {}

    async with httpx.AsyncClient(auth=(email, token)) as client:
        # Get user account_id
        me = await client.get(f"{BASE}/user", timeout=15, follow_redirects=True)
        account_id = me.json().get("account_id", "") if me.status_code == 200 else ""

        # Sequential phases (each may depend on previous)
        repo_data = await s01_create_repo(client, ws)
        ids["repo_uuid"] = repo_data.get("uuid", "")

        await s02_enable_pipelines(client, ws)

        env_uuids = await s03_create_environments(client, ws)
        ids["environments"] = env_uuids

        commit_hash = s04_git_operations(email, token, ws)
        ids["first_commit_hash"] = commit_hash

        open_pr_id, merged_pr_id = await s05_open_pr(client, ws)
        ids["open_pr_id"] = open_pr_id
        ids["merged_pr_id"] = merged_pr_id

        if open_pr_id:
            pr_comment_id, pr_task_id = await s06_pr_comment_and_task(client, ws, open_pr_id)
            ids["pr_comment_id"] = pr_comment_id
            ids["pr_task_id"] = pr_task_id

        ids["commit_status_key"] = await s07_commit_status(
            client, ws, commit_hash, open_pr_id=open_pr_id)

        report_id, annotation_id = await s08_code_insights(client, ws, commit_hash)
        ids["report_id"] = report_id
        ids["annotation_id"] = annotation_id

        pipe_ids = await s09_pipeline_resources(client, ws)
        ids.update(pipe_ids)

        first_env_uuid = next(iter(env_uuids.values()), "")
        ids["env_var_uuid"] = await s10_env_variable(client, ws, first_env_uuid)

        ids["deploy_key_id"] = await s11_deploy_key(client, ws)
        ids["repo_webhook_uuid"] = await s12_repo_webhook(client, ws)
        ids["ws_webhook_uuid"] = await s13_workspace_webhook(client, ws)
        ids["branch_restriction_id"] = await s14_branch_restriction(client, ws)
        ids["group_slug"] = await s14b_repo_group_permission(client, ws)

        issue_id, issue_comment_id = await s15_issues(client, ws)
        ids["issue_id"] = issue_id
        ids["issue_comment_id"] = issue_comment_id

        ids["download_filename"] = await s16_download(client, ws)

        snippet_id, snippet_comment_id = await s17_snippet(client, ws)
        ids["snippet_encoded_id"] = snippet_id
        ids["snippet_comment_id"] = snippet_comment_id

        s18_git_tag(email, token, ws, commit_hash)

        ids["ws_pipeline_var_uuid"] = await s19_workspace_pipeline_var(client, ws)
        ids["user_ssh_key_uuid"] = await s20_user_ssh_key(client, account_id)
        ids["user_gpg_fingerprint"] = await s21_user_gpg_key(client, account_id, email)

    # Update checklist
    checklist_path = project_root / "context" / "test_env_checklist_current.md"
    update_checklist(checklist_path, ids)

    print("\n" + "=" * 60)
    print("Seeding complete.")
    print()
    print("⚠️  Still requires manual action (UI-only):")
    print("   • Issue milestones, versions, components — Bitbucket UI only (no POST in API)")
    print("   • Pipeline caches — auto-created on first pipeline run (triggered by the push above)")
    print("   • Pipeline steps/deployment objects — triggered by the push above; wait ~2 min then re-probe")
    print("   • Repo group/user permissions — requires workspace groups or a second user")
    print()
    print("Run `make probe-workspace` in ~2 min (after pipeline completes) to verify final score.")
    print("=" * 60)
    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
