from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_commits_1_response_200 import GetCommits1Response200
from ...models.get_commits_1_response_401 import GetCommits1Response401
from ...models.get_commits_1_response_404 import GetCommits1Response404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    *,
    avatar_scheme: str | Unset = UNSET,
    with_counts: str | Unset = UNSET,
    avatar_size: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["avatarScheme"] = avatar_scheme

    params["withCounts"] = with_counts

    params["avatarSize"] = avatar_size

    params["start"] = start

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/pull-requests/{pull_request_id}/commits".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            pull_request_id=quote(str(pull_request_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetCommits1Response200 | GetCommits1Response401 | GetCommits1Response404 | None:
    if response.status_code == 200:
        response_200 = GetCommits1Response200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetCommits1Response401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetCommits1Response404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetCommits1Response200 | GetCommits1Response401 | GetCommits1Response404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    *,
    client: AuthenticatedClient | Client,
    avatar_scheme: str | Unset = UNSET,
    with_counts: str | Unset = UNSET,
    avatar_size: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GetCommits1Response200 | GetCommits1Response401 | GetCommits1Response404]:
    """Get pull request commits

     Retrieve commits for the specified pull request.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        avatar_scheme (str | Unset):
        with_counts (str | Unset):
        avatar_size (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCommits1Response200 | GetCommits1Response401 | GetCommits1Response404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
        avatar_scheme=avatar_scheme,
        with_counts=with_counts,
        avatar_size=avatar_size,
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
    pull_request_id: str,
    *,
    client: AuthenticatedClient | Client,
    avatar_scheme: str | Unset = UNSET,
    with_counts: str | Unset = UNSET,
    avatar_size: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetCommits1Response200 | GetCommits1Response401 | GetCommits1Response404 | None:
    """Get pull request commits

     Retrieve commits for the specified pull request.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        avatar_scheme (str | Unset):
        with_counts (str | Unset):
        avatar_size (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCommits1Response200 | GetCommits1Response401 | GetCommits1Response404
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
        client=client,
        avatar_scheme=avatar_scheme,
        with_counts=with_counts,
        avatar_size=avatar_size,
        start=start,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    *,
    client: AuthenticatedClient | Client,
    avatar_scheme: str | Unset = UNSET,
    with_counts: str | Unset = UNSET,
    avatar_size: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GetCommits1Response200 | GetCommits1Response401 | GetCommits1Response404]:
    """Get pull request commits

     Retrieve commits for the specified pull request.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        avatar_scheme (str | Unset):
        with_counts (str | Unset):
        avatar_size (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCommits1Response200 | GetCommits1Response401 | GetCommits1Response404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
        avatar_scheme=avatar_scheme,
        with_counts=with_counts,
        avatar_size=avatar_size,
        start=start,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    *,
    client: AuthenticatedClient | Client,
    avatar_scheme: str | Unset = UNSET,
    with_counts: str | Unset = UNSET,
    avatar_size: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetCommits1Response200 | GetCommits1Response401 | GetCommits1Response404 | None:
    """Get pull request commits

     Retrieve commits for the specified pull request.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        avatar_scheme (str | Unset):
        with_counts (str | Unset):
        avatar_size (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCommits1Response200 | GetCommits1Response401 | GetCommits1Response404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            pull_request_id=pull_request_id,
            client=client,
            avatar_scheme=avatar_scheme,
            with_counts=with_counts,
            avatar_size=avatar_size,
            start=start,
            limit=limit,
        )
    ).parsed
