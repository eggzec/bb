"""Bitbucket Data Center project synchronous SDK wrappers.

Synchronous wrappers around :mod:`bb.datacenter.sdk.projects` using :func:`asyncio.run`.


Maps to the ``project`` API tag under ``/api/latest/projects``."""
from __future__ import annotations
import asyncio
from bb.datacenter.models.rest_project import RestProject
from bb.datacenter.sdk._client import BBDCClient
from bb.datacenter.types import UNSET, Unset
from bb.datacenter.sdk import projects as _async
__all__ = ['list', 'get', 'create', 'update', 'delete']

def list(client: BBDCClient, *, name: str | Unset=UNSET, permission: str | Unset=UNSET, limit: int=25) -> list[RestProject]:
    """List all projects accessible to the authenticated user.

Synchronous wrapper around :func:`~bb.datacenter.sdk.projects.list`.

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
    result = projects.list(client)
    ```

References:
    `GET /api/latest/projects
    <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-project/#api-api-latest-projects-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.datacenter.sdk.projects.list`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.list(client, name=name, permission=permission, limit=limit))

def get(client: BBDCClient, project_key: str) -> RestProject | None:
    """Fetch a single project by key.

Synchronous wrapper around :func:`~bb.datacenter.sdk.projects.get`.

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
    project = projects.get(client, project_key="PRJ")
    ```

References:
    `GET /api/latest/projects/{projectKey}
    <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-project/#api-api-latest-projects-projectkey-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.datacenter.sdk.projects.get`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.get(client, project_key))

def create(client: BBDCClient, *, body: RestProject | Unset=UNSET) -> RestProject | None:
    """Create a new project.

Synchronous wrapper around :func:`~bb.datacenter.sdk.projects.create`.

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
    project = projects.create(
        client,
        body=RestProject(key="MYPRJ", name="My Project"),
    )
    ```

References:
    `POST /api/latest/projects
    <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-project/#api-api-latest-projects-post>`_

Note:
    This synchronous wrapper executes :func:`~bb.datacenter.sdk.projects.create`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.create(client, body=body))

def update(client: BBDCClient, project_key: str, *, body: RestProject | Unset=UNSET) -> RestProject | None:
    """Update a project.

Synchronous wrapper around :func:`~bb.datacenter.sdk.projects.update`.

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
    project = projects.update(
        client,
        project_key="PRJ",
        body=RestProject(description="Updated description"),
    )
    ```

References:
    `PUT /api/latest/projects/{projectKey}
    <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-project/#api-api-latest-projects-projectkey-put>`_

Note:
    This synchronous wrapper executes :func:`~bb.datacenter.sdk.projects.update`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.update(client, project_key, body=body))

def delete(client: BBDCClient, project_key: str) -> None:
    """Delete a project.

Synchronous wrapper around :func:`~bb.datacenter.sdk.projects.delete`.

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
    projects.delete(client, project_key="PRJ")
    ```

References:
    `DELETE /api/latest/projects/{projectKey}
    <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-project/#api-api-latest-projects-projectkey-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.datacenter.sdk.projects.delete`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.delete(client, project_key))
