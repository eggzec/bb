from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.stream_raw_diff_response_400 import StreamRawDiffResponse400
from ...models.stream_raw_diff_response_401 import StreamRawDiffResponse401
from ...models.stream_raw_diff_response_404 import StreamRawDiffResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    *,
    context_lines: str | Unset = UNSET,
    src_path: str | Unset = UNSET,
    until: str | Unset = UNSET,
    whitespace: str | Unset = UNSET,
    since: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["contextLines"] = context_lines

    params["srcPath"] = src_path

    params["until"] = until

    params["whitespace"] = whitespace

    params["since"] = since

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/diff".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | StreamRawDiffResponse400 | StreamRawDiffResponse401 | StreamRawDiffResponse404 | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 400:
        response_400 = StreamRawDiffResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = StreamRawDiffResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = StreamRawDiffResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | StreamRawDiffResponse400 | StreamRawDiffResponse401 | StreamRawDiffResponse404]:
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
    context_lines: str | Unset = UNSET,
    src_path: str | Unset = UNSET,
    until: str | Unset = UNSET,
    whitespace: str | Unset = UNSET,
    since: str | Unset = UNSET,
) -> Response[Any | StreamRawDiffResponse400 | StreamRawDiffResponse401 | StreamRawDiffResponse404]:
    """Get raw diff for path

     Stream the raw diff between two provided revisions.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        context_lines (str | Unset):
        src_path (str | Unset):
        until (str | Unset):
        whitespace (str | Unset):
        since (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | StreamRawDiffResponse400 | StreamRawDiffResponse401 | StreamRawDiffResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        context_lines=context_lines,
        src_path=src_path,
        until=until,
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
    *,
    client: AuthenticatedClient | Client,
    context_lines: str | Unset = UNSET,
    src_path: str | Unset = UNSET,
    until: str | Unset = UNSET,
    whitespace: str | Unset = UNSET,
    since: str | Unset = UNSET,
) -> Any | StreamRawDiffResponse400 | StreamRawDiffResponse401 | StreamRawDiffResponse404 | None:
    """Get raw diff for path

     Stream the raw diff between two provided revisions.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        context_lines (str | Unset):
        src_path (str | Unset):
        until (str | Unset):
        whitespace (str | Unset):
        since (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | StreamRawDiffResponse400 | StreamRawDiffResponse401 | StreamRawDiffResponse404
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        client=client,
        context_lines=context_lines,
        src_path=src_path,
        until=until,
        whitespace=whitespace,
        since=since,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    context_lines: str | Unset = UNSET,
    src_path: str | Unset = UNSET,
    until: str | Unset = UNSET,
    whitespace: str | Unset = UNSET,
    since: str | Unset = UNSET,
) -> Response[Any | StreamRawDiffResponse400 | StreamRawDiffResponse401 | StreamRawDiffResponse404]:
    """Get raw diff for path

     Stream the raw diff between two provided revisions.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        context_lines (str | Unset):
        src_path (str | Unset):
        until (str | Unset):
        whitespace (str | Unset):
        since (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | StreamRawDiffResponse400 | StreamRawDiffResponse401 | StreamRawDiffResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        context_lines=context_lines,
        src_path=src_path,
        until=until,
        whitespace=whitespace,
        since=since,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    context_lines: str | Unset = UNSET,
    src_path: str | Unset = UNSET,
    until: str | Unset = UNSET,
    whitespace: str | Unset = UNSET,
    since: str | Unset = UNSET,
) -> Any | StreamRawDiffResponse400 | StreamRawDiffResponse401 | StreamRawDiffResponse404 | None:
    """Get raw diff for path

     Stream the raw diff between two provided revisions.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        context_lines (str | Unset):
        src_path (str | Unset):
        until (str | Unset):
        whitespace (str | Unset):
        since (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | StreamRawDiffResponse400 | StreamRawDiffResponse401 | StreamRawDiffResponse404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            client=client,
            context_lines=context_lines,
            src_path=src_path,
            until=until,
            whitespace=whitespace,
            since=since,
        )
    ).parsed
