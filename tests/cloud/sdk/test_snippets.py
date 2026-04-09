"""Tests for bb.cloud.sdk.snippets."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from bb.cloud.models.snippet import Snippet
from bb.cloud.models.snippet_comment import SnippetComment
from bb.cloud.models.snippet_commit import SnippetCommit
from bb.cloud.sdk import snippets
from bb.cloud.sdk._errors import AuthenticationError

_API = "bb.cloud.api.snippets"


async def test_list_returns_snippets(mock_client, make_page):
    item = MagicMock(spec=Snippet)
    with patch(f"{_API}.get_snippets_workspace.asyncio", new=AsyncMock(return_value=make_page([item]))):
        result = await snippets.list(mock_client, "ws")
    assert result == [item]


async def test_list_empty(mock_client, make_page):
    with patch(f"{_API}.get_snippets_workspace.asyncio", new=AsyncMock(return_value=make_page([]))):
        result = await snippets.list(mock_client, "ws")
    assert result == []


async def test_get_returns_snippet(mock_client):
    snippet = MagicMock(spec=Snippet)
    with patch(f"{_API}.get_snippets_workspace_encoded_id.asyncio", new=AsyncMock(return_value=snippet)):
        result = await snippets.get(mock_client, "ws", "abc")
    assert result is snippet


async def test_get_returns_none(mock_client):
    with patch(f"{_API}.get_snippets_workspace_encoded_id.asyncio", new=AsyncMock(return_value=None)):
        result = await snippets.get(mock_client, "ws", "abc")
    assert result is None


async def test_create_returns_snippet(mock_client):
    snippet = MagicMock(spec=Snippet)
    with patch(f"{_API}.post_snippets_workspace.asyncio", new=AsyncMock(return_value=snippet)):
        result = await snippets.create(mock_client, "ws")
    assert result is snippet


async def test_update_returns_snippet(mock_client):
    snippet = MagicMock(spec=Snippet)
    with patch(f"{_API}.put_snippets_workspace_encoded_id.asyncio", new=AsyncMock(return_value=snippet)):
        result = await snippets.update(mock_client, "ws", "abc")
    assert result is snippet


async def test_delete_returns_none(mock_client):
    with patch(f"{_API}.delete_snippets_workspace_encoded_id.asyncio", new=AsyncMock(return_value=None)):
        result = await snippets.delete(mock_client, "ws", "abc")
    assert result is None


async def test_comments_returns_list(mock_client, make_page):
    item = MagicMock(spec=SnippetComment)
    with patch(
        f"{_API}.get_snippets_workspace_encoded_id_comments.asyncio", new=AsyncMock(return_value=make_page([item]))
    ):
        result = await snippets.comments(mock_client, "ws", "abc")
    assert result == [item]


async def test_commits_returns_list(mock_client, make_page):
    item = MagicMock(spec=SnippetCommit)
    with patch(
        f"{_API}.get_snippets_workspace_encoded_id_commits.asyncio", new=AsyncMock(return_value=make_page([item]))
    ):
        result = await snippets.commits(mock_client, "ws", "abc")
    assert result == [item]


async def test_watch_returns_none(mock_client):
    with patch(f"{_API}.put_snippets_workspace_encoded_id_watch.asyncio", new=AsyncMock(return_value=None)):
        result = await snippets.watch(mock_client, "ws", "abc")
    assert result is None


async def test_unwatch_returns_none(mock_client):
    with patch(f"{_API}.delete_snippets_workspace_encoded_id_watch.asyncio", new=AsyncMock(return_value=None)):
        result = await snippets.unwatch(mock_client, "ws", "abc")
    assert result is None


async def test_watchers_returns_list(mock_client, make_page):
    item = MagicMock()
    with patch(
        f"{_API}.get_snippets_workspace_encoded_id_watchers.asyncio", new=AsyncMock(return_value=make_page([item]))
    ):
        result = await snippets.watchers(mock_client, "ws", "abc")
    assert result == [item]


async def test_list_all_returns_snippets(mock_client, make_page):
    item = MagicMock(spec=Snippet)
    with patch(f"{_API}.get_snippets.asyncio", new=AsyncMock(return_value=make_page([item]))):
        result = await snippets.list_all(mock_client)
    assert result == [item]


async def test_list_raises_on_bad_auth(bad_auth_client):
    with pytest.raises(AuthenticationError):
        await snippets.list(bad_auth_client, "ws")
