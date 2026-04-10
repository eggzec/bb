from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.has_all_user_permission_response_400 import HasAllUserPermissionResponse400
from ...models.has_all_user_permission_response_401 import HasAllUserPermissionResponse401
from ...models.has_all_user_permission_response_403 import HasAllUserPermissionResponse403
from ...models.has_all_user_permission_response_404 import HasAllUserPermissionResponse404
from ...models.rest_permitted import RestPermitted
from ...types import Response


def _get_kwargs(
    project_key: str,
    permission: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/permissions/{permission}/all".format(
            project_key=quote(str(project_key), safe=""),
            permission=quote(str(permission), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    HasAllUserPermissionResponse400
    | HasAllUserPermissionResponse401
    | HasAllUserPermissionResponse403
    | HasAllUserPermissionResponse404
    | RestPermitted
    | None
):
    if response.status_code == 200:
        response_200 = RestPermitted.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = HasAllUserPermissionResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = HasAllUserPermissionResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = HasAllUserPermissionResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = HasAllUserPermissionResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    HasAllUserPermissionResponse400
    | HasAllUserPermissionResponse401
    | HasAllUserPermissionResponse403
    | HasAllUserPermissionResponse404
    | RestPermitted
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
) -> Response[
    HasAllUserPermissionResponse400
    | HasAllUserPermissionResponse401
    | HasAllUserPermissionResponse403
    | HasAllUserPermissionResponse404
    | RestPermitted
]:
    """Check default project permission

     Check whether the specified permission is the default permission (granted to all users) for a
    project.

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the specified project
    or a higher global permission to call this resource.

    Args:
        project_key (str):
        permission (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HasAllUserPermissionResponse400 | HasAllUserPermissionResponse401 | HasAllUserPermissionResponse403 | HasAllUserPermissionResponse404 | RestPermitted]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        permission=permission,
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
) -> (
    HasAllUserPermissionResponse400
    | HasAllUserPermissionResponse401
    | HasAllUserPermissionResponse403
    | HasAllUserPermissionResponse404
    | RestPermitted
    | None
):
    """Check default project permission

     Check whether the specified permission is the default permission (granted to all users) for a
    project.

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the specified project
    or a higher global permission to call this resource.

    Args:
        project_key (str):
        permission (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HasAllUserPermissionResponse400 | HasAllUserPermissionResponse401 | HasAllUserPermissionResponse403 | HasAllUserPermissionResponse404 | RestPermitted
    """

    return sync_detailed(
        project_key=project_key,
        permission=permission,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    permission: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    HasAllUserPermissionResponse400
    | HasAllUserPermissionResponse401
    | HasAllUserPermissionResponse403
    | HasAllUserPermissionResponse404
    | RestPermitted
]:
    """Check default project permission

     Check whether the specified permission is the default permission (granted to all users) for a
    project.

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the specified project
    or a higher global permission to call this resource.

    Args:
        project_key (str):
        permission (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HasAllUserPermissionResponse400 | HasAllUserPermissionResponse401 | HasAllUserPermissionResponse403 | HasAllUserPermissionResponse404 | RestPermitted]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        permission=permission,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    permission: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    HasAllUserPermissionResponse400
    | HasAllUserPermissionResponse401
    | HasAllUserPermissionResponse403
    | HasAllUserPermissionResponse404
    | RestPermitted
    | None
):
    """Check default project permission

     Check whether the specified permission is the default permission (granted to all users) for a
    project.

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the specified project
    or a higher global permission to call this resource.

    Args:
        project_key (str):
        permission (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HasAllUserPermissionResponse400 | HasAllUserPermissionResponse401 | HasAllUserPermissionResponse403 | HasAllUserPermissionResponse404 | RestPermitted
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            permission=permission,
            client=client,
        )
    ).parsed
