from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.set_permission_for_user_permission import SetPermissionForUserPermission
from ...models.set_permission_for_user_response_400 import SetPermissionForUserResponse400
from ...models.set_permission_for_user_response_401 import SetPermissionForUserResponse401
from ...models.set_permission_for_user_response_403 import SetPermissionForUserResponse403
from ...models.set_permission_for_user_response_404 import SetPermissionForUserResponse404
from ...types import UNSET, Response


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    *,
    name: list[str],
    permission: SetPermissionForUserPermission,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_name = name

    params["name"] = json_name

    json_permission = permission.value
    params["permission"] = json_permission

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/permissions/users".format(
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
    | SetPermissionForUserResponse400
    | SetPermissionForUserResponse401
    | SetPermissionForUserResponse403
    | SetPermissionForUserResponse404
    | None
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = SetPermissionForUserResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = SetPermissionForUserResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = SetPermissionForUserResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = SetPermissionForUserResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | SetPermissionForUserResponse400
    | SetPermissionForUserResponse401
    | SetPermissionForUserResponse403
    | SetPermissionForUserResponse404
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
    permission: SetPermissionForUserPermission,
) -> Response[
    Any
    | SetPermissionForUserResponse400
    | SetPermissionForUserResponse401
    | SetPermissionForUserResponse403
    | SetPermissionForUserResponse404
]:
    r"""Update user repository permission

     Promote or demote a user's permission level for the specified repository. Available repository
    permissions are:

    - REPO_READ</li>- REPO_WRITE</li>- REPO_ADMIN</li></ul>See the <a href=\"https://confluence.atlassia
    n.com/display/BitbucketServer/Using+repository+permissions\">Bitbucket Data Center documentation</a>
    for a detailed explanation of what each permission entails.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the specified repository
    or a higher project or global permission to call this resource. In addition, a user may not reduce
    their own permission level unless they have a project or global permission that already implies that
    permission.

    Args:
        project_key (str):
        repository_slug (str):
        name (list[str]):
        permission (SetPermissionForUserPermission):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SetPermissionForUserResponse400 | SetPermissionForUserResponse401 | SetPermissionForUserResponse403 | SetPermissionForUserResponse404]
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
    permission: SetPermissionForUserPermission,
) -> (
    Any
    | SetPermissionForUserResponse400
    | SetPermissionForUserResponse401
    | SetPermissionForUserResponse403
    | SetPermissionForUserResponse404
    | None
):
    r"""Update user repository permission

     Promote or demote a user's permission level for the specified repository. Available repository
    permissions are:

    - REPO_READ</li>- REPO_WRITE</li>- REPO_ADMIN</li></ul>See the <a href=\"https://confluence.atlassia
    n.com/display/BitbucketServer/Using+repository+permissions\">Bitbucket Data Center documentation</a>
    for a detailed explanation of what each permission entails.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the specified repository
    or a higher project or global permission to call this resource. In addition, a user may not reduce
    their own permission level unless they have a project or global permission that already implies that
    permission.

    Args:
        project_key (str):
        repository_slug (str):
        name (list[str]):
        permission (SetPermissionForUserPermission):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SetPermissionForUserResponse400 | SetPermissionForUserResponse401 | SetPermissionForUserResponse403 | SetPermissionForUserResponse404
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
    permission: SetPermissionForUserPermission,
) -> Response[
    Any
    | SetPermissionForUserResponse400
    | SetPermissionForUserResponse401
    | SetPermissionForUserResponse403
    | SetPermissionForUserResponse404
]:
    r"""Update user repository permission

     Promote or demote a user's permission level for the specified repository. Available repository
    permissions are:

    - REPO_READ</li>- REPO_WRITE</li>- REPO_ADMIN</li></ul>See the <a href=\"https://confluence.atlassia
    n.com/display/BitbucketServer/Using+repository+permissions\">Bitbucket Data Center documentation</a>
    for a detailed explanation of what each permission entails.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the specified repository
    or a higher project or global permission to call this resource. In addition, a user may not reduce
    their own permission level unless they have a project or global permission that already implies that
    permission.

    Args:
        project_key (str):
        repository_slug (str):
        name (list[str]):
        permission (SetPermissionForUserPermission):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SetPermissionForUserResponse400 | SetPermissionForUserResponse401 | SetPermissionForUserResponse403 | SetPermissionForUserResponse404]
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
    permission: SetPermissionForUserPermission,
) -> (
    Any
    | SetPermissionForUserResponse400
    | SetPermissionForUserResponse401
    | SetPermissionForUserResponse403
    | SetPermissionForUserResponse404
    | None
):
    r"""Update user repository permission

     Promote or demote a user's permission level for the specified repository. Available repository
    permissions are:

    - REPO_READ</li>- REPO_WRITE</li>- REPO_ADMIN</li></ul>See the <a href=\"https://confluence.atlassia
    n.com/display/BitbucketServer/Using+repository+permissions\">Bitbucket Data Center documentation</a>
    for a detailed explanation of what each permission entails.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the specified repository
    or a higher project or global permission to call this resource. In addition, a user may not reduce
    their own permission level unless they have a project or global permission that already implies that
    permission.

    Args:
        project_key (str):
        repository_slug (str):
        name (list[str]):
        permission (SetPermissionForUserPermission):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SetPermissionForUserResponse400 | SetPermissionForUserResponse401 | SetPermissionForUserResponse403 | SetPermissionForUserResponse404
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
