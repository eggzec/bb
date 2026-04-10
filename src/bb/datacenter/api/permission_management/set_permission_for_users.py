from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.set_permission_for_users_permission import SetPermissionForUsersPermission
from ...models.set_permission_for_users_response_400 import SetPermissionForUsersResponse400
from ...models.set_permission_for_users_response_401 import SetPermissionForUsersResponse401
from ...models.set_permission_for_users_response_403 import SetPermissionForUsersResponse403
from ...models.set_permission_for_users_response_404 import SetPermissionForUsersResponse404
from ...models.set_permission_for_users_response_409 import SetPermissionForUsersResponse409
from ...types import UNSET, Response


def _get_kwargs(
    *,
    name: list[str],
    permission: SetPermissionForUsersPermission,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_name = name

    params["name"] = json_name

    json_permission = permission.value
    params["permission"] = json_permission

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/latest/admin/permissions/users",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | SetPermissionForUsersResponse400
    | SetPermissionForUsersResponse401
    | SetPermissionForUsersResponse403
    | SetPermissionForUsersResponse404
    | SetPermissionForUsersResponse409
    | None
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = SetPermissionForUsersResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = SetPermissionForUsersResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = SetPermissionForUsersResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = SetPermissionForUsersResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = SetPermissionForUsersResponse409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | SetPermissionForUsersResponse400
    | SetPermissionForUsersResponse401
    | SetPermissionForUsersResponse403
    | SetPermissionForUsersResponse404
    | SetPermissionForUsersResponse409
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
    name: list[str],
    permission: SetPermissionForUsersPermission,
) -> Response[
    Any
    | SetPermissionForUsersResponse400
    | SetPermissionForUsersResponse401
    | SetPermissionForUsersResponse403
    | SetPermissionForUsersResponse404
    | SetPermissionForUsersResponse409
]:
    r"""Update global permission for user

     Promote or demote the global permission level of a user. Available global permissions are:


    - LICENSED_USER
    - PROJECT_CREATE
    - ADMIN
    - SYS_ADMIN


    See the <a
    href=\"https://confluence.atlassian.com/display/BitbucketServer/Global+permissions\">Bitbucket Data
    Center documentation</a> for a detailed explanation of what each permission entails.


    The authenticated user must have:


    - <strong>ADMIN</strong> permission or higher; and
    - the permission they are attempting to grant; and
    - greater or equal permissions than the current permission level of the user (a user may not demote
    the     permission level of a user with higher permissions than them)


    to call this resource. In addition, a user may not demote their own permission level.

    Args:
        name (list[str]):
        permission (SetPermissionForUsersPermission):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SetPermissionForUsersResponse400 | SetPermissionForUsersResponse401 | SetPermissionForUsersResponse403 | SetPermissionForUsersResponse404 | SetPermissionForUsersResponse409]
    """

    kwargs = _get_kwargs(
        name=name,
        permission=permission,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    name: list[str],
    permission: SetPermissionForUsersPermission,
) -> (
    Any
    | SetPermissionForUsersResponse400
    | SetPermissionForUsersResponse401
    | SetPermissionForUsersResponse403
    | SetPermissionForUsersResponse404
    | SetPermissionForUsersResponse409
    | None
):
    r"""Update global permission for user

     Promote or demote the global permission level of a user. Available global permissions are:


    - LICENSED_USER
    - PROJECT_CREATE
    - ADMIN
    - SYS_ADMIN


    See the <a
    href=\"https://confluence.atlassian.com/display/BitbucketServer/Global+permissions\">Bitbucket Data
    Center documentation</a> for a detailed explanation of what each permission entails.


    The authenticated user must have:


    - <strong>ADMIN</strong> permission or higher; and
    - the permission they are attempting to grant; and
    - greater or equal permissions than the current permission level of the user (a user may not demote
    the     permission level of a user with higher permissions than them)


    to call this resource. In addition, a user may not demote their own permission level.

    Args:
        name (list[str]):
        permission (SetPermissionForUsersPermission):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SetPermissionForUsersResponse400 | SetPermissionForUsersResponse401 | SetPermissionForUsersResponse403 | SetPermissionForUsersResponse404 | SetPermissionForUsersResponse409
    """

    return sync_detailed(
        client=client,
        name=name,
        permission=permission,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    name: list[str],
    permission: SetPermissionForUsersPermission,
) -> Response[
    Any
    | SetPermissionForUsersResponse400
    | SetPermissionForUsersResponse401
    | SetPermissionForUsersResponse403
    | SetPermissionForUsersResponse404
    | SetPermissionForUsersResponse409
]:
    r"""Update global permission for user

     Promote or demote the global permission level of a user. Available global permissions are:


    - LICENSED_USER
    - PROJECT_CREATE
    - ADMIN
    - SYS_ADMIN


    See the <a
    href=\"https://confluence.atlassian.com/display/BitbucketServer/Global+permissions\">Bitbucket Data
    Center documentation</a> for a detailed explanation of what each permission entails.


    The authenticated user must have:


    - <strong>ADMIN</strong> permission or higher; and
    - the permission they are attempting to grant; and
    - greater or equal permissions than the current permission level of the user (a user may not demote
    the     permission level of a user with higher permissions than them)


    to call this resource. In addition, a user may not demote their own permission level.

    Args:
        name (list[str]):
        permission (SetPermissionForUsersPermission):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SetPermissionForUsersResponse400 | SetPermissionForUsersResponse401 | SetPermissionForUsersResponse403 | SetPermissionForUsersResponse404 | SetPermissionForUsersResponse409]
    """

    kwargs = _get_kwargs(
        name=name,
        permission=permission,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    name: list[str],
    permission: SetPermissionForUsersPermission,
) -> (
    Any
    | SetPermissionForUsersResponse400
    | SetPermissionForUsersResponse401
    | SetPermissionForUsersResponse403
    | SetPermissionForUsersResponse404
    | SetPermissionForUsersResponse409
    | None
):
    r"""Update global permission for user

     Promote or demote the global permission level of a user. Available global permissions are:


    - LICENSED_USER
    - PROJECT_CREATE
    - ADMIN
    - SYS_ADMIN


    See the <a
    href=\"https://confluence.atlassian.com/display/BitbucketServer/Global+permissions\">Bitbucket Data
    Center documentation</a> for a detailed explanation of what each permission entails.


    The authenticated user must have:


    - <strong>ADMIN</strong> permission or higher; and
    - the permission they are attempting to grant; and
    - greater or equal permissions than the current permission level of the user (a user may not demote
    the     permission level of a user with higher permissions than them)


    to call this resource. In addition, a user may not demote their own permission level.

    Args:
        name (list[str]):
        permission (SetPermissionForUsersPermission):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SetPermissionForUsersResponse400 | SetPermissionForUsersResponse401 | SetPermissionForUsersResponse403 | SetPermissionForUsersResponse404 | SetPermissionForUsersResponse409
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
            permission=permission,
        )
    ).parsed
