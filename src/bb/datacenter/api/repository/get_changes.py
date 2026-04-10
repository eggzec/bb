from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_changes_response_200 import GetChangesResponse200
from ...models.get_changes_response_400 import GetChangesResponse400
from ...models.get_changes_response_401 import GetChangesResponse401
from ...models.get_changes_response_404 import GetChangesResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    *,
    with_comments: str | Unset = UNSET,
    since: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["withComments"] = with_comments

    params["since"] = since

    params["start"] = start

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/commits/{commit_id}/changes".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            commit_id=quote(str(commit_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetChangesResponse200 | GetChangesResponse400 | GetChangesResponse401 | GetChangesResponse404 | None:
    if response.status_code == 200:
        response_200 = GetChangesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetChangesResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetChangesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetChangesResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetChangesResponse200 | GetChangesResponse400 | GetChangesResponse401 | GetChangesResponse404]:
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
    with_comments: str | Unset = UNSET,
    since: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GetChangesResponse200 | GetChangesResponse400 | GetChangesResponse401 | GetChangesResponse404]:
    """Get changes in commit

     Retrieve a page of changes made in a specified commit.

     <strong>Note:</strong> The implementation will apply a hard cap (<code>page.max.changes</code>) and
    it is not possible to request subsequent content when that cap is exceeded.

     The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        with_comments (str | Unset):
        since (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetChangesResponse200 | GetChangesResponse400 | GetChangesResponse401 | GetChangesResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        with_comments=with_comments,
        since=since,
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
    with_comments: str | Unset = UNSET,
    since: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetChangesResponse200 | GetChangesResponse400 | GetChangesResponse401 | GetChangesResponse404 | None:
    """Get changes in commit

     Retrieve a page of changes made in a specified commit.

     <strong>Note:</strong> The implementation will apply a hard cap (<code>page.max.changes</code>) and
    it is not possible to request subsequent content when that cap is exceeded.

     The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        with_comments (str | Unset):
        since (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetChangesResponse200 | GetChangesResponse400 | GetChangesResponse401 | GetChangesResponse404
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        client=client,
        with_comments=with_comments,
        since=since,
        start=start,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    *,
    client: AuthenticatedClient | Client,
    with_comments: str | Unset = UNSET,
    since: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GetChangesResponse200 | GetChangesResponse400 | GetChangesResponse401 | GetChangesResponse404]:
    """Get changes in commit

     Retrieve a page of changes made in a specified commit.

     <strong>Note:</strong> The implementation will apply a hard cap (<code>page.max.changes</code>) and
    it is not possible to request subsequent content when that cap is exceeded.

     The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        with_comments (str | Unset):
        since (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetChangesResponse200 | GetChangesResponse400 | GetChangesResponse401 | GetChangesResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        with_comments=with_comments,
        since=since,
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
    with_comments: str | Unset = UNSET,
    since: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetChangesResponse200 | GetChangesResponse400 | GetChangesResponse401 | GetChangesResponse404 | None:
    """Get changes in commit

     Retrieve a page of changes made in a specified commit.

     <strong>Note:</strong> The implementation will apply a hard cap (<code>page.max.changes</code>) and
    it is not possible to request subsequent content when that cap is exceeded.

     The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        with_comments (str | Unset):
        since (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetChangesResponse200 | GetChangesResponse400 | GetChangesResponse401 | GetChangesResponse404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            commit_id=commit_id,
            client=client,
            with_comments=with_comments,
            since=since,
            start=start,
            limit=limit,
        )
    ).parsed
