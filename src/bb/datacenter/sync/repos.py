"""Bitbucket Data Center repository synchronous SDK wrappers.

Synchronous wrappers around :mod:`bb.datacenter.sdk.repos` using :func:`asyncio.run`.


Maps to the ``project`` and ``repository`` API tags under
``/api/latest/projects/{projectKey}/repos``."""
from __future__ import annotations
import asyncio
from bb.datacenter.models.rest_repository import RestRepository
from bb.datacenter.sdk._client import BBDCClient
from bb.datacenter.types import UNSET, Unset
from bb.datacenter.sdk import repos as _async
__all__ = ['list', 'list_all', 'get', 'create', 'update', 'delete']

def list(client: BBDCClient, project_key: str, *, limit: int=25) -> list[RestRepository]:
    """List all repositories in a project across all pages.

Synchronous wrapper around :func:`~bb.datacenter.sdk.repos.list`.

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
    result = repos.list(client, project_key="PRJ")
    ```

References:
    `GET /api/latest/projects/{projectKey}/repos
    <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-project/#api-api-latest-projects-projectkey-repos-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.datacenter.sdk.repos.list`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.list(client, project_key, limit=limit))

def list_all(client: BBDCClient, *, limit: int=25, name: str | Unset=UNSET, permission: str | Unset=UNSET) -> list[RestRepository]:
    """List all repositories across all accessible projects.

Synchronous wrapper around :func:`~bb.datacenter.sdk.repos.list_all`.

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
    result = repos.list_all(client)
    ```

References:
    `GET /api/latest/repos
    <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-repository/#api-api-latest-repos-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.datacenter.sdk.repos.list_all`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.list_all(client, limit=limit, name=name, permission=permission))

def get(client: BBDCClient, project_key: str, repo_slug: str) -> RestRepository | None:
    """Fetch a single repository by slug.

Synchronous wrapper around :func:`~bb.datacenter.sdk.repos.get`.

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
    repo = repos.get(client, project_key="PRJ", repo_slug="myrepo")
    ```

References:
    `GET /api/latest/projects/{projectKey}/repos/{repositorySlug}
    <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-project/#api-api-latest-projects-projectkey-repos-repositoryslug-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.datacenter.sdk.repos.get`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.get(client, project_key, repo_slug))

def create(client: BBDCClient, project_key: str, *, body: RestRepository | Unset=UNSET) -> RestRepository | None:
    """Create a new repository in a project.

Synchronous wrapper around :func:`~bb.datacenter.sdk.repos.create`.

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
    repo = repos.create(
        client,
        project_key="PRJ",
        body=RestRepository(name="newrepo", scm_id="git"),
    )
    ```

References:
    `POST /api/latest/projects/{projectKey}/repos
    <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-project/#api-api-latest-projects-projectkey-repos-post>`_

Note:
    This synchronous wrapper executes :func:`~bb.datacenter.sdk.repos.create`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.create(client, project_key, body=body))

def update(client: BBDCClient, project_key: str, repo_slug: str, *, body: RestRepository | Unset=UNSET) -> RestRepository | None:
    """Update an existing repository.

Synchronous wrapper around :func:`~bb.datacenter.sdk.repos.update`.

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
    repo = repos.update(
        client,
        project_key="PRJ",
        repo_slug="myrepo",
        body=RestRepository(description="Updated description"),
    )
    ```

References:
    `PUT /api/latest/projects/{projectKey}/repos/{repositorySlug}
    <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-project/#api-api-latest-projects-projectkey-repos-repositoryslug-put>`_

Note:
    This synchronous wrapper executes :func:`~bb.datacenter.sdk.repos.update`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.update(client, project_key, repo_slug, body=body))

def delete(client: BBDCClient, project_key: str, repo_slug: str) -> None:
    """Delete a repository.

Synchronous wrapper around :func:`~bb.datacenter.sdk.repos.delete`.

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
    repos.delete(client, project_key="PRJ", repo_slug="myrepo")
    ```

References:
    `DELETE /api/latest/projects/{projectKey}/repos/{repositorySlug}
    <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-project/#api-api-latest-projects-projectkey-repos-repositoryslug-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.datacenter.sdk.repos.delete`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.delete(client, project_key, repo_slug))
