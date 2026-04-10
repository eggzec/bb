from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_errors import RestErrors
from ...models.rest_indexing_thread_details import RestIndexingThreadDetails
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/indexing/latest/support-info/indexing-thread-snapshot",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RestErrors | list[RestIndexingThreadDetails] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RestIndexingThreadDetails.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 401:
        response_401 = RestErrors.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RestErrors | list[RestIndexingThreadDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[RestErrors | list[RestIndexingThreadDetails]]:
    """Retrieve a snapshot of the indexing thread details.

     Fetches a snapshot of the indexing thread details at the moment the request is processed. Note that
    the result represents the thread's status at a specific point in time, and the state may have
    changed by the time this endpoint responds.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestErrors | list[RestIndexingThreadDetails]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> RestErrors | list[RestIndexingThreadDetails] | None:
    """Retrieve a snapshot of the indexing thread details.

     Fetches a snapshot of the indexing thread details at the moment the request is processed. Note that
    the result represents the thread's status at a specific point in time, and the state may have
    changed by the time this endpoint responds.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestErrors | list[RestIndexingThreadDetails]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[RestErrors | list[RestIndexingThreadDetails]]:
    """Retrieve a snapshot of the indexing thread details.

     Fetches a snapshot of the indexing thread details at the moment the request is processed. Note that
    the result represents the thread's status at a specific point in time, and the state may have
    changed by the time this endpoint responds.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestErrors | list[RestIndexingThreadDetails]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> RestErrors | list[RestIndexingThreadDetails] | None:
    """Retrieve a snapshot of the indexing thread details.

     Fetches a snapshot of the indexing thread details at the moment the request is processed. Note that
    the result represents the thread's status at a specific point in time, and the state may have
    changed by the time this endpoint responds.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestErrors | list[RestIndexingThreadDetails]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
