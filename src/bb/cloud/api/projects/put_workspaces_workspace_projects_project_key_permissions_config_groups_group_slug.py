from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bitbucket_apps_permissions_serializers_project_permission_update_schema import (
    BitbucketAppsPermissionsSerializersProjectPermissionUpdateSchema,
)
from ...models.error import Error
from ...models.project_group_permission import ProjectGroupPermission
from ...types import Response

__all__ = [
    "sync_detailed",
    "asyncio_detailed",
    "sync",
    "asyncio",
]


def _get_kwargs(
    workspace: str,
    project_key: str,
    group_slug: str,
    *,
    body: BitbucketAppsPermissionsSerializersProjectPermissionUpdateSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/workspaces/{workspace}/projects/{project_key}/permissions-config/groups/{group_slug}".format(
            workspace=quote(str(workspace), safe=""),
            project_key=quote(str(project_key), safe=""),
            group_slug=quote(str(group_slug), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


type ParsedPayload = Error | ProjectGroupPermission
type ParseResult = Error | ProjectGroupPermission | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        response_200 = ProjectGroupPermission.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = Error.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ParsedPayload]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace: str,
    project_key: str,
    group_slug: str,
    *,
    client: AuthenticatedClient,
    body: BitbucketAppsPermissionsSerializersProjectPermissionUpdateSchema,
) -> Response[ParsedPayload]:
    """Update an explicit group permission for a project

     Updates the group permission, or grants a new permission if one does not already exist.

    Only users with admin permission for the project may access this resource.

    Due to security concerns, the JWT and OAuth authentication methods are unsupported.
    This is to ensure integrations and add-ons are not allowed to change permissions.

    Permissions can be:

    * `admin`
    * `create-repo`
    * `write`
    * `read`

    Args:
        workspace (str):
        project_key (str):
        group_slug (str):
        body (BitbucketAppsPermissionsSerializersProjectPermissionUpdateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ProjectGroupPermission]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        project_key=project_key,
        group_slug=group_slug,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    project_key: str,
    group_slug: str,
    *,
    client: AuthenticatedClient,
    body: BitbucketAppsPermissionsSerializersProjectPermissionUpdateSchema,
) -> ParsedPayload | None:
    """Update an explicit group permission for a project

     Updates the group permission, or grants a new permission if one does not already exist.

    Only users with admin permission for the project may access this resource.

    Due to security concerns, the JWT and OAuth authentication methods are unsupported.
    This is to ensure integrations and add-ons are not allowed to change permissions.

    Permissions can be:

    * `admin`
    * `create-repo`
    * `write`
    * `read`

    Args:
        workspace (str):
        project_key (str):
        group_slug (str):
        body (BitbucketAppsPermissionsSerializersProjectPermissionUpdateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ProjectGroupPermission
    """

    return sync_detailed(
        workspace=workspace,
        project_key=project_key,
        group_slug=group_slug,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    project_key: str,
    group_slug: str,
    *,
    client: AuthenticatedClient,
    body: BitbucketAppsPermissionsSerializersProjectPermissionUpdateSchema,
) -> Response[ParsedPayload]:
    """Update an explicit group permission for a project

     Updates the group permission, or grants a new permission if one does not already exist.

    Only users with admin permission for the project may access this resource.

    Due to security concerns, the JWT and OAuth authentication methods are unsupported.
    This is to ensure integrations and add-ons are not allowed to change permissions.

    Permissions can be:

    * `admin`
    * `create-repo`
    * `write`
    * `read`

    Args:
        workspace (str):
        project_key (str):
        group_slug (str):
        body (BitbucketAppsPermissionsSerializersProjectPermissionUpdateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ProjectGroupPermission]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        project_key=project_key,
        group_slug=group_slug,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    project_key: str,
    group_slug: str,
    *,
    client: AuthenticatedClient,
    body: BitbucketAppsPermissionsSerializersProjectPermissionUpdateSchema,
) -> ParsedPayload | None:
    """Update an explicit group permission for a project

     Updates the group permission, or grants a new permission if one does not already exist.

    Only users with admin permission for the project may access this resource.

    Due to security concerns, the JWT and OAuth authentication methods are unsupported.
    This is to ensure integrations and add-ons are not allowed to change permissions.

    Permissions can be:

    * `admin`
    * `create-repo`
    * `write`
    * `read`

    Args:
        workspace (str):
        project_key (str):
        group_slug (str):
        body (BitbucketAppsPermissionsSerializersProjectPermissionUpdateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ProjectGroupPermission
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            project_key=project_key,
            group_slug=group_slug,
            client=client,
            body=body,
        )
    ).parsed
