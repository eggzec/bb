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
from ...models.project_user_permission import ProjectUserPermission
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
    selected_user_id: str,
    *,
    body: BitbucketAppsPermissionsSerializersProjectPermissionUpdateSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/workspaces/{workspace}/projects/{project_key}/permissions-config/users/{selected_user_id}".format(
            workspace=quote(str(workspace), safe=""),
            project_key=quote(str(project_key), safe=""),
            selected_user_id=quote(str(selected_user_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


type ParsedPayload = Error | ProjectUserPermission
type ParseResult = Error | ProjectUserPermission | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_200 = ProjectUserPermission.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_402 = Error.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
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
    selected_user_id: str,
    *,
    client: AuthenticatedClient,
    body: BitbucketAppsPermissionsSerializersProjectPermissionUpdateSchema,
) -> Response[ParsedPayload]:
    """Update an explicit user permission for a project

     Updates the explicit user permission for a given user and project. The selected
    user must be a member of the workspace, and cannot be the workspace owner.

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
        selected_user_id (str):
        body (BitbucketAppsPermissionsSerializersProjectPermissionUpdateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ProjectUserPermission]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        project_key=project_key,
        selected_user_id=selected_user_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    project_key: str,
    selected_user_id: str,
    *,
    client: AuthenticatedClient,
    body: BitbucketAppsPermissionsSerializersProjectPermissionUpdateSchema,
) -> ParsedPayload | None:
    """Update an explicit user permission for a project

     Updates the explicit user permission for a given user and project. The selected
    user must be a member of the workspace, and cannot be the workspace owner.

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
        selected_user_id (str):
        body (BitbucketAppsPermissionsSerializersProjectPermissionUpdateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ProjectUserPermission
    """

    return sync_detailed(
        workspace=workspace,
        project_key=project_key,
        selected_user_id=selected_user_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    project_key: str,
    selected_user_id: str,
    *,
    client: AuthenticatedClient,
    body: BitbucketAppsPermissionsSerializersProjectPermissionUpdateSchema,
) -> Response[ParsedPayload]:
    """Update an explicit user permission for a project

     Updates the explicit user permission for a given user and project. The selected
    user must be a member of the workspace, and cannot be the workspace owner.

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
        selected_user_id (str):
        body (BitbucketAppsPermissionsSerializersProjectPermissionUpdateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ProjectUserPermission]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        project_key=project_key,
        selected_user_id=selected_user_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    project_key: str,
    selected_user_id: str,
    *,
    client: AuthenticatedClient,
    body: BitbucketAppsPermissionsSerializersProjectPermissionUpdateSchema,
) -> ParsedPayload | None:
    """Update an explicit user permission for a project

     Updates the explicit user permission for a given user and project. The selected
    user must be a member of the workspace, and cannot be the workspace owner.

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
        selected_user_id (str):
        body (BitbucketAppsPermissionsSerializersProjectPermissionUpdateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ProjectUserPermission
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            project_key=project_key,
            selected_user_id=selected_user_id,
            client=client,
            body=body,
        )
    ).parsed
