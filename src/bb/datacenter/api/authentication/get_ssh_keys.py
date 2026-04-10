from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_ssh_keys_response_200 import GetSshKeysResponse200
from ...models.get_ssh_keys_response_401 import GetSshKeysResponse401
from ...models.get_ssh_keys_response_404 import GetSshKeysResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    user_name: str | Unset = UNSET,
    user: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["userName"] = user_name

    params["user"] = user

    params["start"] = start

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/ssh/latest/keys",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetSshKeysResponse200 | GetSshKeysResponse401 | GetSshKeysResponse404 | None:
    if response.status_code == 200:
        response_200 = GetSshKeysResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetSshKeysResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetSshKeysResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetSshKeysResponse200 | GetSshKeysResponse401 | GetSshKeysResponse404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    user_name: str | Unset = UNSET,
    user: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GetSshKeysResponse200 | GetSshKeysResponse401 | GetSshKeysResponse404]:
    """Get SSH keys for user

     Retrieve a page of SSH keys.

    Args:
        user_name (str | Unset):
        user (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSshKeysResponse200 | GetSshKeysResponse401 | GetSshKeysResponse404]
    """

    kwargs = _get_kwargs(
        user_name=user_name,
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
    user_name: str | Unset = UNSET,
    user: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetSshKeysResponse200 | GetSshKeysResponse401 | GetSshKeysResponse404 | None:
    """Get SSH keys for user

     Retrieve a page of SSH keys.

    Args:
        user_name (str | Unset):
        user (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSshKeysResponse200 | GetSshKeysResponse401 | GetSshKeysResponse404
    """

    return sync_detailed(
        client=client,
        user_name=user_name,
        user=user,
        start=start,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    user_name: str | Unset = UNSET,
    user: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GetSshKeysResponse200 | GetSshKeysResponse401 | GetSshKeysResponse404]:
    """Get SSH keys for user

     Retrieve a page of SSH keys.

    Args:
        user_name (str | Unset):
        user (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSshKeysResponse200 | GetSshKeysResponse401 | GetSshKeysResponse404]
    """

    kwargs = _get_kwargs(
        user_name=user_name,
        user=user,
        start=start,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    user_name: str | Unset = UNSET,
    user: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetSshKeysResponse200 | GetSshKeysResponse401 | GetSshKeysResponse404 | None:
    """Get SSH keys for user

     Retrieve a page of SSH keys.

    Args:
        user_name (str | Unset):
        user (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSshKeysResponse200 | GetSshKeysResponse401 | GetSshKeysResponse404
    """

    return (
        await asyncio_detailed(
            client=client,
            user_name=user_name,
            user=user,
            start=start,
            limit=limit,
        )
    ).parsed
