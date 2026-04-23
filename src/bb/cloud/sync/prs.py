from __future__ import annotations
import asyncio
from typing import Any
from bb.cloud.models.error import Error
from bb.cloud.models.get_repositories_workspace_repo_slug_pullrequests_state import GetRepositoriesWorkspaceRepoSlugPullrequestsState
from bb.cloud.models.participant import Participant
from bb.cloud.models.pull_request_merge_parameters import PullRequestMergeParameters
from bb.cloud.models.pullrequest import Pullrequest
from bb.cloud.models.pullrequest_comment import PullrequestComment as PullRequestComment
from bb.cloud.sdk._client import BBClient
from bb.cloud.types import UNSET, Unset
from bb.cloud.sdk import prs as _async
__all__ = ['list', 'get', 'create', 'update', 'merge', 'approve', 'unapprove', 'decline', 'request_changes', 'unrequest_changes', 'comments', 'add_comment', 'diff', 'commits', 'tasks', 'default_reviewers', 'get_default_reviewer', 'effective_default_reviewers', 'add_default_reviewer', 'remove_default_reviewer', 'get_comment', 'update_comment', 'delete_comment', 'resolve_comment', 'unresolve_comment', 'create_task', 'get_task', 'update_task', 'delete_task', 'activity', 'pr_activity', 'diffstat', 'patch', 'statuses', 'user_prs', 'merge_task_status', 'PullrequestState']
PullrequestState = GetRepositoriesWorkspaceRepoSlugPullrequestsState

def list(client: BBClient, workspace: str, repo_slug: str, *, state: GetRepositoriesWorkspaceRepoSlugPullrequestsState | Unset=UNSET, pagelen: int=25) -> list[Pullrequest] | Error:
    """List all pull requests for a repository across all pages.

Synchronous wrapper around :func:`~bb.cloud.sdk.prs.list`.

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
    result = prs.list(client, workspace="myworkspace", repo_slug="myrepo")
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/pullrequests
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.prs.list`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.list(client, workspace, repo_slug, state=state, pagelen=pagelen))

def get(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int) -> Pullrequest | Error | None:
    """Fetch a single pull request by ID.

Synchronous wrapper around :func:`~bb.cloud.sdk.prs.get`.

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
    pr = prs.get(client, workspace="myworkspace", repo_slug="myrepo", pull_request_id=42)
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.prs.get`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.get(client, workspace, repo_slug, pull_request_id))

def create(client: BBClient, workspace: str, repo_slug: str, *, body: Pullrequest | Unset=UNSET) -> Pullrequest | Error | None:
    """Create a new pull request.

Synchronous wrapper around :func:`~bb.cloud.sdk.prs.create`.

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
    pr = prs.create(client, workspace="myworkspace", repo_slug="myrepo", body=Pullrequest(...))
    ```

References:
    `POST /2.0/repositories/{workspace}/{repo_slug}/pullrequests
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-post>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.prs.create`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.create(client, workspace, repo_slug, body=body))

def update(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int, *, body: Pullrequest | Unset=UNSET) -> Pullrequest | Error | None:
    """Update an existing pull request.

Synchronous wrapper around :func:`~bb.cloud.sdk.prs.update`.

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
    pr = prs.update(
        client, workspace="myworkspace", repo_slug="myrepo", pull_request_id=42,
        body=Pullrequest(title="Updated title"),
    )
    ```

References:
    `PUT /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-put>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.prs.update`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.update(client, workspace, repo_slug, pull_request_id, body=body))

def merge(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int, *, body: PullRequestMergeParameters | Unset=UNSET, async_merge: bool | Unset=UNSET) -> Pullrequest | Error | None:
    """Merge a pull request.

Synchronous wrapper around :func:`~bb.cloud.sdk.prs.merge`.

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
    pr = prs.merge(client, workspace="myworkspace", repo_slug="myrepo", pull_request_id=42)
    ```

References:
    `POST /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/merge
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-merge-post>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.prs.merge`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.merge(client, workspace, repo_slug, pull_request_id, body=body, async_merge=async_merge))

def approve(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int) -> Participant | Error | None:
    """Approve a pull request.

Synchronous wrapper around :func:`~bb.cloud.sdk.prs.approve`.

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
    participant = prs.approve(
        client, workspace="myworkspace", repo_slug="myrepo", pull_request_id=42
    )
    ```

