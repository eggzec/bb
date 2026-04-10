from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.revoke_permissions_for_group_response_401 import RevokePermissionsForGroupResponse401
from ...models.revoke_permissions_for_group_response_404 import RevokePermissionsForGroupResponse404
from ...models.revoke_permissions_for_group_response_409 import RevokePermissionsForGroupResponse409
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
        "url": "/api/latest/admin/permissions/groups",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | RevokePermissionsForGroupResponse401
    | RevokePermissionsForGroupResponse404
    | RevokePermissionsForGroupResponse409
    | None
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = RevokePermissionsForGroupResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = RevokePermissionsForGroupResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = RevokePermissionsForGroupResponse409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | RevokePermissionsForGroupResponse401
    | RevokePermissionsForGroupResponse404
    | RevokePermissionsForGroupResponse409
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
    | RevokePermissionsForGroupResponse401
    | RevokePermissionsForGroupResponse404
    | RevokePermissionsForGroupResponse409
]:
    """Revoke all global permissions for group

     Revoke all global permissions for a group.



    The authenticated user must have:


    - <strong>ADMIN</strong> permission or higher; and
    - greater or equal permissions than the current permission level of the group (a user may not demote
    the     permission level of a group with higher permissions than them)


    to call this resource. In addition, a user may not revoke a group's permissions if their own
    permission level
    would be reduced as a result.

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RevokePermissionsForGroupResponse401 | RevokePermissionsForGroupResponse404 | RevokePermissionsForGroupResponse409]
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
    | RevokePermissionsForGroupResponse401
    | RevokePermissionsForGroupResponse404
    | RevokePermissionsForGroupResponse409
    | None
):
    """Revoke all global permissions for group

     Revoke all global permissions for a group.



    The authenticated user must have:


    - <strong>ADMIN</strong> permission or higher; and
    - greater or equal permissions than the current permission level of the group (a user may not demote
    the     permission level of a group with higher permissions than them)


    to call this resource. In addition, a user may not revoke a group's permissions if their own
    permission level
    would be reduced as a result.

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RevokePermissionsForGroupResponse401 | RevokePermissionsForGroupResponse404 | RevokePermissionsForGroupResponse409
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
    | RevokePermissionsForGroupResponse401
    | RevokePermissionsForGroupResponse404
    | RevokePermissionsForGroupResponse409
]:
    """Revoke all global permissions for group

     Revoke all global permissions for a group.



    The authenticated user must have:


    - <strong>ADMIN</strong> permission or higher; and
    - greater or equal permissions than the current permission level of the group (a user may not demote
    the     permission level of a group with higher permissions than them)


    to call this resource. In addition, a user may not revoke a group's permissions if their own
    permission level
    would be reduced as a result.

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RevokePermissionsForGroupResponse401 | RevokePermissionsForGroupResponse404 | RevokePermissionsForGroupResponse409]
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
    | RevokePermissionsForGroupResponse401
    | RevokePermissionsForGroupResponse404
    | RevokePermissionsForGroupResponse409
    | None
):
    """Revoke all global permissions for group

     Revoke all global permissions for a group.



    The authenticated user must have:


    - <strong>ADMIN</strong> permission or higher; and
    - greater or equal permissions than the current permission level of the group (a user may not demote
    the     permission level of a group with higher permissions than them)


    to call this resource. In addition, a user may not revoke a group's permissions if their own
    permission level
    would be reduced as a result.

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RevokePermissionsForGroupResponse401 | RevokePermissionsForGroupResponse404 | RevokePermissionsForGroupResponse409
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
        )
    ).parsed
