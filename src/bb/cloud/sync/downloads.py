from __future__ import annotations

import asyncio
from typing import Any

from bb.cloud.sdk import downloads as _async
from bb.cloud.sdk._client import BBClient
from bb.cloud.types import UNSET, Unset

__all__ = [
    "list",
    "get",
    "upload",
    "delete",
]


def list(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    pagelen: int = 25,
) -> list[Any]:
    """Sync version of :func:`~bb.cloud.sdk.downloads.list`."""
    return asyncio.run(_async.list(client, workspace, repo_slug, pagelen=pagelen))


def get(client: BBClient, workspace: str, repo_slug: str, filename: str) -> Any:
    """Sync version of :func:`~bb.cloud.sdk.downloads.get`."""
    return asyncio.run(_async.get(client, workspace, repo_slug, filename))


def upload(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: Unset = UNSET,
) -> Any:
    """Sync version of :func:`~bb.cloud.sdk.downloads.upload`."""
    return asyncio.run(_async.upload(client, workspace, repo_slug, body=body))


def delete(client: BBClient, workspace: str, repo_slug: str, filename: str) -> None:
    """Sync version of :func:`~bb.cloud.sdk.downloads.delete`."""
    asyncio.run(_async.delete(client, workspace, repo_slug, filename))
