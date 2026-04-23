from __future__ import annotations
import asyncio
from typing import Any
from bb.cloud.models.error import Error
from bb.cloud.sdk._client import BBClient
from bb.cloud.types import UNSET, Unset
from bb.cloud.sdk import downloads as _async
__all__ = ['list', 'get', 'upload', 'delete']

def list(client: BBClient, workspace: str, repo_slug: str, *, pagelen: int=25) -> list[Any] | Error:
    """Return all download artifacts for a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.downloads.list`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug.
    pagelen: Number of results per page. Defaults to ``25``.

Returns:
    List of download artifact objects.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import downloads

    client = BBClient.from_env()
    artifacts = downloads.list(client, "myws", "myrepo")
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/downloads
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-downloads/#api-repositories-workspace-repo-slug-downloads-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.downloads.list`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.list(client, workspace, repo_slug, pagelen=pagelen))

def get(client: BBClient, workspace: str, repo_slug: str, filename: str) -> Any:
    """Return a single download artifact by filename, or ``None`` if not found.

Synchronous wrapper around :func:`~bb.cloud.sdk.downloads.get`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug.
    filename: Name of the download artifact.

Returns:
    Download artifact object, or ``None`` if not found.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import downloads

    client = BBClient.from_env()
    artifact = downloads.get(client, "myws", "myrepo", "release.tar.gz")
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/downloads/{filename}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-downloads/#api-repositories-workspace-repo-slug-downloads-filename-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.downloads.get`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.get(client, workspace, repo_slug, filename))

def upload(client: BBClient, workspace: str, repo_slug: str, *, body: Unset=UNSET) -> Any:
    """Upload a file as a download artifact for a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.downloads.upload`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug.
    body: Multipart upload body.

Returns:
    Created download artifact object, or ``None`` on error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import downloads

    client = BBClient.from_env()
    result = downloads.upload(client, "myws", "myrepo", body=...)
    ```

References:
    `POST /2.0/repositories/{workspace}/{repo_slug}/downloads
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-downloads/#api-repositories-workspace-repo-slug-downloads-post>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.downloads.upload`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.upload(client, workspace, repo_slug, body=body))

def delete(client: BBClient, workspace: str, repo_slug: str, filename: str) -> None:
    """Delete a download artifact by filename.

Synchronous wrapper around :func:`~bb.cloud.sdk.downloads.delete`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug.
    filename: Name of the download artifact to delete.

Returns:
    None.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import downloads

    client = BBClient.from_env()
    downloads.delete(client, "myws", "myrepo", "release.tar.gz")
    ```

References:
    `DELETE /2.0/repositories/{workspace}/{repo_slug}/downloads/{filename}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-downloads/#api-repositories-workspace-repo-slug-downloads-filename-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.downloads.delete`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.delete(client, workspace, repo_slug, filename))
