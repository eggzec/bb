"""Tests for bb.datacenter.sdk.branches."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from bb.datacenter.models.rest_branch import RestBranch
from bb.datacenter.models.rest_branch_create_request import RestBranchCreateRequest
from bb.datacenter.models.rest_minimal_ref import RestMinimalRef
from bb.datacenter.sdk import branches
from bb.datacenter.sdk._errors import AuthenticationError

_PROJECT_API = "bb.datacenter.api.project"
_REPO_API = "bb.datacenter.api.repository"


# ---------------------------------------------------------------------------
# branches.list
# ---------------------------------------------------------------------------


async def test_branches_list_returns_branches(mock_dc_client, make_dc_page):
    branch = MagicMock(spec=RestBranch)
    with patch(f"{_REPO_API}.get_branches.asyncio", new=AsyncMock(return_value=make_dc_page([branch]))):
        assert await branches.list(mock_dc_client, "PRJ", "repo") == [branch]


async def test_branches_list_multi_page(mock_dc_client, make_dc_page):
    b1, b2 = MagicMock(spec=RestBranch), MagicMock(spec=RestBranch)
    pages = [make_dc_page([b1], is_last=False, next_start=1), make_dc_page([b2])]
    with patch(f"{_REPO_API}.get_branches.asyncio", new=AsyncMock(side_effect=pages)):
        assert await branches.list(mock_dc_client, "PRJ", "repo") == [b1, b2]


async def test_branches_list_empty(mock_dc_client, make_dc_page):
    with patch(f"{_REPO_API}.get_branches.asyncio", new=AsyncMock(return_value=make_dc_page([]))):
        assert await branches.list(mock_dc_client, "PRJ", "repo") == []


async def test_branches_list_wrong_type_filtered_out(mock_dc_client, make_dc_page):
    with patch(f"{_REPO_API}.get_branches.asyncio", new=AsyncMock(return_value=make_dc_page([MagicMock()]))):
        assert await branches.list(mock_dc_client, "PRJ", "repo") == []


async def test_branches_list_bad_auth_raises(bad_auth_dc_client):
    with patch(f"{_REPO_API}.get_branches.asyncio", new=AsyncMock(return_value=None)):
        with pytest.raises(AuthenticationError):
            await branches.list(bad_auth_dc_client, "PRJ", "repo")


async def test_branches_list_basic_auth_accepted(basic_mock_dc_client, make_dc_page):
    branch = MagicMock(spec=RestBranch)
    with patch(f"{_REPO_API}.get_branches.asyncio", new=AsyncMock(return_value=make_dc_page([branch]))):
        result = await branches.list(basic_mock_dc_client, "PRJ", "repo")
    assert result == [branch]


# ---------------------------------------------------------------------------
# branches.search
# ---------------------------------------------------------------------------


async def test_branches_search_returns_branches(mock_dc_client, make_dc_page):
    branch = MagicMock(spec=RestBranch)
    with patch(f"{_REPO_API}.get_branches.asyncio", new=AsyncMock(return_value=make_dc_page([branch]))):
        result = await branches.search(mock_dc_client, "PRJ", "repo", filter_text="feat/")
    assert result == [branch]


async def test_branches_search_passes_filter_text(mock_dc_client, make_dc_page):
    mock_fn = AsyncMock(return_value=make_dc_page([MagicMock(spec=RestBranch)]))
    with patch(f"{_REPO_API}.get_branches.asyncio", new=mock_fn):
        await branches.search(mock_dc_client, "PRJ", "repo", filter_text="main")
    assert mock_fn.call_args.kwargs["filter_text"] == "main"


async def test_branches_search_bad_auth_raises(bad_auth_dc_client):
    with patch(f"{_REPO_API}.get_branches.asyncio", new=AsyncMock(return_value=None)):
        with pytest.raises(AuthenticationError):
            await branches.search(bad_auth_dc_client, "PRJ", "repo")


# ---------------------------------------------------------------------------
# branches.get_default
# ---------------------------------------------------------------------------


async def test_branches_get_default_returns_ref(mock_dc_client):
    ref = MagicMock(spec=RestMinimalRef)
    with patch(f"{_PROJECT_API}.get_default_branch_2.asyncio", new=AsyncMock(return_value=ref)):
        assert await branches.get_default(mock_dc_client, "PRJ", "repo") is ref


async def test_branches_get_default_none_on_wrong_type(mock_dc_client):
    with patch(f"{_PROJECT_API}.get_default_branch_2.asyncio", new=AsyncMock(return_value=MagicMock())):
        assert await branches.get_default(mock_dc_client, "PRJ", "repo") is None


async def test_branches_get_default_bad_auth_raises(bad_auth_dc_client):
    with patch(f"{_PROJECT_API}.get_default_branch_2.asyncio", new=AsyncMock(return_value=None)):
        with pytest.raises(AuthenticationError):
            await branches.get_default(bad_auth_dc_client, "PRJ", "repo")


# ---------------------------------------------------------------------------
# branches.set_default
# ---------------------------------------------------------------------------


async def test_branches_set_default_calls_api(mock_dc_client):
    mock_fn = AsyncMock(return_value=None)
    with patch(f"{_PROJECT_API}.set_default_branch_2.asyncio", new=mock_fn):
        await branches.set_default(mock_dc_client, "PRJ", "repo", body=MagicMock(spec=RestBranch))
    mock_fn.assert_called_once()


async def test_branches_set_default_returns_none(mock_dc_client):
    with patch(f"{_PROJECT_API}.set_default_branch_2.asyncio", new=AsyncMock(return_value=None)):
        assert await branches.set_default(mock_dc_client, "PRJ", "repo") is None


async def test_branches_set_default_bad_auth_raises(bad_auth_dc_client):
    with patch(f"{_PROJECT_API}.set_default_branch_2.asyncio", new=AsyncMock(return_value=None)):
        with pytest.raises(AuthenticationError):
            await branches.set_default(bad_auth_dc_client, "PRJ", "repo")


# ---------------------------------------------------------------------------
# branches.create
# ---------------------------------------------------------------------------


async def test_branches_create_returns_branch(mock_dc_client):
    branch = MagicMock(spec=RestBranch)
    with patch(f"{_REPO_API}.create_branch.asyncio", new=AsyncMock(return_value=branch)):
        result = await branches.create(mock_dc_client, "PRJ", "repo", body=MagicMock(spec=RestBranchCreateRequest))
    assert result is branch


async def test_branches_create_none_on_wrong_type(mock_dc_client):
    with patch(f"{_REPO_API}.create_branch.asyncio", new=AsyncMock(return_value=MagicMock())):
        result = await branches.create(mock_dc_client, "PRJ", "repo", body=MagicMock(spec=RestBranchCreateRequest))
    assert result is None


async def test_branches_create_bad_auth_raises(bad_auth_dc_client):
    with patch(f"{_REPO_API}.create_branch.asyncio", new=AsyncMock(return_value=None)):
        with pytest.raises(AuthenticationError):
            await branches.create(bad_auth_dc_client, "PRJ", "repo", body=MagicMock(spec=RestBranchCreateRequest))


# ---------------------------------------------------------------------------
# branches.delete
# ---------------------------------------------------------------------------


async def test_branches_delete_calls_api(mock_dc_client):
    mock_fn = AsyncMock(return_value=None)
    with patch(f"{_REPO_API}.delete_branch.asyncio", new=mock_fn):
        await branches.delete(mock_dc_client, "PRJ", "repo", branch_id="refs/heads/main")
    mock_fn.assert_called_once()


async def test_branches_delete_returns_none(mock_dc_client):
    with patch(f"{_REPO_API}.delete_branch.asyncio", new=AsyncMock(return_value=None)):
        assert await branches.delete(mock_dc_client, "PRJ", "repo", branch_id="refs/heads/main") is None


async def test_branches_delete_bad_auth_raises(bad_auth_dc_client):
    with patch(f"{_REPO_API}.delete_branch.asyncio", new=AsyncMock(return_value=None)):
        with pytest.raises(AuthenticationError):
            await branches.delete(bad_auth_dc_client, "PRJ", "repo", branch_id="refs/heads/main")


# ---------------------------------------------------------------------------
# branches.get_by_commit
# ---------------------------------------------------------------------------


async def test_branches_get_by_commit_returns_refs(mock_dc_client, make_dc_page):
    ref = MagicMock(spec=RestMinimalRef)
    with patch(f"{_REPO_API}.find_by_commit.asyncio", new=AsyncMock(return_value=make_dc_page([ref]))):
        assert await branches.get_by_commit(mock_dc_client, "PRJ", "repo", "abc123") == [ref]


async def test_branches_get_by_commit_multi_page(mock_dc_client, make_dc_page):
    r1, r2 = MagicMock(spec=RestMinimalRef), MagicMock(spec=RestMinimalRef)
    pages = [make_dc_page([r1], is_last=False, next_start=1), make_dc_page([r2])]
    with patch(f"{_REPO_API}.find_by_commit.asyncio", new=AsyncMock(side_effect=pages)):
        assert await branches.get_by_commit(mock_dc_client, "PRJ", "repo", "abc123") == [r1, r2]


async def test_branches_get_by_commit_empty(mock_dc_client, make_dc_page):
    with patch(f"{_REPO_API}.find_by_commit.asyncio", new=AsyncMock(return_value=make_dc_page([]))):
        assert await branches.get_by_commit(mock_dc_client, "PRJ", "repo", "abc123") == []


async def test_branches_get_by_commit_wrong_type_filtered(mock_dc_client, make_dc_page):
    with patch(f"{_REPO_API}.find_by_commit.asyncio", new=AsyncMock(return_value=make_dc_page([MagicMock()]))):
        assert await branches.get_by_commit(mock_dc_client, "PRJ", "repo", "abc123") == []


async def test_branches_get_by_commit_bad_auth_raises(bad_auth_dc_client):
    with patch(f"{_REPO_API}.find_by_commit.asyncio", new=AsyncMock(return_value=None)):
        with pytest.raises(AuthenticationError):
            await branches.get_by_commit(bad_auth_dc_client, "PRJ", "repo", "abc123")


async def test_branches_get_by_commit_basic_auth_accepted(basic_mock_dc_client, make_dc_page):
    ref = MagicMock(spec=RestMinimalRef)
    with patch(f"{_REPO_API}.find_by_commit.asyncio", new=AsyncMock(return_value=make_dc_page([ref]))):
        assert await branches.get_by_commit(basic_mock_dc_client, "PRJ", "repo", "abc123") == [ref]
