from __future__ import annotations
import asyncio
from bb.cloud.models.error import Error
from bb.cloud.sdk._client import BBClient
from bb.cloud.types import UNSET, Unset
from bb.cloud.sdk import source as _async
__all__ = ['get', 'root', 'history', 'upload']

def get(client: BBClient, workspace: str, repo_slug: str, commit: str, path: str) -> object | Error | None:
    """Return the contents of a file at a given commit and path.

Synchronous wrapper around :func:`~bb.cloud.sdk.source.get`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug.
    commit: Commit hash or branch name.
    path: Path to the file within the repository.

Returns:
    File contents as returned by the API, or ``None`` on error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import source

    client = BBClient.from_env()
    contents = source.get(client, "myws", "myrepo", "main", "README.md")
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/src/{commit}/{path}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-source/#api-repositories-workspace-repo-slug-src-commit-path-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.source.get`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.get(client, workspace, repo_slug, commit, path))

def root(client: BBClient, workspace: str, repo_slug: str) -> object | Error | None:
    """Return the root directory listing of the default branch.

Synchronous wrapper around :func:`~bb.cloud.sdk.source.root`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug.

Returns:
    Directory listing object as returned by the API, or ``None`` on error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import source

    client = BBClient.from_env()
    tree = source.root(client, "myws", "myrepo")
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/src
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-source/#api-repositories-workspace-repo-slug-src-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.source.root`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.root(client, workspace, repo_slug))

def history(client: BBClient, workspace: str, repo_slug: str, commit: str, path: str) -> object | Error | None:
    """Return the file history — commits that touched a given path.

Synchronous wrapper around :func:`~bb.cloud.sdk.source.history`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug.
    commit: Commit hash or branch name.
    path: Path to the file within the repository.

Returns:
    File history object as returned by the API, or ``None`` on error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import source

    client = BBClient.from_env()
    log = source.history(client, "myws", "myrepo", "main", "src/main.py")
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/filehistory/{commit}/{path}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-source/#api-repositories-workspace-repo-slug-filehistory-commit-path-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.source.history`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.history(client, workspace, repo_slug, commit, path))

def upload(client: BBClient, workspace: str, repo_slug: str, *, body: Unset=UNSET) -> object | Error | None:
    """Upload files to a repository via the source endpoint.

Synchronous wrapper around :func:`~bb.cloud.sdk.source.upload`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug.
    body: Multipart upload body.

Returns:
    Response object as returned by the API, or ``None`` on error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import source

    client = BBClient.from_env()
    result = source.upload(client, "myws", "myrepo", body=...)
    ```

References:
    `POST /2.0/repositories/{workspace}/{repo_slug}/src
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-source/#api-repositories-workspace-repo-slug-src-post>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.source.upload`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.upload(client, workspace, repo_slug, body=body))
