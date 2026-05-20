#!/usr/bin/env python3
"""Discover Bitbucket Data Center workspace and suggest .env additions.

Reads credentials from .env in the project root, calls the DC SDK, and
prints a workspace summary plus suggested project/repo for live tests.

Usage:
    uv run python3 scripts/discover_dc_probe.py
    make schema-discover-dc
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

from bb.datacenter.sdk import BBDCClient


def _load_dotenv(path: Path) -> None:
    """Simple dotenv loader — sets os.environ for unset keys."""
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


def _check_repo(client: BBDCClient, project_key: str, repo_slug: str) -> dict:
    """Return a dict with booleans: has_commits, has_branches, has_prs."""
    result: dict[str, bool] = {"has_commits": False, "has_branches": False, "has_prs": False}

    try:
        commits = client.commits.list(project_key, repo_slug, limit=1)
        result["has_commits"] = bool(commits)
    except Exception:
        pass

    try:
        branches = client.branches.list(project_key, repo_slug, limit=1)
        result["has_branches"] = bool(branches)
    except Exception:
        pass

    try:
        prs = client.prs.list(project_key, repo_slug)
        result["has_prs"] = bool(prs)
    except Exception:
        pass

    return result


def main() -> int:
    project_root = Path(__file__).resolve().parent.parent
    _load_dotenv(project_root / ".env")

    # Verify credentials
    try:
        client = BBDCClient.from_env()
    except Exception as e:
        print(f"ERROR: BBDCClient.from_env() failed: {e}", file=sys.stderr)
        print("       Check BB_DC_BASE_URL and BB_DC_TOKEN in .env", file=sys.stderr)
        return 1

    pinned_proj = os.environ.get("BB_DC_PROJECT_KEY", "").strip()
    pinned_repo = os.environ.get("BB_DC_REPO_SLUG", "").strip()

    print("=" * 75)
    print("Bitbucket Data Center — workspace probe")
    print("=" * 75)
    print()

    # List projects
    try:
        projects = client.projects.list()
    except Exception as e:
        print(f"ERROR: Could not list projects: {e}", file=sys.stderr)
        return 1

    print(f"Found {len(projects)} project(s)")
    print()

    if not projects:
        print("No projects found. Create at least one project and repository with commits")
        print("before running live tests. schema-test-dc will still run and catch spec bugs")
        print("on endpoints without seed data.")
        print()
        return 0

    # Probe each project/repo
    best_proj_key: str | None = None
    best_repo_slug: str | None = None
    best_score = -1

    for proj in projects:
        proj_key = proj.key
        print(f"Project {proj_key} ({proj.name})")

        try:
            repos = client.repos.list(proj_key)
        except Exception as e:
            print(f"  [Error listing repos: {e}]")
            print()
            continue

        print(f"  {len(repos)} repo(s):")
        if not repos:
            print("    (no repositories)")
        else:
            print(f"  {'SLUG':<40}  commits  branches  PRs")
            print(f"  {'-' * 65}")

            for repo in repos:
                slug = repo.slug
                check = _check_repo(client, proj_key, slug)
                score = sum(check.values())

                commits_mark = "✓" if check["has_commits"] else "✗"
                branches_mark = "✓" if check["has_branches"] else "✗"
                prs_mark = "✓" if check["has_prs"] else "✗"

                marker = " <-- current selection" if (slug == pinned_repo and proj_key == pinned_proj) else ""
                print(f"    {slug:<38}  {commits_mark:<8}  {branches_mark:<9}  {prs_mark:<4}{marker}")

                if score > best_score:
                    best_score = score
                    best_proj_key = proj_key
                    best_repo_slug = slug

        print()

    # Summary
    print("=" * 75)
    print("Suggested .env additions:")
    print()

    if pinned_proj and pinned_repo:
        print(f"BB_DC_PROJECT_KEY={pinned_proj}   # already set")
        print(f"BB_DC_REPO_SLUG={pinned_repo}     # already set")
        if best_score >= 3 and (best_proj_key != pinned_proj or best_repo_slug != pinned_repo):
            print()
            print(f"Note: Found a repo with higher data richness ({best_score}/3 score)")
            print(f"  BB_DC_PROJECT_KEY={best_proj_key}")
            print(f"  BB_DC_REPO_SLUG={best_repo_slug}")
    elif best_proj_key and best_repo_slug:
        print(f"BB_DC_PROJECT_KEY={best_proj_key}   # {best_score}/3 data richness score")
        print(f"BB_DC_REPO_SLUG={best_repo_slug}")
    else:
        print("No repositories with seed data found.")
        print("Create a project and push at least one commit before running live tests.")
        print()
        print("Example:")
        print(f"  BB_DC_PROJECT_KEY=TEST")
        print(f"  BB_DC_REPO_SLUG=test-repo")

    print()
    print("=" * 75)
    return 0


if __name__ == "__main__":
    sys.exit(main())
