"""Bitbucket Data Center repository SDK wrappers.

Maps to the ``project`` and ``repository`` API tags under
``/api/latest/projects/{projectKey}/repos``.
"""

from __future__ import annotations

from bb.datacenter.api.project import (
    create_repository,
    delete_repository,
    get_repositories,
    get_repository,
    update_repository,
)
from bb.datacenter.api.repository import get_repositories_1
from bb.datacenter.models.rest_repository import RestRepository
from bb.datacenter.sdk._auth_validation import AuthMethod, require_auth
from bb.datacenter.sdk._client import BBDCClient
from bb.datacenter.sdk._pagination import async_paginate
from bb.datacenter.types import UNSET, Unset

__all__ = [
    "list",
    "list_all",
    "get",
    "create",
    "update",
    "delete",
]


@require_auth(AuthMethod.BEARER, AuthMethod.BASIC)
async def list(
    client: BBDCClient,
    project_key: str,
    *,
    limit: int = 25,
) -> list[RestRepository]:
    """List all repositories in a project across all pages.

    Args:
        client: Authenticated :class:`~bb.datacenter.sdk._client.BBDCClient` instance.
        project_key: The project key (e.g. ``"PRJ"``).
        limit: Number of results per page. Defaults to ``25``.

    Returns:
        All repositories in the project across all pages.

    Raises:
        :exc:`~bb.datacenter.sdk._errors.AuthenticationError`: If ``client`` uses an
            unrecognised or unsupported auth method.
        :exc:`~bb.datacenter.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.datacenter import BBDCClient
        from bb.datacenter.sdk import repos

        client = BBDCClient.from_env()
        result = await repos.list(client, project_key="PRJ")
        ```

    References:
        `GET /api/latest/projects/{projectKey}/repos
        <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-project/#api-api-latest-projects-projectkey-repos-get>`_
    """
    return [
        r
        async for r in async_paginate(
            get_repositories.asyncio,
            project_key,
            client=client.auth,
            limit=limit,
        )
        if isinstance(r, RestRepository)
    ]


@require_auth(AuthMethod.BEARER, AuthMethod.BASIC)
async def list_all(
    client: BBDCClient,
    *,
    limit: int = 25,
    name: str | Unset = UNSET,
    permission: str | Unset = UNSET,
) -> list[RestRepository]:  # pyrefly: ignore[unsupported-operation]
    """List all repositories across all accessible projects.

    Args:
        client: Authenticated :class:`~bb.datacenter.sdk._client.BBDCClient` instance.
        limit: Number of results per page. Defaults to ``25``.
        name: Filter repositories by name.
        permission: Restrict results to repositories with this permission level.

    Returns:
        All matching repositories across all pages.

    Raises:
        :exc:`~bb.datacenter.sdk._errors.AuthenticationError`: If ``client`` uses an
            unrecognised or unsupported auth method.
        :exc:`~bb.datacenter.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.datacenter import BBDCClient
        from bb.datacenter.sdk import repos

        client = BBDCClient.from_env()
        result = await repos.list_all(client)
        ```

    References:
        `GET /api/latest/repos
        <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-repository/#api-api-latest-repos-get>`_
    """
    return [
        r
        async for r in async_paginate(
            get_repositories_1.asyncio,
            client=client.auth,
            limit=limit,
            name=name,
            permission=permission,
        )
        if isinstance(r, RestRepository)
    ]


@require_auth(AuthMethod.BEARER, AuthMethod.BASIC)
async def get(client: BBDCClient, project_key: str, repo_slug: str) -> RestRepository | None:
    """Fetch a single repository by slug.

    Args:
        client: Authenticated :class:`~bb.datacenter.sdk._client.BBDCClient` instance.
        project_key: The project key (e.g. ``"PRJ"``).
        repo_slug: Repository slug.

    Returns:
        The :class:`~bb.datacenter.models.rest_repository.RestRepository` object,
        or ``None`` if not found.

    Raises:
        :exc:`~bb.datacenter.sdk._errors.AuthenticationError`: If ``client`` uses an
            unrecognised or unsupported auth method.
        :exc:`~bb.datacenter.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.datacenter import BBDCClient
        from bb.datacenter.sdk import repos

        client = BBDCClient.from_env()
        repo = await repos.get(client, project_key="PRJ", repo_slug="myrepo")
        ```

    References:
        `GET /api/latest/projects/{projectKey}/repos/{repositorySlug}
        <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-project/#api-api-latest-projects-projectkey-repos-repositoryslug-get>`_
    """
    result = await get_repository.asyncio(project_key, repo_slug, client=client.auth)
    return result if isinstance(result, RestRepository) else None


