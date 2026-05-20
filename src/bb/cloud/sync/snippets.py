from __future__ import annotations
from typing import Any
from bb.cloud.models.error import Error
from bb.cloud.models.snippet import Snippet
from bb.cloud.models.snippet_comment import SnippetComment
from bb.cloud.models.snippet_commit import SnippetCommit
from bb.cloud.sdk._client import BBClient
from bb.cloud.types import UNSET, Unset
from bb.cloud.sdk import snippets as _async
__all__ = ['list', 'get', 'create', 'update', 'delete', 'comments', 'add_comment', 'commits', 'watch', 'unwatch', 'watchers', 'get_file', 'list_all', 'create_default', 'get_comment', 'update_comment', 'delete_comment', 'watching', 'get_commit', 'get_node', 'update_node', 'delete_node', 'get_node_file', 'diff', 'patch']

def list(client: BBClient, workspace: str, *, pagelen: int=25) -> list[Snippet] | Error:
    """Return all snippets in a workspace across all pages.

Synchronous wrapper around :func:`~bb.cloud.sdk.snippets.list`.

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
    result = snippets.list(client, workspace="myws")
    ```

References:
    `GET /2.0/snippets/{workspace}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.snippets.list`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.list(client, workspace, pagelen=pagelen))

def get(client: BBClient, workspace: str, encoded_id: str) -> Snippet | Error | None:
    """Return a single snippet by encoded ID, or ``None`` if not found.

Synchronous wrapper around :func:`~bb.cloud.sdk.snippets.get`.

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
    snippet = snippets.get(client, workspace="myws", encoded_id="Xq8F3")
    ```

References:
    `GET /2.0/snippets/{workspace}/{encoded_id}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-encoded-id-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.snippets.get`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.get(client, workspace, encoded_id))

def create(client: BBClient, workspace: str, *, body: Snippet | Unset=UNSET) -> Snippet | Error | None:
    """Create a snippet in a workspace and return the created object.

Synchronous wrapper around :func:`~bb.cloud.sdk.snippets.create`.

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
    created = snippets.create(
        client, workspace="myws", body=Snippet(title="My snippet")
    )
    ```

References:
    `POST /2.0/snippets/{workspace}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-post>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.snippets.create`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.create(client, workspace, body=body))

def update(client: BBClient, workspace: str, encoded_id: str, *, body: Snippet | Unset=UNSET) -> Snippet | Error | None:
    """Update a snippet and return the updated object.

Synchronous wrapper around :func:`~bb.cloud.sdk.snippets.update`.

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
    updated = snippets.update(
        client, workspace="myws", encoded_id="Xq8F3",
        body=Snippet(title="Updated title"),
    )
    ```

References:
    `PUT /2.0/snippets/{workspace}/{encoded_id}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-encoded-id-put>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.snippets.update`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.update(client, workspace, encoded_id, body=body))

def delete(client: BBClient, workspace: str, encoded_id: str) -> None:
    """Delete a snippet.

Synchronous wrapper around :func:`~bb.cloud.sdk.snippets.delete`.

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
    snippets.delete(client, workspace="myws", encoded_id="Xq8F3")
    ```

References:
    `DELETE /2.0/snippets/{workspace}/{encoded_id}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-encoded-id-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.snippets.delete`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.delete(client, workspace, encoded_id))

def comments(client: BBClient, workspace: str, encoded_id: str, *, pagelen: int=25) -> list[SnippetComment] | Error:
    """Return all comments on a snippet across all pages.

Synchronous wrapper around :func:`~bb.cloud.sdk.snippets.comments`.

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
    all_comments = snippets.comments(client, workspace="myws", encoded_id="Xq8F3")
    ```

References:
    `GET /2.0/snippets/{workspace}/{encoded_id}/comments
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-encoded-id-comments-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.snippets.comments`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.comments(client, workspace, encoded_id, pagelen=pagelen))

def add_comment(client: BBClient, workspace: str, encoded_id: str, *, body: SnippetComment | Unset=UNSET) -> SnippetComment | Error | None:
    """Add a comment to a snippet and return the created comment.

Synchronous wrapper around :func:`~bb.cloud.sdk.snippets.add_comment`.

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
    comment = snippets.add_comment(
        client, workspace="myws", encoded_id="Xq8F3",
        body=SnippetComment(content={"raw": "Great snippet!"}),
    )
    ```

References:
    `POST /2.0/snippets/{workspace}/{encoded_id}/comments
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-encoded-id-comments-post>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.snippets.add_comment`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.add_comment(client, workspace, encoded_id, body=body))

def commits(client: BBClient, workspace: str, encoded_id: str, *, pagelen: int=25) -> list[SnippetCommit] | Error:
    """Return all commits for a snippet across all pages.

