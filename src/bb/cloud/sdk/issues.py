from __future__ import annotations

from typing import Any

from bb.cloud.api.issue_tracker import (
    delete_repositories_workspace_repo_slug_issues_issue_id,
    delete_repositories_workspace_repo_slug_issues_issue_id_attachments_path,
    delete_repositories_workspace_repo_slug_issues_issue_id_comments_comment_id,
    delete_repositories_workspace_repo_slug_issues_issue_id_vote,
    delete_repositories_workspace_repo_slug_issues_issue_id_watch,
    get_repositories_workspace_repo_slug_components,
    get_repositories_workspace_repo_slug_components_component_id,
    get_repositories_workspace_repo_slug_issues,
    get_repositories_workspace_repo_slug_issues_export_repo_name_issues_task_id_zip,
    get_repositories_workspace_repo_slug_issues_import,
    get_repositories_workspace_repo_slug_issues_issue_id,
    get_repositories_workspace_repo_slug_issues_issue_id_attachments,
    get_repositories_workspace_repo_slug_issues_issue_id_attachments_path,
    get_repositories_workspace_repo_slug_issues_issue_id_changes,
    get_repositories_workspace_repo_slug_issues_issue_id_changes_change_id,
    get_repositories_workspace_repo_slug_issues_issue_id_comments,
    get_repositories_workspace_repo_slug_issues_issue_id_comments_comment_id,
    get_repositories_workspace_repo_slug_issues_issue_id_vote,
    get_repositories_workspace_repo_slug_issues_issue_id_watch,
    get_repositories_workspace_repo_slug_milestones,
    get_repositories_workspace_repo_slug_milestones_milestone_id,
    get_repositories_workspace_repo_slug_versions,
    get_repositories_workspace_repo_slug_versions_version_id,
    post_repositories_workspace_repo_slug_issues,
    post_repositories_workspace_repo_slug_issues_export,
    post_repositories_workspace_repo_slug_issues_import,
    post_repositories_workspace_repo_slug_issues_issue_id_attachments,
    post_repositories_workspace_repo_slug_issues_issue_id_changes,
    post_repositories_workspace_repo_slug_issues_issue_id_comments,
    put_repositories_workspace_repo_slug_issues_issue_id,
    put_repositories_workspace_repo_slug_issues_issue_id_comments_comment_id,
    put_repositories_workspace_repo_slug_issues_issue_id_vote,
    put_repositories_workspace_repo_slug_issues_issue_id_watch,
)
from bb.cloud.models.component import Component
from bb.cloud.models.error import Error
from bb.cloud.models.issue import Issue
from bb.cloud.models.issue_change import IssueChange
from bb.cloud.models.issue_comment import IssueComment
from bb.cloud.models.milestone import Milestone
from bb.cloud.models.version import Version
from bb.cloud.sdk._auth_validation import AuthMethod, require_auth
from bb.cloud.sdk._client import BBClient
from bb.cloud.sdk._pagination import async_paginate
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


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def list(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    pagelen: int = 25,
) -> list[Issue] | Error:
    """Return all issues for a repository across all pages.

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
        result = await issues.list(client, workspace="myws", repo_slug="myrepo")
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/issues
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-get>`_
    """
    result = await async_paginate(
        get_repositories_workspace_repo_slug_issues.asyncio,
        workspace,
        repo_slug,
        client=client.auth,
        q=q,
        sort=sort,
        pagelen=pagelen,
    )

    if isinstance(result, Error):
        return result

    return [item for item in result if isinstance(item, Issue)]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get(client: BBClient, workspace: str, repo_slug: str, issue_id: int) -> Issue | Error | None:
    """Return a single issue by ID, or ``None`` if not found.

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
        issue = await issues.get(client, workspace="myws", repo_slug="myrepo", issue_id=42)
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/issues/{issue_id}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-issue-id-get>`_
    """
    result = await get_repositories_workspace_repo_slug_issues_issue_id.asyncio(
        workspace, repo_slug, issue_id, client=client.auth
    )
    if isinstance(result, (Issue, Error)):
        return result
    return None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def create(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: Issue | Unset = UNSET,
) -> Issue | Error | None:
    """Create an issue and return the created object.

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
        created = await issues.create(client, workspace="myws", repo_slug="myrepo", body=new_issue)
        ```

    References:
        `POST /2.0/repositories/{workspace}/{repo_slug}/issues
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-post>`_
    """
    result = await post_repositories_workspace_repo_slug_issues.asyncio(
        workspace, repo_slug, client=client.auth, body=body
    )
    if isinstance(result, (Issue, Error)):
        return result
    return None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def update(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    issue_id: int,
    *,
    body: Issue | Unset = UNSET,
) -> Issue | Error | None:
    """Update an issue and return the updated object.

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
        updated = await issues.update(
            client, workspace="myws", repo_slug="myrepo", issue_id=42,
            body=Issue(status="resolved"),
        )
        ```

    References:
        `PUT /2.0/repositories/{workspace}/{repo_slug}/issues/{issue_id}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-issue-id-put>`_
    """
    result = await put_repositories_workspace_repo_slug_issues_issue_id.asyncio(
        workspace, repo_slug, issue_id, client=client.auth, body=body
    )
    if isinstance(result, (Issue, Error)):
        return result
    return None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def delete(client: BBClient, workspace: str, repo_slug: str, issue_id: int) -> None:
    """Delete an issue.

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
        await issues.delete(client, workspace="myws", repo_slug="myrepo", issue_id=42)
        ```

    References:
        `DELETE /2.0/repositories/{workspace}/{repo_slug}/issues/{issue_id}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-issue-id-delete>`_
    """
    await delete_repositories_workspace_repo_slug_issues_issue_id.asyncio(
        workspace, repo_slug, issue_id, client=client.auth
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def comments(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    issue_id: int,
    *,
    pagelen: int = 25,
) -> list[IssueComment] | Error:
    """Return all comments on an issue across all pages.

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
        all_comments = await issues.comments(
            client, workspace="myws", repo_slug="myrepo", issue_id=42
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/issues/{issue_id}/comments
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-issue-id-comments-get>`_
    """
    result = await async_paginate(
        get_repositories_workspace_repo_slug_issues_issue_id_comments.asyncio,
        workspace,
        repo_slug,
        issue_id,
        client=client.auth,
        pagelen=pagelen,
    )

    if isinstance(result, Error):
        return result

    return [item for item in result if isinstance(item, IssueComment)]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def add_comment(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    issue_id: int,
    *,
    body: IssueComment | Unset = UNSET,
) -> IssueComment | Error | None:
    """Add a comment to an issue and return the created comment.

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
        comment = await issues.add_comment(
            client, workspace="myws", repo_slug="myrepo", issue_id=42,
            body=IssueComment(content={"raw": "This is a comment."}),
        )
        ```

    References:
        `POST /2.0/repositories/{workspace}/{repo_slug}/issues/{issue_id}/comments
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-issue-id-comments-post>`_
    """
    result = await post_repositories_workspace_repo_slug_issues_issue_id_comments.asyncio(
        workspace, repo_slug, issue_id, client=client.auth, body=body
    )
    if isinstance(result, (IssueComment, Error)):
        return result
    return None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def changes(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    issue_id: int,
    *,
    pagelen: int = 25,
) -> list[IssueChange] | Error:
    """Return all changes (edit history) for an issue across all pages.

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
        history = await issues.changes(
            client, workspace="myws", repo_slug="myrepo", issue_id=42
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/issues/{issue_id}/changes
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-issue-id-changes-get>`_
    """
    result = await async_paginate(
        get_repositories_workspace_repo_slug_issues_issue_id_changes.asyncio,
        workspace,
        repo_slug,
        issue_id,
        client=client.auth,
        pagelen=pagelen,
    )

    if isinstance(result, Error):
        return result

    return [item for item in result if isinstance(item, IssueChange)]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def vote(client: BBClient, workspace: str, repo_slug: str, issue_id: int) -> None:
    """Cast a vote on an issue.

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
        await issues.vote(client, workspace="myws", repo_slug="myrepo", issue_id=42)
        ```

    References:
        `PUT /2.0/repositories/{workspace}/{repo_slug}/issues/{issue_id}/vote
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-issue-id-vote-put>`_
    """
    await put_repositories_workspace_repo_slug_issues_issue_id_vote.asyncio(
        workspace, repo_slug, issue_id, client=client.auth
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def unvote(client: BBClient, workspace: str, repo_slug: str, issue_id: int) -> None:
    """Remove a vote from an issue.

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
        await issues.unvote(client, workspace="myws", repo_slug="myrepo", issue_id=42)
        ```

    References:
        `DELETE /2.0/repositories/{workspace}/{repo_slug}/issues/{issue_id}/vote
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-issue-id-vote-delete>`_
    """
    await delete_repositories_workspace_repo_slug_issues_issue_id_vote.asyncio(
        workspace, repo_slug, issue_id, client=client.auth
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def watch(client: BBClient, workspace: str, repo_slug: str, issue_id: int) -> None:
    """Start watching an issue.

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
        await issues.watch(client, workspace="myws", repo_slug="myrepo", issue_id=42)
        ```

    References:
        `PUT /2.0/repositories/{workspace}/{repo_slug}/issues/{issue_id}/watch
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-issue-id-watch-put>`_
    """
    await put_repositories_workspace_repo_slug_issues_issue_id_watch.asyncio(
        workspace, repo_slug, issue_id, client=client.auth
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def unwatch(client: BBClient, workspace: str, repo_slug: str, issue_id: int) -> None:
    """Stop watching an issue.

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
        await issues.unwatch(client, workspace="myws", repo_slug="myrepo", issue_id=42)
        ```

    References:
        `DELETE /2.0/repositories/{workspace}/{repo_slug}/issues/{issue_id}/watch
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-issue-id-watch-delete>`_
    """
    await delete_repositories_workspace_repo_slug_issues_issue_id_watch.asyncio(
        workspace, repo_slug, issue_id, client=client.auth
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def milestones(client: BBClient, workspace: str, repo_slug: str) -> list[Milestone] | Error:
    """Return all milestones for a repository.

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
        all_milestones = await issues.milestones(client, workspace="myws", repo_slug="myrepo")
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/milestones
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-milestones-get>`_
    """
    result = await async_paginate(
        get_repositories_workspace_repo_slug_milestones.asyncio,
        workspace,
        repo_slug,
        client=client.auth,
    )

    if isinstance(result, Error):
        return result

    return [item for item in result if isinstance(item, Milestone)]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def versions(client: BBClient, workspace: str, repo_slug: str) -> list[Version] | Error:
    """Return all versions for a repository.

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
        all_versions = await issues.versions(client, workspace="myws", repo_slug="myrepo")
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/versions
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-versions-get>`_
    """
    result = await async_paginate(
        get_repositories_workspace_repo_slug_versions.asyncio,
        workspace,
        repo_slug,
        client=client.auth,
    )

    if isinstance(result, Error):
        return result

    return [item for item in result if isinstance(item, Version)]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def components(client: BBClient, workspace: str, repo_slug: str) -> list[Component] | Error:
    """Return all components for a repository.

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
        all_components = await issues.components(client, workspace="myws", repo_slug="myrepo")
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/components
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-components-get>`_
    """
    result = await async_paginate(
        get_repositories_workspace_repo_slug_components.asyncio,
        workspace,
        repo_slug,
        client=client.auth,
    )

    if isinstance(result, Error):
        return result

    return [item for item in result if isinstance(item, Component)]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get_comment(
    client: BBClient, workspace: str, repo_slug: str, issue_id: int, comment_id: int
) -> IssueComment | Error | None:
    """Return a single comment on an issue, or ``None`` if not found.

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
        comment = await issues.get_comment(
            client, workspace="myws", repo_slug="myrepo", issue_id=42, comment_id=7
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/issues/{issue_id}/comments/{comment_id}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-issue-id-comments-comment-id-get>`_
    """
    result = await get_repositories_workspace_repo_slug_issues_issue_id_comments_comment_id.asyncio(
        workspace, repo_slug, issue_id, comment_id, client=client.auth
    )
    if isinstance(result, (IssueComment, Error)):
        return result
    return None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def update_comment(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    issue_id: int,
    comment_id: int,
    *,
    body: IssueComment | Unset = UNSET,
) -> IssueComment | Error | None:
    """Update a comment on an issue.

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
        updated = await issues.update_comment(
            client, workspace="myws", repo_slug="myrepo", issue_id=42, comment_id=7,
            body=IssueComment(content={"raw": "Updated text."}),
        )
        ```

    References:
        `PUT /2.0/repositories/{workspace}/{repo_slug}/issues/{issue_id}/comments/{comment_id}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-issue-id-comments-comment-id-put>`_
    """
    result = await put_repositories_workspace_repo_slug_issues_issue_id_comments_comment_id.asyncio(
        workspace, repo_slug, issue_id, comment_id, client=client.auth, body=body
    )
    if isinstance(result, (IssueComment, Error)):
        return result
    return None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def delete_comment(client: BBClient, workspace: str, repo_slug: str, issue_id: int, comment_id: int) -> None:
    """Delete a comment on an issue.

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
        await issues.delete_comment(
            client, workspace="myws", repo_slug="myrepo", issue_id=42, comment_id=7
        )
        ```

    References:
        `DELETE /2.0/repositories/{workspace}/{repo_slug}/issues/{issue_id}/comments/{comment_id}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-issue-id-comments-comment-id-delete>`_
    """
    await delete_repositories_workspace_repo_slug_issues_issue_id_comments_comment_id.asyncio(
        workspace, repo_slug, issue_id, comment_id, client=client.auth
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get_change(
    client: BBClient, workspace: str, repo_slug: str, issue_id: int, change_id: int
) -> IssueChange | Error | None:
    """Return a single change entry for an issue, or ``None`` if not found.

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
        change = await issues.get_change(
            client, workspace="myws", repo_slug="myrepo", issue_id=42, change_id=3
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/issues/{issue_id}/changes/{change_id}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-issue-id-changes-change-id-get>`_
    """
    result = await get_repositories_workspace_repo_slug_issues_issue_id_changes_change_id.asyncio(
        workspace, repo_slug, issue_id, change_id, client=client.auth
    )
    if isinstance(result, (IssueChange, Error)):
        return result
    return None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def add_change(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    issue_id: int,
    *,
    body: IssueChange | Unset = UNSET,
) -> IssueChange | Error | None:
    """Record a change on an issue (e.g. a status transition).

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
        change = await issues.add_change(
            client, workspace="myws", repo_slug="myrepo", issue_id=42,
            body=IssueChange(changes={"status": {"new": "resolved"}}),
        )
        ```

    References:
        `POST /2.0/repositories/{workspace}/{repo_slug}/issues/{issue_id}/changes
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-issue-id-changes-post>`_
    """
    result = await post_repositories_workspace_repo_slug_issues_issue_id_changes.asyncio(
        workspace, repo_slug, issue_id, client=client.auth, body=body
    )
    if isinstance(result, (IssueChange, Error)):
        return result
    return None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def voted(client: BBClient, workspace: str, repo_slug: str, issue_id: int) -> Any | Error | None:
    """Return the current user's vote status on an issue.

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
        status = await issues.voted(client, workspace="myws", repo_slug="myrepo", issue_id=42)
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/issues/{issue_id}/vote
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-issue-id-vote-get>`_
    """
    return await get_repositories_workspace_repo_slug_issues_issue_id_vote.asyncio(
        workspace, repo_slug, issue_id, client=client.auth
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def watching(client: BBClient, workspace: str, repo_slug: str, issue_id: int) -> Any | Error | None:
    """Return the current user's watch status on an issue.

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
        status = await issues.watching(client, workspace="myws", repo_slug="myrepo", issue_id=42)
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/issues/{issue_id}/watch
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-issue-id-watch-get>`_
    """
    return await get_repositories_workspace_repo_slug_issues_issue_id_watch.asyncio(
        workspace, repo_slug, issue_id, client=client.auth
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get_milestone(
    client: BBClient, workspace: str, repo_slug: str, milestone_id: int
) -> Milestone | Error | None:
    """Return a single milestone by ID, or ``None`` if not found.

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
        milestone = await issues.get_milestone(
            client, workspace="myws", repo_slug="myrepo", milestone_id=1
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/milestones/{milestone_id}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-milestones-milestone-id-get>`_
    """
    result = await get_repositories_workspace_repo_slug_milestones_milestone_id.asyncio(
        workspace, repo_slug, milestone_id, client=client.auth
    )
    if isinstance(result, (Milestone, Error)):
        return result
    return None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get_version(client: BBClient, workspace: str, repo_slug: str, version_id: int) -> Version | Error | None:
    """Return a single version by ID, or ``None`` if not found.

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
        version = await issues.get_version(
            client, workspace="myws", repo_slug="myrepo", version_id=2
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/versions/{version_id}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-versions-version-id-get>`_
    """
    result = await get_repositories_workspace_repo_slug_versions_version_id.asyncio(
        workspace, repo_slug, version_id, client=client.auth
    )
    if isinstance(result, (Version, Error)):
        return result
    return None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get_component(
    client: BBClient, workspace: str, repo_slug: str, component_id: int
) -> Component | Error | None:
    """Return a single component by ID, or ``None`` if not found.

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
        component = await issues.get_component(
            client, workspace="myws", repo_slug="myrepo", component_id=5
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/components/{component_id}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-components-component-id-get>`_
    """
    result = await get_repositories_workspace_repo_slug_components_component_id.asyncio(
        workspace, repo_slug, component_id, client=client.auth
    )
    if isinstance(result, (Component, Error)):
        return result
    return None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def attachments(client: BBClient, workspace: str, repo_slug: str, issue_id: int) -> Any | Error | None:
    """Return the list of attachments on an issue.

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
        files = await issues.attachments(
            client, workspace="myws", repo_slug="myrepo", issue_id=42
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/issues/{issue_id}/attachments
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-issue-id-attachments-get>`_
    """
    return await get_repositories_workspace_repo_slug_issues_issue_id_attachments.asyncio(
        workspace, repo_slug, issue_id, client=client.auth
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get_attachment(
    client: BBClient, workspace: str, repo_slug: str, issue_id: int, path: str
) -> Any | Error | None:
    """Return the redirect URL for a specific attachment on an issue.

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
        attachment = await issues.get_attachment(
            client, workspace="myws", repo_slug="myrepo", issue_id=42, path="screenshot.png"
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/issues/{issue_id}/attachments/{path}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-issue-id-attachments-path-get>`_
    """
    return await get_repositories_workspace_repo_slug_issues_issue_id_attachments_path.asyncio(
        workspace, repo_slug, issue_id, path, client=client.auth
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def upload_attachment(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    issue_id: int,
    *,
    body: Unset = UNSET,
) -> None:
    """Upload an attachment to an issue.

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
        await issues.upload_attachment(
            client, workspace="myws", repo_slug="myrepo", issue_id=42
        )
        ```

    References:
        `POST /2.0/repositories/{workspace}/{repo_slug}/issues/{issue_id}/attachments
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-issue-id-attachments-post>`_
    """
    await post_repositories_workspace_repo_slug_issues_issue_id_attachments.asyncio(
        workspace, repo_slug, issue_id, client=client.auth, body=body
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def delete_attachment(client: BBClient, workspace: str, repo_slug: str, issue_id: int, path: str) -> None:
    """Delete an attachment from an issue.

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
        await issues.delete_attachment(
            client, workspace="myws", repo_slug="myrepo", issue_id=42, path="screenshot.png"
        )
        ```

    References:
        `DELETE /2.0/repositories/{workspace}/{repo_slug}/issues/{issue_id}/attachments/{path}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-issue-id-attachments-path-delete>`_
    """
    await delete_repositories_workspace_repo_slug_issues_issue_id_attachments_path.asyncio(
        workspace, repo_slug, issue_id, path, client=client.auth
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def export(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: Unset = UNSET,
) -> None:
    """Start an asynchronous export of all issues for a repository.

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
        await issues.export(client, workspace="myws", repo_slug="myrepo")
        ```

    References:
        `POST /2.0/repositories/{workspace}/{repo_slug}/issues/export
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-export-post>`_
    """
    await post_repositories_workspace_repo_slug_issues_export.asyncio(
        workspace, repo_slug, client=client.auth, body=body
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def export_status(
    client: BBClient, workspace: str, repo_slug: str, repo_name: str, task_id: str
) -> Any | Error | None:
    """Check the status of an in-progress issue export task.

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
        status = await issues.export_status(
            client, workspace="myws", repo_slug="myrepo",
            repo_name="myrepo", task_id="abc123",
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/issues/export/{repo_name}-issues-{task_id}.zip
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-export-repo-name-issues-task-id-zip-get>`_
    """
    return await get_repositories_workspace_repo_slug_issues_export_repo_name_issues_task_id_zip.asyncio(
        workspace, repo_slug, repo_name, task_id, client=client.auth
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def import_status(client: BBClient, workspace: str, repo_slug: str) -> Any | Error | None:
    """Check the status of an in-progress issue import task.

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
        status = await issues.import_status(client, workspace="myws", repo_slug="myrepo")
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/issues/import
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-import-get>`_
    """
    return await get_repositories_workspace_repo_slug_issues_import.asyncio(workspace, repo_slug, client=client.auth)


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def import_data(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: Unset = UNSET,
) -> None:
    """Start an asynchronous import of issues for a repository.

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
        await issues.import_data(client, workspace="myws", repo_slug="myrepo")
        ```

    References:
        `POST /2.0/repositories/{workspace}/{repo_slug}/issues/import
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-issue-tracker/#api-repositories-workspace-repo-slug-issues-import-post>`_
    """
    await post_repositories_workspace_repo_slug_issues_import.asyncio(
        workspace, repo_slug, client=client.auth, body=body
    )
