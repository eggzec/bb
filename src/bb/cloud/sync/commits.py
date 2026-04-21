from __future__ import annotations

import asyncio

from bb.cloud.models.base_commit import BaseCommit
from bb.cloud.models.commit import Commit
from bb.cloud.models.error import Error
from bb.cloud.models.pullrequest import Pullrequest
from bb.cloud.sdk import commits as _async
from bb.cloud.sdk._client import BBClient

__all__ = [
    "list",
    "get",
    "prs",
]


def list(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    pagelen: int = 25,
) -> list[BaseCommit] | Error:
    """Sync version of :func:`~bb.cloud.sdk.commits.list`."""
    return asyncio.run(_async.list(client, workspace, repo_slug, pagelen=pagelen))


def get(client: BBClient, workspace: str, repo_slug: str, commit: str) -> Commit | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.commits.get`."""
    return asyncio.run(_async.get(client, workspace, repo_slug, commit))


def prs(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    commit: str,
    *,
    pagelen: int = 25,
) -> list[Pullrequest] | Error:
    """Sync version of :func:`~bb.cloud.sdk.commits.prs`."""
    return asyncio.run(_async.prs(client, workspace, repo_slug, commit, pagelen=pagelen))
