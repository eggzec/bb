from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.set_permission_for_group_permission import SetPermissionForGroupPermission
from ...models.set_permission_for_group_response_400 import SetPermissionForGroupResponse400
from ...models.set_permission_for_group_response_401 import SetPermissionForGroupResponse401
from ...models.set_permission_for_group_response_403 import SetPermissionForGroupResponse403
from ...models.set_permission_for_group_response_404 import SetPermissionForGroupResponse404
from ...types import UNSET, Response


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    *,
    name: list[str],
    permission: SetPermissionForGroupPermission,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_name = name

    params["name"] = json_name

    json_permission = permission.value
    params["permission"] = json_permission

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
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
    | SetPermissionForGroupResponse400
    | SetPermissionForGroupResponse401
    | SetPermissionForGroupResponse403
    | SetPermissionForGroupResponse404
    | None
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = SetPermissionForGroupResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = SetPermissionForGroupResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = SetPermissionForGroupResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = SetPermissionForGroupResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | SetPermissionForGroupResponse400
    | SetPermissionForGroupResponse401
    | SetPermissionForGroupResponse403
    | SetPermissionForGroupResponse404
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
    name: list[str],
    permission: SetPermissionForGroupPermission,
) -> Response[
    Any
    | SetPermissionForGroupResponse400
    | SetPermissionForGroupResponse401
    | SetPermissionForGroupResponse403
    | SetPermissionForGroupResponse404
]:
    r"""Update group repository permission

     Promote or demote a group's permission level for the specified repository. Available repository
    permissions are:

    - REPO_READ
    - REPO_WRITE
    - REPO_ADMIN


    See the <a href=\"https://confluence.atlassian.com/display/BitbucketServer/Using+repository+permissi
    ons\">Bitbucket Data Center documentation</a> for a detailed explanation of what each permission
    entails.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the specified repository
    or a higher project or global permission to call this resource. In addition, a user may not demote a
    group's permission level if their own permission level would be reduced as a result.

    Args:
        project_key (str):
        repository_slug (str):
        name (list[str]):
        permission (SetPermissionForGroupPermission):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SetPermissionForGroupResponse400 | SetPermissionForGroupResponse401 | SetPermissionForGroupResponse403 | SetPermissionForGroupResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        name=name,
        permission=permission,
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
    name: list[str],
    permission: SetPermissionForGroupPermission,
) -> (
    Any
    | SetPermissionForGroupResponse400
    | SetPermissionForGroupResponse401
    | SetPermissionForGroupResponse403
    | SetPermissionForGroupResponse404
    | None
):
    r"""Update group repository permission

     Promote or demote a group's permission level for the specified repository. Available repository
    permissions are:

    - REPO_READ
    - REPO_WRITE
    - REPO_ADMIN


    See the <a href=\"https://confluence.atlassian.com/display/BitbucketServer/Using+repository+permissi
    ons\">Bitbucket Data Center documentation</a> for a detailed explanation of what each permission
    entails.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the specified repository
    or a higher project or global permission to call this resource. In addition, a user may not demote a
    group's permission level if their own permission level would be reduced as a result.

    Args:
        project_key (str):
        repository_slug (str):
        name (list[str]):
        permission (SetPermissionForGroupPermission):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SetPermissionForGroupResponse400 | SetPermissionForGroupResponse401 | SetPermissionForGroupResponse403 | SetPermissionForGroupResponse404
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        client=client,
        name=name,
        permission=permission,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    name: list[str],
    permission: SetPermissionForGroupPermission,
) -> Response[
    Any
    | SetPermissionForGroupResponse400
    | SetPermissionForGroupResponse401
    | SetPermissionForGroupResponse403
    | SetPermissionForGroupResponse404
]:
    r"""Update group repository permission

     Promote or demote a group's permission level for the specified repository. Available repository
    permissions are:

    - REPO_READ
    - REPO_WRITE
    - REPO_ADMIN


    See the <a href=\"https://confluence.atlassian.com/display/BitbucketServer/Using+repository+permissi
    ons\">Bitbucket Data Center documentation</a> for a detailed explanation of what each permission
    entails.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the specified repository
    or a higher project or global permission to call this resource. In addition, a user may not demote a
    group's permission level if their own permission level would be reduced as a result.

    Args:
        project_key (str):
        repository_slug (str):
        name (list[str]):
        permission (SetPermissionForGroupPermission):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SetPermissionForGroupResponse400 | SetPermissionForGroupResponse401 | SetPermissionForGroupResponse403 | SetPermissionForGroupResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        name=name,
        permission=permission,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    name: list[str],
    permission: SetPermissionForGroupPermission,
) -> (
    Any
    | SetPermissionForGroupResponse400
    | SetPermissionForGroupResponse401
    | SetPermissionForGroupResponse403
    | SetPermissionForGroupResponse404
    | None
):
    r"""Update group repository permission

     Promote or demote a group's permission level for the specified repository. Available repository
    permissions are:

    - REPO_READ
    - REPO_WRITE
    - REPO_ADMIN


    See the <a href=\"https://confluence.atlassian.com/display/BitbucketServer/Using+repository+permissi
    ons\">Bitbucket Data Center documentation</a> for a detailed explanation of what each permission
    entails.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the specified repository
    or a higher project or global permission to call this resource. In addition, a user may not demote a
    group's permission level if their own permission level would be reduced as a result.

    Args:
        project_key (str):
        repository_slug (str):
        name (list[str]):
        permission (SetPermissionForGroupPermission):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SetPermissionForGroupResponse400 | SetPermissionForGroupResponse401 | SetPermissionForGroupResponse403 | SetPermissionForGroupResponse404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            client=client,
            name=name,
            permission=permission,
        )
    ).parsed
