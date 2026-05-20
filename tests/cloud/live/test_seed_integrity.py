"""Seed integrity checks — these FAIL (not skip) if expected workspace data is missing.

Run these first to diagnose workspace/credential misconfiguration before the rest
of the suite silently skips half its tests.
"""

from __future__ import annotations

import pytest

from bb.cloud.models.branch import Branch
from bb.cloud.models.error import Error
from bb.cloud.models.repository import Repository
from bb.cloud.models.tag import Tag
from bb.cloud.models.pullrequest import Pullrequest
from bb.cloud.sdk import branches, commits, prs, repos, workspaces
from bb.cloud.sdk._client import BBClient

pytestmark = pytest.mark.live

# Seed constants extracted from other test files
PROBE_REPO = "bb-probe"
SEED_BRANCH = "main"
SEED_COMMIT = "84952fad87fb39e3c6d61811a93769378dd4fad7"
SEED_TAG = "v0.1.0"
SEED_PR_ID = 1


async def test_workspace_is_reachable(client: BBClient, workspace: str) -> None:
    """Verify the configured workspace is reachable and valid."""
    result = await workspaces.get(client, workspace)
    assert not isinstance(result, Error), (
        f"Workspace {workspace!r} is unreachable — check BB_WORKSPACE and credentials"
    )
    assert result is not None, (
        f"Workspace {workspace!r} is unreachable — check BB_WORKSPACE and credentials"
    )


async def test_probe_repo_exists(client: BBClient, workspace: str) -> None:
    """Verify the probe repo exists in the seeded workspace."""
    result = await repos.get(client, workspace, PROBE_REPO)
    assert isinstance(result, Repository), (
        f"Probe repo {PROBE_REPO!r} not found — run seed script to create it"
    )


async def test_probe_branch_exists(client: BBClient, workspace: str) -> None:
    """Verify the seed branch exists in the probe repo."""
    result = await branches.get(client, workspace, PROBE_REPO, SEED_BRANCH)
    assert isinstance(result, Branch), (
        f"Branch {SEED_BRANCH!r} not found in {PROBE_REPO!r} — check seed data"
    )


async def test_seed_commit_exists(client: BBClient, workspace: str) -> None:
    """Verify the seed commit hash exists in the probe repo."""
    result = await commits.get(client, workspace, PROBE_REPO, SEED_COMMIT)
    assert not isinstance(result, Error) and result is not None, (
        f"Commit {SEED_COMMIT!r} not found in {PROBE_REPO!r} — check seed data"
    )


async def test_seed_pr_exists(client: BBClient, workspace: str) -> None:
    """Verify the seed PR exists in the probe repo."""
    result = await prs.get(client, workspace, PROBE_REPO, SEED_PR_ID)
    assert isinstance(result, Pullrequest), (
        f"PR #{SEED_PR_ID} not found in {PROBE_REPO!r} — check seed data"
    )


async def test_seed_tag_exists(client: BBClient, workspace: str) -> None:
    """Verify the seed tag exists in the probe repo."""
    result = await branches.get_tag(client, workspace, PROBE_REPO, SEED_TAG)
    assert isinstance(result, Tag), (
        f"Tag {SEED_TAG!r} not found in {PROBE_REPO!r} — check seed data"
    )
