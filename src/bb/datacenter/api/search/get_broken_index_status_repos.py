from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_broken_index_status_repos_response_200 import GetBrokenIndexStatusReposResponse200
from ...models.get_broken_index_status_repos_response_400 import GetBrokenIndexStatusReposResponse400
from ...models.get_broken_index_status_repos_response_401 import GetBrokenIndexStatusReposResponse401
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["start"] = start

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/indexing/latest/support-info/broken-index-status-repos",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetBrokenIndexStatusReposResponse200
    | GetBrokenIndexStatusReposResponse400
    | GetBrokenIndexStatusReposResponse401
    | None
):
    if response.status_code == 200:
        response_200 = GetBrokenIndexStatusReposResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetBrokenIndexStatusReposResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetBrokenIndexStatusReposResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetBrokenIndexStatusReposResponse200 | GetBrokenIndexStatusReposResponse400 | GetBrokenIndexStatusReposResponse401
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[
    GetBrokenIndexStatusReposResponse200 | GetBrokenIndexStatusReposResponse400 | GetBrokenIndexStatusReposResponse401
]:
    """Retrieve a paged list of repositories which have exceeded the configured maximum indexing retries.

     Retrieve repositories which are in the <code>BROKEN</code> indexing state.

    When a repository has a <code>BROKEN</code> indexing status it will no longer attempt to be re-
    indexed by the system, even when changes are made to its code. A repository is given a
    <code>BROKEN</code> indexing status when it fails to index too many times.

    The authenticated user must have <b>SYS_ADMIN</b> permission to call this resource.

    Args:
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBrokenIndexStatusReposResponse200 | GetBrokenIndexStatusReposResponse400 | GetBrokenIndexStatusReposResponse401]
    """

    kwargs = _get_kwargs(
        start=start,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> (
    GetBrokenIndexStatusReposResponse200
    | GetBrokenIndexStatusReposResponse400
    | GetBrokenIndexStatusReposResponse401
    | None
):
    """Retrieve a paged list of repositories which have exceeded the configured maximum indexing retries.

     Retrieve repositories which are in the <code>BROKEN</code> indexing state.

    When a repository has a <code>BROKEN</code> indexing status it will no longer attempt to be re-
    indexed by the system, even when changes are made to its code. A repository is given a
    <code>BROKEN</code> indexing status when it fails to index too many times.

    The authenticated user must have <b>SYS_ADMIN</b> permission to call this resource.

    Args:
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBrokenIndexStatusReposResponse200 | GetBrokenIndexStatusReposResponse400 | GetBrokenIndexStatusReposResponse401
    """

    return sync_detailed(
        client=client,
        start=start,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[
    GetBrokenIndexStatusReposResponse200 | GetBrokenIndexStatusReposResponse400 | GetBrokenIndexStatusReposResponse401
]:
    """Retrieve a paged list of repositories which have exceeded the configured maximum indexing retries.

     Retrieve repositories which are in the <code>BROKEN</code> indexing state.

    When a repository has a <code>BROKEN</code> indexing status it will no longer attempt to be re-
    indexed by the system, even when changes are made to its code. A repository is given a
    <code>BROKEN</code> indexing status when it fails to index too many times.

    The authenticated user must have <b>SYS_ADMIN</b> permission to call this resource.

    Args:
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBrokenIndexStatusReposResponse200 | GetBrokenIndexStatusReposResponse400 | GetBrokenIndexStatusReposResponse401]
    """

    kwargs = _get_kwargs(
        start=start,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> (
    GetBrokenIndexStatusReposResponse200
    | GetBrokenIndexStatusReposResponse400
    | GetBrokenIndexStatusReposResponse401
    | None
):
    """Retrieve a paged list of repositories which have exceeded the configured maximum indexing retries.

     Retrieve repositories which are in the <code>BROKEN</code> indexing state.

    When a repository has a <code>BROKEN</code> indexing status it will no longer attempt to be re-
    indexed by the system, even when changes are made to its code. A repository is given a
    <code>BROKEN</code> indexing status when it fails to index too many times.

    The authenticated user must have <b>SYS_ADMIN</b> permission to call this resource.

    Args:
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBrokenIndexStatusReposResponse200 | GetBrokenIndexStatusReposResponse400 | GetBrokenIndexStatusReposResponse401
    """

    return (
        await asyncio_detailed(
            client=client,
            start=start,
            limit=limit,
        )
    ).parsed
