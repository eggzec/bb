"""Tests for bb.cloud.sdk.downloads."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from bb.cloud.sdk import downloads
from bb.cloud.sdk._errors import AuthenticationError

_API = "bb.cloud.api.downloads"


async def test_list_returns_downloads(mock_client, make_page):
    item = MagicMock()
    with patch(
        f"{_API}.get_repositories_workspace_repo_slug_downloads.asyncio", new=AsyncMock(return_value=make_page([item]))
    ):
        result = await downloads.list(mock_client, "ws", "slug")
    assert result == [item]


async def test_list_empty(mock_client, make_page):
    with patch(
        f"{_API}.get_repositories_workspace_repo_slug_downloads.asyncio", new=AsyncMock(return_value=make_page([]))
    ):
        result = await downloads.list(mock_client, "ws", "slug")
    assert result == []


async def test_get_returns_download(mock_client):
    dl = MagicMock()
    with patch(
        f"{_API}.get_repositories_workspace_repo_slug_downloads_filename.asyncio", new=AsyncMock(return_value=dl)
    ):
        result = await downloads.get(mock_client, "ws", "slug", "file.zip")
    assert result is dl


async def test_get_returns_none(mock_client):
    with patch(
        f"{_API}.get_repositories_workspace_repo_slug_downloads_filename.asyncio", new=AsyncMock(return_value=None)
    ):
        result = await downloads.get(mock_client, "ws", "slug", "file.zip")
    assert result is None


async def test_upload_returns_result(mock_client):
    upload_result = MagicMock()
    with patch(
        f"{_API}.post_repositories_workspace_repo_slug_downloads.asyncio", new=AsyncMock(return_value=upload_result)
    ):
        result = await downloads.upload(mock_client, "ws", "slug")
    assert result is upload_result


async def test_delete_returns_none(mock_client):
    with patch(
        f"{_API}.delete_repositories_workspace_repo_slug_downloads_filename.asyncio", new=AsyncMock(return_value=None)
    ):
        result = await downloads.delete(mock_client, "ws", "slug", "file.zip")
    assert result is None


async def test_list_raises_on_bad_auth(bad_auth_client):
    with pytest.raises(AuthenticationError):
        await downloads.list(bad_auth_client, "ws", "slug")
