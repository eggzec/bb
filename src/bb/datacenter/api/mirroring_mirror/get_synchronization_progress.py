from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_synchronization_progress_response_404 import GetSynchronizationProgressResponse404
from ...models.rest_sync_progress import RestSyncProgress
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/mirroring/latest/progress",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetSynchronizationProgressResponse404 | RestSyncProgress | None:
    if response.status_code == 200:
        response_200 = RestSyncProgress.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = GetSynchronizationProgressResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetSynchronizationProgressResponse404 | RestSyncProgress]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetSynchronizationProgressResponse404 | RestSyncProgress]:
    r"""Get synchronization progress state

      Retrieves synchronization progress state.If there's no progress to report, this resource will
    return <pre><code> {\"discovering\":false,\"syncedRepos\":0,\"totalRepos\":0}</code></pre> If there
    are repositories in the process of synchronizing, but the precise number hasn't been discovered yet,
    this resource will return: <pre><code>
    {\"discovering\":true,\"syncedRepos\":3,\"totalRepos\":100}</code></pre> If there is progress to
    report and the total number of repositories is known, this resource will return: <pre> <code>
    {\"discovering\":false,\"syncedRepos\":242,\"totalRepos\":1071}</code> </pre>

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSynchronizationProgressResponse404 | RestSyncProgress]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> GetSynchronizationProgressResponse404 | RestSyncProgress | None:
    r"""Get synchronization progress state

      Retrieves synchronization progress state.If there's no progress to report, this resource will
    return <pre><code> {\"discovering\":false,\"syncedRepos\":0,\"totalRepos\":0}</code></pre> If there
    are repositories in the process of synchronizing, but the precise number hasn't been discovered yet,
    this resource will return: <pre><code>
    {\"discovering\":true,\"syncedRepos\":3,\"totalRepos\":100}</code></pre> If there is progress to
    report and the total number of repositories is known, this resource will return: <pre> <code>
    {\"discovering\":false,\"syncedRepos\":242,\"totalRepos\":1071}</code> </pre>

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSynchronizationProgressResponse404 | RestSyncProgress
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetSynchronizationProgressResponse404 | RestSyncProgress]:
    r"""Get synchronization progress state

      Retrieves synchronization progress state.If there's no progress to report, this resource will
    return <pre><code> {\"discovering\":false,\"syncedRepos\":0,\"totalRepos\":0}</code></pre> If there
    are repositories in the process of synchronizing, but the precise number hasn't been discovered yet,
    this resource will return: <pre><code>
    {\"discovering\":true,\"syncedRepos\":3,\"totalRepos\":100}</code></pre> If there is progress to
    report and the total number of repositories is known, this resource will return: <pre> <code>
    {\"discovering\":false,\"syncedRepos\":242,\"totalRepos\":1071}</code> </pre>

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSynchronizationProgressResponse404 | RestSyncProgress]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> GetSynchronizationProgressResponse404 | RestSyncProgress | None:
    r"""Get synchronization progress state

      Retrieves synchronization progress state.If there's no progress to report, this resource will
    return <pre><code> {\"discovering\":false,\"syncedRepos\":0,\"totalRepos\":0}</code></pre> If there
    are repositories in the process of synchronizing, but the precise number hasn't been discovered yet,
    this resource will return: <pre><code>
    {\"discovering\":true,\"syncedRepos\":3,\"totalRepos\":100}</code></pre> If there is progress to
    report and the total number of repositories is known, this resource will return: <pre> <code>
    {\"discovering\":false,\"syncedRepos\":242,\"totalRepos\":1071}</code> </pre>

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSynchronizationProgressResponse404 | RestSyncProgress
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
