"""Tests for bb.cloud.sdk.commit_statuses."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from bb.cloud.models.commitstatus import Commitstatus
from bb.cloud.sdk import commit_statuses
from bb.cloud.sdk._errors import AuthenticationError

_API = "bb.cloud.api.commit_statuses"


async def test_list_returns_statuses(mock_client, make_page):
    item = MagicMock(spec=Commitstatus)
    with patch(
        f"{_API}.get_repositories_workspace_repo_slug_commit_commit_statuses.asyncio",
        new=AsyncMock(return_value=make_page([item])),
    ):
        result = await commit_statuses.list(mock_client, "ws", "slug", "abc")
    assert result == [item]


async def test_get_returns_status(mock_client):
    status = MagicMock(spec=Commitstatus)
    with patch(
        f"{_API}.get_repositories_workspace_repo_slug_commit_commit_statuses_build_key.asyncio",
        new=AsyncMock(return_value=status),
    ):
        result = await commit_statuses.get(mock_client, "ws", "slug", "abc", "my-key")
    assert result is status


async def test_get_returns_none(mock_client):
    with patch(
        f"{_API}.get_repositories_workspace_repo_slug_commit_commit_statuses_build_key.asyncio",
        new=AsyncMock(return_value=None),
    ):
        result = await commit_statuses.get(mock_client, "ws", "slug", "abc", "my-key")
    assert result is None


async def test_create_returns_status(mock_client):
    status = MagicMock(spec=Commitstatus)
    with patch(
        f"{_API}.post_repositories_workspace_repo_slug_commit_commit_statuses_build.asyncio",
        new=AsyncMock(return_value=status),
    ):
        result = await commit_statuses.create(mock_client, "ws", "slug", "abc")
    assert result is status


async def test_update_returns_status(mock_client):
    status = MagicMock(spec=Commitstatus)
    with patch(
        f"{_API}.put_repositories_workspace_repo_slug_commit_commit_statuses_build_key.asyncio",
        new=AsyncMock(return_value=status),
    ):
        result = await commit_statuses.update(mock_client, "ws", "slug", "abc", "my-key")
    assert result is status


async def test_list_raises_on_bad_auth(bad_auth_client):
    with pytest.raises(AuthenticationError):
        await commit_statuses.list(bad_auth_client, "ws", "slug", "abc")
