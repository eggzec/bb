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
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["pagelen"] = pagelen

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/workspaces/{workspace}/members".format(
            workspace=quote(str(workspace), safe=""),
        ),
        "params": params,
    }

    return _kwargs


type ParsedPayload = Error | PaginatedWorkspaceMemberships
type ParseResult = Error | PaginatedWorkspaceMemberships | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        response_200 = PaginatedWorkspaceMemberships.from_dict(response.json())

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
    workspace: str,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> Response[ParsedPayload]:
    r"""List users in a workspace

     Returns all members of the requested workspace.

    This endpoint additionally supports [filtering](/cloud/bitbucket/rest/intro/#filtering) by
    email address, if called by a workspace administrator, integration or workspace access
    token. This is done by adding the following query string parameter:

    * `q=user.email IN (\"user1@org.com\",\"user2@org.com\")`

    When filtering by email, you can query up to 90 addresses at a time.
    Note that the query parameter values need to be URL escaped, so the final query string
    should be:

    * `q=user.email%20IN%20(%22user1@org.com%22,%22user2@org.com%22)`

    Email addresses that you filter by (and only these email addresses) can be included in the
    response using the `fields` query parameter:

    * `&fields=+values.user.email` - add the `email` field to the default `user` response object
    * `&fields=values.user.email,values.user.account_id` - only return user email addresses and
    account IDs

    Once again, all query parameter values must be URL escaped.

    Args:
        workspace (str):
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
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> ParsedPayload | None:
    r"""List users in a workspace

     Returns all members of the requested workspace.

    This endpoint additionally supports [filtering](/cloud/bitbucket/rest/intro/#filtering) by
    email address, if called by a workspace administrator, integration or workspace access
    token. This is done by adding the following query string parameter:

    * `q=user.email IN (\"user1@org.com\",\"user2@org.com\")`

    When filtering by email, you can query up to 90 addresses at a time.
    Note that the query parameter values need to be URL escaped, so the final query string
    should be:

    * `q=user.email%20IN%20(%22user1@org.com%22,%22user2@org.com%22)`

    Email addresses that you filter by (and only these email addresses) can be included in the
    response using the `fields` query parameter:

    * `&fields=+values.user.email` - add the `email` field to the default `user` response object
    * `&fields=values.user.email,values.user.account_id` - only return user email addresses and
    account IDs

    Once again, all query parameter values must be URL escaped.

    Args:
        workspace (str):
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
        page=page,
        pagelen=pagelen,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> Response[ParsedPayload]:
    r"""List users in a workspace

     Returns all members of the requested workspace.

    This endpoint additionally supports [filtering](/cloud/bitbucket/rest/intro/#filtering) by
    email address, if called by a workspace administrator, integration or workspace access
    token. This is done by adding the following query string parameter:

    * `q=user.email IN (\"user1@org.com\",\"user2@org.com\")`

    When filtering by email, you can query up to 90 addresses at a time.
    Note that the query parameter values need to be URL escaped, so the final query string
    should be:

    * `q=user.email%20IN%20(%22user1@org.com%22,%22user2@org.com%22)`

    Email addresses that you filter by (and only these email addresses) can be included in the
    response using the `fields` query parameter:

    * `&fields=+values.user.email` - add the `email` field to the default `user` response object
    * `&fields=values.user.email,values.user.account_id` - only return user email addresses and
    account IDs

    Once again, all query parameter values must be URL escaped.

    Args:
        workspace (str):
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
        page=page,
        pagelen=pagelen,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> ParsedPayload | None:
    r"""List users in a workspace

     Returns all members of the requested workspace.

    This endpoint additionally supports [filtering](/cloud/bitbucket/rest/intro/#filtering) by
    email address, if called by a workspace administrator, integration or workspace access
    token. This is done by adding the following query string parameter:

    * `q=user.email IN (\"user1@org.com\",\"user2@org.com\")`

    When filtering by email, you can query up to 90 addresses at a time.
    Note that the query parameter values need to be URL escaped, so the final query string
    should be:

    * `q=user.email%20IN%20(%22user1@org.com%22,%22user2@org.com%22)`

    Email addresses that you filter by (and only these email addresses) can be included in the
    response using the `fields` query parameter:

    * `&fields=+values.user.email` - add the `email` field to the default `user` response object
    * `&fields=values.user.email,values.user.account_id` - only return user email addresses and
    account IDs

    Once again, all query parameter values must be URL escaped.

    Args:
        workspace (str):
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
            page=page,
            pagelen=pagelen,
        )
    ).parsed