@require_auth(AuthMethod.BEARER, AuthMethod.BASIC)
async def create(
    client: BBDCClient,
    project_key: str,
    *,
    body: RestRepository | Unset = UNSET,
) -> RestRepository | None:
    """Create a new repository in a project.

    Args:
        client: Authenticated :class:`~bb.datacenter.sdk._client.BBDCClient` instance.
        project_key: The project key (e.g. ``"PRJ"``).
        body: Repository configuration.
            Use :class:`~bb.datacenter.models.rest_repository.RestRepository`.

    Returns:
        The created :class:`~bb.datacenter.models.rest_repository.RestRepository`,
        or ``None`` on error.

    Raises:
        :exc:`~bb.datacenter.sdk._errors.AuthenticationError`: If ``client`` uses an
            unrecognised or unsupported auth method.
        :exc:`~bb.datacenter.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.datacenter import BBDCClient
        from bb.datacenter.models.rest_repository import RestRepository
        from bb.datacenter.sdk import repos

        client = BBDCClient.from_env()
        repo = await repos.create(
            client,
            project_key="PRJ",
            body=RestRepository(name="newrepo", scm_id="git"),
        )
        ```

    References:
        `POST /api/latest/projects/{projectKey}/repos
        <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-project/#api-api-latest-projects-projectkey-repos-post>`_
    """
    result = await create_repository.asyncio(project_key, client=client.auth, body=body)
    return result if isinstance(result, RestRepository) else None


@require_auth(AuthMethod.BEARER, AuthMethod.BASIC)
async def update(
    client: BBDCClient,
    project_key: str,
    repo_slug: str,
    *,
    body: RestRepository | Unset = UNSET,
) -> RestRepository | None:
    """Update an existing repository.

    Args:
        client: Authenticated :class:`~bb.datacenter.sdk._client.BBDCClient` instance.
        project_key: The project key (e.g. ``"PRJ"``).
        repo_slug: Repository slug.
        body: Fields to update.
            Use :class:`~bb.datacenter.models.rest_repository.RestRepository`.

    Returns:
        The updated :class:`~bb.datacenter.models.rest_repository.RestRepository`,
        or ``None`` on error.

    Raises:
        :exc:`~bb.datacenter.sdk._errors.AuthenticationError`: If ``client`` uses an
            unrecognised or unsupported auth method.
        :exc:`~bb.datacenter.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.datacenter import BBDCClient
        from bb.datacenter.models.rest_repository import RestRepository
        from bb.datacenter.sdk import repos

        client = BBDCClient.from_env()
        repo = await repos.update(
            client,
            project_key="PRJ",
            repo_slug="myrepo",
            body=RestRepository(description="Updated description"),
        )
        ```

    References:
        `PUT /api/latest/projects/{projectKey}/repos/{repositorySlug}
        <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-project/#api-api-latest-projects-projectkey-repos-repositoryslug-put>`_
    """
    result = await update_repository.asyncio(project_key, repo_slug, client=client.auth, body=body)
    return result if isinstance(result, RestRepository) else None


@require_auth(AuthMethod.BEARER, AuthMethod.BASIC)
async def delete(client: BBDCClient, project_key: str, repo_slug: str) -> None:
    """Delete a repository.

    Args:
        client: Authenticated :class:`~bb.datacenter.sdk._client.BBDCClient` instance.
        project_key: The project key (e.g. ``"PRJ"``).
        repo_slug: Repository slug.

    Returns:
        ``None``.

    Raises:
        :exc:`~bb.datacenter.sdk._errors.AuthenticationError`: If ``client`` uses an
            unrecognised or unsupported auth method.
        :exc:`~bb.datacenter.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.datacenter import BBDCClient
        from bb.datacenter.sdk import repos

        client = BBDCClient.from_env()
        await repos.delete(client, project_key="PRJ", repo_slug="myrepo")
        ```

    References:
        `DELETE /api/latest/projects/{projectKey}/repos/{repositorySlug}
        <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-project/#api-api-latest-projects-projectkey-repos-repositoryslug-delete>`_
    """
    await delete_repository.asyncio(project_key, repo_slug, client=client.auth)
