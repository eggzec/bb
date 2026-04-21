from __future__ import annotations

from bb.cloud.api.source import (
    get_repositories_workspace_repo_slug_filehistory_commit_path,
    get_repositories_workspace_repo_slug_src,
    get_repositories_workspace_repo_slug_src_commit_path,
    post_repositories_workspace_repo_slug_src,
)
from bb.cloud.models.error import Error
from bb.cloud.sdk._auth_validation import AuthMethod, require_auth
from bb.cloud.sdk._client import BBClient
from bb.cloud.types import UNSET, Unset

__all__ = ["get", "root", "history", "upload"]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    commit: str,
    path: str,
) -> object | Error | None:
    """Return the contents of a file at a given commit and path.

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
        contents = await source.get(client, "myws", "myrepo", "main", "README.md")
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/src/{commit}/{path}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-source/#api-repositories-workspace-repo-slug-src-commit-path-get>`_
    """
    return await get_repositories_workspace_repo_slug_src_commit_path.asyncio(
        workspace, repo_slug, commit, path, client=client.auth
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def root(client: BBClient, workspace: str, repo_slug: str) -> object | Error | None:
    """Return the root directory listing of the default branch.

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
        tree = await source.root(client, "myws", "myrepo")
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/src
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-source/#api-repositories-workspace-repo-slug-src-get>`_
    """
    return await get_repositories_workspace_repo_slug_src.asyncio(workspace, repo_slug, client=client.auth)


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def history(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    commit: str,
    path: str,
) -> object | Error | None:
    """Return the file history — commits that touched a given path.

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
        log = await source.history(client, "myws", "myrepo", "main", "src/main.py")
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/filehistory/{commit}/{path}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-source/#api-repositories-workspace-repo-slug-filehistory-commit-path-get>`_
    """
    return await get_repositories_workspace_repo_slug_filehistory_commit_path.asyncio(
        workspace, repo_slug, commit, path, client=client.auth
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def upload(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: Unset = UNSET,
) -> object | Error | None:
    """Upload files to a repository via the source endpoint.

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
        result = await source.upload(client, "myws", "myrepo", body=...)
        ```

    References:
        `POST /2.0/repositories/{workspace}/{repo_slug}/src
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-source/#api-repositories-workspace-repo-slug-src-post>`_
    """
    return await post_repositories_workspace_repo_slug_src.asyncio(workspace, repo_slug, client=client.auth, body=body)
