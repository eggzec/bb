from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_diff import RestDiff
from ...models.stream_diff_response_400 import StreamDiffResponse400
from ...models.stream_diff_response_401 import StreamDiffResponse401
from ...models.stream_diff_response_404 import StreamDiffResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    path: str,
    *,
    src_path: str | Unset = UNSET,
    avatar_size: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    avatar_scheme: str | Unset = UNSET,
    context_lines: str | Unset = UNSET,
    auto_src_path: str | Unset = UNSET,
    whitespace: str | Unset = UNSET,
    with_comments: str | Unset = UNSET,
    since: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["srcPath"] = src_path

    params["avatarSize"] = avatar_size

    params["filter"] = filter_

    params["avatarScheme"] = avatar_scheme

    params["contextLines"] = context_lines

    params["autoSrcPath"] = auto_src_path

    params["whitespace"] = whitespace

    params["withComments"] = with_comments

    params["since"] = since

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/commits/{commit_id}/diff/{path}".format(
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
) -> RestDiff | StreamDiffResponse400 | StreamDiffResponse401 | StreamDiffResponse404 | None:
    if response.status_code == 200:
        response_200 = RestDiff.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = StreamDiffResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = StreamDiffResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = StreamDiffResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RestDiff | StreamDiffResponse400 | StreamDiffResponse401 | StreamDiffResponse404]:
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
    avatar_size: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    avatar_scheme: str | Unset = UNSET,
    context_lines: str | Unset = UNSET,
    auto_src_path: str | Unset = UNSET,
    whitespace: str | Unset = UNSET,
    with_comments: str | Unset = UNSET,
    since: str | Unset = UNSET,
) -> Response[RestDiff | StreamDiffResponse400 | StreamDiffResponse401 | StreamDiffResponse404]:
    r"""Get diff between revisions

     Retrieve the diff between two provided revisions.

    To stream a raw text representation of the diff, this endpoint can be called with the request header
    'Accept: text/plain'.

    Note:</strong> This resource is currently <i>not paged</i>. The server will internally apply a hard
    cap to the streamed lines, and it is not possible to request subsequent pages if that cap is
    exceeded. In the event that the cap is reached, the diff will be cut short and one or more {@code
    truncated} flags will be set to true on the \"segments\", \"hunks\" and \"diffs\" properties, as
    well as the top-level object, in the returned JSON response.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        path (str):
        src_path (str | Unset):
        avatar_size (str | Unset):
        filter_ (str | Unset):
        avatar_scheme (str | Unset):
        context_lines (str | Unset):
        auto_src_path (str | Unset):
        whitespace (str | Unset):
        with_comments (str | Unset):
        since (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestDiff | StreamDiffResponse400 | StreamDiffResponse401 | StreamDiffResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        path=path,
        src_path=src_path,
        avatar_size=avatar_size,
        filter_=filter_,
        avatar_scheme=avatar_scheme,
        context_lines=context_lines,
        auto_src_path=auto_src_path,
        whitespace=whitespace,
        with_comments=with_comments,
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
    avatar_size: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    avatar_scheme: str | Unset = UNSET,
    context_lines: str | Unset = UNSET,
    auto_src_path: str | Unset = UNSET,
    whitespace: str | Unset = UNSET,
    with_comments: str | Unset = UNSET,
    since: str | Unset = UNSET,
) -> RestDiff | StreamDiffResponse400 | StreamDiffResponse401 | StreamDiffResponse404 | None:
    r"""Get diff between revisions

     Retrieve the diff between two provided revisions.

    To stream a raw text representation of the diff, this endpoint can be called with the request header
    'Accept: text/plain'.

    Note:</strong> This resource is currently <i>not paged</i>. The server will internally apply a hard
    cap to the streamed lines, and it is not possible to request subsequent pages if that cap is
    exceeded. In the event that the cap is reached, the diff will be cut short and one or more {@code
    truncated} flags will be set to true on the \"segments\", \"hunks\" and \"diffs\" properties, as
    well as the top-level object, in the returned JSON response.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        path (str):
        src_path (str | Unset):
        avatar_size (str | Unset):
        filter_ (str | Unset):
        avatar_scheme (str | Unset):
        context_lines (str | Unset):
        auto_src_path (str | Unset):
        whitespace (str | Unset):
        with_comments (str | Unset):
        since (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestDiff | StreamDiffResponse400 | StreamDiffResponse401 | StreamDiffResponse404
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        path=path,
        client=client,
        src_path=src_path,
        avatar_size=avatar_size,
        filter_=filter_,
        avatar_scheme=avatar_scheme,
        context_lines=context_lines,
        auto_src_path=auto_src_path,
        whitespace=whitespace,
        with_comments=with_comments,
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
    avatar_size: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    avatar_scheme: str | Unset = UNSET,
    context_lines: str | Unset = UNSET,
    auto_src_path: str | Unset = UNSET,
    whitespace: str | Unset = UNSET,
    with_comments: str | Unset = UNSET,
    since: str | Unset = UNSET,
) -> Response[RestDiff | StreamDiffResponse400 | StreamDiffResponse401 | StreamDiffResponse404]:
    r"""Get diff between revisions

     Retrieve the diff between two provided revisions.

    To stream a raw text representation of the diff, this endpoint can be called with the request header
    'Accept: text/plain'.

    Note:</strong> This resource is currently <i>not paged</i>. The server will internally apply a hard
    cap to the streamed lines, and it is not possible to request subsequent pages if that cap is
    exceeded. In the event that the cap is reached, the diff will be cut short and one or more {@code
    truncated} flags will be set to true on the \"segments\", \"hunks\" and \"diffs\" properties, as
    well as the top-level object, in the returned JSON response.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        path (str):
        src_path (str | Unset):
        avatar_size (str | Unset):
        filter_ (str | Unset):
        avatar_scheme (str | Unset):
        context_lines (str | Unset):
        auto_src_path (str | Unset):
        whitespace (str | Unset):
        with_comments (str | Unset):
        since (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestDiff | StreamDiffResponse400 | StreamDiffResponse401 | StreamDiffResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        path=path,
        src_path=src_path,
        avatar_size=avatar_size,
        filter_=filter_,
        avatar_scheme=avatar_scheme,
        context_lines=context_lines,
        auto_src_path=auto_src_path,
        whitespace=whitespace,
        with_comments=with_comments,
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
    avatar_size: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    avatar_scheme: str | Unset = UNSET,
    context_lines: str | Unset = UNSET,
    auto_src_path: str | Unset = UNSET,
    whitespace: str | Unset = UNSET,
    with_comments: str | Unset = UNSET,
    since: str | Unset = UNSET,
) -> RestDiff | StreamDiffResponse400 | StreamDiffResponse401 | StreamDiffResponse404 | None:
    r"""Get diff between revisions

     Retrieve the diff between two provided revisions.

    To stream a raw text representation of the diff, this endpoint can be called with the request header
    'Accept: text/plain'.

    Note:</strong> This resource is currently <i>not paged</i>. The server will internally apply a hard
    cap to the streamed lines, and it is not possible to request subsequent pages if that cap is
    exceeded. In the event that the cap is reached, the diff will be cut short and one or more {@code
    truncated} flags will be set to true on the \"segments\", \"hunks\" and \"diffs\" properties, as
    well as the top-level object, in the returned JSON response.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        path (str):
        src_path (str | Unset):
        avatar_size (str | Unset):
        filter_ (str | Unset):
        avatar_scheme (str | Unset):
        context_lines (str | Unset):
        auto_src_path (str | Unset):
        whitespace (str | Unset):
        with_comments (str | Unset):
        since (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestDiff | StreamDiffResponse400 | StreamDiffResponse401 | StreamDiffResponse404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            commit_id=commit_id,
            path=path,
            client=client,
            src_path=src_path,
            avatar_size=avatar_size,
            filter_=filter_,
            avatar_scheme=avatar_scheme,
            context_lines=context_lines,
            auto_src_path=auto_src_path,
            whitespace=whitespace,
            with_comments=with_comments,
            since=since,
        )
    ).parsed