References:
    `POST /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/approve
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-approve-post>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.prs.approve`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.approve(client, workspace, repo_slug, pull_request_id))

def unapprove(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int) -> None:
    """Remove an approval from a pull request.

Synchronous wrapper around :func:`~bb.cloud.sdk.prs.unapprove`.

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
    prs.unapprove(client, workspace="myworkspace", repo_slug="myrepo", pull_request_id=42)
    ```

References:
    `DELETE /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/approve
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-approve-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.prs.unapprove`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.unapprove(client, workspace, repo_slug, pull_request_id))

def decline(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int) -> Pullrequest | Error | None:
    """Decline a pull request.

Synchronous wrapper around :func:`~bb.cloud.sdk.prs.decline`.

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
    pr = prs.decline(
        client, workspace="myworkspace", repo_slug="myrepo", pull_request_id=42
    )
    ```

References:
    `POST /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/decline
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-decline-post>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.prs.decline`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.decline(client, workspace, repo_slug, pull_request_id))

def request_changes(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int) -> Participant | Error | None:
    """Request changes on a pull request.

Synchronous wrapper around :func:`~bb.cloud.sdk.prs.request_changes`.

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
    participant = prs.request_changes(
        client, workspace="myworkspace", repo_slug="myrepo", pull_request_id=42
    )
    ```

References:
    `POST /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/request-changes
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-request-changes-post>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.prs.request_changes`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.request_changes(client, workspace, repo_slug, pull_request_id))

def unrequest_changes(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int) -> None:
    """Remove a request for changes from a pull request.

Synchronous wrapper around :func:`~bb.cloud.sdk.prs.unrequest_changes`.

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
    prs.unrequest_changes(
        client, workspace="myworkspace", repo_slug="myrepo", pull_request_id=42
    )
    ```

References:
    `DELETE /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/request-changes
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-request-changes-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.prs.unrequest_changes`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.unrequest_changes(client, workspace, repo_slug, pull_request_id))

def comments(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int, *, pagelen: int=25) -> list[PullRequestComment] | Error:
    """List all comments on a pull request across all pages.

Synchronous wrapper around :func:`~bb.cloud.sdk.prs.comments`.

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
    result = prs.comments(
        client, workspace="myworkspace", repo_slug="myrepo", pull_request_id=42
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-comments-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.prs.comments`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.comments(client, workspace, repo_slug, pull_request_id, pagelen=pagelen))

def add_comment(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int, *, body: PullRequestComment | Unset=UNSET) -> PullRequestComment | Error | None:
    """Add a comment to a pull request.

Synchronous wrapper around :func:`~bb.cloud.sdk.prs.add_comment`.

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
    comment = prs.add_comment(
        client, workspace="myworkspace", repo_slug="myrepo", pull_request_id=42,
        body=PullrequestComment(content=...),
    )
    ```

References:
    `POST /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-comments-post>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.prs.add_comment`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.add_comment(client, workspace, repo_slug, pull_request_id, body=body))

def diff(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int) -> str | Error | None:
    """Return the unified diff of a pull request as a string.

Synchronous wrapper around :func:`~bb.cloud.sdk.prs.diff`.

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
    unified_diff = prs.diff(
        client, workspace="myworkspace", repo_slug="myrepo", pull_request_id=42
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/diff
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-diff-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.prs.diff`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.diff(client, workspace, repo_slug, pull_request_id))

def commits(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int, *, pagelen: int=25) -> list[Any] | Error:
    """List all commits included in a pull request across all pages.

