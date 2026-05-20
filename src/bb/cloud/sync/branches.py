from __future__ import annotations
from bb.cloud.models.branch import Branch
from bb.cloud.models.error import Error
from bb.cloud.models.tag import Tag
from bb.cloud.sdk._client import BBClient
from bb.cloud.types import UNSET, Unset
from bb.cloud.sdk import branches as _async
__all__ = ['list', 'get', 'create', 'delete', 'tags', 'get_tag', 'create_tag', 'delete_tag']

def list(client: BBClient, workspace: str, repo_slug: str, *, q: str | Unset=UNSET, sort: str | Unset=UNSET, pagelen: int=25) -> list[Branch] | Error:
    """List all branches for a repository across all pages.

Synchronous wrapper around :func:`~bb.cloud.sdk.branches.list`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
    repo_slug: Repository slug or UUID.
    q: Optional query filter string (Bitbucket query syntax, e.g. ``name ~ "feature"``).
    sort: Optional sort field (e.g. ``-target.date`` for newest first).
    pagelen: Number of results per page. Defaults to ``25``.

Returns:
    All :class:`~bb.cloud.models.branch.Branch` objects across all pages.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import branches

    client = BBClient.from_env()
    result = branches.list(client, workspace="myworkspace", repo_slug="myrepo")
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/refs/branches
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-refs/#api-repositories-workspace-repo-slug-refs-branches-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.branches.list`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.list(client, workspace, repo_slug, q=q, sort=sort, pagelen=pagelen))

def get(client: BBClient, workspace: str, repo_slug: str, name: str) -> Branch | Error | None:
    """Fetch a single branch by name.

Synchronous wrapper around :func:`~bb.cloud.sdk.branches.get`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
    repo_slug: Repository slug or UUID.
    name: Branch name (e.g. ``main`` or ``feature/my-feature``).

Returns:
    The :class:`~bb.cloud.models.branch.Branch`, or ``None`` if not found.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import branches

    client = BBClient.from_env()
    branch = branches.get(
        client, workspace="myworkspace", repo_slug="myrepo", name="main"
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/refs/branches/{name}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-refs/#api-repositories-workspace-repo-slug-refs-branches-name-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.branches.get`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.get(client, workspace, repo_slug, name))

def create(client: BBClient, workspace: str, repo_slug: str, *, name: str, target_hash: str) -> Branch | Error | None:
    """Create a branch pointing at a target commit hash.

Synchronous wrapper around :func:`~bb.cloud.sdk.branches.create`.

The Bitbucket Cloud spec omits ``requestBody`` for this endpoint so the generated
wrapper has no body parameter. This function sends the JSON body directly via the
underlying async httpx client.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
    repo_slug: Repository slug or UUID.
    name: Name of the new branch.
    target_hash: Full commit hash that the new branch should point to.

Returns:
    The created :class:`~bb.cloud.models.branch.Branch`, or ``None`` on error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import branches

    client = BBClient.from_env()
    branch = branches.create(
        client,
        workspace="myworkspace",
        repo_slug="myrepo",
        name="feature/new-branch",
        target_hash="a1b2c3d4e5f6",
    )
    ```

References:
    `POST /2.0/repositories/{workspace}/{repo_slug}/refs/branches
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-refs/#api-repositories-workspace-repo-slug-refs-branches-post>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.branches.create`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.create(client, workspace, repo_slug, name=name, target_hash=target_hash))

def delete(client: BBClient, workspace: str, repo_slug: str, name: str) -> None:
    """Delete a branch.

Synchronous wrapper around :func:`~bb.cloud.sdk.branches.delete`.

Does not raise on 404 or other non-success status codes.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
    repo_slug: Repository slug or UUID.
    name: Branch name to delete.

Returns:
    None.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import branches

    client = BBClient.from_env()
    branches.delete(
        client, workspace="myworkspace", repo_slug="myrepo", name="feature/old-branch"
    )
    ```

References:
    `DELETE /2.0/repositories/{workspace}/{repo_slug}/refs/branches/{name}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-refs/#api-repositories-workspace-repo-slug-refs-branches-name-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.branches.delete`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.delete(client, workspace, repo_slug, name))

def tags(client: BBClient, workspace: str, repo_slug: str, *, q: str | Unset=UNSET, sort: str | Unset=UNSET, pagelen: int=25) -> list[Tag] | Error:
    """List all tags for a repository across all pages.

Synchronous wrapper around :func:`~bb.cloud.sdk.branches.tags`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
    repo_slug: Repository slug or UUID.
    q: Optional query filter string (Bitbucket query syntax).
    sort: Optional sort field (e.g. ``-target.date`` for newest first).
    pagelen: Number of results per page. Defaults to ``25``.

Returns:
    All :class:`~bb.cloud.models.tag.Tag` objects across all pages.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import branches

    client = BBClient.from_env()
    result = branches.tags(client, workspace="myworkspace", repo_slug="myrepo")
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/refs/tags
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-refs/#api-repositories-workspace-repo-slug-refs-tags-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.branches.tags`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.tags(client, workspace, repo_slug, q=q, sort=sort, pagelen=pagelen))

def get_tag(client: BBClient, workspace: str, repo_slug: str, name: str) -> Tag | Error | None:
    """Fetch a single tag by name.

Synchronous wrapper around :func:`~bb.cloud.sdk.branches.get_tag`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
    repo_slug: Repository slug or UUID.
    name: Tag name.

Returns:
    The :class:`~bb.cloud.models.tag.Tag`, or ``None`` if not found.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import branches

    client = BBClient.from_env()
    tag = branches.get_tag(
        client, workspace="myworkspace", repo_slug="myrepo", name="v1.0.0"
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/refs/tags/{name}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-refs/#api-repositories-workspace-repo-slug-refs-tags-name-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.branches.get_tag`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.get_tag(client, workspace, repo_slug, name))

def create_tag(client: BBClient, workspace: str, repo_slug: str, *, body: Tag | Unset=UNSET) -> Tag | Error | None:
    """Create a tag in a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.branches.create_tag`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
    repo_slug: Repository slug or UUID.
    body: Tag payload. Use :class:`~bb.cloud.models.tag.Tag` populated with at minimum
        ``name`` and ``target``.

Returns:
    The created :class:`~bb.cloud.models.tag.Tag`, or ``None`` on error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import branches
    from bb.cloud.models.tag import Tag

    client = BBClient.from_env()
    tag = branches.create_tag(
        client, workspace="myworkspace", repo_slug="myrepo", body=Tag(name="v1.0.0", ...)
    )
    ```

References:
    `POST /2.0/repositories/{workspace}/{repo_slug}/refs/tags
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-refs/#api-repositories-workspace-repo-slug-refs-tags-post>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.branches.create_tag`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.create_tag(client, workspace, repo_slug, body=body))

def delete_tag(client: BBClient, workspace: str, repo_slug: str, name: str) -> None:
    """Delete a tag from a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.branches.delete_tag`.

Does not raise on 404 or other non-success status codes.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
    repo_slug: Repository slug or UUID.
    name: Tag name to delete.

Returns:
    None.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import branches

    client = BBClient.from_env()
    branches.delete_tag(
        client, workspace="myworkspace", repo_slug="myrepo", name="v0.9.0"
    )
    ```

References:
    `DELETE /2.0/repositories/{workspace}/{repo_slug}/refs/tags/{name}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-refs/#api-repositories-workspace-repo-slug-refs-tags-name-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.branches.delete_tag`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.delete_tag(client, workspace, repo_slug, name))
