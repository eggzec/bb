from __future__ import annotations
from typing import Any
from bb.cloud.models.component import Component
from bb.cloud.models.error import Error
from bb.cloud.models.issue import Issue
from bb.cloud.models.issue_change import IssueChange
from bb.cloud.models.issue_comment import IssueComment
from bb.cloud.models.milestone import Milestone
from bb.cloud.models.version import Version
from bb.cloud.sdk._client import BBClient
from bb.cloud.types import UNSET, Unset
from bb.cloud.sdk import issues as _async
__all__ = ['list', 'get', 'create', 'update', 'delete', 'comments', 'get_comment', 'add_comment', 'update_comment', 'delete_comment', 'changes', 'get_change', 'add_change', 'vote', 'unvote', 'voted', 'watch', 'unwatch', 'watching', 'milestones', 'get_milestone', 'versions', 'get_version', 'components', 'get_component', 'attachments', 'get_attachment', 'upload_attachment', 'delete_attachment', 'export', 'export_status', 'import_status', 'import_data']

def list(client: BBClient, workspace: str, repo_slug: str, *, q: str | Unset=UNSET, sort: str | Unset=UNSET, pagelen: int=25) -> list[Issue] | Error:
    """Return all issues for a repository across all pages.

Synchronous wrapper around :func:`~bb.cloud.sdk.issues.list`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug.
    q: Optional filter query string (Bitbucket query syntax).
    sort: Optional field name to sort results by.
    pagelen: Number of results per page. Defaults to ``25``.

Returns:
    All :class:`~bb.cloud.models.issue.Issue` objects matching the query,
    flattened from all pages.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import issues

    client = BBClient.from_env()
    result = issues.list(client, workspace="myws", repo_slug="myrepo")
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/issues
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.issues.list`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.list(client, workspace, repo_slug, q=q, sort=sort, pagelen=pagelen))

def get(client: BBClient, workspace: str, repo_slug: str, issue_id: int) -> Issue | Error | None:
    """Return a single issue by ID, or ``None`` if not found.

Synchronous wrapper around :func:`~bb.cloud.sdk.issues.get`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug.
    issue_id: Numeric issue ID.

Returns:
    The matching :class:`~bb.cloud.models.issue.Issue`, or ``None`` if the
    issue does not exist.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import issues

    client = BBClient.from_env()
    issue = issues.get(client, workspace="myws", repo_slug="myrepo", issue_id=42)
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/issues/{issue_id}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-issue-id-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.issues.get`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.get(client, workspace, repo_slug, issue_id))

def create(client: BBClient, workspace: str, repo_slug: str, *, body: Issue | Unset=UNSET) -> Issue | Error | None:
    """Create an issue and return the created object.

Synchronous wrapper around :func:`~bb.cloud.sdk.issues.create`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug.
    body: Issue object with the fields to set on the new issue.

Returns:
    The newly created :class:`~bb.cloud.models.issue.Issue`, or ``None`` on
    error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.models.issue import Issue
    from bb.cloud.sdk import issues

    client = BBClient.from_env()
    new_issue = Issue(title="Bug report", kind="bug")
    created = issues.create(client, workspace="myws", repo_slug="myrepo", body=new_issue)
    ```

References:
    `POST /2.0/repositories/{workspace}/{repo_slug}/issues
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-post>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.issues.create`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.create(client, workspace, repo_slug, body=body))

def update(client: BBClient, workspace: str, repo_slug: str, issue_id: int, *, body: Issue | Unset=UNSET) -> Issue | Error | None:
    """Update an issue and return the updated object.

Synchronous wrapper around :func:`~bb.cloud.sdk.issues.update`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug.
    issue_id: Numeric issue ID.
    body: Issue object with updated field values.

Returns:
    The updated :class:`~bb.cloud.models.issue.Issue`, or ``None`` on error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.models.issue import Issue
    from bb.cloud.sdk import issues

    client = BBClient.from_env()
    updated = issues.update(
        client, workspace="myws", repo_slug="myrepo", issue_id=42,
        body=Issue(status="resolved"),
    )
    ```

References:
    `PUT /2.0/repositories/{workspace}/{repo_slug}/issues/{issue_id}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-issue-id-put>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.issues.update`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.update(client, workspace, repo_slug, issue_id, body=body))

def delete(client: BBClient, workspace: str, repo_slug: str, issue_id: int) -> None:
    """Delete an issue.

