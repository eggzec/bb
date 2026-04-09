from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.paginated_branch_restrictions import PaginatedBranchRestrictions
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
    kind: str | Unset = UNSET,
    pattern: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["kind"] = kind

    params["pattern"] = pattern

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/repositories/{workspace}/{repo_slug}/branch-restrictions".format(
            workspace=quote(str(workspace), safe=""),
            repo_slug=quote(str(repo_slug), safe=""),
        ),
        "params": params,
    }

    return _kwargs


type ParsedPayload = Error | PaginatedBranchRestrictions
type ParseResult = Error | PaginatedBranchRestrictions | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        response_200 = PaginatedBranchRestrictions.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

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
    *,
    client: AuthenticatedClient,
    kind: str | Unset = UNSET,
    pattern: str | Unset = UNSET,
) -> Response[ParsedPayload]:
    """List branch restrictions

     Returns a paginated list of all branch restrictions on the
    repository.

    Args:
        workspace (str):
        repo_slug (str):
        kind (str | Unset):
        pattern (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PaginatedBranchRestrictions]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        kind=kind,
        pattern=pattern,
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
    kind: str | Unset = UNSET,
    pattern: str | Unset = UNSET,
) -> ParsedPayload | None:
    """List branch restrictions

     Returns a paginated list of all branch restrictions on the
    repository.

    Args:
        workspace (str):
        repo_slug (str):
        kind (str | Unset):
        pattern (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PaginatedBranchRestrictions
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        client=client,
        kind=kind,
        pattern=pattern,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
    kind: str | Unset = UNSET,
    pattern: str | Unset = UNSET,
) -> Response[ParsedPayload]:
    """List branch restrictions

     Returns a paginated list of all branch restrictions on the
    repository.

    Args:
        workspace (str):
        repo_slug (str):
        kind (str | Unset):
        pattern (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PaginatedBranchRestrictions]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        kind=kind,
        pattern=pattern,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
    kind: str | Unset = UNSET,
    pattern: str | Unset = UNSET,
) -> ParsedPayload | None:
    """List branch restrictions

     Returns a paginated list of all branch restrictions on the
    repository.

    Args:
        workspace (str):
        repo_slug (str):
        kind (str | Unset):
        pattern (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PaginatedBranchRestrictions
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            client=client,
            kind=kind,
            pattern=pattern,
        )
    ).parsed