Synchronous wrapper around :func:`~bb.cloud.sdk.snippets.commits`.

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
    all_commits = snippets.commits(client, workspace="myws", encoded_id="Xq8F3")
    ```

References:
    `GET /2.0/snippets/{workspace}/{encoded_id}/commits
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-encoded-id-commits-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.snippets.commits`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.commits(client, workspace, encoded_id, pagelen=pagelen))

def watch(client: BBClient, workspace: str, encoded_id: str) -> None:
    """Start watching a snippet.

Synchronous wrapper around :func:`~bb.cloud.sdk.snippets.watch`.

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
    snippets.watch(client, workspace="myws", encoded_id="Xq8F3")
    ```

References:
    `PUT /2.0/snippets/{workspace}/{encoded_id}/watch
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-encoded-id-watch-put>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.snippets.watch`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.watch(client, workspace, encoded_id))

def unwatch(client: BBClient, workspace: str, encoded_id: str) -> None:
    """Stop watching a snippet.

Synchronous wrapper around :func:`~bb.cloud.sdk.snippets.unwatch`.

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
    snippets.unwatch(client, workspace="myws", encoded_id="Xq8F3")
    ```

References:
    `DELETE /2.0/snippets/{workspace}/{encoded_id}/watch
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-encoded-id-watch-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.snippets.unwatch`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.unwatch(client, workspace, encoded_id))

def watchers(client: BBClient, workspace: str, encoded_id: str, *, pagelen: int=25) -> list[Any] | Error:
    """Return all accounts watching a snippet across all pages.

Synchronous wrapper around :func:`~bb.cloud.sdk.snippets.watchers`.

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
    all_watchers = snippets.watchers(client, workspace="myws", encoded_id="Xq8F3")
    ```

References:
    `GET /2.0/snippets/{workspace}/{encoded_id}/watchers
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-encoded-id-watchers-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.snippets.watchers`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.watchers(client, workspace, encoded_id, pagelen=pagelen))

def get_file(client: BBClient, workspace: str, encoded_id: str, path: str) -> str | Error | None:
    """Return the contents of a file within a snippet.

Synchronous wrapper around :func:`~bb.cloud.sdk.snippets.get_file`.

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
    content = snippets.get_file(
        client, workspace="myws", encoded_id="Xq8F3", path="hello.py"
    )
    ```

References:
    `GET /2.0/snippets/{workspace}/{encoded_id}/files/{path}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-encoded-id-files-path-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.snippets.get_file`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.get_file(client, workspace, encoded_id, path))

def list_all(client: BBClient, *, pagelen: int=25) -> list[Snippet] | Error:
    """Return all public snippets across Bitbucket Cloud.

Synchronous wrapper around :func:`~bb.cloud.sdk.snippets.list_all`.

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
    public_snippets = snippets.list_all(client)
    ```

References:
    `GET /2.0/snippets
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.snippets.list_all`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.list_all(client, pagelen=pagelen))

def create_default(client: BBClient, *, body: Snippet | Unset=UNSET) -> Snippet | Error | None:
    """Create a snippet under the authenticated user's default workspace.

Synchronous wrapper around :func:`~bb.cloud.sdk.snippets.create_default`.

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
    created = snippets.create_default(client, body=Snippet(title="My snippet"))
    ```

References:
    `POST /2.0/snippets
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-post>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.snippets.create_default`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.create_default(client, body=body))

def get_comment(client: BBClient, workspace: str, encoded_id: str, comment_id: int) -> SnippetComment | Error | None:
    """Return a single comment on a snippet, or ``None`` if not found.

Synchronous wrapper around :func:`~bb.cloud.sdk.snippets.get_comment`.

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
    comment = snippets.get_comment(
        client, workspace="myws", encoded_id="Xq8F3", comment_id=5
    )
    ```

References:
    `GET /2.0/snippets/{workspace}/{encoded_id}/comments/{comment_id}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-encoded-id-comments-comment-id-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.snippets.get_comment`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.get_comment(client, workspace, encoded_id, comment_id))

def update_comment(client: BBClient, workspace: str, encoded_id: str, comment_id: int, *, body: SnippetComment | Unset=UNSET) -> SnippetComment | Error | None:
    """Update a comment on a snippet.

Synchronous wrapper around :func:`~bb.cloud.sdk.snippets.update_comment`.

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
    updated = snippets.update_comment(
        client, workspace="myws", encoded_id="Xq8F3", comment_id=5,
        body=SnippetComment(content={"raw": "Updated text."}),
    )
    ```

References:
    `PUT /2.0/snippets/{workspace}/{encoded_id}/comments/{comment_id}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-encoded-id-comments-comment-id-put>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.snippets.update_comment`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.update_comment(client, workspace, encoded_id, comment_id, body=body))

def delete_comment(client: BBClient, workspace: str, encoded_id: str, comment_id: int) -> None:
    """Delete a comment on a snippet.

