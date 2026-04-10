from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.watch_response_401 import WatchResponse401
from ...models.watch_response_404 import WatchResponse404
from ...types import Response


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    commit_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/commits/{commit_id}/watch".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            commit_id=quote(str(commit_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | WatchResponse401 | WatchResponse404 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = WatchResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = WatchResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | WatchResponse401 | WatchResponse404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | WatchResponse401 | WatchResponse404]:
    """Watch commit

     Add the authenticated user as a watcher for the specified commit.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository containing
    the commit to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | WatchResponse401 | WatchResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | WatchResponse401 | WatchResponse404 | None:
    """Watch commit

     Add the authenticated user as a watcher for the specified commit.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository containing
    the commit to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | WatchResponse401 | WatchResponse404
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | WatchResponse401 | WatchResponse404]:
    """Watch commit

     Add the authenticated user as a watcher for the specified commit.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository containing
    the commit to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | WatchResponse401 | WatchResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | WatchResponse401 | WatchResponse404 | None:
    """Watch commit

     Add the authenticated user as a watcher for the specified commit.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository containing
    the commit to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | WatchResponse401 | WatchResponse404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            commit_id=commit_id,
            client=client,
        )
    ).parsed
