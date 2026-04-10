"""Tests for bb.datacenter.sdk.repos."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from bb.datacenter.models.rest_repository import RestRepository
from bb.datacenter.sdk import repos
from bb.datacenter.sdk._errors import AuthenticationError

_PROJECT_API = "bb.datacenter.api.project"
_REPO_API = "bb.datacenter.api.repository"


# ---------------------------------------------------------------------------
# repos.list
# ---------------------------------------------------------------------------


async def test_repos_list_returns_repos(mock_dc_client, make_dc_page):
    repo = MagicMock(spec=RestRepository)
    with patch(f"{_PROJECT_API}.get_repositories.asyncio", new=AsyncMock(return_value=make_dc_page([repo]))):
        assert await repos.list(mock_dc_client, "PRJ") == [repo]


async def test_repos_list_multi_page(mock_dc_client, make_dc_page):
    r1, r2 = MagicMock(spec=RestRepository), MagicMock(spec=RestRepository)
    pages = [make_dc_page([r1], is_last=False, next_start=1), make_dc_page([r2])]
    with patch(f"{_PROJECT_API}.get_repositories.asyncio", new=AsyncMock(side_effect=pages)):
        assert await repos.list(mock_dc_client, "PRJ") == [r1, r2]


async def test_repos_list_empty(mock_dc_client, make_dc_page):
    with patch(f"{_PROJECT_API}.get_repositories.asyncio", new=AsyncMock(return_value=make_dc_page([]))):
        assert await repos.list(mock_dc_client, "PRJ") == []


async def test_repos_list_wrong_type_filtered(mock_dc_client, make_dc_page):
    with patch(f"{_PROJECT_API}.get_repositories.asyncio", new=AsyncMock(return_value=make_dc_page([MagicMock()]))):
        assert await repos.list(mock_dc_client, "PRJ") == []


async def test_repos_list_bad_auth_raises(bad_auth_dc_client):
    with patch(f"{_PROJECT_API}.get_repositories.asyncio", new=AsyncMock(return_value=None)):
        with pytest.raises(AuthenticationError):
            await repos.list(bad_auth_dc_client, "PRJ")


async def test_repos_list_basic_auth_accepted(basic_mock_dc_client, make_dc_page):
    repo = MagicMock(spec=RestRepository)
    with patch(f"{_PROJECT_API}.get_repositories.asyncio", new=AsyncMock(return_value=make_dc_page([repo]))):
        assert await repos.list(basic_mock_dc_client, "PRJ") == [repo]


# ---------------------------------------------------------------------------
# repos.list_all
# ---------------------------------------------------------------------------


async def test_repos_list_all_returns_repos(mock_dc_client, make_dc_page):
    repo = MagicMock(spec=RestRepository)
    with patch(f"{_REPO_API}.get_repositories_1.asyncio", new=AsyncMock(return_value=make_dc_page([repo]))):
        assert await repos.list_all(mock_dc_client) == [repo]


async def test_repos_list_all_bad_auth_raises(bad_auth_dc_client):
    with patch(f"{_REPO_API}.get_repositories_1.asyncio", new=AsyncMock(return_value=None)):
        with pytest.raises(AuthenticationError):
            await repos.list_all(bad_auth_dc_client)


async def test_repos_list_all_passes_name_and_permission(mock_dc_client, make_dc_page):
    mock_fn = AsyncMock(return_value=make_dc_page([]))
    with patch(f"{_REPO_API}.get_repositories_1.asyncio", new=mock_fn):
        await repos.list_all(mock_dc_client, name="myrepo", permission="REPO_READ")
    assert mock_fn.call_args.kwargs["name"] == "myrepo"
    assert mock_fn.call_args.kwargs["permission"] == "REPO_READ"


# ---------------------------------------------------------------------------
# repos.get
# ---------------------------------------------------------------------------


async def test_repos_get_returns_repo(mock_dc_client):
    repo = MagicMock(spec=RestRepository)
    with patch(f"{_PROJECT_API}.get_repository.asyncio", new=AsyncMock(return_value=repo)):
        assert await repos.get(mock_dc_client, "PRJ", "myrepo") is repo


async def test_repos_get_none_on_wrong_type(mock_dc_client):
    with patch(f"{_PROJECT_API}.get_repository.asyncio", new=AsyncMock(return_value=MagicMock())):
        assert await repos.get(mock_dc_client, "PRJ", "myrepo") is None


async def test_repos_get_none_on_none(mock_dc_client):
    with patch(f"{_PROJECT_API}.get_repository.asyncio", new=AsyncMock(return_value=None)):
        assert await repos.get(mock_dc_client, "PRJ", "myrepo") is None


async def test_repos_get_bad_auth_raises(bad_auth_dc_client):
    with patch(f"{_PROJECT_API}.get_repository.asyncio", new=AsyncMock(return_value=None)):
        with pytest.raises(AuthenticationError):
            await repos.get(bad_auth_dc_client, "PRJ", "myrepo")


async def test_repos_get_basic_auth_accepted(basic_mock_dc_client):
    repo = MagicMock(spec=RestRepository)
    with patch(f"{_PROJECT_API}.get_repository.asyncio", new=AsyncMock(return_value=repo)):
        assert await repos.get(basic_mock_dc_client, "PRJ", "myrepo") is repo


# ---------------------------------------------------------------------------
# repos.create
# ---------------------------------------------------------------------------


async def test_repos_create_returns_repo(mock_dc_client):
    repo = MagicMock(spec=RestRepository)
    with patch(f"{_PROJECT_API}.create_repository.asyncio", new=AsyncMock(return_value=repo)):
        assert await repos.create(mock_dc_client, "PRJ") is repo


async def test_repos_create_none_on_wrong_type(mock_dc_client):
    with patch(f"{_PROJECT_API}.create_repository.asyncio", new=AsyncMock(return_value=MagicMock())):
        assert await repos.create(mock_dc_client, "PRJ") is None


async def test_repos_create_bad_auth_raises(bad_auth_dc_client):
    with patch(f"{_PROJECT_API}.create_repository.asyncio", new=AsyncMock(return_value=None)):
        with pytest.raises(AuthenticationError):
            await repos.create(bad_auth_dc_client, "PRJ")


# ---------------------------------------------------------------------------
# repos.update
# ---------------------------------------------------------------------------


async def test_repos_update_returns_repo(mock_dc_client):
    repo = MagicMock(spec=RestRepository)
    with patch(f"{_PROJECT_API}.update_repository.asyncio", new=AsyncMock(return_value=repo)):
        assert await repos.update(mock_dc_client, "PRJ", "myrepo") is repo


async def test_repos_update_none_on_wrong_type(mock_dc_client):
    with patch(f"{_PROJECT_API}.update_repository.asyncio", new=AsyncMock(return_value=MagicMock())):
        assert await repos.update(mock_dc_client, "PRJ", "myrepo") is None


async def test_repos_update_bad_auth_raises(bad_auth_dc_client):
    with patch(f"{_PROJECT_API}.update_repository.asyncio", new=AsyncMock(return_value=None)):
        with pytest.raises(AuthenticationError):
            await repos.update(bad_auth_dc_client, "PRJ", "myrepo")


# ---------------------------------------------------------------------------
# repos.delete
# ---------------------------------------------------------------------------


async def test_repos_delete_calls_api(mock_dc_client):
    mock_fn = AsyncMock(return_value=None)
    with patch(f"{_PROJECT_API}.delete_repository.asyncio", new=mock_fn):
        await repos.delete(mock_dc_client, "PRJ", "myrepo")
    mock_fn.assert_called_once()


async def test_repos_delete_returns_none(mock_dc_client):
    with patch(f"{_PROJECT_API}.delete_repository.asyncio", new=AsyncMock(return_value=None)):
        assert await repos.delete(mock_dc_client, "PRJ", "myrepo") is None


async def test_repos_delete_bad_auth_raises(bad_auth_dc_client):
    with patch(f"{_PROJECT_API}.delete_repository.asyncio", new=AsyncMock(return_value=None)):
        with pytest.raises(AuthenticationError):
            await repos.delete(bad_auth_dc_client, "PRJ", "myrepo")
