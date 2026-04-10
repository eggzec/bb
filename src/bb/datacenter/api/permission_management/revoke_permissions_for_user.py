from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.revoke_permissions_for_user_response_401 import RevokePermissionsForUserResponse401
from ...models.revoke_permissions_for_user_response_404 import RevokePermissionsForUserResponse404
from ...models.revoke_permissions_for_user_response_409 import RevokePermissionsForUserResponse409
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
        "url": "/api/latest/admin/permissions/users",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | RevokePermissionsForUserResponse401
    | RevokePermissionsForUserResponse404
    | RevokePermissionsForUserResponse409
    | None
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = RevokePermissionsForUserResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = RevokePermissionsForUserResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = RevokePermissionsForUserResponse409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | RevokePermissionsForUserResponse401
    | RevokePermissionsForUserResponse404
    | RevokePermissionsForUserResponse409
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
    Any
    | RevokePermissionsForUserResponse401
    | RevokePermissionsForUserResponse404
    | RevokePermissionsForUserResponse409
]:
    """Revoke all global permissions for user

     Revoke all global permissions for a user.


    The authenticated user must have:


    - <strong>ADMIN</strong> permission or higher; and
    - greater or equal permissions than the current permission level of the user (a user may not demote
    the     permission level of a user with higher permissions than them)


    to call this resource. In addition, a user may not demote their own permission level.

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RevokePermissionsForUserResponse401 | RevokePermissionsForUserResponse404 | RevokePermissionsForUserResponse409]
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
    Any
    | RevokePermissionsForUserResponse401
    | RevokePermissionsForUserResponse404
    | RevokePermissionsForUserResponse409
    | None
):
    """Revoke all global permissions for user

     Revoke all global permissions for a user.


    The authenticated user must have:


    - <strong>ADMIN</strong> permission or higher; and
    - greater or equal permissions than the current permission level of the user (a user may not demote
    the     permission level of a user with higher permissions than them)


    to call this resource. In addition, a user may not demote their own permission level.

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RevokePermissionsForUserResponse401 | RevokePermissionsForUserResponse404 | RevokePermissionsForUserResponse409
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
    Any
    | RevokePermissionsForUserResponse401
    | RevokePermissionsForUserResponse404
    | RevokePermissionsForUserResponse409
]:
    """Revoke all global permissions for user

     Revoke all global permissions for a user.


    The authenticated user must have:


    - <strong>ADMIN</strong> permission or higher; and
    - greater or equal permissions than the current permission level of the user (a user may not demote
    the     permission level of a user with higher permissions than them)


    to call this resource. In addition, a user may not demote their own permission level.

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RevokePermissionsForUserResponse401 | RevokePermissionsForUserResponse404 | RevokePermissionsForUserResponse409]
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
    Any
    | RevokePermissionsForUserResponse401
    | RevokePermissionsForUserResponse404
    | RevokePermissionsForUserResponse409
    | None
):
    """Revoke all global permissions for user

     Revoke all global permissions for a user.


    The authenticated user must have:


    - <strong>ADMIN</strong> permission or higher; and
    - greater or equal permissions than the current permission level of the user (a user may not demote
    the     permission level of a user with higher permissions than them)


    to call this resource. In addition, a user may not demote their own permission level.

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RevokePermissionsForUserResponse401 | RevokePermissionsForUserResponse404 | RevokePermissionsForUserResponse409
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
        )
    ).parsed
