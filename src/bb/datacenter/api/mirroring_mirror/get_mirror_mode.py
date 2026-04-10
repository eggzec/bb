from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_mirror_mode_response_401 import GetMirrorModeResponse401
from ...models.get_mirror_mode_response_404 import GetMirrorModeResponse404
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/mirroring/latest/syncSettings/mode",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetMirrorModeResponse401 | GetMirrorModeResponse404 | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 401:
        response_401 = GetMirrorModeResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetMirrorModeResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetMirrorModeResponse401 | GetMirrorModeResponse404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetMirrorModeResponse401 | GetMirrorModeResponse404]:
    """Get mirror mode

     Gets the current mirror mode

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetMirrorModeResponse401 | GetMirrorModeResponse404]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetMirrorModeResponse401 | GetMirrorModeResponse404 | None:
    """Get mirror mode

     Gets the current mirror mode

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetMirrorModeResponse401 | GetMirrorModeResponse404
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetMirrorModeResponse401 | GetMirrorModeResponse404]:
    """Get mirror mode

     Gets the current mirror mode

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetMirrorModeResponse401 | GetMirrorModeResponse404]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetMirrorModeResponse401 | GetMirrorModeResponse404 | None:
    """Get mirror mode

     Gets the current mirror mode

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetMirrorModeResponse401 | GetMirrorModeResponse404
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
