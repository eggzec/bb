from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_diff import RestDiff
from ...models.stream_diff_2_response_400 import StreamDiff2Response400
from ...models.stream_diff_2_response_401 import StreamDiff2Response401
from ...models.stream_diff_2_response_404 import StreamDiff2Response404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    path: str,
    *,
    avatar_scheme: str | Unset = UNSET,
    context_lines: str | Unset = UNSET,
    since_id: str | Unset = UNSET,
    src_path: str | Unset = UNSET,
    diff_type: str | Unset = UNSET,
    until_id: str | Unset = UNSET,
    whitespace: str | Unset = UNSET,
    with_comments: str | Unset = UNSET,
    avatar_size: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["avatarScheme"] = avatar_scheme

    params["contextLines"] = context_lines

    params["sinceId"] = since_id

    params["srcPath"] = src_path

    params["diffType"] = diff_type

    params["untilId"] = until_id

    params["whitespace"] = whitespace

    params["withComments"] = with_comments

    params["avatarSize"] = avatar_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/pull-requests/{pull_request_id}/diff/{path}".format(
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
) -> RestDiff | StreamDiff2Response400 | StreamDiff2Response401 | StreamDiff2Response404 | None:
    if response.status_code == 200:
        response_200 = RestDiff.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = StreamDiff2Response400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = StreamDiff2Response401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = StreamDiff2Response404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RestDiff | StreamDiff2Response400 | StreamDiff2Response401 | StreamDiff2Response404]:
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
    avatar_scheme: str | Unset = UNSET,
    context_lines: str | Unset = UNSET,
    since_id: str | Unset = UNSET,
    src_path: str | Unset = UNSET,
    diff_type: str | Unset = UNSET,
    until_id: str | Unset = UNSET,
    whitespace: str | Unset = UNSET,
    with_comments: str | Unset = UNSET,
    avatar_size: str | Unset = UNSET,
) -> Response[RestDiff | StreamDiff2Response400 | StreamDiff2Response401 | StreamDiff2Response404]:
    """Stream a diff within a pull request

     Streams a diff within a pull request.

    If the specified file has been copied, moved or renamed, the <code>srcPath</code> must also be
    specified to produce the correct diff.

    To stream a raw text representation of the diff, this endpoint can be called with the request header
    'Accept: text/plain'.

    Note: This RESTful endpoint is currently <i>not paged</i>. The server will internally apply a hard
    cap to the streamed lines, and it is not possible to request subsequent pages if that cap is
    exceeded.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        path (str):
        avatar_scheme (str | Unset):
        context_lines (str | Unset):
        since_id (str | Unset):
        src_path (str | Unset):
        diff_type (str | Unset):
        until_id (str | Unset):
        whitespace (str | Unset):
        with_comments (str | Unset):
        avatar_size (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestDiff | StreamDiff2Response400 | StreamDiff2Response401 | StreamDiff2Response404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
        path=path,
        avatar_scheme=avatar_scheme,
        context_lines=context_lines,
        since_id=since_id,
        src_path=src_path,
        diff_type=diff_type,
        until_id=until_id,
        whitespace=whitespace,
        with_comments=with_comments,
        avatar_size=avatar_size,
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
    avatar_scheme: str | Unset = UNSET,
    context_lines: str | Unset = UNSET,
    since_id: str | Unset = UNSET,
    src_path: str | Unset = UNSET,
    diff_type: str | Unset = UNSET,
    until_id: str | Unset = UNSET,
    whitespace: str | Unset = UNSET,
    with_comments: str | Unset = UNSET,
    avatar_size: str | Unset = UNSET,
) -> RestDiff | StreamDiff2Response400 | StreamDiff2Response401 | StreamDiff2Response404 | None:
    """Stream a diff within a pull request

     Streams a diff within a pull request.

    If the specified file has been copied, moved or renamed, the <code>srcPath</code> must also be
    specified to produce the correct diff.

    To stream a raw text representation of the diff, this endpoint can be called with the request header
    'Accept: text/plain'.

    Note: This RESTful endpoint is currently <i>not paged</i>. The server will internally apply a hard
    cap to the streamed lines, and it is not possible to request subsequent pages if that cap is
    exceeded.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        path (str):
        avatar_scheme (str | Unset):
        context_lines (str | Unset):
        since_id (str | Unset):
        src_path (str | Unset):
        diff_type (str | Unset):
        until_id (str | Unset):
        whitespace (str | Unset):
        with_comments (str | Unset):
        avatar_size (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestDiff | StreamDiff2Response400 | StreamDiff2Response401 | StreamDiff2Response404
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
        path=path,
        client=client,
        avatar_scheme=avatar_scheme,
        context_lines=context_lines,
        since_id=since_id,
        src_path=src_path,
        diff_type=diff_type,
        until_id=until_id,
        whitespace=whitespace,
        with_comments=with_comments,
        avatar_size=avatar_size,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    path: str,
    *,
    client: AuthenticatedClient | Client,
    avatar_scheme: str | Unset = UNSET,
    context_lines: str | Unset = UNSET,
    since_id: str | Unset = UNSET,
    src_path: str | Unset = UNSET,
    diff_type: str | Unset = UNSET,
    until_id: str | Unset = UNSET,
    whitespace: str | Unset = UNSET,
    with_comments: str | Unset = UNSET,
    avatar_size: str | Unset = UNSET,
) -> Response[RestDiff | StreamDiff2Response400 | StreamDiff2Response401 | StreamDiff2Response404]:
    """Stream a diff within a pull request

     Streams a diff within a pull request.

    If the specified file has been copied, moved or renamed, the <code>srcPath</code> must also be
    specified to produce the correct diff.

    To stream a raw text representation of the diff, this endpoint can be called with the request header
    'Accept: text/plain'.

    Note: This RESTful endpoint is currently <i>not paged</i>. The server will internally apply a hard
    cap to the streamed lines, and it is not possible to request subsequent pages if that cap is
    exceeded.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        path (str):
        avatar_scheme (str | Unset):
        context_lines (str | Unset):
        since_id (str | Unset):
        src_path (str | Unset):
        diff_type (str | Unset):
        until_id (str | Unset):
        whitespace (str | Unset):
        with_comments (str | Unset):
        avatar_size (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestDiff | StreamDiff2Response400 | StreamDiff2Response401 | StreamDiff2Response404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
        path=path,
        avatar_scheme=avatar_scheme,
        context_lines=context_lines,
        since_id=since_id,
        src_path=src_path,
        diff_type=diff_type,
        until_id=until_id,
        whitespace=whitespace,
        with_comments=with_comments,
        avatar_size=avatar_size,
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
    avatar_scheme: str | Unset = UNSET,
    context_lines: str | Unset = UNSET,
    since_id: str | Unset = UNSET,
    src_path: str | Unset = UNSET,
    diff_type: str | Unset = UNSET,
    until_id: str | Unset = UNSET,
    whitespace: str | Unset = UNSET,
    with_comments: str | Unset = UNSET,
    avatar_size: str | Unset = UNSET,
) -> RestDiff | StreamDiff2Response400 | StreamDiff2Response401 | StreamDiff2Response404 | None:
    """Stream a diff within a pull request

     Streams a diff within a pull request.

    If the specified file has been copied, moved or renamed, the <code>srcPath</code> must also be
    specified to produce the correct diff.

    To stream a raw text representation of the diff, this endpoint can be called with the request header
    'Accept: text/plain'.

    Note: This RESTful endpoint is currently <i>not paged</i>. The server will internally apply a hard
    cap to the streamed lines, and it is not possible to request subsequent pages if that cap is
    exceeded.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        path (str):
        avatar_scheme (str | Unset):
        context_lines (str | Unset):
        since_id (str | Unset):
        src_path (str | Unset):
        diff_type (str | Unset):
        until_id (str | Unset):
        whitespace (str | Unset):
        with_comments (str | Unset):
        avatar_size (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestDiff | StreamDiff2Response400 | StreamDiff2Response401 | StreamDiff2Response404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            pull_request_id=pull_request_id,
            path=path,
            client=client,
            avatar_scheme=avatar_scheme,
            context_lines=context_lines,
            since_id=since_id,
            src_path=src_path,
            diff_type=diff_type,
            until_id=until_id,
            whitespace=whitespace,
            with_comments=with_comments,
            avatar_size=avatar_size,
        )
    ).parsed
