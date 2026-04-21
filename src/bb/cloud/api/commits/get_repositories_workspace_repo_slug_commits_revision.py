from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.page import Page
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
    revision: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/repositories/{workspace}/{repo_slug}/commits/{revision}".format(
            workspace=quote(str(workspace), safe=""),
            repo_slug=quote(str(repo_slug), safe=""),
            revision=quote(str(revision), safe=""),
        ),
    }

    return _kwargs


type ParsedPayload = Error | Page
type ParseResult = Error | Page | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_200 = Page.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_404 = Error.from_dict(response.json())

        return response_404

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
    revision: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """List commits for revision

     These are the repository's commits. They are paginated and returned
    in reverse chronological order, similar to the output of `git log`.
    Like these tools, the DAG can be filtered.

    #### GET /repositories/{workspace}/{repo_slug}/commits/master

    Returns all commits on ref `master` (similar to `git log master`).

    #### GET /repositories/{workspace}/{repo_slug}/commits/dev?include=foo&exclude=master

    Returns all commits on ref `dev` or `foo`, except those that are reachable on
    `master` (similar to `git log dev foo ^master`).

    An optional `path` parameter can be specified that will limit the
    results to commits that affect that path. `path` can either be a file
    or a directory. If a directory is specified, commits are returned that
    have modified any file in the directory tree rooted by `path`. It is
    important to note that if the `path` parameter is specified, the commits
    returned by this endpoint may no longer be a DAG, parent commits that
    do not modify the path will be omitted from the response.

    #### GET /repositories/{workspace}/{repo_slug}/commits/dev?path=README.md&include=foo&include=bar&ex
    clude=master

    Returns all commits that are on refs `dev` or `foo` or `bar`, but not on `master`
    that changed the file README.md.

    #### GET /repositories/{workspace}/{repo_slug}/commits/dev?path=src/&include=foo&exclude=master

    Returns all commits that are on refs `dev` or `foo`, but not on `master`
    that changed to a file in any file in the directory src or its children.

    Because the response could include a very large number of commits, it
    is paginated. Follow the 'next' link in the response to navigate to the
    next page of commits. As with other paginated resources, do not
    construct your own links.

    When the include and exclude parameters are more than can fit in a
    query string, clients can use a `x-www-form-urlencoded` POST instead.

    Args:
        workspace (str):
        repo_slug (str):
        revision (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Page]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        revision=revision,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    repo_slug: str,
    revision: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    """List commits for revision

     These are the repository's commits. They are paginated and returned
    in reverse chronological order, similar to the output of `git log`.
    Like these tools, the DAG can be filtered.

    #### GET /repositories/{workspace}/{repo_slug}/commits/master

    Returns all commits on ref `master` (similar to `git log master`).

    #### GET /repositories/{workspace}/{repo_slug}/commits/dev?include=foo&exclude=master

    Returns all commits on ref `dev` or `foo`, except those that are reachable on
    `master` (similar to `git log dev foo ^master`).

    An optional `path` parameter can be specified that will limit the
    results to commits that affect that path. `path` can either be a file
    or a directory. If a directory is specified, commits are returned that
    have modified any file in the directory tree rooted by `path`. It is
    important to note that if the `path` parameter is specified, the commits
    returned by this endpoint may no longer be a DAG, parent commits that
    do not modify the path will be omitted from the response.

    #### GET /repositories/{workspace}/{repo_slug}/commits/dev?path=README.md&include=foo&include=bar&ex
    clude=master

    Returns all commits that are on refs `dev` or `foo` or `bar`, but not on `master`
    that changed the file README.md.

    #### GET /repositories/{workspace}/{repo_slug}/commits/dev?path=src/&include=foo&exclude=master

    Returns all commits that are on refs `dev` or `foo`, but not on `master`
    that changed to a file in any file in the directory src or its children.

    Because the response could include a very large number of commits, it
    is paginated. Follow the 'next' link in the response to navigate to the
    next page of commits. As with other paginated resources, do not
    construct your own links.

    When the include and exclude parameters are more than can fit in a
    query string, clients can use a `x-www-form-urlencoded` POST instead.

    Args:
        workspace (str):
        repo_slug (str):
        revision (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Page
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        revision=revision,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    revision: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """List commits for revision

     These are the repository's commits. They are paginated and returned
    in reverse chronological order, similar to the output of `git log`.
    Like these tools, the DAG can be filtered.

    #### GET /repositories/{workspace}/{repo_slug}/commits/master

    Returns all commits on ref `master` (similar to `git log master`).

    #### GET /repositories/{workspace}/{repo_slug}/commits/dev?include=foo&exclude=master

    Returns all commits on ref `dev` or `foo`, except those that are reachable on
    `master` (similar to `git log dev foo ^master`).

    An optional `path` parameter can be specified that will limit the
    results to commits that affect that path. `path` can either be a file
    or a directory. If a directory is specified, commits are returned that
    have modified any file in the directory tree rooted by `path`. It is
    important to note that if the `path` parameter is specified, the commits
    returned by this endpoint may no longer be a DAG, parent commits that
    do not modify the path will be omitted from the response.

    #### GET /repositories/{workspace}/{repo_slug}/commits/dev?path=README.md&include=foo&include=bar&ex
    clude=master

    Returns all commits that are on refs `dev` or `foo` or `bar`, but not on `master`
    that changed the file README.md.

    #### GET /repositories/{workspace}/{repo_slug}/commits/dev?path=src/&include=foo&exclude=master

    Returns all commits that are on refs `dev` or `foo`, but not on `master`
    that changed to a file in any file in the directory src or its children.

    Because the response could include a very large number of commits, it
    is paginated. Follow the 'next' link in the response to navigate to the
    next page of commits. As with other paginated resources, do not
    construct your own links.

    When the include and exclude parameters are more than can fit in a
    query string, clients can use a `x-www-form-urlencoded` POST instead.

    Args:
        workspace (str):
        repo_slug (str):
        revision (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Page]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        revision=revision,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    revision: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    """List commits for revision

     These are the repository's commits. They are paginated and returned
    in reverse chronological order, similar to the output of `git log`.
    Like these tools, the DAG can be filtered.

    #### GET /repositories/{workspace}/{repo_slug}/commits/master

    Returns all commits on ref `master` (similar to `git log master`).

    #### GET /repositories/{workspace}/{repo_slug}/commits/dev?include=foo&exclude=master

    Returns all commits on ref `dev` or `foo`, except those that are reachable on
    `master` (similar to `git log dev foo ^master`).

    An optional `path` parameter can be specified that will limit the
    results to commits that affect that path. `path` can either be a file
    or a directory. If a directory is specified, commits are returned that
    have modified any file in the directory tree rooted by `path`. It is
    important to note that if the `path` parameter is specified, the commits
    returned by this endpoint may no longer be a DAG, parent commits that
    do not modify the path will be omitted from the response.

    #### GET /repositories/{workspace}/{repo_slug}/commits/dev?path=README.md&include=foo&include=bar&ex
    clude=master

    Returns all commits that are on refs `dev` or `foo` or `bar`, but not on `master`
    that changed the file README.md.

    #### GET /repositories/{workspace}/{repo_slug}/commits/dev?path=src/&include=foo&exclude=master

    Returns all commits that are on refs `dev` or `foo`, but not on `master`
    that changed to a file in any file in the directory src or its children.

    Because the response could include a very large number of commits, it
    is paginated. Follow the 'next' link in the response to navigate to the
    next page of commits. As with other paginated resources, do not
    construct your own links.

    When the include and exclude parameters are more than can fit in a
    query string, clients can use a `x-www-form-urlencoded` POST instead.

    Args:
        workspace (str):
        repo_slug (str):
        revision (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Page
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            revision=revision,
            client=client,
        )
    ).parsed
