from __future__ import annotations

import asyncio
from typing import Any

from bb.cloud.models.participant import Participant
from bb.cloud.models.pull_request_merge_parameters import PullRequestMergeParameters
from bb.cloud.models.pullrequest import Pullrequest
from bb.cloud.models.pullrequest_comment import PullrequestComment as PullRequestComment
from bb.cloud.sdk import prs as _async
from bb.cloud.sdk._client import BBClient
from bb.cloud.sdk.prs import PullrequestState
from bb.cloud.types import UNSET, Unset

__all__ = [
    "list",
    "get",
    "create",
    "update",
    "merge",
    "approve",
    "unapprove",
    "decline",
    "request_changes",
    "unrequest_changes",
    "comments",
    "add_comment",
    "diff",
    "commits",
    "tasks",
    "default_reviewers",
    "get_default_reviewer",
    "effective_default_reviewers",
    "add_default_reviewer",
    "remove_default_reviewer",
    "get_comment",
    "update_comment",
    "delete_comment",
    "resolve_comment",
    "unresolve_comment",
    "create_task",
    "get_task",
    "update_task",
    "delete_task",
    "activity",
    "pr_activity",
    "diffstat",
    "patch",
    "statuses",
    "user_prs",
    "merge_task_status",
    "PullrequestState",
]


def list(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    state: PullrequestState | Unset = UNSET,
    pagelen: int = 25,
) -> list[Pullrequest]:
    """Sync version of :func:`~bb.cloud.sdk.prs.list`."""
    return asyncio.run(_async.list(client, workspace, repo_slug, state=state, pagelen=pagelen))


def get(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int) -> Pullrequest | None:
    """Sync version of :func:`~bb.cloud.sdk.prs.get`."""
    return asyncio.run(_async.get(client, workspace, repo_slug, pull_request_id))


def create(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: Pullrequest | Unset = UNSET,
) -> Pullrequest | None:
    """Sync version of :func:`~bb.cloud.sdk.prs.create`."""
    return asyncio.run(_async.create(client, workspace, repo_slug, body=body))


def update(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    *,
    body: Pullrequest | Unset = UNSET,
) -> Pullrequest | None:
    """Sync version of :func:`~bb.cloud.sdk.prs.update`."""
    return asyncio.run(_async.update(client, workspace, repo_slug, pull_request_id, body=body))


def merge(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    *,
    body: PullRequestMergeParameters | Unset = UNSET,
    async_merge: bool | Unset = UNSET,
) -> Pullrequest | None:
    """Sync version of :func:`~bb.cloud.sdk.prs.merge`."""
    return asyncio.run(_async.merge(client, workspace, repo_slug, pull_request_id, body=body, async_merge=async_merge))


def approve(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int) -> Participant | None:
    """Sync version of :func:`~bb.cloud.sdk.prs.approve`."""
    return asyncio.run(_async.approve(client, workspace, repo_slug, pull_request_id))


def unapprove(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int) -> None:
    """Sync version of :func:`~bb.cloud.sdk.prs.unapprove`."""
    asyncio.run(_async.unapprove(client, workspace, repo_slug, pull_request_id))


def decline(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int) -> Pullrequest | None:
    """Sync version of :func:`~bb.cloud.sdk.prs.decline`."""
    return asyncio.run(_async.decline(client, workspace, repo_slug, pull_request_id))


def request_changes(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int) -> Participant | None:
    """Sync version of :func:`~bb.cloud.sdk.prs.request_changes`."""
    return asyncio.run(_async.request_changes(client, workspace, repo_slug, pull_request_id))


def unrequest_changes(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int) -> None:
    """Sync version of :func:`~bb.cloud.sdk.prs.unrequest_changes`."""
    asyncio.run(_async.unrequest_changes(client, workspace, repo_slug, pull_request_id))


def comments(
    client: BBClient, workspace: str, repo_slug: str, pull_request_id: int, *, pagelen: int = 25
) -> list[PullRequestComment]:
    """Sync version of :func:`~bb.cloud.sdk.prs.comments`."""
    return asyncio.run(_async.comments(client, workspace, repo_slug, pull_request_id, pagelen=pagelen))


def add_comment(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    *,
    body: PullRequestComment | Unset = UNSET,
) -> PullRequestComment | None:
    """Sync version of :func:`~bb.cloud.sdk.prs.add_comment`."""
    return asyncio.run(_async.add_comment(client, workspace, repo_slug, pull_request_id, body=body))


def diff(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int) -> str | None:
    """Sync version of :func:`~bb.cloud.sdk.prs.diff`."""
    return asyncio.run(_async.diff(client, workspace, repo_slug, pull_request_id))


def commits(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int, *, pagelen: int = 25) -> list[Any]:
    """Sync version of :func:`~bb.cloud.sdk.prs.commits`."""
    return asyncio.run(_async.commits(client, workspace, repo_slug, pull_request_id, pagelen=pagelen))


def tasks(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int, *, pagelen: int = 25) -> list[Any]:
    """Sync version of :func:`~bb.cloud.sdk.prs.tasks`."""
    return asyncio.run(_async.tasks(client, workspace, repo_slug, pull_request_id, pagelen=pagelen))


def default_reviewers(client: BBClient, workspace: str, repo_slug: str, *, pagelen: int = 25) -> list[Any]:
    """Sync version of :func:`~bb.cloud.sdk.prs.default_reviewers`."""
    return asyncio.run(_async.default_reviewers(client, workspace, repo_slug, pagelen=pagelen))


