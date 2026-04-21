from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...types import Response

__all__ = [
    "sync_detailed",
    "asyncio_detailed",
    "sync",
    "asyncio",
]


def _get_kwargs(
    email: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/user/emails/{email}".format(
            email=quote(str(email), safe=""),
        ),
    }

    return _kwargs


type ParsedPayload = Error
type ParseResult = Error


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if "application/json" not in response.headers.get("content-type", ""):
        return None
    response_default = Error.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ParsedPayload]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    email: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """Get an email address for current user

     Returns details about a specific one of the authenticated user's
    email addresses.

    Details describe whether the address has been confirmed by the user and
    whether it is the user's primary address or not.

    Args:
        email (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        email=email,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    email: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    """Get an email address for current user

     Returns details about a specific one of the authenticated user's
    email addresses.

    Details describe whether the address has been confirmed by the user and
    whether it is the user's primary address or not.

    Args:
        email (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error
    """

    return sync_detailed(
        email=email,
        client=client,
    ).parsed


async def asyncio_detailed(
    email: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """Get an email address for current user

     Returns details about a specific one of the authenticated user's
    email addresses.

    Details describe whether the address has been confirmed by the user and
    whether it is the user's primary address or not.

    Args:
        email (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        email=email,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    email: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    """Get an email address for current user

     Returns details about a specific one of the authenticated user's
    email addresses.

    Details describe whether the address has been confirmed by the user and
    whether it is the user's primary address or not.

    Args:
        email (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error
    """

    return (
        await asyncio_detailed(
            email=email,
            client=client,
        )
    ).parsed
