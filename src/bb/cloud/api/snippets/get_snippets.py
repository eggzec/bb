from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...deprecation import deprecated_endpoint
from ...models.error import Error
from ...models.get_snippets_role import GetSnippetsRole
from ...models.paginated_snippets import PaginatedSnippets
from ...types import UNSET, Response, Unset

__all__ = [
    "sync_detailed",
    "asyncio_detailed",
    "sync",
    "asyncio",
]


def _get_kwargs(
    *,
    role: GetSnippetsRole | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_role: str | Unset = UNSET
    if not isinstance(role, Unset):
        json_role = role.value

    params["role"] = json_role

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/snippets",
        "params": params,
    }

    return _kwargs


type ParsedPayload = Error | PaginatedSnippets
type ParseResult = Error | PaginatedSnippets | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        response_200 = PaginatedSnippets.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

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
    role: GetSnippetsRole | Unset = UNSET,
) -> Response[ParsedPayload]:
    """List snippets

     **This endpoint is deprecated. Please use the
    [workspace scoped alternative](/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-
    get).**

    Returns all snippets. Like pull requests, repositories and workspaces, the
    full set of snippets is defined by what the current user has access to.

    This includes all snippets owned by any of the workspaces the user is a member of,
    or snippets by other users that the current user is either watching or has collaborated
    on (for instance by commenting on it).

    To limit the set of returned snippets, apply the
    `?role=[owner|contributor|member]` query parameter where the roles are
    defined as follows:

    * `owner`: all snippets owned by the current user
    * `contributor`: all snippets owned by, or watched by the current user
    * `member`: created in a workspaces or watched by the current user

    When no role is specified, all public snippets are returned, as well as all
    privately owned snippets watched or commented on.

    The returned response is a normal paginated JSON list. This endpoint
    only supports `application/json` responses and no
    `multipart/form-data` or `multipart/related`. As a result, it is not
    possible to include the file contents.

    Args:
        role (GetSnippetsRole | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PaginatedSnippets]
    """

    kwargs = _get_kwargs(
        role=role,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated_endpoint(None)
def sync(
    *,
    client: AuthenticatedClient,
    role: GetSnippetsRole | Unset = UNSET,
) -> ParsedPayload | None:
    """List snippets

     **This endpoint is deprecated. Please use the
    [workspace scoped alternative](/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-
    get).**

    Returns all snippets. Like pull requests, repositories and workspaces, the
    full set of snippets is defined by what the current user has access to.

    This includes all snippets owned by any of the workspaces the user is a member of,
    or snippets by other users that the current user is either watching or has collaborated
    on (for instance by commenting on it).

    To limit the set of returned snippets, apply the
    `?role=[owner|contributor|member]` query parameter where the roles are
    defined as follows:

    * `owner`: all snippets owned by the current user
    * `contributor`: all snippets owned by, or watched by the current user
    * `member`: created in a workspaces or watched by the current user

    When no role is specified, all public snippets are returned, as well as all
    privately owned snippets watched or commented on.

    The returned response is a normal paginated JSON list. This endpoint
    only supports `application/json` responses and no
    `multipart/form-data` or `multipart/related`. As a result, it is not
    possible to include the file contents.

    Args:
        role (GetSnippetsRole | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PaginatedSnippets
    """

    return sync_detailed(
        client=client,
        role=role,
    ).parsed


@deprecated_endpoint(None)
async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    role: GetSnippetsRole | Unset = UNSET,
) -> Response[ParsedPayload]:
    """List snippets

     **This endpoint is deprecated. Please use the
    [workspace scoped alternative](/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-
    get).**

    Returns all snippets. Like pull requests, repositories and workspaces, the
    full set of snippets is defined by what the current user has access to.

    This includes all snippets owned by any of the workspaces the user is a member of,
    or snippets by other users that the current user is either watching or has collaborated
    on (for instance by commenting on it).

    To limit the set of returned snippets, apply the
    `?role=[owner|contributor|member]` query parameter where the roles are
    defined as follows:

    * `owner`: all snippets owned by the current user
    * `contributor`: all snippets owned by, or watched by the current user
    * `member`: created in a workspaces or watched by the current user

    When no role is specified, all public snippets are returned, as well as all
    privately owned snippets watched or commented on.

    The returned response is a normal paginated JSON list. This endpoint
    only supports `application/json` responses and no
    `multipart/form-data` or `multipart/related`. As a result, it is not
    possible to include the file contents.

    Args:
        role (GetSnippetsRole | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PaginatedSnippets]
    """

    kwargs = _get_kwargs(
        role=role,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated_endpoint(None)
async def asyncio(
    *,
    client: AuthenticatedClient,
    role: GetSnippetsRole | Unset = UNSET,
) -> ParsedPayload | None:
    """List snippets

     **This endpoint is deprecated. Please use the
    [workspace scoped alternative](/cloud/bitbucket/rest/api-group-snippets/#api-snippets-workspace-
    get).**

    Returns all snippets. Like pull requests, repositories and workspaces, the
    full set of snippets is defined by what the current user has access to.

    This includes all snippets owned by any of the workspaces the user is a member of,
    or snippets by other users that the current user is either watching or has collaborated
    on (for instance by commenting on it).

    To limit the set of returned snippets, apply the
    `?role=[owner|contributor|member]` query parameter where the roles are
    defined as follows:

    * `owner`: all snippets owned by the current user
    * `contributor`: all snippets owned by, or watched by the current user
    * `member`: created in a workspaces or watched by the current user

    When no role is specified, all public snippets are returned, as well as all
    privately owned snippets watched or commented on.

    The returned response is a normal paginated JSON list. This endpoint
    only supports `application/json` responses and no
    `multipart/form-data` or `multipart/related`. As a result, it is not
    possible to include the file contents.

    Args:
        role (GetSnippetsRole | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PaginatedSnippets
    """

    return (
        await asyncio_detailed(
            client=client,
            role=role,
        )
    ).parsed
