from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...deprecation import deprecated_endpoint
from ...models.error import Error
from ...models.paginated_workspace_memberships import PaginatedWorkspaceMemberships
from ...types import UNSET, Response, Unset

__all__ = [
    "sync_detailed",
    "asyncio_detailed",
    "sync",
    "asyncio",
]


def _get_kwargs(
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
        "url": "/user/permissions/workspaces",
        "params": params,
    }

    return _kwargs


type ParsedPayload = Error | PaginatedWorkspaceMemberships
type ParseResult = Error | PaginatedWorkspaceMemberships | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_200 = PaginatedWorkspaceMemberships.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 410:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_410 = Error.from_dict(response.json())

        return response_410

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


@deprecated_endpoint(None)
def sync_detailed(
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> Response[ParsedPayload]:
    r"""List workspaces for the current user

     **This endpoint is deprecated. Please use the supported alternatives:**
    * [List workspaces for user](/cloud/bitbucket/rest/api-group-workspaces/#api-user-workspaces-get)
    * [Get user permission on a workspace](/cloud/bitbucket/rest/api-group-workspaces/#api-user-
    workspaces-workspace-permission-get)

    Returns an object for each workspace the caller is a member of, and
    their effective role - the highest level of privilege the caller has.
    If a user is a member of multiple groups with distinct roles, only the
    highest level is returned.

    Permissions can be:

    * `owner`
    * `collaborator`
    * `member`

    **The `collaborator` role is being removed from the Bitbucket Cloud API. For more information,
    see the [deprecation announcement](/cloud/bitbucket/deprecation-notice-collaborator-role/).**

    **When you move your administration from Bitbucket Cloud to admin.atlassian.com, the following
    fields on
    `workspace_membership` will no longer be present: `last_accessed` and `added_on`. See the
    [deprecation announcement](/cloud/bitbucket/announcement-breaking-change-workspace-membership/).**

    Results may be further [filtered or sorted](/cloud/bitbucket/rest/intro/#filtering) by
    workspace or permission by adding the following query string parameters:

    * `q=workspace.slug=\"bbworkspace1\"` or `q=permission=\"owner\"`
    * `sort=workspace.slug`

    Note that the query parameter values need to be URL escaped so that `=`
    would become `%3D`.

    Args:
        q (str | Unset):
        sort (str | Unset):
        page (int | Unset):  Default: 1.
        pagelen (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PaginatedWorkspaceMemberships]
    """

    kwargs = _get_kwargs(
        q=q,
        sort=sort,
        page=page,
        pagelen=pagelen,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated_endpoint(None)
def sync(
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> ParsedPayload | None:
    r"""List workspaces for the current user

     **This endpoint is deprecated. Please use the supported alternatives:**
    * [List workspaces for user](/cloud/bitbucket/rest/api-group-workspaces/#api-user-workspaces-get)
    * [Get user permission on a workspace](/cloud/bitbucket/rest/api-group-workspaces/#api-user-
    workspaces-workspace-permission-get)

    Returns an object for each workspace the caller is a member of, and
    their effective role - the highest level of privilege the caller has.
    If a user is a member of multiple groups with distinct roles, only the
    highest level is returned.

    Permissions can be:

    * `owner`
    * `collaborator`
    * `member`

    **The `collaborator` role is being removed from the Bitbucket Cloud API. For more information,
    see the [deprecation announcement](/cloud/bitbucket/deprecation-notice-collaborator-role/).**

    **When you move your administration from Bitbucket Cloud to admin.atlassian.com, the following
    fields on
    `workspace_membership` will no longer be present: `last_accessed` and `added_on`. See the
    [deprecation announcement](/cloud/bitbucket/announcement-breaking-change-workspace-membership/).**

    Results may be further [filtered or sorted](/cloud/bitbucket/rest/intro/#filtering) by
    workspace or permission by adding the following query string parameters:

    * `q=workspace.slug=\"bbworkspace1\"` or `q=permission=\"owner\"`
    * `sort=workspace.slug`

    Note that the query parameter values need to be URL escaped so that `=`
    would become `%3D`.

    Args:
        q (str | Unset):
        sort (str | Unset):
        page (int | Unset):  Default: 1.
        pagelen (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PaginatedWorkspaceMemberships
    """

    return sync_detailed(
        client=client,
        q=q,
        sort=sort,
        page=page,
        pagelen=pagelen,
    ).parsed


@deprecated_endpoint(None)
async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> Response[ParsedPayload]:
    r"""List workspaces for the current user

     **This endpoint is deprecated. Please use the supported alternatives:**
    * [List workspaces for user](/cloud/bitbucket/rest/api-group-workspaces/#api-user-workspaces-get)
    * [Get user permission on a workspace](/cloud/bitbucket/rest/api-group-workspaces/#api-user-
    workspaces-workspace-permission-get)

    Returns an object for each workspace the caller is a member of, and
    their effective role - the highest level of privilege the caller has.
    If a user is a member of multiple groups with distinct roles, only the
    highest level is returned.

    Permissions can be:

    * `owner`
    * `collaborator`
    * `member`

    **The `collaborator` role is being removed from the Bitbucket Cloud API. For more information,
    see the [deprecation announcement](/cloud/bitbucket/deprecation-notice-collaborator-role/).**

    **When you move your administration from Bitbucket Cloud to admin.atlassian.com, the following
    fields on
    `workspace_membership` will no longer be present: `last_accessed` and `added_on`. See the
    [deprecation announcement](/cloud/bitbucket/announcement-breaking-change-workspace-membership/).**

    Results may be further [filtered or sorted](/cloud/bitbucket/rest/intro/#filtering) by
    workspace or permission by adding the following query string parameters:

    * `q=workspace.slug=\"bbworkspace1\"` or `q=permission=\"owner\"`
    * `sort=workspace.slug`

    Note that the query parameter values need to be URL escaped so that `=`
    would become `%3D`.

    Args:
        q (str | Unset):
        sort (str | Unset):
        page (int | Unset):  Default: 1.
        pagelen (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PaginatedWorkspaceMemberships]
    """

    kwargs = _get_kwargs(
        q=q,
        sort=sort,
        page=page,
        pagelen=pagelen,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated_endpoint(None)
async def asyncio(
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> ParsedPayload | None:
    r"""List workspaces for the current user

     **This endpoint is deprecated. Please use the supported alternatives:**
    * [List workspaces for user](/cloud/bitbucket/rest/api-group-workspaces/#api-user-workspaces-get)
    * [Get user permission on a workspace](/cloud/bitbucket/rest/api-group-workspaces/#api-user-
    workspaces-workspace-permission-get)

    Returns an object for each workspace the caller is a member of, and
    their effective role - the highest level of privilege the caller has.
    If a user is a member of multiple groups with distinct roles, only the
    highest level is returned.

    Permissions can be:

    * `owner`
    * `collaborator`
    * `member`

    **The `collaborator` role is being removed from the Bitbucket Cloud API. For more information,
    see the [deprecation announcement](/cloud/bitbucket/deprecation-notice-collaborator-role/).**

    **When you move your administration from Bitbucket Cloud to admin.atlassian.com, the following
    fields on
    `workspace_membership` will no longer be present: `last_accessed` and `added_on`. See the
    [deprecation announcement](/cloud/bitbucket/announcement-breaking-change-workspace-membership/).**

    Results may be further [filtered or sorted](/cloud/bitbucket/rest/intro/#filtering) by
    workspace or permission by adding the following query string parameters:

    * `q=workspace.slug=\"bbworkspace1\"` or `q=permission=\"owner\"`
    * `sort=workspace.slug`

    Note that the query parameter values need to be URL escaped so that `=`
    would become `%3D`.

    Args:
        q (str | Unset):
        sort (str | Unset):
        page (int | Unset):  Default: 1.
        pagelen (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PaginatedWorkspaceMemberships
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            sort=sort,
            page=page,
            pagelen=pagelen,
        )
    ).parsed
