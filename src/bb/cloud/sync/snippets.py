from __future__ import annotations

import asyncio
from typing import Any

from bb.cloud.models.error import Error
from bb.cloud.models.snippet import Snippet
from bb.cloud.models.snippet_comment import SnippetComment
from bb.cloud.models.snippet_commit import SnippetCommit
from bb.cloud.sdk import snippets as _async
from bb.cloud.sdk._client import BBClient
from bb.cloud.types import UNSET, Unset

__all__ = [
    "list",
    "get",
    "create",
    "update",
    "delete",
    "comments",
    "add_comment",
    "commits",
    "watch",
    "unwatch",
    "watchers",
    "get_file",
    "list_all",
    "create_default",
    "get_comment",
    "update_comment",
    "delete_comment",
    "watching",
    "get_commit",
    "get_node",
    "update_node",
    "delete_node",
    "get_node_file",
    "diff",
    "patch",
]


def list(
    client: BBClient,
    workspace: str,
    *,
    pagelen: int = 25,
) -> list[Snippet] | Error:
    """Sync version of :func:`~bb.cloud.sdk.snippets.list`."""
    return asyncio.run(_async.list(client, workspace, pagelen=pagelen))


def get(client: BBClient, workspace: str, encoded_id: str) -> Snippet | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.snippets.get`."""
    return asyncio.run(_async.get(client, workspace, encoded_id))


def create(
    client: BBClient,
    workspace: str,
    *,
    body: Snippet | Unset = UNSET,
) -> Snippet | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.snippets.create`."""
    return asyncio.run(_async.create(client, workspace, body=body))


def update(
    client: BBClient,
    workspace: str,
    encoded_id: str,
    *,
    body: Snippet | Unset = UNSET,
) -> Snippet | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.snippets.update`."""
    return asyncio.run(_async.update(client, workspace, encoded_id, body=body))


def delete(client: BBClient, workspace: str, encoded_id: str) -> None:
    """Sync version of :func:`~bb.cloud.sdk.snippets.delete`."""
    asyncio.run(_async.delete(client, workspace, encoded_id))


def comments(client: BBClient, workspace: str, encoded_id: str, *, pagelen: int = 25) -> list[SnippetComment] | Error:
    """Sync version of :func:`~bb.cloud.sdk.snippets.comments`."""
    return asyncio.run(_async.comments(client, workspace, encoded_id, pagelen=pagelen))


def add_comment(
    client: BBClient,
    workspace: str,
    encoded_id: str,
    *,
    body: SnippetComment | Unset = UNSET,
) -> SnippetComment | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.snippets.add_comment`."""
    return asyncio.run(_async.add_comment(client, workspace, encoded_id, body=body))


def commits(client: BBClient, workspace: str, encoded_id: str, *, pagelen: int = 25) -> list[SnippetCommit] | Error:
    """Sync version of :func:`~bb.cloud.sdk.snippets.commits`."""
    return asyncio.run(_async.commits(client, workspace, encoded_id, pagelen=pagelen))


def watch(client: BBClient, workspace: str, encoded_id: str) -> None:
    """Sync version of :func:`~bb.cloud.sdk.snippets.watch`."""
    asyncio.run(_async.watch(client, workspace, encoded_id))


def unwatch(client: BBClient, workspace: str, encoded_id: str) -> None:
    """Sync version of :func:`~bb.cloud.sdk.snippets.unwatch`."""
    asyncio.run(_async.unwatch(client, workspace, encoded_id))


def watchers(client: BBClient, workspace: str, encoded_id: str, *, pagelen: int = 25) -> list[Any] | Error:
    """Sync version of :func:`~bb.cloud.sdk.snippets.watchers`."""
    return asyncio.run(_async.watchers(client, workspace, encoded_id, pagelen=pagelen))


def get_file(client: BBClient, workspace: str, encoded_id: str, path: str) -> str | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.snippets.get_file`."""
    return asyncio.run(_async.get_file(client, workspace, encoded_id, path))


def list_all(client: BBClient, *, pagelen: int = 25) -> list[Snippet] | Error:
    """Sync version of :func:`~bb.cloud.sdk.snippets.list_all`."""
    return asyncio.run(_async.list_all(client, pagelen=pagelen))


def create_default(client: BBClient, *, body: Snippet | Unset = UNSET) -> Snippet | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.snippets.create_default`."""
    return asyncio.run(_async.create_default(client, body=body))


def get_comment(client: BBClient, workspace: str, encoded_id: str, comment_id: int) -> SnippetComment | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.snippets.get_comment`."""
    return asyncio.run(_async.get_comment(client, workspace, encoded_id, comment_id))


def update_comment(
    client: BBClient,
    workspace: str,
    encoded_id: str,
    comment_id: int,
    *,
    body: SnippetComment | Unset = UNSET,
) -> SnippetComment | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.snippets.update_comment`."""
    return asyncio.run(_async.update_comment(client, workspace, encoded_id, comment_id, body=body))


def delete_comment(client: BBClient, workspace: str, encoded_id: str, comment_id: int) -> None:
    """Sync version of :func:`~bb.cloud.sdk.snippets.delete_comment`."""
    asyncio.run(_async.delete_comment(client, workspace, encoded_id, comment_id))


def watching(client: BBClient, workspace: str, encoded_id: str) -> Any | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.snippets.watching`."""
    return asyncio.run(_async.watching(client, workspace, encoded_id))


def get_commit(client: BBClient, workspace: str, encoded_id: str, revision: str) -> SnippetCommit | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.snippets.get_commit`."""
    return asyncio.run(_async.get_commit(client, workspace, encoded_id, revision))


def get_node(client: BBClient, workspace: str, encoded_id: str, node_id: str) -> Any | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.snippets.get_node`."""
    return asyncio.run(_async.get_node(client, workspace, encoded_id, node_id))


def update_node(
    client: BBClient,
    workspace: str,
    encoded_id: str,
    node_id: str,
    *,
    body: Snippet | Unset = UNSET,
) -> Any | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.snippets.update_node`."""
    return asyncio.run(_async.update_node(client, workspace, encoded_id, node_id, body=body))


def delete_node(client: BBClient, workspace: str, encoded_id: str, node_id: str) -> None:
    """Sync version of :func:`~bb.cloud.sdk.snippets.delete_node`."""
    asyncio.run(_async.delete_node(client, workspace, encoded_id, node_id))


def get_node_file(client: BBClient, workspace: str, encoded_id: str, node_id: str, path: str) -> Any | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.snippets.get_node_file`."""
    return asyncio.run(_async.get_node_file(client, workspace, encoded_id, node_id, path))


def diff(client: BBClient, workspace: str, encoded_id: str, revision: str) -> str | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.snippets.diff`."""
    return asyncio.run(_async.diff(client, workspace, encoded_id, revision))


def patch(client: BBClient, workspace: str, encoded_id: str, revision: str) -> str | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.snippets.patch`."""
    return asyncio.run(_async.patch(client, workspace, encoded_id, revision))
