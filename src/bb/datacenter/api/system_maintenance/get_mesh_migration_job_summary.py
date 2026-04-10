from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_mesh_migration_job_summary_response_400 import GetMeshMigrationJobSummaryResponse400
from ...models.get_mesh_migration_job_summary_response_401 import GetMeshMigrationJobSummaryResponse401
from ...models.get_mesh_migration_job_summary_response_404 import GetMeshMigrationJobSummaryResponse404
from ...models.rest_mesh_migration_summary import RestMeshMigrationSummary
from ...types import Response


def _get_kwargs(
    job_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/migration/mesh/{job_id}/summary".format(
            job_id=quote(str(job_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetMeshMigrationJobSummaryResponse400
    | GetMeshMigrationJobSummaryResponse401
    | GetMeshMigrationJobSummaryResponse404
    | RestMeshMigrationSummary
    | None
):
    if response.status_code == 200:
        response_200 = RestMeshMigrationSummary.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetMeshMigrationJobSummaryResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetMeshMigrationJobSummaryResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetMeshMigrationJobSummaryResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetMeshMigrationJobSummaryResponse400
    | GetMeshMigrationJobSummaryResponse401
    | GetMeshMigrationJobSummaryResponse404
    | RestMeshMigrationSummary
]:
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
) -> Response[
    GetMeshMigrationJobSummaryResponse400
    | GetMeshMigrationJobSummaryResponse401
    | GetMeshMigrationJobSummaryResponse404
    | RestMeshMigrationSummary
]:
    """Get Mesh migration job summary

     Gets the summary, including the queue status and progress, of a Mesh migration job.

    The authenticated user must have **SYS_ADMIN** permission to call this resource.

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMeshMigrationJobSummaryResponse400 | GetMeshMigrationJobSummaryResponse401 | GetMeshMigrationJobSummaryResponse404 | RestMeshMigrationSummary]
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
) -> (
    GetMeshMigrationJobSummaryResponse400
    | GetMeshMigrationJobSummaryResponse401
    | GetMeshMigrationJobSummaryResponse404
    | RestMeshMigrationSummary
    | None
):
    """Get Mesh migration job summary

     Gets the summary, including the queue status and progress, of a Mesh migration job.

    The authenticated user must have **SYS_ADMIN** permission to call this resource.

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMeshMigrationJobSummaryResponse400 | GetMeshMigrationJobSummaryResponse401 | GetMeshMigrationJobSummaryResponse404 | RestMeshMigrationSummary
    """

    return sync_detailed(
        job_id=job_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetMeshMigrationJobSummaryResponse400
    | GetMeshMigrationJobSummaryResponse401
    | GetMeshMigrationJobSummaryResponse404
    | RestMeshMigrationSummary
]:
    """Get Mesh migration job summary

     Gets the summary, including the queue status and progress, of a Mesh migration job.

    The authenticated user must have **SYS_ADMIN** permission to call this resource.

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMeshMigrationJobSummaryResponse400 | GetMeshMigrationJobSummaryResponse401 | GetMeshMigrationJobSummaryResponse404 | RestMeshMigrationSummary]
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
) -> (
    GetMeshMigrationJobSummaryResponse400
    | GetMeshMigrationJobSummaryResponse401
    | GetMeshMigrationJobSummaryResponse404
    | RestMeshMigrationSummary
    | None
):
    """Get Mesh migration job summary

     Gets the summary, including the queue status and progress, of a Mesh migration job.

    The authenticated user must have **SYS_ADMIN** permission to call this resource.

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMeshMigrationJobSummaryResponse400 | GetMeshMigrationJobSummaryResponse401 | GetMeshMigrationJobSummaryResponse404 | RestMeshMigrationSummary
    """

    return (
        await asyncio_detailed(
            job_id=job_id,
            client=client,
        )
    ).parsed
