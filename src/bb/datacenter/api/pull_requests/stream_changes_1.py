from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_change import RestChange
from ...models.stream_changes_1_response_401 import StreamChanges1Response401
from ...models.stream_changes_1_response_404 import StreamChanges1Response404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    *,
    since_id: str | Unset = UNSET,
    change_scope: str | Unset = UNSET,
    until_id: str | Unset = UNSET,
    with_comments: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["sinceId"] = since_id

    params["changeScope"] = change_scope

    params["untilId"] = until_id

    params["withComments"] = with_comments

    params["start"] = start

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/pull-requests/{pull_request_id}/changes".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            pull_request_id=quote(str(pull_request_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RestChange | StreamChanges1Response401 | StreamChanges1Response404 | None:
    if response.status_code == 200:
        response_200 = RestChange.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = StreamChanges1Response401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = StreamChanges1Response404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RestChange | StreamChanges1Response401 | StreamChanges1Response404]:
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
    since_id: str | Unset = UNSET,
    change_scope: str | Unset = UNSET,
    until_id: str | Unset = UNSET,
    with_comments: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[RestChange | StreamChanges1Response401 | StreamChanges1Response404]:
    """Gets pull request changes

     Gets changes for the specified PullRequest.

    If the changeScope query parameter is set to 'UNREVIEWED', the application will attempt to stream
    unreviewed changes based on the lastReviewedCommit of the current user, which are the changes
    between the lastReviewedCommit and the latest commit of the source branch. The current user is
    considered to <i>not</i> have any unreviewed changes for the pull request when the
    lastReviewedCommit is either null (everything is unreviewed, so all changes are streamed), equal to
    the latest commit of the source branch (everything is reviewed), or no longer on the source branch
    (the source branch has been rebased). In these cases, the application will fall back to streaming
    all changes (the default), which is the effective diff for the pull request. The type of changes
    streamed can be determined by the changeScope parameter included in the properties map of the
    response.

    Note: This resource is currently <i>not paged</i>. The server will return at most one page. The
    server will truncate the number of changes to either the request's page limit or an internal
    maximum, whichever is smaller. The start parameter of the page request is also ignored.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        since_id (str | Unset):
        change_scope (str | Unset):
        until_id (str | Unset):
        with_comments (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestChange | StreamChanges1Response401 | StreamChanges1Response404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
        since_id=since_id,
        change_scope=change_scope,
        until_id=until_id,
        with_comments=with_comments,
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
    since_id: str | Unset = UNSET,
    change_scope: str | Unset = UNSET,
    until_id: str | Unset = UNSET,
    with_comments: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> RestChange | StreamChanges1Response401 | StreamChanges1Response404 | None:
    """Gets pull request changes

     Gets changes for the specified PullRequest.

    If the changeScope query parameter is set to 'UNREVIEWED', the application will attempt to stream
    unreviewed changes based on the lastReviewedCommit of the current user, which are the changes
    between the lastReviewedCommit and the latest commit of the source branch. The current user is
    considered to <i>not</i> have any unreviewed changes for the pull request when the
    lastReviewedCommit is either null (everything is unreviewed, so all changes are streamed), equal to
    the latest commit of the source branch (everything is reviewed), or no longer on the source branch
    (the source branch has been rebased). In these cases, the application will fall back to streaming
    all changes (the default), which is the effective diff for the pull request. The type of changes
    streamed can be determined by the changeScope parameter included in the properties map of the
    response.

    Note: This resource is currently <i>not paged</i>. The server will return at most one page. The
    server will truncate the number of changes to either the request's page limit or an internal
    maximum, whichever is smaller. The start parameter of the page request is also ignored.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        since_id (str | Unset):
        change_scope (str | Unset):
        until_id (str | Unset):
        with_comments (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestChange | StreamChanges1Response401 | StreamChanges1Response404
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
        client=client,
        since_id=since_id,
        change_scope=change_scope,
        until_id=until_id,
        with_comments=with_comments,
        start=start,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    *,
    client: AuthenticatedClient | Client,
    since_id: str | Unset = UNSET,
    change_scope: str | Unset = UNSET,
    until_id: str | Unset = UNSET,
    with_comments: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[RestChange | StreamChanges1Response401 | StreamChanges1Response404]:
    """Gets pull request changes

     Gets changes for the specified PullRequest.

    If the changeScope query parameter is set to 'UNREVIEWED', the application will attempt to stream
    unreviewed changes based on the lastReviewedCommit of the current user, which are the changes
    between the lastReviewedCommit and the latest commit of the source branch. The current user is
    considered to <i>not</i> have any unreviewed changes for the pull request when the
    lastReviewedCommit is either null (everything is unreviewed, so all changes are streamed), equal to
    the latest commit of the source branch (everything is reviewed), or no longer on the source branch
    (the source branch has been rebased). In these cases, the application will fall back to streaming
    all changes (the default), which is the effective diff for the pull request. The type of changes
    streamed can be determined by the changeScope parameter included in the properties map of the
    response.

    Note: This resource is currently <i>not paged</i>. The server will return at most one page. The
    server will truncate the number of changes to either the request's page limit or an internal
    maximum, whichever is smaller. The start parameter of the page request is also ignored.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        since_id (str | Unset):
        change_scope (str | Unset):
        until_id (str | Unset):
        with_comments (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestChange | StreamChanges1Response401 | StreamChanges1Response404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
        since_id=since_id,
        change_scope=change_scope,
        until_id=until_id,
        with_comments=with_comments,
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
    since_id: str | Unset = UNSET,
    change_scope: str | Unset = UNSET,
    until_id: str | Unset = UNSET,
    with_comments: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> RestChange | StreamChanges1Response401 | StreamChanges1Response404 | None:
    """Gets pull request changes

     Gets changes for the specified PullRequest.

    If the changeScope query parameter is set to 'UNREVIEWED', the application will attempt to stream
    unreviewed changes based on the lastReviewedCommit of the current user, which are the changes
    between the lastReviewedCommit and the latest commit of the source branch. The current user is
    considered to <i>not</i> have any unreviewed changes for the pull request when the
    lastReviewedCommit is either null (everything is unreviewed, so all changes are streamed), equal to
    the latest commit of the source branch (everything is reviewed), or no longer on the source branch
    (the source branch has been rebased). In these cases, the application will fall back to streaming
    all changes (the default), which is the effective diff for the pull request. The type of changes
    streamed can be determined by the changeScope parameter included in the properties map of the
    response.

    Note: This resource is currently <i>not paged</i>. The server will return at most one page. The
    server will truncate the number of changes to either the request's page limit or an internal
    maximum, whichever is smaller. The start parameter of the page request is also ignored.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        since_id (str | Unset):
        change_scope (str | Unset):
        until_id (str | Unset):
        with_comments (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestChange | StreamChanges1Response401 | StreamChanges1Response404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            pull_request_id=pull_request_id,
            client=client,
            since_id=since_id,
            change_scope=change_scope,
            until_id=until_id,
            with_comments=with_comments,
            start=start,
            limit=limit,
        )
    ).parsed
