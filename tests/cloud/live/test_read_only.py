"""Read-only live API tests — safe to run on any workspace.

Every function here calls the real Bitbucket Cloud API. The suite is
skipped automatically when BB_EMAIL/BB_TOKEN/BB_WORKSPACE aren't set.
"""

from __future__ import annotations

import pytest

from bb.cloud.models.account import Account
from bb.cloud.models.branch import Branch
from bb.cloud.models.error import Error
from bb.cloud.models.repository import Repository
from bb.cloud.models.workspace import Workspace
from bb.cloud.sdk import branches, repos, users, workspaces
from bb.cloud.sdk._client import BBClient

pytestmark = pytest.mark.live


# ---------------------------------------------------------------------------
# client / auth
# ---------------------------------------------------------------------------


def test_bbclient_from_env_builds(client: BBClient):
    assert client.workspace
    assert client.auth is not None


async def test_users_me_returns_user(client: BBClient):
    result = await users.me(client)
    assert not isinstance(result, Error)
    assert isinstance(result, Account)
    assert hasattr(result, "uuid") or hasattr(result, "account_id")


# ---------------------------------------------------------------------------
# workspaces
# ---------------------------------------------------------------------------


async def test_workspaces_mine_returns_list(client: BBClient):
    result = await workspaces.mine(client, pagelen=5)
    assert not isinstance(result, Error)
    assert isinstance(result, list)
    if result:
        assert isinstance(result[0], Workspace)


async def test_workspaces_get_returns_workspace(client: BBClient, workspace: str):
    result = await workspaces.get(client, workspace)
    assert not isinstance(result, Error)
    assert result is not None
    # Slug or UUID must match what we queried.
    slug_match = result.slug == workspace
    uuid_match = result.uuid is not None and workspace in str(result.uuid)
    assert slug_match or uuid_match, f"workspace slug/uuid mismatch: got {result.slug!r} / {result.uuid!r}"


# ---------------------------------------------------------------------------
# repositories (read only)
# ---------------------------------------------------------------------------


async def test_repos_list_returns_list(client: BBClient, workspace: str):
    result = await repos.list(client, workspace, pagelen=5)
    assert not isinstance(result, Error), f"API error: {result}"
    assert isinstance(result, list)
    # A workspace may have zero repos; all items must be Repository.
    for item in result:
        assert isinstance(item, Repository)


async def test_repos_list_respects_pagelen(client: BBClient, workspace: str):
    # Fetching with pagelen=1 should still return all repos via pagination.
    small = await repos.list(client, workspace, pagelen=1)
    big = await repos.list(client, workspace, pagelen=50)
    assert not isinstance(small, Error)
    assert not isinstance(big, Error)
    assert len(small) == len(big), "pagination lost or duplicated items"


async def test_repos_get_missing_returns_error_or_none(client: BBClient, workspace: str):
    result = await repos.get(client, workspace, "definitely-does-not-exist-zzz")
    # 404 should either come back as Error or None — never a Repository.
    assert not isinstance(result, Repository)


# ---------------------------------------------------------------------------
# branches (read only) — exercises a paginated SDK module beyond repos
# ---------------------------------------------------------------------------


async def test_branches_list_on_first_repo(client: BBClient, workspace: str):
    """List branches of the first repo — verifies branches.list + pagination."""
    repo_list = await repos.list(client, workspace, pagelen=1)
    assert not isinstance(repo_list, Error)
    if not repo_list:
        pytest.skip(f"workspace {workspace!r} has no repositories")
    # full_name is "workspace/repo-slug"; extract slug from it.
    full_name = repo_list[0].full_name
    assert full_name, "repo has no full_name"
    first_slug = full_name.split("/", 1)[-1]

    result = await branches.list(client, workspace, first_slug, pagelen=10)
    assert not isinstance(result, Error), f"branches.list failed: {result}"
    assert isinstance(result, list)
    for item in result:
        assert isinstance(item, Branch), f"unexpected item type: {type(item)}"


async def test_branches_get_missing_returns_error_or_none(client: BBClient, workspace: str):
    """404 branch lookup must return Error or None, never a Branch."""
    repo_list = await repos.list(client, workspace, pagelen=1)
    assert not isinstance(repo_list, Error)
    if not repo_list:
        pytest.skip(f"workspace {workspace!r} has no repositories")
    full_name = repo_list[0].full_name
    assert full_name
    first_slug = full_name.split("/", 1)[-1]

    result = await branches.get(client, workspace, first_slug, "this-branch-does-not-exist-zzz")
    assert not isinstance(result, Branch), f"expected Error/None, got Branch: {result}"
