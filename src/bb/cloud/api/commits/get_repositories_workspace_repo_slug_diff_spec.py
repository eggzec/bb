from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...types import UNSET, Response, Unset

__all__ = [
    "sync_detailed",
    "asyncio_detailed",
    "sync",
    "asyncio",
]


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    spec: str,
    *,
    context: int | Unset = UNSET,
    path: str | Unset = UNSET,
    ignore_whitespace: bool | Unset = UNSET,
    binary: bool | Unset = UNSET,
    renames: bool | Unset = UNSET,
    merge: bool | Unset = UNSET,
    topic: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["context"] = context

    params["path"] = path

    params["ignore_whitespace"] = ignore_whitespace

    params["binary"] = binary

    params["renames"] = renames

    params["merge"] = merge

    params["topic"] = topic

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/repositories/{workspace}/{repo_slug}/diff/{spec}".format(
            workspace=quote(str(workspace), safe=""),
            repo_slug=quote(str(repo_slug), safe=""),
            spec=quote(str(spec), safe=""),
        ),
        "params": params,
    }

    return _kwargs


type ParsedPayload = Any | Error
type ParseResult = Any | Error | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 555:
        response_555 = Error.from_dict(response.json())

        return response_555

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ParsedPayload]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace: str,
    repo_slug: str,
    spec: str,
    *,
    client: AuthenticatedClient,
    context: int | Unset = UNSET,
    path: str | Unset = UNSET,
    ignore_whitespace: bool | Unset = UNSET,
    binary: bool | Unset = UNSET,
    renames: bool | Unset = UNSET,
    merge: bool | Unset = UNSET,
    topic: bool | Unset = UNSET,
) -> Response[ParsedPayload]:
    """Compare two commits

     Produces a raw git-style diff.

    #### Single commit spec

    If the `spec` argument to this API is a single commit, the diff is
    produced against the first parent of the specified commit.

    #### Two commit spec

    Two commits separated by `..` may be provided as the `spec`, e.g.,
    `3a8b42..9ff173`. When two commits are provided and the `topic` query
    parameter is true, this API produces a 2-way three dot diff.
    This is the diff between source commit and the merge base of the source
    commit and the destination commit. When the `topic` query param is false,
    a simple git-style diff is produced.

    The two commits are interpreted as follows:

    * First commit: the commit containing the changes we wish to preview
    * Second commit: the commit representing the state to which we want to
      compare the first commit
    * **Note**: This is the opposite of the order used in `git diff`.

    #### Comparison to patches

    While similar to patches, diffs:

    * Don't have a commit header (username, commit message, etc)
    * Support the optional `path=foo/bar.py` query param to filter
      the diff to just that one file diff

    #### Response

    The raw diff is returned as-is, in whatever encoding the files in the
    repository use. It is not decoded into unicode. As such, the
    content-type is `text/plain`.

    Args:
        workspace (str):
        repo_slug (str):
        spec (str):
        context (int | Unset):
        path (str | Unset):
        ignore_whitespace (bool | Unset):
        binary (bool | Unset):
        renames (bool | Unset):
        merge (bool | Unset):
        topic (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        spec=spec,
        context=context,
        path=path,
        ignore_whitespace=ignore_whitespace,
        binary=binary,
        renames=renames,
        merge=merge,
        topic=topic,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    repo_slug: str,
    spec: str,
    *,
    client: AuthenticatedClient,
    context: int | Unset = UNSET,
    path: str | Unset = UNSET,
    ignore_whitespace: bool | Unset = UNSET,
    binary: bool | Unset = UNSET,
    renames: bool | Unset = UNSET,
    merge: bool | Unset = UNSET,
    topic: bool | Unset = UNSET,
) -> ParsedPayload | None:
    """Compare two commits

     Produces a raw git-style diff.

    #### Single commit spec

    If the `spec` argument to this API is a single commit, the diff is
    produced against the first parent of the specified commit.

    #### Two commit spec

    Two commits separated by `..` may be provided as the `spec`, e.g.,
    `3a8b42..9ff173`. When two commits are provided and the `topic` query
    parameter is true, this API produces a 2-way three dot diff.
    This is the diff between source commit and the merge base of the source
    commit and the destination commit. When the `topic` query param is false,
    a simple git-style diff is produced.

    The two commits are interpreted as follows:

    * First commit: the commit containing the changes we wish to preview
    * Second commit: the commit representing the state to which we want to
      compare the first commit
    * **Note**: This is the opposite of the order used in `git diff`.

    #### Comparison to patches

    While similar to patches, diffs:

    * Don't have a commit header (username, commit message, etc)
    * Support the optional `path=foo/bar.py` query param to filter
      the diff to just that one file diff

    #### Response

    The raw diff is returned as-is, in whatever encoding the files in the
    repository use. It is not decoded into unicode. As such, the
    content-type is `text/plain`.

    Args:
        workspace (str):
        repo_slug (str):
        spec (str):
        context (int | Unset):
        path (str | Unset):
        ignore_whitespace (bool | Unset):
        binary (bool | Unset):
        renames (bool | Unset):
        merge (bool | Unset):
        topic (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        spec=spec,
        client=client,
        context=context,
        path=path,
        ignore_whitespace=ignore_whitespace,
        binary=binary,
        renames=renames,
        merge=merge,
        topic=topic,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    spec: str,
    *,
    client: AuthenticatedClient,
    context: int | Unset = UNSET,
    path: str | Unset = UNSET,
    ignore_whitespace: bool | Unset = UNSET,
    binary: bool | Unset = UNSET,
    renames: bool | Unset = UNSET,
    merge: bool | Unset = UNSET,
    topic: bool | Unset = UNSET,
) -> Response[ParsedPayload]:
    """Compare two commits

     Produces a raw git-style diff.

    #### Single commit spec

    If the `spec` argument to this API is a single commit, the diff is
    produced against the first parent of the specified commit.

    #### Two commit spec

    Two commits separated by `..` may be provided as the `spec`, e.g.,
    `3a8b42..9ff173`. When two commits are provided and the `topic` query
    parameter is true, this API produces a 2-way three dot diff.
    This is the diff between source commit and the merge base of the source
    commit and the destination commit. When the `topic` query param is false,
    a simple git-style diff is produced.

    The two commits are interpreted as follows:

    * First commit: the commit containing the changes we wish to preview
    * Second commit: the commit representing the state to which we want to
      compare the first commit
    * **Note**: This is the opposite of the order used in `git diff`.

    #### Comparison to patches

    While similar to patches, diffs:

    * Don't have a commit header (username, commit message, etc)
    * Support the optional `path=foo/bar.py` query param to filter
      the diff to just that one file diff

    #### Response

    The raw diff is returned as-is, in whatever encoding the files in the
    repository use. It is not decoded into unicode. As such, the
    content-type is `text/plain`.

    Args:
        workspace (str):
        repo_slug (str):
        spec (str):
        context (int | Unset):
        path (str | Unset):
        ignore_whitespace (bool | Unset):
        binary (bool | Unset):
        renames (bool | Unset):
        merge (bool | Unset):
        topic (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        spec=spec,
        context=context,
        path=path,
        ignore_whitespace=ignore_whitespace,
        binary=binary,
        renames=renames,
        merge=merge,
        topic=topic,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    spec: str,
    *,
    client: AuthenticatedClient,
    context: int | Unset = UNSET,
    path: str | Unset = UNSET,
    ignore_whitespace: bool | Unset = UNSET,
    binary: bool | Unset = UNSET,
    renames: bool | Unset = UNSET,
    merge: bool | Unset = UNSET,
    topic: bool | Unset = UNSET,
) -> ParsedPayload | None:
    """Compare two commits

     Produces a raw git-style diff.

    #### Single commit spec

    If the `spec` argument to this API is a single commit, the diff is
    produced against the first parent of the specified commit.

    #### Two commit spec

    Two commits separated by `..` may be provided as the `spec`, e.g.,
    `3a8b42..9ff173`. When two commits are provided and the `topic` query
    parameter is true, this API produces a 2-way three dot diff.
    This is the diff between source commit and the merge base of the source
    commit and the destination commit. When the `topic` query param is false,
    a simple git-style diff is produced.

    The two commits are interpreted as follows:

    * First commit: the commit containing the changes we wish to preview
    * Second commit: the commit representing the state to which we want to
      compare the first commit
    * **Note**: This is the opposite of the order used in `git diff`.

    #### Comparison to patches

    While similar to patches, diffs:

    * Don't have a commit header (username, commit message, etc)
    * Support the optional `path=foo/bar.py` query param to filter
      the diff to just that one file diff

    #### Response

    The raw diff is returned as-is, in whatever encoding the files in the
    repository use. It is not decoded into unicode. As such, the
    content-type is `text/plain`.

    Args:
        workspace (str):
        repo_slug (str):
        spec (str):
        context (int | Unset):
        path (str | Unset):
        ignore_whitespace (bool | Unset):
        binary (bool | Unset):
        renames (bool | Unset):
        merge (bool | Unset):
        topic (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            spec=spec,
            client=client,
            context=context,
            path=path,
            ignore_whitespace=ignore_whitespace,
            binary=binary,
            renames=renames,
            merge=merge,
            topic=topic,
        )
    ).parsed
