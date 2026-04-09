from __future__ import annotations

from bb.cloud.api.branch_restrictions import (
    delete_repositories_workspace_repo_slug_branch_restrictions_id,
    get_repositories_workspace_repo_slug_branch_restrictions,
    get_repositories_workspace_repo_slug_branch_restrictions_id,
    post_repositories_workspace_repo_slug_branch_restrictions,
    put_repositories_workspace_repo_slug_branch_restrictions_id,
)
from bb.cloud.models.branchrestriction import Branchrestriction
from bb.cloud.sdk._auth_validation import AuthMethod, require_auth
from bb.cloud.sdk._client import BBClient
from bb.cloud.sdk._pagination import async_paginate
from bb.cloud.types import UNSET, Unset

__all__ = ["list", "get", "create", "update", "delete"]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def list(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    pagelen: int = 25,
) -> list[Branchrestriction]:
    """List all branch restrictions for a repository.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        repo_slug: Repository slug or UUID.
        pagelen: Number of results per page. Defaults to ``25``.

    Returns:
        List of :class:`~bb.cloud.models.branchrestriction.Branchrestriction` objects.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import branch_restrictions

        client = BBClient.from_env()
        result = await branch_restrictions.list(client, workspace="myws", repo_slug="myrepo")
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/branch-restrictions
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-branch-restrictions/#api-repositories-workspace-repo-slug-branch-restrictions-get>`_
    """
    return [
        r
        async for r in async_paginate(
            get_repositories_workspace_repo_slug_branch_restrictions.asyncio,
            workspace,
            repo_slug,
            client=client.auth,
            pagelen=pagelen,
        )
        if isinstance(r, Branchrestriction)
    ]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get(client: BBClient, workspace: str, repo_slug: str, id: int) -> Branchrestriction | None:
    """Retrieve a single branch restriction by ID.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        repo_slug: Repository slug or UUID.
        id: Numeric ID of the branch restriction.

    Returns:
        A :class:`~bb.cloud.models.branchrestriction.Branchrestriction` object, or ``None`` if not found.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import branch_restrictions

        client = BBClient.from_env()
        restriction = await branch_restrictions.get(client, workspace="myws", repo_slug="myrepo", id=1)
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/branch-restrictions/{id}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-branch-restrictions/#api-repositories-workspace-repo-slug-branch-restrictions-id-get>`_
    """
    result = await get_repositories_workspace_repo_slug_branch_restrictions_id.asyncio(
        workspace, repo_slug, id, client=client.auth
    )
    return result if isinstance(result, Branchrestriction) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def create(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: Branchrestriction | Unset = UNSET,
) -> Branchrestriction | None:
    """Create a branch restriction on a repository.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        repo_slug: Repository slug or UUID.
        body: Branch restriction payload. Defaults to :data:`~bb.cloud.types.UNSET`.

    Returns:
        The created :class:`~bb.cloud.models.branchrestriction.Branchrestriction`, or ``None`` on error.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import branch_restrictions
        from bb.cloud.models.branchrestriction import Branchrestriction

        client = BBClient.from_env()
        restriction = await branch_restrictions.create(
            client, workspace="myws", repo_slug="myrepo", body=Branchrestriction(...)
        )
        ```

    References:
        `POST /2.0/repositories/{workspace}/{repo_slug}/branch-restrictions
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-branch-restrictions/#api-repositories-workspace-repo-slug-branch-restrictions-post>`_
    """
    result = await post_repositories_workspace_repo_slug_branch_restrictions.asyncio(
        workspace, repo_slug, client=client.auth, body=body
    )
    return result if isinstance(result, Branchrestriction) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def update(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    id: int,
    *,
    body: Branchrestriction | Unset = UNSET,
) -> Branchrestriction | None:
    """Update a branch restriction on a repository.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        repo_slug: Repository slug or UUID.
        id: Numeric ID of the branch restriction to update.
        body: Updated branch restriction payload. Defaults to :data:`~bb.cloud.types.UNSET`.

    Returns:
        The updated :class:`~bb.cloud.models.branchrestriction.Branchrestriction`, or ``None`` on error.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import branch_restrictions
        from bb.cloud.models.branchrestriction import Branchrestriction

        client = BBClient.from_env()
        restriction = await branch_restrictions.update(
            client, workspace="myws", repo_slug="myrepo", id=1, body=Branchrestriction(...)
        )
        ```

    References:
        `PUT /2.0/repositories/{workspace}/{repo_slug}/branch-restrictions/{id}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-branch-restrictions/#api-repositories-workspace-repo-slug-branch-restrictions-id-put>`_
    """
    result = await put_repositories_workspace_repo_slug_branch_restrictions_id.asyncio(
        workspace, repo_slug, id, client=client.auth, body=body
    )
    return result if isinstance(result, Branchrestriction) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def delete(client: BBClient, workspace: str, repo_slug: str, id: int) -> None:
    """Delete a branch restriction from a repository.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        repo_slug: Repository slug or UUID.
        id: Numeric ID of the branch restriction to delete.

    Returns:
        None.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import branch_restrictions

        client = BBClient.from_env()
        await branch_restrictions.delete(client, workspace="myws", repo_slug="myrepo", id=1)
        ```

    References:
        `DELETE /2.0/repositories/{workspace}/{repo_slug}/branch-restrictions/{id}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-branch-restrictions/#api-repositories-workspace-repo-slug-branch-restrictions-id-delete>`_
    """
    await delete_repositories_workspace_repo_slug_branch_restrictions_id.asyncio(
        workspace, repo_slug, id, client=client.auth
    )
