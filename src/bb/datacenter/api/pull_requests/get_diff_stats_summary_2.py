from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_diff_stats_summary_2_response_401 import GetDiffStatsSummary2Response401
from ...models.get_diff_stats_summary_2_response_404 import GetDiffStatsSummary2Response404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    path: str,
    *,
    since_id: str | Unset = UNSET,
    src_path: str | Unset = UNSET,
    until_id: str | Unset = UNSET,
    whitespace: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["sinceId"] = since_id

    params["srcPath"] = src_path

    params["untilId"] = until_id

    params["whitespace"] = whitespace

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/pull-requests/{pull_request_id}/diff-stats-summary/{path}".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            pull_request_id=quote(str(pull_request_id), safe=""),
            path=quote(str(path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetDiffStatsSummary2Response401 | GetDiffStatsSummary2Response404 | None:
    if response.status_code == 200:
        response_200 = response.json()
        return response_200

    if response.status_code == 401:
        response_401 = GetDiffStatsSummary2Response401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetDiffStatsSummary2Response404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetDiffStatsSummary2Response401 | GetDiffStatsSummary2Response404]:
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
    path: str,
    *,
    client: AuthenticatedClient | Client,
    since_id: str | Unset = UNSET,
    src_path: str | Unset = UNSET,
    until_id: str | Unset = UNSET,
    whitespace: str | Unset = UNSET,
) -> Response[Any | GetDiffStatsSummary2Response401 | GetDiffStatsSummary2Response404]:
    """Get diff stats summary for pull request

     Retrieve the diff stats summary for the given Pull Request.

    The stats summary include the total number of modified files, added lines, and deleted lines.

    Note: The authenticated user must have <strong>REPO_READ</strong> permission for the repository that
    this pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        path (str):
        since_id (str | Unset):
        src_path (str | Unset):
        until_id (str | Unset):
        whitespace (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetDiffStatsSummary2Response401 | GetDiffStatsSummary2Response404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
        path=path,
        since_id=since_id,
        src_path=src_path,
        until_id=until_id,
        whitespace=whitespace,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    path: str,
    *,
    client: AuthenticatedClient | Client,
    since_id: str | Unset = UNSET,
    src_path: str | Unset = UNSET,
    until_id: str | Unset = UNSET,
    whitespace: str | Unset = UNSET,
) -> Any | GetDiffStatsSummary2Response401 | GetDiffStatsSummary2Response404 | None:
    """Get diff stats summary for pull request

     Retrieve the diff stats summary for the given Pull Request.

    The stats summary include the total number of modified files, added lines, and deleted lines.

    Note: The authenticated user must have <strong>REPO_READ</strong> permission for the repository that
    this pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        path (str):
        since_id (str | Unset):
        src_path (str | Unset):
        until_id (str | Unset):
        whitespace (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetDiffStatsSummary2Response401 | GetDiffStatsSummary2Response404
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
        path=path,
        client=client,
        since_id=since_id,
        src_path=src_path,
        until_id=until_id,
        whitespace=whitespace,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    path: str,
    *,
    client: AuthenticatedClient | Client,
    since_id: str | Unset = UNSET,
    src_path: str | Unset = UNSET,
    until_id: str | Unset = UNSET,
    whitespace: str | Unset = UNSET,
) -> Response[Any | GetDiffStatsSummary2Response401 | GetDiffStatsSummary2Response404]:
    """Get diff stats summary for pull request

     Retrieve the diff stats summary for the given Pull Request.

    The stats summary include the total number of modified files, added lines, and deleted lines.

    Note: The authenticated user must have <strong>REPO_READ</strong> permission for the repository that
    this pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        path (str):
        since_id (str | Unset):
        src_path (str | Unset):
        until_id (str | Unset):
        whitespace (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetDiffStatsSummary2Response401 | GetDiffStatsSummary2Response404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
        path=path,
        since_id=since_id,
        src_path=src_path,
        until_id=until_id,
        whitespace=whitespace,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    path: str,
    *,
    client: AuthenticatedClient | Client,
    since_id: str | Unset = UNSET,
    src_path: str | Unset = UNSET,
    until_id: str | Unset = UNSET,
    whitespace: str | Unset = UNSET,
) -> Any | GetDiffStatsSummary2Response401 | GetDiffStatsSummary2Response404 | None:
    """Get diff stats summary for pull request

     Retrieve the diff stats summary for the given Pull Request.

    The stats summary include the total number of modified files, added lines, and deleted lines.

    Note: The authenticated user must have <strong>REPO_READ</strong> permission for the repository that
    this pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        path (str):
        since_id (str | Unset):
        src_path (str | Unset):
        until_id (str | Unset):
        whitespace (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetDiffStatsSummary2Response401 | GetDiffStatsSummary2Response404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            pull_request_id=pull_request_id,
            path=path,
            client=client,
            since_id=since_id,
            src_path=src_path,
            until_id=until_id,
            whitespace=whitespace,
        )
    ).parsed
