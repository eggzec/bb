#!/usr/bin/env python3
"""Comprehensive async probe of the Bitbucket Cloud workspace.

Covers every resource category needed to exercise all ~407 public functions
across the full bb.cloud.sdk surface — not just existing live tests.

Checks: repos, branches, tags, commits, commit-statuses, commit-reports
(Code Insights), pull requests, PR comments, PR tasks, PR statuses,
pipelines, pipeline steps, pipeline logs, pipeline variables, pipeline
schedules, pipeline known-hosts, pipeline SSH key pair, pipeline caches,
pipeline workspace-variables, deployments, deployment environments,
deployment env-variables, deploy keys, branch restrictions, default
reviewers, branching model, source tree, issues, issue comments,
issue changes, issue milestones, issue versions, issue components,
downloads, webhooks (repo + workspace), snippets, snippet comments,
snippet commits, users, user SSH keys, user GPG keys, workspace members,
repo permissions (group + user), properties (Connect — untestable note),
addon (Connect — untestable note), search.

Outputs:
  cmd_outputs/<ts>_probe_workspace.json   — machine-readable
  cmd_outputs/<ts>_probe_workspace.md     — human-readable strategy doc

Usage:
    uv run python3 scripts/probe_workspace.py
    make probe-workspace
"""
from __future__ import annotations

import argparse
import asyncio
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import httpx

# ---------------------------------------------------------------------------
# Env loader
# ---------------------------------------------------------------------------

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
# Async HTTP helpers
# ---------------------------------------------------------------------------

BASE = "https://api.bitbucket.org/2.0"


async def _get(
    client: httpx.AsyncClient,
    url: str,
    *,
    params: dict | None = None,
) -> dict | None:
    try:
        resp = await client.get(url, params=params or {}, timeout=20, follow_redirects=True)
        if resp.status_code in (404, 403, 401):
            return None
        resp.raise_for_status()
        ct = resp.headers.get("content-type", "")
        if "json" not in ct:
            return {"_raw": resp.text[:200]}
        return resp.json()
    except Exception as exc:
        return {"_error": str(exc), "_url": url}


async def _first(
    client: httpx.AsyncClient,
    url: str,
    *,
    params: dict | None = None,
    page_size: int = 3,
) -> list[dict]:
    p = dict(params or {})
    p["pagelen"] = page_size
    data = await _get(client, url, params=p)
    if not data or "_error" in data or "_raw" in data:
        return []
    vals = data.get("values", [])
    return [v for v in vals if isinstance(v, dict)]


def _ok(lst: list) -> bool:
    return bool(lst)


def _id0(lst: list, key: str) -> str | None:
    return lst[0].get(key) if lst else None


# ---------------------------------------------------------------------------
# Tier-1 probes (workspace-level)
# ---------------------------------------------------------------------------

async def probe_user(client: httpx.AsyncClient) -> dict:
    data = await _get(client, f"{BASE}/user")
    if not data or "_error" in data:
        return {"ok": False}
    return {
        "ok": True,
        "account_id": data.get("account_id"),
        "display_name": data.get("display_name"),
        "nickname": data.get("nickname"),
        "uuid": data.get("uuid"),
    }


async def probe_workspace(client: httpx.AsyncClient, workspace: str) -> dict:
    data = await _get(client, f"{BASE}/workspaces/{workspace}")
    if not data or "_error" in data:
        return {"ok": False}
    return {
        "ok": True,
        "slug": data.get("slug"),
        "name": data.get("name"),
        "uuid": data.get("uuid"),
    }


async def probe_repos(client: httpx.AsyncClient, workspace: str) -> list[dict]:
    data = await _get(client, f"{BASE}/repositories/{workspace}",
        params={"pagelen": 25, "fields": "values.slug,values.full_name,values.scm,values.size,values.language,values.has_issues,size"})
    if not data or "_error" in data:
        return []
    return [v for v in data.get("values", []) if isinstance(v, dict)]


async def probe_projects(client: httpx.AsyncClient, workspace: str) -> list[dict]:
    return await _first(client, f"{BASE}/workspaces/{workspace}/projects",
        params={"fields": "values.key,values.name,values.uuid"}, page_size=10)


async def probe_snippets_workspace(client: httpx.AsyncClient, workspace: str) -> dict:
    data = await _get(client, f"{BASE}/snippets/{workspace}",
        params={"pagelen": 5, "fields": "values.id,values.title,values.scm,size"})
    if not data or "_error" in data:
        return {"ok": False, "count": 0, "samples": []}
    vals = [v for v in data.get("values", []) if isinstance(v, dict)]
    return {
        "ok": bool(vals),
        "count": data.get("size", len(vals)),
        "samples": [{"id": v.get("id"), "title": v.get("title")} for v in vals[:5]],
    }


async def probe_workspace_members(client: httpx.AsyncClient, workspace: str) -> dict:
    items = await _first(client, f"{BASE}/workspaces/{workspace}/members",
        params={"fields": "values.account_id,values.display_name"})
    return {"ok": _ok(items), "count": len(items),
            "account_ids": [i.get("account_id") for i in items]}


async def probe_workspace_webhooks(client: httpx.AsyncClient, workspace: str) -> dict:
    items = await _first(client, f"{BASE}/workspaces/{workspace}/hooks",
        params={"fields": "values.uuid,values.url"})
    return {"ok": _ok(items), "count": len(items),
            "uuids": [i.get("uuid") for i in items]}


async def probe_workspace_pipeline_vars(client: httpx.AsyncClient, workspace: str) -> dict:
    items = await _first(client, f"{BASE}/workspaces/{workspace}/pipelines-config/variables",
        params={"fields": "values.uuid,values.key"})
    return {"ok": _ok(items), "count": len(items),
            "uuids": [i.get("uuid") for i in items]}


async def probe_user_ssh_keys(client: httpx.AsyncClient, account_id: str) -> dict:
    if not account_id:
        return {"ok": False, "count": 0}
    items = await _first(client, f"{BASE}/users/{account_id}/ssh-keys",
        params={"fields": "values.uuid,values.label"})
    return {"ok": _ok(items), "count": len(items),
            "uuids": [i.get("uuid") for i in items]}


async def probe_user_gpg_keys(client: httpx.AsyncClient, account_id: str) -> dict:
    if not account_id:
        return {"ok": False, "count": 0}
    items = await _first(client, f"{BASE}/users/{account_id}/gpg-keys",
        params={"fields": "values.fingerprint,values.name"})
    return {"ok": _ok(items), "count": len(items),
            "fingerprints": [i.get("fingerprint") for i in items]}


# ---------------------------------------------------------------------------
# Tier-2 probes (repo-scoped base resources)
# ---------------------------------------------------------------------------

