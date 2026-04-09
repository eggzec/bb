from __future__ import annotations

import asyncio
from typing import Any

from bb.cloud.models.project import Project
from bb.cloud.sdk import projects as _async
from bb.cloud.sdk._client import BBClient
from bb.cloud.types import UNSET, Unset

__all__ = [
    "list",
    "get",
    "create",
    "update",
    "delete",
    "default_reviewers",
    "get_default_reviewer",
    "add_default_reviewer",
    "remove_default_reviewer",
    "group_permissions",
    "update_group_permission",
    "delete_group_permission",
    "user_permissions",
    "update_user_permission",
    "delete_user_permission",
]


def list(client: BBClient, workspace: str, *, pagelen: int = 25) -> list[Project]:
    """Sync version of :func:`~bb.cloud.sdk.projects.list`."""
    return asyncio.run(_async.list(client, workspace, pagelen=pagelen))


def get(client: BBClient, workspace: str, project_key: str) -> Project | None:
    """Sync version of :func:`~bb.cloud.sdk.projects.get`."""
    return asyncio.run(_async.get(client, workspace, project_key))


def create(
    client: BBClient,
    workspace: str,
    *,
    body: Project | Unset = UNSET,
) -> Project | None:
    """Sync version of :func:`~bb.cloud.sdk.projects.create`."""
    return asyncio.run(_async.create(client, workspace, body=body))


def update(
    client: BBClient,
    workspace: str,
    project_key: str,
    *,
    body: Project | Unset = UNSET,
) -> Project | None:
    """Sync version of :func:`~bb.cloud.sdk.projects.update`."""
    return asyncio.run(_async.update(client, workspace, project_key, body=body))


def delete(client: BBClient, workspace: str, project_key: str) -> None:
    """Sync version of :func:`~bb.cloud.sdk.projects.delete`."""
    return asyncio.run(_async.delete(client, workspace, project_key))


def default_reviewers(client: BBClient, workspace: str, project_key: str, *, pagelen: int = 25) -> list[Any]:
    """Sync version of :func:`~bb.cloud.sdk.projects.default_reviewers`."""
    return asyncio.run(_async.default_reviewers(client, workspace, project_key, pagelen=pagelen))


def get_default_reviewer(client: BBClient, workspace: str, project_key: str, selected_user: str) -> Any | None:
    """Sync version of :func:`~bb.cloud.sdk.projects.get_default_reviewer`."""
    return asyncio.run(_async.get_default_reviewer(client, workspace, project_key, selected_user))


def add_default_reviewer(client: BBClient, workspace: str, project_key: str, selected_user: str) -> None:
    """Sync version of :func:`~bb.cloud.sdk.projects.add_default_reviewer`."""
    return asyncio.run(_async.add_default_reviewer(client, workspace, project_key, selected_user))


def remove_default_reviewer(client: BBClient, workspace: str, project_key: str, selected_user: str) -> None:
    """Sync version of :func:`~bb.cloud.sdk.projects.remove_default_reviewer`."""
    return asyncio.run(_async.remove_default_reviewer(client, workspace, project_key, selected_user))


def group_permissions(client: BBClient, workspace: str, project_key: str, *, pagelen: int = 25) -> list[Any]:
    """Sync version of :func:`~bb.cloud.sdk.projects.group_permissions`."""
    return asyncio.run(_async.group_permissions(client, workspace, project_key, pagelen=pagelen))


def update_group_permission(
    client: BBClient,
    workspace: str,
    project_key: str,
    group_slug: str,
    *,
    body: Unset = UNSET,
) -> Any | None:
    """Sync version of :func:`~bb.cloud.sdk.projects.update_group_permission`."""
    return asyncio.run(_async.update_group_permission(client, workspace, project_key, group_slug, body=body))


def delete_group_permission(client: BBClient, workspace: str, project_key: str, group_slug: str) -> None:
    """Sync version of :func:`~bb.cloud.sdk.projects.delete_group_permission`."""
    return asyncio.run(_async.delete_group_permission(client, workspace, project_key, group_slug))


def user_permissions(client: BBClient, workspace: str, project_key: str, *, pagelen: int = 25) -> list[Any]:
    """Sync version of :func:`~bb.cloud.sdk.projects.user_permissions`."""
    return asyncio.run(_async.user_permissions(client, workspace, project_key, pagelen=pagelen))


def update_user_permission(
    client: BBClient,
    workspace: str,
    project_key: str,
    selected_user_id: str,
    *,
    body: Unset = UNSET,
) -> Any | None:
    """Sync version of :func:`~bb.cloud.sdk.projects.update_user_permission`."""
    return asyncio.run(_async.update_user_permission(client, workspace, project_key, selected_user_id, body=body))


def delete_user_permission(client: BBClient, workspace: str, project_key: str, selected_user_id: str) -> None:
    """Sync version of :func:`~bb.cloud.sdk.projects.delete_user_permission`."""
    return asyncio.run(_async.delete_user_permission(client, workspace, project_key, selected_user_id))
