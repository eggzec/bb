"""Tests for bb.cloud.sdk.source."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from bb.cloud.sdk import source
from bb.cloud.sdk._errors import AuthenticationError

_API = "bb.cloud.api.source"


async def test_get_returns_content(mock_client):
    content = MagicMock()
    with patch(
        f"{_API}.get_repositories_workspace_repo_slug_src_commit_path.asyncio", new=AsyncMock(return_value=content)
    ):
        result = await source.get(mock_client, "ws", "slug", "abc123", "README.md")
    assert result is content


async def test_get_returns_none(mock_client):
    with patch(
        f"{_API}.get_repositories_workspace_repo_slug_src_commit_path.asyncio", new=AsyncMock(return_value=None)
    ):
        result = await source.get(mock_client, "ws", "slug", "abc123", "README.md")
    assert result is None


async def test_root_returns_tree(mock_client):
    tree = MagicMock()
    with patch(f"{_API}.get_repositories_workspace_repo_slug_src.asyncio", new=AsyncMock(return_value=tree)):
        result = await source.root(mock_client, "ws", "slug")
    assert result is tree


async def test_root_returns_none(mock_client):
    with patch(f"{_API}.get_repositories_workspace_repo_slug_src.asyncio", new=AsyncMock(return_value=None)):
        result = await source.root(mock_client, "ws", "slug")
    assert result is None


async def test_history_returns_list(mock_client):
    history = MagicMock()
    with patch(
        f"{_API}.get_repositories_workspace_repo_slug_filehistory_commit_path.asyncio",
        new=AsyncMock(return_value=history),
    ):
        result = await source.history(mock_client, "ws", "slug", "abc123", "README.md")
    assert result is history


async def test_upload_returns_result(mock_client):
    upload = MagicMock()
    with patch(f"{_API}.post_repositories_workspace_repo_slug_src.asyncio", new=AsyncMock(return_value=upload)):
        result = await source.upload(mock_client, "ws", "slug")
    assert result is upload


async def test_get_raises_on_bad_auth(bad_auth_client):
    with pytest.raises(AuthenticationError):
        await source.get(bad_auth_client, "ws", "slug", "abc123", "README.md")
