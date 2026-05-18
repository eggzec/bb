from __future__ import annotations

from typing import Any

from bb.cloud.api.pullrequests import (
    delete_repositories_workspace_repo_slug_default_reviewers_target_username,
    delete_repositories_workspace_repo_slug_pullrequests_pull_request_id_approve,
    delete_repositories_workspace_repo_slug_pullrequests_pull_request_id_comments_comment_id,
    delete_repositories_workspace_repo_slug_pullrequests_pull_request_id_comments_comment_id_resolve,
    delete_repositories_workspace_repo_slug_pullrequests_pull_request_id_request_changes,
    delete_repositories_workspace_repo_slug_pullrequests_pull_request_id_tasks_task_id,
    get_repositories_workspace_repo_slug_default_reviewers,
    get_repositories_workspace_repo_slug_default_reviewers_target_username,
    get_repositories_workspace_repo_slug_effective_default_reviewers,
    get_repositories_workspace_repo_slug_pullrequests,
    get_repositories_workspace_repo_slug_pullrequests_activity,
    get_repositories_workspace_repo_slug_pullrequests_pull_request_id,
    get_repositories_workspace_repo_slug_pullrequests_pull_request_id_activity,
    get_repositories_workspace_repo_slug_pullrequests_pull_request_id_comments,
    get_repositories_workspace_repo_slug_pullrequests_pull_request_id_comments_comment_id,
    get_repositories_workspace_repo_slug_pullrequests_pull_request_id_commits,
    get_repositories_workspace_repo_slug_pullrequests_pull_request_id_diff,
    get_repositories_workspace_repo_slug_pullrequests_pull_request_id_diffstat,
    get_repositories_workspace_repo_slug_pullrequests_pull_request_id_merge_task_status_task_id,
    get_repositories_workspace_repo_slug_pullrequests_pull_request_id_patch,
    get_repositories_workspace_repo_slug_pullrequests_pull_request_id_statuses,
    get_repositories_workspace_repo_slug_pullrequests_pull_request_id_tasks,
    get_repositories_workspace_repo_slug_pullrequests_pull_request_id_tasks_task_id,
    get_workspaces_workspace_pullrequests_selected_user,
    post_repositories_workspace_repo_slug_pullrequests,
    post_repositories_workspace_repo_slug_pullrequests_pull_request_id_approve,
    post_repositories_workspace_repo_slug_pullrequests_pull_request_id_comments,
    post_repositories_workspace_repo_slug_pullrequests_pull_request_id_comments_comment_id_resolve,
    post_repositories_workspace_repo_slug_pullrequests_pull_request_id_decline,
    post_repositories_workspace_repo_slug_pullrequests_pull_request_id_merge,
    post_repositories_workspace_repo_slug_pullrequests_pull_request_id_request_changes,
    post_repositories_workspace_repo_slug_pullrequests_pull_request_id_tasks,
    put_repositories_workspace_repo_slug_default_reviewers_target_username,
    put_repositories_workspace_repo_slug_pullrequests_pull_request_id,
    put_repositories_workspace_repo_slug_pullrequests_pull_request_id_comments_comment_id,
    put_repositories_workspace_repo_slug_pullrequests_pull_request_id_tasks_task_id,
)
from bb.cloud.models.error import Error
from bb.cloud.models.get_repositories_workspace_repo_slug_pullrequests_state import (
    GetRepositoriesWorkspaceRepoSlugPullrequestsState,
)
from bb.cloud.models.participant import Participant
from bb.cloud.models.pull_request_merge_parameters import PullRequestMergeParameters
from bb.cloud.models.pullrequest import Pullrequest
from bb.cloud.models.pull_request_task_create import PullRequestTaskCreate
from bb.cloud.models.pull_request_task_update import PullRequestTaskUpdate
from bb.cloud.models.pullrequest_comment import PullrequestComment as PullRequestComment
from bb.cloud.sdk._auth_validation import AuthMethod, require_auth
from bb.cloud.sdk._client import BBClient
from bb.cloud.sdk._pagination import async_paginate
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

