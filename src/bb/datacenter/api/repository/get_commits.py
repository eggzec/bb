from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_commits_response_200 import GetCommitsResponse200
from ...models.get_commits_response_400 import GetCommitsResponse400
from ...models.get_commits_response_401 import GetCommitsResponse401
from ...models.get_commits_response_404 import GetCommitsResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    *,
    avatar_scheme: str | Unset = UNSET,
    path: str | Unset = UNSET,
    with_counts: str | Unset = UNSET,
    follow_renames: str | Unset = UNSET,
    until: str | Unset = UNSET,
    avatar_size: str | Unset = UNSET,
    since: str | Unset = UNSET,
    merges: str | Unset = UNSET,
    ignore_missing: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["avatarScheme"] = avatar_scheme

    params["path"] = path

    params["withCounts"] = with_counts

    params["followRenames"] = follow_renames

    params["until"] = until

    params["avatarSize"] = avatar_size

    params["since"] = since

    params["merges"] = merges

    params["ignoreMissing"] = ignore_missing

    params["start"] = start

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/commits".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetCommitsResponse200 | GetCommitsResponse400 | GetCommitsResponse401 | GetCommitsResponse404 | None:
    if response.status_code == 200:
        response_200 = GetCommitsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetCommitsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetCommitsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetCommitsResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetCommitsResponse200 | GetCommitsResponse400 | GetCommitsResponse401 | GetCommitsResponse404]:
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
    avatar_scheme: str | Unset = UNSET,
    path: str | Unset = UNSET,
    with_counts: str | Unset = UNSET,
    follow_renames: str | Unset = UNSET,
    until: str | Unset = UNSET,
    avatar_size: str | Unset = UNSET,
    since: str | Unset = UNSET,
    merges: str | Unset = UNSET,
    ignore_missing: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GetCommitsResponse200 | GetCommitsResponse400 | GetCommitsResponse401 | GetCommitsResponse404]:
    r"""Get commits

     Retrieve a page of commits from a given starting commit or \"between\" two commits. If no explicit
    commit is specified, the tip of the repository's default branch is assumed. commits may be
    identified by branch or tag name or by ID. A path may be supplied to restrict the returned commits
    to only those which affect that path.

    The authenticated user must have <b>REPO_READ</b> permission for the specified repository to call
    this resource.

    Args:
        project_key (str):
        repository_slug (str):
        avatar_scheme (str | Unset):
        path (str | Unset):
        with_counts (str | Unset):
        follow_renames (str | Unset):
        until (str | Unset):
        avatar_size (str | Unset):
        since (str | Unset):
        merges (str | Unset):
        ignore_missing (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCommitsResponse200 | GetCommitsResponse400 | GetCommitsResponse401 | GetCommitsResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        avatar_scheme=avatar_scheme,
        path=path,
        with_counts=with_counts,
        follow_renames=follow_renames,
        until=until,
        avatar_size=avatar_size,
        since=since,
        merges=merges,
        ignore_missing=ignore_missing,
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
    avatar_scheme: str | Unset = UNSET,
    path: str | Unset = UNSET,
    with_counts: str | Unset = UNSET,
    follow_renames: str | Unset = UNSET,
    until: str | Unset = UNSET,
    avatar_size: str | Unset = UNSET,
    since: str | Unset = UNSET,
    merges: str | Unset = UNSET,
    ignore_missing: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetCommitsResponse200 | GetCommitsResponse400 | GetCommitsResponse401 | GetCommitsResponse404 | None:
    r"""Get commits

     Retrieve a page of commits from a given starting commit or \"between\" two commits. If no explicit
    commit is specified, the tip of the repository's default branch is assumed. commits may be
    identified by branch or tag name or by ID. A path may be supplied to restrict the returned commits
    to only those which affect that path.

    The authenticated user must have <b>REPO_READ</b> permission for the specified repository to call
    this resource.

    Args:
        project_key (str):
        repository_slug (str):
        avatar_scheme (str | Unset):
        path (str | Unset):
        with_counts (str | Unset):
        follow_renames (str | Unset):
        until (str | Unset):
        avatar_size (str | Unset):
        since (str | Unset):
        merges (str | Unset):
        ignore_missing (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCommitsResponse200 | GetCommitsResponse400 | GetCommitsResponse401 | GetCommitsResponse404
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        client=client,
        avatar_scheme=avatar_scheme,
        path=path,
        with_counts=with_counts,
        follow_renames=follow_renames,
        until=until,
        avatar_size=avatar_size,
        since=since,
        merges=merges,
        ignore_missing=ignore_missing,
        start=start,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    avatar_scheme: str | Unset = UNSET,
    path: str | Unset = UNSET,
    with_counts: str | Unset = UNSET,
    follow_renames: str | Unset = UNSET,
    until: str | Unset = UNSET,
    avatar_size: str | Unset = UNSET,
    since: str | Unset = UNSET,
    merges: str | Unset = UNSET,
    ignore_missing: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GetCommitsResponse200 | GetCommitsResponse400 | GetCommitsResponse401 | GetCommitsResponse404]:
    r"""Get commits

     Retrieve a page of commits from a given starting commit or \"between\" two commits. If no explicit
    commit is specified, the tip of the repository's default branch is assumed. commits may be
    identified by branch or tag name or by ID. A path may be supplied to restrict the returned commits
    to only those which affect that path.

    The authenticated user must have <b>REPO_READ</b> permission for the specified repository to call
    this resource.

    Args:
        project_key (str):
        repository_slug (str):
        avatar_scheme (str | Unset):
        path (str | Unset):
        with_counts (str | Unset):
        follow_renames (str | Unset):
        until (str | Unset):
        avatar_size (str | Unset):
        since (str | Unset):
        merges (str | Unset):
        ignore_missing (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCommitsResponse200 | GetCommitsResponse400 | GetCommitsResponse401 | GetCommitsResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        avatar_scheme=avatar_scheme,
        path=path,
        with_counts=with_counts,
        follow_renames=follow_renames,
        until=until,
        avatar_size=avatar_size,
        since=since,
        merges=merges,
        ignore_missing=ignore_missing,
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
    avatar_scheme: str | Unset = UNSET,
    path: str | Unset = UNSET,
    with_counts: str | Unset = UNSET,
    follow_renames: str | Unset = UNSET,
    until: str | Unset = UNSET,
    avatar_size: str | Unset = UNSET,
    since: str | Unset = UNSET,
    merges: str | Unset = UNSET,
    ignore_missing: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetCommitsResponse200 | GetCommitsResponse400 | GetCommitsResponse401 | GetCommitsResponse404 | None:
    r"""Get commits

     Retrieve a page of commits from a given starting commit or \"between\" two commits. If no explicit
    commit is specified, the tip of the repository's default branch is assumed. commits may be
    identified by branch or tag name or by ID. A path may be supplied to restrict the returned commits
    to only those which affect that path.

    The authenticated user must have <b>REPO_READ</b> permission for the specified repository to call
    this resource.

    Args:
        project_key (str):
        repository_slug (str):
        avatar_scheme (str | Unset):
        path (str | Unset):
        with_counts (str | Unset):
        follow_renames (str | Unset):
        until (str | Unset):
        avatar_size (str | Unset):
        since (str | Unset):
        merges (str | Unset):
        ignore_missing (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCommitsResponse200 | GetCommitsResponse400 | GetCommitsResponse401 | GetCommitsResponse404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            client=client,
            avatar_scheme=avatar_scheme,
            path=path,
            with_counts=with_counts,
            follow_renames=follow_renames,
            until=until,
            avatar_size=avatar_size,
            since=since,
            merges=merges,
            ignore_missing=ignore_missing,
            start=start,
            limit=limit,
        )
    ).parsed
