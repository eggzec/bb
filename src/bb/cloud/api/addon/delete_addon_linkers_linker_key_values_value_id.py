from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...deprecation import deprecated_endpoint
from ...models.error import Error
from ...types import Response

__all__ = [
    "sync_detailed",
    "asyncio_detailed",
    "sync",
    "asyncio",
]


def _get_kwargs(
    linker_key: str,
    value_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/addon/linkers/{linker_key}/values/{value_id}".format(
            linker_key=quote(str(linker_key), safe=""),
            value_id=quote(str(value_id), safe=""),
        ),
    }

    return _kwargs


type ParsedPayload = Any | Error
type ParseResult = Any | Error | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ParsedPayload]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated_endpoint("May 2026")
def sync_detailed(
    linker_key: str,
    value_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """Delete a linker value

     Delete a single [linker](/cloud/bitbucket/modules/linker/) value
    of the authenticated application.

    This endpoint is deprecated and will be removed by May 2026.

    Args:
        linker_key (str):
        value_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
    """

    kwargs = _get_kwargs(
        linker_key=linker_key,
        value_id=value_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated_endpoint("May 2026")
def sync(
    linker_key: str,
    value_id: int,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    """Delete a linker value

     Delete a single [linker](/cloud/bitbucket/modules/linker/) value
    of the authenticated application.

    This endpoint is deprecated and will be removed by May 2026.

    Args:
        linker_key (str):
        value_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
    """

    return sync_detailed(
        linker_key=linker_key,
        value_id=value_id,
        client=client,
    ).parsed


@deprecated_endpoint("May 2026")
async def asyncio_detailed(
    linker_key: str,
    value_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """Delete a linker value

     Delete a single [linker](/cloud/bitbucket/modules/linker/) value
    of the authenticated application.

    This endpoint is deprecated and will be removed by May 2026.

    Args:
        linker_key (str):
        value_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
    """

    kwargs = _get_kwargs(
        linker_key=linker_key,
        value_id=value_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated_endpoint("May 2026")
async def asyncio(
    linker_key: str,
    value_id: int,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    """Delete a linker value

     Delete a single [linker](/cloud/bitbucket/modules/linker/) value
    of the authenticated application.

    This endpoint is deprecated and will be removed by May 2026.

    Args:
        linker_key (str):
        value_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
    """

    return (
        await asyncio_detailed(
            linker_key=linker_key,
            value_id=value_id,
            client=client,
        )
    ).parsed
