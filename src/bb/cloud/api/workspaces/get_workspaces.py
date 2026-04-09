from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...deprecation import deprecated_endpoint
from ...models.error import Error
from ...models.get_workspaces_role import GetWorkspacesRole
from ...models.paginated_workspaces import PaginatedWorkspaces
from ...types import UNSET, Response, Unset

__all__ = [
    "sync_detailed",
    "asyncio_detailed",
    "sync",
    "asyncio",
]


def _get_kwargs(
    *,
    role: GetWorkspacesRole | Unset = UNSET,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_role: str | Unset = UNSET
    if not isinstance(role, Unset):
        json_role = role.value

    params["role"] = json_role

    params["q"] = q

    params["sort"] = sort

    params["page"] = page

    params["pagelen"] = pagelen

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/workspaces",
        "params": params,
    }

    return _kwargs


type ParsedPayload = Error | PaginatedWorkspaces
type ParseResult = Error | PaginatedWorkspaces | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        response_200 = PaginatedWorkspaces.from_dict(response.json())

        return response_200

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


@deprecated_endpoint(None)
def sync_detailed(
    *,
    client: AuthenticatedClient,
    role: GetWorkspacesRole | Unset = UNSET,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> Response[ParsedPayload]:
    r"""List workspaces for user

     **This endpoint is deprecated. Please use the
    [supported alternative](/cloud/bitbucket/rest/api-group-workspaces/#api-user-workspaces-get).**

    Returns a list of workspaces accessible by the authenticated user.

    Results may be further [filtered or sorted](/cloud/bitbucket/rest/intro/#filtering) by
    workspace or permission by adding the following query string parameters:

    * `q=slug=\"bbworkspace1\"` or `q=is_private=true`
    * `sort=created_on`

    Note that the query parameter values need to be URL escaped so that `=`
    would become `%3D`.

    **The `collaborator` role is being removed from the Bitbucket Cloud API. For more information,
    see the [deprecation announcement](/cloud/bitbucket/deprecation-notice-collaborator-role/).**

    Args:
        role (GetWorkspacesRole | Unset):
        q (str | Unset):
        sort (str | Unset):
        page (int | Unset):  Default: 1.
        pagelen (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PaginatedWorkspaces]
    """

    kwargs = _get_kwargs(
        role=role,
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
    role: GetWorkspacesRole | Unset = UNSET,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> ParsedPayload | None:
    r"""List workspaces for user

     **This endpoint is deprecated. Please use the
    [supported alternative](/cloud/bitbucket/rest/api-group-workspaces/#api-user-workspaces-get).**

    Returns a list of workspaces accessible by the authenticated user.

    Results may be further [filtered or sorted](/cloud/bitbucket/rest/intro/#filtering) by
    workspace or permission by adding the following query string parameters:

    * `q=slug=\"bbworkspace1\"` or `q=is_private=true`
    * `sort=created_on`

    Note that the query parameter values need to be URL escaped so that `=`
    would become `%3D`.

    **The `collaborator` role is being removed from the Bitbucket Cloud API. For more information,
    see the [deprecation announcement](/cloud/bitbucket/deprecation-notice-collaborator-role/).**

    Args:
        role (GetWorkspacesRole | Unset):
        q (str | Unset):
        sort (str | Unset):
        page (int | Unset):  Default: 1.
        pagelen (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PaginatedWorkspaces
    """

    return sync_detailed(
        client=client,
        role=role,
        q=q,
        sort=sort,
        page=page,
        pagelen=pagelen,
    ).parsed


@deprecated_endpoint(None)
async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    role: GetWorkspacesRole | Unset = UNSET,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> Response[ParsedPayload]:
    r"""List workspaces for user

     **This endpoint is deprecated. Please use the
    [supported alternative](/cloud/bitbucket/rest/api-group-workspaces/#api-user-workspaces-get).**

    Returns a list of workspaces accessible by the authenticated user.

    Results may be further [filtered or sorted](/cloud/bitbucket/rest/intro/#filtering) by
    workspace or permission by adding the following query string parameters:

    * `q=slug=\"bbworkspace1\"` or `q=is_private=true`
    * `sort=created_on`

    Note that the query parameter values need to be URL escaped so that `=`
    would become `%3D`.

    **The `collaborator` role is being removed from the Bitbucket Cloud API. For more information,
    see the [deprecation announcement](/cloud/bitbucket/deprecation-notice-collaborator-role/).**

    Args:
        role (GetWorkspacesRole | Unset):
        q (str | Unset):
        sort (str | Unset):
        page (int | Unset):  Default: 1.
        pagelen (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PaginatedWorkspaces]
    """

    kwargs = _get_kwargs(
        role=role,
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
    role: GetWorkspacesRole | Unset = UNSET,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> ParsedPayload | None:
    r"""List workspaces for user

     **This endpoint is deprecated. Please use the
    [supported alternative](/cloud/bitbucket/rest/api-group-workspaces/#api-user-workspaces-get).**

    Returns a list of workspaces accessible by the authenticated user.

    Results may be further [filtered or sorted](/cloud/bitbucket/rest/intro/#filtering) by
    workspace or permission by adding the following query string parameters:

    * `q=slug=\"bbworkspace1\"` or `q=is_private=true`
    * `sort=created_on`

    Note that the query parameter values need to be URL escaped so that `=`
    would become `%3D`.

    **The `collaborator` role is being removed from the Bitbucket Cloud API. For more information,
    see the [deprecation announcement](/cloud/bitbucket/deprecation-notice-collaborator-role/).**

    Args:
        role (GetWorkspacesRole | Unset):
        q (str | Unset):
        sort (str | Unset):
        page (int | Unset):  Default: 1.
        pagelen (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PaginatedWorkspaces
    """

    return (
        await asyncio_detailed(
            client=client,
            role=role,
            q=q,
            sort=sort,
            page=page,
            pagelen=pagelen,
        )
    ).parsed