Synchronous wrapper around :func:`~bb.cloud.sdk.prs.commits`.

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
    result = prs.commits(
        client, workspace="myworkspace", repo_slug="myrepo", pull_request_id=42
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/commits
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-commits-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.prs.commits`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.commits(client, workspace, repo_slug, pull_request_id, pagelen=pagelen))

def tasks(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int, *, pagelen: int=25) -> list[Any] | Error:
    """List all tasks on a pull request across all pages.

Synchronous wrapper around :func:`~bb.cloud.sdk.prs.tasks`.

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
    result = prs.tasks(
        client, workspace="myworkspace", repo_slug="myrepo", pull_request_id=42
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/tasks
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-tasks-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.prs.tasks`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.tasks(client, workspace, repo_slug, pull_request_id, pagelen=pagelen))

def default_reviewers(client: BBClient, workspace: str, repo_slug: str, *, pagelen: int=25) -> list[Any] | Error:
    """List all default reviewers for a repository across all pages.

Synchronous wrapper around :func:`~bb.cloud.sdk.prs.default_reviewers`.

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
    result = prs.default_reviewers(
        client, workspace="myworkspace", repo_slug="myrepo"
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/default-reviewers
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-default-reviewers-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.prs.default_reviewers`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.default_reviewers(client, workspace, repo_slug, pagelen=pagelen))

def add_default_reviewer(client: BBClient, workspace: str, repo_slug: str, target_username: str) -> None:
    """Add a user as a default reviewer for a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.prs.add_default_reviewer`.

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
    prs.add_default_reviewer(
        client, workspace="myworkspace", repo_slug="myrepo", target_username="jsmith"
    )
    ```

References:
    `PUT /2.0/repositories/{workspace}/{repo_slug}/default-reviewers/{target_username}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-default-reviewers-target-username-put>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.prs.add_default_reviewer`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.add_default_reviewer(client, workspace, repo_slug, target_username))

def remove_default_reviewer(client: BBClient, workspace: str, repo_slug: str, target_username: str) -> None:
    """Remove a user from the default reviewers for a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.prs.remove_default_reviewer`.

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
    prs.remove_default_reviewer(
        client, workspace="myworkspace", repo_slug="myrepo", target_username="jsmith"
    )
    ```

References:
    `DELETE /2.0/repositories/{workspace}/{repo_slug}/default-reviewers/{target_username}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-default-reviewers-target-username-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.prs.remove_default_reviewer`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.remove_default_reviewer(client, workspace, repo_slug, target_username))

def get_default_reviewer(client: BBClient, workspace: str, repo_slug: str, target_username: str) -> Any | Error | None:
    """Fetch details of a specific default reviewer for a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.prs.get_default_reviewer`.

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
    reviewer = prs.get_default_reviewer(
        client, workspace="myworkspace", repo_slug="myrepo", target_username="jsmith"
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/default-reviewers/{target_username}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-default-reviewers-target-username-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.prs.get_default_reviewer`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.get_default_reviewer(client, workspace, repo_slug, target_username))

def effective_default_reviewers(client: BBClient, workspace: str, repo_slug: str, *, pagelen: int=25) -> list[Any] | Error:
    """List the effective default reviewers for a repository across all pages.

Synchronous wrapper around :func:`~bb.cloud.sdk.prs.effective_default_reviewers`.

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
    result = prs.effective_default_reviewers(
        client, workspace="myworkspace", repo_slug="myrepo"
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/effective-default-reviewers
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-effective-default-reviewers-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.prs.effective_default_reviewers`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.effective_default_reviewers(client, workspace, repo_slug, pagelen=pagelen))

def get_comment(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int, comment_id: int) -> PullRequestComment | Error | None:
    """Fetch a single comment on a pull request.

Synchronous wrapper around :func:`~bb.cloud.sdk.prs.get_comment`.

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
    comment = prs.get_comment(
        client, workspace="myworkspace", repo_slug="myrepo",
        pull_request_id=42, comment_id=101,
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments/{comment_id}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-comments-comment-id-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.prs.get_comment`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.get_comment(client, workspace, repo_slug, pull_request_id, comment_id))

def update_comment(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int, comment_id: int, *, body: PullRequestComment | Unset=UNSET) -> PullRequestComment | Error | None:
    """Update a comment on a pull request.

Synchronous wrapper around :func:`~bb.cloud.sdk.prs.update_comment`.

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
    comment = prs.update_comment(
        client, workspace="myworkspace", repo_slug="myrepo",
        pull_request_id=42, comment_id=101, body=PullrequestComment(content=...),
    )
    ```

References:
    `PUT /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments/{comment_id}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-comments-comment-id-put>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.prs.update_comment`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.update_comment(client, workspace, repo_slug, pull_request_id, comment_id, body=body))

