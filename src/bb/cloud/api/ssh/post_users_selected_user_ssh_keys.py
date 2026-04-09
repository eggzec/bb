from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.ssh_account_key import SshAccountKey
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
    body: SshAccountKey | Unset = UNSET,
    expires_on: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["expires_on"] = expires_on

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/users/{selected_user}/ssh-keys".format(
            selected_user=quote(str(selected_user), safe=""),
        ),
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


type ParsedPayload = Any | Error | SshAccountKey
type ParseResult = Any | Error | SshAccountKey | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 201:
        response_201 = SshAccountKey.from_dict(response.json())

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
    body: SshAccountKey | Unset = UNSET,
    expires_on: str | Unset = UNSET,
) -> Response[ParsedPayload]:
    r"""Add a new SSH key

     Adds a new SSH public key to the specified user account and returns the resulting key.

    Example:

    ```
    $ curl -X POST -H \"Content-Type: application/json\" -d '{\"key\": \"ssh-ed25519
    AAAAC3NzaC1lZDI1NTE5AAAAIKqP3Cr632C2dNhhgKVcon4ldUSAeKiku2yP9O9/bDtY user@myhost\"}'
    https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}/ssh-keys
    ```

    Args:
        selected_user (str):
        expires_on (str | Unset):
        body (SshAccountKey | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | SshAccountKey]
    """

    kwargs = _get_kwargs(
        selected_user=selected_user,
        body=body,
        expires_on=expires_on,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    selected_user: str,
    *,
    client: AuthenticatedClient,
    body: SshAccountKey | Unset = UNSET,
    expires_on: str | Unset = UNSET,
) -> ParsedPayload | None:
    r"""Add a new SSH key

     Adds a new SSH public key to the specified user account and returns the resulting key.

    Example:

    ```
    $ curl -X POST -H \"Content-Type: application/json\" -d '{\"key\": \"ssh-ed25519
    AAAAC3NzaC1lZDI1NTE5AAAAIKqP3Cr632C2dNhhgKVcon4ldUSAeKiku2yP9O9/bDtY user@myhost\"}'
    https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}/ssh-keys
    ```

    Args:
        selected_user (str):
        expires_on (str | Unset):
        body (SshAccountKey | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | SshAccountKey
    """

    return sync_detailed(
        selected_user=selected_user,
        client=client,
        body=body,
        expires_on=expires_on,
    ).parsed


async def asyncio_detailed(
    selected_user: str,
    *,
    client: AuthenticatedClient,
    body: SshAccountKey | Unset = UNSET,
    expires_on: str | Unset = UNSET,
) -> Response[ParsedPayload]:
    r"""Add a new SSH key

     Adds a new SSH public key to the specified user account and returns the resulting key.

    Example:

    ```
    $ curl -X POST -H \"Content-Type: application/json\" -d '{\"key\": \"ssh-ed25519
    AAAAC3NzaC1lZDI1NTE5AAAAIKqP3Cr632C2dNhhgKVcon4ldUSAeKiku2yP9O9/bDtY user@myhost\"}'
    https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}/ssh-keys
    ```

    Args:
        selected_user (str):
        expires_on (str | Unset):
        body (SshAccountKey | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | SshAccountKey]
    """

    kwargs = _get_kwargs(
        selected_user=selected_user,
        body=body,
        expires_on=expires_on,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    selected_user: str,
    *,
    client: AuthenticatedClient,
    body: SshAccountKey | Unset = UNSET,
    expires_on: str | Unset = UNSET,
) -> ParsedPayload | None:
    r"""Add a new SSH key

     Adds a new SSH public key to the specified user account and returns the resulting key.

    Example:

    ```
    $ curl -X POST -H \"Content-Type: application/json\" -d '{\"key\": \"ssh-ed25519
    AAAAC3NzaC1lZDI1NTE5AAAAIKqP3Cr632C2dNhhgKVcon4ldUSAeKiku2yP9O9/bDtY user@myhost\"}'
    https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}/ssh-keys
    ```

    Args:
        selected_user (str):
        expires_on (str | Unset):
        body (SshAccountKey | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | SshAccountKey
    """

    return (
        await asyncio_detailed(
            selected_user=selected_user,
            client=client,
            body=body,
            expires_on=expires_on,
        )
    ).parsed