Synchronous wrapper around :func:`~bb.cloud.sdk.issues.delete`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug.
    issue_id: Numeric issue ID.

Returns:
    None

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import issues

    client = BBClient.from_env()
    issues.delete(client, workspace="myws", repo_slug="myrepo", issue_id=42)
    ```

References:
    `DELETE /2.0/repositories/{workspace}/{repo_slug}/issues/{issue_id}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-issue-id-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.issues.delete`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.delete(client, workspace, repo_slug, issue_id))

def comments(client: BBClient, workspace: str, repo_slug: str, issue_id: int, *, pagelen: int=25) -> list[IssueComment] | Error:
    """Return all comments on an issue across all pages.

Synchronous wrapper around :func:`~bb.cloud.sdk.issues.comments`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug.
    issue_id: Numeric issue ID.
    pagelen: Number of results per page. Defaults to ``25``.

Returns:
    All :class:`~bb.cloud.models.issue_comment.IssueComment` objects for the
    issue.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import issues

    client = BBClient.from_env()
    all_comments = issues.comments(
        client, workspace="myws", repo_slug="myrepo", issue_id=42
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/issues/{issue_id}/comments
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-issue-id-comments-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.issues.comments`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.comments(client, workspace, repo_slug, issue_id, pagelen=pagelen))

def add_comment(client: BBClient, workspace: str, repo_slug: str, issue_id: int, *, body: IssueComment | Unset=UNSET) -> IssueComment | Error | None:
    """Add a comment to an issue and return the created comment.

Synchronous wrapper around :func:`~bb.cloud.sdk.issues.add_comment`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug.
    issue_id: Numeric issue ID.
    body: Comment object with the content to post.

Returns:
    The newly created :class:`~bb.cloud.models.issue_comment.IssueComment`,
    or ``None`` on error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.models.issue_comment import IssueComment
    from bb.cloud.sdk import issues

    client = BBClient.from_env()
    comment = issues.add_comment(
        client, workspace="myws", repo_slug="myrepo", issue_id=42,
        body=IssueComment(content={"raw": "This is a comment."}),
    )
    ```

References:
    `POST /2.0/repositories/{workspace}/{repo_slug}/issues/{issue_id}/comments
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-issue-id-comments-post>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.issues.add_comment`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.add_comment(client, workspace, repo_slug, issue_id, body=body))

def changes(client: BBClient, workspace: str, repo_slug: str, issue_id: int, *, pagelen: int=25) -> list[IssueChange] | Error:
    """Return all changes (edit history) for an issue across all pages.

Synchronous wrapper around :func:`~bb.cloud.sdk.issues.changes`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug.
    issue_id: Numeric issue ID.
    pagelen: Number of results per page. Defaults to ``25``.

Returns:
    All :class:`~bb.cloud.models.issue_change.IssueChange` objects for the
    issue.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import issues

    client = BBClient.from_env()
    history = issues.changes(
        client, workspace="myws", repo_slug="myrepo", issue_id=42
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/issues/{issue_id}/changes
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-issue-id-changes-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.issues.changes`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.changes(client, workspace, repo_slug, issue_id, pagelen=pagelen))

def vote(client: BBClient, workspace: str, repo_slug: str, issue_id: int) -> None:
    """Cast a vote on an issue.

Synchronous wrapper around :func:`~bb.cloud.sdk.issues.vote`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug.
    issue_id: Numeric issue ID.

Returns:
    None

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import issues

    client = BBClient.from_env()
    issues.vote(client, workspace="myws", repo_slug="myrepo", issue_id=42)
    ```

References:
    `PUT /2.0/repositories/{workspace}/{repo_slug}/issues/{issue_id}/vote
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-issue-id-vote-put>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.issues.vote`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.vote(client, workspace, repo_slug, issue_id))

