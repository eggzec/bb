from __future__ import annotations

import asyncio
from typing import Any

from bb.cloud.models.component import Component
from bb.cloud.models.error import Error
from bb.cloud.models.issue import Issue
from bb.cloud.models.issue_change import IssueChange
from bb.cloud.models.issue_comment import IssueComment
from bb.cloud.models.milestone import Milestone
from bb.cloud.models.version import Version
from bb.cloud.sdk import issues as _async
from bb.cloud.sdk._client import BBClient
from bb.cloud.types import UNSET, Unset

__all__ = [
    "list",
    "get",
    "create",
    "update",
    "delete",
    "comments",
    "get_comment",
    "add_comment",
    "update_comment",
    "delete_comment",
    "changes",
    "get_change",
    "add_change",
    "vote",
    "unvote",
    "voted",
    "watch",
    "unwatch",
    "watching",
    "milestones",
    "get_milestone",
    "versions",
    "get_version",
    "components",
    "get_component",
    "attachments",
    "get_attachment",
    "upload_attachment",
    "delete_attachment",
    "export",
    "export_status",
    "import_status",
    "import_data",
]


def list(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    pagelen: int = 25,
) -> list[Issue] | Error:
    """Sync version of :func:`~bb.cloud.sdk.issues.list`."""
    return asyncio.run(_async.list(client, workspace, repo_slug, q=q, sort=sort, pagelen=pagelen))


def get(client: BBClient, workspace: str, repo_slug: str, issue_id: int) -> Issue | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.issues.get`."""
    return asyncio.run(_async.get(client, workspace, repo_slug, issue_id))


def create(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: Issue | Unset = UNSET,
) -> Issue | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.issues.create`."""
    return asyncio.run(_async.create(client, workspace, repo_slug, body=body))


def update(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    issue_id: int,
    *,
    body: Issue | Unset = UNSET,
) -> Issue | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.issues.update`."""
    return asyncio.run(_async.update(client, workspace, repo_slug, issue_id, body=body))


def delete(client: BBClient, workspace: str, repo_slug: str, issue_id: int) -> None:
    """Sync version of :func:`~bb.cloud.sdk.issues.delete`."""
    asyncio.run(_async.delete(client, workspace, repo_slug, issue_id))


def comments(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    issue_id: int,
    *,
    pagelen: int = 25,
) -> list[IssueComment] | Error:
    """Sync version of :func:`~bb.cloud.sdk.issues.comments`."""
    return asyncio.run(_async.comments(client, workspace, repo_slug, issue_id, pagelen=pagelen))


def get_comment(
    client: BBClient, workspace: str, repo_slug: str, issue_id: int, comment_id: int
) -> IssueComment | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.issues.get_comment`."""
    return asyncio.run(_async.get_comment(client, workspace, repo_slug, issue_id, comment_id))


def add_comment(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    issue_id: int,
    *,
    body: IssueComment | Unset = UNSET,
) -> IssueComment | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.issues.add_comment`."""
    return asyncio.run(_async.add_comment(client, workspace, repo_slug, issue_id, body=body))


def update_comment(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    issue_id: int,
    comment_id: int,
    *,
    body: IssueComment | Unset = UNSET,
) -> IssueComment | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.issues.update_comment`."""
    return asyncio.run(_async.update_comment(client, workspace, repo_slug, issue_id, comment_id, body=body))


def delete_comment(client: BBClient, workspace: str, repo_slug: str, issue_id: int, comment_id: int) -> None:
    """Sync version of :func:`~bb.cloud.sdk.issues.delete_comment`."""
    asyncio.run(_async.delete_comment(client, workspace, repo_slug, issue_id, comment_id))


def changes(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    issue_id: int,
    *,
    pagelen: int = 25,
) -> list[IssueChange] | Error:
    """Sync version of :func:`~bb.cloud.sdk.issues.changes`."""
    return asyncio.run(_async.changes(client, workspace, repo_slug, issue_id, pagelen=pagelen))


def get_change(
    client: BBClient, workspace: str, repo_slug: str, issue_id: int, change_id: int
) -> IssueChange | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.issues.get_change`."""
    return asyncio.run(_async.get_change(client, workspace, repo_slug, issue_id, change_id))


def add_change(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    issue_id: int,
    *,
    body: IssueChange | Unset = UNSET,
) -> IssueChange | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.issues.add_change`."""
    return asyncio.run(_async.add_change(client, workspace, repo_slug, issue_id, body=body))


def vote(client: BBClient, workspace: str, repo_slug: str, issue_id: int) -> None:
    """Sync version of :func:`~bb.cloud.sdk.issues.vote`."""
    asyncio.run(_async.vote(client, workspace, repo_slug, issue_id))


def unvote(client: BBClient, workspace: str, repo_slug: str, issue_id: int) -> None:
    """Sync version of :func:`~bb.cloud.sdk.issues.unvote`."""
    asyncio.run(_async.unvote(client, workspace, repo_slug, issue_id))


def voted(client: BBClient, workspace: str, repo_slug: str, issue_id: int) -> Any | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.issues.voted`."""
    return asyncio.run(_async.voted(client, workspace, repo_slug, issue_id))


