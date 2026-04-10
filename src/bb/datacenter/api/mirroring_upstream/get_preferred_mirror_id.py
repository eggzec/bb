from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_preferred_mirror_id_response_404 import GetPreferredMirrorIdResponse404
from ...models.rest_mirror_server import RestMirrorServer
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/mirroring/latest/account/settings/preferred-mirror",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetPreferredMirrorIdResponse404 | RestMirrorServer | None:
    if response.status_code == 200:
        response_200 = RestMirrorServer.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = GetPreferredMirrorIdResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetPreferredMirrorIdResponse404 | RestMirrorServer]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetPreferredMirrorIdResponse404 | RestMirrorServer]:
    """Get preferred mirror

     Retrieves the current user's preferred mirror server

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPreferredMirrorIdResponse404 | RestMirrorServer]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> GetPreferredMirrorIdResponse404 | RestMirrorServer | None:
    """Get preferred mirror

     Retrieves the current user's preferred mirror server

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPreferredMirrorIdResponse404 | RestMirrorServer
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetPreferredMirrorIdResponse404 | RestMirrorServer]:
    """Get preferred mirror

     Retrieves the current user's preferred mirror server

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPreferredMirrorIdResponse404 | RestMirrorServer]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> GetPreferredMirrorIdResponse404 | RestMirrorServer | None:
    """Get preferred mirror

     Retrieves the current user's preferred mirror server

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPreferredMirrorIdResponse404 | RestMirrorServer
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
