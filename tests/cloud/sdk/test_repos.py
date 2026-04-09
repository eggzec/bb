"""Tests for bb.cloud.sdk.repos."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from bb.cloud.models.repository import Repository
from bb.cloud.sdk import repos
from bb.cloud.sdk._errors import AuthenticationError

_API = "bb.cloud.api.repositories"


async def test_list_returns_repositories(mock_client, make_page):
    item = MagicMock(spec=Repository)
    with patch(f"{_API}.get_repositories_workspace.asyncio", new=AsyncMock(return_value=make_page([item]))):
        result = await repos.list(mock_client, workspace="ws")
    assert result == [item]


async def test_list_empty_page(mock_client, make_page):
    with patch(f"{_API}.get_repositories_workspace.asyncio", new=AsyncMock(return_value=make_page([]))):
        result = await repos.list(mock_client, workspace="ws")
    assert result == []


async def test_list_none_result(mock_client):
    with patch(f"{_API}.get_repositories_workspace.asyncio", new=AsyncMock(return_value=None)):
        result = await repos.list(mock_client, workspace="ws")
    assert result == []


async def test_get_returns_repository(mock_client):
    repo = MagicMock(spec=Repository)
    with patch(f"{_API}.get_repositories_workspace_repo_slug.asyncio", new=AsyncMock(return_value=repo)):
        result = await repos.get(mock_client, "ws", "slug")
    assert result is repo


async def test_get_returns_none_on_miss(mock_client):
    with patch(f"{_API}.get_repositories_workspace_repo_slug.asyncio", new=AsyncMock(return_value=None)):
        result = await repos.get(mock_client, "ws", "slug")
    assert result is None


async def test_create_returns_repository(mock_client):
    repo = MagicMock(spec=Repository)
    with patch(f"{_API}.post_repositories_workspace_repo_slug.asyncio", new=AsyncMock(return_value=repo)):
        result = await repos.create(mock_client, "ws", "slug")
    assert result is repo


async def test_create_returns_none_on_error(mock_client):
    with patch(f"{_API}.post_repositories_workspace_repo_slug.asyncio", new=AsyncMock(return_value=None)):
        result = await repos.create(mock_client, "ws", "slug")
    assert result is None


async def test_update_returns_repository(mock_client):
    repo = MagicMock(spec=Repository)
    with patch(f"{_API}.put_repositories_workspace_repo_slug.asyncio", new=AsyncMock(return_value=repo)):
        result = await repos.update(mock_client, "ws", "slug")
    assert result is repo


async def test_delete_returns_none(mock_client):
    with patch(f"{_API}.delete_repositories_workspace_repo_slug.asyncio", new=AsyncMock(return_value=None)):
        result = await repos.delete(mock_client, "ws", "slug")
    assert result is None


async def test_fork_returns_repository(mock_client):
    repo = MagicMock(spec=Repository)
    with patch(f"{_API}.post_repositories_workspace_repo_slug_forks.asyncio", new=AsyncMock(return_value=repo)):
        result = await repos.fork(mock_client, "ws", "slug")
    assert result is repo


async def test_forks_returns_list(mock_client, make_page):
    item = MagicMock(spec=Repository)
    with patch(
        f"{_API}.get_repositories_workspace_repo_slug_forks.asyncio", new=AsyncMock(return_value=make_page([item]))
    ):
        result = await repos.forks(mock_client, "ws", "slug")
    assert result == [item]


async def test_watchers_returns_list(mock_client, make_page):
    item = MagicMock(spec=Repository)
    with patch(
        f"{_API}.get_repositories_workspace_repo_slug_watchers.asyncio", new=AsyncMock(return_value=make_page([item]))
    ):
        result = await repos.watchers(mock_client, "ws", "slug")
    assert result == [item]


async def test_my_permissions_returns_list(mock_client, make_page):
    item = MagicMock()
    with patch(f"{_API}.get_user_permissions_repositories.asyncio", new=AsyncMock(return_value=make_page([item]))):
        result = await repos.my_permissions(mock_client)
    assert result == [item]


async def test_list_raises_on_bad_auth(bad_auth_client):
    with pytest.raises(AuthenticationError):
        await repos.list(bad_auth_client, workspace="ws")
