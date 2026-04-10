from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_for_user_response_401 import DeleteForUserResponse401
from ...models.delete_for_user_response_404 import DeleteForUserResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    user: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["user"] = user

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/gpg/latest/keys",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteForUserResponse401 | DeleteForUserResponse404 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = DeleteForUserResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = DeleteForUserResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteForUserResponse401 | DeleteForUserResponse404]:
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
) -> Response[Any | DeleteForUserResponse401 | DeleteForUserResponse404]:
    """Delete all GPG keys for user

     Delete all GPG keys for a supplied user.

    Args:
        user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteForUserResponse401 | DeleteForUserResponse404]
    """

    kwargs = _get_kwargs(
        user=user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    user: str | Unset = UNSET,
) -> Any | DeleteForUserResponse401 | DeleteForUserResponse404 | None:
    """Delete all GPG keys for user

     Delete all GPG keys for a supplied user.

    Args:
        user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteForUserResponse401 | DeleteForUserResponse404
    """

    return sync_detailed(
        client=client,
        user=user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    user: str | Unset = UNSET,
) -> Response[Any | DeleteForUserResponse401 | DeleteForUserResponse404]:
    """Delete all GPG keys for user

     Delete all GPG keys for a supplied user.

    Args:
        user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteForUserResponse401 | DeleteForUserResponse404]
    """

    kwargs = _get_kwargs(
        user=user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    user: str | Unset = UNSET,
) -> Any | DeleteForUserResponse401 | DeleteForUserResponse404 | None:
    """Delete all GPG keys for user

     Delete all GPG keys for a supplied user.

    Args:
        user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteForUserResponse401 | DeleteForUserResponse404
    """

    return (
        await asyncio_detailed(
            client=client,
            user=user,
        )
    ).parsed