async def _probe_repo_base(client: httpx.AsyncClient, ws: str, slug: str) -> dict:
    """Probe all base-level repo resources concurrently."""
    (
        commits_r, branches_r, tags_r,
        hooks_r, issues_r, downloads_r,
        pipelines_r, envs_r, deployments_r,
        branch_restr_r, deploy_keys_r, defrev_r,
        pipeline_vars_r, pipeline_schedules_r,
        pipeline_known_hosts_r,
        source_root, branching_model,
        pipeline_config, override_settings,
        repo_group_perms_r, repo_user_perms_r,
    ) = await asyncio.gather(
        _first(client, f"{BASE}/repositories/{ws}/{slug}/commits",
               params={"fields": "values.hash,values.author.user.account_id,values.message"}),
        _first(client, f"{BASE}/repositories/{ws}/{slug}/refs/branches",
               params={"fields": "values.name,values.target.hash"}),
        _first(client, f"{BASE}/repositories/{ws}/{slug}/refs/tags",
               params={"fields": "values.name,values.target.hash"}),
        _first(client, f"{BASE}/repositories/{ws}/{slug}/hooks",
               params={"fields": "values.uuid,values.url,values.active"}),
        _first(client, f"{BASE}/repositories/{ws}/{slug}/issues",
               params={"fields": "values.id,values.title,values.status"}),
        _first(client, f"{BASE}/repositories/{ws}/{slug}/downloads",
               params={"fields": "values.name,values.size"}),
        _first(client, f"{BASE}/repositories/{ws}/{slug}/pipelines",
               params={"sort": "-created_on", "fields": "values.uuid,values.state,values.trigger"}),
        _first(client, f"{BASE}/repositories/{ws}/{slug}/environments",
               params={"fields": "values.uuid,values.name,values.type.name"}),
        _first(client, f"{BASE}/repositories/{ws}/{slug}/deployments",
               params={"fields": "values.uuid,values.state.name,values.environment.uuid"}),
        _first(client, f"{BASE}/repositories/{ws}/{slug}/branch-restrictions",
               params={"fields": "values.id,values.kind,values.branch_match_kind"}),
        _first(client, f"{BASE}/repositories/{ws}/{slug}/deploy-keys",
               params={"fields": "values.id,values.label"}),
        _first(client, f"{BASE}/repositories/{ws}/{slug}/default-reviewers",
               params={"fields": "values.account_id,values.display_name"}),
        _first(client, f"{BASE}/repositories/{ws}/{slug}/pipelines_config/variables",
               params={"fields": "values.uuid,values.key"}),
        _first(client, f"{BASE}/repositories/{ws}/{slug}/pipelines_config/schedules",
               params={"fields": "values.uuid,values.enabled,values.cron_pattern"}),
        _first(client, f"{BASE}/repositories/{ws}/{slug}/pipelines_config/ssh/known_hosts",
               params={"fields": "values.uuid,values.hostname"}),
        _get(client, f"{BASE}/repositories/{ws}/{slug}/src"),
        _get(client, f"{BASE}/repositories/{ws}/{slug}/effective-branching-model"),
        _get(client, f"{BASE}/repositories/{ws}/{slug}/pipelines_config"),
        _get(client, f"{BASE}/repositories/{ws}/{slug}/override-settings"),
        _first(client, f"{BASE}/repositories/{ws}/{slug}/permissions-config/groups",
               params={"fields": "values.group.slug,values.permission"}),
        _first(client, f"{BASE}/repositories/{ws}/{slug}/permissions-config/users",
               params={"fields": "values.user.account_id,values.permission"}),
    )
    return {
        "commits": commits_r,
        "branches": branches_r,
        "tags": tags_r,
        "hooks": hooks_r,
        "issues": issues_r,
        "downloads": downloads_r,
        "pipelines": pipelines_r,
        "environments": envs_r,
        "deployments": deployments_r,
        "branch_restrictions": branch_restr_r,
        "deploy_keys": deploy_keys_r,
        "default_reviewers": defrev_r,
        "pipeline_vars": pipeline_vars_r,
        "pipeline_schedules": pipeline_schedules_r,
        "pipeline_known_hosts": pipeline_known_hosts_r,
        "source_root": source_root,
        "branching_model": branching_model,
        "pipeline_config": pipeline_config,
        "override_settings": override_settings,
        "repo_group_perms": repo_group_perms_r,
        "repo_user_perms": repo_user_perms_r,
    }


# ---------------------------------------------------------------------------
# Tier-3 probes (sub-resources requiring IDs from tier-2)
# ---------------------------------------------------------------------------

async def _probe_repo_sub(client: httpx.AsyncClient, ws: str, slug: str, base: dict) -> dict:
    """Probe sub-resources that depend on IDs discovered in tier-2."""
    sub: dict[str, Any] = {}

    # --- Commits ---
    first_commit = _id0(base["commits"], "hash")
    sub["first_commit_hash"] = first_commit

    commit_statuses, commit_reports = [], []
    if first_commit:
        commit_statuses, commit_reports = await asyncio.gather(
            _first(client, f"{BASE}/repositories/{ws}/{slug}/commit/{first_commit}/statuses",
                   params={"fields": "values.key,values.state,values.name"}),
            _first(client, f"{BASE}/repositories/{ws}/{slug}/commit/{first_commit}/reports",
                   params={"fields": "values.uuid,values.title,values.report_type"}),
        )
    sub["commit_statuses"] = commit_statuses
    sub["commit_reports"] = commit_reports

    # Commit report annotations
    first_report_id = _id0(commit_reports, "uuid")
    sub["first_report_id"] = first_report_id
    report_annotations = []
    if first_commit and first_report_id:
        report_annotations = await _first(
            client,
            f"{BASE}/repositories/{ws}/{slug}/commit/{first_commit}/reports/{first_report_id}/annotations",
            params={"fields": "values.uuid,values.annotation_type"})
    sub["report_annotations"] = report_annotations

    # Source path (get a real file from the root)
    source_file_path: str | None = None
    if base.get("source_root") and isinstance(base["source_root"], dict):
        vals = base["source_root"].get("values", [])
        for v in vals:
            if isinstance(v, dict) and v.get("type") == "commit_file":
                source_file_path = v.get("path")
                break
    sub["source_file_path"] = source_file_path

    # --- Pull requests ---
    prs_open, prs_merged, prs_declined = await asyncio.gather(
        _first(client, f"{BASE}/repositories/{ws}/{slug}/pullrequests",
               params={"state": "OPEN", "fields": "values.id,values.title,values.source.branch.name,values.destination.branch.name"}),
        _first(client, f"{BASE}/repositories/{ws}/{slug}/pullrequests",
               params={"state": "MERGED", "fields": "values.id,values.title"}),
        _first(client, f"{BASE}/repositories/{ws}/{slug}/pullrequests",
               params={"state": "DECLINED", "fields": "values.id,values.title"}),
    )
    sub["prs_open"] = prs_open
    sub["prs_merged"] = prs_merged
    sub["prs_declined"] = prs_declined

    first_pr_id: int | None = None
    for prl in (prs_open, prs_merged, prs_declined):
        if prl and prl[0].get("id") is not None:
            first_pr_id = prl[0]["id"]
            break
    sub["first_pr_id"] = first_pr_id

    pr_comments, pr_tasks, pr_statuses, pr_activity = [], [], [], []
    if first_pr_id is not None:
        pr_comments, pr_tasks, pr_statuses, pr_activity = await asyncio.gather(
            _first(client, f"{BASE}/repositories/{ws}/{slug}/pullrequests/{first_pr_id}/comments",
                   params={"fields": "values.id,values.content.raw"}),
            _first(client, f"{BASE}/repositories/{ws}/{slug}/pullrequests/{first_pr_id}/tasks",
                   params={"fields": "values.id,values.state,values.content.raw"}),
            _first(client, f"{BASE}/repositories/{ws}/{slug}/pullrequests/{first_pr_id}/statuses",
                   params={"fields": "values.key,values.state"}),
            _first(client, f"{BASE}/repositories/{ws}/{slug}/pullrequests/{first_pr_id}/activity",
                   params={"fields": "values.update"}),
        )
    sub["pr_comments"] = pr_comments
    sub["pr_tasks"] = pr_tasks
    sub["pr_statuses"] = pr_statuses
    sub["pr_activity"] = pr_activity
    sub["first_pr_comment_id"] = _id0(pr_comments, "id")
    sub["first_pr_task_id"] = _id0(pr_tasks, "id")

    # --- Pipelines ---
    first_pipeline_uuid = _id0(base["pipelines"], "uuid")
    sub["first_pipeline_uuid"] = first_pipeline_uuid

    pipeline_steps, pipeline_ssh_key_pair = [], None
    if first_pipeline_uuid:
        pipeline_steps, pipeline_ssh_key_pair = await asyncio.gather(
            _first(client, f"{BASE}/repositories/{ws}/{slug}/pipelines/{first_pipeline_uuid}/steps",
                   params={"fields": "values.uuid,values.name,values.state.name"}),
            _get(client, f"{BASE}/repositories/{ws}/{slug}/pipelines_config/ssh/key_pair"),
        )
    else:
        pipeline_ssh_key_pair = await _get(
            client, f"{BASE}/repositories/{ws}/{slug}/pipelines_config/ssh/key_pair")

    sub["pipeline_steps"] = pipeline_steps
    sub["pipeline_ssh_key_pair"] = {"ok": pipeline_ssh_key_pair is not None and "_error" not in (pipeline_ssh_key_pair or {})}

    first_step_uuid = _id0(pipeline_steps, "uuid")
    sub["first_step_uuid"] = first_step_uuid

    # Pipeline caches (discovered after a run)
    pipeline_caches = await _first(
        client, f"{BASE}/repositories/{ws}/{slug}/pipelines-config/caches",
        params={"fields": "values.uuid,values.name"})
    sub["pipeline_caches"] = pipeline_caches
    sub["first_cache_uuid"] = _id0(pipeline_caches, "uuid")

    # --- Environments & deployment env variables ---
    first_env_uuid = _id0(base["environments"], "uuid")
    sub["first_env_uuid"] = first_env_uuid

    env_variables: list = []
    if first_env_uuid:
        env_variables = await _first(
            client,
            f"{BASE}/repositories/{ws}/{slug}/deployments_config/environments/{first_env_uuid}/variables",
            params={"fields": "values.uuid,values.key"})
    sub["env_variables"] = env_variables
    sub["first_env_var_uuid"] = _id0(env_variables, "uuid")

    # --- Deploy key ID (deploy_keys uses integer id, not uuid) ---
    sub["first_deploy_key_id"] = _id0(base["deploy_keys"], "id")

    # --- Branch restriction ID ---
    sub["first_branch_restriction_id"] = _id0(base["branch_restrictions"], "id")

    # --- Pipeline sub-IDs ---
    sub["first_pipeline_var_uuid"] = _id0(base["pipeline_vars"], "uuid")
    sub["first_pipeline_schedule_uuid"] = _id0(base["pipeline_schedules"], "uuid")
    sub["first_pipeline_known_host_uuid"] = _id0(base["pipeline_known_hosts"], "uuid")

    # Schedule executions
    schedule_executions: list = []
    first_sched_uuid = sub["first_pipeline_schedule_uuid"]
    if first_sched_uuid:
        schedule_executions = await _first(
            client,
            f"{BASE}/repositories/{ws}/{slug}/pipelines_config/schedules/{first_sched_uuid}/executions",
            params={"fields": "values.uuid"})
    sub["schedule_executions"] = schedule_executions

    # --- Issues sub-resources ---
    first_issue_id = _id0(base["issues"], "id")
    sub["first_issue_id"] = first_issue_id

    issue_comments, issue_changes = [], []
    if first_issue_id:
        issue_comments, issue_changes = await asyncio.gather(
            _first(client, f"{BASE}/repositories/{ws}/{slug}/issues/{first_issue_id}/comments",
                   params={"fields": "values.id,values.content.raw"}),
            _first(client, f"{BASE}/repositories/{ws}/{slug}/issues/{first_issue_id}/changes",
                   params={"fields": "values.id"}),
        )
    sub["issue_comments"] = issue_comments
    sub["issue_changes"] = issue_changes
    sub["first_issue_comment_id"] = _id0(issue_comments, "id")
    sub["first_issue_change_id"] = _id0(issue_changes, "id")

    # Issue milestones, versions, components
    milestones, versions, components = await asyncio.gather(
        _first(client, f"{BASE}/repositories/{ws}/{slug}/milestones",
               params={"fields": "values.id,values.name"}),
        _get(client, f"{BASE}/repositories/{ws}/{slug}/versions"),
        _first(client, f"{BASE}/repositories/{ws}/{slug}/components",
               params={"fields": "values.id,values.name"}),
    )
    sub["issue_milestones"] = milestones
    sub["issue_versions"] = []
    if isinstance(versions, dict) and "values" in versions:
        sub["issue_versions"] = [v for v in versions["values"] if isinstance(v, dict)]
    sub["issue_components"] = components
    sub["first_milestone_id"] = _id0(milestones, "id")
    sub["first_version_id"] = _id0(sub["issue_versions"], "id")
    sub["first_component_id"] = _id0(components, "id")

    return sub


