from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_response_400 import GetResponse400
from ...models.get_response_401 import GetResponse401
from ...models.get_response_404 import GetResponse404
from ...models.rest_build_status import RestBuildStatus
from ...types import UNSET, Response


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    *,
    key: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["key"] = key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/commits/{commit_id}/builds".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            commit_id=quote(str(commit_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetResponse400 | GetResponse401 | GetResponse404 | RestBuildStatus | None:
    if response.status_code == 200:
        response_200 = RestBuildStatus.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetResponse400 | GetResponse401 | GetResponse404 | RestBuildStatus]:
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
    key: str,
) -> Response[GetResponse400 | GetResponse401 | GetResponse404 | RestBuildStatus]:
    """Get a specific build status

     Get a specific build status.


    The authenticated user must have **REPO_READ** permission for the provided repository.The request
    can also be made with anonymous 2-legged OAuth.<br>Since 7.14

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetResponse400 | GetResponse401 | GetResponse404 | RestBuildStatus]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        key=key,
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
    key: str,
) -> GetResponse400 | GetResponse401 | GetResponse404 | RestBuildStatus | None:
    """Get a specific build status

     Get a specific build status.


    The authenticated user must have **REPO_READ** permission for the provided repository.The request
    can also be made with anonymous 2-legged OAuth.<br>Since 7.14

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetResponse400 | GetResponse401 | GetResponse404 | RestBuildStatus
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        client=client,
        key=key,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    *,
    client: AuthenticatedClient | Client,
    key: str,
) -> Response[GetResponse400 | GetResponse401 | GetResponse404 | RestBuildStatus]:
    """Get a specific build status

     Get a specific build status.


    The authenticated user must have **REPO_READ** permission for the provided repository.The request
    can also be made with anonymous 2-legged OAuth.<br>Since 7.14

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetResponse400 | GetResponse401 | GetResponse404 | RestBuildStatus]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        key=key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    *,
    client: AuthenticatedClient | Client,
    key: str,
) -> GetResponse400 | GetResponse401 | GetResponse404 | RestBuildStatus | None:
    """Get a specific build status

     Get a specific build status.


    The authenticated user must have **REPO_READ** permission for the provided repository.The request
    can also be made with anonymous 2-legged OAuth.<br>Since 7.14

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetResponse400 | GetResponse401 | GetResponse404 | RestBuildStatus
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            commit_id=commit_id,
            client=client,
            key=key,
        )
    ).parsed
