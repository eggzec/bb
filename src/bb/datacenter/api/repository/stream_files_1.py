from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.stream_files_1_response_200 import StreamFiles1Response200
from ...models.stream_files_1_response_400 import StreamFiles1Response400
from ...models.stream_files_1_response_401 import StreamFiles1Response401
from ...models.stream_files_1_response_404 import StreamFiles1Response404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    path: str,
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
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/files/{path}".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            path=quote(str(path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> StreamFiles1Response200 | StreamFiles1Response400 | StreamFiles1Response401 | StreamFiles1Response404 | None:
    if response.status_code == 200:
        response_200 = StreamFiles1Response200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = StreamFiles1Response400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = StreamFiles1Response401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = StreamFiles1Response404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[StreamFiles1Response200 | StreamFiles1Response400 | StreamFiles1Response401 | StreamFiles1Response404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    repository_slug: str,
    path: str,
    *,
    client: AuthenticatedClient | Client,
    at: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[StreamFiles1Response200 | StreamFiles1Response400 | StreamFiles1Response401 | StreamFiles1Response404]:
    """Get files in directory

     Retrieve a page of files from particular directory of a repository. The search is done recursively,
    so all files from any sub-directory of the specified directory will be returned.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        path (str):
        at (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StreamFiles1Response200 | StreamFiles1Response400 | StreamFiles1Response401 | StreamFiles1Response404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        path=path,
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
    path: str,
    *,
    client: AuthenticatedClient | Client,
    at: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> StreamFiles1Response200 | StreamFiles1Response400 | StreamFiles1Response401 | StreamFiles1Response404 | None:
    """Get files in directory

     Retrieve a page of files from particular directory of a repository. The search is done recursively,
    so all files from any sub-directory of the specified directory will be returned.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        path (str):
        at (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StreamFiles1Response200 | StreamFiles1Response400 | StreamFiles1Response401 | StreamFiles1Response404
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        path=path,
        client=client,
        at=at,
        start=start,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    path: str,
    *,
    client: AuthenticatedClient | Client,
    at: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[StreamFiles1Response200 | StreamFiles1Response400 | StreamFiles1Response401 | StreamFiles1Response404]:
    """Get files in directory

     Retrieve a page of files from particular directory of a repository. The search is done recursively,
    so all files from any sub-directory of the specified directory will be returned.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        path (str):
        at (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StreamFiles1Response200 | StreamFiles1Response400 | StreamFiles1Response401 | StreamFiles1Response404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        path=path,
        at=at,
        start=start,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    path: str,
    *,
    client: AuthenticatedClient | Client,
    at: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> StreamFiles1Response200 | StreamFiles1Response400 | StreamFiles1Response401 | StreamFiles1Response404 | None:
    """Get files in directory

     Retrieve a page of files from particular directory of a repository. The search is done recursively,
    so all files from any sub-directory of the specified directory will be returned.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        path (str):
        at (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StreamFiles1Response200 | StreamFiles1Response400 | StreamFiles1Response401 | StreamFiles1Response404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            path=path,
            client=client,
            at=at,
            start=start,
            limit=limit,
        )
    ).parsed