# ---------------------------------------------------------------------------
# Tier-4: snippet sub-resources
# ---------------------------------------------------------------------------

async def probe_snippet_detail(client: httpx.AsyncClient, workspace: str, encoded_id: str) -> dict:
    snippet_comments, snippet_commits = await asyncio.gather(
        _first(client, f"{BASE}/snippets/{workspace}/{encoded_id}/comments",
               params={"fields": "values.id,values.content.raw"}),
        _first(client, f"{BASE}/snippets/{workspace}/{encoded_id}/commits",
               params={"fields": "values.hash,values.message"}),
    )
    first_commit = _id0(snippet_commits, "hash")
    snippet_diff = None
    if first_commit:
        snippet_diff = await _get(client, f"{BASE}/snippets/{workspace}/{encoded_id}/{first_commit}/diff")

    return {
        "encoded_id": encoded_id,
        "comments": snippet_comments,
        "commits": snippet_commits,
        "first_comment_id": _id0(snippet_comments, "id"),
        "first_revision": first_commit,
        "has_diff": snippet_diff is not None,
    }


# ---------------------------------------------------------------------------
# Assemble full repo detail
# ---------------------------------------------------------------------------

async def probe_repo_full(client: httpx.AsyncClient, ws: str, slug: str) -> dict:
    base = await _probe_repo_base(client, ws, slug)
    sub = await _probe_repo_sub(client, ws, slug, base)
    return {"slug": slug, "base": base, "sub": sub}


# ---------------------------------------------------------------------------
# Score
# ---------------------------------------------------------------------------

def _score_repo(d: dict) -> tuple[int, int, list[str]]:
    """Return (present, total, missing_labels)."""
    base = d.get("base", {})
    sub = d.get("sub", {})

    checks = [
        ("commits",              _ok(base.get("commits", []))),
        ("branches",             _ok(base.get("branches", []))),
        ("tags",                 _ok(base.get("tags", []))),
        ("pull_requests",        _ok(sub.get("prs_open", [])) or _ok(sub.get("prs_merged", []))),
        ("pr_comments",          _ok(sub.get("pr_comments", []))),
        ("pr_tasks",             _ok(sub.get("pr_tasks", []))),
        ("pr_statuses",          _ok(sub.get("pr_statuses", []))),
        ("commit_statuses",      _ok(sub.get("commit_statuses", []))),
        ("commit_reports",       _ok(sub.get("commit_reports", []))),
        ("report_annotations",   _ok(sub.get("report_annotations", []))),
        ("source_tree",          base.get("source_root") is not None and "_error" not in (base.get("source_root") or {})),
        ("source_file_path",     bool(sub.get("source_file_path"))),
        ("pipelines",            _ok(base.get("pipelines", []))),
        ("pipeline_steps",       _ok(sub.get("pipeline_steps", []))),
        ("pipeline_vars",        _ok(base.get("pipeline_vars", []))),
        ("pipeline_schedules",   _ok(base.get("pipeline_schedules", []))),
        ("pipeline_known_hosts", _ok(base.get("pipeline_known_hosts", []))),
        ("pipeline_ssh_key",     sub.get("pipeline_ssh_key_pair", {}).get("ok", False)),
        ("pipeline_caches",      _ok(sub.get("pipeline_caches", []))),
        ("sched_executions",     _ok(sub.get("schedule_executions", []))),
        ("environments",         _ok(base.get("environments", []))),
        ("deployments",          _ok(base.get("deployments", []))),
        ("env_variables",        _ok(sub.get("env_variables", []))),
        ("deploy_keys",          _ok(base.get("deploy_keys", []))),
        ("branch_restrictions",  _ok(base.get("branch_restrictions", []))),
        ("default_reviewers",    _ok(base.get("default_reviewers", []))),
        ("branching_model",      base.get("branching_model") is not None and "_error" not in (base.get("branching_model") or {})),
        ("override_settings",    base.get("override_settings") is not None),
        ("repo_group_perms",     _ok(base.get("repo_group_perms", []))),
        ("repo_user_perms",      _ok(base.get("repo_user_perms", []))),
        ("hooks_repo",           _ok(base.get("hooks", []))),
        ("issues",               _ok(base.get("issues", []))),
        ("issue_comments",       _ok(sub.get("issue_comments", []))),
        ("issue_changes",        _ok(sub.get("issue_changes", []))),
        ("issue_milestones",     _ok(sub.get("issue_milestones", []))),
        ("issue_versions",       _ok(sub.get("issue_versions", []))),
        ("issue_components",     _ok(sub.get("issue_components", []))),
        ("downloads",            _ok(base.get("downloads", []))),
    ]
    present = sum(1 for _, v in checks if v)
    missing = [label for label, v in checks if not v]
    return present, len(checks), missing


# ---------------------------------------------------------------------------
# Seeding action builder
# ---------------------------------------------------------------------------

