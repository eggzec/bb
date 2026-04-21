from __future__ import annotations

import asyncio

from bb.cloud.models.commitstatus import Commitstatus
from bb.cloud.models.error import Error
from bb.cloud.sdk import commit_statuses as _async
from bb.cloud.sdk._client import BBClient
from bb.cloud.types import UNSET, Unset

__all__ = [
    "list",
    "get",
    "create",
    "update",
]


def list(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    commit: str,
    *,
    pagelen: int = 25,
) -> list[Commitstatus] | Error:
    """Sync version of :func:`~bb.cloud.sdk.commit_statuses.list`."""
    return asyncio.run(_async.list(client, workspace, repo_slug, commit, pagelen=pagelen))


def get(client: BBClient, workspace: str, repo_slug: str, commit: str, key: str) -> Commitstatus | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.commit_statuses.get`."""
    return asyncio.run(_async.get(client, workspace, repo_slug, commit, key))


def create(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    commit: str,
    *,
    body: Commitstatus | Unset = UNSET,
) -> Commitstatus | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.commit_statuses.create`."""
    return asyncio.run(_async.create(client, workspace, repo_slug, commit, body=body))


def update(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    commit: str,
    key: str,
    *,
    body: Commitstatus | Unset = UNSET,
) -> Commitstatus | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.commit_statuses.update`."""
    return asyncio.run(_async.update(client, workspace, repo_slug, commit, key, body=body))