# Re-exported for callers
PullrequestState = GetRepositoriesWorkspaceRepoSlugPullrequestsState


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def list(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    state: GetRepositoriesWorkspaceRepoSlugPullrequestsState | Unset = UNSET,
    pagelen: int = 25,
) -> list[Pullrequest] | Error:
    """List all pull requests for a repository across all pages.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
        repo_slug: Repository slug or UUID.
        state: Filter by pull request state. Pass a
            :class:`~bb.cloud.models.get_repositories_workspace_repo_slug_pullrequests_state.GetRepositoriesWorkspaceRepoSlugPullrequestsState`
            value, or omit to return all states.
        pagelen: Number of results per page. Defaults to ``25``.

    Returns:
        All pull requests across all pages matching the given filters.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import prs

        client = BBClient.from_env()
        result = await prs.list(client, workspace="myworkspace", repo_slug="myrepo")
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/pullrequests
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-get>`_
    """
    result = await async_paginate(
        get_repositories_workspace_repo_slug_pullrequests.asyncio,
        workspace,
        repo_slug,
        client=client.auth,
        state=state,
        pagelen=pagelen,
    )

    if isinstance(result, Error):
        return result

    return [item for item in result if isinstance(item, Pullrequest)]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int) -> Pullrequest | Error | None:
    """Fetch a single pull request by ID.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
        repo_slug: Repository slug or UUID.
        pull_request_id: Numeric pull request ID.

    Returns:
        The :class:`~bb.cloud.models.pullrequest.Pullrequest`, or ``None`` if not found.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import prs

        client = BBClient.from_env()
        pr = await prs.get(client, workspace="myworkspace", repo_slug="myrepo", pull_request_id=42)
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-get>`_
    """
    result = await get_repositories_workspace_repo_slug_pullrequests_pull_request_id.asyncio(
        workspace, repo_slug, pull_request_id, client=client.auth
    )
    if isinstance(result, (Pullrequest, Error)):
        return result
    return None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def create(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: Pullrequest | Unset = UNSET,
) -> Pullrequest | Error | None:
    """Create a new pull request.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
        repo_slug: Repository slug or UUID.
        body: Pull request payload. Use :class:`~bb.cloud.models.pullrequest.Pullrequest`
            populated with at minimum ``title``, ``source``, and ``destination``.

    Returns:
        The created :class:`~bb.cloud.models.pullrequest.Pullrequest`, or ``None`` on error.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import prs
        from bb.cloud.models.pullrequest import Pullrequest

        client = BBClient.from_env()
        pr = await prs.create(client, workspace="myworkspace", repo_slug="myrepo", body=Pullrequest(...))
        ```

    References:
        `POST /2.0/repositories/{workspace}/{repo_slug}/pullrequests
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-post>`_
    """
    result = await post_repositories_workspace_repo_slug_pullrequests.asyncio(
        workspace, repo_slug, client=client.auth, body=body
    )
    if isinstance(result, (Pullrequest, Error)):
        return result
    return None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def update(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    *,
    body: Pullrequest | Unset = UNSET,
) -> Pullrequest | Error | None:
    """Update an existing pull request.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
        repo_slug: Repository slug or UUID.
        pull_request_id: Numeric pull request ID.
        body: Updated pull request payload.

    Returns:
        The updated :class:`~bb.cloud.models.pullrequest.Pullrequest`, or ``None`` on error.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import prs
        from bb.cloud.models.pullrequest import Pullrequest

        client = BBClient.from_env()
        pr = await prs.update(
            client, workspace="myworkspace", repo_slug="myrepo", pull_request_id=42,
            body=Pullrequest(title="Updated title"),
        )
        ```

    References:
        `PUT /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-put>`_
    """
    result = await put_repositories_workspace_repo_slug_pullrequests_pull_request_id.asyncio(
        workspace, repo_slug, pull_request_id, client=client.auth, body=body
    )
    if isinstance(result, (Pullrequest, Error)):
        return result
    return None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def merge(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    *,
    body: PullRequestMergeParameters | Unset = UNSET,
    async_merge: bool | Unset = UNSET,
) -> Pullrequest | Error | None:
    """Merge a pull request.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
        repo_slug: Repository slug or UUID.
        pull_request_id: Numeric pull request ID.
        body: Merge parameters such as merge strategy and commit message. Use
            :class:`~bb.cloud.models.pull_request_merge_parameters.PullRequestMergeParameters`.
        async_merge: When ``True``, the merge is performed asynchronously. Poll
            :func:`merge_task_status` for completion.

    Returns:
        The merged :class:`~bb.cloud.models.pullrequest.Pullrequest`, or ``None`` if the merge
        was initiated asynchronously or an error occurred.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import prs

        client = BBClient.from_env()
        pr = await prs.merge(client, workspace="myworkspace", repo_slug="myrepo", pull_request_id=42)
        ```

    References:
        `POST /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/merge
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-merge-post>`_
    """
    result = await post_repositories_workspace_repo_slug_pullrequests_pull_request_id_merge.asyncio(
        workspace,
        repo_slug,
        pull_request_id,
        client=client.auth,
        body=body,
        async_=async_merge,
    )
    if isinstance(result, (Pullrequest, Error)):
        return result
    return None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def approve(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int) -> Participant | Error | None:
    """Approve a pull request.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
        repo_slug: Repository slug or UUID.
        pull_request_id: Numeric pull request ID.

    Returns:
        The :class:`~bb.cloud.models.participant.Participant` record for the approving user,
        or ``None`` on error.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import prs

        client = BBClient.from_env()
        participant = await prs.approve(
            client, workspace="myworkspace", repo_slug="myrepo", pull_request_id=42
        )
        ```

    References:
        `POST /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/approve
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-approve-post>`_
    """
    result = await post_repositories_workspace_repo_slug_pullrequests_pull_request_id_approve.asyncio(
        workspace, repo_slug, pull_request_id, client=client.auth
    )
    if isinstance(result, (Participant, Error)):
        return result
    return None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def unapprove(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int) -> None:
    """Remove an approval from a pull request.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
        repo_slug: Repository slug or UUID.
        pull_request_id: Numeric pull request ID.

    Returns:
        None.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import prs

        client = BBClient.from_env()
        await prs.unapprove(client, workspace="myworkspace", repo_slug="myrepo", pull_request_id=42)
        ```

    References:
        `DELETE /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/approve
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-approve-delete>`_
    """
    await delete_repositories_workspace_repo_slug_pullrequests_pull_request_id_approve.asyncio(
        workspace, repo_slug, pull_request_id, client=client.auth
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def decline(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int) -> Pullrequest | Error | None:
    """Decline a pull request.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
        repo_slug: Repository slug or UUID.
        pull_request_id: Numeric pull request ID.

    Returns:
        The updated :class:`~bb.cloud.models.pullrequest.Pullrequest` in DECLINED state,
        or ``None`` on error.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import prs

        client = BBClient.from_env()
        pr = await prs.decline(
            client, workspace="myworkspace", repo_slug="myrepo", pull_request_id=42
        )
        ```

    References:
        `POST /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/decline
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-decline-post>`_
    """
    result = await post_repositories_workspace_repo_slug_pullrequests_pull_request_id_decline.asyncio(
        workspace, repo_slug, pull_request_id, client=client.auth
    )
    if isinstance(result, (Pullrequest, Error)):
        return result
    return None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def request_changes(
    client: BBClient, workspace: str, repo_slug: str, pull_request_id: int
) -> Participant | Error | None:
    """Request changes on a pull request.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
        repo_slug: Repository slug or UUID.
        pull_request_id: Numeric pull request ID.

    Returns:
        The :class:`~bb.cloud.models.participant.Participant` record for the requesting user,
        or ``None`` on error.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import prs

        client = BBClient.from_env()
        participant = await prs.request_changes(
            client, workspace="myworkspace", repo_slug="myrepo", pull_request_id=42
        )
        ```

    References:
        `POST /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/request-changes
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-request-changes-post>`_
    """
    result = await post_repositories_workspace_repo_slug_pullrequests_pull_request_id_request_changes.asyncio(
        workspace, repo_slug, pull_request_id, client=client.auth
    )
    if isinstance(result, (Participant, Error)):
        return result
    return None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def unrequest_changes(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int) -> None:
    """Remove a request for changes from a pull request.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
        repo_slug: Repository slug or UUID.
        pull_request_id: Numeric pull request ID.

    Returns:
        None.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import prs

        client = BBClient.from_env()
        await prs.unrequest_changes(
            client, workspace="myworkspace", repo_slug="myrepo", pull_request_id=42
        )
        ```

    References:
        `DELETE /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/request-changes
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-request-changes-delete>`_
    """
    await delete_repositories_workspace_repo_slug_pullrequests_pull_request_id_request_changes.asyncio(
        workspace, repo_slug, pull_request_id, client=client.auth
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def comments(
    client: BBClient, workspace: str, repo_slug: str, pull_request_id: int, *, pagelen: int = 25
) -> list[PullRequestComment] | Error:
    """List all comments on a pull request across all pages.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
        repo_slug: Repository slug or UUID.
        pull_request_id: Numeric pull request ID.
        pagelen: Number of results per page. Defaults to ``25``.

    Returns:
        All :class:`~bb.cloud.models.pullrequest_comment.PullrequestComment` objects across
        all pages.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import prs

        client = BBClient.from_env()
        result = await prs.comments(
            client, workspace="myworkspace", repo_slug="myrepo", pull_request_id=42
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-comments-get>`_
    """
    result = await async_paginate(
        get_repositories_workspace_repo_slug_pullrequests_pull_request_id_comments.asyncio,
        workspace,
        repo_slug,
        pull_request_id,
        client=client.auth,
        pagelen=pagelen,
    )

    if isinstance(result, Error):
        return result

    return [item for item in result if isinstance(item, PullRequestComment)]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def add_comment(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    *,
    body: PullRequestComment | Unset = UNSET,
) -> PullRequestComment | Error | None:
    """Add a comment to a pull request.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
        repo_slug: Repository slug or UUID.
        pull_request_id: Numeric pull request ID.
        body: Comment payload. Use
            :class:`~bb.cloud.models.pullrequest_comment.PullrequestComment`.

    Returns:
        The created :class:`~bb.cloud.models.pullrequest_comment.PullrequestComment`,
        or ``None`` on error.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import prs

        client = BBClient.from_env()
        comment = await prs.add_comment(
            client, workspace="myworkspace", repo_slug="myrepo", pull_request_id=42,
            body=PullrequestComment(content=...),
        )
        ```

    References:
        `POST /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-comments-post>`_
    """
    response = await post_repositories_workspace_repo_slug_pullrequests_pull_request_id_comments.asyncio_detailed(
        workspace, repo_slug, pull_request_id, client=client.auth, body=body
    )
    if response.status_code.value in (200, 201):
        import json as _json
        return PullRequestComment.from_dict(_json.loads(response.content))
    if isinstance(response.parsed, Error):
        return response.parsed
    return None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def diff(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int) -> str | Error | None:
    """Return the unified diff of a pull request as a string.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
        repo_slug: Repository slug or UUID.
        pull_request_id: Numeric pull request ID.

    Returns:
        The unified diff as a plain string, or ``None`` on error.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import prs

        client = BBClient.from_env()
        unified_diff = await prs.diff(
            client, workspace="myworkspace", repo_slug="myrepo", pull_request_id=42
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/diff
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-diff-get>`_
    """
    response = await get_repositories_workspace_repo_slug_pullrequests_pull_request_id_diff.asyncio_detailed(
        workspace, repo_slug, pull_request_id, client=client.auth
    )
    if response.status_code.value in (200, 302):
        return response.content.decode()
    if isinstance(response.parsed, Error):
        return response.parsed
    return None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def commits(
    client: BBClient, workspace: str, repo_slug: str, pull_request_id: int, *, pagelen: int = 25
) -> list[Any] | Error:
    """List all commits included in a pull request across all pages.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
        repo_slug: Repository slug or UUID.
        pull_request_id: Numeric pull request ID.
        pagelen: Number of results per page. Defaults to ``25``.

    Returns:
        All commit objects across all pages.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import prs

        client = BBClient.from_env()
        result = await prs.commits(
            client, workspace="myworkspace", repo_slug="myrepo", pull_request_id=42
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/commits
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-commits-get>`_
    """
    result = await async_paginate(
        get_repositories_workspace_repo_slug_pullrequests_pull_request_id_commits.asyncio,
        workspace,
        repo_slug,
        pull_request_id,
        client=client.auth,
        pagelen=pagelen,
    )

    if isinstance(result, Error):
        return result

    return [x for x in result]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def tasks(
    client: BBClient, workspace: str, repo_slug: str, pull_request_id: int, *, pagelen: int = 25
) -> list[Any] | Error:
    """List all tasks on a pull request across all pages.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
        repo_slug: Repository slug or UUID.
        pull_request_id: Numeric pull request ID.
        pagelen: Number of results per page. Defaults to ``25``.

    Returns:
        All task objects across all pages.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import prs

        client = BBClient.from_env()
        result = await prs.tasks(
            client, workspace="myworkspace", repo_slug="myrepo", pull_request_id=42
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/tasks
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-tasks-get>`_
    """
    result = await async_paginate(
        get_repositories_workspace_repo_slug_pullrequests_pull_request_id_tasks.asyncio,
        workspace,
        repo_slug,
        pull_request_id,
        client=client.auth,
        pagelen=pagelen,
    )

    if isinstance(result, Error):
        return result

    return [x for x in result]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def default_reviewers(
    client: BBClient, workspace: str, repo_slug: str, *, pagelen: int = 25
) -> list[Any] | Error:
    """List all default reviewers for a repository across all pages.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
        repo_slug: Repository slug or UUID.
        pagelen: Number of results per page. Defaults to ``25``.

    Returns:
        All default reviewer objects across all pages.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import prs

        client = BBClient.from_env()
        result = await prs.default_reviewers(
            client, workspace="myworkspace", repo_slug="myrepo"
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/default-reviewers
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-default-reviewers-get>`_
    """
    result = await async_paginate(
        get_repositories_workspace_repo_slug_default_reviewers.asyncio,
        workspace,
        repo_slug,
        client=client.auth,
        pagelen=pagelen,
    )

    if isinstance(result, Error):
        return result

    return [x for x in result]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def add_default_reviewer(client: BBClient, workspace: str, repo_slug: str, target_username: str) -> None:
    """Add a user as a default reviewer for a repository.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
        repo_slug: Repository slug or UUID.
        target_username: The account ID or username of the user to add.

    Returns:
        None.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import prs

        client = BBClient.from_env()
        await prs.add_default_reviewer(
            client, workspace="myworkspace", repo_slug="myrepo", target_username="jsmith"
        )
        ```

    References:
        `PUT /2.0/repositories/{workspace}/{repo_slug}/default-reviewers/{target_username}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-default-reviewers-target-username-put>`_
    """
    await put_repositories_workspace_repo_slug_default_reviewers_target_username.asyncio(
        workspace, repo_slug, target_username, client=client.auth
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def remove_default_reviewer(client: BBClient, workspace: str, repo_slug: str, target_username: str) -> None:
    """Remove a user from the default reviewers for a repository.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
        repo_slug: Repository slug or UUID.
        target_username: The account ID or username of the user to remove.

    Returns:
        None.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import prs

        client = BBClient.from_env()
        await prs.remove_default_reviewer(
            client, workspace="myworkspace", repo_slug="myrepo", target_username="jsmith"
        )
        ```

    References:
        `DELETE /2.0/repositories/{workspace}/{repo_slug}/default-reviewers/{target_username}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-default-reviewers-target-username-delete>`_
    """
    await delete_repositories_workspace_repo_slug_default_reviewers_target_username.asyncio(
        workspace, repo_slug, target_username, client=client.auth
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get_default_reviewer(
    client: BBClient, workspace: str, repo_slug: str, target_username: str
) -> Any | Error | None:
    """Fetch details of a specific default reviewer for a repository.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
        repo_slug: Repository slug or UUID.
        target_username: The account ID or username of the reviewer.

    Returns:
        The reviewer object, or ``None`` if not found.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import prs

        client = BBClient.from_env()
        reviewer = await prs.get_default_reviewer(
            client, workspace="myworkspace", repo_slug="myrepo", target_username="jsmith"
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/default-reviewers/{target_username}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-default-reviewers-target-username-get>`_
    """
    return await get_repositories_workspace_repo_slug_default_reviewers_target_username.asyncio(
        workspace, repo_slug, target_username, client=client.auth
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def effective_default_reviewers(
    client: BBClient, workspace: str, repo_slug: str, *, pagelen: int = 25
) -> list[Any] | Error:
    """List the effective default reviewers for a repository across all pages.

    Effective reviewers include those inherited from the parent project as well as
    those set directly on the repository.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
        repo_slug: Repository slug or UUID.
        pagelen: Number of results per page. Defaults to ``25``.

    Returns:
        All effective default reviewer objects across all pages.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import prs

        client = BBClient.from_env()
        result = await prs.effective_default_reviewers(
            client, workspace="myworkspace", repo_slug="myrepo"
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/effective-default-reviewers
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-effective-default-reviewers-get>`_
    """
    result = await async_paginate(
        get_repositories_workspace_repo_slug_effective_default_reviewers.asyncio,
        workspace,
        repo_slug,
        client=client.auth,
        pagelen=pagelen,
    )

    if isinstance(result, Error):
        return result

    return [x for x in result]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get_comment(
    client: BBClient, workspace: str, repo_slug: str, pull_request_id: int, comment_id: int
) -> PullRequestComment | Error | None:
    """Fetch a single comment on a pull request.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
        repo_slug: Repository slug or UUID.
        pull_request_id: Numeric pull request ID.
        comment_id: Numeric comment ID.

    Returns:
        The :class:`~bb.cloud.models.pullrequest_comment.PullrequestComment`,
        or ``None`` if not found.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import prs

        client = BBClient.from_env()
        comment = await prs.get_comment(
            client, workspace="myworkspace", repo_slug="myrepo",
            pull_request_id=42, comment_id=101,
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments/{comment_id}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-comments-comment-id-get>`_
    """
    result = await get_repositories_workspace_repo_slug_pullrequests_pull_request_id_comments_comment_id.asyncio(
        workspace, repo_slug, pull_request_id, comment_id, client=client.auth
    )
    if isinstance(result, (PullRequestComment, Error)):
        return result
    return None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def update_comment(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    comment_id: int,
    *,
    body: PullRequestComment | Unset = UNSET,
) -> PullRequestComment | Error | None:
    """Update a comment on a pull request.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
        repo_slug: Repository slug or UUID.
        pull_request_id: Numeric pull request ID.
        comment_id: Numeric comment ID.
        body: Updated comment payload.

    Returns:
        The updated :class:`~bb.cloud.models.pullrequest_comment.PullrequestComment`,
        or ``None`` on error.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import prs

        client = BBClient.from_env()
        comment = await prs.update_comment(
            client, workspace="myworkspace", repo_slug="myrepo",
            pull_request_id=42, comment_id=101, body=PullrequestComment(content=...),
        )
        ```

    References:
        `PUT /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments/{comment_id}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-comments-comment-id-put>`_
    """
    result = await put_repositories_workspace_repo_slug_pullrequests_pull_request_id_comments_comment_id.asyncio(
        workspace, repo_slug, pull_request_id, comment_id, client=client.auth, body=body
    )
    if isinstance(result, (PullRequestComment, Error)):
        return result
    return None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def delete_comment(
    client: BBClient, workspace: str, repo_slug: str, pull_request_id: int, comment_id: int
) -> None:
    """Delete a comment on a pull request.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
        repo_slug: Repository slug or UUID.
        pull_request_id: Numeric pull request ID.
        comment_id: Numeric comment ID.

    Returns:
        None.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import prs

        client = BBClient.from_env()
        await prs.delete_comment(
            client, workspace="myworkspace", repo_slug="myrepo",
            pull_request_id=42, comment_id=101,
        )
        ```

    References:
        `DELETE /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments/{comment_id}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-comments-comment-id-delete>`_
    """
    await delete_repositories_workspace_repo_slug_pullrequests_pull_request_id_comments_comment_id.asyncio(
        workspace, repo_slug, pull_request_id, comment_id, client=client.auth
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def resolve_comment(
    client: BBClient, workspace: str, repo_slug: str, pull_request_id: int, comment_id: int
) -> Any | Error | None:
    """Mark a pull request comment as resolved.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
        repo_slug: Repository slug or UUID.
        pull_request_id: Numeric pull request ID.
        comment_id: Numeric comment ID.

    Returns:
        The API response object, or ``None`` on error.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import prs

        client = BBClient.from_env()
        await prs.resolve_comment(
            client, workspace="myworkspace", repo_slug="myrepo",
            pull_request_id=42, comment_id=101,
        )
        ```

    References:
        `POST /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments/{comment_id}/resolve
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-comments-comment-id-resolve-post>`_
    """
    return await post_repositories_workspace_repo_slug_pullrequests_pull_request_id_comments_comment_id_resolve.asyncio(
        workspace, repo_slug, pull_request_id, comment_id, client=client.auth
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def unresolve_comment(
    client: BBClient, workspace: str, repo_slug: str, pull_request_id: int, comment_id: int
) -> None:
    """Unmark a pull request comment as resolved.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
        repo_slug: Repository slug or UUID.
        pull_request_id: Numeric pull request ID.
        comment_id: Numeric comment ID.

    Returns:
        None.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import prs

        client = BBClient.from_env()
        await prs.unresolve_comment(
            client, workspace="myworkspace", repo_slug="myrepo",
            pull_request_id=42, comment_id=101,
        )
        ```

    References:
        `DELETE /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments/{comment_id}/resolve
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-comments-comment-id-resolve-delete>`_
    """
    await delete_repositories_workspace_repo_slug_pullrequests_pull_request_id_comments_comment_id_resolve.asyncio(
        workspace, repo_slug, pull_request_id, comment_id, client=client.auth
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def create_task(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    *,
    body: PullRequestTaskCreate,
) -> Any | Error | None:
    """Create a task on a pull request.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
        repo_slug: Repository slug or UUID.
        pull_request_id: Numeric pull request ID.
        body: Task payload — a :class:`~bb.cloud.models.pull_request_task_create.PullRequestTaskCreate` object.

    Returns:
        The created task object, or ``None`` on error.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import prs

        client = BBClient.from_env()
        task = await prs.create_task(
            client, workspace="myworkspace", repo_slug="myrepo", pull_request_id=42
        )
        ```

    References:
        `POST /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/tasks
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-tasks-post>`_
    """
    return await post_repositories_workspace_repo_slug_pullrequests_pull_request_id_tasks.asyncio(
        workspace, repo_slug, pull_request_id, client=client.auth, body=body
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get_task(
    client: BBClient, workspace: str, repo_slug: str, pull_request_id: int, task_id: int
) -> Any | Error | None:
    """Fetch a single task on a pull request.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
        repo_slug: Repository slug or UUID.
        pull_request_id: Numeric pull request ID.
        task_id: Numeric task ID.

    Returns:
        The task object, or ``None`` if not found.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import prs

        client = BBClient.from_env()
        task = await prs.get_task(
            client, workspace="myworkspace", repo_slug="myrepo",
            pull_request_id=42, task_id=7,
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/tasks/{task_id}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-tasks-task-id-get>`_
    """
    return await get_repositories_workspace_repo_slug_pullrequests_pull_request_id_tasks_task_id.asyncio(
        workspace, repo_slug, pull_request_id, task_id, client=client.auth
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def update_task(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    task_id: int,
    *,
    body: PullRequestTaskUpdate,
) -> Any | Error | None:
    """Update a task on a pull request.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
        repo_slug: Repository slug or UUID.
        pull_request_id: Numeric pull request ID.
        task_id: Numeric task ID.
        body: Updated task payload — a :class:`~bb.cloud.models.pull_request_task_update.PullRequestTaskUpdate` object.

    Returns:
        The updated task object, or ``None`` on error.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import prs

        client = BBClient.from_env()
        task = await prs.update_task(
            client, workspace="myworkspace", repo_slug="myrepo",
            pull_request_id=42, task_id=7,
        )
        ```

    References:
        `PUT /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/tasks/{task_id}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-tasks-task-id-put>`_
    """
    return await put_repositories_workspace_repo_slug_pullrequests_pull_request_id_tasks_task_id.asyncio(
        workspace, repo_slug, pull_request_id, task_id, client=client.auth, body=body
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def delete_task(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int, task_id: int) -> None:
    """Delete a task from a pull request.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
        repo_slug: Repository slug or UUID.
        pull_request_id: Numeric pull request ID.
        task_id: Numeric task ID.

    Returns:
        None.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import prs

        client = BBClient.from_env()
        await prs.delete_task(
            client, workspace="myworkspace", repo_slug="myrepo",
            pull_request_id=42, task_id=7,
        )
        ```

    References:
        `DELETE /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/tasks/{task_id}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-tasks-task-id-delete>`_
    """
    await delete_repositories_workspace_repo_slug_pullrequests_pull_request_id_tasks_task_id.asyncio(
        workspace, repo_slug, pull_request_id, task_id, client=client.auth
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def activity(client: BBClient, workspace: str, repo_slug: str, *, pagelen: int = 25) -> list[Any] | Error:
    """List activity for all pull requests in a repository across all pages.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
        repo_slug: Repository slug or UUID.
        pagelen: Number of results per page. Defaults to ``25``.

    Returns:
        All activity event objects across all pages.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import prs

        client = BBClient.from_env()
        result = await prs.activity(client, workspace="myworkspace", repo_slug="myrepo")
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/pullrequests/activity
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-activity-get>`_
    """
    result = await async_paginate(
        get_repositories_workspace_repo_slug_pullrequests_activity.asyncio,
        workspace,
        repo_slug,
        client=client.auth,
        pagelen=pagelen,
    )

    if isinstance(result, Error):
        return result

    return [x for x in result]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def pr_activity(
    client: BBClient, workspace: str, repo_slug: str, pull_request_id: int, *, pagelen: int = 25
) -> list[Any] | Error:
    """List activity for a specific pull request across all pages.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
        repo_slug: Repository slug or UUID.
        pull_request_id: Numeric pull request ID.
        pagelen: Number of results per page. Defaults to ``25``.

    Returns:
        All activity event objects for the pull request across all pages.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import prs

        client = BBClient.from_env()
        result = await prs.pr_activity(
            client, workspace="myworkspace", repo_slug="myrepo", pull_request_id=42
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/activity
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-activity-get>`_
    """
    result = await async_paginate(
        get_repositories_workspace_repo_slug_pullrequests_pull_request_id_activity.asyncio,
        workspace,
        repo_slug,
        pull_request_id,
        client=client.auth,
        pagelen=pagelen,
    )

    if isinstance(result, Error):
        return result

    return [x for x in result]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def diffstat(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int) -> Any:
    """Return the diffstat (changed files summary) for a pull request.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
        repo_slug: Repository slug or UUID.
        pull_request_id: Numeric pull request ID.

    Returns:
        The diffstat object containing per-file change statistics.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import prs

        client = BBClient.from_env()
        stat = await prs.diffstat(
            client, workspace="myworkspace", repo_slug="myrepo", pull_request_id=42
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/diffstat
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-diffstat-get>`_
    """
    response = await get_repositories_workspace_repo_slug_pullrequests_pull_request_id_diffstat.asyncio_detailed(
        workspace, repo_slug, pull_request_id, client=client.auth
    )
    if response.status_code.value == 200:
        import json as _json
        return _json.loads(response.content)
    return response.parsed


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def patch(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int) -> str | Error | None:
    """Return the patch for a pull request as a string.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
        repo_slug: Repository slug or UUID.
        pull_request_id: Numeric pull request ID.

    Returns:
        The patch as a plain string, or ``None`` on error.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import prs

        client = BBClient.from_env()
        patch_text = await prs.patch(
            client, workspace="myworkspace", repo_slug="myrepo", pull_request_id=42
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/patch
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-patch-get>`_
    """
    response = await get_repositories_workspace_repo_slug_pullrequests_pull_request_id_patch.asyncio_detailed(
        workspace, repo_slug, pull_request_id, client=client.auth
    )
    if response.status_code.value in (200, 302):
        return response.content.decode()
    if isinstance(response.parsed, Error):
        return response.parsed
    return None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def statuses(
    client: BBClient, workspace: str, repo_slug: str, pull_request_id: int, *, pagelen: int = 25
) -> list[Any] | Error:
    """List all commit statuses for a pull request across all pages.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
        repo_slug: Repository slug or UUID.
        pull_request_id: Numeric pull request ID.
        pagelen: Number of results per page. Defaults to ``25``.

    Returns:
        All commit status objects across all pages.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import prs

        client = BBClient.from_env()
        result = await prs.statuses(
            client, workspace="myworkspace", repo_slug="myrepo", pull_request_id=42
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/statuses
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-statuses-get>`_
    """
    result = await async_paginate(
        get_repositories_workspace_repo_slug_pullrequests_pull_request_id_statuses.asyncio,
        workspace,
        repo_slug,
        pull_request_id,
        client=client.auth,
        pagelen=pagelen,
    )

    if isinstance(result, Error):
        return result

    return [x for x in result]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def user_prs(
    client: BBClient, workspace: str, selected_user: str, *, pagelen: int = 25
) -> list[Pullrequest] | Error:
    """List all pull requests authored by a user in a workspace across all pages.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
        selected_user: Account ID or username of the author to filter by.
        pagelen: Number of results per page. Defaults to ``25``.

    Returns:
        All :class:`~bb.cloud.models.pullrequest.Pullrequest` objects authored by the user
        across all pages.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import prs

        client = BBClient.from_env()
        result = await prs.user_prs(client, workspace="myworkspace", selected_user="jsmith")
        ```

    References:
        `GET /2.0/workspaces/{workspace}/pullrequests/{selected_user}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-workspaces/#api-workspaces-workspace-pullrequests-selected-user-get>`_
    """
    result = await async_paginate(
        get_workspaces_workspace_pullrequests_selected_user.asyncio,
        workspace,
        selected_user,
        client=client.auth,
        pagelen=pagelen,
    )

    if isinstance(result, Error):
        return result

    return [item for item in result if isinstance(item, Pullrequest)]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def merge_task_status(
    client: BBClient, workspace: str, repo_slug: str, pull_request_id: int, task_id: str
) -> Any | Error | None:
    """Return the status of an asynchronous merge task.

    Use this to poll for completion after calling :func:`merge` with ``async_merge=True``.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
        repo_slug: Repository slug or UUID.
        pull_request_id: Numeric pull request ID.
        task_id: Async merge task ID returned by the merge endpoint.

    Returns:
        The merge task status object, or ``None`` if not found.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import prs

        client = BBClient.from_env()
        status = await prs.merge_task_status(
            client, workspace="myworkspace", repo_slug="myrepo",
            pull_request_id=42, task_id="abc-task-123",
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/merge/task-status/{task_id}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-merge-task-status-task-id-get>`_
    """
    response = await get_repositories_workspace_repo_slug_pullrequests_pull_request_id_merge_task_status_task_id.asyncio_detailed(
        workspace, repo_slug, pull_request_id, task_id, client=client.auth
    )
    return response.parsed
