"""Tests for bb.cloud.sdk.source."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from bb.cloud.sdk import source
from bb.cloud.sdk._errors import AuthenticationError

_API = "bb.cloud.api.source"


async def test_get_returns_parsed_on_json_response(mock_client):
    """On 200 with application/json content-type, return response.parsed."""
    expected = MagicMock()
    mock_resp = MagicMock()
    mock_resp.status_code.value = 200
    mock_resp.headers.get.return_value = "application/json; charset=utf-8"
    mock_resp.parsed = expected
    with patch(
        f"{_API}.get_repositories_workspace_repo_slug_src_commit_path.asyncio_detailed",
        new=AsyncMock(return_value=mock_resp),
    ):
        result = await source.get(mock_client, "ws", "slug", "abc123", "README.md")
    assert result is expected


async def test_get_returns_decoded_on_raw_response(mock_client):
    """On 200 with non-JSON content-type, return decoded bytes."""
    mock_resp = MagicMock()
    mock_resp.status_code.value = 200
    mock_resp.headers.get.return_value = "text/plain"
    mock_resp.content = b"file content here"
    with patch(
        f"{_API}.get_repositories_workspace_repo_slug_src_commit_path.asyncio_detailed",
        new=AsyncMock(return_value=mock_resp),
    ):
        result = await source.get(mock_client, "ws", "slug", "abc123", "README.md")
    assert result == "file content here"


async def test_get_returns_none_on_non_200(mock_client):
    """On non-200 status, return response.parsed (None when resource not found)."""
    mock_resp = MagicMock()
    mock_resp.status_code.value = 404
    mock_resp.parsed = None
    with patch(
        f"{_API}.get_repositories_workspace_repo_slug_src_commit_path.asyncio_detailed",
        new=AsyncMock(return_value=mock_resp),
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
