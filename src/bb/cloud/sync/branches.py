from __future__ import annotations

import asyncio

from bb.cloud.models.branch import Branch
from bb.cloud.models.error import Error
from bb.cloud.models.tag import Tag
from bb.cloud.sdk import branches as _async
from bb.cloud.sdk._client import BBClient
from bb.cloud.types import UNSET, Unset

__all__ = [
    "list",
    "get",
    "create",
    "delete",
    "tags",
    "get_tag",
    "create_tag",
    "delete_tag",
]


def list(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    pagelen: int = 25,
) -> list[Branch] | Error:
    """Sync version of :func:`~bb.cloud.sdk.branches.list`."""
    return asyncio.run(_async.list(client, workspace, repo_slug, q=q, sort=sort, pagelen=pagelen))


def get(client: BBClient, workspace: str, repo_slug: str, name: str) -> Branch | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.branches.get`."""
    return asyncio.run(_async.get(client, workspace, repo_slug, name))


def create(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    name: str,
    target_hash: str,
) -> Branch | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.branches.create`."""
    return asyncio.run(_async.create(client, workspace, repo_slug, name=name, target_hash=target_hash))


def delete(client: BBClient, workspace: str, repo_slug: str, name: str) -> None:
    """Sync version of :func:`~bb.cloud.sdk.branches.delete`."""
    asyncio.run(_async.delete(client, workspace, repo_slug, name))


def tags(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    pagelen: int = 25,
) -> list[Tag] | Error:
    """Sync version of :func:`~bb.cloud.sdk.branches.tags`."""
    return asyncio.run(_async.tags(client, workspace, repo_slug, q=q, sort=sort, pagelen=pagelen))


def get_tag(client: BBClient, workspace: str, repo_slug: str, name: str) -> Tag | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.branches.get_tag`."""
    return asyncio.run(_async.get_tag(client, workspace, repo_slug, name))


def create_tag(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: Tag | Unset = UNSET,
) -> Tag | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.branches.create_tag`."""
    return asyncio.run(_async.create_tag(client, workspace, repo_slug, body=body))


def delete_tag(client: BBClient, workspace: str, repo_slug: str, name: str) -> None:
    """Sync version of :func:`~bb.cloud.sdk.branches.delete_tag`."""
    asyncio.run(_async.delete_tag(client, workspace, repo_slug, name))
