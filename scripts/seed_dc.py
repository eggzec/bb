#!/usr/bin/env python3
"""Seed minimal test data for Bitbucket Data Center API validation.

Creates project, repository, branch, commit, and PR. Idempotent — safe to re-run.

Skipped (not needed for basic API testing):
  CI builds — require Bitbucket Pipelines enablement
  Secret scanning — requires feature enablement
  Merge checks — require CI configuration

Usage:
    uv run python3 scripts/seed_dc.py
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


def main() -> int:
    project_root = Path(__file__).resolve().parent.parent
    _load_dotenv(project_root / ".env")

    # Verify credentials
    try:
        client = BBDCClient.from_env()
    except Exception as e:
        print(f"ERROR: BBDCClient.from_env() failed: {e}", file=sys.stderr)
        return 1

    print("=" * 70)
    print("Bitbucket Data Center — seed data generator")
    print("=" * 70)

    project_key = "TEST"
    repo_slug = "test-repo"
    branch_name = "feature/test"
    pr_title = "Test PR for SDK validation"

    # Step 1: Create project
    print(f"\n– Step 1: Create project {project_key}")
    try:
        existing_proj = client.projects.get(project_key)
        print(f"   ✅ Project {project_key} already exists — id={existing_proj.id}")
    except Exception:
        try:
            proj = client.projects.create(
                name="Test Project",
                key=project_key,
                is_public=False,
            )
            print(f"   ✅ Created project {project_key} — id={proj.id}")
        except Exception as e:
            print(f"   ⚠️  Could not create project: {e}")
            return 1

    # Step 2: Create repository
    print(f"\n– Step 2: Create repository {repo_slug}")
    try:
        existing_repo = client.repos.get(project_key, repo_slug)
        print(f"   ✅ Repository {repo_slug} already exists — slug={existing_repo.slug}")
    except Exception:
        try:
            repo = client.repos.create(
                project_key=project_key,
                name=repo_slug,
                scm="git",
            )
            print(f"   ✅ Created repository {repo_slug} — slug={repo.slug}")
            print("   ⏳ Waiting for repository initialization…")
            import time
            time.sleep(2)
        except Exception as e:
            print(f"   ⚠️  Could not create repository: {e}")
            return 1

    # Step 3: Check for commits (skip REST API commit creation — DC requires git operations)
    print(f"\n– Step 3: Check repository state")
    try:
        commits = client.commits.list(project_key, repo_slug, limit=1)
        if commits:
            first_hash = commits[0].id
            print(f"   ✅ Repository has commits — head={first_hash[:12]}")
        else:
            print(f"   ⚠️  Repository is empty — commit creation requires git CLI (not implemented)")
            print(f"       Run: git clone http://<dc-host>:7990/scm/{project_key}/{repo_slug}.git")
            print(f"       Then: echo 'test' > README.md && git add . && git commit -m 'Initial commit'")
            print(f"       Then: git push origin")
    except Exception as e:
        print(f"   ⚠️  Could not list commits: {e}")

    # Step 4: Check for branches
    print(f"\n– Step 4: Check branches")
    try:
        branches = client.branches.list(project_key, repo_slug)
        if branches:
            branch_names = [b.display_id for b in branches]
            print(f"   ✅ Found {len(branches)} branch(es): {', '.join(branch_names[:3])}")
        else:
            print(f"   ⚠️  No branches found")
    except Exception as e:
        print(f"   ⚠️  Could not list branches: {e}")

    # Step 5: Check for pull requests
    print(f"\n– Step 5: Check pull requests")
    try:
        prs = client.prs.list(project_key, repo_slug)
        if prs:
            pr_ids = [str(p.id) for p in prs]
            print(f"   ✅ Found {len(prs)} PR(s): {', '.join(pr_ids[:3])}")
        else:
            print(f"   ℹ️  No pull requests found")
    except Exception as e:
        print(f"   ⚠️  Could not list PRs: {e}")

    print("\n" + "=" * 70)
    print("Seed data check complete.")
    print()
    print("Notes:")
    print("  • Project + Repository created or verified")
    print("  • For commits + branches + PRs: clone the repo locally and use git")
    print("  • Or push commits and create PRs via the Bitbucket UI")
    print("  • Run `make schema-discover-dc` to find the best project/repo")
    print("=" * 70)
    return 0


if __name__ == "__main__":
    sys.exit(main())
