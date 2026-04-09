"""Tests for bb.cloud.sdk.commits."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from bb.cloud.models.base_commit import BaseCommit
from bb.cloud.models.commit import Commit
from bb.cloud.models.pullrequest import Pullrequest
from bb.cloud.sdk import commits
from bb.cloud.sdk._errors import AuthenticationError

_COMMITS = "bb.cloud.api.commits"
_PRS = "bb.cloud.api.pullrequests"


async def test_list_returns_commits(mock_client, make_page):
    item = MagicMock(spec=BaseCommit)
    with patch(
        f"{_COMMITS}.get_repositories_workspace_repo_slug_commits.asyncio",
        new=AsyncMock(return_value=make_page([item])),
    ):
        result = await commits.list(mock_client, "ws", "slug")
    assert result == [item]


async def test_list_empty(mock_client, make_page):
    with patch(
        f"{_COMMITS}.get_repositories_workspace_repo_slug_commits.asyncio", new=AsyncMock(return_value=make_page([]))
    ):
        result = await commits.list(mock_client, "ws", "slug")
    assert result == []


async def test_get_returns_commit(mock_client):
    commit = MagicMock(spec=Commit)
    with patch(
        f"{_COMMITS}.get_repositories_workspace_repo_slug_commit_commit.asyncio", new=AsyncMock(return_value=commit)
    ):
        result = await commits.get(mock_client, "ws", "slug", "abc123")
    assert result is commit


async def test_get_returns_none(mock_client):
    with patch(
        f"{_COMMITS}.get_repositories_workspace_repo_slug_commit_commit.asyncio", new=AsyncMock(return_value=None)
    ):
        result = await commits.get(mock_client, "ws", "slug", "abc123")
    assert result is None


async def test_prs_returns_list(mock_client, make_page):
    item = MagicMock(spec=Pullrequest)
    with patch(f"{_PRS}.get_pullrequests_for_commit.asyncio", new=AsyncMock(return_value=make_page([item]))):
        result = await commits.prs(mock_client, "ws", "slug", "abc123")
    assert result == [item]


async def test_list_raises_on_bad_auth(bad_auth_client):
    with pytest.raises(AuthenticationError):
        await commits.list(bad_auth_client, "ws", "slug")
