from __future__ import annotations

import asyncio
from typing import Any

from bb.cloud.models.error import Error
from bb.cloud.models.workspace import Workspace
from bb.cloud.sdk import workspaces as _async
from bb.cloud.sdk._client import BBClient

__all__ = [
    "list",
    "get",
    "members",
    "get_member",
    "permissions",
    "repo_permissions",
    "get_repo_permission",
    "user_prs",
    "gpg_key",
    "mine",
    "my_permissions",
    "my_permission",
]


def list(client: BBClient, *, pagelen: int = 25) -> list[Workspace] | Error:
    """Sync version of :func:`~bb.cloud.sdk.workspaces.list`."""
    return asyncio.run(_async.list(client, pagelen=pagelen))


def get(client: BBClient, workspace: str) -> Workspace | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.workspaces.get`."""
    return asyncio.run(_async.get(client, workspace))


def members(client: BBClient, workspace: str, *, pagelen: int = 25) -> list[Any] | Error:
    """Sync version of :func:`~bb.cloud.sdk.workspaces.members`."""
    return asyncio.run(_async.members(client, workspace, pagelen=pagelen))


def get_member(client: BBClient, workspace: str, member: str) -> Any | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.workspaces.get_member`."""
    return asyncio.run(_async.get_member(client, workspace, member))


def permissions(client: BBClient, workspace: str, *, pagelen: int = 25) -> list[Any] | Error:
    """Sync version of :func:`~bb.cloud.sdk.workspaces.permissions`."""
    return asyncio.run(_async.permissions(client, workspace, pagelen=pagelen))


def repo_permissions(client: BBClient, workspace: str, *, pagelen: int = 25) -> list[Any] | Error:
    """Sync version of :func:`~bb.cloud.sdk.workspaces.repo_permissions`."""
    return asyncio.run(_async.repo_permissions(client, workspace, pagelen=pagelen))


def get_repo_permission(client: BBClient, workspace: str, repo_slug: str) -> Any | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.workspaces.get_repo_permission`."""
    return asyncio.run(_async.get_repo_permission(client, workspace, repo_slug))


def user_prs(client: BBClient, workspace: str, selected_user: str, *, pagelen: int = 25) -> list[Any] | Error:
    """Sync version of :func:`~bb.cloud.sdk.workspaces.user_prs`."""
    return asyncio.run(_async.user_prs(client, workspace, selected_user, pagelen=pagelen))


def gpg_key(client: BBClient, workspace: str) -> Any | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.workspaces.gpg_key`."""
    return asyncio.run(_async.gpg_key(client, workspace))


def mine(client: BBClient, *, pagelen: int = 25) -> list[Workspace] | Error:
    """Sync version of :func:`~bb.cloud.sdk.workspaces.mine`."""
    return asyncio.run(_async.mine(client, pagelen=pagelen))


def my_permissions(client: BBClient, *, pagelen: int = 25) -> list[Any] | Error:
    """Sync version of :func:`~bb.cloud.sdk.workspaces.my_permissions`."""
    return asyncio.run(_async.my_permissions(client, pagelen=pagelen))


def my_permission(client: BBClient, workspace: str) -> Any | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.workspaces.my_permission`."""
    return asyncio.run(_async.my_permission(client, workspace))
