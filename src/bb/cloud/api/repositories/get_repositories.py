from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...deprecation import deprecated_endpoint
from ...models.get_repositories_role import GetRepositoriesRole
from ...models.paginated_repositories import PaginatedRepositories
from ...types import UNSET, Response, Unset

__all__ = [
    "sync_detailed",
    "asyncio_detailed",
    "sync",
    "asyncio",
]


def _get_kwargs(
    *,
    after: str | Unset = UNSET,
    role: GetRepositoriesRole | Unset = UNSET,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["after"] = after

    json_role: str | Unset = UNSET
    if not isinstance(role, Unset):
        json_role = role.value

    params["role"] = json_role

    params["q"] = q

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/repositories",
        "params": params,
    }

    return _kwargs


type ParsedPayload = PaginatedRepositories
type ParseResult = PaginatedRepositories | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        response_200 = PaginatedRepositories.from_dict(response.json())

        return response_200

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
    after: str | Unset = UNSET,
    role: GetRepositoriesRole | Unset = UNSET,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Response[ParsedPayload]:
    """List public repositories

     **This endpoint is deprecated. Please use the
    [workspace scoped alternative](/cloud/bitbucket/rest/api-group-repositories/#api-repositories-
    workspace-get).**

    Returns a paginated list of all public repositories.

    This endpoint also supports filtering and sorting of the results. See
    [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for more details.

    Args:
        after (str | Unset):
        role (GetRepositoriesRole | Unset):
        q (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedRepositories]
    """

    kwargs = _get_kwargs(
        after=after,
        role=role,
        q=q,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated_endpoint(None)
def sync(
    *,
    client: AuthenticatedClient,
    after: str | Unset = UNSET,
    role: GetRepositoriesRole | Unset = UNSET,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> ParsedPayload | None:
    """List public repositories

     **This endpoint is deprecated. Please use the
    [workspace scoped alternative](/cloud/bitbucket/rest/api-group-repositories/#api-repositories-
    workspace-get).**

    Returns a paginated list of all public repositories.

    This endpoint also supports filtering and sorting of the results. See
    [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for more details.

    Args:
        after (str | Unset):
        role (GetRepositoriesRole | Unset):
        q (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedRepositories
    """

    return sync_detailed(
        client=client,
        after=after,
        role=role,
        q=q,
        sort=sort,
    ).parsed


@deprecated_endpoint(None)
async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    after: str | Unset = UNSET,
    role: GetRepositoriesRole | Unset = UNSET,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Response[ParsedPayload]:
    """List public repositories

     **This endpoint is deprecated. Please use the
    [workspace scoped alternative](/cloud/bitbucket/rest/api-group-repositories/#api-repositories-
    workspace-get).**

    Returns a paginated list of all public repositories.

    This endpoint also supports filtering and sorting of the results. See
    [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for more details.

    Args:
        after (str | Unset):
        role (GetRepositoriesRole | Unset):
        q (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedRepositories]
    """

    kwargs = _get_kwargs(
        after=after,
        role=role,
        q=q,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated_endpoint(None)
async def asyncio(
    *,
    client: AuthenticatedClient,
    after: str | Unset = UNSET,
    role: GetRepositoriesRole | Unset = UNSET,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> ParsedPayload | None:
    """List public repositories

     **This endpoint is deprecated. Please use the
    [workspace scoped alternative](/cloud/bitbucket/rest/api-group-repositories/#api-repositories-
    workspace-get).**

    Returns a paginated list of all public repositories.

    This endpoint also supports filtering and sorting of the results. See
    [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for more details.

    Args:
        after (str | Unset):
        role (GetRepositoriesRole | Unset):
        q (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedRepositories
    """

    return (
        await asyncio_detailed(
            client=client,
            after=after,
            role=role,
            q=q,
            sort=sort,
        )
    ).parsed
