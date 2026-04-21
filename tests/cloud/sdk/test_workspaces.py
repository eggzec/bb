"""Tests for bb.cloud.sdk.workspaces."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from bb.cloud.models.error import Error
from bb.cloud.models.error_error import ErrorError
from bb.cloud.models.workspace import Workspace
from bb.cloud.sdk import workspaces
from bb.cloud.sdk._errors import AuthenticationError


def _make_error(msg: str = "not found") -> Error:
    return Error(type_="error", error=ErrorError(message=msg))


_API = "bb.cloud.api.workspaces"


async def test_list_returns_workspaces(mock_client, make_page):
    item = MagicMock(spec=Workspace)
    with patch(f"{_API}.get_workspaces.asyncio", new=AsyncMock(return_value=make_page([item]))):
        result = await workspaces.list(mock_client)
    assert result == [item]


async def test_list_empty(mock_client, make_page):
    with patch(f"{_API}.get_workspaces.asyncio", new=AsyncMock(return_value=make_page([]))):
        result = await workspaces.list(mock_client)
    assert result == []


async def test_get_returns_workspace(mock_client):
    ws = MagicMock(spec=Workspace)
    with patch(f"{_API}.get_workspaces_workspace.asyncio", new=AsyncMock(return_value=ws)):
        result = await workspaces.get(mock_client, "ws")
    assert result is ws


async def test_get_returns_none(mock_client):
    with patch(f"{_API}.get_workspaces_workspace.asyncio", new=AsyncMock(return_value=None)):
        result = await workspaces.get(mock_client, "ws")
    assert result is None


async def test_members_returns_list(mock_client, make_page):
    item = MagicMock()
    with patch(f"{_API}.get_workspaces_workspace_members.asyncio", new=AsyncMock(return_value=make_page([item]))):
        result = await workspaces.members(mock_client, "ws")
    assert result == [item]


async def test_get_member_returns_member(mock_client):
    member = MagicMock()
    with patch(f"{_API}.get_workspaces_workspace_members_member.asyncio", new=AsyncMock(return_value=member)):
        result = await workspaces.get_member(mock_client, "ws", "user1")
    assert result is member


async def test_permissions_returns_list(mock_client, make_page):
    item = MagicMock()
    with patch(f"{_API}.get_workspaces_workspace_permissions.asyncio", new=AsyncMock(return_value=make_page([item]))):
        result = await workspaces.permissions(mock_client, "ws")
    assert result == [item]


async def test_repo_permissions_returns_list(mock_client, make_page):
    item = MagicMock()
    with patch(
        f"{_API}.get_workspaces_workspace_permissions_repositories.asyncio",
        new=AsyncMock(return_value=make_page([item])),
    ):
        result = await workspaces.repo_permissions(mock_client, "ws")
    assert result == [item]


async def test_get_repo_permission_returns_permission(mock_client):
    perm = MagicMock()
    with patch(
        f"{_API}.get_workspaces_workspace_permissions_repositories_repo_slug.asyncio", new=AsyncMock(return_value=perm)
    ):
        result = await workspaces.get_repo_permission(mock_client, "ws", "slug")
    assert result is perm


async def test_user_prs_returns_list(mock_client, make_page):
    item = MagicMock()
    with patch(
        f"{_API}.get_workspaces_workspace_pullrequests_selected_user.asyncio",
        new=AsyncMock(return_value=make_page([item])),
    ):
        result = await workspaces.user_prs(mock_client, "ws", "user1")
    assert result == [item]


async def test_mine_returns_workspaces(mock_client, make_page):
    item = MagicMock(spec=Workspace)
    with patch(f"{_API}.get_user_workspaces.asyncio", new=AsyncMock(return_value=make_page([item]))):
        result = await workspaces.mine(mock_client)
    assert result == [item]


async def test_my_permissions_returns_list(mock_client, make_page):
    item = MagicMock()
    with patch(f"{_API}.get_user_permissions_workspaces.asyncio", new=AsyncMock(return_value=make_page([item]))):
        result = await workspaces.my_permissions(mock_client)
    assert result == [item]


async def test_my_permission_returns_permission(mock_client):
    perm = MagicMock()
    with patch(f"{_API}.get_user_workspaces_workspace_permission.asyncio", new=AsyncMock(return_value=perm)):
        result = await workspaces.my_permission(mock_client, "ws")
    assert result is perm


async def test_get_propagates_error(mock_client):
    err = _make_error("workspace not found")
    with patch(f"{_API}.get_workspaces_workspace.asyncio", new=AsyncMock(return_value=err)):
        result = await workspaces.get(mock_client, "myws")
    assert result is err
    assert isinstance(result, Error)


async def test_list_raises_on_bad_auth(bad_auth_client):
    with pytest.raises(AuthenticationError):
        await workspaces.list(bad_auth_client)