def unvote(client: BBClient, workspace: str, repo_slug: str, issue_id: int) -> None:
    """Remove a vote from an issue.

Synchronous wrapper around :func:`~bb.cloud.sdk.issues.unvote`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug.
    issue_id: Numeric issue ID.

Returns:
    None

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import issues

    client = BBClient.from_env()
    issues.unvote(client, workspace="myws", repo_slug="myrepo", issue_id=42)
    ```

References:
    `DELETE /2.0/repositories/{workspace}/{repo_slug}/issues/{issue_id}/vote
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-issue-id-vote-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.issues.unvote`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.unvote(client, workspace, repo_slug, issue_id))

def watch(client: BBClient, workspace: str, repo_slug: str, issue_id: int) -> None:
    """Start watching an issue.

Synchronous wrapper around :func:`~bb.cloud.sdk.issues.watch`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug.
    issue_id: Numeric issue ID.

Returns:
    None

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import issues

    client = BBClient.from_env()
    issues.watch(client, workspace="myws", repo_slug="myrepo", issue_id=42)
    ```

References:
    `PUT /2.0/repositories/{workspace}/{repo_slug}/issues/{issue_id}/watch
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-issue-id-watch-put>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.issues.watch`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.watch(client, workspace, repo_slug, issue_id))

def unwatch(client: BBClient, workspace: str, repo_slug: str, issue_id: int) -> None:
    """Stop watching an issue.

Synchronous wrapper around :func:`~bb.cloud.sdk.issues.unwatch`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug.
    issue_id: Numeric issue ID.

Returns:
    None

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import issues

    client = BBClient.from_env()
    issues.unwatch(client, workspace="myws", repo_slug="myrepo", issue_id=42)
    ```

References:
    `DELETE /2.0/repositories/{workspace}/{repo_slug}/issues/{issue_id}/watch
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-issue-id-watch-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.issues.unwatch`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.unwatch(client, workspace, repo_slug, issue_id))

def milestones(client: BBClient, workspace: str, repo_slug: str) -> list[Milestone] | Error:
    """Return all milestones for a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.issues.milestones`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug.

Returns:
    All :class:`~bb.cloud.models.milestone.Milestone` objects for the
    repository.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import issues

    client = BBClient.from_env()
    all_milestones = issues.milestones(client, workspace="myws", repo_slug="myrepo")
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/milestones
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-milestones-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.issues.milestones`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.milestones(client, workspace, repo_slug))

def versions(client: BBClient, workspace: str, repo_slug: str) -> list[Version] | Error:
    """Return all versions for a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.issues.versions`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug.

Returns:
    All :class:`~bb.cloud.models.version.Version` objects for the repository.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import issues

    client = BBClient.from_env()
    all_versions = issues.versions(client, workspace="myws", repo_slug="myrepo")
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/versions
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-versions-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.issues.versions`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.versions(client, workspace, repo_slug))

def components(client: BBClient, workspace: str, repo_slug: str) -> list[Component] | Error:
    """Return all components for a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.issues.components`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug.

Returns:
    All :class:`~bb.cloud.models.component.Component` objects for the
    repository.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import issues

    client = BBClient.from_env()
    all_components = issues.components(client, workspace="myws", repo_slug="myrepo")
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/components
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-components-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.issues.components`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.components(client, workspace, repo_slug))

def get_comment(client: BBClient, workspace: str, repo_slug: str, issue_id: int, comment_id: int) -> IssueComment | Error | None:
    """Return a single comment on an issue, or ``None`` if not found.

Synchronous wrapper around :func:`~bb.cloud.sdk.issues.get_comment`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug.
    issue_id: Numeric issue ID.
    comment_id: Numeric comment ID.

