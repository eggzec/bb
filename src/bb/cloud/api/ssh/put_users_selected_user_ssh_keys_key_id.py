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
    key_id: str,
    *,
    body: SshAccountKey | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/users/{selected_user}/ssh-keys/{key_id}".format(
            selected_user=quote(str(selected_user), safe=""),
            key_id=quote(str(key_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


type ParsedPayload = Any | Error | SshAccountKey
type ParseResult = Any | Error | SshAccountKey | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_200 = SshAccountKey.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_400 = Error.from_dict(response.json())

        return response_400

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
    key_id: str,
    *,
    client: AuthenticatedClient,
    body: SshAccountKey | Unset = UNSET,
) -> Response[ParsedPayload]:
    r"""Update a SSH key

     Updates a specific SSH public key on a user's account

    Note: Only the 'comment' field can be updated using this API. To modify the key or comment values,
    you must delete and add the key again.

    Example:

    ```
    $ curl -X PUT -H \"Content-Type: application/json\" -d '{\"label\": \"Work key\"}'
    https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}/ssh-
    keys/{b15b6026-9c02-4626-b4ad-b905f99f763a}
    ```

    Args:
        selected_user (str):
        key_id (str):
        body (SshAccountKey | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | SshAccountKey]
    """

    kwargs = _get_kwargs(
        selected_user=selected_user,
        key_id=key_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    selected_user: str,
    key_id: str,
    *,
    client: AuthenticatedClient,
    body: SshAccountKey | Unset = UNSET,
) -> ParsedPayload | None:
    r"""Update a SSH key

     Updates a specific SSH public key on a user's account

    Note: Only the 'comment' field can be updated using this API. To modify the key or comment values,
    you must delete and add the key again.

    Example:

    ```
    $ curl -X PUT -H \"Content-Type: application/json\" -d '{\"label\": \"Work key\"}'
    https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}/ssh-
    keys/{b15b6026-9c02-4626-b4ad-b905f99f763a}
    ```

    Args:
        selected_user (str):
        key_id (str):
        body (SshAccountKey | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | SshAccountKey
    """

    return sync_detailed(
        selected_user=selected_user,
        key_id=key_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    selected_user: str,
    key_id: str,
    *,
    client: AuthenticatedClient,
    body: SshAccountKey | Unset = UNSET,
) -> Response[ParsedPayload]:
    r"""Update a SSH key

     Updates a specific SSH public key on a user's account

    Note: Only the 'comment' field can be updated using this API. To modify the key or comment values,
    you must delete and add the key again.

    Example:

    ```
    $ curl -X PUT -H \"Content-Type: application/json\" -d '{\"label\": \"Work key\"}'
    https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}/ssh-
    keys/{b15b6026-9c02-4626-b4ad-b905f99f763a}
    ```

    Args:
        selected_user (str):
        key_id (str):
        body (SshAccountKey | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | SshAccountKey]
    """

    kwargs = _get_kwargs(
        selected_user=selected_user,
        key_id=key_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    selected_user: str,
    key_id: str,
    *,
    client: AuthenticatedClient,
    body: SshAccountKey | Unset = UNSET,
) -> ParsedPayload | None:
    r"""Update a SSH key

     Updates a specific SSH public key on a user's account

    Note: Only the 'comment' field can be updated using this API. To modify the key or comment values,
    you must delete and add the key again.

    Example:

    ```
    $ curl -X PUT -H \"Content-Type: application/json\" -d '{\"label\": \"Work key\"}'
    https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}/ssh-
    keys/{b15b6026-9c02-4626-b4ad-b905f99f763a}
    ```

    Args:
        selected_user (str):
        key_id (str):
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
            key_id=key_id,
            client=client,
            body=body,
        )
    ).parsed
