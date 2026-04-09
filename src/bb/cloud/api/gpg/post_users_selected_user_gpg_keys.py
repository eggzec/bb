from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.gpg_account_key import GPGAccountKey
from ...types import UNSET, Response, Unset

__all__ = [
    "sync_detailed",
    "asyncio_detailed",
    "sync",
    "asyncio",
]


def _get_kwargs(
    selected_user: str,
    *,
    body: GPGAccountKey | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/users/{selected_user}/gpg-keys".format(
            selected_user=quote(str(selected_user), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


type ParsedPayload = Any | Error | GPGAccountKey
type ParseResult = Any | Error | GPGAccountKey | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 201:
        response_201 = GPGAccountKey.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

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
    body: GPGAccountKey | Unset = UNSET,
) -> Response[ParsedPayload]:
    r"""Add a new GPG key

     Adds a new GPG public key to the specified user account and returns the resulting key.

    Example:

    ```
    $ curl -X POST -H \"Content-Type: application/json\" -d
    '{\"key\": \"<insert GPG Key>\"}'
    https://api.bitbucket.org/2.0/users/{d7dd0e2d-3994-4a50-a9ee-d260b6cefdab}/gpg-keys
    ```

    Args:
        selected_user (str):
        body (GPGAccountKey | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | GPGAccountKey]
    """

    kwargs = _get_kwargs(
        selected_user=selected_user,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    selected_user: str,
    *,
    client: AuthenticatedClient,
    body: GPGAccountKey | Unset = UNSET,
) -> ParsedPayload | None:
    r"""Add a new GPG key

     Adds a new GPG public key to the specified user account and returns the resulting key.

    Example:

    ```
    $ curl -X POST -H \"Content-Type: application/json\" -d
    '{\"key\": \"<insert GPG Key>\"}'
    https://api.bitbucket.org/2.0/users/{d7dd0e2d-3994-4a50-a9ee-d260b6cefdab}/gpg-keys
    ```

    Args:
        selected_user (str):
        body (GPGAccountKey | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | GPGAccountKey
    """

    return sync_detailed(
        selected_user=selected_user,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    selected_user: str,
    *,
    client: AuthenticatedClient,
    body: GPGAccountKey | Unset = UNSET,
) -> Response[ParsedPayload]:
    r"""Add a new GPG key

     Adds a new GPG public key to the specified user account and returns the resulting key.

    Example:

    ```
    $ curl -X POST -H \"Content-Type: application/json\" -d
    '{\"key\": \"<insert GPG Key>\"}'
    https://api.bitbucket.org/2.0/users/{d7dd0e2d-3994-4a50-a9ee-d260b6cefdab}/gpg-keys
    ```

    Args:
        selected_user (str):
        body (GPGAccountKey | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | GPGAccountKey]
    """

    kwargs = _get_kwargs(
        selected_user=selected_user,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    selected_user: str,
    *,
    client: AuthenticatedClient,
    body: GPGAccountKey | Unset = UNSET,
) -> ParsedPayload | None:
    r"""Add a new GPG key

     Adds a new GPG public key to the specified user account and returns the resulting key.

    Example:

    ```
    $ curl -X POST -H \"Content-Type: application/json\" -d
    '{\"key\": \"<insert GPG Key>\"}'
    https://api.bitbucket.org/2.0/users/{d7dd0e2d-3994-4a50-a9ee-d260b6cefdab}/gpg-keys
    ```

    Args:
        selected_user (str):
        body (GPGAccountKey | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | GPGAccountKey
    """

    return (
        await asyncio_detailed(
            selected_user=selected_user,
            client=client,
            body=body,
        )
    ).parsed
