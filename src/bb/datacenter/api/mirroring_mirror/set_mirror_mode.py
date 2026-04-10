from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.set_mirror_mode_response_400 import SetMirrorModeResponse400
from ...models.set_mirror_mode_response_401 import SetMirrorModeResponse401
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/mirroring/latest/syncSettings/mode",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | SetMirrorModeResponse400 | SetMirrorModeResponse401 | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 400:
        response_400 = SetMirrorModeResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = SetMirrorModeResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | SetMirrorModeResponse400 | SetMirrorModeResponse401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: str | Unset = UNSET,
) -> Response[Any | SetMirrorModeResponse400 | SetMirrorModeResponse401]:
    """Update mirror mode

     Sets the mirror mode for the specified upstream

    Args:
        body (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SetMirrorModeResponse400 | SetMirrorModeResponse401]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: str | Unset = UNSET,
) -> Any | SetMirrorModeResponse400 | SetMirrorModeResponse401 | None:
    """Update mirror mode

     Sets the mirror mode for the specified upstream

    Args:
        body (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SetMirrorModeResponse400 | SetMirrorModeResponse401
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: str | Unset = UNSET,
) -> Response[Any | SetMirrorModeResponse400 | SetMirrorModeResponse401]:
    """Update mirror mode

     Sets the mirror mode for the specified upstream

    Args:
        body (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SetMirrorModeResponse400 | SetMirrorModeResponse401]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: str | Unset = UNSET,
) -> Any | SetMirrorModeResponse400 | SetMirrorModeResponse401 | None:
    """Update mirror mode

     Sets the mirror mode for the specified upstream

    Args:
        body (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SetMirrorModeResponse400 | SetMirrorModeResponse401
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
