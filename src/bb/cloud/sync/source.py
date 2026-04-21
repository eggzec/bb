from __future__ import annotations

import asyncio

from bb.cloud.models.error import Error
from bb.cloud.sdk import source as _async
from bb.cloud.sdk._client import BBClient
from bb.cloud.types import UNSET, Unset

__all__ = [
    "get",
    "root",
    "history",
    "upload",
]


def get(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    commit: str,
    path: str,
) -> object | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.source.get`."""
    return asyncio.run(_async.get(client, workspace, repo_slug, commit, path))


def root(client: BBClient, workspace: str, repo_slug: str) -> object | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.source.root`."""
    return asyncio.run(_async.root(client, workspace, repo_slug))


def history(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    commit: str,
    path: str,
) -> object | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.source.history`."""
    return asyncio.run(_async.history(client, workspace, repo_slug, commit, path))


def upload(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: Unset = UNSET,
) -> object | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.source.upload`."""
    return asyncio.run(_async.upload(client, workspace, repo_slug, body=body))
