from __future__ import annotations

import asyncio
from typing import Any

from bb.cloud.models.error import Error
from bb.cloud.models.repository import Repository
from bb.cloud.sdk import repos as _async
from bb.cloud.sdk._client import BBClient
from bb.cloud.types import UNSET, Unset

__all__ = [
    "list",
    "get",
    "create",
    "update",
    "delete",
    "fork",
    "forks",
    "watchers",
    "override_settings",
    "update_override_settings",
    "group_permissions",
    "get_group_permission",
    "set_group_permission",
    "delete_group_permission",
    "user_permissions",
    "get_user_permission",
    "set_user_permission",
    "delete_user_permission",
    "my_permissions",
    "workspace_user_permissions",
]


def list(
    client: BBClient,
    workspace: str,
    *,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    pagelen: int = 25,
) -> list[Repository] | Error:
    """Sync version of :func:`~bb.cloud.sdk.repos.list`."""
    return asyncio.run(_async.list(client, workspace, q=q, sort=sort, pagelen=pagelen))


def get(client: BBClient, workspace: str, repo_slug: str) -> Repository | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.repos.get`."""
    return asyncio.run(_async.get(client, workspace, repo_slug))


def create(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: Repository | Unset = UNSET,
) -> Repository | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.repos.create`."""
    return asyncio.run(_async.create(client, workspace, repo_slug, body=body))


def update(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: Repository | Unset = UNSET,
) -> Repository | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.repos.update`."""
    return asyncio.run(_async.update(client, workspace, repo_slug, body=body))


def delete(client: BBClient, workspace: str, repo_slug: str) -> None:
    """Sync version of :func:`~bb.cloud.sdk.repos.delete`."""
    return asyncio.run(_async.delete(client, workspace, repo_slug))


def fork(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: Repository | Unset = UNSET,
) -> Repository | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.repos.fork`."""
    return asyncio.run(_async.fork(client, workspace, repo_slug, body=body))


def forks(client: BBClient, workspace: str, repo_slug: str) -> list[Repository] | Error:
    """Sync version of :func:`~bb.cloud.sdk.repos.forks`."""
    return asyncio.run(_async.forks(client, workspace, repo_slug))


def watchers(client: BBClient, workspace: str, repo_slug: str) -> list[Repository] | Error:
    """Sync version of :func:`~bb.cloud.sdk.repos.watchers`."""
    return asyncio.run(_async.watchers(client, workspace, repo_slug))


def override_settings(client: BBClient, workspace: str, repo_slug: str) -> Any | None:
    """Sync version of :func:`~bb.cloud.sdk.repos.override_settings`."""
    return asyncio.run(_async.override_settings(client, workspace, repo_slug))


def update_override_settings(client: BBClient, workspace: str, repo_slug: str, *, body: Unset = UNSET) -> Any | None:
    """Sync version of :func:`~bb.cloud.sdk.repos.update_override_settings`."""
    return asyncio.run(_async.update_override_settings(client, workspace, repo_slug, body=body))


def group_permissions(client: BBClient, workspace: str, repo_slug: str, *, pagelen: int = 25) -> list[Any] | Error:
    """Sync version of :func:`~bb.cloud.sdk.repos.group_permissions`."""
    return asyncio.run(_async.group_permissions(client, workspace, repo_slug, pagelen=pagelen))


def get_group_permission(client: BBClient, workspace: str, repo_slug: str, group_slug: str) -> Any | None:
    """Sync version of :func:`~bb.cloud.sdk.repos.get_group_permission`."""
    return asyncio.run(_async.get_group_permission(client, workspace, repo_slug, group_slug))


def set_group_permission(
    client: BBClient, workspace: str, repo_slug: str, group_slug: str, *, body: Unset = UNSET
) -> Any | None:
    """Sync version of :func:`~bb.cloud.sdk.repos.set_group_permission`."""
    return asyncio.run(_async.set_group_permission(client, workspace, repo_slug, group_slug, body=body))


def delete_group_permission(client: BBClient, workspace: str, repo_slug: str, group_slug: str) -> None:
    """Sync version of :func:`~bb.cloud.sdk.repos.delete_group_permission`."""
    return asyncio.run(_async.delete_group_permission(client, workspace, repo_slug, group_slug))


def user_permissions(client: BBClient, workspace: str, repo_slug: str, *, pagelen: int = 25) -> list[Any] | Error:
    """Sync version of :func:`~bb.cloud.sdk.repos.user_permissions`."""
    return asyncio.run(_async.user_permissions(client, workspace, repo_slug, pagelen=pagelen))


def get_user_permission(client: BBClient, workspace: str, repo_slug: str, selected_user_id: str) -> Any | None:
    """Sync version of :func:`~bb.cloud.sdk.repos.get_user_permission`."""
    return asyncio.run(_async.get_user_permission(client, workspace, repo_slug, selected_user_id))


def set_user_permission(
    client: BBClient, workspace: str, repo_slug: str, selected_user_id: str, *, body: Unset = UNSET
) -> Any | None:
    """Sync version of :func:`~bb.cloud.sdk.repos.set_user_permission`."""
    return asyncio.run(_async.set_user_permission(client, workspace, repo_slug, selected_user_id, body=body))


def delete_user_permission(client: BBClient, workspace: str, repo_slug: str, selected_user_id: str) -> None:
    """Sync version of :func:`~bb.cloud.sdk.repos.delete_user_permission`."""
    return asyncio.run(_async.delete_user_permission(client, workspace, repo_slug, selected_user_id))


def my_permissions(client: BBClient, *, pagelen: int = 25) -> list[Any] | Error:
    """Sync version of :func:`~bb.cloud.sdk.repos.my_permissions`."""
    return asyncio.run(_async.my_permissions(client, pagelen=pagelen))


def workspace_user_permissions(client: BBClient, workspace: str, *, pagelen: int = 25) -> list[Any] | Error:
    """Sync version of :func:`~bb.cloud.sdk.repos.workspace_user_permissions`."""
    return asyncio.run(_async.workspace_user_permissions(client, workspace, pagelen=pagelen))
