from __future__ import annotations

from bb.cloud.api.commit_statuses import (
    get_repositories_workspace_repo_slug_commit_commit_statuses,
    get_repositories_workspace_repo_slug_commit_commit_statuses_build_key,
    post_repositories_workspace_repo_slug_commit_commit_statuses_build,
    put_repositories_workspace_repo_slug_commit_commit_statuses_build_key,
)
from bb.cloud.models.commitstatus import Commitstatus
from bb.cloud.models.error import Error
from bb.cloud.sdk._auth_validation import AuthMethod, require_auth
from bb.cloud.sdk._client import BBClient
from bb.cloud.sdk._pagination import async_paginate
from bb.cloud.types import UNSET, Unset

__all__ = ["list", "get", "create", "update"]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def list(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    commit: str,
    *,
    pagelen: int = 25,
) -> list[Commitstatus] | Error:
    """List all commit statuses for a given commit.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        repo_slug: Repository slug or UUID.
        commit: Full SHA1 of the commit.
        pagelen: Number of results per page. Defaults to ``25``.

    Returns:
        List of :class:`~bb.cloud.models.commitstatus.Commitstatus` objects.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import commit_statuses

        client = BBClient.from_env()
        statuses = await commit_statuses.list(
            client, workspace="myws", repo_slug="myrepo", commit="abc123"
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/commit/{commit}/statuses
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-commit-statuses/#api-repositories-workspace-repo-slug-commit-commit-statuses-get>`_
    """
    result = await async_paginate(
        get_repositories_workspace_repo_slug_commit_commit_statuses.asyncio,
        workspace,
        repo_slug,
        commit,
        client=client.auth,
        pagelen=pagelen,
    )

    if isinstance(result, Error):
        return result

    return [item for item in result if isinstance(item, Commitstatus)]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get(client: BBClient, workspace: str, repo_slug: str, commit: str, key: str) -> Commitstatus | Error | None:
    """Retrieve a single commit status by build key.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        repo_slug: Repository slug or UUID.
        commit: Full SHA1 of the commit.
        key: Unique key identifying the build status.

    Returns:
        A :class:`~bb.cloud.models.commitstatus.Commitstatus` object, or ``None`` if not found.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import commit_statuses

        client = BBClient.from_env()
        status = await commit_statuses.get(
            client, workspace="myws", repo_slug="myrepo", commit="abc123", key="my-build"
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/commit/{commit}/statuses/build/{key}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-commit-statuses/#api-repositories-workspace-repo-slug-commit-commit-statuses-build-key-get>`_
    """
    result = await get_repositories_workspace_repo_slug_commit_commit_statuses_build_key.asyncio(
        workspace, repo_slug, commit, key, client=client.auth
    )
    if isinstance(result, (Commitstatus, Error)):
        return result
    return None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def create(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    commit: str,
    *,
    body: Commitstatus | Unset = UNSET,
) -> Commitstatus | Error | None:
    """Create a commit status (build result) for a commit.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        repo_slug: Repository slug or UUID.
        commit: Full SHA1 of the commit.
        body: Commit status payload. Defaults to :data:`~bb.cloud.types.UNSET`.

    Returns:
        The created :class:`~bb.cloud.models.commitstatus.Commitstatus`, or ``None`` on error.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import commit_statuses
        from bb.cloud.models.commitstatus import Commitstatus

        client = BBClient.from_env()
        status = await commit_statuses.create(
            client, workspace="myws", repo_slug="myrepo", commit="abc123", body=Commitstatus(...)
        )
        ```

    References:
        `POST /2.0/repositories/{workspace}/{repo_slug}/commit/{commit}/statuses/build
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-commit-statuses/#api-repositories-workspace-repo-slug-commit-commit-statuses-build-post>`_
    """
    result = await post_repositories_workspace_repo_slug_commit_commit_statuses_build.asyncio(
        workspace, repo_slug, commit, client=client.auth, body=body
    )
    if isinstance(result, (Commitstatus, Error)):
        return result
    return None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def update(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    commit: str,
    key: str,
    *,
    body: Commitstatus | Unset = UNSET,
) -> Commitstatus | Error | None:
    """Update an existing commit status by build key.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        repo_slug: Repository slug or UUID.
        commit: Full SHA1 of the commit.
        key: Unique key identifying the build status to update.
        body: Updated commit status payload. Defaults to :data:`~bb.cloud.types.UNSET`.

    Returns:
        The updated :class:`~bb.cloud.models.commitstatus.Commitstatus`, or ``None`` on error.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import commit_statuses
        from bb.cloud.models.commitstatus import Commitstatus

        client = BBClient.from_env()
        status = await commit_statuses.update(
            client,
            workspace="myws",
            repo_slug="myrepo",
            commit="abc123",
            key="my-build",
            body=Commitstatus(...),
        )
        ```

    References:
        `PUT /2.0/repositories/{workspace}/{repo_slug}/commit/{commit}/statuses/build/{key}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-commit-statuses/#api-repositories-workspace-repo-slug-commit-commit-statuses-build-key-put>`_
    """
    result = await put_repositories_workspace_repo_slug_commit_commit_statuses_build_key.asyncio(
        workspace, repo_slug, commit, key, client=client.auth, body=body
    )
    if isinstance(result, (Commitstatus, Error)):
        return result
    return None
