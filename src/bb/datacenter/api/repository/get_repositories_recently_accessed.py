from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_repositories_recently_accessed_response_200 import GetRepositoriesRecentlyAccessedResponse200
from ...models.get_repositories_recently_accessed_response_400 import GetRepositoriesRecentlyAccessedResponse400
from ...models.get_repositories_recently_accessed_response_401 import GetRepositoriesRecentlyAccessedResponse401
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    permission: str | Unset = "REPO_READ",
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["permission"] = permission

    params["start"] = start

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/profile/recent/repos",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetRepositoriesRecentlyAccessedResponse200
    | GetRepositoriesRecentlyAccessedResponse400
    | GetRepositoriesRecentlyAccessedResponse401
    | None
):
    if response.status_code == 200:
        response_200 = GetRepositoriesRecentlyAccessedResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetRepositoriesRecentlyAccessedResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetRepositoriesRecentlyAccessedResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetRepositoriesRecentlyAccessedResponse200
    | GetRepositoriesRecentlyAccessedResponse400
    | GetRepositoriesRecentlyAccessedResponse401
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
    permission: str | Unset = "REPO_READ",
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[
    GetRepositoriesRecentlyAccessedResponse200
    | GetRepositoriesRecentlyAccessedResponse400
    | GetRepositoriesRecentlyAccessedResponse401
]:
    """Get recently accessed repositories

     Retrieve a page of recently accessed repositories for the currently authenticated user.

    Repositories are ordered from most recently to least recently accessed. <p>Only authenticated users
    may call this resource.

    Args:
        permission (str | Unset):  Default: 'REPO_READ'.
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRepositoriesRecentlyAccessedResponse200 | GetRepositoriesRecentlyAccessedResponse400 | GetRepositoriesRecentlyAccessedResponse401]
    """

    kwargs = _get_kwargs(
        permission=permission,
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
    permission: str | Unset = "REPO_READ",
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> (
    GetRepositoriesRecentlyAccessedResponse200
    | GetRepositoriesRecentlyAccessedResponse400
    | GetRepositoriesRecentlyAccessedResponse401
    | None
):
    """Get recently accessed repositories

     Retrieve a page of recently accessed repositories for the currently authenticated user.

    Repositories are ordered from most recently to least recently accessed. <p>Only authenticated users
    may call this resource.

    Args:
        permission (str | Unset):  Default: 'REPO_READ'.
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRepositoriesRecentlyAccessedResponse200 | GetRepositoriesRecentlyAccessedResponse400 | GetRepositoriesRecentlyAccessedResponse401
    """

    return sync_detailed(
        client=client,
        permission=permission,
        start=start,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    permission: str | Unset = "REPO_READ",
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[
    GetRepositoriesRecentlyAccessedResponse200
    | GetRepositoriesRecentlyAccessedResponse400
    | GetRepositoriesRecentlyAccessedResponse401
]:
    """Get recently accessed repositories

     Retrieve a page of recently accessed repositories for the currently authenticated user.

    Repositories are ordered from most recently to least recently accessed. <p>Only authenticated users
    may call this resource.

    Args:
        permission (str | Unset):  Default: 'REPO_READ'.
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRepositoriesRecentlyAccessedResponse200 | GetRepositoriesRecentlyAccessedResponse400 | GetRepositoriesRecentlyAccessedResponse401]
    """

    kwargs = _get_kwargs(
        permission=permission,
        start=start,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    permission: str | Unset = "REPO_READ",
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> (
    GetRepositoriesRecentlyAccessedResponse200
    | GetRepositoriesRecentlyAccessedResponse400
    | GetRepositoriesRecentlyAccessedResponse401
    | None
):
    """Get recently accessed repositories

     Retrieve a page of recently accessed repositories for the currently authenticated user.

    Repositories are ordered from most recently to least recently accessed. <p>Only authenticated users
    may call this resource.

    Args:
        permission (str | Unset):  Default: 'REPO_READ'.
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRepositoriesRecentlyAccessedResponse200 | GetRepositoriesRecentlyAccessedResponse400 | GetRepositoriesRecentlyAccessedResponse401
    """

    return (
        await asyncio_detailed(
            client=client,
            permission=permission,
            start=start,
            limit=limit,
        )
    ).parsed
