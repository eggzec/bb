"""Tests for bb.datacenter.sdk.commits."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from bb.datacenter.models.rest_commit import RestCommit
from bb.datacenter.sdk import commits
from bb.datacenter.sdk._errors import AuthenticationError

_REPO_API = "bb.datacenter.api.repository"


# ---------------------------------------------------------------------------
# commits.list
# ---------------------------------------------------------------------------


async def test_commits_list_returns_commits(mock_dc_client, make_dc_page):
    commit = MagicMock(spec=RestCommit)
    with patch(f"{_REPO_API}.get_commits.asyncio", new=AsyncMock(return_value=make_dc_page([commit]))):
        assert await commits.list(mock_dc_client, "PRJ", "repo") == [commit]


async def test_commits_list_multi_page(mock_dc_client, make_dc_page):
    c1, c2 = MagicMock(spec=RestCommit), MagicMock(spec=RestCommit)
    pages = [make_dc_page([c1], is_last=False, next_start=1), make_dc_page([c2])]
    with patch(f"{_REPO_API}.get_commits.asyncio", new=AsyncMock(side_effect=pages)):
        assert await commits.list(mock_dc_client, "PRJ", "repo") == [c1, c2]


async def test_commits_list_empty(mock_dc_client, make_dc_page):
    with patch(f"{_REPO_API}.get_commits.asyncio", new=AsyncMock(return_value=make_dc_page([]))):
        assert await commits.list(mock_dc_client, "PRJ", "repo") == []


async def test_commits_list_wrong_type_filtered(mock_dc_client, make_dc_page):
    with patch(f"{_REPO_API}.get_commits.asyncio", new=AsyncMock(return_value=make_dc_page([MagicMock()]))):
        assert await commits.list(mock_dc_client, "PRJ", "repo") == []


async def test_commits_list_bad_auth_raises(bad_auth_dc_client):
    with patch(f"{_REPO_API}.get_commits.asyncio", new=AsyncMock(return_value=None)):
        with pytest.raises(AuthenticationError):
            await commits.list(bad_auth_dc_client, "PRJ", "repo")


async def test_commits_list_basic_auth_accepted(basic_mock_dc_client, make_dc_page):
    commit = MagicMock(spec=RestCommit)
    with patch(f"{_REPO_API}.get_commits.asyncio", new=AsyncMock(return_value=make_dc_page([commit]))):
        assert await commits.list(basic_mock_dc_client, "PRJ", "repo") == [commit]


# ---------------------------------------------------------------------------
# commits.get
# ---------------------------------------------------------------------------


async def test_commits_get_returns_commit(mock_dc_client):
    commit = MagicMock(spec=RestCommit)
    with patch(f"{_REPO_API}.get_commit.asyncio", new=AsyncMock(return_value=commit)):
        assert await commits.get(mock_dc_client, "PRJ", "repo", "abc123") is commit


async def test_commits_get_none_on_wrong_type(mock_dc_client):
    with patch(f"{_REPO_API}.get_commit.asyncio", new=AsyncMock(return_value=MagicMock())):
        assert await commits.get(mock_dc_client, "PRJ", "repo", "abc123") is None


async def test_commits_get_none_on_none_response(mock_dc_client):
    with patch(f"{_REPO_API}.get_commit.asyncio", new=AsyncMock(return_value=None)):
        assert await commits.get(mock_dc_client, "PRJ", "repo", "abc123") is None


async def test_commits_get_bad_auth_raises(bad_auth_dc_client):
    with patch(f"{_REPO_API}.get_commit.asyncio", new=AsyncMock(return_value=None)):
        with pytest.raises(AuthenticationError):
            await commits.get(bad_auth_dc_client, "PRJ", "repo", "abc123")


async def test_commits_get_basic_auth_accepted(basic_mock_dc_client):
    commit = MagicMock(spec=RestCommit)
    with patch(f"{_REPO_API}.get_commit.asyncio", new=AsyncMock(return_value=commit)):
        assert await commits.get(basic_mock_dc_client, "PRJ", "repo", "abc123") is commit


async def test_commits_get_passes_commit_id(mock_dc_client):
    commit = MagicMock(spec=RestCommit)
    mock_fn = AsyncMock(return_value=commit)
    with patch(f"{_REPO_API}.get_commit.asyncio", new=mock_fn):
        await commits.get(mock_dc_client, "PRJ", "repo", "deadbeef")
    assert mock_fn.call_args.args[2] == "deadbeef"