def _seeding_actions(
    user: dict,
    ws: dict,
    repos: list[dict],
    best: dict | None,
    projects: list[dict],
    snippets: dict,
    ws_members: dict,
    ws_webhooks: dict,
    ws_pipeline_vars: dict,
    user_ssh_keys: dict,
    user_gpg_keys: dict,
) -> list[dict]:

    def _add(actions: list, pri: str, action: str, why: str, sdk_fns: list[str]) -> None:
        actions.append({"priority": pri, "action": action, "why": why, "sdk_functions": sdk_fns})

    actions: list[dict] = []

    if not user.get("ok"):
        _add(actions, "🔴 BLOCKER", "Fix BB_EMAIL / BB_TOKEN credentials", "Everything fails without auth", ["*"])
        return actions
    if not ws.get("ok"):
        _add(actions, "🔴 BLOCKER", "Fix BB_WORKSPACE slug", "Workspace not accessible", ["*"])
        return actions
    if not repos:
        _add(actions, "🔴 BLOCKER", "Create a repository", "All repo-scoped SDK functions require a repo",
             ["repos.*", "branches.*", "commits.*", "prs.*", "pipelines.*", "...all repo-scoped"])
        return actions

    b = best
    if not b:
        return actions

    base = b.get("base", {})
    sub = b.get("sub", {})
    slug = b.get("slug", "bb-probe")

    # Core data
    if not _ok(base.get("commits", [])):
        _add(actions, "🔴 BLOCKER",
             f"Push at least one commit to `{slug}` (init repo with README + code file)",
             "Required by: commits.list/get/prs, branches.list/get, source.root/get/history, "
             "branching_model.get/effective, commit_statuses.list/create, reports.list/create, search.code",
             ["commits.list", "commits.get", "commits.prs",
              "branches.list", "branches.get", "branches.create", "branches.delete",
              "source.root", "source.get", "source.history", "source.upload",
              "branching_model.get", "branching_model.effective", "branching_model.settings",
              "commit_statuses.list", "commit_statuses.get", "commit_statuses.create", "commit_statuses.update",
              "reports.list", "reports.get", "reports.create_or_update", "reports.annotations",
              "search.code"])

    if not _ok(base.get("tags", [])):
        _add(actions, "🟡 MEDIUM",
             f"Create a git tag in `{slug}` (`git tag v0.1.0 && git push origin v0.1.0`)",
             "Required by: branches.tags / branches.get_tag / branches.create_tag / branches.delete_tag",
             ["branches.tags", "branches.get_tag", "branches.create_tag", "branches.delete_tag"])

    if not (_ok(sub.get("prs_open", [])) or _ok(sub.get("prs_merged", []))):
        _add(actions, "🔴 BLOCKER",
             f"Create a feature branch and open a pull request in `{slug}`",
             "Required by all prs.* functions, commits.prs, properties.pr_get/set/delete",
             ["prs.list", "prs.get", "prs.create", "prs.update", "prs.merge",
              "prs.approve", "prs.unapprove", "prs.decline", "prs.request_changes",
              "prs.comments", "prs.add_comment", "prs.get_comment", "prs.update_comment",
              "prs.create_task", "prs.get_task", "prs.diff", "prs.commits",
              "prs.activity", "prs.pr_activity", "prs.diffstat", "prs.patch", "prs.statuses",
              "commits.prs", "properties.pr_get", "properties.pr_set", "properties.pr_delete"])

    if not _ok(sub.get("pr_comments", [])):
        _add(actions, "🟡 MEDIUM",
             f"Add a comment to the open PR in `{slug}`",
             "Required by: prs.get_comment, prs.update_comment, prs.delete_comment, prs.resolve_comment",
             ["prs.get_comment", "prs.update_comment", "prs.delete_comment",
              "prs.resolve_comment", "prs.unresolve_comment"])

    if not _ok(sub.get("pr_tasks", [])):
        _add(actions, "🟢 LOW",
             f"Create a PR task (inline TODO) on the open PR in `{slug}`",
             "Required by: prs.get_task, prs.update_task, prs.delete_task, prs.merge_task_status",
             ["prs.get_task", "prs.update_task", "prs.delete_task", "prs.merge_task_status"])

    if not _ok(sub.get("commit_statuses", [])):
        _add(actions, "🟡 MEDIUM",
             f"POST a build status on the latest commit in `{slug}` via API",
             "Required by: commit_statuses.list, commit_statuses.get, commit_statuses.update",
             ["commit_statuses.list", "commit_statuses.get", "commit_statuses.update"])

    if not _ok(sub.get("commit_reports", [])):
        _add(actions, "🟡 MEDIUM",
             f"POST a Code Insights report on the latest commit in `{slug}` via API",
             "Required by: reports.list, reports.get, reports.create_or_update, reports.delete, "
             "reports.annotations, reports.get_annotation, reports.create_annotation, reports.bulk_annotations",
             ["reports.list", "reports.get", "reports.create_or_update", "reports.delete",
              "reports.annotations", "reports.get_annotation", "reports.create_annotation",
              "reports.bulk_annotations", "reports.delete_annotation"])

    if not _ok(base.get("pipelines", [])):
        _add(actions, "🟡 MEDIUM",
             f"Enable Pipelines and push bitbucket-pipelines.yml to `{slug}`; trigger at least one run",
             "Required by all pipelines.list/get/run/stop/steps/step/step_log and pipeline config functions",
             ["pipelines.list", "pipelines.get", "pipelines.run", "pipelines.stop",
              "pipelines.steps", "pipelines.step", "pipelines.step_log",
              "pipelines.config", "pipelines.update_config"])

    if not _ok(sub.get("pipeline_steps", [])):
        _add(actions, "🟡 MEDIUM",
             "Ensure the pipeline run completes at least one step",
             "Required by: pipelines.step, pipelines.step_log, pipelines.container_log, "
             "pipelines.test_reports, pipelines.test_cases",
             ["pipelines.step", "pipelines.step_log", "pipelines.container_log",
              "pipelines.test_reports", "pipelines.test_cases", "pipelines.test_case_reasons"])

    if not _ok(base.get("pipeline_vars", [])):
        _add(actions, "🟢 LOW",
             f"Add a pipeline repository variable to `{slug}`",
             "Required by: pipelines.variables, pipelines.get_variable, pipelines.update_variable, pipelines.delete_variable",
             ["pipelines.variables", "pipelines.get_variable", "pipelines.update_variable", "pipelines.delete_variable"])

    if not _ok(base.get("pipeline_schedules", [])):
        _add(actions, "🟢 LOW",
             f"Add a pipeline schedule to `{slug}`",
             "Required by: pipelines.schedules, pipelines.get_schedule, pipelines.update_schedule, "
             "pipelines.delete_schedule, pipelines.schedule_executions",
             ["pipelines.schedules", "pipelines.get_schedule", "pipelines.update_schedule",
              "pipelines.delete_schedule", "pipelines.schedule_executions"])

    if not _ok(base.get("pipeline_known_hosts", [])):
        _add(actions, "🟢 LOW",
             f"Add a pipeline known host entry to `{slug}` (e.g. hostname=github.com)",
             "Required by: pipelines.known_hosts, pipelines.get_known_host, pipelines.update_known_host, pipelines.delete_known_host",
             ["pipelines.known_hosts", "pipelines.get_known_host", "pipelines.create_known_host",
              "pipelines.update_known_host", "pipelines.delete_known_host"])

    if not sub.get("pipeline_ssh_key_pair", {}).get("ok"):
        _add(actions, "🟢 LOW",
             f"Generate a pipeline SSH key pair for `{slug}` (Pipelines settings → SSH keys → Generate)",
             "Required by: pipelines.ssh_key_pair, pipelines.update_ssh_key_pair, pipelines.delete_ssh_key_pair",
             ["pipelines.ssh_key_pair", "pipelines.update_ssh_key_pair", "pipelines.delete_ssh_key_pair"])

    if not _ok(sub.get("pipeline_caches", [])):
        _add(actions, "🟢 LOW",
             f"Trigger a pipeline that uses `caches:` in bitbucket-pipelines.yml to generate cache entries",
             "Required by: pipelines.caches, pipelines.delete_cache, pipelines.cache_uri, pipelines.clear_caches",
             ["pipelines.caches", "pipelines.delete_cache", "pipelines.cache_uri", "pipelines.clear_caches"])

    if not _ok(base.get("environments", [])):
        _add(actions, "🟡 MEDIUM",
             f"Add deployment environments (Test/Staging/Production) to `{slug}` via Repo settings → Deployments",
             "Required by: deployments.envs, deployments.get_env, deployments.update_env, "
             "deployments.delete_env, deployments.env_variables",
             ["deployments.envs", "deployments.get_env", "deployments.create_env",
              "deployments.update_env", "deployments.delete_env",
              "deployments.env_variables", "deployments.create_env_variable",
              "deployments.update_env_variable", "deployments.delete_env_variable"])

    if not _ok(base.get("deployments", [])):
        _add(actions, "🟡 MEDIUM",
             "Run a pipeline step with `deployment: <env-name>` to generate a Deployment object",
             "Required by: deployments.list, deployments.get",
             ["deployments.list", "deployments.get"])

    if not _ok(sub.get("env_variables", [])):
        _add(actions, "🟢 LOW",
             f"Add a variable to one of the deployment environments in `{slug}`",
             "Required by: deployments.env_variables, deployments.create_env_variable, "
             "deployments.update_env_variable, deployments.delete_env_variable",
             ["deployments.env_variables", "deployments.create_env_variable",
              "deployments.update_env_variable", "deployments.delete_env_variable"])

    if not _ok(base.get("hooks", [])):
        _add(actions, "🟢 LOW",
             f"Add a repo webhook to `{slug}` (any URL)",
             "Required by: webhooks.list_repo, webhooks.get_repo, webhooks.update_repo, webhooks.delete_repo",
             ["webhooks.list_repo", "webhooks.get_repo", "webhooks.create_repo",
              "webhooks.update_repo", "webhooks.delete_repo"])

    if not ws_webhooks.get("ok"):
        _add(actions, "🟢 LOW",
             "Add a workspace webhook (Workspace settings → Webhooks)",
             "Required by: webhooks.list_workspace, webhooks.get_workspace, webhooks.update_workspace, webhooks.delete_workspace",
             ["webhooks.list_workspace", "webhooks.get_workspace", "webhooks.create_workspace",
              "webhooks.update_workspace", "webhooks.delete_workspace"])

    if not _ok(base.get("issues", [])):
        _add(actions, "🟡 MEDIUM",
             f"Enable issue tracker in `{slug}` settings and create at least 1 issue",
             "Required by all issues.* functions",
             ["issues.list", "issues.get", "issues.create", "issues.update", "issues.delete",
              "issues.comments", "issues.add_comment", "issues.get_comment", "issues.update_comment",
              "issues.changes", "issues.vote", "issues.watch",
              "issues.milestones", "issues.versions", "issues.components", "issues.attachments",
              "issues.export", "issues.import_data"])

    if not _ok(sub.get("issue_comments", [])):
        _add(actions, "🟢 LOW",
             "Add a comment to the first issue",
             "Required by: issues.get_comment, issues.update_comment, issues.delete_comment",
             ["issues.get_comment", "issues.update_comment", "issues.delete_comment"])

    if not _ok(sub.get("issue_milestones", [])):
        _add(actions, "🟢 LOW",
             f"Create a milestone in `{slug}`'s issue tracker",
             "Required by: issues.milestones, issues.get_milestone",
             ["issues.milestones", "issues.get_milestone"])

    if not _ok(sub.get("issue_versions", [])):
        _add(actions, "🟢 LOW",
             f"Create a version in `{slug}`'s issue tracker",
             "Required by: issues.versions, issues.get_version",
             ["issues.versions", "issues.get_version"])

    if not _ok(sub.get("issue_components", [])):
        _add(actions, "🟢 LOW",
             f"Create a component in `{slug}`'s issue tracker",
             "Required by: issues.components, issues.get_component",
             ["issues.components", "issues.get_component"])

    if not _ok(base.get("downloads", [])):
        _add(actions, "🟢 LOW",
             f"Upload any file to `{slug}` downloads section",
             "Required by: downloads.list, downloads.get, downloads.delete",
             ["downloads.list", "downloads.get", "downloads.delete"])

    if not _ok(base.get("branch_restrictions", [])):
        _add(actions, "🟢 LOW",
             f"Add at least one branch restriction rule to `{slug}`",
             "Required by: branch_restrictions.list, branch_restrictions.get, branch_restrictions.update, branch_restrictions.delete",
             ["branch_restrictions.list", "branch_restrictions.get",
              "branch_restrictions.update", "branch_restrictions.delete"])

    if not _ok(base.get("deploy_keys", [])):
        _add(actions, "🟢 LOW",
             f"Add an SSH deploy key to `{slug}`",
             "Required by: deployments.deploy_keys, deployments.get_deploy_key, deployments.update_deploy_key, deployments.delete_deploy_key",
             ["deployments.deploy_keys", "deployments.get_deploy_key",
              "deployments.create_deploy_key", "deployments.update_deploy_key",
              "deployments.delete_deploy_key"])

    if not _ok(base.get("repo_group_perms", [])):
        _add(actions, "🟢 LOW",
             f"Add a group permission to `{slug}` (requires a workspace group to exist)",
             "Required by: repos.group_permissions, repos.get_group_permission, repos.set_group_permission, repos.delete_group_permission",
             ["repos.group_permissions", "repos.get_group_permission",
              "repos.set_group_permission", "repos.delete_group_permission"])

    if not _ok(base.get("repo_user_perms", [])):
        _add(actions, "🟢 LOW",
             f"Add a user permission to `{slug}` (grant another user explicit access)",
             "Required by: repos.user_permissions, repos.get_user_permission, repos.set_user_permission, repos.delete_user_permission",
             ["repos.user_permissions", "repos.get_user_permission",
              "repos.set_user_permission", "repos.delete_user_permission"])

    if not projects:
        _add(actions, "🟡 MEDIUM",
             "Create a project in the workspace",
             "Required by: projects.list, projects.get, projects.update, projects.delete, "
             "projects.default_reviewers, projects.group_permissions, projects.user_permissions, "
             "branching_model.project_get, branching_model.project_settings",
             ["projects.list", "projects.get", "projects.update", "projects.delete",
              "projects.default_reviewers", "projects.get_default_reviewer",
              "projects.group_permissions", "projects.user_permissions",
              "branching_model.project_get", "branching_model.project_settings",
              "branching_model.update_project_settings"])

    if not snippets.get("ok"):
        _add(actions, "🟡 MEDIUM",
             "Create at least one snippet in the workspace (with a text file inside)",
             "Required by all snippets.* functions",
             ["snippets.list", "snippets.get", "snippets.create", "snippets.update", "snippets.delete",
              "snippets.comments", "snippets.add_comment", "snippets.get_comment",
              "snippets.commits", "snippets.get_commit", "snippets.get_file",
              "snippets.watch", "snippets.watchers", "snippets.diff", "snippets.patch"])

    if not ws_pipeline_vars.get("ok"):
        _add(actions, "🟢 LOW",
             "Add a workspace-level pipeline variable (Workspace settings → Pipelines → Variables)",
             "Required by: pipelines.workspace_variables, pipelines.get_workspace_variable, "
             "pipelines.update_workspace_variable, pipelines.delete_workspace_variable",
             ["pipelines.workspace_variables", "pipelines.get_workspace_variable",
              "pipelines.create_workspace_variable", "pipelines.update_workspace_variable",
              "pipelines.delete_workspace_variable"])

    if not user_ssh_keys.get("ok"):
        _add(actions, "🟢 LOW",
             "Add an SSH key to your Bitbucket account (Account settings → SSH keys)",
             "Required by: users.ssh_keys, users.get_ssh_key, users.update_ssh_key, users.delete_ssh_key",
             ["users.ssh_keys", "users.get_ssh_key", "users.add_ssh_key",
              "users.update_ssh_key", "users.delete_ssh_key"])

    if not user_gpg_keys.get("ok"):
        _add(actions, "🟢 LOW",
             "Add a GPG key to your Bitbucket account (Account settings → GPG keys)",
             "Required by: users.gpg_keys, users.get_gpg_key, users.delete_gpg_key",
             ["users.gpg_keys", "users.get_gpg_key", "users.add_gpg_key", "users.delete_gpg_key"])

    # Always note Connect-app as untestable
    _add(actions, "⚪ UNTESTABLE",
         "Install a Bitbucket Connect add-on with linker support (requires a Connect app deployment)",
         "Required by all addon.* and properties.* functions — needs a real Connect app with app_key",
         ["addon.delete", "addon.update", "addon.linkers", "addon.get_linker",
          "addon.linker_values", "addon.get_linker_value", "addon.create_linker_value",
          "addon.set_linker_values", "addon.clear_linker_values", "addon.delete_linker_value",
          "properties.repo_get", "properties.repo_set", "properties.repo_delete",
          "properties.commit_get", "properties.commit_set", "properties.commit_delete",
          "properties.pr_get", "properties.pr_set", "properties.pr_delete",
          "properties.user_get", "properties.user_set", "properties.user_delete"])

    _add(actions, "⚪ UNTESTABLE",
         "Provision Bitbucket Cloud runners (requires a self-hosted runner registration)",
         "Required by all pipelines.runners / pipelines.workspace_runners functions",
         ["pipelines.runners", "pipelines.get_runner", "pipelines.create_runner",
          "pipelines.update_runner", "pipelines.delete_runner",
          "pipelines.workspace_runners", "pipelines.get_workspace_runner",
          "pipelines.create_workspace_runner", "pipelines.update_workspace_runner",
          "pipelines.delete_workspace_runner"])

    _add(actions, "⚪ UNTESTABLE",
         "Run a pipeline with test reporting enabled to generate test-report objects",
         "Required by: pipelines.test_reports, pipelines.test_cases, pipelines.test_case_reasons",
         ["pipelines.test_reports", "pipelines.test_cases", "pipelines.test_case_reasons"])

    return actions


