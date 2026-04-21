from __future__ import annotations

import asyncio

from bb.cloud.models.error import Error
from bb.cloud.models.get_hook_events_subject_type_subject_type import GetHookEventsSubjectTypeSubjectType
from bb.cloud.models.hook_event import HookEvent
from bb.cloud.models.webhook_subscription import WebhookSubscription
from bb.cloud.sdk import webhooks as _async
from bb.cloud.sdk._client import BBClient
from bb.cloud.sdk.webhooks import HookSubjectType
from bb.cloud.types import UNSET, Unset

__all__ = [
    "HookSubjectType",
    "list_repo",
    "get_repo",
    "create_repo",
    "update_repo",
    "delete_repo",
    "list_workspace",
    "get_workspace",
    "create_workspace",
    "update_workspace",
    "delete_workspace",
    "events",
]


def list_repo(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    pagelen: int = 25,
) -> list[WebhookSubscription] | Error:
    """Sync version of :func:`~bb.cloud.sdk.webhooks.list_repo`."""
    return asyncio.run(_async.list_repo(client, workspace, repo_slug, pagelen=pagelen))


def get_repo(client: BBClient, workspace: str, repo_slug: str, uid: str) -> WebhookSubscription | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.webhooks.get_repo`."""
    return asyncio.run(_async.get_repo(client, workspace, repo_slug, uid))


def create_repo(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: WebhookSubscription | Unset = UNSET,
) -> WebhookSubscription | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.webhooks.create_repo`."""
    return asyncio.run(_async.create_repo(client, workspace, repo_slug, body=body))


def update_repo(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    uid: str,
    *,
    body: WebhookSubscription | Unset = UNSET,
) -> WebhookSubscription | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.webhooks.update_repo`."""
    return asyncio.run(_async.update_repo(client, workspace, repo_slug, uid, body=body))


def delete_repo(client: BBClient, workspace: str, repo_slug: str, uid: str) -> None:
    """Sync version of :func:`~bb.cloud.sdk.webhooks.delete_repo`."""
    asyncio.run(_async.delete_repo(client, workspace, repo_slug, uid))


def list_workspace(
    client: BBClient,
    workspace: str,
    *,
    pagelen: int = 25,
) -> list[WebhookSubscription] | Error:
    """Sync version of :func:`~bb.cloud.sdk.webhooks.list_workspace`."""
    return asyncio.run(_async.list_workspace(client, workspace, pagelen=pagelen))


def get_workspace(client: BBClient, workspace: str, uid: str) -> WebhookSubscription | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.webhooks.get_workspace`."""
    return asyncio.run(_async.get_workspace(client, workspace, uid))


def create_workspace(
    client: BBClient,
    workspace: str,
    *,
    body: WebhookSubscription | Unset = UNSET,
) -> WebhookSubscription | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.webhooks.create_workspace`."""
    return asyncio.run(_async.create_workspace(client, workspace, body=body))


def update_workspace(
    client: BBClient,
    workspace: str,
    uid: str,
    *,
    body: WebhookSubscription | Unset = UNSET,
) -> WebhookSubscription | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.webhooks.update_workspace`."""
    return asyncio.run(_async.update_workspace(client, workspace, uid, body=body))


def delete_workspace(client: BBClient, workspace: str, uid: str) -> None:
    """Sync version of :func:`~bb.cloud.sdk.webhooks.delete_workspace`."""
    asyncio.run(_async.delete_workspace(client, workspace, uid))


def events(
    client: BBClient,
    subject_type: GetHookEventsSubjectTypeSubjectType,
) -> list[HookEvent] | Error:
    """Sync version of :func:`~bb.cloud.sdk.webhooks.events`."""
    return asyncio.run(_async.events(client, subject_type))
