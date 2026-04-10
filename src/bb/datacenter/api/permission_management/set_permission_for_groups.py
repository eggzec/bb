from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.set_permission_for_groups_permission import SetPermissionForGroupsPermission
from ...models.set_permission_for_groups_response_400 import SetPermissionForGroupsResponse400
from ...models.set_permission_for_groups_response_401 import SetPermissionForGroupsResponse401
from ...models.set_permission_for_groups_response_403 import SetPermissionForGroupsResponse403
from ...models.set_permission_for_groups_response_404 import SetPermissionForGroupsResponse404
from ...models.set_permission_for_groups_response_409 import SetPermissionForGroupsResponse409
from ...types import UNSET, Response


def _get_kwargs(
    *,
    name: list[str],
    permission: SetPermissionForGroupsPermission,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_name = name

    params["name"] = json_name

    json_permission = permission.value
    params["permission"] = json_permission

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/latest/admin/permissions/groups",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | SetPermissionForGroupsResponse400
    | SetPermissionForGroupsResponse401
    | SetPermissionForGroupsResponse403
    | SetPermissionForGroupsResponse404
    | SetPermissionForGroupsResponse409
    | None
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = SetPermissionForGroupsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = SetPermissionForGroupsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = SetPermissionForGroupsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = SetPermissionForGroupsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = SetPermissionForGroupsResponse409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | SetPermissionForGroupsResponse400
    | SetPermissionForGroupsResponse401
    | SetPermissionForGroupsResponse403
    | SetPermissionForGroupsResponse404
    | SetPermissionForGroupsResponse409
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
    permission: SetPermissionForGroupsPermission,
) -> Response[
    Any
    | SetPermissionForGroupsResponse400
    | SetPermissionForGroupsResponse401
    | SetPermissionForGroupsResponse403
    | SetPermissionForGroupsResponse404
    | SetPermissionForGroupsResponse409
]:
    r"""Update global permission for group

     Promote or demote a group's global permission level. Available global permissions are:


    - LICENSED_USER
    - PROJECT_CREATE
    - ADMIN
    - SYS_ADMIN

    See the <a
    href=\"https://confluence.atlassian.com/display/BitbucketServer/Global+permissions\">Bitbucket Data
    Center documentation</a> for a detailed explanation of what each permission entails.


    The authenticated user must have:


    - <strong>ADMIN</strong> permission or higher; and
    - the permission they are attempting to grant or higher; and
    - greater or equal permissions than the current permission level of the group (a user may not demote
    the     permission level of a group with higher permissions than them)


    to call this resource. In addition, a user may not demote a group's permission level if their own
    permission
    level would be reduced as a result.

    Args:
        name (list[str]):
        permission (SetPermissionForGroupsPermission):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SetPermissionForGroupsResponse400 | SetPermissionForGroupsResponse401 | SetPermissionForGroupsResponse403 | SetPermissionForGroupsResponse404 | SetPermissionForGroupsResponse409]
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
    permission: SetPermissionForGroupsPermission,
) -> (
    Any
    | SetPermissionForGroupsResponse400
    | SetPermissionForGroupsResponse401
    | SetPermissionForGroupsResponse403
    | SetPermissionForGroupsResponse404
    | SetPermissionForGroupsResponse409
    | None
):
    r"""Update global permission for group

     Promote or demote a group's global permission level. Available global permissions are:


    - LICENSED_USER
    - PROJECT_CREATE
    - ADMIN
    - SYS_ADMIN

    See the <a
    href=\"https://confluence.atlassian.com/display/BitbucketServer/Global+permissions\">Bitbucket Data
    Center documentation</a> for a detailed explanation of what each permission entails.


    The authenticated user must have:


    - <strong>ADMIN</strong> permission or higher; and
    - the permission they are attempting to grant or higher; and
    - greater or equal permissions than the current permission level of the group (a user may not demote
    the     permission level of a group with higher permissions than them)


    to call this resource. In addition, a user may not demote a group's permission level if their own
    permission
    level would be reduced as a result.

    Args:
        name (list[str]):
        permission (SetPermissionForGroupsPermission):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SetPermissionForGroupsResponse400 | SetPermissionForGroupsResponse401 | SetPermissionForGroupsResponse403 | SetPermissionForGroupsResponse404 | SetPermissionForGroupsResponse409
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
    permission: SetPermissionForGroupsPermission,
) -> Response[
    Any
    | SetPermissionForGroupsResponse400
    | SetPermissionForGroupsResponse401
    | SetPermissionForGroupsResponse403
    | SetPermissionForGroupsResponse404
    | SetPermissionForGroupsResponse409
]:
    r"""Update global permission for group

     Promote or demote a group's global permission level. Available global permissions are:


    - LICENSED_USER
    - PROJECT_CREATE
    - ADMIN
    - SYS_ADMIN

    See the <a
    href=\"https://confluence.atlassian.com/display/BitbucketServer/Global+permissions\">Bitbucket Data
    Center documentation</a> for a detailed explanation of what each permission entails.


    The authenticated user must have:


    - <strong>ADMIN</strong> permission or higher; and
    - the permission they are attempting to grant or higher; and
    - greater or equal permissions than the current permission level of the group (a user may not demote
    the     permission level of a group with higher permissions than them)


    to call this resource. In addition, a user may not demote a group's permission level if their own
    permission
    level would be reduced as a result.

    Args:
        name (list[str]):
        permission (SetPermissionForGroupsPermission):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SetPermissionForGroupsResponse400 | SetPermissionForGroupsResponse401 | SetPermissionForGroupsResponse403 | SetPermissionForGroupsResponse404 | SetPermissionForGroupsResponse409]
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
    permission: SetPermissionForGroupsPermission,
) -> (
    Any
    | SetPermissionForGroupsResponse400
    | SetPermissionForGroupsResponse401
    | SetPermissionForGroupsResponse403
    | SetPermissionForGroupsResponse404
    | SetPermissionForGroupsResponse409
    | None
):
    r"""Update global permission for group

     Promote or demote a group's global permission level. Available global permissions are:


    - LICENSED_USER
    - PROJECT_CREATE
    - ADMIN
    - SYS_ADMIN

    See the <a
    href=\"https://confluence.atlassian.com/display/BitbucketServer/Global+permissions\">Bitbucket Data
    Center documentation</a> for a detailed explanation of what each permission entails.


    The authenticated user must have:


    - <strong>ADMIN</strong> permission or higher; and
    - the permission they are attempting to grant or higher; and
    - greater or equal permissions than the current permission level of the group (a user may not demote
    the     permission level of a group with higher permissions than them)


    to call this resource. In addition, a user may not demote a group's permission level if their own
    permission
    level would be reduced as a result.

    Args:
        name (list[str]):
        permission (SetPermissionForGroupsPermission):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SetPermissionForGroupsResponse400 | SetPermissionForGroupsResponse401 | SetPermissionForGroupsResponse403 | SetPermissionForGroupsResponse404 | SetPermissionForGroupsResponse409
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
            permission=permission,
        )
    ).parsed