Returns:
    The matching :class:`~bb.cloud.models.issue_comment.IssueComment`, or
    ``None`` if not found.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import issues

    client = BBClient.from_env()
    comment = issues.get_comment(
        client, workspace="myws", repo_slug="myrepo", issue_id=42, comment_id=7
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/issues/{issue_id}/comments/{comment_id}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-issue-id-comments-comment-id-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.issues.get_comment`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.get_comment(client, workspace, repo_slug, issue_id, comment_id))

def update_comment(client: BBClient, workspace: str, repo_slug: str, issue_id: int, comment_id: int, *, body: IssueComment | Unset=UNSET) -> IssueComment | Error | None:
    """Update a comment on an issue.

Synchronous wrapper around :func:`~bb.cloud.sdk.issues.update_comment`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug.
    issue_id: Numeric issue ID.
    comment_id: Numeric comment ID.
    body: Comment object with updated content.

Returns:
    The updated :class:`~bb.cloud.models.issue_comment.IssueComment`, or
    ``None`` on error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.models.issue_comment import IssueComment
    from bb.cloud.sdk import issues

    client = BBClient.from_env()
    updated = issues.update_comment(
        client, workspace="myws", repo_slug="myrepo", issue_id=42, comment_id=7,
        body=IssueComment(content={"raw": "Updated text."}),
    )
    ```

References:
    `PUT /2.0/repositories/{workspace}/{repo_slug}/issues/{issue_id}/comments/{comment_id}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-issue-id-comments-comment-id-put>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.issues.update_comment`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.update_comment(client, workspace, repo_slug, issue_id, comment_id, body=body))

def delete_comment(client: BBClient, workspace: str, repo_slug: str, issue_id: int, comment_id: int) -> None:
    """Delete a comment on an issue.

Synchronous wrapper around :func:`~bb.cloud.sdk.issues.delete_comment`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug.
    issue_id: Numeric issue ID.
    comment_id: Numeric comment ID.

Returns:
    None

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import issues

    client = BBClient.from_env()
    issues.delete_comment(
        client, workspace="myws", repo_slug="myrepo", issue_id=42, comment_id=7
    )
    ```

References:
    `DELETE /2.0/repositories/{workspace}/{repo_slug}/issues/{issue_id}/comments/{comment_id}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-issue-id-comments-comment-id-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.issues.delete_comment`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.delete_comment(client, workspace, repo_slug, issue_id, comment_id))

def get_change(client: BBClient, workspace: str, repo_slug: str, issue_id: int, change_id: int) -> IssueChange | Error | None:
    """Return a single change entry for an issue, or ``None`` if not found.

Synchronous wrapper around :func:`~bb.cloud.sdk.issues.get_change`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug.
    issue_id: Numeric issue ID.
    change_id: Numeric change ID.

Returns:
    The matching :class:`~bb.cloud.models.issue_change.IssueChange`, or
    ``None`` if not found.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import issues

    client = BBClient.from_env()
    change = issues.get_change(
        client, workspace="myws", repo_slug="myrepo", issue_id=42, change_id=3
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/issues/{issue_id}/changes/{change_id}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-issue-id-changes-change-id-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.issues.get_change`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.get_change(client, workspace, repo_slug, issue_id, change_id))

def add_change(client: BBClient, workspace: str, repo_slug: str, issue_id: int, *, body: IssueChange | Unset=UNSET) -> IssueChange | Error | None:
    """Record a change on an issue (e.g. a status transition).

Synchronous wrapper around :func:`~bb.cloud.sdk.issues.add_change`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug.
    issue_id: Numeric issue ID.
    body: Change object describing the transition to apply.

Returns:
    The recorded :class:`~bb.cloud.models.issue_change.IssueChange`, or
    ``None`` on error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.models.issue_change import IssueChange
    from bb.cloud.sdk import issues

    client = BBClient.from_env()
    change = issues.add_change(
        client, workspace="myws", repo_slug="myrepo", issue_id=42,
        body=IssueChange(changes={"status": {"new": "resolved"}}),
    )
    ```

References:
    `POST /2.0/repositories/{workspace}/{repo_slug}/issues/{issue_id}/changes
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-issue-id-changes-post>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.issues.add_change`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.add_change(client, workspace, repo_slug, issue_id, body=body))

def voted(client: BBClient, workspace: str, repo_slug: str, issue_id: int) -> Any | Error | None:
    """Return the current user's vote status on an issue.

Synchronous wrapper around :func:`~bb.cloud.sdk.issues.voted`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug.
    issue_id: Numeric issue ID.

Returns:
    The API response object representing the vote status, or ``None`` if the
    user has not voted.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import issues

    client = BBClient.from_env()
    status = issues.voted(client, workspace="myws", repo_slug="myrepo", issue_id=42)
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/issues/{issue_id}/vote
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-issue-id-vote-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.issues.voted`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.voted(client, workspace, repo_slug, issue_id))

def watching(client: BBClient, workspace: str, repo_slug: str, issue_id: int) -> Any | Error | None:
    """Return the current user's watch status on an issue.

