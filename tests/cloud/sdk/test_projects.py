"""Tests for bb.cloud.sdk.projects."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from bb.cloud.models.project import Project
from bb.cloud.sdk import projects
from bb.cloud.sdk._errors import AuthenticationError

_API = "bb.cloud.api.projects"
_WS_API = "bb.cloud.api.workspaces"


async def test_list_returns_projects(mock_client, make_page):
    item = MagicMock(spec=Project)
    with patch(f"{_WS_API}.get_workspaces_workspace_projects.asyncio", new=AsyncMock(return_value=make_page([item]))):
        result = await projects.list(mock_client, "ws")
    assert result == [item]


async def test_list_empty(mock_client, make_page):
    with patch(f"{_WS_API}.get_workspaces_workspace_projects.asyncio", new=AsyncMock(return_value=make_page([]))):
        result = await projects.list(mock_client, "ws")
    assert result == []


async def test_get_returns_project(mock_client):
    project = MagicMock(spec=Project)
    with patch(f"{_API}.get_workspaces_workspace_projects_project_key.asyncio", new=AsyncMock(return_value=project)):
        result = await projects.get(mock_client, "ws", "PROJ")
    assert result is project


async def test_get_returns_none(mock_client):
    with patch(f"{_API}.get_workspaces_workspace_projects_project_key.asyncio", new=AsyncMock(return_value=None)):
        result = await projects.get(mock_client, "ws", "PROJ")
    assert result is None


async def test_create_returns_project(mock_client):
    project = MagicMock(spec=Project)
    with patch(f"{_API}.post_workspaces_workspace_projects.asyncio", new=AsyncMock(return_value=project)):
        result = await projects.create(mock_client, "ws")
    assert result is project


async def test_update_returns_project(mock_client):
    project = MagicMock(spec=Project)
    with patch(f"{_API}.put_workspaces_workspace_projects_project_key.asyncio", new=AsyncMock(return_value=project)):
        result = await projects.update(mock_client, "ws", "PROJ")
    assert result is project


async def test_delete_returns_none(mock_client):
    with patch(f"{_API}.delete_workspaces_workspace_projects_project_key.asyncio", new=AsyncMock(return_value=None)):
        result = await projects.delete(mock_client, "ws", "PROJ")
    assert result is None


async def test_default_reviewers_returns_list(mock_client, make_page):
    item = MagicMock()
    with patch(
        f"{_API}.get_workspaces_workspace_projects_project_key_default_reviewers.asyncio",
        new=AsyncMock(return_value=make_page([item])),
    ):
        result = await projects.default_reviewers(mock_client, "ws", "PROJ")
    assert result == [item]


async def test_group_permissions_returns_list(mock_client, make_page):
    item = MagicMock()
    with patch(
        f"{_API}.get_workspaces_workspace_projects_project_key_permissions_config_groups.asyncio",
        new=AsyncMock(return_value=make_page([item])),
    ):
        result = await projects.group_permissions(mock_client, "ws", "PROJ")
    assert result == [item]


async def test_user_permissions_returns_list(mock_client, make_page):
    item = MagicMock()
    with patch(
        f"{_API}.get_workspaces_workspace_projects_project_key_permissions_config_users.asyncio",
        new=AsyncMock(return_value=make_page([item])),
    ):
        result = await projects.user_permissions(mock_client, "ws", "PROJ")
    assert result == [item]


async def test_list_raises_on_bad_auth(bad_auth_client):
    with pytest.raises(AuthenticationError):
        await projects.list(bad_auth_client, "ws")
