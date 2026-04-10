from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.modify_all_user_permission_response_400 import ModifyAllUserPermissionResponse400
from ...models.modify_all_user_permission_response_401 import ModifyAllUserPermissionResponse401
from ...models.modify_all_user_permission_response_404 import ModifyAllUserPermissionResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    permission: str,
    *,
    allow: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["allow"] = allow

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/latest/projects/{project_key}/permissions/{permission}/all".format(
            project_key=quote(str(project_key), safe=""),
            permission=quote(str(permission), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | ModifyAllUserPermissionResponse400
    | ModifyAllUserPermissionResponse401
    | ModifyAllUserPermissionResponse404
    | None
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = ModifyAllUserPermissionResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ModifyAllUserPermissionResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ModifyAllUserPermissionResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | ModifyAllUserPermissionResponse400 | ModifyAllUserPermissionResponse401 | ModifyAllUserPermissionResponse404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    permission: str,
    *,
    client: AuthenticatedClient | Client,
    allow: str | Unset = UNSET,
) -> Response[
    Any | ModifyAllUserPermissionResponse400 | ModifyAllUserPermissionResponse401 | ModifyAllUserPermissionResponse404
]:
    """Grant project permission

     Grant or revoke a project permission to all users, i.e. set the default permission.


    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the specified project
    or a higher
    global permission to call this resource.

    Args:
        project_key (str):
        permission (str):
        allow (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ModifyAllUserPermissionResponse400 | ModifyAllUserPermissionResponse401 | ModifyAllUserPermissionResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        permission=permission,
        allow=allow,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    permission: str,
    *,
    client: AuthenticatedClient | Client,
    allow: str | Unset = UNSET,
) -> (
    Any
    | ModifyAllUserPermissionResponse400
    | ModifyAllUserPermissionResponse401
    | ModifyAllUserPermissionResponse404
    | None
):
    """Grant project permission

     Grant or revoke a project permission to all users, i.e. set the default permission.


    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the specified project
    or a higher
    global permission to call this resource.

    Args:
        project_key (str):
        permission (str):
        allow (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ModifyAllUserPermissionResponse400 | ModifyAllUserPermissionResponse401 | ModifyAllUserPermissionResponse404
    """

    return sync_detailed(
        project_key=project_key,
        permission=permission,
        client=client,
        allow=allow,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    permission: str,
    *,
    client: AuthenticatedClient | Client,
    allow: str | Unset = UNSET,
) -> Response[
    Any | ModifyAllUserPermissionResponse400 | ModifyAllUserPermissionResponse401 | ModifyAllUserPermissionResponse404
]:
    """Grant project permission

     Grant or revoke a project permission to all users, i.e. set the default permission.


    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the specified project
    or a higher
    global permission to call this resource.

    Args:
        project_key (str):
        permission (str):
        allow (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ModifyAllUserPermissionResponse400 | ModifyAllUserPermissionResponse401 | ModifyAllUserPermissionResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        permission=permission,
        allow=allow,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    permission: str,
    *,
    client: AuthenticatedClient | Client,
    allow: str | Unset = UNSET,
) -> (
    Any
    | ModifyAllUserPermissionResponse400
    | ModifyAllUserPermissionResponse401
    | ModifyAllUserPermissionResponse404
    | None
):
    """Grant project permission

     Grant or revoke a project permission to all users, i.e. set the default permission.


    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the specified project
    or a higher
    global permission to call this resource.

    Args:
        project_key (str):
        permission (str):
        allow (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ModifyAllUserPermissionResponse400 | ModifyAllUserPermissionResponse401 | ModifyAllUserPermissionResponse404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            permission=permission,
            client=client,
            allow=allow,
        )
    ).parsed