def delete_comment(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int, comment_id: int) -> None:
    """Delete a comment on a pull request.

Synchronous wrapper around :func:`~bb.cloud.sdk.prs.delete_comment`.

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
    prs.delete_comment(
        client, workspace="myworkspace", repo_slug="myrepo",
        pull_request_id=42, comment_id=101,
    )
    ```

References:
    `DELETE /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments/{comment_id}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-comments-comment-id-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.prs.delete_comment`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.delete_comment(client, workspace, repo_slug, pull_request_id, comment_id))

def resolve_comment(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int, comment_id: int) -> Any | Error | None:
    """Mark a pull request comment as resolved.

Synchronous wrapper around :func:`~bb.cloud.sdk.prs.resolve_comment`.

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
    prs.resolve_comment(
        client, workspace="myworkspace", repo_slug="myrepo",
        pull_request_id=42, comment_id=101,
    )
    ```

References:
    `POST /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments/{comment_id}/resolve
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-comments-comment-id-resolve-post>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.prs.resolve_comment`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.resolve_comment(client, workspace, repo_slug, pull_request_id, comment_id))

def unresolve_comment(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int, comment_id: int) -> None:
    """Unmark a pull request comment as resolved.

Synchronous wrapper around :func:`~bb.cloud.sdk.prs.unresolve_comment`.

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
    prs.unresolve_comment(
        client, workspace="myworkspace", repo_slug="myrepo",
        pull_request_id=42, comment_id=101,
    )
    ```

References:
    `DELETE /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments/{comment_id}/resolve
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-comments-comment-id-resolve-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.prs.unresolve_comment`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.unresolve_comment(client, workspace, repo_slug, pull_request_id, comment_id))

def create_task(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int, *, body: Unset=UNSET) -> Any | Error | None:
    """Create a task on a pull request.

Synchronous wrapper around :func:`~bb.cloud.sdk.prs.create_task`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
    repo_slug: Repository slug or UUID.
    pull_request_id: Numeric pull request ID.
    body: Task payload. Currently limited to :data:`~bb.cloud.types.UNSET` due to
        spec constraints.

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
    task = prs.create_task(
        client, workspace="myworkspace", repo_slug="myrepo", pull_request_id=42
    )
    ```

References:
    `POST /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/tasks
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-tasks-post>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.prs.create_task`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.create_task(client, workspace, repo_slug, pull_request_id, body=body))

def get_task(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int, task_id: int) -> Any | Error | None:
    """Fetch a single task on a pull request.

Synchronous wrapper around :func:`~bb.cloud.sdk.prs.get_task`.

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
    task = prs.get_task(
        client, workspace="myworkspace", repo_slug="myrepo",
        pull_request_id=42, task_id=7,
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/tasks/{task_id}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-tasks-task-id-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.prs.get_task`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.get_task(client, workspace, repo_slug, pull_request_id, task_id))

def update_task(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int, task_id: int, *, body: Unset=UNSET) -> Any | Error | None:
    """Update a task on a pull request.

Synchronous wrapper around :func:`~bb.cloud.sdk.prs.update_task`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
    repo_slug: Repository slug or UUID.
    pull_request_id: Numeric pull request ID.
    task_id: Numeric task ID.
    body: Updated task payload. Currently limited to :data:`~bb.cloud.types.UNSET` due to
        spec constraints.

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
    task = prs.update_task(
        client, workspace="myworkspace", repo_slug="myrepo",
        pull_request_id=42, task_id=7,
    )
    ```

References:
    `PUT /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/tasks/{task_id}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-tasks-task-id-put>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.prs.update_task`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.update_task(client, workspace, repo_slug, pull_request_id, task_id, body=body))

