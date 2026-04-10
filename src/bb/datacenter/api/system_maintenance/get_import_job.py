from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_import_job_response_401 import GetImportJobResponse401
from ...models.get_import_job_response_404 import GetImportJobResponse404
from ...models.rest_job import RestJob
from ...types import Response


def _get_kwargs(
    job_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/migration/imports/{job_id}".format(
            job_id=quote(str(job_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetImportJobResponse401 | GetImportJobResponse404 | RestJob | None:
    if response.status_code == 200:
        response_200 = RestJob.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetImportJobResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetImportJobResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetImportJobResponse401 | GetImportJobResponse404 | RestJob]:
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
) -> Response[GetImportJobResponse401 | GetImportJobResponse404 | RestJob]:
    """Get import job status

     Gets the details, including the current status and progress, of the import job identified by the
    given ID.

    The authenticated user must have **ADMIN** permission or higher to call this resource.

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetImportJobResponse401 | GetImportJobResponse404 | RestJob]
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
) -> GetImportJobResponse401 | GetImportJobResponse404 | RestJob | None:
    """Get import job status

     Gets the details, including the current status and progress, of the import job identified by the
    given ID.

    The authenticated user must have **ADMIN** permission or higher to call this resource.

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetImportJobResponse401 | GetImportJobResponse404 | RestJob
    """

    return sync_detailed(
        job_id=job_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetImportJobResponse401 | GetImportJobResponse404 | RestJob]:
    """Get import job status

     Gets the details, including the current status and progress, of the import job identified by the
    given ID.

    The authenticated user must have **ADMIN** permission or higher to call this resource.

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetImportJobResponse401 | GetImportJobResponse404 | RestJob]
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
) -> GetImportJobResponse401 | GetImportJobResponse404 | RestJob | None:
    """Get import job status

     Gets the details, including the current status and progress, of the import job identified by the
    given ID.

    The authenticated user must have **ADMIN** permission or higher to call this resource.

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetImportJobResponse401 | GetImportJobResponse404 | RestJob
    """

    return (
        await asyncio_detailed(
            job_id=job_id,
            client=client,
        )
    ).parsed
