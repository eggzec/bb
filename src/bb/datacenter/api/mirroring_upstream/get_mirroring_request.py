from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_mirroring_request_response_409 import GetMirroringRequestResponse409
from ...models.rest_mirroring_request import RestMirroringRequest
from ...types import Response


def _get_kwargs(
    mirroring_request_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/mirroring/latest/requests/{mirroring_request_id}".format(
            mirroring_request_id=quote(str(mirroring_request_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetMirroringRequestResponse409 | RestMirroringRequest | None:
    if response.status_code == 200:
        response_200 = RestMirroringRequest.from_dict(response.json())

        return response_200

    if response.status_code == 409:
        response_409 = GetMirroringRequestResponse409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetMirroringRequestResponse409 | RestMirroringRequest]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    mirroring_request_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetMirroringRequestResponse409 | RestMirroringRequest]:
    """Get a mirroring request

     Retrieves a mirroring request

    Args:
        mirroring_request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMirroringRequestResponse409 | RestMirroringRequest]
    """

    kwargs = _get_kwargs(
        mirroring_request_id=mirroring_request_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    mirroring_request_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetMirroringRequestResponse409 | RestMirroringRequest | None:
    """Get a mirroring request

     Retrieves a mirroring request

    Args:
        mirroring_request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMirroringRequestResponse409 | RestMirroringRequest
    """

    return sync_detailed(
        mirroring_request_id=mirroring_request_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    mirroring_request_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetMirroringRequestResponse409 | RestMirroringRequest]:
    """Get a mirroring request

     Retrieves a mirroring request

    Args:
        mirroring_request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMirroringRequestResponse409 | RestMirroringRequest]
    """

    kwargs = _get_kwargs(
        mirroring_request_id=mirroring_request_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    mirroring_request_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetMirroringRequestResponse409 | RestMirroringRequest | None:
    """Get a mirroring request

     Retrieves a mirroring request

    Args:
        mirroring_request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMirroringRequestResponse409 | RestMirroringRequest
    """

    return (
        await asyncio_detailed(
            mirroring_request_id=mirroring_request_id,
            client=client,
        )
    ).parsed
