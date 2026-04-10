from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.example_files import ExampleFiles
from ...models.stream_1_response_400 import Stream1Response400
from ...models.stream_1_response_401 import Stream1Response401
from ...models.stream_1_response_404 import Stream1Response404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    path: str,
    *,
    at: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["at"] = at

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/last-modified/{path}".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            path=quote(str(path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ExampleFiles | Stream1Response400 | Stream1Response401 | Stream1Response404 | None:
    if response.status_code == 200:
        response_200 = ExampleFiles.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Stream1Response400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Stream1Response401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = Stream1Response404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ExampleFiles | Stream1Response400 | Stream1Response401 | Stream1Response404]:
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
) -> Response[ExampleFiles | Stream1Response400 | Stream1Response401 | Stream1Response404]:
    """Stream files with last modified commit in path

     Streams files in the requested <code>path</code> with the last commit to modify each file. Commit
    modifications are traversed starting from the <code>at</code> commit or, if not specified, from the
    tip of the default branch.

    Unless the repository is public, the authenticated user must have <b>REPO_READ</b> access to call
    this resource.

    Args:
        project_key (str):
        repository_slug (str):
        path (str):
        at (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExampleFiles | Stream1Response400 | Stream1Response401 | Stream1Response404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        path=path,
        at=at,
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
) -> ExampleFiles | Stream1Response400 | Stream1Response401 | Stream1Response404 | None:
    """Stream files with last modified commit in path

     Streams files in the requested <code>path</code> with the last commit to modify each file. Commit
    modifications are traversed starting from the <code>at</code> commit or, if not specified, from the
    tip of the default branch.

    Unless the repository is public, the authenticated user must have <b>REPO_READ</b> access to call
    this resource.

    Args:
        project_key (str):
        repository_slug (str):
        path (str):
        at (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExampleFiles | Stream1Response400 | Stream1Response401 | Stream1Response404
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        path=path,
        client=client,
        at=at,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    path: str,
    *,
    client: AuthenticatedClient | Client,
    at: str | Unset = UNSET,
) -> Response[ExampleFiles | Stream1Response400 | Stream1Response401 | Stream1Response404]:
    """Stream files with last modified commit in path

     Streams files in the requested <code>path</code> with the last commit to modify each file. Commit
    modifications are traversed starting from the <code>at</code> commit or, if not specified, from the
    tip of the default branch.

    Unless the repository is public, the authenticated user must have <b>REPO_READ</b> access to call
    this resource.

    Args:
        project_key (str):
        repository_slug (str):
        path (str):
        at (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExampleFiles | Stream1Response400 | Stream1Response401 | Stream1Response404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        path=path,
        at=at,
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
) -> ExampleFiles | Stream1Response400 | Stream1Response401 | Stream1Response404 | None:
    """Stream files with last modified commit in path

     Streams files in the requested <code>path</code> with the last commit to modify each file. Commit
    modifications are traversed starting from the <code>at</code> commit or, if not specified, from the
    tip of the default branch.

    Unless the repository is public, the authenticated user must have <b>REPO_READ</b> access to call
    this resource.

    Args:
        project_key (str):
        repository_slug (str):
        path (str):
        at (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExampleFiles | Stream1Response400 | Stream1Response401 | Stream1Response404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            path=path,
            client=client,
            at=at,
        )
    ).parsed