def delete_task(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int, task_id: int) -> None:
    """Delete a task from a pull request.

Synchronous wrapper around :func:`~bb.cloud.sdk.prs.delete_task`.

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
    prs.delete_task(
        client, workspace="myworkspace", repo_slug="myrepo",
        pull_request_id=42, task_id=7,
    )
    ```

References:
    `DELETE /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/tasks/{task_id}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-tasks-task-id-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.prs.delete_task`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.delete_task(client, workspace, repo_slug, pull_request_id, task_id))

def activity(client: BBClient, workspace: str, repo_slug: str, *, pagelen: int=25) -> list[Any] | Error:
    """List activity for all pull requests in a repository across all pages.

Synchronous wrapper around :func:`~bb.cloud.sdk.prs.activity`.

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
    result = prs.activity(client, workspace="myworkspace", repo_slug="myrepo")
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/pullrequests/activity
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-activity-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.prs.activity`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.activity(client, workspace, repo_slug, pagelen=pagelen))

def pr_activity(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int, *, pagelen: int=25) -> list[Any] | Error:
    """List activity for a specific pull request across all pages.

Synchronous wrapper around :func:`~bb.cloud.sdk.prs.pr_activity`.

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
    result = prs.pr_activity(
        client, workspace="myworkspace", repo_slug="myrepo", pull_request_id=42
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/activity
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-activity-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.prs.pr_activity`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.pr_activity(client, workspace, repo_slug, pull_request_id, pagelen=pagelen))

def diffstat(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int) -> Any:
    """Return the diffstat (changed files summary) for a pull request.

Synchronous wrapper around :func:`~bb.cloud.sdk.prs.diffstat`.

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
    stat = prs.diffstat(
        client, workspace="myworkspace", repo_slug="myrepo", pull_request_id=42
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/diffstat
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-diffstat-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.prs.diffstat`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.diffstat(client, workspace, repo_slug, pull_request_id))

def patch(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int) -> str | Error | None:
    """Return the patch for a pull request as a string.

Synchronous wrapper around :func:`~bb.cloud.sdk.prs.patch`.

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
    patch_text = prs.patch(
        client, workspace="myworkspace", repo_slug="myrepo", pull_request_id=42
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/patch
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-patch-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.prs.patch`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.patch(client, workspace, repo_slug, pull_request_id))

def statuses(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int, *, pagelen: int=25) -> list[Any] | Error:
    """List all commit statuses for a pull request across all pages.

Synchronous wrapper around :func:`~bb.cloud.sdk.prs.statuses`.

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
    result = prs.statuses(
        client, workspace="myworkspace", repo_slug="myrepo", pull_request_id=42
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/statuses
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-statuses-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.prs.statuses`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.statuses(client, workspace, repo_slug, pull_request_id, pagelen=pagelen))

def user_prs(client: BBClient, workspace: str, selected_user: str, *, pagelen: int=25) -> list[Pullrequest] | Error:
    """List all pull requests authored by a user in a workspace across all pages.

Synchronous wrapper around :func:`~bb.cloud.sdk.prs.user_prs`.

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
    result = prs.user_prs(client, workspace="myworkspace", selected_user="jsmith")
    ```

References:
    `GET /2.0/workspaces/{workspace}/pullrequests/{selected_user}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-workspaces/#api-workspaces-workspace-pullrequests-selected-user-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.prs.user_prs`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.user_prs(client, workspace, selected_user, pagelen=pagelen))

def merge_task_status(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int, task_id: str) -> Any | Error | None:
    """Return the status of an asynchronous merge task.

Synchronous wrapper around :func:`~bb.cloud.sdk.prs.merge_task_status`.

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
    status = prs.merge_task_status(
        client, workspace="myworkspace", repo_slug="myrepo",
        pull_request_id=42, task_id="abc-task-123",
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/merge/task-status/{task_id}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-pullrequests-pull-request-id-merge-task-status-task-id-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.prs.merge_task_status`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.merge_task_status(client, workspace, repo_slug, pull_request_id, task_id))