# ---------------------------------------------------------------------------
# Markdown report
# ---------------------------------------------------------------------------

OK = "✅"
FAIL = "❌"
SKIP = "⚪"

def _s(v: bool) -> str:
    return OK if v else FAIL


def generate_markdown(
    report: dict,
    ws_members: dict,
    ws_webhooks: dict,
    ws_pipeline_vars: dict,
    user_ssh_keys: dict,
    user_gpg_keys: dict,
    snippet_detail: dict | None,
) -> str:
    user = report["user"]
    ws = report["workspace"]
    repos = report["repos"]
    best = report.get("best_repo")
    projects = report["projects"]
    snippets = report["snippets"]
    seeding = report["seeding_actions"]
    ts = report["generated_at"]

    lines: list[str] = []
    a = lines.append

    a("# Bitbucket Cloud — Full SDK Test Data Probe Report")
    a("")
    a(f"Generated: {ts}  ")
    a(f"Target: all ~407 public functions across 19 `bb.cloud.sdk` modules")
    a("")

    # Identity
    a("## Identity")
    a("")
    a("| Field | Value |")
    a("|---|---|")
    if user.get("ok"):
        a(f"| User | {user['display_name']} (`{user['nickname']}`) |")
        a(f"| Account ID | `{user['account_id']}` |")
        a(f"| UUID | `{user['uuid']}` |")
    else:
        a("| User | ❌ Auth failed |")
    a(f"| Workspace | `{ws.get('slug', '?')}` — {ws.get('name', '?')} |")
    a(f"| Workspace UUID | `{ws.get('uuid', '?')}` |")
    a("")

    # Workspace-level resources
    a("## Workspace-Level Resources")
    a("")
    a("| Resource | Status | Detail | SDK Functions |")
    a("|---|---|---|---|")
    a(f"| Projects | {_s(bool(projects))} | {len(projects)} found | `projects.*`, `branching_model.project_*` |")
    a(f"| Snippets | {_s(snippets.get('ok', False))} | {snippets.get('count', 0)} found | `snippets.*` |")
    a(f"| Workspace webhooks | {_s(ws_webhooks.get('ok', False))} | {ws_webhooks.get('count', 0)} found | `webhooks.list_workspace` etc |")
    a(f"| Workspace pipeline vars | {_s(ws_pipeline_vars.get('ok', False))} | {ws_pipeline_vars.get('count', 0)} found | `pipelines.workspace_variables` etc |")
    a(f"| Workspace members | {_s(ws_members.get('ok', False))} | {ws_members.get('count', 0)} found | `workspaces.members`, `workspaces.get_member` |")
    a(f"| User SSH keys | {_s(user_ssh_keys.get('ok', False))} | {user_ssh_keys.get('count', 0)} found | `users.ssh_keys`, `users.get_ssh_key` |")
    a(f"| User GPG keys | {_s(user_gpg_keys.get('ok', False))} | {user_gpg_keys.get('count', 0)} found | `users.gpg_keys`, `users.get_gpg_key` |")
    a("")

    # Repos overview
    a(f"## Repositories ({len(repos)} in workspace)")
    a("")
    if not repos:
        a("❌ No repositories found.")
    else:
        a("| Score | Slug | Commits | Branches | Tags | PRs | Pipelines | Issues | Envs | Snippets-like |")
        a("|---|---|---|---|---|---|---|---|---|---|")
        for r in repos:
            d = r.get("_detail")
            if not d:
                a(f"| ? | `{r['slug']}` | (not probed) | | | | | | | |")
                continue
            present, total, _ = _score_repo(d)
            base2 = d.get("base", {})
            sub2 = d.get("sub", {})
            b_mark = " **← probe**" if r["slug"] == (best or {}).get("slug") else ""
            a(f"| {present}/{total} | `{r['slug']}`{b_mark} "
              f"| {_s(_ok(base2.get('commits',[])))} "
              f"| {_s(_ok(base2.get('branches',[])))} "
              f"| {_s(_ok(base2.get('tags',[])))} "
              f"| {_s(_ok(sub2.get('prs_open',[])) or _ok(sub2.get('prs_merged',[])))} "
              f"| {_s(_ok(base2.get('pipelines',[])))} "
              f"| {_s(_ok(base2.get('issues',[])))} "
              f"| {_s(_ok(base2.get('environments',[])))} "
              f"| — |")
    a("")

    # Best repo full matrix
    if best:
        d = best.get("_detail", {})
        base2 = d.get("base", {})
        sub2 = d.get("sub", {})
        present, total, missing = _score_repo(d)
        a(f"## Probe Repo: `{best['slug']}` — Full Coverage Matrix ({present}/{total})")
        a("")
        a("### Core repository data")
        a("")
        a("| Status | Resource | Key IDs | SDK Functions |")
        a("|---|---|---|---|")

        def _row(label, ok, ids, fns):
            a(f"| {_s(ok)} | `{label}` | {ids} | {fns} |")

        _row("commits", _ok(base2.get("commits",[])),
             f"first hash: `{sub2.get('first_commit_hash') or 'none'}`",
             "`commits.list` `commits.get` `commits.prs`")
        _row("branches", _ok(base2.get("branches",[])),
             ", ".join(f"`{b.get('name')}`" for b in base2.get("branches",[])[:3]) or "none",
             "`branches.list` `branches.get` `branches.create` `branches.delete`")
        _row("tags", _ok(base2.get("tags",[])),
             ", ".join(f"`{t.get('name')}`" for t in base2.get("tags",[])[:3]) or "none",
             "`branches.tags` `branches.get_tag` `branches.create_tag` `branches.delete_tag`")
        _row("source_tree", base2.get("source_root") is not None,
             f"file: `{sub2.get('source_file_path') or 'none'}`",
             "`source.root` `source.get` `source.history` `source.upload`")
        _row("branching_model", base2.get("branching_model") is not None,
             f"dev branch: `{(base2.get('branching_model') or {}).get('development', {}).get('branch', {}).get('name', 'n/a') if isinstance(base2.get('branching_model'), dict) else 'n/a'}`",
             "`branching_model.get` `branching_model.effective` `branching_model.settings`")
        _row("override_settings", base2.get("override_settings") is not None, "—",
             "`repos.override_settings` `repos.update_override_settings`")

        a("")
        a("### Commits & statuses")
        a("")
        a("| Status | Resource | Key IDs | SDK Functions |")
        a("|---|---|---|---|")
        _row("commit_statuses", _ok(sub2.get("commit_statuses",[])),
             f"{len(sub2.get('commit_statuses',[]))} on latest commit",
             "`commit_statuses.list` `commit_statuses.get` `commit_statuses.create` `commit_statuses.update`")
        _row("commit_reports (Code Insights)", _ok(sub2.get("commit_reports",[])),
             f"first report ID: `{sub2.get('first_report_id') or 'none'}`",
             "`reports.list` `reports.get` `reports.create_or_update` `reports.delete`")
        _row("report_annotations", _ok(sub2.get("report_annotations",[])),
             f"{len(sub2.get('report_annotations',[]))} annotations",
             "`reports.annotations` `reports.get_annotation` `reports.create_annotation` `reports.bulk_annotations`")

        a("")
        a("### Pull requests")
        a("")
        a("| Status | Resource | Key IDs | SDK Functions |")
        a("|---|---|---|---|")
        open_ids = [p.get("id") for p in sub2.get("prs_open", [])]
        merged_ids = [p.get("id") for p in sub2.get("prs_merged", [])]
        _row("prs", _ok(sub2.get("prs_open",[])) or _ok(sub2.get("prs_merged",[])),
             f"open: {open_ids[:2]}, merged: {merged_ids[:2]}",
             "`prs.list` `prs.get` `prs.create` `prs.update` `prs.merge` `prs.approve` `prs.decline`")
        _row("pr_comments", _ok(sub2.get("pr_comments",[])),
             f"first comment ID: `{sub2.get('first_pr_comment_id') or 'none'}`",
             "`prs.comments` `prs.get_comment` `prs.update_comment` `prs.delete_comment` `prs.resolve_comment`")
        _row("pr_tasks", _ok(sub2.get("pr_tasks",[])),
             f"first task ID: `{sub2.get('first_pr_task_id') or 'none'}`",
             "`prs.create_task` `prs.get_task` `prs.update_task` `prs.delete_task` `prs.merge_task_status`")
        _row("pr_statuses", _ok(sub2.get("pr_statuses",[])),
             f"{len(sub2.get('pr_statuses',[]))} statuses on first PR",
             "`prs.statuses`")
        _row("pr_activity", _ok(sub2.get("pr_activity",[])),
             f"{len(sub2.get('pr_activity',[]))} events",
             "`prs.activity` `prs.pr_activity`")

        a("")
        a("### Pipelines")
        a("")
        a("| Status | Resource | Key IDs | SDK Functions |")
        a("|---|---|---|---|")
        _row("pipeline_runs", _ok(base2.get("pipelines",[])),
             f"first UUID: `{sub2.get('first_pipeline_uuid') or 'none'}`",
             "`pipelines.list` `pipelines.get` `pipelines.run` `pipelines.stop`")
        _row("pipeline_steps", _ok(sub2.get("pipeline_steps",[])),
             f"first step UUID: `{sub2.get('first_step_uuid') or 'none'}`",
             "`pipelines.steps` `pipelines.step` `pipelines.step_log` `pipelines.container_log`")
        _row("pipeline_vars", _ok(base2.get("pipeline_vars",[])),
             f"first UUID: `{sub2.get('first_pipeline_var_uuid') or 'none'}`",
             "`pipelines.variables` `pipelines.get_variable` `pipelines.create_variable` etc")
        _row("pipeline_schedules", _ok(base2.get("pipeline_schedules",[])),
             f"first UUID: `{sub2.get('first_pipeline_schedule_uuid') or 'none'}`",
             "`pipelines.schedules` `pipelines.get_schedule` `pipelines.create_schedule` etc")
        _row("schedule_executions", _ok(sub2.get("schedule_executions",[])),
             f"{len(sub2.get('schedule_executions',[]))} runs",
             "`pipelines.schedule_executions`")
        _row("pipeline_known_hosts", _ok(base2.get("pipeline_known_hosts",[])),
             f"first UUID: `{sub2.get('first_pipeline_known_host_uuid') or 'none'}`",
             "`pipelines.known_hosts` `pipelines.get_known_host` etc")
        _row("pipeline_ssh_key_pair", sub2.get("pipeline_ssh_key_pair", {}).get("ok", False), "—",
             "`pipelines.ssh_key_pair` `pipelines.update_ssh_key_pair` `pipelines.delete_ssh_key_pair`")
        _row("pipeline_caches", _ok(sub2.get("pipeline_caches",[])),
             f"first UUID: `{sub2.get('first_cache_uuid') or 'none'}`",
             "`pipelines.caches` `pipelines.delete_cache` `pipelines.cache_uri` `pipelines.clear_caches`")

        a("")
        a("### Deployments")
        a("")
        a("| Status | Resource | Key IDs | SDK Functions |")
        a("|---|---|---|---|")
        env_names = [e.get("name") for e in base2.get("environments",[])]
        _row("environments", _ok(base2.get("environments",[])),
             f"{len(env_names)} found: {', '.join(f'`{n}`' for n in env_names[:3])} — first UUID: `{sub2.get('first_env_uuid') or 'none'}`",
             "`deployments.envs` `deployments.get_env` `deployments.create_env` `deployments.update_env` `deployments.delete_env`")
        _row("deployments", _ok(base2.get("deployments",[])),
             f"{len(base2.get('deployments',[]))} objects",
             "`deployments.list` `deployments.get`")
        _row("deploy_keys", _ok(base2.get("deploy_keys",[])),
             f"first key ID: `{sub2.get('first_deploy_key_id') or 'none'}`",
             "`deployments.deploy_keys` `deployments.get_deploy_key` etc")
        _row("env_variables", _ok(sub2.get("env_variables",[])),
             f"first UUID: `{sub2.get('first_env_var_uuid') or 'none'}`",
             "`deployments.env_variables` `deployments.create_env_variable` etc")

        a("")
        a("### Issues")
        a("")
        a("| Status | Resource | Key IDs | SDK Functions |")
        a("|---|---|---|---|")
        _row("issues", _ok(base2.get("issues",[])),
             f"first issue ID: `{sub2.get('first_issue_id') or 'none'}`",
             "`issues.list` `issues.get` `issues.create` `issues.update` `issues.delete`")
        _row("issue_comments", _ok(sub2.get("issue_comments",[])),
             f"first comment ID: `{sub2.get('first_issue_comment_id') or 'none'}`",
             "`issues.comments` `issues.get_comment` `issues.update_comment` `issues.delete_comment`")
        _row("issue_changes", _ok(sub2.get("issue_changes",[])),
             f"first change ID: `{sub2.get('first_issue_change_id') or 'none'}`",
             "`issues.changes` `issues.get_change` `issues.add_change`")
        _row("issue_milestones", _ok(sub2.get("issue_milestones",[])),
             f"first milestone ID: `{sub2.get('first_milestone_id') or 'none'}`",
             "`issues.milestones` `issues.get_milestone`")
        _row("issue_versions", _ok(sub2.get("issue_versions",[])),
             f"first version ID: `{sub2.get('first_version_id') or 'none'}`",
             "`issues.versions` `issues.get_version`")
        _row("issue_components", _ok(sub2.get("issue_components",[])),
             f"first component ID: `{sub2.get('first_component_id') or 'none'}`",
             "`issues.components` `issues.get_component`")

        a("")
        a("### Access control & webhooks")
        a("")
        a("| Status | Resource | Key IDs | SDK Functions |")
        a("|---|---|---|---|")
        _row("branch_restrictions", _ok(base2.get("branch_restrictions",[])),
             f"first ID: `{sub2.get('first_branch_restriction_id') or 'none'}`",
             "`branch_restrictions.list` `branch_restrictions.get` etc")
        _row("default_reviewers", _ok(base2.get("default_reviewers",[])),
             f"{len(base2.get('default_reviewers',[]))} users",
             "`prs.default_reviewers` `prs.get_default_reviewer` `prs.effective_default_reviewers`")
        _row("repo_group_permissions", _ok(base2.get("repo_group_perms",[])),
             f"{len(base2.get('repo_group_perms',[]))} groups",
             "`repos.group_permissions` `repos.get_group_permission` etc")
        _row("repo_user_permissions", _ok(base2.get("repo_user_perms",[])),
             f"{len(base2.get('repo_user_perms',[]))} users",
             "`repos.user_permissions` `repos.get_user_permission` etc")
        _row("hooks_repo", _ok(base2.get("hooks",[])),
             f"{len(base2.get('hooks',[]))} hooks",
             "`webhooks.list_repo` `webhooks.get_repo` `webhooks.create_repo` etc")

        a("")
        a("### Downloads")
        a("")
        a("| Status | Resource | Detail | SDK Functions |")
        a("|---|---|---|---|")
        _row("downloads", _ok(base2.get("downloads",[])),
             f"{len(base2.get('downloads',[]))} files",
             "`downloads.list` `downloads.get` `downloads.upload` `downloads.delete`")

    # Snippets detail
    a("")
    a("## Snippets")
    a("")
    a("| Status | Resource | Key IDs | SDK Functions |")
    a("|---|---|---|---|")
    a(f"| {_s(snippets.get('ok',False))} | `snippets_list` | {snippets.get('count',0)} snippets | `snippets.list` `snippets.list_all` |")
    if snippet_detail:
        enc_id = snippet_detail.get("encoded_id")
        a(f"| {_s(bool(enc_id))} | `snippet_encoded_id` | `{enc_id or 'none'}` | `snippets.get` `snippets.update` `snippets.delete` |")
        a(f"| {_s(_ok(snippet_detail.get('comments',[])))} | `snippet_comments` | first comment ID: `{snippet_detail.get('first_comment_id') or 'none'}` | `snippets.comments` `snippets.get_comment` etc |")
        a(f"| {_s(_ok(snippet_detail.get('commits',[])))} | `snippet_commits` | first revision: `{snippet_detail.get('first_revision') or 'none'}` | `snippets.commits` `snippets.get_commit` `snippets.diff` `snippets.patch` |")

    # Always-available
    a("")
    a("## Always-Available (no seeding required)")
    a("")
    a("| Status | Resource | SDK Functions |")
    a("|---|---|---|")
    a(f"| {_s(user.get('ok',False))} | Authenticated user | `users.me` `users.emails` `users.get_email` |")
    a(f"| {_s(ws.get('ok',False))} | Workspace | `workspaces.get` `workspaces.mine` `workspaces.my_permissions` `workspaces.my_permission` |")
    a(f"| {_s(ws_members.get('ok',False))} | Workspace members | `workspaces.members` `workspaces.get_member` |")
    a(f"| {_s(bool(repos))} | Repo list | `repos.list` `repos.my_permissions` `repos.workspace_user_permissions` |")
    a(f"| ✅ | Webhook event types | `webhooks.events` |")
    a(f"| ✅ | OIDC config/keys | `pipelines.oidc_config` `pipelines.oidc_keys` |")
    a(f"| {_s(bool(projects))} | Projects | `projects.list` `projects.get` |")
    a(f"| ✅ | Search (workspace) | `search.code` (needs commits + BB_SEARCH_QUERY) |")
    a("")

    # Untestable
    a("## Untestable Without Special Setup")
    a("")
    a("| Category | Reason | SDK Functions |")
    a("|---|---|---|")
    a("| Connect add-on (addon.*) | Requires a deployed Bitbucket Connect app with installed lifecycle | `addon.*` (10 functions) |")
    a("| Connect properties (properties.*) | Requires app_key from an installed Connect app | `properties.*` (12 functions) |")
    a("| Self-hosted runners | Requires running a runner agent and registering it | `pipelines.runners` / `pipelines.workspace_runners` (10 functions) |")
    a("| Pipeline test reports | Requires a pipeline step that publishes JUnit XML via Bitbucket's test-report feature | `pipelines.test_reports` `pipelines.test_cases` `pipelines.test_case_reasons` (3 functions) |")
    a("| Repo forking | Fork creates a new repo — needs workspace write + storage | `repos.fork` `repos.forks` |")
    a("| PR merge (destructive) | Merging closes the PR — breaks other tests if shared | `prs.merge` (needs isolated throwaway PR) |")
    a("")

    # Seeding plan
    a("## Seeding Action Plan")
    a("")
    a("| Priority | Action | SDK Functions Unlocked |")
    a("|---|---|---|")
    for item in seeding:
        fns = ", ".join(f"`{f}`" for f in item["sdk_functions"][:6])
        if len(item["sdk_functions"]) > 6:
            fns += f" +{len(item['sdk_functions'])-6} more"
        a(f"| {item['priority']} | {item['action']} | {fns} |")
    a("")

    # Env suggestions
    a("## Suggested `.env` Additions")
    a("")
    a("```dotenv")
    if best:
        a(f"BB_REPO_SLUG={best['slug']}")
    if projects:
        a(f"BB_PROJECT_KEY={projects[0].get('key', 'PROJ')}")
    a("BB_SEARCH_QUERY=def  # a string that exists in your repo code")
    a("```")
    a("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

async def main(args: argparse.Namespace) -> int:
    project_root = Path(__file__).resolve().parent.parent
    _load_dotenv(project_root / ".env")

    email = os.environ.get("BB_EMAIL", "").strip()
    token = os.environ.get("BB_TOKEN", "").strip()
    workspace = os.environ.get("BB_WORKSPACE", "").strip()
    pinned_slug = args.repo or os.environ.get("BB_REPO_SLUG", "").strip()

    missing = [n for n, v in [("BB_EMAIL", email), ("BB_TOKEN", token), ("BB_WORKSPACE", workspace)] if not v]
    if missing:
        print(f"ERROR: missing env vars: {', '.join(missing)}", file=sys.stderr)
        return 1

    print(f"=== bb.cloud.sdk full probe: workspace={workspace!r} ===")
    print(f"    auth: {email}")
    print()

    async with httpx.AsyncClient(auth=(email, token)) as client:
        print("Phase 1: identity + workspace-level resources …")
        (
            user, ws_info, repos_raw, projects_raw, snippets_info,
            ws_members, ws_webhooks, ws_pipeline_vars,
        ) = await asyncio.gather(
            probe_user(client),
            probe_workspace(client, workspace),
            probe_repos(client, workspace),
            probe_projects(client, workspace),
            probe_snippets_workspace(client, workspace),
            probe_workspace_members(client, workspace),
            probe_workspace_webhooks(client, workspace),
            probe_workspace_pipeline_vars(client, workspace),
        )

        account_id = user.get("account_id", "")
        user_ssh_keys, user_gpg_keys = await asyncio.gather(
            probe_user_ssh_keys(client, account_id),
            probe_user_gpg_keys(client, account_id),
        )

        print(f"  user: {user.get('display_name','?')} | ws: {ws_info.get('name','?')} | repos: {len(repos_raw)} | projects: {len(projects_raw)} | snippets: {snippets_info.get('count',0)}")
        print(f"  ws-members: {ws_members['count']} | ws-webhooks: {ws_webhooks['count']} | ws-pipeline-vars: {ws_pipeline_vars['count']}")
        print(f"  user-ssh-keys: {user_ssh_keys['count']} | user-gpg-keys: {user_gpg_keys['count']}")
        print()

        # Phase 2: probe repos
        repos_to_probe = repos_raw[:10]
        if pinned_slug and not any(r["slug"] == pinned_slug for r in repos_to_probe):
            d = await _get(client, f"{BASE}/repositories/{workspace}/{pinned_slug}")
            if d and "_error" not in d:
                repos_to_probe.insert(0, d)

        print(f"Phase 2: deep-probing {len(repos_to_probe)} repo(s) (tier-2 + tier-3 concurrently) …")
        repo_details = await asyncio.gather(*[
            probe_repo_full(client, workspace, r["slug"])
            for r in repos_to_probe
        ])

        slug_to_detail: dict[str, dict] = {d["slug"]: d for d in repo_details}
        for r in repos_raw:
            if r["slug"] in slug_to_detail:
                r["_detail"] = slug_to_detail[r["slug"]]

        # Select best repo
        best_repo: dict | None = None
        if pinned_slug:
            for r in repos_raw:
                if r["slug"] == pinned_slug and "_detail" in r:
                    best_repo = r
                    break
        if not best_repo:
            candidates = [r for r in repos_raw if "_detail" in r]
            if candidates:
                best_repo = max(candidates, key=lambda r: _score_repo(r["_detail"])[0])

        if best_repo:
            present, total, missing_labels = _score_repo(best_repo["_detail"])
            print(f"  best repo: {best_repo['slug']!r} score={present}/{total}")
            if missing_labels:
                print(f"  missing:   {', '.join(missing_labels[:10])}{' ...' if len(missing_labels) > 10 else ''}")
        print()

        # Phase 3: snippet sub-resources
        snippet_detail: dict | None = None
        if snippets_info.get("samples"):
            enc_id = snippets_info["samples"][0].get("id")
            if enc_id:
                print(f"Phase 3: probing snippet {enc_id!r} …")
                snippet_detail = await probe_snippet_detail(client, workspace, enc_id)
                print(f"  snippet: comments={len(snippet_detail.get('commits',[]))} commits={len(snippet_detail.get('commits',[]))}")
        print()

    # Build seeding actions
    seeding = _seeding_actions(
        user, ws_info, repos_raw, best_repo, projects_raw, snippets_info,
        ws_members, ws_webhooks, ws_pipeline_vars, user_ssh_keys, user_gpg_keys,
    )

    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "workspace_slug": workspace,
        "user": user,
        "workspace": ws_info,
        "repos": repos_raw,
        "best_repo": best_repo,
        "projects": projects_raw,
        "snippets": snippets_info,
        "snippet_detail": snippet_detail,
        "workspace_members": ws_members,
        "workspace_webhooks": ws_webhooks,
        "workspace_pipeline_vars": ws_pipeline_vars,
        "user_ssh_keys": user_ssh_keys,
        "user_gpg_keys": user_gpg_keys,
        "seeding_actions": seeding,
    }

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_dir = project_root / "cmd_outputs"
    out_dir.mkdir(exist_ok=True)

    json_path = out_dir / f"{ts}_probe_workspace.json"
    json_path.write_text(json.dumps(report, indent=2, default=str))
    print(f"JSON report → {json_path.relative_to(project_root)}")

    if not args.json_only:
        md = generate_markdown(
            report, ws_members, ws_webhooks, ws_pipeline_vars,
            user_ssh_keys, user_gpg_keys, snippet_detail,
        )
        md_path = out_dir / f"{ts}_probe_workspace.md"
        md_path.write_text(md)
        print(f"Markdown    → {md_path.relative_to(project_root)}")

    # Console summary
    print()
    print("=== Seeding Action Plan ===")
    for item in seeding:
        print(f"  {item['priority']:20s}  {item['action']}")
    print()

    if best_repo:
        present, total, _ = _score_repo(best_repo["_detail"])
        pct = round(100 * present / total)
        print(f"Coverage: {present}/{total} resource categories present ({pct}%)")

    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Full SDK probe for bb.cloud.sdk test data")
    parser.add_argument("--repo", metavar="SLUG", default="",
                        help="Pin probe repo (overrides BB_REPO_SLUG)")
    parser.add_argument("--json-only", action="store_true",
                        help="Skip markdown generation")
    sys.exit(asyncio.run(main(parser.parse_args())))
