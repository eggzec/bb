from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cancel_import_job_response_401 import CancelImportJobResponse401
from ...models.cancel_import_job_response_404 import CancelImportJobResponse404
from ...models.cancel_import_job_response_409 import CancelImportJobResponse409
from ...types import Response


def _get_kwargs(
    job_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/latest/migration/imports/{job_id}/cancel".format(
            job_id=quote(str(job_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CancelImportJobResponse401 | CancelImportJobResponse404 | CancelImportJobResponse409 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = CancelImportJobResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = CancelImportJobResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = CancelImportJobResponse409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CancelImportJobResponse401 | CancelImportJobResponse404 | CancelImportJobResponse409]:
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
) -> Response[Any | CancelImportJobResponse401 | CancelImportJobResponse404 | CancelImportJobResponse409]:
    """Cancel import job

     Requests the cancellation of an import job.

    The request to cancel a job will be processed successfully if the job is actually still running. If
    it has already finished (successfully or with errors) or if it has already been canceled before,
    then an error will be returned.

    Note that import jobs are not canceled as instantaneously as export jobs. Rather, once the request
    has been accepted, there are a number of checkpoints at which the job will actually apply it and
    stop. This is to keep the system in a reasonably consistent state:

    - After the current fork hierarchy has been imported and verified.
    - Before the next repository is imported.
    - Before the next pull request is imported.

    A client should always actively query the job status to confirm that a job has been successfully
    canceled.

    The authenticated user must have **ADMIN** permission or higher to call this resource.

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CancelImportJobResponse401 | CancelImportJobResponse404 | CancelImportJobResponse409]
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
) -> Any | CancelImportJobResponse401 | CancelImportJobResponse404 | CancelImportJobResponse409 | None:
    """Cancel import job

     Requests the cancellation of an import job.

    The request to cancel a job will be processed successfully if the job is actually still running. If
    it has already finished (successfully or with errors) or if it has already been canceled before,
    then an error will be returned.

    Note that import jobs are not canceled as instantaneously as export jobs. Rather, once the request
    has been accepted, there are a number of checkpoints at which the job will actually apply it and
    stop. This is to keep the system in a reasonably consistent state:

    - After the current fork hierarchy has been imported and verified.
    - Before the next repository is imported.
    - Before the next pull request is imported.

    A client should always actively query the job status to confirm that a job has been successfully
    canceled.

    The authenticated user must have **ADMIN** permission or higher to call this resource.

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CancelImportJobResponse401 | CancelImportJobResponse404 | CancelImportJobResponse409
    """

    return sync_detailed(
        job_id=job_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | CancelImportJobResponse401 | CancelImportJobResponse404 | CancelImportJobResponse409]:
    """Cancel import job

     Requests the cancellation of an import job.

    The request to cancel a job will be processed successfully if the job is actually still running. If
    it has already finished (successfully or with errors) or if it has already been canceled before,
    then an error will be returned.

    Note that import jobs are not canceled as instantaneously as export jobs. Rather, once the request
    has been accepted, there are a number of checkpoints at which the job will actually apply it and
    stop. This is to keep the system in a reasonably consistent state:

    - After the current fork hierarchy has been imported and verified.
    - Before the next repository is imported.
    - Before the next pull request is imported.

    A client should always actively query the job status to confirm that a job has been successfully
    canceled.

    The authenticated user must have **ADMIN** permission or higher to call this resource.

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CancelImportJobResponse401 | CancelImportJobResponse404 | CancelImportJobResponse409]
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
) -> Any | CancelImportJobResponse401 | CancelImportJobResponse404 | CancelImportJobResponse409 | None:
    """Cancel import job

     Requests the cancellation of an import job.

    The request to cancel a job will be processed successfully if the job is actually still running. If
    it has already finished (successfully or with errors) or if it has already been canceled before,
    then an error will be returned.

    Note that import jobs are not canceled as instantaneously as export jobs. Rather, once the request
    has been accepted, there are a number of checkpoints at which the job will actually apply it and
    stop. This is to keep the system in a reasonably consistent state:

    - After the current fork hierarchy has been imported and verified.
    - Before the next repository is imported.
    - Before the next pull request is imported.

    A client should always actively query the job status to confirm that a job has been successfully
    canceled.

    The authenticated user must have **ADMIN** permission or higher to call this resource.

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CancelImportJobResponse401 | CancelImportJobResponse404 | CancelImportJobResponse409
    """

    return (
        await asyncio_detailed(
            job_id=job_id,
            client=client,
        )
    ).parsed
