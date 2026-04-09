from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.account import Account
from ...models.error import Error
from ...types import Response

__all__ = [
    "sync_detailed",
    "asyncio_detailed",
    "sync",
    "asyncio",
]


def _get_kwargs(
    selected_user: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users/{selected_user}".format(
            selected_user=quote(str(selected_user), safe=""),
        ),
    }

    return _kwargs


type ParsedPayload = Account | Error
type ParseResult = Account | Error | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        response_200 = Account.from_dict(response.json())

        return response_200

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


def sync_detailed(
    selected_user: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """Get a user

     Gets the public information associated with a user account.

    If the user's profile is private, `location`, `website` and
    `created_on` elements are omitted.

    Note that the user object returned by this operation is changing significantly, due to privacy
    changes.
    See the [announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-changes-
    gdpr/#changes-to-bitbucket-user-objects) for details.

    Args:
        selected_user (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Account | Error]
    """

    kwargs = _get_kwargs(
        selected_user=selected_user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    selected_user: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    """Get a user

     Gets the public information associated with a user account.

    If the user's profile is private, `location`, `website` and
    `created_on` elements are omitted.

    Note that the user object returned by this operation is changing significantly, due to privacy
    changes.
    See the [announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-changes-
    gdpr/#changes-to-bitbucket-user-objects) for details.

    Args:
        selected_user (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Account | Error
    """

    return sync_detailed(
        selected_user=selected_user,
        client=client,
    ).parsed


async def asyncio_detailed(
    selected_user: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """Get a user

     Gets the public information associated with a user account.

    If the user's profile is private, `location`, `website` and
    `created_on` elements are omitted.

    Note that the user object returned by this operation is changing significantly, due to privacy
    changes.
    See the [announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-changes-
    gdpr/#changes-to-bitbucket-user-objects) for details.

    Args:
        selected_user (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Account | Error]
    """

    kwargs = _get_kwargs(
        selected_user=selected_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    selected_user: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    """Get a user

     Gets the public information associated with a user account.

    If the user's profile is private, `location`, `website` and
    `created_on` elements are omitted.

    Note that the user object returned by this operation is changing significantly, due to privacy
    changes.
    See the [announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-changes-
    gdpr/#changes-to-bitbucket-user-objects) for details.

    Args:
        selected_user (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Account | Error
    """

    return (
        await asyncio_detailed(
            selected_user=selected_user,
            client=client,
        )
    ).parsed
