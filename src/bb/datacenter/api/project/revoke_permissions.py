from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.revoke_permissions_response_401 import RevokePermissionsResponse401
from ...models.revoke_permissions_response_404 import RevokePermissionsResponse404
from ...models.revoke_permissions_response_409 import RevokePermissionsResponse409
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    *,
    user: str | Unset = UNSET,
    group: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["user"] = user

    params["group"] = group

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/latest/projects/{project_key}/permissions".format(
            project_key=quote(str(project_key), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RevokePermissionsResponse401 | RevokePermissionsResponse404 | RevokePermissionsResponse409 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = RevokePermissionsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = RevokePermissionsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = RevokePermissionsResponse409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RevokePermissionsResponse401 | RevokePermissionsResponse404 | RevokePermissionsResponse409]:
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
    user: str | Unset = UNSET,
    group: str | Unset = UNSET,
) -> Response[Any | RevokePermissionsResponse401 | RevokePermissionsResponse404 | RevokePermissionsResponse409]:
    """Revoke project permissions

     Revoke all permissions for the specified project for the given groups and users.

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the specified project
    or a higher global permission to call this resource.

    In addition, a user may not revoke a group's permission if their own permission would be revoked as
    a result, nor may they revoke their own permission unless they have a global permission that already
    implies that permission.

    Args:
        project_key (str):
        user (str | Unset):
        group (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RevokePermissionsResponse401 | RevokePermissionsResponse404 | RevokePermissionsResponse409]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        user=user,
        group=group,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    user: str | Unset = UNSET,
    group: str | Unset = UNSET,
) -> Any | RevokePermissionsResponse401 | RevokePermissionsResponse404 | RevokePermissionsResponse409 | None:
    """Revoke project permissions

     Revoke all permissions for the specified project for the given groups and users.

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the specified project
    or a higher global permission to call this resource.

    In addition, a user may not revoke a group's permission if their own permission would be revoked as
    a result, nor may they revoke their own permission unless they have a global permission that already
    implies that permission.

    Args:
        project_key (str):
        user (str | Unset):
        group (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RevokePermissionsResponse401 | RevokePermissionsResponse404 | RevokePermissionsResponse409
    """

    return sync_detailed(
        project_key=project_key,
        client=client,
        user=user,
        group=group,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    user: str | Unset = UNSET,
    group: str | Unset = UNSET,
) -> Response[Any | RevokePermissionsResponse401 | RevokePermissionsResponse404 | RevokePermissionsResponse409]:
    """Revoke project permissions

     Revoke all permissions for the specified project for the given groups and users.

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the specified project
    or a higher global permission to call this resource.

    In addition, a user may not revoke a group's permission if their own permission would be revoked as
    a result, nor may they revoke their own permission unless they have a global permission that already
    implies that permission.

    Args:
        project_key (str):
        user (str | Unset):
        group (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RevokePermissionsResponse401 | RevokePermissionsResponse404 | RevokePermissionsResponse409]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        user=user,
        group=group,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    user: str | Unset = UNSET,
    group: str | Unset = UNSET,
) -> Any | RevokePermissionsResponse401 | RevokePermissionsResponse404 | RevokePermissionsResponse409 | None:
    """Revoke project permissions

     Revoke all permissions for the specified project for the given groups and users.

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the specified project
    or a higher global permission to call this resource.

    In addition, a user may not revoke a group's permission if their own permission would be revoked as
    a result, nor may they revoke their own permission unless they have a global permission that already
    implies that permission.

    Args:
        project_key (str):
        user (str | Unset):
        group (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RevokePermissionsResponse401 | RevokePermissionsResponse404 | RevokePermissionsResponse409
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            client=client,
            user=user,
            group=group,
        )
    ).parsed
