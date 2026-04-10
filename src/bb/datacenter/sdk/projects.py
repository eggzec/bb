"""Bitbucket Data Center project SDK wrappers.

Maps to the ``project`` API tag under ``/api/latest/projects``.
"""

from __future__ import annotations

from bb.datacenter.api.project import (
    create_project,
    get_project,
    get_projects,
)
from bb.datacenter.models.rest_project import RestProject
from bb.datacenter.sdk._auth_validation import AuthMethod, require_auth
from bb.datacenter.sdk._client import BBDCClient
from bb.datacenter.sdk._pagination import async_paginate
from bb.datacenter.types import UNSET, Unset

__all__ = [
    "list",
    "get",
    "create",
    "update",
    "delete",
]


@require_auth(AuthMethod.BEARER, AuthMethod.BASIC)
async def list(
    client: BBDCClient,
    *,
    name: str | Unset = UNSET,
    permission: str | Unset = UNSET,
    limit: int = 25,
) -> list[RestProject]:
    """List all projects accessible to the authenticated user.

    Args:
        client: Authenticated :class:`~bb.datacenter.sdk._client.BBDCClient` instance.
        name: Filter projects by name.
        permission: Restrict results to projects where the authenticated user
            has this permission (e.g. ``"PROJECT_ADMIN"``).
        limit: Number of results per page. Defaults to ``25``.

    Returns:
        All matching projects across all pages.

    Raises:
        :exc:`~bb.datacenter.sdk._errors.AuthenticationError`: If ``client`` uses an
            unrecognised or unsupported auth method.
        :exc:`~bb.datacenter.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.datacenter import BBDCClient
        from bb.datacenter.sdk import projects

        client = BBDCClient.from_env()
        result = await projects.list(client)
        ```

    References:
        `GET /api/latest/projects
        <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-project/#api-api-latest-projects-get>`_
    """
    return [
        p
        async for p in async_paginate(
            get_projects.asyncio,
            client=client.auth,
            name=name,
            permission=permission,
            limit=limit,
        )
        if isinstance(p, RestProject)
    ]


@require_auth(AuthMethod.BEARER, AuthMethod.BASIC)
async def get(client: BBDCClient, project_key: str) -> RestProject | None:
    """Fetch a single project by key.

    Args:
        client: Authenticated :class:`~bb.datacenter.sdk._client.BBDCClient` instance.
        project_key: The project key (e.g. ``"PRJ"``).

    Returns:
        The :class:`~bb.datacenter.models.rest_project.RestProject`,
        or ``None`` if not found.

    Raises:
        :exc:`~bb.datacenter.sdk._errors.AuthenticationError`: If ``client`` uses an
            unrecognised or unsupported auth method.
        :exc:`~bb.datacenter.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.datacenter import BBDCClient
        from bb.datacenter.sdk import projects

        client = BBDCClient.from_env()
        project = await projects.get(client, project_key="PRJ")
        ```

    References:
        `GET /api/latest/projects/{projectKey}
        <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-project/#api-api-latest-projects-projectkey-get>`_
    """
    result = await get_project.asyncio(project_key, client=client.auth)
    return result if isinstance(result, RestProject) else None


@require_auth(AuthMethod.BEARER, AuthMethod.BASIC)
async def create(
    client: BBDCClient,
    *,
    body: RestProject | Unset = UNSET,
) -> RestProject | None:
    """Create a new project.

    Args:
        client: Authenticated :class:`~bb.datacenter.sdk._client.BBDCClient` instance.
        body: Project configuration.
            Use :class:`~bb.datacenter.models.rest_project.RestProject`.

    Returns:
        The created :class:`~bb.datacenter.models.rest_project.RestProject`,
        or ``None`` on error.

    Raises:
        :exc:`~bb.datacenter.sdk._errors.AuthenticationError`: If ``client`` uses an
            unrecognised or unsupported auth method.
        :exc:`~bb.datacenter.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.datacenter import BBDCClient
        from bb.datacenter.models.rest_project import RestProject
        from bb.datacenter.sdk import projects

        client = BBDCClient.from_env()
        project = await projects.create(
            client,
            body=RestProject(key="MYPRJ", name="My Project"),
        )
        ```

    References:
        `POST /api/latest/projects
        <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-project/#api-api-latest-projects-post>`_
    """
    result = await create_project.asyncio(client=client.auth, body=body)
    return result if isinstance(result, RestProject) else None


@require_auth(AuthMethod.BEARER, AuthMethod.BASIC)
async def update(
    client: BBDCClient,
    project_key: str,
    *,
    body: RestProject | Unset = UNSET,
) -> RestProject | None:
    """Update a project.

    Args:
        client: Authenticated :class:`~bb.datacenter.sdk._client.BBDCClient` instance.
        project_key: The project key (e.g. ``"PRJ"``).
        body: Fields to update.
            Use :class:`~bb.datacenter.models.rest_project.RestProject`.

    Returns:
        The updated :class:`~bb.datacenter.models.rest_project.RestProject`,
        or ``None`` on error.

    Raises:
        :exc:`~bb.datacenter.sdk._errors.AuthenticationError`: If ``client`` uses an
            unrecognised or unsupported auth method.
        :exc:`~bb.datacenter.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.datacenter import BBDCClient
        from bb.datacenter.models.rest_project import RestProject
        from bb.datacenter.sdk import projects

        client = BBDCClient.from_env()
        project = await projects.update(
            client,
            project_key="PRJ",
            body=RestProject(description="Updated description"),
        )
        ```

    References:
        `PUT /api/latest/projects/{projectKey}
        <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-project/#api-api-latest-projects-projectkey-put>`_
    """
    from bb.datacenter.api.project import update_project

    result = await update_project.asyncio(project_key, client=client.auth, body=body)
    return result if isinstance(result, RestProject) else None


@require_auth(AuthMethod.BEARER, AuthMethod.BASIC)
async def delete(client: BBDCClient, project_key: str) -> None:
    """Delete a project.

    Args:
        client: Authenticated :class:`~bb.datacenter.sdk._client.BBDCClient` instance.
        project_key: The project key (e.g. ``"PRJ"``).

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
        from bb.datacenter.sdk import projects

        client = BBDCClient.from_env()
        await projects.delete(client, project_key="PRJ")
        ```

    References:
        `DELETE /api/latest/projects/{projectKey}
        <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-project/#api-api-latest-projects-projectkey-delete>`_
    """
    from bb.datacenter.api.project import delete_project

    await delete_project.asyncio(project_key, client=client.auth)
