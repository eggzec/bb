from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_keys_for_user_response_200 import GetKeysForUserResponse200
from ...models.get_keys_for_user_response_401 import GetKeysForUserResponse401
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    user: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["user"] = user

    params["start"] = start

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/gpg/latest/keys",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetKeysForUserResponse200 | GetKeysForUserResponse401 | None:
    if response.status_code == 200:
        response_200 = GetKeysForUserResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetKeysForUserResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetKeysForUserResponse200 | GetKeysForUserResponse401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    user: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GetKeysForUserResponse200 | GetKeysForUserResponse401]:
    """Get all GPG keys

     Find all the keys for the currently authenticated user. Optionally, users with ADMIN and higher
    permissions may choose to specify the <code>user</code> parameter to retrieve GPG keys for another
    user.

    Only authenticated users may call this endpoint.

    Args:
        user (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetKeysForUserResponse200 | GetKeysForUserResponse401]
    """

    kwargs = _get_kwargs(
        user=user,
        start=start,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    user: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetKeysForUserResponse200 | GetKeysForUserResponse401 | None:
    """Get all GPG keys

     Find all the keys for the currently authenticated user. Optionally, users with ADMIN and higher
    permissions may choose to specify the <code>user</code> parameter to retrieve GPG keys for another
    user.

    Only authenticated users may call this endpoint.

    Args:
        user (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetKeysForUserResponse200 | GetKeysForUserResponse401
    """

    return sync_detailed(
        client=client,
        user=user,
        start=start,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    user: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GetKeysForUserResponse200 | GetKeysForUserResponse401]:
    """Get all GPG keys

     Find all the keys for the currently authenticated user. Optionally, users with ADMIN and higher
    permissions may choose to specify the <code>user</code> parameter to retrieve GPG keys for another
    user.

    Only authenticated users may call this endpoint.

    Args:
        user (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetKeysForUserResponse200 | GetKeysForUserResponse401]
    """

    kwargs = _get_kwargs(
        user=user,
        start=start,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    user: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetKeysForUserResponse200 | GetKeysForUserResponse401 | None:
    """Get all GPG keys

     Find all the keys for the currently authenticated user. Optionally, users with ADMIN and higher
    permissions may choose to specify the <code>user</code> parameter to retrieve GPG keys for another
    user.

    Only authenticated users may call this endpoint.

    Args:
        user (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetKeysForUserResponse200 | GetKeysForUserResponse401
    """

    return (
        await asyncio_detailed(
            client=client,
            user=user,
            start=start,
            limit=limit,
        )
    ).parsed
