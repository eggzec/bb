from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.paginated_repository_permissions import PaginatedRepositoryPermissions
from ...types import UNSET, Response, Unset

__all__ = [
    "sync_detailed",
    "asyncio_detailed",
    "sync",
    "asyncio",
]


def _get_kwargs(
    workspace: str,
    *,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["q"] = q

    params["sort"] = sort

    params["page"] = page

    params["pagelen"] = pagelen

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/workspaces/{workspace}/permissions/repositories".format(
            workspace=quote(str(workspace), safe=""),
        ),
        "params": params,
    }

    return _kwargs


type ParsedPayload = Error | PaginatedRepositoryPermissions
type ParseResult = Error | PaginatedRepositoryPermissions | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        response_200 = PaginatedRepositoryPermissions.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

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
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> Response[ParsedPayload]:
    r"""List all repository permissions for a workspace

     Returns an object for each repository permission for all of a
    workspace's repositories.

    Permissions returned are effective permissions: the highest level of
    permission the user has. This does not distinguish between direct and
    indirect (group) privileges.

    Only users with admin permission for the team may access this resource.

    Permissions can be:

    * `admin`
    * `write`
    * `read`

    Results may be further [filtered or sorted](/cloud/bitbucket/rest/intro/#filtering)
    by repository, user, or permission by adding the following query string
    parameters:

    * `q=repository.name=\"geordi\"` or `q=permission>\"read\"`
    * `sort=user.display_name`

    Note that the query parameter values need to be URL escaped so that `=`
    would become `%3D`.

    Args:
        workspace (str):
        q (str | Unset):
        sort (str | Unset):
        page (int | Unset):  Default: 1.
        pagelen (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PaginatedRepositoryPermissions]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        q=q,
        sort=sort,
        page=page,
        pagelen=pagelen,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> ParsedPayload | None:
    r"""List all repository permissions for a workspace

     Returns an object for each repository permission for all of a
    workspace's repositories.

    Permissions returned are effective permissions: the highest level of
    permission the user has. This does not distinguish between direct and
    indirect (group) privileges.

    Only users with admin permission for the team may access this resource.

    Permissions can be:

    * `admin`
    * `write`
    * `read`

    Results may be further [filtered or sorted](/cloud/bitbucket/rest/intro/#filtering)
    by repository, user, or permission by adding the following query string
    parameters:

    * `q=repository.name=\"geordi\"` or `q=permission>\"read\"`
    * `sort=user.display_name`

    Note that the query parameter values need to be URL escaped so that `=`
    would become `%3D`.

    Args:
        workspace (str):
        q (str | Unset):
        sort (str | Unset):
        page (int | Unset):  Default: 1.
        pagelen (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PaginatedRepositoryPermissions
    """

    return sync_detailed(
        workspace=workspace,
        client=client,
        q=q,
        sort=sort,
        page=page,
        pagelen=pagelen,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> Response[ParsedPayload]:
    r"""List all repository permissions for a workspace

     Returns an object for each repository permission for all of a
    workspace's repositories.

    Permissions returned are effective permissions: the highest level of
    permission the user has. This does not distinguish between direct and
    indirect (group) privileges.

    Only users with admin permission for the team may access this resource.

    Permissions can be:

    * `admin`
    * `write`
    * `read`

    Results may be further [filtered or sorted](/cloud/bitbucket/rest/intro/#filtering)
    by repository, user, or permission by adding the following query string
    parameters:

    * `q=repository.name=\"geordi\"` or `q=permission>\"read\"`
    * `sort=user.display_name`

    Note that the query parameter values need to be URL escaped so that `=`
    would become `%3D`.

    Args:
        workspace (str):
        q (str | Unset):
        sort (str | Unset):
        page (int | Unset):  Default: 1.
        pagelen (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PaginatedRepositoryPermissions]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        q=q,
        sort=sort,
        page=page,
        pagelen=pagelen,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> ParsedPayload | None:
    r"""List all repository permissions for a workspace

     Returns an object for each repository permission for all of a
    workspace's repositories.

    Permissions returned are effective permissions: the highest level of
    permission the user has. This does not distinguish between direct and
    indirect (group) privileges.

    Only users with admin permission for the team may access this resource.

    Permissions can be:

    * `admin`
    * `write`
    * `read`

    Results may be further [filtered or sorted](/cloud/bitbucket/rest/intro/#filtering)
    by repository, user, or permission by adding the following query string
    parameters:

    * `q=repository.name=\"geordi\"` or `q=permission>\"read\"`
    * `sort=user.display_name`

    Note that the query parameter values need to be URL escaped so that `=`
    would become `%3D`.

    Args:
        workspace (str):
        q (str | Unset):
        sort (str | Unset):
        page (int | Unset):  Default: 1.
        pagelen (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PaginatedRepositoryPermissions
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            client=client,
            q=q,
            sort=sort,
            page=page,
            pagelen=pagelen,
        )
    ).parsed
