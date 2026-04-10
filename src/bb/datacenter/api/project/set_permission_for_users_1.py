from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.set_permission_for_users_1_response_400 import SetPermissionForUsers1Response400
from ...models.set_permission_for_users_1_response_401 import SetPermissionForUsers1Response401
from ...models.set_permission_for_users_1_response_403 import SetPermissionForUsers1Response403
from ...models.set_permission_for_users_1_response_404 import SetPermissionForUsers1Response404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    *,
    name: str | Unset = UNSET,
    permission: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["name"] = name

    params["permission"] = permission

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/latest/projects/{project_key}/permissions/users".format(
            project_key=quote(str(project_key), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | SetPermissionForUsers1Response400
    | SetPermissionForUsers1Response401
    | SetPermissionForUsers1Response403
    | SetPermissionForUsers1Response404
    | None
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = SetPermissionForUsers1Response400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = SetPermissionForUsers1Response401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = SetPermissionForUsers1Response403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = SetPermissionForUsers1Response404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | SetPermissionForUsers1Response400
    | SetPermissionForUsers1Response401
    | SetPermissionForUsers1Response403
    | SetPermissionForUsers1Response404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    name: str | Unset = UNSET,
    permission: str | Unset = UNSET,
) -> Response[
    Any
    | SetPermissionForUsers1Response400
    | SetPermissionForUsers1Response401
    | SetPermissionForUsers1Response403
    | SetPermissionForUsers1Response404
]:
    """Update user project permission

     Promote or demote a user's permission level for the specified project.


    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the specified project
    or a higher global permission to call this resource. In addition, a user may not reduce their own
    permission level unless they have a global permission that already implies that permission.

    Args:
        project_key (str):
        name (str | Unset):
        permission (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SetPermissionForUsers1Response400 | SetPermissionForUsers1Response401 | SetPermissionForUsers1Response403 | SetPermissionForUsers1Response404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        name=name,
        permission=permission,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    name: str | Unset = UNSET,
    permission: str | Unset = UNSET,
) -> (
    Any
    | SetPermissionForUsers1Response400
    | SetPermissionForUsers1Response401
    | SetPermissionForUsers1Response403
    | SetPermissionForUsers1Response404
    | None
):
    """Update user project permission

     Promote or demote a user's permission level for the specified project.


    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the specified project
    or a higher global permission to call this resource. In addition, a user may not reduce their own
    permission level unless they have a global permission that already implies that permission.

    Args:
        project_key (str):
        name (str | Unset):
        permission (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SetPermissionForUsers1Response400 | SetPermissionForUsers1Response401 | SetPermissionForUsers1Response403 | SetPermissionForUsers1Response404
    """

    return sync_detailed(
        project_key=project_key,
        client=client,
        name=name,
        permission=permission,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    name: str | Unset = UNSET,
    permission: str | Unset = UNSET,
) -> Response[
    Any
    | SetPermissionForUsers1Response400
    | SetPermissionForUsers1Response401
    | SetPermissionForUsers1Response403
    | SetPermissionForUsers1Response404
]:
    """Update user project permission

     Promote or demote a user's permission level for the specified project.


    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the specified project
    or a higher global permission to call this resource. In addition, a user may not reduce their own
    permission level unless they have a global permission that already implies that permission.

    Args:
        project_key (str):
        name (str | Unset):
        permission (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SetPermissionForUsers1Response400 | SetPermissionForUsers1Response401 | SetPermissionForUsers1Response403 | SetPermissionForUsers1Response404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        name=name,
        permission=permission,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    name: str | Unset = UNSET,
    permission: str | Unset = UNSET,
) -> (
    Any
    | SetPermissionForUsers1Response400
    | SetPermissionForUsers1Response401
    | SetPermissionForUsers1Response403
    | SetPermissionForUsers1Response404
    | None
):
    """Update user project permission

     Promote or demote a user's permission level for the specified project.


    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the specified project
    or a higher global permission to call this resource. In addition, a user may not reduce their own
    permission level unless they have a global permission that already implies that permission.

    Args:
        project_key (str):
        name (str | Unset):
        permission (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SetPermissionForUsers1Response400 | SetPermissionForUsers1Response401 | SetPermissionForUsers1Response403 | SetPermissionForUsers1Response404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            client=client,
            name=name,
            permission=permission,
        )
    ).parsed
