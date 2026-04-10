from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_key_response_400 import AddKeyResponse400
from ...models.add_key_response_401 import AddKeyResponse401
from ...models.rest_gpg_key import RestGpgKey
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RestGpgKey | Unset = UNSET,
    user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["user"] = user

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/gpg/latest/keys",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AddKeyResponse400 | AddKeyResponse401 | RestGpgKey | None:
    if response.status_code == 200:
        response_200 = RestGpgKey.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = AddKeyResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = AddKeyResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AddKeyResponse400 | AddKeyResponse401 | RestGpgKey]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RestGpgKey | Unset = UNSET,
    user: str | Unset = UNSET,
) -> Response[AddKeyResponse400 | AddKeyResponse401 | RestGpgKey]:
    """Create a GPG key

     Add a GPG key to the authenticated user's account. Optionally, users with ADMIN and higher
    permissions may choose to specify the <code>user</code> parameter to add a GPG key for another user.

    Only authenticated users may call this endpoint.

    Args:
        user (str | Unset):
        body (RestGpgKey | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddKeyResponse400 | AddKeyResponse401 | RestGpgKey]
    """

    kwargs = _get_kwargs(
        body=body,
        user=user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: RestGpgKey | Unset = UNSET,
    user: str | Unset = UNSET,
) -> AddKeyResponse400 | AddKeyResponse401 | RestGpgKey | None:
    """Create a GPG key

     Add a GPG key to the authenticated user's account. Optionally, users with ADMIN and higher
    permissions may choose to specify the <code>user</code> parameter to add a GPG key for another user.

    Only authenticated users may call this endpoint.

    Args:
        user (str | Unset):
        body (RestGpgKey | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddKeyResponse400 | AddKeyResponse401 | RestGpgKey
    """

    return sync_detailed(
        client=client,
        body=body,
        user=user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RestGpgKey | Unset = UNSET,
    user: str | Unset = UNSET,
) -> Response[AddKeyResponse400 | AddKeyResponse401 | RestGpgKey]:
    """Create a GPG key

     Add a GPG key to the authenticated user's account. Optionally, users with ADMIN and higher
    permissions may choose to specify the <code>user</code> parameter to add a GPG key for another user.

    Only authenticated users may call this endpoint.

    Args:
        user (str | Unset):
        body (RestGpgKey | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddKeyResponse400 | AddKeyResponse401 | RestGpgKey]
    """

    kwargs = _get_kwargs(
        body=body,
        user=user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RestGpgKey | Unset = UNSET,
    user: str | Unset = UNSET,
) -> AddKeyResponse400 | AddKeyResponse401 | RestGpgKey | None:
    """Create a GPG key

     Add a GPG key to the authenticated user's account. Optionally, users with ADMIN and higher
    permissions may choose to specify the <code>user</code> parameter to add a GPG key for another user.

    Only authenticated users may call this endpoint.

    Args:
        user (str | Unset):
        body (RestGpgKey | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddKeyResponse400 | AddKeyResponse401 | RestGpgKey
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            user=user,
        )
    ).parsed
