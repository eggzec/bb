from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_diff_stats_summary_response_400 import GetDiffStatsSummaryResponse400
from ...models.get_diff_stats_summary_response_401 import GetDiffStatsSummaryResponse401
from ...models.get_diff_stats_summary_response_404 import GetDiffStatsSummaryResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    path: str,
    *,
    src_path: str | Unset = UNSET,
    auto_src_path: str | Unset = UNSET,
    whitespace: str | Unset = UNSET,
    since: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["srcPath"] = src_path

    params["autoSrcPath"] = auto_src_path

    params["whitespace"] = whitespace

    params["since"] = since

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/commits/{commit_id}/diff-stats-summary/{path}".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            commit_id=quote(str(commit_id), safe=""),
            path=quote(str(path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetDiffStatsSummaryResponse400 | GetDiffStatsSummaryResponse401 | GetDiffStatsSummaryResponse404 | None:
    if response.status_code == 200:
        response_200 = response.json()
        return response_200

    if response.status_code == 400:
        response_400 = GetDiffStatsSummaryResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetDiffStatsSummaryResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetDiffStatsSummaryResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetDiffStatsSummaryResponse400 | GetDiffStatsSummaryResponse401 | GetDiffStatsSummaryResponse404]:
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
    path: str,
    *,
    client: AuthenticatedClient | Client,
    src_path: str | Unset = UNSET,
    auto_src_path: str | Unset = UNSET,
    whitespace: str | Unset = UNSET,
    since: str | Unset = UNSET,
) -> Response[Any | GetDiffStatsSummaryResponse400 | GetDiffStatsSummaryResponse401 | GetDiffStatsSummaryResponse404]:
    """Get diff stats summary between revisions

     Retrieve the diff stats summary for a commit.

    The stats summary include the total number of modified files, added lines, and deleted lines.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        path (str):
        src_path (str | Unset):
        auto_src_path (str | Unset):
        whitespace (str | Unset):
        since (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetDiffStatsSummaryResponse400 | GetDiffStatsSummaryResponse401 | GetDiffStatsSummaryResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        path=path,
        src_path=src_path,
        auto_src_path=auto_src_path,
        whitespace=whitespace,
        since=since,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    path: str,
    *,
    client: AuthenticatedClient | Client,
    src_path: str | Unset = UNSET,
    auto_src_path: str | Unset = UNSET,
    whitespace: str | Unset = UNSET,
    since: str | Unset = UNSET,
) -> Any | GetDiffStatsSummaryResponse400 | GetDiffStatsSummaryResponse401 | GetDiffStatsSummaryResponse404 | None:
    """Get diff stats summary between revisions

     Retrieve the diff stats summary for a commit.

    The stats summary include the total number of modified files, added lines, and deleted lines.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        path (str):
        src_path (str | Unset):
        auto_src_path (str | Unset):
        whitespace (str | Unset):
        since (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetDiffStatsSummaryResponse400 | GetDiffStatsSummaryResponse401 | GetDiffStatsSummaryResponse404
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        path=path,
        client=client,
        src_path=src_path,
        auto_src_path=auto_src_path,
        whitespace=whitespace,
        since=since,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    path: str,
    *,
    client: AuthenticatedClient | Client,
    src_path: str | Unset = UNSET,
    auto_src_path: str | Unset = UNSET,
    whitespace: str | Unset = UNSET,
    since: str | Unset = UNSET,
) -> Response[Any | GetDiffStatsSummaryResponse400 | GetDiffStatsSummaryResponse401 | GetDiffStatsSummaryResponse404]:
    """Get diff stats summary between revisions

     Retrieve the diff stats summary for a commit.

    The stats summary include the total number of modified files, added lines, and deleted lines.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        path (str):
        src_path (str | Unset):
        auto_src_path (str | Unset):
        whitespace (str | Unset):
        since (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetDiffStatsSummaryResponse400 | GetDiffStatsSummaryResponse401 | GetDiffStatsSummaryResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        path=path,
        src_path=src_path,
        auto_src_path=auto_src_path,
        whitespace=whitespace,
        since=since,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    path: str,
    *,
    client: AuthenticatedClient | Client,
    src_path: str | Unset = UNSET,
    auto_src_path: str | Unset = UNSET,
    whitespace: str | Unset = UNSET,
    since: str | Unset = UNSET,
) -> Any | GetDiffStatsSummaryResponse400 | GetDiffStatsSummaryResponse401 | GetDiffStatsSummaryResponse404 | None:
    """Get diff stats summary between revisions

     Retrieve the diff stats summary for a commit.

    The stats summary include the total number of modified files, added lines, and deleted lines.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        path (str):
        src_path (str | Unset):
        auto_src_path (str | Unset):
        whitespace (str | Unset):
        since (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetDiffStatsSummaryResponse400 | GetDiffStatsSummaryResponse401 | GetDiffStatsSummaryResponse404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            commit_id=commit_id,
            path=path,
            client=client,
            src_path=src_path,
            auto_src_path=auto_src_path,
            whitespace=whitespace,
            since=since,
        )
    ).parsed
