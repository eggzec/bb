"""Tests for bb.cloud.sdk.branch_restrictions."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from bb.cloud.models.branchrestriction import Branchrestriction
from bb.cloud.sdk import branch_restrictions
from bb.cloud.sdk._errors import AuthenticationError

_API = "bb.cloud.api.branch_restrictions"


async def test_list_returns_restrictions(mock_client, make_page):
    item = MagicMock(spec=Branchrestriction)
    with patch(
        f"{_API}.get_repositories_workspace_repo_slug_branch_restrictions.asyncio",
        new=AsyncMock(return_value=make_page([item])),
    ):
        result = await branch_restrictions.list(mock_client, "ws", "slug")
    assert result == [item]


async def test_list_empty(mock_client, make_page):
    with patch(
        f"{_API}.get_repositories_workspace_repo_slug_branch_restrictions.asyncio",
        new=AsyncMock(return_value=make_page([])),
    ):
        result = await branch_restrictions.list(mock_client, "ws", "slug")
    assert result == []


async def test_get_returns_restriction(mock_client):
    restriction = MagicMock(spec=Branchrestriction)
    with patch(
        f"{_API}.get_repositories_workspace_repo_slug_branch_restrictions_id.asyncio",
        new=AsyncMock(return_value=restriction),
    ):
        result = await branch_restrictions.get(mock_client, "ws", "slug", 42)
    assert result is restriction


async def test_get_returns_none(mock_client):
    with patch(
        f"{_API}.get_repositories_workspace_repo_slug_branch_restrictions_id.asyncio", new=AsyncMock(return_value=None)
    ):
        result = await branch_restrictions.get(mock_client, "ws", "slug", 42)
    assert result is None


async def test_create_returns_restriction(mock_client):
    restriction = MagicMock(spec=Branchrestriction)
    with patch(
        f"{_API}.post_repositories_workspace_repo_slug_branch_restrictions.asyncio",
        new=AsyncMock(return_value=restriction),
    ):
        result = await branch_restrictions.create(mock_client, "ws", "slug")
    assert result is restriction


async def test_update_returns_restriction(mock_client):
    restriction = MagicMock(spec=Branchrestriction)
    with patch(
        f"{_API}.put_repositories_workspace_repo_slug_branch_restrictions_id.asyncio",
        new=AsyncMock(return_value=restriction),
    ):
        result = await branch_restrictions.update(mock_client, "ws", "slug", 42)
    assert result is restriction


async def test_delete_returns_none(mock_client):
    with patch(
        f"{_API}.delete_repositories_workspace_repo_slug_branch_restrictions_id.asyncio",
        new=AsyncMock(return_value=None),
    ):
        result = await branch_restrictions.delete(mock_client, "ws", "slug", 42)
    assert result is None


async def test_list_raises_on_bad_auth(bad_auth_client):
    with pytest.raises(AuthenticationError):
        await branch_restrictions.list(bad_auth_client, "ws", "slug")
