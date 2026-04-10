from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_ssh_access_key import RestSshAccessKey
from ...models.update_permission_response_401 import UpdatePermissionResponse401
from ...models.update_permission_response_404 import UpdatePermissionResponse404
from ...types import Response


def _get_kwargs(
    project_key: str,
    key_id: str,
    permission: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/keys/latest/projects/{project_key}/ssh/{key_id}/permission/{permission}".format(
            project_key=quote(str(project_key), safe=""),
            key_id=quote(str(key_id), safe=""),
            permission=quote(str(permission), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RestSshAccessKey | UpdatePermissionResponse401 | UpdatePermissionResponse404 | None:
    if response.status_code == 200:
        response_200 = RestSshAccessKey.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = UpdatePermissionResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = UpdatePermissionResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RestSshAccessKey | UpdatePermissionResponse401 | UpdatePermissionResponse404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    key_id: str,
    permission: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RestSshAccessKey | UpdatePermissionResponse401 | UpdatePermissionResponse404]:
    """Update project SSH key permission

     Updates the permission granted to the specified SSH key to the project identified in the URL.

    Args:
        project_key (str):
        key_id (str):
        permission (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestSshAccessKey | UpdatePermissionResponse401 | UpdatePermissionResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        key_id=key_id,
        permission=permission,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    key_id: str,
    permission: str,
    *,
    client: AuthenticatedClient | Client,
) -> RestSshAccessKey | UpdatePermissionResponse401 | UpdatePermissionResponse404 | None:
    """Update project SSH key permission

     Updates the permission granted to the specified SSH key to the project identified in the URL.

    Args:
        project_key (str):
        key_id (str):
        permission (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestSshAccessKey | UpdatePermissionResponse401 | UpdatePermissionResponse404
    """

    return sync_detailed(
        project_key=project_key,
        key_id=key_id,
        permission=permission,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    key_id: str,
    permission: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RestSshAccessKey | UpdatePermissionResponse401 | UpdatePermissionResponse404]:
    """Update project SSH key permission

     Updates the permission granted to the specified SSH key to the project identified in the URL.

    Args:
        project_key (str):
        key_id (str):
        permission (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestSshAccessKey | UpdatePermissionResponse401 | UpdatePermissionResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        key_id=key_id,
        permission=permission,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    key_id: str,
    permission: str,
    *,
    client: AuthenticatedClient | Client,
) -> RestSshAccessKey | UpdatePermissionResponse401 | UpdatePermissionResponse404 | None:
    """Update project SSH key permission

     Updates the permission granted to the specified SSH key to the project identified in the URL.

    Args:
        project_key (str):
        key_id (str):
        permission (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestSshAccessKey | UpdatePermissionResponse401 | UpdatePermissionResponse404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            key_id=key_id,
            permission=permission,
            client=client,
        )
    ).parsed
