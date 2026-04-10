"""Tests for bb.datacenter.sdk.projects."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from bb.datacenter.models.rest_project import RestProject
from bb.datacenter.sdk import projects
from bb.datacenter.sdk._errors import AuthenticationError

_PROJECT_API = "bb.datacenter.api.project"


# ---------------------------------------------------------------------------
# projects.list
# ---------------------------------------------------------------------------


async def test_projects_list_returns_projects(mock_dc_client, make_dc_page):
    project = MagicMock(spec=RestProject)
    with patch(f"{_PROJECT_API}.get_projects.asyncio", new=AsyncMock(return_value=make_dc_page([project]))):
        assert await projects.list(mock_dc_client) == [project]


async def test_projects_list_multi_page(mock_dc_client, make_dc_page):
    p1, p2 = MagicMock(spec=RestProject), MagicMock(spec=RestProject)
    pages = [make_dc_page([p1], is_last=False, next_start=1), make_dc_page([p2])]
    with patch(f"{_PROJECT_API}.get_projects.asyncio", new=AsyncMock(side_effect=pages)):
        assert await projects.list(mock_dc_client) == [p1, p2]


async def test_projects_list_empty(mock_dc_client, make_dc_page):
    with patch(f"{_PROJECT_API}.get_projects.asyncio", new=AsyncMock(return_value=make_dc_page([]))):
        assert await projects.list(mock_dc_client) == []


async def test_projects_list_wrong_type_filtered(mock_dc_client, make_dc_page):
    with patch(f"{_PROJECT_API}.get_projects.asyncio", new=AsyncMock(return_value=make_dc_page([MagicMock()]))):
        assert await projects.list(mock_dc_client) == []


async def test_projects_list_bad_auth_raises(bad_auth_dc_client):
    with patch(f"{_PROJECT_API}.get_projects.asyncio", new=AsyncMock(return_value=None)):
        with pytest.raises(AuthenticationError):
            await projects.list(bad_auth_dc_client)


async def test_projects_list_basic_auth_accepted(basic_mock_dc_client, make_dc_page):
    project = MagicMock(spec=RestProject)
    with patch(f"{_PROJECT_API}.get_projects.asyncio", new=AsyncMock(return_value=make_dc_page([project]))):
        assert await projects.list(basic_mock_dc_client) == [project]


async def test_projects_list_passes_name_filter(mock_dc_client, make_dc_page):
    mock_fn = AsyncMock(return_value=make_dc_page([]))
    with patch(f"{_PROJECT_API}.get_projects.asyncio", new=mock_fn):
        await projects.list(mock_dc_client, name="MyProject")
    assert mock_fn.call_args.kwargs["name"] == "MyProject"


# ---------------------------------------------------------------------------
# projects.get
# ---------------------------------------------------------------------------


async def test_projects_get_returns_project(mock_dc_client):
    project = MagicMock(spec=RestProject)
    with patch(f"{_PROJECT_API}.get_project.asyncio", new=AsyncMock(return_value=project)):
        assert await projects.get(mock_dc_client, "PRJ") is project


async def test_projects_get_none_on_wrong_type(mock_dc_client):
    with patch(f"{_PROJECT_API}.get_project.asyncio", new=AsyncMock(return_value=MagicMock())):
        assert await projects.get(mock_dc_client, "PRJ") is None


async def test_projects_get_none_on_none(mock_dc_client):
    with patch(f"{_PROJECT_API}.get_project.asyncio", new=AsyncMock(return_value=None)):
        assert await projects.get(mock_dc_client, "PRJ") is None


async def test_projects_get_bad_auth_raises(bad_auth_dc_client):
    with patch(f"{_PROJECT_API}.get_project.asyncio", new=AsyncMock(return_value=None)):
        with pytest.raises(AuthenticationError):
            await projects.get(bad_auth_dc_client, "PRJ")


async def test_projects_get_basic_auth_accepted(basic_mock_dc_client):
    project = MagicMock(spec=RestProject)
    with patch(f"{_PROJECT_API}.get_project.asyncio", new=AsyncMock(return_value=project)):
        assert await projects.get(basic_mock_dc_client, "PRJ") is project


# ---------------------------------------------------------------------------
# projects.create
# ---------------------------------------------------------------------------


async def test_projects_create_returns_project(mock_dc_client):
    project = MagicMock(spec=RestProject)
    with patch(f"{_PROJECT_API}.create_project.asyncio", new=AsyncMock(return_value=project)):
        assert await projects.create(mock_dc_client) is project


async def test_projects_create_none_on_wrong_type(mock_dc_client):
    with patch(f"{_PROJECT_API}.create_project.asyncio", new=AsyncMock(return_value=MagicMock())):
        assert await projects.create(mock_dc_client) is None


async def test_projects_create_bad_auth_raises(bad_auth_dc_client):
    with patch(f"{_PROJECT_API}.create_project.asyncio", new=AsyncMock(return_value=None)):
        with pytest.raises(AuthenticationError):
            await projects.create(bad_auth_dc_client)


# ---------------------------------------------------------------------------
# projects.update  (lazy import: update_project)
# ---------------------------------------------------------------------------


async def test_projects_update_returns_project(mock_dc_client):
    project = MagicMock(spec=RestProject)
    with patch(f"{_PROJECT_API}.update_project.asyncio", new=AsyncMock(return_value=project)):
        assert await projects.update(mock_dc_client, "PRJ") is project


async def test_projects_update_none_on_wrong_type(mock_dc_client):
    with patch(f"{_PROJECT_API}.update_project.asyncio", new=AsyncMock(return_value=MagicMock())):
        assert await projects.update(mock_dc_client, "PRJ") is None


async def test_projects_update_passes_body(mock_dc_client):
    project = MagicMock(spec=RestProject)
    mock_fn = AsyncMock(return_value=project)
    body = MagicMock(spec=RestProject)
    with patch(f"{_PROJECT_API}.update_project.asyncio", new=mock_fn):
        await projects.update(mock_dc_client, "PRJ", body=body)
    assert mock_fn.call_args.kwargs["body"] is body


async def test_projects_update_bad_auth_raises(bad_auth_dc_client):
    with patch(f"{_PROJECT_API}.update_project.asyncio", new=AsyncMock(return_value=None)):
        with pytest.raises(AuthenticationError):
            await projects.update(bad_auth_dc_client, "PRJ")


# ---------------------------------------------------------------------------
# projects.delete  (lazy import: delete_project)
# ---------------------------------------------------------------------------


async def test_projects_delete_calls_api(mock_dc_client):
    mock_fn = AsyncMock(return_value=None)
    with patch(f"{_PROJECT_API}.delete_project.asyncio", new=mock_fn):
        await projects.delete(mock_dc_client, "PRJ")
    mock_fn.assert_called_once()


async def test_projects_delete_returns_none(mock_dc_client):
    with patch(f"{_PROJECT_API}.delete_project.asyncio", new=AsyncMock(return_value=None)):
        assert await projects.delete(mock_dc_client, "PRJ") is None


async def test_projects_delete_bad_auth_raises(bad_auth_dc_client):
    with patch(f"{_PROJECT_API}.delete_project.asyncio", new=AsyncMock(return_value=None)):
        with pytest.raises(AuthenticationError):
            await projects.delete(bad_auth_dc_client, "PRJ")
