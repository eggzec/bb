from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...types import Response

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
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/repositories/{workspace}/{repo_slug}/patch/{spec}".format(
            workspace=quote(str(workspace), safe=""),
            repo_slug=quote(str(repo_slug), safe=""),
            spec=quote(str(spec), safe=""),
        ),
    }

    return _kwargs


type ParsedPayload = Any | Error
type ParseResult = Any | Error | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 401:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 555:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
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
) -> Response[ParsedPayload]:
    """Get a patch for two commits

     Produces a raw patch for a single commit (diffed against its first
    parent), or a patch-series for a revspec of 2 commits (e.g.
    `3a8b42..9ff173` where the first commit represents the source and the
    second commit the destination).

    In case of the latter (diffing a revspec), a patch series is returned
    for the commits on the source branch (`3a8b42` and its ancestors in
    our example).

    While similar to diffs, patches:

    * Have a commit header (username, commit message, etc)
    * Do not support the `path=foo/bar.py` query parameter

    The raw patch is returned as-is, in whatever encoding the files in the
    repository use. It is not decoded into unicode. As such, the
    content-type is `text/plain`.

    Args:
        workspace (str):
        repo_slug (str):
        spec (str):

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
) -> ParsedPayload | None:
    """Get a patch for two commits

     Produces a raw patch for a single commit (diffed against its first
    parent), or a patch-series for a revspec of 2 commits (e.g.
    `3a8b42..9ff173` where the first commit represents the source and the
    second commit the destination).

    In case of the latter (diffing a revspec), a patch series is returned
    for the commits on the source branch (`3a8b42` and its ancestors in
    our example).

    While similar to diffs, patches:

    * Have a commit header (username, commit message, etc)
    * Do not support the `path=foo/bar.py` query parameter

    The raw patch is returned as-is, in whatever encoding the files in the
    repository use. It is not decoded into unicode. As such, the
    content-type is `text/plain`.

    Args:
        workspace (str):
        repo_slug (str):
        spec (str):

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
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    spec: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """Get a patch for two commits

     Produces a raw patch for a single commit (diffed against its first
    parent), or a patch-series for a revspec of 2 commits (e.g.
    `3a8b42..9ff173` where the first commit represents the source and the
    second commit the destination).

    In case of the latter (diffing a revspec), a patch series is returned
    for the commits on the source branch (`3a8b42` and its ancestors in
    our example).

    While similar to diffs, patches:

    * Have a commit header (username, commit message, etc)
    * Do not support the `path=foo/bar.py` query parameter

    The raw patch is returned as-is, in whatever encoding the files in the
    repository use. It is not decoded into unicode. As such, the
    content-type is `text/plain`.

    Args:
        workspace (str):
        repo_slug (str):
        spec (str):

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
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    spec: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    """Get a patch for two commits

     Produces a raw patch for a single commit (diffed against its first
    parent), or a patch-series for a revspec of 2 commits (e.g.
    `3a8b42..9ff173` where the first commit represents the source and the
    second commit the destination).

    In case of the latter (diffing a revspec), a patch series is returned
    for the commits on the source branch (`3a8b42` and its ancestors in
    our example).

    While similar to diffs, patches:

    * Have a commit header (username, commit message, etc)
    * Do not support the `path=foo/bar.py` query parameter

    The raw patch is returned as-is, in whatever encoding the files in the
    repository use. It is not decoded into unicode. As such, the
    content-type is `text/plain`.

    Args:
        workspace (str):
        repo_slug (str):
        spec (str):

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
        )
    ).parsed