Synchronous wrapper around :func:`~bb.cloud.sdk.snippets.delete_comment`.

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
    snippets.delete_comment(
        client, workspace="myws", encoded_id="Xq8F3", comment_id=5
    )
    ```

References:
    `DELETE /2.0/snippets/{workspace}/{encoded_id}/comments/{comment_id}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-encoded-id-comments-comment-id-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.snippets.delete_comment`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.delete_comment(client, workspace, encoded_id, comment_id))

def watching(client: BBClient, workspace: str, encoded_id: str) -> Any | Error | None:
    """Return the current user's watch status for a snippet.

Synchronous wrapper around :func:`~bb.cloud.sdk.snippets.watching`.

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
    status = snippets.watching(client, workspace="myws", encoded_id="Xq8F3")
    ```

References:
    `GET /2.0/snippets/{workspace}/{encoded_id}/watch
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-encoded-id-watch-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.snippets.watching`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.watching(client, workspace, encoded_id))

def get_commit(client: BBClient, workspace: str, encoded_id: str, revision: str) -> SnippetCommit | Error | None:
    """Return a single commit in a snippet's history, or ``None`` if not found.

Synchronous wrapper around :func:`~bb.cloud.sdk.snippets.get_commit`.

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
    commit = snippets.get_commit(
        client, workspace="myws", encoded_id="Xq8F3", revision="a3c4d5e"
    )
    ```

References:
    `GET /2.0/snippets/{workspace}/{encoded_id}/commits/{revision}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-encoded-id-commits-revision-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.snippets.get_commit`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.get_commit(client, workspace, encoded_id, revision))

def get_node(client: BBClient, workspace: str, encoded_id: str, node_id: str) -> Any | Error | None:
    """Return a snippet at a specific node (commit) in its history.

Synchronous wrapper around :func:`~bb.cloud.sdk.snippets.get_node`.

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
    node = snippets.get_node(
        client, workspace="myws", encoded_id="Xq8F3", node_id="a3c4d5e"
    )
    ```

References:
    `GET /2.0/snippets/{workspace}/{encoded_id}/{node_id}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-encoded-id-node-id-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.snippets.get_node`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.get_node(client, workspace, encoded_id, node_id))

def update_node(client: BBClient, workspace: str, encoded_id: str, node_id: str, *, body: Snippet | Unset=UNSET) -> Any | Error | None:
    """Update a snippet at a specific node.

Synchronous wrapper around :func:`~bb.cloud.sdk.snippets.update_node`.

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
    result = snippets.update_node(
        client, workspace="myws", encoded_id="Xq8F3", node_id="a3c4d5e",
        body=Snippet(title="Updated at node"),
    )
    ```

References:
    `PUT /2.0/snippets/{workspace}/{encoded_id}/{node_id}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-encoded-id-node-id-put>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.snippets.update_node`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.update_node(client, workspace, encoded_id, node_id, body=body))

def delete_node(client: BBClient, workspace: str, encoded_id: str, node_id: str) -> None:
    """Delete a snippet at a specific node.

Synchronous wrapper around :func:`~bb.cloud.sdk.snippets.delete_node`.

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
    snippets.delete_node(
        client, workspace="myws", encoded_id="Xq8F3", node_id="a3c4d5e"
    )
    ```

References:
    `DELETE /2.0/snippets/{workspace}/{encoded_id}/{node_id}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-encoded-id-node-id-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.snippets.delete_node`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.delete_node(client, workspace, encoded_id, node_id))

def get_node_file(client: BBClient, workspace: str, encoded_id: str, node_id: str, path: str) -> Any | Error | None:
    """Return a file from a snippet at a specific node.

Synchronous wrapper around :func:`~bb.cloud.sdk.snippets.get_node_file`.

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
    content = snippets.get_node_file(
        client, workspace="myws", encoded_id="Xq8F3", node_id="a3c4d5e", path="hello.py"
    )
    ```

References:
    `GET /2.0/snippets/{workspace}/{encoded_id}/{node_id}/files/{path}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-encoded-id-node-id-files-path-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.snippets.get_node_file`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.get_node_file(client, workspace, encoded_id, node_id, path))

def diff(client: BBClient, workspace: str, encoded_id: str, revision: str) -> str | Error | None:
    """Return the diff for a snippet at a specific revision.

Synchronous wrapper around :func:`~bb.cloud.sdk.snippets.diff`.

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
    diff_text = snippets.diff(
        client, workspace="myws", encoded_id="Xq8F3", revision="a3c4d5e"
    )
    ```

References:
    `GET /2.0/snippets/{workspace}/{encoded_id}/{revision}/diff
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-encoded-id-revision-diff-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.snippets.diff`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.diff(client, workspace, encoded_id, revision))

def patch(client: BBClient, workspace: str, encoded_id: str, revision: str) -> str | Error | None:
    """Return the patch for a snippet at a specific revision.

Synchronous wrapper around :func:`~bb.cloud.sdk.snippets.patch`.

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
    patch_text = snippets.patch(
        client, workspace="myws", encoded_id="Xq8F3", revision="a3c4d5e"
    )
    ```

References:
    `GET /2.0/snippets/{workspace}/{encoded_id}/{revision}/patch
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-encoded-id-revision-patch-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.snippets.patch`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.patch(client, workspace, encoded_id, revision))
