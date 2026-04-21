from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.paginated_default_reviewer_and_type import PaginatedDefaultReviewerAndType
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
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["pagelen"] = pagelen

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/repositories/{workspace}/{repo_slug}/effective-default-reviewers".format(
            workspace=quote(str(workspace), safe=""),
            repo_slug=quote(str(repo_slug), safe=""),
        ),
        "params": params,
    }

    return _kwargs


type ParsedPayload = Error | PaginatedDefaultReviewerAndType
type ParseResult = Error | PaginatedDefaultReviewerAndType | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_200 = PaginatedDefaultReviewerAndType.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_403 = Error.from_dict(response.json())

        return response_403

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
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> Response[ParsedPayload]:
    """List effective default reviewers

     Returns the repository's effective default reviewers. This includes both default
    reviewers defined at the repository level as well as those inherited from its project.

    These are the users that are automatically added as reviewers on every
    new pull request that is created.

    Args:
        workspace (str):
        repo_slug (str):
        page (int | Unset):  Default: 1.
        pagelen (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PaginatedDefaultReviewerAndType]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
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
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> ParsedPayload | None:
    """List effective default reviewers

     Returns the repository's effective default reviewers. This includes both default
    reviewers defined at the repository level as well as those inherited from its project.

    These are the users that are automatically added as reviewers on every
    new pull request that is created.

    Args:
        workspace (str):
        repo_slug (str):
        page (int | Unset):  Default: 1.
        pagelen (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PaginatedDefaultReviewerAndType
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        client=client,
        page=page,
        pagelen=pagelen,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> Response[ParsedPayload]:
    """List effective default reviewers

     Returns the repository's effective default reviewers. This includes both default
    reviewers defined at the repository level as well as those inherited from its project.

    These are the users that are automatically added as reviewers on every
    new pull request that is created.

    Args:
        workspace (str):
        repo_slug (str):
        page (int | Unset):  Default: 1.
        pagelen (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PaginatedDefaultReviewerAndType]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        page=page,
        pagelen=pagelen,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> ParsedPayload | None:
    """List effective default reviewers

     Returns the repository's effective default reviewers. This includes both default
    reviewers defined at the repository level as well as those inherited from its project.

    These are the users that are automatically added as reviewers on every
    new pull request that is created.

    Args:
        workspace (str):
        repo_slug (str):
        page (int | Unset):  Default: 1.
        pagelen (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PaginatedDefaultReviewerAndType
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            client=client,
            page=page,
            pagelen=pagelen,
        )
    ).parsed
