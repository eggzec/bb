from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_upstream_server_response_404 import GetUpstreamServerResponse404
from ...models.rest_upstream_server import RestUpstreamServer
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/mirroring/latest/upstreamServer",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetUpstreamServerResponse404 | RestUpstreamServer | None:
    if response.status_code == 200:
        response_200 = RestUpstreamServer.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = GetUpstreamServerResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetUpstreamServerResponse404 | RestUpstreamServer]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetUpstreamServerResponse404 | RestUpstreamServer]:
    """Get upstream server

     Retrieves upstream server details.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUpstreamServerResponse404 | RestUpstreamServer]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> GetUpstreamServerResponse404 | RestUpstreamServer | None:
    """Get upstream server

     Retrieves upstream server details.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUpstreamServerResponse404 | RestUpstreamServer
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetUpstreamServerResponse404 | RestUpstreamServer]:
    """Get upstream server

     Retrieves upstream server details.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUpstreamServerResponse404 | RestUpstreamServer]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> GetUpstreamServerResponse404 | RestUpstreamServer | None:
    """Get upstream server

     Retrieves upstream server details.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUpstreamServerResponse404 | RestUpstreamServer
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
