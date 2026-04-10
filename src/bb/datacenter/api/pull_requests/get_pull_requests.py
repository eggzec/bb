from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_pull_requests_response_200 import GetPullRequestsResponse200
from ...models.get_pull_requests_response_401 import GetPullRequestsResponse401
from ...models.get_pull_requests_response_404 import GetPullRequestsResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    commit_id: str,
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
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/commits/{commit_id}/pull-requests".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            commit_id=quote(str(commit_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetPullRequestsResponse200 | GetPullRequestsResponse401 | GetPullRequestsResponse404 | None:
    if response.status_code == 200:
        response_200 = GetPullRequestsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetPullRequestsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetPullRequestsResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetPullRequestsResponse200 | GetPullRequestsResponse401 | GetPullRequestsResponse404]:
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
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GetPullRequestsResponse200 | GetPullRequestsResponse401 | GetPullRequestsResponse404]:
    """Get repository pull requests containing commit

     Retrieve a page of pull requests in the current repository that contain the given commit.

    The user must be authenticated and have access to the specified repository to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPullRequestsResponse200 | GetPullRequestsResponse401 | GetPullRequestsResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
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
    commit_id: str,
    *,
    client: AuthenticatedClient | Client,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetPullRequestsResponse200 | GetPullRequestsResponse401 | GetPullRequestsResponse404 | None:
    """Get repository pull requests containing commit

     Retrieve a page of pull requests in the current repository that contain the given commit.

    The user must be authenticated and have access to the specified repository to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPullRequestsResponse200 | GetPullRequestsResponse401 | GetPullRequestsResponse404
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        client=client,
        start=start,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    *,
    client: AuthenticatedClient | Client,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GetPullRequestsResponse200 | GetPullRequestsResponse401 | GetPullRequestsResponse404]:
    """Get repository pull requests containing commit

     Retrieve a page of pull requests in the current repository that contain the given commit.

    The user must be authenticated and have access to the specified repository to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPullRequestsResponse200 | GetPullRequestsResponse401 | GetPullRequestsResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        start=start,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    *,
    client: AuthenticatedClient | Client,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetPullRequestsResponse200 | GetPullRequestsResponse401 | GetPullRequestsResponse404 | None:
    """Get repository pull requests containing commit

     Retrieve a page of pull requests in the current repository that contain the given commit.

    The user must be authenticated and have access to the specified repository to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPullRequestsResponse200 | GetPullRequestsResponse401 | GetPullRequestsResponse404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            commit_id=commit_id,
            client=client,
            start=start,
            limit=limit,
        )
    ).parsed
