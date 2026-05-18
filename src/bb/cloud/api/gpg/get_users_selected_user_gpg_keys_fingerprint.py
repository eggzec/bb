from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.gpg_account_key import GPGAccountKey
from ...types import Response

__all__ = [
    "sync_detailed",
    "asyncio_detailed",
    "sync",
    "asyncio",
]


def _get_kwargs(
    selected_user: str,
    fingerprint: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users/{selected_user}/gpg-keys/{fingerprint}".format(
            selected_user=quote(str(selected_user), safe=""),
            fingerprint=quote(str(fingerprint), safe=""),
        ),
    }

    return _kwargs


type ParsedPayload = Any | Error | GPGAccountKey
type ParseResult = Any | Error | GPGAccountKey | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_200 = GPGAccountKey.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
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
    fingerprint: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """Get a GPG key

     Returns a specific GPG public key belonging to a user.
    The `key` and `subkeys` fields can also be requested from the endpoint.
    See [Partial Responses](/cloud/bitbucket/rest/intro/#partial-response) for more details.

    Args:
        selected_user (str):
        fingerprint (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | GPGAccountKey]
    """

    kwargs = _get_kwargs(
        selected_user=selected_user,
        fingerprint=fingerprint,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    selected_user: str,
    fingerprint: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    """Get a GPG key

     Returns a specific GPG public key belonging to a user.
    The `key` and `subkeys` fields can also be requested from the endpoint.
    See [Partial Responses](/cloud/bitbucket/rest/intro/#partial-response) for more details.

    Args:
        selected_user (str):
        fingerprint (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | GPGAccountKey
    """

    return sync_detailed(
        selected_user=selected_user,
        fingerprint=fingerprint,
        client=client,
    ).parsed


async def asyncio_detailed(
    selected_user: str,
    fingerprint: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """Get a GPG key

     Returns a specific GPG public key belonging to a user.
    The `key` and `subkeys` fields can also be requested from the endpoint.
    See [Partial Responses](/cloud/bitbucket/rest/intro/#partial-response) for more details.

    Args:
        selected_user (str):
        fingerprint (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | GPGAccountKey]
    """

    kwargs = _get_kwargs(
        selected_user=selected_user,
        fingerprint=fingerprint,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    selected_user: str,
    fingerprint: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    """Get a GPG key

     Returns a specific GPG public key belonging to a user.
    The `key` and `subkeys` fields can also be requested from the endpoint.
    See [Partial Responses](/cloud/bitbucket/rest/intro/#partial-response) for more details.

    Args:
        selected_user (str):
        fingerprint (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | GPGAccountKey
    """

    return (
        await asyncio_detailed(
            selected_user=selected_user,
            fingerprint=fingerprint,
            client=client,
        )
    ).parsed
