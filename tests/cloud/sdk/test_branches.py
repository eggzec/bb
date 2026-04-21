"""Tests for bb.cloud.sdk.branches."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from bb.cloud.models.branch import Branch
from bb.cloud.models.error import Error
from bb.cloud.models.error_error import ErrorError
from bb.cloud.models.tag import Tag
from bb.cloud.sdk import branches
from bb.cloud.sdk._errors import AuthenticationError

_API = "bb.cloud.api.refs"


def _make_error(msg: str = "not found") -> Error:
    return Error(type_="error", error=ErrorError(message=msg))


async def test_list_returns_branches(mock_client, make_page):
    item = MagicMock(spec=Branch)
    with patch(
        f"{_API}.get_repositories_workspace_repo_slug_refs_branches.asyncio",
        new=AsyncMock(return_value=make_page([item])),
    ):
        result = await branches.list(mock_client, "ws", "slug")
    assert result == [item]


async def test_list_empty(mock_client, make_page):
    with patch(
        f"{_API}.get_repositories_workspace_repo_slug_refs_branches.asyncio", new=AsyncMock(return_value=make_page([]))
    ):
        result = await branches.list(mock_client, "ws", "slug")
    assert result == []


async def test_get_returns_branch(mock_client):
    branch = MagicMock(spec=Branch)
    with patch(
        f"{_API}.get_repositories_workspace_repo_slug_refs_branches_name.asyncio", new=AsyncMock(return_value=branch)
    ):
        result = await branches.get(mock_client, "ws", "slug", "main")
    assert result is branch


async def test_get_returns_none(mock_client):
    with patch(
        f"{_API}.get_repositories_workspace_repo_slug_refs_branches_name.asyncio", new=AsyncMock(return_value=None)
    ):
        result = await branches.get(mock_client, "ws", "slug", "main")
    assert result is None


async def test_delete_returns_none(mock_client):
    with patch(
        f"{_API}.delete_repositories_workspace_repo_slug_refs_branches_name.asyncio", new=AsyncMock(return_value=None)
    ):
        result = await branches.delete(mock_client, "ws", "slug", "main")
    assert result is None


async def test_tags_returns_list(mock_client, make_page):
    item = MagicMock(spec=Tag)
    with patch(
        f"{_API}.get_repositories_workspace_repo_slug_refs_tags.asyncio", new=AsyncMock(return_value=make_page([item]))
    ):
        result = await branches.tags(mock_client, "ws", "slug")
    assert result == [item]


async def test_get_tag_returns_tag(mock_client):
    tag = MagicMock(spec=Tag)
    with patch(f"{_API}.get_repositories_workspace_repo_slug_refs_tags_name.asyncio", new=AsyncMock(return_value=tag)):
        result = await branches.get_tag(mock_client, "ws", "slug", "v1.0")
    assert result is tag


async def test_delete_tag_returns_none(mock_client):
    with patch(
        f"{_API}.delete_repositories_workspace_repo_slug_refs_tags_name.asyncio", new=AsyncMock(return_value=None)
    ):
        result = await branches.delete_tag(mock_client, "ws", "slug", "v1.0")
    assert result is None


async def test_get_propagates_error(mock_client):
    err = _make_error("branch not found")
    with patch(
        f"{_API}.get_repositories_workspace_repo_slug_refs_branches_name.asyncio", new=AsyncMock(return_value=err)
    ):
        result = await branches.get(mock_client, "ws", "slug", "main")
    assert result is err
    assert isinstance(result, Error)


async def test_list_raises_on_bad_auth(bad_auth_client):
    with pytest.raises(AuthenticationError):
        await branches.list(bad_auth_client, "ws", "slug")
