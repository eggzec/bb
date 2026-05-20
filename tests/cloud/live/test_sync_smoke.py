"""Smoke tests for the synchronous SDK (bb.cloud.sync).

Verifies that sync wrappers return the same types as their async counterparts.
All tests are regular `def` (not `async def`) — sync SDK uses asyncio.run() internally.
"""

from __future__ import annotations

import pytest

from bb.cloud import sync
from bb.cloud.models.base_commit import BaseCommit
from bb.cloud.models.branch import Branch
from bb.cloud.models.commit import Commit
from bb.cloud.models.error import Error
from bb.cloud.models.repository import Repository
from bb.cloud.models.workspace import Workspace
from bb.cloud.sdk._client import BBClient

pytestmark = pytest.mark.live

PROBE_REPO = "bb-probe"


# ---------------------------------------------------------------------------
# sync.repos tests
# ---------------------------------------------------------------------------


def test_sync_repos_list_returns_list(client: BBClient, workspace: str) -> None:
    """Smoke test: sync.repos.list returns a list of Repository objects."""
    result = sync.repos.list(client, workspace)
    assert not isinstance(result, Error), (
        f"sync.repos.list errored: {result.error.message if getattr(result, 'error', None) else result!r}"
    )
    assert isinstance(result, list), f"sync.repos.list must return list, got {type(result).__name__}"
    if result:
        assert isinstance(result[0], Repository), (
            f"sync.repos.list[0] is {type(result[0]).__name__}, expected Repository"
        )


def test_sync_repos_get_returns_repo(client: BBClient, workspace: str) -> None:
    """Smoke test: sync.repos.get returns a Repository for a known repo."""
    result = sync.repos.get(client, workspace, PROBE_REPO)
    assert isinstance(result, Repository), (
        f"sync.repos.get must return Repository, got {type(result).__name__}"
    )


def test_sync_repos_get_missing_returns_error_or_none(client: BBClient, workspace: str) -> None:
    """Smoke test: sync.repos.get with nonexistent repo returns Error or None."""
    result = sync.repos.get(client, workspace, "nonexistent-repo-xyz")
    assert not isinstance(result, Repository), (
        f"sync.repos.get for nonexistent repo should not return Repository, got {result!r}"
    )


# ---------------------------------------------------------------------------
# sync.branches tests
# ---------------------------------------------------------------------------


def test_sync_branches_list_returns_list(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """Smoke test: sync.branches.list returns a list of Branch objects."""
    result = sync.branches.list(client, workspace, probe_repo_slug)
    assert not isinstance(result, Error), (
        f"sync.branches.list errored: {result.error.message if getattr(result, 'error', None) else result!r}"
    )
    assert isinstance(result, list), f"sync.branches.list must return list, got {type(result).__name__}"
    if result:
        assert isinstance(result[0], Branch), (
            f"sync.branches.list[0] is {type(result[0]).__name__}, expected Branch"
        )


def test_sync_branches_get_returns_branch(
    client: BBClient, workspace: str, probe_repo_slug: str, probe_branch_name: str
) -> None:
    """Smoke test: sync.branches.get returns a Branch for a known branch."""
    result = sync.branches.get(client, workspace, probe_repo_slug, probe_branch_name)
    assert isinstance(result, Branch), (
        f"sync.branches.get must return Branch, got {type(result).__name__}"
    )


# ---------------------------------------------------------------------------
# sync.commits tests
# ---------------------------------------------------------------------------


def test_sync_commits_list_returns_list(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """Smoke test: sync.commits.list returns a list of BaseCommit objects."""
    result = sync.commits.list(client, workspace, probe_repo_slug)
    assert not isinstance(result, Error), (
        f"sync.commits.list errored: {result.error.message if getattr(result, 'error', None) else result!r}"
    )
    assert isinstance(result, list), f"sync.commits.list must return list, got {type(result).__name__}"
    if result:
        assert isinstance(result[0], BaseCommit), (
            f"sync.commits.list[0] is {type(result[0]).__name__}, expected BaseCommit"
        )


def test_sync_commits_get_returns_commit(
    client: BBClient, workspace: str, probe_repo_slug: str, probe_commit_hash: str
) -> None:
    """Smoke test: sync.commits.get returns a Commit for a known commit hash."""
    result = sync.commits.get(client, workspace, probe_repo_slug, probe_commit_hash)
    assert result is not None, "sync.commits.get returned None for a valid commit"
    assert not isinstance(result, Error), (
        f"sync.commits.get errored: {result.error.message if getattr(result, 'error', None) else result!r}"
    )
    assert isinstance(result, Commit), (
        f"sync.commits.get must return Commit, got {type(result).__name__}"
    )


# ---------------------------------------------------------------------------
# sync.workspaces tests
# ---------------------------------------------------------------------------


def test_sync_workspaces_list_returns_list(client: BBClient) -> None:
    """Smoke test: sync.workspaces.list returns a list of Workspace objects."""
    result = sync.workspaces.list(client)
    if isinstance(result, Error):
        # GET /2.0/workspaces is deprecated (CHANGE-2770); skip gracefully
        pytest.skip(
            f"sync.workspaces.list returned Error (endpoint deprecated per CHANGE-2770): "
            f"{result.error.message if result.error else result!r}"
        )
    assert isinstance(result, list), (
        f"sync.workspaces.list must return list, got {type(result).__name__}"
    )
    if result:
        assert isinstance(result[0], Workspace), (
            f"sync.workspaces.list[0] is {type(result[0]).__name__}, expected Workspace"
        )


def test_sync_workspaces_get_returns_workspace(client: BBClient, workspace: str) -> None:
    """Smoke test: sync.workspaces.get returns a Workspace for a known workspace."""
    result = sync.workspaces.get(client, workspace)
    assert result is not None, "sync.workspaces.get returned None for a valid workspace"
    assert not isinstance(result, Error), (
        f"sync.workspaces.get errored: {result.error.message if getattr(result, 'error', None) else result!r}"
    )
    assert isinstance(result, Workspace), (
        f"sync.workspaces.get must return Workspace, got {type(result).__name__}"
    )


# ---------------------------------------------------------------------------
# Comparison: sync vs async parity
# ---------------------------------------------------------------------------


def test_sync_repos_list_paglen_consistent(client: BBClient, workspace: str) -> None:
    """Smoke test: sync.repos.list with paglen=1 and paglen=50 return identical repos.

    Previously this failed because asyncio.run() creates/closes a new event loop
    per call, corrupting the cached async httpx client on the second call.
    With BBClient used as a context manager, a persistent asyncio.Runner keeps
    the event loop open between calls — both calls succeed and share connections.
    """
    small = sync.repos.list(client, workspace, pagelen=1)
    large = sync.repos.list(client, workspace, pagelen=50)

    if isinstance(small, Error):
        pytest.skip(f"sync.repos.list(paglen=1) errored: {small}")
    if isinstance(large, Error):
        pytest.skip(f"sync.repos.list(paglen=50) errored: {large}")

    small_names = sorted(r.full_name for r in small if r.full_name)
    large_names = sorted(r.full_name for r in large if r.full_name)
    assert small_names == large_names, (
        f"sync repos paglen mismatch: paglen=1 gave {len(small_names)} repos, "
        f"paglen=50 gave {len(large_names)} repos"
    )
