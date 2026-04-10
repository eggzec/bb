from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_user_response_400 import DeleteUserResponse400
from ...models.delete_user_response_401 import DeleteUserResponse401
from ...models.delete_user_response_403 import DeleteUserResponse403
from ...models.delete_user_response_404 import DeleteUserResponse404
from ...models.delete_user_response_409 import DeleteUserResponse409
from ...models.rest_detailed_user import RestDetailedUser
from ...types import UNSET, Response


def _get_kwargs(
    *,
    name: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["name"] = name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/latest/admin/users",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteUserResponse400
    | DeleteUserResponse401
    | DeleteUserResponse403
    | DeleteUserResponse404
    | DeleteUserResponse409
    | RestDetailedUser
    | None
):
    if response.status_code == 200:
        response_200 = RestDetailedUser.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = DeleteUserResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteUserResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteUserResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteUserResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = DeleteUserResponse409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteUserResponse400
    | DeleteUserResponse401
    | DeleteUserResponse403
    | DeleteUserResponse404
    | DeleteUserResponse409
    | RestDetailedUser
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    name: str,
) -> Response[
    DeleteUserResponse400
    | DeleteUserResponse401
    | DeleteUserResponse403
    | DeleteUserResponse404
    | DeleteUserResponse409
    | RestDetailedUser
]:
    """Remove user

     Deletes the specified user, removing them from the system. This also removes any permissions that
    may have been granted to the user.

    A user may not delete themselves, and a user with <strong>ADMIN</strong> permissions may not delete
    a user with <strong>SYS_ADMIN</strong> permissions.

    The authenticated user must have the <strong>ADMIN</strong> permission to call this resource.

    Note: The permission removal process occurs 7 days after the user deletion.

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteUserResponse400 | DeleteUserResponse401 | DeleteUserResponse403 | DeleteUserResponse404 | DeleteUserResponse409 | RestDetailedUser]
    """

    kwargs = _get_kwargs(
        name=name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    name: str,
) -> (
    DeleteUserResponse400
    | DeleteUserResponse401
    | DeleteUserResponse403
    | DeleteUserResponse404
    | DeleteUserResponse409
    | RestDetailedUser
    | None
):
    """Remove user

     Deletes the specified user, removing them from the system. This also removes any permissions that
    may have been granted to the user.

    A user may not delete themselves, and a user with <strong>ADMIN</strong> permissions may not delete
    a user with <strong>SYS_ADMIN</strong> permissions.

    The authenticated user must have the <strong>ADMIN</strong> permission to call this resource.

    Note: The permission removal process occurs 7 days after the user deletion.

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteUserResponse400 | DeleteUserResponse401 | DeleteUserResponse403 | DeleteUserResponse404 | DeleteUserResponse409 | RestDetailedUser
    """

    return sync_detailed(
        client=client,
        name=name,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    name: str,
) -> Response[
    DeleteUserResponse400
    | DeleteUserResponse401
    | DeleteUserResponse403
    | DeleteUserResponse404
    | DeleteUserResponse409
    | RestDetailedUser
]:
    """Remove user

     Deletes the specified user, removing them from the system. This also removes any permissions that
    may have been granted to the user.

    A user may not delete themselves, and a user with <strong>ADMIN</strong> permissions may not delete
    a user with <strong>SYS_ADMIN</strong> permissions.

    The authenticated user must have the <strong>ADMIN</strong> permission to call this resource.

    Note: The permission removal process occurs 7 days after the user deletion.

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteUserResponse400 | DeleteUserResponse401 | DeleteUserResponse403 | DeleteUserResponse404 | DeleteUserResponse409 | RestDetailedUser]
    """

    kwargs = _get_kwargs(
        name=name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    name: str,
) -> (
    DeleteUserResponse400
    | DeleteUserResponse401
    | DeleteUserResponse403
    | DeleteUserResponse404
    | DeleteUserResponse409
    | RestDetailedUser
    | None
):
    """Remove user

     Deletes the specified user, removing them from the system. This also removes any permissions that
    may have been granted to the user.

    A user may not delete themselves, and a user with <strong>ADMIN</strong> permissions may not delete
    a user with <strong>SYS_ADMIN</strong> permissions.

    The authenticated user must have the <strong>ADMIN</strong> permission to call this resource.

    Note: The permission removal process occurs 7 days after the user deletion.

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteUserResponse400 | DeleteUserResponse401 | DeleteUserResponse403 | DeleteUserResponse404 | DeleteUserResponse409 | RestDetailedUser
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
        )
    ).parsed
