"""Tests for bb.cloud.sdk.webhooks."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from bb.cloud.models.webhook_subscription import WebhookSubscription
from bb.cloud.sdk import webhooks
from bb.cloud.sdk._errors import AuthenticationError

_API = "bb.cloud.api.webhooks"


async def test_list_repo_returns_webhooks(mock_client, make_page):
    item = MagicMock(spec=WebhookSubscription)
    with patch(
        f"{_API}.get_repositories_workspace_repo_slug_hooks.asyncio", new=AsyncMock(return_value=make_page([item]))
    ):
        result = await webhooks.list_repo(mock_client, "ws", "slug")
    assert result == [item]


async def test_list_repo_empty(mock_client, make_page):
    with patch(f"{_API}.get_repositories_workspace_repo_slug_hooks.asyncio", new=AsyncMock(return_value=make_page([]))):
        result = await webhooks.list_repo(mock_client, "ws", "slug")
    assert result == []


async def test_get_repo_returns_webhook(mock_client):
    hook = MagicMock(spec=WebhookSubscription)
    with patch(f"{_API}.get_repositories_workspace_repo_slug_hooks_uid.asyncio", new=AsyncMock(return_value=hook)):
        result = await webhooks.get_repo(mock_client, "ws", "slug", "{uid}")
    assert result is hook


async def test_get_repo_returns_none(mock_client):
    with patch(f"{_API}.get_repositories_workspace_repo_slug_hooks_uid.asyncio", new=AsyncMock(return_value=None)):
        result = await webhooks.get_repo(mock_client, "ws", "slug", "{uid}")
    assert result is None


async def test_create_repo_returns_webhook(mock_client):
    hook = MagicMock(spec=WebhookSubscription)
    with patch(f"{_API}.post_repositories_workspace_repo_slug_hooks.asyncio", new=AsyncMock(return_value=hook)):
        result = await webhooks.create_repo(mock_client, "ws", "slug")
    assert result is hook


async def test_update_repo_returns_webhook(mock_client):
    hook = MagicMock(spec=WebhookSubscription)
    with patch(f"{_API}.put_repositories_workspace_repo_slug_hooks_uid.asyncio", new=AsyncMock(return_value=hook)):
        result = await webhooks.update_repo(mock_client, "ws", "slug", "{uid}")
    assert result is hook


async def test_delete_repo_returns_none(mock_client):
    with patch(f"{_API}.delete_repositories_workspace_repo_slug_hooks_uid.asyncio", new=AsyncMock(return_value=None)):
        result = await webhooks.delete_repo(mock_client, "ws", "slug", "{uid}")
    assert result is None


async def test_list_workspace_returns_webhooks(mock_client, make_page):
    item = MagicMock(spec=WebhookSubscription)
    with patch(f"{_API}.get_workspaces_workspace_hooks.asyncio", new=AsyncMock(return_value=make_page([item]))):
        result = await webhooks.list_workspace(mock_client, "ws")
    assert result == [item]


async def test_get_workspace_returns_webhook(mock_client):
    hook = MagicMock(spec=WebhookSubscription)
    with patch(f"{_API}.get_workspaces_workspace_hooks_uid.asyncio", new=AsyncMock(return_value=hook)):
        result = await webhooks.get_workspace(mock_client, "ws", "{uid}")
    assert result is hook


async def test_create_workspace_returns_webhook(mock_client):
    hook = MagicMock(spec=WebhookSubscription)
    with patch(f"{_API}.post_workspaces_workspace_hooks.asyncio", new=AsyncMock(return_value=hook)):
        result = await webhooks.create_workspace(mock_client, "ws")
    assert result is hook


async def test_update_workspace_returns_webhook(mock_client):
    hook = MagicMock(spec=WebhookSubscription)
    with patch(f"{_API}.put_workspaces_workspace_hooks_uid.asyncio", new=AsyncMock(return_value=hook)):
        result = await webhooks.update_workspace(mock_client, "ws", "{uid}")
    assert result is hook


async def test_delete_workspace_returns_none(mock_client):
    with patch(f"{_API}.delete_workspaces_workspace_hooks_uid.asyncio", new=AsyncMock(return_value=None)):
        result = await webhooks.delete_workspace(mock_client, "ws", "{uid}")
    assert result is None


async def test_events_returns_list(mock_client, make_page):
    item = MagicMock()
    with patch(f"{_API}.get_hook_events_subject_type.asyncio", new=AsyncMock(return_value=make_page([item]))):
        result = await webhooks.events(mock_client, "repository")
    assert result == [item]


async def test_list_repo_raises_on_bad_auth(bad_auth_client):
    with pytest.raises(AuthenticationError):
        await webhooks.list_repo(bad_auth_client, "ws", "slug")
