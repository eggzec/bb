from __future__ import annotations

import asyncio

from bb.cloud.models.branchrestriction import Branchrestriction
from bb.cloud.models.error import Error
from bb.cloud.sdk import branch_restrictions as _async
from bb.cloud.sdk._client import BBClient
from bb.cloud.types import UNSET, Unset

__all__ = [
    "list",
    "get",
    "create",
    "update",
    "delete",
]


def list(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    pagelen: int = 25,
) -> list[Branchrestriction] | Error:
    """Sync version of :func:`~bb.cloud.sdk.branch_restrictions.list`."""
    return asyncio.run(_async.list(client, workspace, repo_slug, pagelen=pagelen))


def get(client: BBClient, workspace: str, repo_slug: str, id: int) -> Branchrestriction | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.branch_restrictions.get`."""
    return asyncio.run(_async.get(client, workspace, repo_slug, id))


def create(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: Branchrestriction | Unset = UNSET,
) -> Branchrestriction | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.branch_restrictions.create`."""
    return asyncio.run(_async.create(client, workspace, repo_slug, body=body))


def update(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    id: int,
    *,
    body: Branchrestriction | Unset = UNSET,
) -> Branchrestriction | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.branch_restrictions.update`."""
    return asyncio.run(_async.update(client, workspace, repo_slug, id, body=body))


def delete(client: BBClient, workspace: str, repo_slug: str, id: int) -> None:
    """Sync version of :func:`~bb.cloud.sdk.branch_restrictions.delete`."""
    return asyncio.run(_async.delete(client, workspace, repo_slug, id))
