from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.indexing_queued_status_response_401 import IndexingQueuedStatusResponse401
from ...models.indexing_queued_status_response_404 import IndexingQueuedStatusResponse404
from ...models.rest_indexing_is_repository_queued import RestIndexingIsRepositoryQueued
from ...types import Response


def _get_kwargs(
    project_key: str,
    repository_slug: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/indexing/latest/projects/{project_key}/repos/{repository_slug}/indexing-queued-status".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> IndexingQueuedStatusResponse401 | IndexingQueuedStatusResponse404 | RestIndexingIsRepositoryQueued | None:
    if response.status_code == 200:
        response_200 = RestIndexingIsRepositoryQueued.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = IndexingQueuedStatusResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = IndexingQueuedStatusResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[IndexingQueuedStatusResponse401 | IndexingQueuedStatusResponse404 | RestIndexingIsRepositoryQueued]:
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
) -> Response[IndexingQueuedStatusResponse401 | IndexingQueuedStatusResponse404 | RestIndexingIsRepositoryQueued]:
    """Checks if a repository has been queued for indexing.

     Checks if a repository has been queued for indexing.

    The authenticated user must have <b>REPO_ADMIN</b> permission for the specified repository to call
    this resource.

    Args:
        project_key (str):
        repository_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IndexingQueuedStatusResponse401 | IndexingQueuedStatusResponse404 | RestIndexingIsRepositoryQueued]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
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
) -> IndexingQueuedStatusResponse401 | IndexingQueuedStatusResponse404 | RestIndexingIsRepositoryQueued | None:
    """Checks if a repository has been queued for indexing.

     Checks if a repository has been queued for indexing.

    The authenticated user must have <b>REPO_ADMIN</b> permission for the specified repository to call
    this resource.

    Args:
        project_key (str):
        repository_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IndexingQueuedStatusResponse401 | IndexingQueuedStatusResponse404 | RestIndexingIsRepositoryQueued
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[IndexingQueuedStatusResponse401 | IndexingQueuedStatusResponse404 | RestIndexingIsRepositoryQueued]:
    """Checks if a repository has been queued for indexing.

     Checks if a repository has been queued for indexing.

    The authenticated user must have <b>REPO_ADMIN</b> permission for the specified repository to call
    this resource.

    Args:
        project_key (str):
        repository_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IndexingQueuedStatusResponse401 | IndexingQueuedStatusResponse404 | RestIndexingIsRepositoryQueued]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
) -> IndexingQueuedStatusResponse401 | IndexingQueuedStatusResponse404 | RestIndexingIsRepositoryQueued | None:
    """Checks if a repository has been queued for indexing.

     Checks if a repository has been queued for indexing.

    The authenticated user must have <b>REPO_ADMIN</b> permission for the specified repository to call
    this resource.

    Args:
        project_key (str):
        repository_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IndexingQueuedStatusResponse401 | IndexingQueuedStatusResponse404 | RestIndexingIsRepositoryQueued
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            client=client,
        )
    ).parsed
