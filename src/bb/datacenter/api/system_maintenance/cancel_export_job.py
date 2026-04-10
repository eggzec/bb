from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cancel_export_job_response_401 import CancelExportJobResponse401
from ...models.cancel_export_job_response_404 import CancelExportJobResponse404
from ...models.cancel_export_job_response_409 import CancelExportJobResponse409
from ...types import Response


def _get_kwargs(
    job_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/latest/migration/exports/{job_id}/cancel".format(
            job_id=quote(str(job_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CancelExportJobResponse401 | CancelExportJobResponse404 | CancelExportJobResponse409 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = CancelExportJobResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = CancelExportJobResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = CancelExportJobResponse409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CancelExportJobResponse401 | CancelExportJobResponse404 | CancelExportJobResponse409]:
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
) -> Response[Any | CancelExportJobResponse401 | CancelExportJobResponse404 | CancelExportJobResponse409]:
    """Cancel export job

     Requests the cancellation of an export job.

    The request to cancel a job will be processed successfully if the job is actually still running. If
    it has already finished (successfully or with errors) or if it has already been canceled before,
    then an error will be returned.

    There might be a small delay between accepting the request and actually cancelling the job. In most
    cases, the delay will be close to instantaneously. In the unlikely case of communication issues
    across a cluster, it can however take a few seconds to cancel a job.

    A client should always actively query the job status to confirm that a job has been successfully
    canceled.

    The authenticated user must have **ADMIN** permission or higher to call this resource.

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CancelExportJobResponse401 | CancelExportJobResponse404 | CancelExportJobResponse409]
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
) -> Any | CancelExportJobResponse401 | CancelExportJobResponse404 | CancelExportJobResponse409 | None:
    """Cancel export job

     Requests the cancellation of an export job.

    The request to cancel a job will be processed successfully if the job is actually still running. If
    it has already finished (successfully or with errors) or if it has already been canceled before,
    then an error will be returned.

    There might be a small delay between accepting the request and actually cancelling the job. In most
    cases, the delay will be close to instantaneously. In the unlikely case of communication issues
    across a cluster, it can however take a few seconds to cancel a job.

    A client should always actively query the job status to confirm that a job has been successfully
    canceled.

    The authenticated user must have **ADMIN** permission or higher to call this resource.

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CancelExportJobResponse401 | CancelExportJobResponse404 | CancelExportJobResponse409
    """

    return sync_detailed(
        job_id=job_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | CancelExportJobResponse401 | CancelExportJobResponse404 | CancelExportJobResponse409]:
    """Cancel export job

     Requests the cancellation of an export job.

    The request to cancel a job will be processed successfully if the job is actually still running. If
    it has already finished (successfully or with errors) or if it has already been canceled before,
    then an error will be returned.

    There might be a small delay between accepting the request and actually cancelling the job. In most
    cases, the delay will be close to instantaneously. In the unlikely case of communication issues
    across a cluster, it can however take a few seconds to cancel a job.

    A client should always actively query the job status to confirm that a job has been successfully
    canceled.

    The authenticated user must have **ADMIN** permission or higher to call this resource.

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CancelExportJobResponse401 | CancelExportJobResponse404 | CancelExportJobResponse409]
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
) -> Any | CancelExportJobResponse401 | CancelExportJobResponse404 | CancelExportJobResponse409 | None:
    """Cancel export job

     Requests the cancellation of an export job.

    The request to cancel a job will be processed successfully if the job is actually still running. If
    it has already finished (successfully or with errors) or if it has already been canceled before,
    then an error will be returned.

    There might be a small delay between accepting the request and actually cancelling the job. In most
    cases, the delay will be close to instantaneously. In the unlikely case of communication issues
    across a cluster, it can however take a few seconds to cancel a job.

    A client should always actively query the job status to confirm that a job has been successfully
    canceled.

    The authenticated user must have **ADMIN** permission or higher to call this resource.

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CancelExportJobResponse401 | CancelExportJobResponse404 | CancelExportJobResponse409
    """

    return (
        await asyncio_detailed(
            job_id=job_id,
            client=client,
        )
    ).parsed
