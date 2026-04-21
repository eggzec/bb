from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bitbucket_apps_permissions_serializers_repo_permission_update_schema import (
    BitbucketAppsPermissionsSerializersRepoPermissionUpdateSchema,
)
from ...models.error import Error
from ...models.repository_group_permission import RepositoryGroupPermission
from ...types import Response

__all__ = [
    "sync_detailed",
    "asyncio_detailed",
    "sync",
    "asyncio",
]


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    group_slug: str,
    *,
    body: BitbucketAppsPermissionsSerializersRepoPermissionUpdateSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/repositories/{workspace}/{repo_slug}/permissions-config/groups/{group_slug}".format(
            workspace=quote(str(workspace), safe=""),
            repo_slug=quote(str(repo_slug), safe=""),
            group_slug=quote(str(group_slug), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


type ParsedPayload = Error | RepositoryGroupPermission
type ParseResult = Error | RepositoryGroupPermission | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_200 = RepositoryGroupPermission.from_dict(response.json())

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
    repo_slug: str,
    group_slug: str,
    *,
    client: AuthenticatedClient,
    body: BitbucketAppsPermissionsSerializersRepoPermissionUpdateSchema,
) -> Response[ParsedPayload]:
    """Update an explicit group permission for a repository

     Updates the group permission, or grants a new permission if one does not already exist.

    Only users with admin permission for the repository may access this resource.

    The only authentication method supported for this endpoint is via app passwords.

    Permissions can be:

    * `admin`
    * `write`
    * `read`

    Args:
        workspace (str):
        repo_slug (str):
        group_slug (str):
        body (BitbucketAppsPermissionsSerializersRepoPermissionUpdateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | RepositoryGroupPermission]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        group_slug=group_slug,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    repo_slug: str,
    group_slug: str,
    *,
    client: AuthenticatedClient,
    body: BitbucketAppsPermissionsSerializersRepoPermissionUpdateSchema,
) -> ParsedPayload | None:
    """Update an explicit group permission for a repository

     Updates the group permission, or grants a new permission if one does not already exist.

    Only users with admin permission for the repository may access this resource.

    The only authentication method supported for this endpoint is via app passwords.

    Permissions can be:

    * `admin`
    * `write`
    * `read`

    Args:
        workspace (str):
        repo_slug (str):
        group_slug (str):
        body (BitbucketAppsPermissionsSerializersRepoPermissionUpdateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | RepositoryGroupPermission
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        group_slug=group_slug,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    group_slug: str,
    *,
    client: AuthenticatedClient,
    body: BitbucketAppsPermissionsSerializersRepoPermissionUpdateSchema,
) -> Response[ParsedPayload]:
    """Update an explicit group permission for a repository

     Updates the group permission, or grants a new permission if one does not already exist.

    Only users with admin permission for the repository may access this resource.

    The only authentication method supported for this endpoint is via app passwords.

    Permissions can be:

    * `admin`
    * `write`
    * `read`

    Args:
        workspace (str):
        repo_slug (str):
        group_slug (str):
        body (BitbucketAppsPermissionsSerializersRepoPermissionUpdateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | RepositoryGroupPermission]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        group_slug=group_slug,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    group_slug: str,
    *,
    client: AuthenticatedClient,
    body: BitbucketAppsPermissionsSerializersRepoPermissionUpdateSchema,
) -> ParsedPayload | None:
    """Update an explicit group permission for a repository

     Updates the group permission, or grants a new permission if one does not already exist.

    Only users with admin permission for the repository may access this resource.

    The only authentication method supported for this endpoint is via app passwords.

    Permissions can be:

    * `admin`
    * `write`
    * `read`

    Args:
        workspace (str):
        repo_slug (str):
        group_slug (str):
        body (BitbucketAppsPermissionsSerializersRepoPermissionUpdateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | RepositoryGroupPermission
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            group_slug=group_slug,
            client=client,
            body=body,
        )
    ).parsed