def get_default_reviewer(client: BBClient, workspace: str, repo_slug: str, target_username: str) -> Any | None:
    """Sync version of :func:`~bb.cloud.sdk.prs.get_default_reviewer`."""
    return asyncio.run(_async.get_default_reviewer(client, workspace, repo_slug, target_username))


def effective_default_reviewers(client: BBClient, workspace: str, repo_slug: str, *, pagelen: int = 25) -> list[Any]:
    """Sync version of :func:`~bb.cloud.sdk.prs.effective_default_reviewers`."""
    return asyncio.run(_async.effective_default_reviewers(client, workspace, repo_slug, pagelen=pagelen))


def add_default_reviewer(client: BBClient, workspace: str, repo_slug: str, target_username: str) -> None:
    """Sync version of :func:`~bb.cloud.sdk.prs.add_default_reviewer`."""
    asyncio.run(_async.add_default_reviewer(client, workspace, repo_slug, target_username))


def remove_default_reviewer(client: BBClient, workspace: str, repo_slug: str, target_username: str) -> None:
    """Sync version of :func:`~bb.cloud.sdk.prs.remove_default_reviewer`."""
    asyncio.run(_async.remove_default_reviewer(client, workspace, repo_slug, target_username))


def get_comment(
    client: BBClient, workspace: str, repo_slug: str, pull_request_id: int, comment_id: int
) -> PullRequestComment | None:
    """Sync version of :func:`~bb.cloud.sdk.prs.get_comment`."""
    return asyncio.run(_async.get_comment(client, workspace, repo_slug, pull_request_id, comment_id))


def update_comment(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    comment_id: int,
    *,
    body: PullRequestComment | Unset = UNSET,
) -> PullRequestComment | None:
    """Sync version of :func:`~bb.cloud.sdk.prs.update_comment`."""
    return asyncio.run(_async.update_comment(client, workspace, repo_slug, pull_request_id, comment_id, body=body))


def delete_comment(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int, comment_id: int) -> None:
    """Sync version of :func:`~bb.cloud.sdk.prs.delete_comment`."""
    asyncio.run(_async.delete_comment(client, workspace, repo_slug, pull_request_id, comment_id))


def resolve_comment(
    client: BBClient, workspace: str, repo_slug: str, pull_request_id: int, comment_id: int
) -> Any | None:
    """Sync version of :func:`~bb.cloud.sdk.prs.resolve_comment`."""
    return asyncio.run(_async.resolve_comment(client, workspace, repo_slug, pull_request_id, comment_id))


def unresolve_comment(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int, comment_id: int) -> None:
    """Sync version of :func:`~bb.cloud.sdk.prs.unresolve_comment`."""
    asyncio.run(_async.unresolve_comment(client, workspace, repo_slug, pull_request_id, comment_id))


def create_task(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    *,
    body: Unset = UNSET,
) -> Any | None:
    """Sync version of :func:`~bb.cloud.sdk.prs.create_task`."""
    return asyncio.run(_async.create_task(client, workspace, repo_slug, pull_request_id, body=body))


def get_task(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int, task_id: int) -> Any | None:
    """Sync version of :func:`~bb.cloud.sdk.prs.get_task`."""
    return asyncio.run(_async.get_task(client, workspace, repo_slug, pull_request_id, task_id))


def update_task(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    task_id: int,
    *,
    body: Unset = UNSET,
) -> Any | None:
    """Sync version of :func:`~bb.cloud.sdk.prs.update_task`."""
    return asyncio.run(_async.update_task(client, workspace, repo_slug, pull_request_id, task_id, body=body))


def delete_task(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int, task_id: int) -> None:
    """Sync version of :func:`~bb.cloud.sdk.prs.delete_task`."""
    asyncio.run(_async.delete_task(client, workspace, repo_slug, pull_request_id, task_id))


def activity(client: BBClient, workspace: str, repo_slug: str, *, pagelen: int = 25) -> list[Any]:
    """Sync version of :func:`~bb.cloud.sdk.prs.activity`."""
    return asyncio.run(_async.activity(client, workspace, repo_slug, pagelen=pagelen))


def pr_activity(
    client: BBClient, workspace: str, repo_slug: str, pull_request_id: int, *, pagelen: int = 25
) -> list[Any]:
    """Sync version of :func:`~bb.cloud.sdk.prs.pr_activity`."""
    return asyncio.run(_async.pr_activity(client, workspace, repo_slug, pull_request_id, pagelen=pagelen))


def diffstat(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int) -> Any:
    """Sync version of :func:`~bb.cloud.sdk.prs.diffstat`."""
    return asyncio.run(_async.diffstat(client, workspace, repo_slug, pull_request_id))


def patch(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int) -> str | None:
    """Sync version of :func:`~bb.cloud.sdk.prs.patch`."""
    return asyncio.run(_async.patch(client, workspace, repo_slug, pull_request_id))


def statuses(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int, *, pagelen: int = 25) -> list[Any]:
    """Sync version of :func:`~bb.cloud.sdk.prs.statuses`."""
    return asyncio.run(_async.statuses(client, workspace, repo_slug, pull_request_id, pagelen=pagelen))


def user_prs(client: BBClient, workspace: str, selected_user: str, *, pagelen: int = 25) -> list[Pullrequest]:
    """Sync version of :func:`~bb.cloud.sdk.prs.user_prs`."""
    return asyncio.run(_async.user_prs(client, workspace, selected_user, pagelen=pagelen))


def merge_task_status(
    client: BBClient, workspace: str, repo_slug: str, pull_request_id: int, task_id: str
) -> Any | None:
    """Sync version of :func:`~bb.cloud.sdk.prs.merge_task_status`."""
    return asyncio.run(_async.merge_task_status(client, workspace, repo_slug, pull_request_id, task_id))
