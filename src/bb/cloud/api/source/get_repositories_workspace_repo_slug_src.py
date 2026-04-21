from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.get_repositories_workspace_repo_slug_src_format import GetRepositoriesWorkspaceRepoSlugSrcFormat
from ...models.paginated_tree_entry import PaginatedTreeEntry
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
    *,
    format_: GetRepositoriesWorkspaceRepoSlugSrcFormat | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_format_: str | Unset = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value

    params["format"] = json_format_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/repositories/{workspace}/{repo_slug}/src".format(
            workspace=quote(str(workspace), safe=""),
            repo_slug=quote(str(repo_slug), safe=""),
        ),
        "params": params,
    }

    return _kwargs


type ParsedPayload = Error | PaginatedTreeEntry
type ParseResult = Error | PaginatedTreeEntry | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_200 = PaginatedTreeEntry.from_dict(response.json())

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
    *,
    client: AuthenticatedClient,
    format_: GetRepositoriesWorkspaceRepoSlugSrcFormat | Unset = UNSET,
) -> Response[ParsedPayload]:
    """Get the root directory of the main branch

     This endpoint redirects the client to the directory listing of the
    root directory on the main branch.

    This is equivalent to directly hitting
    [/2.0/repositories/{username}/{repo_slug}/src/{commit}/{path}](src/%7Bcommit%7D/%7Bpath%7D)
    without having to know the name or SHA1 of the repo's main branch.

    To create new commits, [POST to this endpoint](#post)

    Args:
        workspace (str):
        repo_slug (str):
        format_ (GetRepositoriesWorkspaceRepoSlugSrcFormat | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PaginatedTreeEntry]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        format_=format_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
    format_: GetRepositoriesWorkspaceRepoSlugSrcFormat | Unset = UNSET,
) -> ParsedPayload | None:
    """Get the root directory of the main branch

     This endpoint redirects the client to the directory listing of the
    root directory on the main branch.

    This is equivalent to directly hitting
    [/2.0/repositories/{username}/{repo_slug}/src/{commit}/{path}](src/%7Bcommit%7D/%7Bpath%7D)
    without having to know the name or SHA1 of the repo's main branch.

    To create new commits, [POST to this endpoint](#post)

    Args:
        workspace (str):
        repo_slug (str):
        format_ (GetRepositoriesWorkspaceRepoSlugSrcFormat | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PaginatedTreeEntry
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        client=client,
        format_=format_,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
    format_: GetRepositoriesWorkspaceRepoSlugSrcFormat | Unset = UNSET,
) -> Response[ParsedPayload]:
    """Get the root directory of the main branch

     This endpoint redirects the client to the directory listing of the
    root directory on the main branch.

    This is equivalent to directly hitting
    [/2.0/repositories/{username}/{repo_slug}/src/{commit}/{path}](src/%7Bcommit%7D/%7Bpath%7D)
    without having to know the name or SHA1 of the repo's main branch.

    To create new commits, [POST to this endpoint](#post)

    Args:
        workspace (str):
        repo_slug (str):
        format_ (GetRepositoriesWorkspaceRepoSlugSrcFormat | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PaginatedTreeEntry]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        format_=format_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
    format_: GetRepositoriesWorkspaceRepoSlugSrcFormat | Unset = UNSET,
) -> ParsedPayload | None:
    """Get the root directory of the main branch

     This endpoint redirects the client to the directory listing of the
    root directory on the main branch.

    This is equivalent to directly hitting
    [/2.0/repositories/{username}/{repo_slug}/src/{commit}/{path}](src/%7Bcommit%7D/%7Bpath%7D)
    without having to know the name or SHA1 of the repo's main branch.

    To create new commits, [POST to this endpoint](#post)

    Args:
        workspace (str):
        repo_slug (str):
        format_ (GetRepositoriesWorkspaceRepoSlugSrcFormat | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PaginatedTreeEntry
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            client=client,
            format_=format_,
        )
    ).parsed
