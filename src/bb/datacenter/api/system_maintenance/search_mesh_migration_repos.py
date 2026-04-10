from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.search_mesh_migration_repos_response_200 import SearchMeshMigrationReposResponse200
from ...models.search_mesh_migration_repos_response_400 import SearchMeshMigrationReposResponse400
from ...models.search_mesh_migration_repos_response_401 import SearchMeshMigrationReposResponse401
from ...models.search_mesh_migration_repos_response_404 import SearchMeshMigrationReposResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    migration_id: str | Unset = UNSET,
    project_key: str | Unset = UNSET,
    name: str | Unset = UNSET,
    state: str | Unset = UNSET,
    remote: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["migrationId"] = migration_id

    params["projectKey"] = project_key

    params["name"] = name

    params["state"] = state

    params["remote"] = remote

    params["start"] = start

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/migration/mesh/repos",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    SearchMeshMigrationReposResponse200
    | SearchMeshMigrationReposResponse400
    | SearchMeshMigrationReposResponse401
    | SearchMeshMigrationReposResponse404
    | None
):
    if response.status_code == 200:
        response_200 = SearchMeshMigrationReposResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = SearchMeshMigrationReposResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = SearchMeshMigrationReposResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = SearchMeshMigrationReposResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    SearchMeshMigrationReposResponse200
    | SearchMeshMigrationReposResponse400
    | SearchMeshMigrationReposResponse401
    | SearchMeshMigrationReposResponse404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    migration_id: str | Unset = UNSET,
    project_key: str | Unset = UNSET,
    name: str | Unset = UNSET,
    state: str | Unset = UNSET,
    remote: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[
    SearchMeshMigrationReposResponse200
    | SearchMeshMigrationReposResponse400
    | SearchMeshMigrationReposResponse401
    | SearchMeshMigrationReposResponse404
]:
    """Find repositories by Mesh migration state

     Searches for repositories in the system matching the specified criteria and enriches their
    MeshMigrationQueueState migration state if a migration is currently in progress.

    The currently active migration can optionally be specified by passing a migrationId, if known. If
    this isn't passed, an attempt is made to locate the active migration and its ID is used.

    If a migration is currently active, only repositories that are a part of the migration are filtered
    and returned. Otherwise, all repositories in the systems are filtered and returned.

    Filtering by state is ignored when no migration is currently in progress. In such a case, results
    are not enriched with their MeshMigrationQueueState migration state.

    The authenticated user must have **SYS_ADMIN** permission to call this resource.

    Args:
        migration_id (str | Unset):
        project_key (str | Unset):
        name (str | Unset):
        state (str | Unset):
        remote (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchMeshMigrationReposResponse200 | SearchMeshMigrationReposResponse400 | SearchMeshMigrationReposResponse401 | SearchMeshMigrationReposResponse404]
    """

    kwargs = _get_kwargs(
        migration_id=migration_id,
        project_key=project_key,
        name=name,
        state=state,
        remote=remote,
        start=start,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    migration_id: str | Unset = UNSET,
    project_key: str | Unset = UNSET,
    name: str | Unset = UNSET,
    state: str | Unset = UNSET,
    remote: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> (
    SearchMeshMigrationReposResponse200
    | SearchMeshMigrationReposResponse400
    | SearchMeshMigrationReposResponse401
    | SearchMeshMigrationReposResponse404
    | None
):
    """Find repositories by Mesh migration state

     Searches for repositories in the system matching the specified criteria and enriches their
    MeshMigrationQueueState migration state if a migration is currently in progress.

    The currently active migration can optionally be specified by passing a migrationId, if known. If
    this isn't passed, an attempt is made to locate the active migration and its ID is used.

    If a migration is currently active, only repositories that are a part of the migration are filtered
    and returned. Otherwise, all repositories in the systems are filtered and returned.

    Filtering by state is ignored when no migration is currently in progress. In such a case, results
    are not enriched with their MeshMigrationQueueState migration state.

    The authenticated user must have **SYS_ADMIN** permission to call this resource.

    Args:
        migration_id (str | Unset):
        project_key (str | Unset):
        name (str | Unset):
        state (str | Unset):
        remote (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchMeshMigrationReposResponse200 | SearchMeshMigrationReposResponse400 | SearchMeshMigrationReposResponse401 | SearchMeshMigrationReposResponse404
    """

    return sync_detailed(
        client=client,
        migration_id=migration_id,
        project_key=project_key,
        name=name,
        state=state,
        remote=remote,
        start=start,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    migration_id: str | Unset = UNSET,
    project_key: str | Unset = UNSET,
    name: str | Unset = UNSET,
    state: str | Unset = UNSET,
    remote: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[
    SearchMeshMigrationReposResponse200
    | SearchMeshMigrationReposResponse400
    | SearchMeshMigrationReposResponse401
    | SearchMeshMigrationReposResponse404
]:
    """Find repositories by Mesh migration state

     Searches for repositories in the system matching the specified criteria and enriches their
    MeshMigrationQueueState migration state if a migration is currently in progress.

    The currently active migration can optionally be specified by passing a migrationId, if known. If
    this isn't passed, an attempt is made to locate the active migration and its ID is used.

    If a migration is currently active, only repositories that are a part of the migration are filtered
    and returned. Otherwise, all repositories in the systems are filtered and returned.

    Filtering by state is ignored when no migration is currently in progress. In such a case, results
    are not enriched with their MeshMigrationQueueState migration state.

    The authenticated user must have **SYS_ADMIN** permission to call this resource.

    Args:
        migration_id (str | Unset):
        project_key (str | Unset):
        name (str | Unset):
        state (str | Unset):
        remote (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchMeshMigrationReposResponse200 | SearchMeshMigrationReposResponse400 | SearchMeshMigrationReposResponse401 | SearchMeshMigrationReposResponse404]
    """

    kwargs = _get_kwargs(
        migration_id=migration_id,
        project_key=project_key,
        name=name,
        state=state,
        remote=remote,
        start=start,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    migration_id: str | Unset = UNSET,
    project_key: str | Unset = UNSET,
    name: str | Unset = UNSET,
    state: str | Unset = UNSET,
    remote: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> (
    SearchMeshMigrationReposResponse200
    | SearchMeshMigrationReposResponse400
    | SearchMeshMigrationReposResponse401
    | SearchMeshMigrationReposResponse404
    | None
):
    """Find repositories by Mesh migration state

     Searches for repositories in the system matching the specified criteria and enriches their
    MeshMigrationQueueState migration state if a migration is currently in progress.

    The currently active migration can optionally be specified by passing a migrationId, if known. If
    this isn't passed, an attempt is made to locate the active migration and its ID is used.

    If a migration is currently active, only repositories that are a part of the migration are filtered
    and returned. Otherwise, all repositories in the systems are filtered and returned.

    Filtering by state is ignored when no migration is currently in progress. In such a case, results
    are not enriched with their MeshMigrationQueueState migration state.

    The authenticated user must have **SYS_ADMIN** permission to call this resource.

    Args:
        migration_id (str | Unset):
        project_key (str | Unset):
        name (str | Unset):
        state (str | Unset):
        remote (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchMeshMigrationReposResponse200 | SearchMeshMigrationReposResponse400 | SearchMeshMigrationReposResponse401 | SearchMeshMigrationReposResponse404
    """

    return (
        await asyncio_detailed(
            client=client,
            migration_id=migration_id,
            project_key=project_key,
            name=name,
            state=state,
            remote=remote,
            start=start,
            limit=limit,
        )
    ).parsed
