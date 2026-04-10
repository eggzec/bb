from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_forked_repositories_response_200 import GetForkedRepositoriesResponse200
from ...models.get_forked_repositories_response_401 import GetForkedRepositoriesResponse401
from ...models.get_forked_repositories_response_404 import GetForkedRepositoriesResponse404
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
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/forks".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetForkedRepositoriesResponse200 | GetForkedRepositoriesResponse401 | GetForkedRepositoriesResponse404 | None:
    if response.status_code == 200:
        response_200 = GetForkedRepositoriesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetForkedRepositoriesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetForkedRepositoriesResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetForkedRepositoriesResponse200 | GetForkedRepositoriesResponse401 | GetForkedRepositoriesResponse404]:
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
) -> Response[GetForkedRepositoriesResponse200 | GetForkedRepositoriesResponse401 | GetForkedRepositoriesResponse404]:
    r"""Get repository forks

     Retrieve repositories which have been forked from this one. Unlike
    #getRelatedRepositories(Repository, PageRequest) related repositories, this only looks at a given
    repository's direct forks. If those forks have themselves been the origin of more forks, such
    \"grandchildren\" repositories will not be retrieved.

    Only repositories to which the authenticated user has <b>REPO_READ</b> permission will be included,
    even if other repositories have been forked from this one.

    Args:
        project_key (str):
        repository_slug (str):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetForkedRepositoriesResponse200 | GetForkedRepositoriesResponse401 | GetForkedRepositoriesResponse404]
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
) -> GetForkedRepositoriesResponse200 | GetForkedRepositoriesResponse401 | GetForkedRepositoriesResponse404 | None:
    r"""Get repository forks

     Retrieve repositories which have been forked from this one. Unlike
    #getRelatedRepositories(Repository, PageRequest) related repositories, this only looks at a given
    repository's direct forks. If those forks have themselves been the origin of more forks, such
    \"grandchildren\" repositories will not be retrieved.

    Only repositories to which the authenticated user has <b>REPO_READ</b> permission will be included,
    even if other repositories have been forked from this one.

    Args:
        project_key (str):
        repository_slug (str):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetForkedRepositoriesResponse200 | GetForkedRepositoriesResponse401 | GetForkedRepositoriesResponse404
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
) -> Response[GetForkedRepositoriesResponse200 | GetForkedRepositoriesResponse401 | GetForkedRepositoriesResponse404]:
    r"""Get repository forks

     Retrieve repositories which have been forked from this one. Unlike
    #getRelatedRepositories(Repository, PageRequest) related repositories, this only looks at a given
    repository's direct forks. If those forks have themselves been the origin of more forks, such
    \"grandchildren\" repositories will not be retrieved.

    Only repositories to which the authenticated user has <b>REPO_READ</b> permission will be included,
    even if other repositories have been forked from this one.

    Args:
        project_key (str):
        repository_slug (str):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetForkedRepositoriesResponse200 | GetForkedRepositoriesResponse401 | GetForkedRepositoriesResponse404]
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
) -> GetForkedRepositoriesResponse200 | GetForkedRepositoriesResponse401 | GetForkedRepositoriesResponse404 | None:
    r"""Get repository forks

     Retrieve repositories which have been forked from this one. Unlike
    #getRelatedRepositories(Repository, PageRequest) related repositories, this only looks at a given
    repository's direct forks. If those forks have themselves been the origin of more forks, such
    \"grandchildren\" repositories will not be retrieved.

    Only repositories to which the authenticated user has <b>REPO_READ</b> permission will be included,
    even if other repositories have been forked from this one.

    Args:
        project_key (str):
        repository_slug (str):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetForkedRepositoriesResponse200 | GetForkedRepositoriesResponse401 | GetForkedRepositoriesResponse404
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
