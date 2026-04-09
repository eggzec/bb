from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.paginated_pull_requests import PaginatedPullRequests
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
    commit: str,
    *,
    page: int | Unset = 1,
    pagelen: int | Unset = 30,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["pagelen"] = pagelen

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/repositories/{workspace}/{repo_slug}/commit/{commit}/pullrequests".format(
            workspace=quote(str(workspace), safe=""),
            repo_slug=quote(str(repo_slug), safe=""),
            commit=quote(str(commit), safe=""),
        ),
        "params": params,
    }

    return _kwargs


type ParsedPayload = Error | PaginatedPullRequests
type ParseResult = Error | PaginatedPullRequests | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        response_200 = PaginatedPullRequests.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = PaginatedPullRequests.from_dict(response.json())

        return response_202

    if response.status_code == 404:
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
    commit: str,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    pagelen: int | Unset = 30,
) -> Response[ParsedPayload]:
    """List pull requests that contain a commit

     Returns a paginated list of all pull requests as part of which this commit was reviewed. Pull
    Request Commit Links app must be installed first before using this API; installation automatically
    occurs when 'Go to pull request' is clicked from the web interface for a commit's details.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        page (int | Unset):  Default: 1.
        pagelen (int | Unset):  Default: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PaginatedPullRequests]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        commit=commit,
        page=page,
        pagelen=pagelen,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    repo_slug: str,
    commit: str,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    pagelen: int | Unset = 30,
) -> ParsedPayload | None:
    """List pull requests that contain a commit

     Returns a paginated list of all pull requests as part of which this commit was reviewed. Pull
    Request Commit Links app must be installed first before using this API; installation automatically
    occurs when 'Go to pull request' is clicked from the web interface for a commit's details.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        page (int | Unset):  Default: 1.
        pagelen (int | Unset):  Default: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PaginatedPullRequests
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        commit=commit,
        client=client,
        page=page,
        pagelen=pagelen,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    commit: str,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    pagelen: int | Unset = 30,
) -> Response[ParsedPayload]:
    """List pull requests that contain a commit

     Returns a paginated list of all pull requests as part of which this commit was reviewed. Pull
    Request Commit Links app must be installed first before using this API; installation automatically
    occurs when 'Go to pull request' is clicked from the web interface for a commit's details.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        page (int | Unset):  Default: 1.
        pagelen (int | Unset):  Default: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PaginatedPullRequests]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        commit=commit,
        page=page,
        pagelen=pagelen,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    commit: str,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    pagelen: int | Unset = 30,
) -> ParsedPayload | None:
    """List pull requests that contain a commit

     Returns a paginated list of all pull requests as part of which this commit was reviewed. Pull
    Request Commit Links app must be installed first before using this API; installation automatically
    occurs when 'Go to pull request' is clicked from the web interface for a commit's details.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        page (int | Unset):  Default: 1.
        pagelen (int | Unset):  Default: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PaginatedPullRequests
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            commit=commit,
            client=client,
            page=page,
            pagelen=pagelen,
        )
    ).parsed
