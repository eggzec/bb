from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_mesh_migration_job_response_400 import GetMeshMigrationJobResponse400
from ...models.get_mesh_migration_job_response_401 import GetMeshMigrationJobResponse401
from ...models.get_mesh_migration_job_response_404 import GetMeshMigrationJobResponse404
from ...types import Response


def _get_kwargs(
    job_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/migration/mesh/{job_id}".format(
            job_id=quote(str(job_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetMeshMigrationJobResponse400 | GetMeshMigrationJobResponse401 | GetMeshMigrationJobResponse404 | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 400:
        response_400 = GetMeshMigrationJobResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetMeshMigrationJobResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetMeshMigrationJobResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetMeshMigrationJobResponse400 | GetMeshMigrationJobResponse401 | GetMeshMigrationJobResponse404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetMeshMigrationJobResponse400 | GetMeshMigrationJobResponse401 | GetMeshMigrationJobResponse404]:
    """Get Mesh migration job details

     Gets the details, including the current status and progress, of the job identified by the given ID.

    The authenticated user must have **SYS_ADMIN** permission to call this resource.

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetMeshMigrationJobResponse400 | GetMeshMigrationJobResponse401 | GetMeshMigrationJobResponse404]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetMeshMigrationJobResponse400 | GetMeshMigrationJobResponse401 | GetMeshMigrationJobResponse404 | None:
    """Get Mesh migration job details

     Gets the details, including the current status and progress, of the job identified by the given ID.

    The authenticated user must have **SYS_ADMIN** permission to call this resource.

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetMeshMigrationJobResponse400 | GetMeshMigrationJobResponse401 | GetMeshMigrationJobResponse404
    """

    return sync_detailed(
        job_id=job_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetMeshMigrationJobResponse400 | GetMeshMigrationJobResponse401 | GetMeshMigrationJobResponse404]:
    """Get Mesh migration job details

     Gets the details, including the current status and progress, of the job identified by the given ID.

    The authenticated user must have **SYS_ADMIN** permission to call this resource.

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetMeshMigrationJobResponse400 | GetMeshMigrationJobResponse401 | GetMeshMigrationJobResponse404]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetMeshMigrationJobResponse400 | GetMeshMigrationJobResponse401 | GetMeshMigrationJobResponse404 | None:
    """Get Mesh migration job details

     Gets the details, including the current status and progress, of the job identified by the given ID.

    The authenticated user must have **SYS_ADMIN** permission to call this resource.

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetMeshMigrationJobResponse400 | GetMeshMigrationJobResponse401 | GetMeshMigrationJobResponse404
    """

    return (
        await asyncio_detailed(
            job_id=job_id,
            client=client,
        )
    ).parsed