def watch(client: BBClient, workspace: str, repo_slug: str, issue_id: int) -> None:
    """Sync version of :func:`~bb.cloud.sdk.issues.watch`."""
    asyncio.run(_async.watch(client, workspace, repo_slug, issue_id))


def unwatch(client: BBClient, workspace: str, repo_slug: str, issue_id: int) -> None:
    """Sync version of :func:`~bb.cloud.sdk.issues.unwatch`."""
    asyncio.run(_async.unwatch(client, workspace, repo_slug, issue_id))


def watching(client: BBClient, workspace: str, repo_slug: str, issue_id: int) -> Any | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.issues.watching`."""
    return asyncio.run(_async.watching(client, workspace, repo_slug, issue_id))


def milestones(client: BBClient, workspace: str, repo_slug: str) -> list[Milestone] | Error:
    """Sync version of :func:`~bb.cloud.sdk.issues.milestones`."""
    return asyncio.run(_async.milestones(client, workspace, repo_slug))


def get_milestone(client: BBClient, workspace: str, repo_slug: str, milestone_id: int) -> Milestone | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.issues.get_milestone`."""
    return asyncio.run(_async.get_milestone(client, workspace, repo_slug, milestone_id))


def versions(client: BBClient, workspace: str, repo_slug: str) -> list[Version] | Error:
    """Sync version of :func:`~bb.cloud.sdk.issues.versions`."""
    return asyncio.run(_async.versions(client, workspace, repo_slug))


def get_version(client: BBClient, workspace: str, repo_slug: str, version_id: int) -> Version | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.issues.get_version`."""
    return asyncio.run(_async.get_version(client, workspace, repo_slug, version_id))


def components(client: BBClient, workspace: str, repo_slug: str) -> list[Component] | Error:
    """Sync version of :func:`~bb.cloud.sdk.issues.components`."""
    return asyncio.run(_async.components(client, workspace, repo_slug))


def get_component(client: BBClient, workspace: str, repo_slug: str, component_id: int) -> Component | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.issues.get_component`."""
    return asyncio.run(_async.get_component(client, workspace, repo_slug, component_id))


def attachments(client: BBClient, workspace: str, repo_slug: str, issue_id: int) -> Any | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.issues.attachments`."""
    return asyncio.run(_async.attachments(client, workspace, repo_slug, issue_id))


def get_attachment(client: BBClient, workspace: str, repo_slug: str, issue_id: int, path: str) -> Any | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.issues.get_attachment`."""
    return asyncio.run(_async.get_attachment(client, workspace, repo_slug, issue_id, path))


def upload_attachment(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    issue_id: int,
    *,
    body: Unset = UNSET,
) -> None:
    """Sync version of :func:`~bb.cloud.sdk.issues.upload_attachment`."""
    asyncio.run(_async.upload_attachment(client, workspace, repo_slug, issue_id, body=body))


def delete_attachment(client: BBClient, workspace: str, repo_slug: str, issue_id: int, path: str) -> None:
    """Sync version of :func:`~bb.cloud.sdk.issues.delete_attachment`."""
    asyncio.run(_async.delete_attachment(client, workspace, repo_slug, issue_id, path))


def export(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: Unset = UNSET,
) -> None:
    """Sync version of :func:`~bb.cloud.sdk.issues.export`."""
    asyncio.run(_async.export(client, workspace, repo_slug, body=body))


def export_status(client: BBClient, workspace: str, repo_slug: str, repo_name: str, task_id: str) -> Any | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.issues.export_status`."""
    return asyncio.run(_async.export_status(client, workspace, repo_slug, repo_name, task_id))


def import_status(client: BBClient, workspace: str, repo_slug: str) -> Any | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.issues.import_status`."""
    return asyncio.run(_async.import_status(client, workspace, repo_slug))


def import_data(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: Unset = UNSET,
) -> None:
    """Sync version of :func:`~bb.cloud.sdk.issues.import_data`."""
    asyncio.run(_async.import_data(client, workspace, repo_slug, body=body))
