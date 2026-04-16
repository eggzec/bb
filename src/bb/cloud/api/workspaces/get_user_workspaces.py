from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.paginated_workspace_permissions import PaginatedWorkspacePermissions
from ...types import UNSET, Response, Unset

__all__ = [
    "sync_detailed",
    "asyncio_detailed",
    "sync",
    "asyncio",
]


def _get_kwargs(
    *,
    sort: str | Unset = UNSET,
    administrator: bool | Unset = UNSET,
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["sort"] = sort

    params["administrator"] = administrator

    params["page"] = page

    params["pagelen"] = pagelen

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/user/workspaces",
        "params": params,
    }

    return _kwargs


type ParsedPayload = Error | PaginatedWorkspacePermissions
type ParseResult = Error | PaginatedWorkspacePermissions | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        response_200 = PaginatedWorkspacePermissions.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

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
    *,
    client: AuthenticatedClient,
    sort: str | Unset = UNSET,
    administrator: bool | Unset = UNSET,
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> Response[ParsedPayload]:
    r"""List workspaces for the current user

     Returns an object for each workspace accessible to the caller. This object
    also contains details on whether the caller has admin permissions on the workspace
    (`\"administrator\" = true`) or not (`\"administrator\" = false`).

    Queries support filtering based on administrator permissions,
    [sorting](/cloud/bitbucket/rest/intro/#sorting-query-results) or
    [filtering](/cloud/bitbucket/rest/intro/#filtering) by `slug`. Results can
    be [paginated](/cloud/bitbucket/rest/intro/#pagination).

    Args:
        sort (str | Unset):
        administrator (bool | Unset):
        page (int | Unset):  Default: 1.
        pagelen (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PaginatedWorkspacePermissions]
    """

    kwargs = _get_kwargs(
        sort=sort,
        administrator=administrator,
        page=page,
        pagelen=pagelen,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    sort: str | Unset = UNSET,
    administrator: bool | Unset = UNSET,
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> ParsedPayload | None:
    r"""List workspaces for the current user

     Returns an object for each workspace accessible to the caller. This object
    also contains details on whether the caller has admin permissions on the workspace
    (`\"administrator\" = true`) or not (`\"administrator\" = false`).

    Queries support filtering based on administrator permissions,
    [sorting](/cloud/bitbucket/rest/intro/#sorting-query-results) or
    [filtering](/cloud/bitbucket/rest/intro/#filtering) by `slug`. Results can
    be [paginated](/cloud/bitbucket/rest/intro/#pagination).

    Args:
        sort (str | Unset):
        administrator (bool | Unset):
        page (int | Unset):  Default: 1.
        pagelen (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PaginatedWorkspacePermissions
    """

    return sync_detailed(
        client=client,
        sort=sort,
        administrator=administrator,
        page=page,
        pagelen=pagelen,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    sort: str | Unset = UNSET,
    administrator: bool | Unset = UNSET,
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> Response[ParsedPayload]:
    r"""List workspaces for the current user

     Returns an object for each workspace accessible to the caller. This object
    also contains details on whether the caller has admin permissions on the workspace
    (`\"administrator\" = true`) or not (`\"administrator\" = false`).

    Queries support filtering based on administrator permissions,
    [sorting](/cloud/bitbucket/rest/intro/#sorting-query-results) or
    [filtering](/cloud/bitbucket/rest/intro/#filtering) by `slug`. Results can
    be [paginated](/cloud/bitbucket/rest/intro/#pagination).

    Args:
        sort (str | Unset):
        administrator (bool | Unset):
        page (int | Unset):  Default: 1.
        pagelen (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PaginatedWorkspacePermissions]
    """

    kwargs = _get_kwargs(
        sort=sort,
        administrator=administrator,
        page=page,
        pagelen=pagelen,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    sort: str | Unset = UNSET,
    administrator: bool | Unset = UNSET,
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> ParsedPayload | None:
    r"""List workspaces for the current user

     Returns an object for each workspace accessible to the caller. This object
    also contains details on whether the caller has admin permissions on the workspace
    (`\"administrator\" = true`) or not (`\"administrator\" = false`).

    Queries support filtering based on administrator permissions,
    [sorting](/cloud/bitbucket/rest/intro/#sorting-query-results) or
    [filtering](/cloud/bitbucket/rest/intro/#filtering) by `slug`. Results can
    be [paginated](/cloud/bitbucket/rest/intro/#pagination).

    Args:
        sort (str | Unset):
        administrator (bool | Unset):
        page (int | Unset):  Default: 1.
        pagelen (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PaginatedWorkspacePermissions
    """

    return (
        await asyncio_detailed(
            client=client,
            sort=sort,
            administrator=administrator,
            page=page,
            pagelen=pagelen,
        )
    ).parsed
