from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_diff import RestDiff
from ...models.stream_diff_1_response_404 import StreamDiff1Response404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    path: str,
    *,
    context_lines: str | Unset = UNSET,
    from_repo: str | Unset = UNSET,
    src_path: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    whitespace: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["contextLines"] = context_lines

    params["fromRepo"] = from_repo

    params["srcPath"] = src_path

    params["from"] = from_

    params["to"] = to

    params["whitespace"] = whitespace

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/compare/diff{path}".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            path=quote(str(path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RestDiff | StreamDiff1Response404 | None:
    if response.status_code == 200:
        response_200 = RestDiff.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = StreamDiff1Response404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RestDiff | StreamDiff1Response404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    repository_slug: str,
    path: str,
    *,
    client: AuthenticatedClient | Client,
    context_lines: str | Unset = UNSET,
    from_repo: str | Unset = UNSET,
    src_path: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    whitespace: str | Unset = UNSET,
) -> Response[RestDiff | StreamDiff1Response404]:
    """Get diff between commits

     Gets a diff of the changes available in the <code>from</code> commit but not in the <code> to</code>
    commit.

    If either the <code> from</code> or <code> to</code> commit are not specified, they will be replaced
    by the default branch of their containing repository.

    Args:
        project_key (str):
        repository_slug (str):
        path (str):
        context_lines (str | Unset):
        from_repo (str | Unset):
        src_path (str | Unset):
        from_ (str | Unset):
        to (str | Unset):
        whitespace (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestDiff | StreamDiff1Response404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        path=path,
        context_lines=context_lines,
        from_repo=from_repo,
        src_path=src_path,
        from_=from_,
        to=to,
        whitespace=whitespace,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    repository_slug: str,
    path: str,
    *,
    client: AuthenticatedClient | Client,
    context_lines: str | Unset = UNSET,
    from_repo: str | Unset = UNSET,
    src_path: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    whitespace: str | Unset = UNSET,
) -> RestDiff | StreamDiff1Response404 | None:
    """Get diff between commits

     Gets a diff of the changes available in the <code>from</code> commit but not in the <code> to</code>
    commit.

    If either the <code> from</code> or <code> to</code> commit are not specified, they will be replaced
    by the default branch of their containing repository.

    Args:
        project_key (str):
        repository_slug (str):
        path (str):
        context_lines (str | Unset):
        from_repo (str | Unset):
        src_path (str | Unset):
        from_ (str | Unset):
        to (str | Unset):
        whitespace (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestDiff | StreamDiff1Response404
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        path=path,
        client=client,
        context_lines=context_lines,
        from_repo=from_repo,
        src_path=src_path,
        from_=from_,
        to=to,
        whitespace=whitespace,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    path: str,
    *,
    client: AuthenticatedClient | Client,
    context_lines: str | Unset = UNSET,
    from_repo: str | Unset = UNSET,
    src_path: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    whitespace: str | Unset = UNSET,
) -> Response[RestDiff | StreamDiff1Response404]:
    """Get diff between commits

     Gets a diff of the changes available in the <code>from</code> commit but not in the <code> to</code>
    commit.

    If either the <code> from</code> or <code> to</code> commit are not specified, they will be replaced
    by the default branch of their containing repository.

    Args:
        project_key (str):
        repository_slug (str):
        path (str):
        context_lines (str | Unset):
        from_repo (str | Unset):
        src_path (str | Unset):
        from_ (str | Unset):
        to (str | Unset):
        whitespace (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestDiff | StreamDiff1Response404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        path=path,
        context_lines=context_lines,
        from_repo=from_repo,
        src_path=src_path,
        from_=from_,
        to=to,
        whitespace=whitespace,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    path: str,
    *,
    client: AuthenticatedClient | Client,
    context_lines: str | Unset = UNSET,
    from_repo: str | Unset = UNSET,
    src_path: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    whitespace: str | Unset = UNSET,
) -> RestDiff | StreamDiff1Response404 | None:
    """Get diff between commits

     Gets a diff of the changes available in the <code>from</code> commit but not in the <code> to</code>
    commit.

    If either the <code> from</code> or <code> to</code> commit are not specified, they will be replaced
    by the default branch of their containing repository.

    Args:
        project_key (str):
        repository_slug (str):
        path (str):
        context_lines (str | Unset):
        from_repo (str | Unset):
        src_path (str | Unset):
        from_ (str | Unset):
        to (str | Unset):
        whitespace (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestDiff | StreamDiff1Response404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            path=path,
            client=client,
            context_lines=context_lines,
            from_repo=from_repo,
            src_path=src_path,
            from_=from_,
            to=to,
            whitespace=whitespace,
        )
    ).parsed