Synchronous wrapper around :func:`~bb.cloud.sdk.issues.watching`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug.
    issue_id: Numeric issue ID.

Returns:
    The API response object representing the watch status, or ``None`` if the
    user is not watching the issue.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import issues

    client = BBClient.from_env()
    status = issues.watching(client, workspace="myws", repo_slug="myrepo", issue_id=42)
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/issues/{issue_id}/watch
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-issue-id-watch-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.issues.watching`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.watching(client, workspace, repo_slug, issue_id))

def get_milestone(client: BBClient, workspace: str, repo_slug: str, milestone_id: int) -> Milestone | Error | None:
    """Return a single milestone by ID, or ``None`` if not found.

Synchronous wrapper around :func:`~bb.cloud.sdk.issues.get_milestone`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug.
    milestone_id: Numeric milestone ID.

Returns:
    The matching :class:`~bb.cloud.models.milestone.Milestone`, or ``None``
    if not found.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import issues

    client = BBClient.from_env()
    milestone = issues.get_milestone(
        client, workspace="myws", repo_slug="myrepo", milestone_id=1
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/milestones/{milestone_id}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-milestones-milestone-id-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.issues.get_milestone`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.get_milestone(client, workspace, repo_slug, milestone_id))

def get_version(client: BBClient, workspace: str, repo_slug: str, version_id: int) -> Version | Error | None:
    """Return a single version by ID, or ``None`` if not found.

Synchronous wrapper around :func:`~bb.cloud.sdk.issues.get_version`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug.
    version_id: Numeric version ID.

Returns:
    The matching :class:`~bb.cloud.models.version.Version`, or ``None`` if
    not found.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import issues

    client = BBClient.from_env()
    version = issues.get_version(
        client, workspace="myws", repo_slug="myrepo", version_id=2
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/versions/{version_id}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-versions-version-id-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.issues.get_version`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.get_version(client, workspace, repo_slug, version_id))

def get_component(client: BBClient, workspace: str, repo_slug: str, component_id: int) -> Component | Error | None:
    """Return a single component by ID, or ``None`` if not found.

Synchronous wrapper around :func:`~bb.cloud.sdk.issues.get_component`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug.
    component_id: Numeric component ID.

Returns:
    The matching :class:`~bb.cloud.models.component.Component`, or ``None``
    if not found.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import issues

    client = BBClient.from_env()
    component = issues.get_component(
        client, workspace="myws", repo_slug="myrepo", component_id=5
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/components/{component_id}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-components-component-id-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.issues.get_component`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.get_component(client, workspace, repo_slug, component_id))

def attachments(client: BBClient, workspace: str, repo_slug: str, issue_id: int) -> Any | Error | None:
    """Return the list of attachments on an issue.

Synchronous wrapper around :func:`~bb.cloud.sdk.issues.attachments`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug.
    issue_id: Numeric issue ID.

Returns:
    The API response object containing attachment metadata, or ``None`` on
    error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import issues

    client = BBClient.from_env()
    files = issues.attachments(
        client, workspace="myws", repo_slug="myrepo", issue_id=42
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/issues/{issue_id}/attachments
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-issue-id-attachments-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.issues.attachments`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.attachments(client, workspace, repo_slug, issue_id))

def get_attachment(client: BBClient, workspace: str, repo_slug: str, issue_id: int, path: str) -> Any | Error | None:
    """Return the redirect URL for a specific attachment on an issue.

Synchronous wrapper around :func:`~bb.cloud.sdk.issues.get_attachment`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug.
    issue_id: Numeric issue ID.
    path: Filename of the attachment.

Returns:
    The API response for the attachment redirect, or ``None`` on error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import issues

    client = BBClient.from_env()
    attachment = issues.get_attachment(
        client, workspace="myws", repo_slug="myrepo", issue_id=42, path="screenshot.png"
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/issues/{issue_id}/attachments/{path}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-issue-id-attachments-path-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.issues.get_attachment`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.get_attachment(client, workspace, repo_slug, issue_id, path))

def upload_attachment(client: BBClient, workspace: str, repo_slug: str, issue_id: int, *, body: Unset=UNSET) -> None:
    """Upload an attachment to an issue.

