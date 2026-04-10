from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_ssh_access_key import RestSshAccessKey
from ...models.update_permission_1_response_401 import UpdatePermission1Response401
from ...models.update_permission_1_response_404 import UpdatePermission1Response404
from ...types import Response


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    key_id: str,
    permission: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/keys/latest/projects/{project_key}/repos/{repository_slug}/ssh/{key_id}/permission/{permission}".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            key_id=quote(str(key_id), safe=""),
            permission=quote(str(permission), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RestSshAccessKey | UpdatePermission1Response401 | UpdatePermission1Response404 | None:
    if response.status_code == 200:
        response_200 = RestSshAccessKey.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = UpdatePermission1Response401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = UpdatePermission1Response404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RestSshAccessKey | UpdatePermission1Response401 | UpdatePermission1Response404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    repository_slug: str,
    key_id: str,
    permission: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RestSshAccessKey | UpdatePermission1Response401 | UpdatePermission1Response404]:
    """Update repository SSH key permission

     Updates the permission granted to the specified SSH key to the repository identified in the URL.

    Args:
        project_key (str):
        repository_slug (str):
        key_id (str):
        permission (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestSshAccessKey | UpdatePermission1Response401 | UpdatePermission1Response404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        key_id=key_id,
        permission=permission,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    repository_slug: str,
    key_id: str,
    permission: str,
    *,
    client: AuthenticatedClient | Client,
) -> RestSshAccessKey | UpdatePermission1Response401 | UpdatePermission1Response404 | None:
    """Update repository SSH key permission

     Updates the permission granted to the specified SSH key to the repository identified in the URL.

    Args:
        project_key (str):
        repository_slug (str):
        key_id (str):
        permission (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestSshAccessKey | UpdatePermission1Response401 | UpdatePermission1Response404
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        key_id=key_id,
        permission=permission,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    key_id: str,
    permission: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RestSshAccessKey | UpdatePermission1Response401 | UpdatePermission1Response404]:
    """Update repository SSH key permission

     Updates the permission granted to the specified SSH key to the repository identified in the URL.

    Args:
        project_key (str):
        repository_slug (str):
        key_id (str):
        permission (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestSshAccessKey | UpdatePermission1Response401 | UpdatePermission1Response404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        key_id=key_id,
        permission=permission,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    key_id: str,
    permission: str,
    *,
    client: AuthenticatedClient | Client,
) -> RestSshAccessKey | UpdatePermission1Response401 | UpdatePermission1Response404 | None:
    """Update repository SSH key permission

     Updates the permission granted to the specified SSH key to the repository identified in the URL.

    Args:
        project_key (str):
        repository_slug (str):
        key_id (str):
        permission (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestSshAccessKey | UpdatePermission1Response401 | UpdatePermission1Response404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            key_id=key_id,
            permission=permission,
            client=client,
        )
    ).parsed
