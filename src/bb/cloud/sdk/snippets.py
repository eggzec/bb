from __future__ import annotations

from typing import Any

from bb.cloud.api.snippets import (
    delete_snippets_workspace_encoded_id,
    delete_snippets_workspace_encoded_id_comments_comment_id,
    delete_snippets_workspace_encoded_id_node_id,
    delete_snippets_workspace_encoded_id_watch,
    get_snippets,
    get_snippets_workspace,
    get_snippets_workspace_encoded_id,
    get_snippets_workspace_encoded_id_comments,
    get_snippets_workspace_encoded_id_comments_comment_id,
    get_snippets_workspace_encoded_id_commits,
    get_snippets_workspace_encoded_id_commits_revision,
    get_snippets_workspace_encoded_id_files_path,
    get_snippets_workspace_encoded_id_node_id,
    get_snippets_workspace_encoded_id_node_id_files_path,
    get_snippets_workspace_encoded_id_revision_diff,
    get_snippets_workspace_encoded_id_revision_patch,
    get_snippets_workspace_encoded_id_watch,
    get_snippets_workspace_encoded_id_watchers,
    post_snippets,
    post_snippets_workspace,
    post_snippets_workspace_encoded_id_comments,
    put_snippets_workspace_encoded_id,
    put_snippets_workspace_encoded_id_comments_comment_id,
    put_snippets_workspace_encoded_id_node_id,
    put_snippets_workspace_encoded_id_watch,
)
from bb.cloud.models.error import Error
from bb.cloud.models.snippet import Snippet
from bb.cloud.models.snippet_comment import SnippetComment
from bb.cloud.models.snippet_commit import SnippetCommit
from bb.cloud.sdk._auth_validation import AuthMethod, require_auth
from bb.cloud.sdk._client import BBClient
from bb.cloud.sdk._pagination import async_paginate

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


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def list(
    client: BBClient,
    workspace: str,
    *,
    pagelen: int = 25,
) -> list[Snippet] | Error:
    """Return all snippets in a workspace across all pages.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        pagelen: Number of results per page. Defaults to ``25``.

    Returns:
        All :class:`~bb.cloud.models.snippet.Snippet` objects in the workspace.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import snippets

        client = BBClient.from_env()
        result = await snippets.list(client, workspace="myws")
        ```

    References:
        `GET /2.0/snippets/{workspace}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-get>`_
    """
    result = await async_paginate(
        get_snippets_workspace.asyncio,
        workspace,
        client=client.auth,
        pagelen=pagelen,
    )

    if isinstance(result, Error):
        return result

    # Bitbucket API quirk (Free plan): returns HTTP 200 with a plain error string
    # as the first element of values[] instead of snippet objects.  Detect this
    # and surface it as an Error so callers are not silently handed garbage data.
    if result and isinstance(result[0], str):
        return Error.from_dict({"type": "error", "error": {"message": result[0]}})

    return [item for item in result if isinstance(item, Snippet)]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get(client: BBClient, workspace: str, encoded_id: str) -> Snippet | Error | None:
    """Return a single snippet by encoded ID, or ``None`` if not found.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        encoded_id: The snippet's encoded ID.

    Returns:
        The matching :class:`~bb.cloud.models.snippet.Snippet`, or ``None`` if
        the snippet does not exist.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import snippets

        client = BBClient.from_env()
        snippet = await snippets.get(client, workspace="myws", encoded_id="Xq8F3")
        ```

    References:
        `GET /2.0/snippets/{workspace}/{encoded_id}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-encoded-id-get>`_
    """
    result = await get_snippets_workspace_encoded_id.asyncio(workspace, encoded_id, client=client.auth)
    if isinstance(result, (Snippet, Error)):
        return result
    return None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def create(
    client: BBClient,
    workspace: str,
    *,
    body: Snippet = Snippet(),
) -> Snippet | Error | None:
    """Create a snippet in a workspace and return the created object.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        body: Snippet object with the fields to set on the new snippet.

    Returns:
        The newly created :class:`~bb.cloud.models.snippet.Snippet`, or ``None``
        on error.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.models.snippet import Snippet
        from bb.cloud.sdk import snippets

        client = BBClient.from_env()
        created = await snippets.create(
            client, workspace="myws", body=Snippet(title="My snippet")
        )
        ```

    References:
        `POST /2.0/snippets/{workspace}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-post>`_
    """
    result = await post_snippets_workspace.asyncio(workspace, client=client.auth, body=body)
    if isinstance(result, (Snippet, Error)):
        return result
    return None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def update(
    client: BBClient,
    workspace: str,
    encoded_id: str,
    *,
    body: Snippet = Snippet(),
) -> Snippet | Error | None:
    """Update a snippet and return the updated object.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        encoded_id: The snippet's encoded ID.
        body: Snippet object with updated field values.

    Returns:
        The updated :class:`~bb.cloud.models.snippet.Snippet`, or ``None`` on
        error.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.models.snippet import Snippet
        from bb.cloud.sdk import snippets

        client = BBClient.from_env()
        updated = await snippets.update(
            client, workspace="myws", encoded_id="Xq8F3",
            body=Snippet(title="Updated title"),
        )
        ```

    References:
        `PUT /2.0/snippets/{workspace}/{encoded_id}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-encoded-id-put>`_
    """
    result = await put_snippets_workspace_encoded_id.asyncio(workspace, encoded_id, client=client.auth, body=body)
    if isinstance(result, (Snippet, Error)):
        return result
    return None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def delete(client: BBClient, workspace: str, encoded_id: str) -> None:
    """Delete a snippet.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        encoded_id: The snippet's encoded ID.

    Returns:
        None

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import snippets

        client = BBClient.from_env()
        await snippets.delete(client, workspace="myws", encoded_id="Xq8F3")
        ```

    References:
        `DELETE /2.0/snippets/{workspace}/{encoded_id}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-encoded-id-delete>`_
    """
    await delete_snippets_workspace_encoded_id.asyncio(workspace, encoded_id, client=client.auth)


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def comments(
    client: BBClient, workspace: str, encoded_id: str, *, pagelen: int = 25
) -> list[SnippetComment] | Error:
    """Return all comments on a snippet across all pages.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        encoded_id: The snippet's encoded ID.
        pagelen: Number of results per page. Defaults to ``25``.

    Returns:
        All :class:`~bb.cloud.models.snippet_comment.SnippetComment` objects for
        the snippet.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import snippets

        client = BBClient.from_env()
        all_comments = await snippets.comments(client, workspace="myws", encoded_id="Xq8F3")
        ```

    References:
        `GET /2.0/snippets/{workspace}/{encoded_id}/comments
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-encoded-id-comments-get>`_
    """
    result = await async_paginate(
        get_snippets_workspace_encoded_id_comments.asyncio,
        workspace,
        encoded_id,
        client=client.auth,
        pagelen=pagelen,
    )

    if isinstance(result, Error):
        return result

    return [item for item in result if isinstance(item, SnippetComment)]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def add_comment(
    client: BBClient,
    workspace: str,
    encoded_id: str,
    *,
    body: SnippetComment = SnippetComment(),
) -> SnippetComment | Error | None:
    """Add a comment to a snippet and return the created comment.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        encoded_id: The snippet's encoded ID.
        body: Comment object with the content to post.

    Returns:
        The newly created :class:`~bb.cloud.models.snippet_comment.SnippetComment`,
        or ``None`` on error.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.models.snippet_comment import SnippetComment
        from bb.cloud.sdk import snippets

        client = BBClient.from_env()
        comment = await snippets.add_comment(
            client, workspace="myws", encoded_id="Xq8F3",
            body=SnippetComment(content={"raw": "Great snippet!"}),
        )
        ```

    References:
        `POST /2.0/snippets/{workspace}/{encoded_id}/comments
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-encoded-id-comments-post>`_
    """
    result = await post_snippets_workspace_encoded_id_comments.asyncio(
        workspace, encoded_id, client=client.auth, body=body
    )
    if isinstance(result, (SnippetComment, Error)):
        return result
    return None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def commits(
    client: BBClient, workspace: str, encoded_id: str, *, pagelen: int = 25
) -> list[SnippetCommit] | Error:
    """Return all commits for a snippet across all pages.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        encoded_id: The snippet's encoded ID.
        pagelen: Number of results per page. Defaults to ``25``.

    Returns:
        All :class:`~bb.cloud.models.snippet_commit.SnippetCommit` objects for
        the snippet.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import snippets

        client = BBClient.from_env()
        all_commits = await snippets.commits(client, workspace="myws", encoded_id="Xq8F3")
        ```

    References:
        `GET /2.0/snippets/{workspace}/{encoded_id}/commits
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-encoded-id-commits-get>`_
    """
    result = await async_paginate(
        get_snippets_workspace_encoded_id_commits.asyncio,
        workspace,
        encoded_id,
        client=client.auth,
        pagelen=pagelen,
    )

    if isinstance(result, Error):
        return result

    return [item for item in result if isinstance(item, SnippetCommit)]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def watch(client: BBClient, workspace: str, encoded_id: str) -> None:
    """Start watching a snippet.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        encoded_id: The snippet's encoded ID.

    Returns:
        None

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import snippets

        client = BBClient.from_env()
        await snippets.watch(client, workspace="myws", encoded_id="Xq8F3")
        ```

    References:
        `PUT /2.0/snippets/{workspace}/{encoded_id}/watch
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-encoded-id-watch-put>`_
    """
    await put_snippets_workspace_encoded_id_watch.asyncio(workspace, encoded_id, client=client.auth)


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def unwatch(client: BBClient, workspace: str, encoded_id: str) -> None:
    """Stop watching a snippet.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        encoded_id: The snippet's encoded ID.

    Returns:
        None

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import snippets

        client = BBClient.from_env()
        await snippets.unwatch(client, workspace="myws", encoded_id="Xq8F3")
        ```

    References:
        `DELETE /2.0/snippets/{workspace}/{encoded_id}/watch
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-encoded-id-watch-delete>`_
    """
    await delete_snippets_workspace_encoded_id_watch.asyncio(workspace, encoded_id, client=client.auth)


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def watchers(client: BBClient, workspace: str, encoded_id: str, *, pagelen: int = 25) -> list[Any] | Error:
    """Return all accounts watching a snippet across all pages.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        encoded_id: The snippet's encoded ID.
        pagelen: Number of results per page. Defaults to ``25``.

    Returns:
        All account objects watching the snippet.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import snippets

        client = BBClient.from_env()
        all_watchers = await snippets.watchers(client, workspace="myws", encoded_id="Xq8F3")
        ```

    References:
        `GET /2.0/snippets/{workspace}/{encoded_id}/watchers
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-encoded-id-watchers-get>`_
    """
    result = await async_paginate(
        get_snippets_workspace_encoded_id_watchers.asyncio,
        workspace,
        encoded_id,
        client=client.auth,
        pagelen=pagelen,
    )

    if isinstance(result, Error):
        return result

    return [x for x in result]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get_file(client: BBClient, workspace: str, encoded_id: str, path: str) -> str | Error | None:
    """Return the contents of a file within a snippet.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        encoded_id: The snippet's encoded ID.
        path: Path to the file within the snippet.

    Returns:
        The raw file contents as a string, or ``None`` on error.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import snippets

        client = BBClient.from_env()
        content = await snippets.get_file(
            client, workspace="myws", encoded_id="Xq8F3", path="hello.py"
        )
        ```

    References:
        `GET /2.0/snippets/{workspace}/{encoded_id}/files/{path}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-encoded-id-files-path-get>`_
    """
    return await get_snippets_workspace_encoded_id_files_path.asyncio(workspace, encoded_id, path, client=client.auth)


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def list_all(client: BBClient, *, pagelen: int = 25) -> list[Snippet] | Error:
    """Return all public snippets across Bitbucket Cloud.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        pagelen: Number of results per page. Defaults to ``25``.

    Returns:
        All public :class:`~bb.cloud.models.snippet.Snippet` objects.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import snippets

        client = BBClient.from_env()
        public_snippets = await snippets.list_all(client)
        ```

    References:
        `GET /2.0/snippets
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-get>`_
    """
    result = await async_paginate(
        get_snippets.asyncio,
        client=client.auth,
        pagelen=pagelen,
    )

    if isinstance(result, Error):
        return result

    return [item for item in result if isinstance(item, Snippet)]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def create_default(client: BBClient, *, body: Snippet = Snippet()) -> Snippet | Error | None:
    """Create a snippet under the authenticated user's default workspace.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        body: Snippet object with the fields to set on the new snippet.

    Returns:
        The newly created :class:`~bb.cloud.models.snippet.Snippet`, or ``None``
        on error.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.models.snippet import Snippet
        from bb.cloud.sdk import snippets

        client = BBClient.from_env()
        created = await snippets.create_default(client, body=Snippet(title="My snippet"))
        ```

    References:
        `POST /2.0/snippets
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-post>`_
    """
    result = await post_snippets.asyncio(client=client.auth, body=body)
    if isinstance(result, (Snippet, Error)):
        return result
    return None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get_comment(
    client: BBClient, workspace: str, encoded_id: str, comment_id: int
) -> SnippetComment | Error | None:
    """Return a single comment on a snippet, or ``None`` if not found.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        encoded_id: The snippet's encoded ID.
        comment_id: Numeric comment ID.

    Returns:
        The matching :class:`~bb.cloud.models.snippet_comment.SnippetComment`,
        or ``None`` if not found.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import snippets

        client = BBClient.from_env()
        comment = await snippets.get_comment(
            client, workspace="myws", encoded_id="Xq8F3", comment_id=5
        )
        ```

    References:
        `GET /2.0/snippets/{workspace}/{encoded_id}/comments/{comment_id}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-encoded-id-comments-comment-id-get>`_
    """
    result = await get_snippets_workspace_encoded_id_comments_comment_id.asyncio(
        workspace, encoded_id, comment_id, client=client.auth
    )
    if isinstance(result, (SnippetComment, Error)):
        return result
    return None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def update_comment(
    client: BBClient,
    workspace: str,
    encoded_id: str,
    comment_id: int,
    *,
    body: SnippetComment = SnippetComment(),
) -> SnippetComment | Error | None:
    """Update a comment on a snippet.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        encoded_id: The snippet's encoded ID.
        comment_id: Numeric comment ID.
        body: Comment object with updated content.

    Returns:
        The updated :class:`~bb.cloud.models.snippet_comment.SnippetComment`, or
        ``None`` on error.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.models.snippet_comment import SnippetComment
        from bb.cloud.sdk import snippets

        client = BBClient.from_env()
        updated = await snippets.update_comment(
            client, workspace="myws", encoded_id="Xq8F3", comment_id=5,
            body=SnippetComment(content={"raw": "Updated text."}),
        )
        ```

    References:
        `PUT /2.0/snippets/{workspace}/{encoded_id}/comments/{comment_id}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-encoded-id-comments-comment-id-put>`_
    """
    result = await put_snippets_workspace_encoded_id_comments_comment_id.asyncio(
        workspace, encoded_id, comment_id, client=client.auth, body=body
    )
    if isinstance(result, (SnippetComment, Error)):
        return result
    return None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def delete_comment(client: BBClient, workspace: str, encoded_id: str, comment_id: int) -> None:
    """Delete a comment on a snippet.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        encoded_id: The snippet's encoded ID.
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
        from bb.cloud.sdk import snippets

        client = BBClient.from_env()
        await snippets.delete_comment(
            client, workspace="myws", encoded_id="Xq8F3", comment_id=5
        )
        ```

    References:
        `DELETE /2.0/snippets/{workspace}/{encoded_id}/comments/{comment_id}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-encoded-id-comments-comment-id-delete>`_
    """
    await delete_snippets_workspace_encoded_id_comments_comment_id.asyncio(
        workspace, encoded_id, comment_id, client=client.auth
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def watching(client: BBClient, workspace: str, encoded_id: str) -> Any | Error | None:
    """Return the current user's watch status for a snippet.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        encoded_id: The snippet's encoded ID.

    Returns:
        The API response object representing the watch status, or ``None`` if the
        user is not watching the snippet.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import snippets

        client = BBClient.from_env()
        status = await snippets.watching(client, workspace="myws", encoded_id="Xq8F3")
        ```

    References:
        `GET /2.0/snippets/{workspace}/{encoded_id}/watch
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-encoded-id-watch-get>`_
    """
    return await get_snippets_workspace_encoded_id_watch.asyncio(workspace, encoded_id, client=client.auth)


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get_commit(client: BBClient, workspace: str, encoded_id: str, revision: str) -> SnippetCommit | Error | None:
    """Return a single commit in a snippet's history, or ``None`` if not found.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        encoded_id: The snippet's encoded ID.
        revision: The commit hash or revision identifier.

    Returns:
        The matching :class:`~bb.cloud.models.snippet_commit.SnippetCommit`, or
        ``None`` if not found.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import snippets

        client = BBClient.from_env()
        commit = await snippets.get_commit(
            client, workspace="myws", encoded_id="Xq8F3", revision="a3c4d5e"
        )
        ```

    References:
        `GET /2.0/snippets/{workspace}/{encoded_id}/commits/{revision}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-encoded-id-commits-revision-get>`_
    """
    result = await get_snippets_workspace_encoded_id_commits_revision.asyncio(
        workspace, encoded_id, revision, client=client.auth
    )
    if isinstance(result, (SnippetCommit, Error)):
        return result
    return None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get_node(client: BBClient, workspace: str, encoded_id: str, node_id: str) -> Any | Error | None:
    """Return a snippet at a specific node (commit) in its history.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        encoded_id: The snippet's encoded ID.
        node_id: The node (commit) hash.

    Returns:
        The API response object for the snippet at the given node, or ``None``
        on error.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import snippets

        client = BBClient.from_env()
        node = await snippets.get_node(
            client, workspace="myws", encoded_id="Xq8F3", node_id="a3c4d5e"
        )
        ```

    References:
        `GET /2.0/snippets/{workspace}/{encoded_id}/{node_id}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-encoded-id-node-id-get>`_
    """
    return await get_snippets_workspace_encoded_id_node_id.asyncio(workspace, encoded_id, node_id, client=client.auth)


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def update_node(
    client: BBClient,
    workspace: str,
    encoded_id: str,
    node_id: str,
    *,
    body: Snippet = Snippet(),
) -> Any | Error | None:
    """Update a snippet at a specific node.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        encoded_id: The snippet's encoded ID.
        node_id: The node (commit) hash to update from.
        body: Snippet object with updated field values.

    Returns:
        The API response object for the updated snippet node, or ``None`` on
        error.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.models.snippet import Snippet
        from bb.cloud.sdk import snippets

        client = BBClient.from_env()
        result = await snippets.update_node(
            client, workspace="myws", encoded_id="Xq8F3", node_id="a3c4d5e",
            body=Snippet(title="Updated at node"),
        )
        ```

    References:
        `PUT /2.0/snippets/{workspace}/{encoded_id}/{node_id}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-encoded-id-node-id-put>`_
    """
    return await put_snippets_workspace_encoded_id_node_id.asyncio(
        workspace, encoded_id, node_id, client=client.auth, body=body
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def delete_node(client: BBClient, workspace: str, encoded_id: str, node_id: str) -> None:
    """Delete a snippet at a specific node.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        encoded_id: The snippet's encoded ID.
        node_id: The node (commit) hash to delete from.

    Returns:
        None

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import snippets

        client = BBClient.from_env()
        await snippets.delete_node(
            client, workspace="myws", encoded_id="Xq8F3", node_id="a3c4d5e"
        )
        ```

    References:
        `DELETE /2.0/snippets/{workspace}/{encoded_id}/{node_id}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-encoded-id-node-id-delete>`_
    """
    await delete_snippets_workspace_encoded_id_node_id.asyncio(workspace, encoded_id, node_id, client=client.auth)


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get_node_file(
    client: BBClient, workspace: str, encoded_id: str, node_id: str, path: str
) -> Any | Error | None:
    """Return a file from a snippet at a specific node.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        encoded_id: The snippet's encoded ID.
        node_id: The node (commit) hash.
        path: Path to the file within the snippet.

    Returns:
        The raw file contents or API response object, or ``None`` on error.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import snippets

        client = BBClient.from_env()
        content = await snippets.get_node_file(
            client, workspace="myws", encoded_id="Xq8F3", node_id="a3c4d5e", path="hello.py"
        )
        ```

    References:
        `GET /2.0/snippets/{workspace}/{encoded_id}/{node_id}/files/{path}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-encoded-id-node-id-files-path-get>`_
    """
    return await get_snippets_workspace_encoded_id_node_id_files_path.asyncio(
        workspace, encoded_id, node_id, path, client=client.auth
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def diff(client: BBClient, workspace: str, encoded_id: str, revision: str) -> str | Error | None:
    """Return the diff for a snippet at a specific revision.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        encoded_id: The snippet's encoded ID.
        revision: The revision or commit hash to diff against.

    Returns:
        The unified diff as a string, or ``None`` on error.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import snippets

        client = BBClient.from_env()
        diff_text = await snippets.diff(
            client, workspace="myws", encoded_id="Xq8F3", revision="a3c4d5e"
        )
        ```

    References:
        `GET /2.0/snippets/{workspace}/{encoded_id}/{revision}/diff
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-encoded-id-revision-diff-get>`_
    """
    return await get_snippets_workspace_encoded_id_revision_diff.asyncio(
        workspace, encoded_id, revision, client=client.auth
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def patch(client: BBClient, workspace: str, encoded_id: str, revision: str) -> str | Error | None:
    """Return the patch for a snippet at a specific revision.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        encoded_id: The snippet's encoded ID.
        revision: The revision or commit hash to generate a patch for.

    Returns:
        The patch as a string, or ``None`` on error.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import snippets

        client = BBClient.from_env()
        patch_text = await snippets.patch(
            client, workspace="myws", encoded_id="Xq8F3", revision="a3c4d5e"
        )
        ```

    References:
        `GET /2.0/snippets/{workspace}/{encoded_id}/{revision}/patch
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-encoded-id-revision-patch-get>`_
    """
    return await get_snippets_workspace_encoded_id_revision_patch.asyncio(
        workspace, encoded_id, revision, client=client.auth
    )
