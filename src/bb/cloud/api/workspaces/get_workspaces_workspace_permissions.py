from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
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
    workspace: str,
    *,
    q: str | Unset = UNSET,
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["q"] = q

    params["page"] = page

    params["pagelen"] = pagelen

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/workspaces/{workspace}/permissions".format(
            workspace=quote(str(workspace), safe=""),
        ),
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
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> Response[ParsedPayload]:
    r"""List user permissions in a workspace

     Returns the list of members in a workspace
    and their permission levels.
    Permission can be:
    * `owner`
    * `collaborator`
    * `member`

    **The `collaborator` role is being removed from the Bitbucket Cloud API. For more information,
    see the [deprecation announcement](/cloud/bitbucket/deprecation-notice-collaborator-role/).**

    **When you move your administration from Bitbucket Cloud to admin.atlassian.com, the following
    fields on
    `workspace_membership` will no longer be present: `last_accessed` and `added_on`. See the
    [deprecation announcement](/cloud/bitbucket/announcement-breaking-change-workspace-membership/).**

    Results may be further [filtered](/cloud/bitbucket/rest/intro/#filtering) by
    permission by adding the following query string parameters:

    * `q=permission=\"owner\"`

    Args:
        workspace (str):
        q (str | Unset):
        page (int | Unset):  Default: 1.
        pagelen (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PaginatedWorkspaceMemberships]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        q=q,
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
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> ParsedPayload | None:
    r"""List user permissions in a workspace

     Returns the list of members in a workspace
    and their permission levels.
    Permission can be:
    * `owner`
    * `collaborator`
    * `member`

    **The `collaborator` role is being removed from the Bitbucket Cloud API. For more information,
    see the [deprecation announcement](/cloud/bitbucket/deprecation-notice-collaborator-role/).**

    **When you move your administration from Bitbucket Cloud to admin.atlassian.com, the following
    fields on
    `workspace_membership` will no longer be present: `last_accessed` and `added_on`. See the
    [deprecation announcement](/cloud/bitbucket/announcement-breaking-change-workspace-membership/).**

    Results may be further [filtered](/cloud/bitbucket/rest/intro/#filtering) by
    permission by adding the following query string parameters:

    * `q=permission=\"owner\"`

    Args:
        workspace (str):
        q (str | Unset):
        page (int | Unset):  Default: 1.
        pagelen (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PaginatedWorkspaceMemberships
    """

    return sync_detailed(
        workspace=workspace,
        client=client,
        q=q,
        page=page,
        pagelen=pagelen,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> Response[ParsedPayload]:
    r"""List user permissions in a workspace

     Returns the list of members in a workspace
    and their permission levels.
    Permission can be:
    * `owner`
    * `collaborator`
    * `member`

    **The `collaborator` role is being removed from the Bitbucket Cloud API. For more information,
    see the [deprecation announcement](/cloud/bitbucket/deprecation-notice-collaborator-role/).**

    **When you move your administration from Bitbucket Cloud to admin.atlassian.com, the following
    fields on
    `workspace_membership` will no longer be present: `last_accessed` and `added_on`. See the
    [deprecation announcement](/cloud/bitbucket/announcement-breaking-change-workspace-membership/).**

    Results may be further [filtered](/cloud/bitbucket/rest/intro/#filtering) by
    permission by adding the following query string parameters:

    * `q=permission=\"owner\"`

    Args:
        workspace (str):
        q (str | Unset):
        page (int | Unset):  Default: 1.
        pagelen (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PaginatedWorkspaceMemberships]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        q=q,
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
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> ParsedPayload | None:
    r"""List user permissions in a workspace

     Returns the list of members in a workspace
    and their permission levels.
    Permission can be:
    * `owner`
    * `collaborator`
    * `member`

    **The `collaborator` role is being removed from the Bitbucket Cloud API. For more information,
    see the [deprecation announcement](/cloud/bitbucket/deprecation-notice-collaborator-role/).**

    **When you move your administration from Bitbucket Cloud to admin.atlassian.com, the following
    fields on
    `workspace_membership` will no longer be present: `last_accessed` and `added_on`. See the
    [deprecation announcement](/cloud/bitbucket/announcement-breaking-change-workspace-membership/).**

    Results may be further [filtered](/cloud/bitbucket/rest/intro/#filtering) by
    permission by adding the following query string parameters:

    * `q=permission=\"owner\"`

    Args:
        workspace (str):
        q (str | Unset):
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
            workspace=workspace,
            client=client,
            q=q,
            page=page,
            pagelen=pagelen,
        )
    ).parsed
