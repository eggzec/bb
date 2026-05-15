#!/usr/bin/env python3
"""Discover Bitbucket Cloud workspace probe data for schema and live testing.

Reads credentials from .env in the project root, calls the BB Cloud API, and
prints a workspace summary plus suggested additions to .env.

Usage:
    uv run python3 scripts/discover_cloud_probe.py
    make schema-discover-cloud
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

import httpx


# ---------------------------------------------------------------------------
# .env loader (same logic as tests/cloud/live/conftest.py)
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
# HTTP helper  (httpx preserves auth headers through same-host redirects)
# ---------------------------------------------------------------------------

def _get(url: str, email: str, token: str) -> dict:
    resp = httpx.get(url, auth=(email, token), timeout=15, follow_redirects=True)
    resp.raise_for_status()
    return resp.json()


def _get_safe(url: str, email: str, token: str) -> dict | None:
    try:
        return _get(url, email, token)
    except httpx.HTTPStatusError as exc:
        if exc.response.status_code in (404, 403):
            return None
        raise


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------

BASE = "https://api.bitbucket.org/2.0"


def _check_repo(slug: str, workspace: str, email: str, token: str) -> dict:
    """Return a dict with booleans: has_commits, has_branches, has_prs."""
    result: dict[str, bool] = {"has_commits": False, "has_branches": False, "has_prs": False}

    commits = _get_safe(
        f"{BASE}/repositories/{workspace}/{slug}/commits?pagelen=1&fields=values.hash",
        email, token,
    )
    if commits and commits.get("values"):
        result["has_commits"] = True

    branches = _get_safe(
        f"{BASE}/repositories/{workspace}/{slug}/refs/branches?pagelen=1&fields=values.name",
        email, token,
    )
    if branches and branches.get("values"):
        result["has_branches"] = True

    prs = _get_safe(
        f"{BASE}/repositories/{workspace}/{slug}/pullrequests?state=OPEN&pagelen=1&fields=values.id",
        email, token,
    )
    if prs and prs.get("values"):
        result["has_prs"] = True

    return result


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    project_root = Path(__file__).resolve().parent.parent
    _load_dotenv(project_root / ".env")

    email = os.environ.get("BB_EMAIL", "").strip()
    token = os.environ.get("BB_TOKEN", "").strip()
    workspace = os.environ.get("BB_WORKSPACE", "").strip()
    pinned_slug = os.environ.get("BB_REPO_SLUG", "").strip()

    missing = [name for name, val in [("BB_EMAIL", email), ("BB_TOKEN", token), ("BB_WORKSPACE", workspace)] if not val]
    if missing:
        print(f"ERROR: missing required env vars: {', '.join(missing)}", file=sys.stderr)
        print("       Add them to .env (copy .env.example) and re-run.", file=sys.stderr)
        return 1

    print(f"=== Bitbucket Cloud workspace probe: {workspace!r} ===")
    print()

    # List repos
    try:
        data = _get(
            f"{BASE}/repositories/{workspace}?pagelen=10&fields=values.slug,values.full_name,size",
            email, token,
        )
    except urllib.error.HTTPError as exc:
        print(f"ERROR: GET /repositories/{workspace} returned HTTP {exc.code}")
        if exc.code == 401:
            print("       Check BB_EMAIL and BB_TOKEN — credentials rejected.")
        elif exc.code == 403:
            print("       Authenticated successfully but no access to this workspace.")
        elif exc.code == 404:
            print("       Workspace not found — check BB_WORKSPACE slug.")
        return 1

    repos = data.get("values", [])
    total = data.get("size", "?")
    print(f"Repos in workspace: {total} total, probing first {len(repos)}")
    print()

    if not repos:
        print("No repos found. Create at least one repository with a commit before running")
        print("schema-test-cloud for full 200-response coverage.")
        print()
        print("schema-test-cloud will still run and catch status_code/schema issues on")
        print("404/403 responses (missing status codes in spec, wrong error bodies, etc.).")
        print()
        print("Suggested .env additions:")
        print(f"BB_WORKSPACE={workspace}  # already set")
        return 0

    # Probe each repo for data richness
    print(f"{'SLUG':<35}  commits  branches  open-PRs")
    print("-" * 65)

    best_slug: str | None = None
    best_score = -1

    for repo in repos:
        slug = repo["slug"]
        check = _check_repo(slug, workspace, email, token)
        score = sum(check.values())
        commits_mark = "yes" if check["has_commits"] else "no"
        branches_mark = "yes" if check["has_branches"] else "no"
        prs_mark = "yes" if check["has_prs"] else "no"
        marker = " <-- current BB_REPO_SLUG" if slug == pinned_slug else ""
        print(f"  {slug:<33}  {commits_mark:<7}  {branches_mark:<8}  {prs_mark:<8}{marker}")
        if score > best_score:
            best_score = score
            best_slug = slug

    print()

    if pinned_slug:
        print(f"BB_REPO_SLUG is already set to: {pinned_slug!r}")
        if not any(r["slug"] == pinned_slug for r in repos):
            print("  WARNING: that slug was not found in the first 10 repos — verify it exists.")
    else:
        print("BB_REPO_SLUG is not set — repo-scoped endpoints will use random slugs (→ 404s).")

    print()
    print("=== Suggested .env additions ===")
    if best_slug and best_slug != pinned_slug:
        print(f"BB_REPO_SLUG={best_slug}   # best probe: {best_score}/3 data richness score")
    elif best_slug:
        print(f"BB_REPO_SLUG={best_slug}   # already optimal")

    if best_score == 0:
        print()
        print("NOTE: No repos have commits yet. Populate at least one repo before running the")
        print("      live pytest suite. schema-test-cloud (schemathesis) will still run but")
        print("      only catch spec bugs visible on 404/403 responses.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
