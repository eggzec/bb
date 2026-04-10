from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.revoke_permissions_for_group_2_response_401 import RevokePermissionsForGroup2Response401
from ...models.revoke_permissions_for_group_2_response_404 import RevokePermissionsForGroup2Response404
from ...models.revoke_permissions_for_group_2_response_409 import RevokePermissionsForGroup2Response409
from ...types import UNSET, Response


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    *,
    name: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["name"] = name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/permissions/groups".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | RevokePermissionsForGroup2Response401
    | RevokePermissionsForGroup2Response404
    | RevokePermissionsForGroup2Response409
    | None
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = RevokePermissionsForGroup2Response401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = RevokePermissionsForGroup2Response404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = RevokePermissionsForGroup2Response409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | RevokePermissionsForGroup2Response401
    | RevokePermissionsForGroup2Response404
    | RevokePermissionsForGroup2Response409
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    name: str,
) -> Response[
    Any
    | RevokePermissionsForGroup2Response401
    | RevokePermissionsForGroup2Response404
    | RevokePermissionsForGroup2Response409
]:
    """Revoke group repository permission

     Revoke all permissions for the specified repository for a group.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the specified repository
    or a higher project or global permission to call this resource.

    In addition, a user may not revoke a group's permissions if it will reduce their own permission
    level.

    Args:
        project_key (str):
        repository_slug (str):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RevokePermissionsForGroup2Response401 | RevokePermissionsForGroup2Response404 | RevokePermissionsForGroup2Response409]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        name=name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    name: str,
) -> (
    Any
    | RevokePermissionsForGroup2Response401
    | RevokePermissionsForGroup2Response404
    | RevokePermissionsForGroup2Response409
    | None
):
    """Revoke group repository permission

     Revoke all permissions for the specified repository for a group.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the specified repository
    or a higher project or global permission to call this resource.

    In addition, a user may not revoke a group's permissions if it will reduce their own permission
    level.

    Args:
        project_key (str):
        repository_slug (str):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RevokePermissionsForGroup2Response401 | RevokePermissionsForGroup2Response404 | RevokePermissionsForGroup2Response409
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        client=client,
        name=name,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    name: str,
) -> Response[
    Any
    | RevokePermissionsForGroup2Response401
    | RevokePermissionsForGroup2Response404
    | RevokePermissionsForGroup2Response409
]:
    """Revoke group repository permission

     Revoke all permissions for the specified repository for a group.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the specified repository
    or a higher project or global permission to call this resource.

    In addition, a user may not revoke a group's permissions if it will reduce their own permission
    level.

    Args:
        project_key (str):
        repository_slug (str):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RevokePermissionsForGroup2Response401 | RevokePermissionsForGroup2Response404 | RevokePermissionsForGroup2Response409]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        name=name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    name: str,
) -> (
    Any
    | RevokePermissionsForGroup2Response401
    | RevokePermissionsForGroup2Response404
    | RevokePermissionsForGroup2Response409
    | None
):
    """Revoke group repository permission

     Revoke all permissions for the specified repository for a group.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the specified repository
    or a higher project or global permission to call this resource.

    In addition, a user may not revoke a group's permissions if it will reduce their own permission
    level.

    Args:
        project_key (str):
        repository_slug (str):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RevokePermissionsForGroup2Response401 | RevokePermissionsForGroup2Response404 | RevokePermissionsForGroup2Response409
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            client=client,
            name=name,
        )
    ).parsed
