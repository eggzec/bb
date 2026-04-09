from __future__ import annotations

from typing import Any

from bb.cloud.api.downloads import (
    delete_repositories_workspace_repo_slug_downloads_filename,
    get_repositories_workspace_repo_slug_downloads,
    get_repositories_workspace_repo_slug_downloads_filename,
    post_repositories_workspace_repo_slug_downloads,
)
from bb.cloud.sdk._auth_validation import AuthMethod, require_auth
from bb.cloud.sdk._client import BBClient
from bb.cloud.sdk._pagination import async_paginate
from bb.cloud.types import UNSET, Unset

__all__ = ["list", "get", "upload", "delete"]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def list(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    pagelen: int = 25,
) -> list[Any]:
    """Return all download artifacts for a repository.

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
        artifacts = await downloads.list(client, "myws", "myrepo")
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/downloads
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-downloads/#api-repositories-workspace-repo-slug-downloads-get>`_
    """
    return [
        d
        async for d in async_paginate(
            get_repositories_workspace_repo_slug_downloads.asyncio,
            workspace,
            repo_slug,
            client=client.auth,
            pagelen=pagelen,
        )
    ]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get(client: BBClient, workspace: str, repo_slug: str, filename: str) -> Any:
    """Return a single download artifact by filename, or ``None`` if not found.

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
        artifact = await downloads.get(client, "myws", "myrepo", "release.tar.gz")
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/downloads/{filename}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-downloads/#api-repositories-workspace-repo-slug-downloads-filename-get>`_
    """
    return await get_repositories_workspace_repo_slug_downloads_filename.asyncio(
        workspace, repo_slug, filename, client=client.auth
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def upload(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: Unset = UNSET,
) -> Any:
    """Upload a file as a download artifact for a repository.

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
        result = await downloads.upload(client, "myws", "myrepo", body=...)
        ```

    References:
        `POST /2.0/repositories/{workspace}/{repo_slug}/downloads
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-downloads/#api-repositories-workspace-repo-slug-downloads-post>`_
    """
    return await post_repositories_workspace_repo_slug_downloads.asyncio(
        workspace, repo_slug, client=client.auth, body=body
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def delete(client: BBClient, workspace: str, repo_slug: str, filename: str) -> None:
    """Delete a download artifact by filename.

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
        await downloads.delete(client, "myws", "myrepo", "release.tar.gz")
        ```

    References:
        `DELETE /2.0/repositories/{workspace}/{repo_slug}/downloads/{filename}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-downloads/#api-repositories-workspace-repo-slug-downloads-filename-delete>`_
    """
    await delete_repositories_workspace_repo_slug_downloads_filename.asyncio(
        workspace, repo_slug, filename, client=client.auth
    )
