from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_mirror_response_404 import GetMirrorResponse404
from ...models.rest_mirror_server import RestMirrorServer
from ...types import Response


def _get_kwargs(
    mirror_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/mirroring/latest/mirrorServers/{mirror_id}".format(
            mirror_id=quote(str(mirror_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetMirrorResponse404 | RestMirrorServer | None:
    if response.status_code == 200:
        response_200 = RestMirrorServer.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = GetMirrorResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetMirrorResponse404 | RestMirrorServer]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    mirror_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetMirrorResponse404 | RestMirrorServer]:
    """Get mirror by ID

     Returns the mirror specified by a mirror ID

    Args:
        mirror_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMirrorResponse404 | RestMirrorServer]
    """

    kwargs = _get_kwargs(
        mirror_id=mirror_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    mirror_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetMirrorResponse404 | RestMirrorServer | None:
    """Get mirror by ID

     Returns the mirror specified by a mirror ID

    Args:
        mirror_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMirrorResponse404 | RestMirrorServer
    """

    return sync_detailed(
        mirror_id=mirror_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    mirror_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetMirrorResponse404 | RestMirrorServer]:
    """Get mirror by ID

     Returns the mirror specified by a mirror ID

    Args:
        mirror_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMirrorResponse404 | RestMirrorServer]
    """

    kwargs = _get_kwargs(
        mirror_id=mirror_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    mirror_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetMirrorResponse404 | RestMirrorServer | None:
    """Get mirror by ID

     Returns the mirror specified by a mirror ID

    Args:
        mirror_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMirrorResponse404 | RestMirrorServer
    """

    return (
        await asyncio_detailed(
            mirror_id=mirror_id,
            client=client,
        )
    ).parsed