Synchronous wrapper around :func:`~bb.cloud.sdk.issues.upload_attachment`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug.
    issue_id: Numeric issue ID.
    body: Multipart form data body containing the file to upload.

Returns:
    None

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import issues

    client = BBClient.from_env()
    issues.upload_attachment(
        client, workspace="myws", repo_slug="myrepo", issue_id=42
    )
    ```

References:
    `POST /2.0/repositories/{workspace}/{repo_slug}/issues/{issue_id}/attachments
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-issue-id-attachments-post>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.issues.upload_attachment`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.upload_attachment(client, workspace, repo_slug, issue_id, body=body))

def delete_attachment(client: BBClient, workspace: str, repo_slug: str, issue_id: int, path: str) -> None:
    """Delete an attachment from an issue.

Synchronous wrapper around :func:`~bb.cloud.sdk.issues.delete_attachment`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug.
    issue_id: Numeric issue ID.
    path: Filename of the attachment to delete.

Returns:
    None

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import issues

    client = BBClient.from_env()
    issues.delete_attachment(
        client, workspace="myws", repo_slug="myrepo", issue_id=42, path="screenshot.png"
    )
    ```

References:
    `DELETE /2.0/repositories/{workspace}/{repo_slug}/issues/{issue_id}/attachments/{path}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-issue-id-attachments-path-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.issues.delete_attachment`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.delete_attachment(client, workspace, repo_slug, issue_id, path))

def export(client: BBClient, workspace: str, repo_slug: str, *, body: Unset=UNSET) -> None:
    """Start an asynchronous export of all issues for a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.issues.export`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug.
    body: Optional request body for the export operation.

Returns:
    None

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import issues

    client = BBClient.from_env()
    issues.export(client, workspace="myws", repo_slug="myrepo")
    ```

References:
    `POST /2.0/repositories/{workspace}/{repo_slug}/issues/export
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-export-post>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.issues.export`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.export(client, workspace, repo_slug, body=body))

def export_status(client: BBClient, workspace: str, repo_slug: str, repo_name: str, task_id: str) -> Any | Error | None:
    """Check the status of an in-progress issue export task.

Synchronous wrapper around :func:`~bb.cloud.sdk.issues.export_status`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug.
    repo_name: Repository name (as included in the export zip filename).
    task_id: Export task ID returned when the export was initiated.

Returns:
    The API response object describing the export status, or ``None`` on
    error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import issues

    client = BBClient.from_env()
    status = issues.export_status(
        client, workspace="myws", repo_slug="myrepo",
        repo_name="myrepo", task_id="abc123",
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/issues/export/{repo_name}-issues-{task_id}.zip
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-export-repo-name-issues-task-id-zip-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.issues.export_status`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.export_status(client, workspace, repo_slug, repo_name, task_id))

def import_status(client: BBClient, workspace: str, repo_slug: str) -> Any | Error | None:
    """Check the status of an in-progress issue import task.

Synchronous wrapper around :func:`~bb.cloud.sdk.issues.import_status`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug.

Returns:
    The API response object describing the import status, or ``None`` on
    error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import issues

    client = BBClient.from_env()
    status = issues.import_status(client, workspace="myws", repo_slug="myrepo")
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/issues/import
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-import-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.issues.import_status`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.import_status(client, workspace, repo_slug))

def import_data(client: BBClient, workspace: str, repo_slug: str, *, body: Unset=UNSET) -> None:
    """Start an asynchronous import of issues for a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.issues.import_data`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug.
    body: Optional request body containing the import data.

Returns:
    None

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import issues

    client = BBClient.from_env()
    issues.import_data(client, workspace="myws", repo_slug="myrepo")
    ```

References:
    `POST /2.0/repositories/{workspace}/{repo_slug}/issues/import
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-import-post>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.issues.import_data`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.import_data(client, workspace, repo_slug, body=body))
