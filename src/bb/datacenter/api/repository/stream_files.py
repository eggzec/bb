from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.stream_files_response_200 import StreamFilesResponse200
from ...models.stream_files_response_400 import StreamFilesResponse400
from ...models.stream_files_response_401 import StreamFilesResponse401
from ...models.stream_files_response_404 import StreamFilesResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    *,
    at: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["at"] = at

    params["start"] = start

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/files".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> StreamFilesResponse200 | StreamFilesResponse400 | StreamFilesResponse401 | StreamFilesResponse404 | None:
    if response.status_code == 200:
        response_200 = StreamFilesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = StreamFilesResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = StreamFilesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = StreamFilesResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[StreamFilesResponse200 | StreamFilesResponse400 | StreamFilesResponse401 | StreamFilesResponse404]:
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
    at: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[StreamFilesResponse200 | StreamFilesResponse400 | StreamFilesResponse401 | StreamFilesResponse404]:
    """Get files in directory

     Retrieve a page of files from particular directory of a repository. The search is done recursively,
    so all files from any sub-directory of the specified directory will be returned.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        at (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StreamFilesResponse200 | StreamFilesResponse400 | StreamFilesResponse401 | StreamFilesResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        at=at,
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
    at: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> StreamFilesResponse200 | StreamFilesResponse400 | StreamFilesResponse401 | StreamFilesResponse404 | None:
    """Get files in directory

     Retrieve a page of files from particular directory of a repository. The search is done recursively,
    so all files from any sub-directory of the specified directory will be returned.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        at (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StreamFilesResponse200 | StreamFilesResponse400 | StreamFilesResponse401 | StreamFilesResponse404
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        client=client,
        at=at,
        start=start,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    at: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[StreamFilesResponse200 | StreamFilesResponse400 | StreamFilesResponse401 | StreamFilesResponse404]:
    """Get files in directory

     Retrieve a page of files from particular directory of a repository. The search is done recursively,
    so all files from any sub-directory of the specified directory will be returned.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        at (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StreamFilesResponse200 | StreamFilesResponse400 | StreamFilesResponse401 | StreamFilesResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        at=at,
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
    at: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> StreamFilesResponse200 | StreamFilesResponse400 | StreamFilesResponse401 | StreamFilesResponse404 | None:
    """Get files in directory

     Retrieve a page of files from particular directory of a repository. The search is done recursively,
    so all files from any sub-directory of the specified directory will be returned.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        at (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StreamFilesResponse200 | StreamFilesResponse400 | StreamFilesResponse401 | StreamFilesResponse404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            client=client,
            at=at,
            start=start,
            limit=limit,
        )
    ).parsed
