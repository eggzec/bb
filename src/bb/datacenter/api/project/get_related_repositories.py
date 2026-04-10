from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_related_repositories_response_200 import GetRelatedRepositoriesResponse200
from ...models.get_related_repositories_response_401 import GetRelatedRepositoriesResponse401
from ...models.get_related_repositories_response_404 import GetRelatedRepositoriesResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
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
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/related".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetRelatedRepositoriesResponse200 | GetRelatedRepositoriesResponse401 | GetRelatedRepositoriesResponse404 | None:
    if response.status_code == 200:
        response_200 = GetRelatedRepositoriesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetRelatedRepositoriesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetRelatedRepositoriesResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetRelatedRepositoriesResponse200 | GetRelatedRepositoriesResponse401 | GetRelatedRepositoriesResponse404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[
    GetRelatedRepositoriesResponse200 | GetRelatedRepositoriesResponse401 | GetRelatedRepositoriesResponse404
]:
    """Get related repository

     Retrieve repositories which are related to this one. Related repositories are from the same
    Repository#getHierarchyId() hierarchy as this repository.

    Only repositories to which the authenticated user has <b>REPO_READ</b> permission will be included,
    even if more repositories are part of this repository's hierarchy.

    Args:
        project_key (str):
        repository_slug (str):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRelatedRepositoriesResponse200 | GetRelatedRepositoriesResponse401 | GetRelatedRepositoriesResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        start=start,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetRelatedRepositoriesResponse200 | GetRelatedRepositoriesResponse401 | GetRelatedRepositoriesResponse404 | None:
    """Get related repository

     Retrieve repositories which are related to this one. Related repositories are from the same
    Repository#getHierarchyId() hierarchy as this repository.

    Only repositories to which the authenticated user has <b>REPO_READ</b> permission will be included,
    even if more repositories are part of this repository's hierarchy.

    Args:
        project_key (str):
        repository_slug (str):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRelatedRepositoriesResponse200 | GetRelatedRepositoriesResponse401 | GetRelatedRepositoriesResponse404
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        client=client,
        start=start,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[
    GetRelatedRepositoriesResponse200 | GetRelatedRepositoriesResponse401 | GetRelatedRepositoriesResponse404
]:
    """Get related repository

     Retrieve repositories which are related to this one. Related repositories are from the same
    Repository#getHierarchyId() hierarchy as this repository.

    Only repositories to which the authenticated user has <b>REPO_READ</b> permission will be included,
    even if more repositories are part of this repository's hierarchy.

    Args:
        project_key (str):
        repository_slug (str):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRelatedRepositoriesResponse200 | GetRelatedRepositoriesResponse401 | GetRelatedRepositoriesResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        start=start,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetRelatedRepositoriesResponse200 | GetRelatedRepositoriesResponse401 | GetRelatedRepositoriesResponse404 | None:
    """Get related repository

     Retrieve repositories which are related to this one. Related repositories are from the same
    Repository#getHierarchyId() hierarchy as this repository.

    Only repositories to which the authenticated user has <b>REPO_READ</b> permission will be included,
    even if more repositories are part of this repository's hierarchy.

    Args:
        project_key (str):
        repository_slug (str):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRelatedRepositoriesResponse200 | GetRelatedRepositoriesResponse401 | GetRelatedRepositoriesResponse404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            client=client,
            start=start,
            limit=limit,
        )
    ).parsed
