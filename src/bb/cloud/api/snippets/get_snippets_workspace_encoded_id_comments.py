from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.paginated_snippet_comments import PaginatedSnippetComments
from ...types import Response

__all__ = [
    "sync_detailed",
    "asyncio_detailed",
    "sync",
    "asyncio",
]


def _get_kwargs(
    workspace: str,
    encoded_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/snippets/{workspace}/{encoded_id}/comments".format(
            workspace=quote(str(workspace), safe=""),
            encoded_id=quote(str(encoded_id), safe=""),
        ),
    }

    return _kwargs


type ParsedPayload = Error | PaginatedSnippetComments
type ParseResult = Error | PaginatedSnippetComments | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_200 = PaginatedSnippetComments.from_dict(response.json())

        return response_200

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
    encoded_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """List comments on a snippet

     Used to retrieve a paginated list of all comments for a specific
    snippet.

    This resource works identical to commit and pull request comments.

    The default sorting is oldest to newest and can be overridden with
    the `sort` query parameter.

    Args:
        workspace (str):
        encoded_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PaginatedSnippetComments]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        encoded_id=encoded_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    encoded_id: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    """List comments on a snippet

     Used to retrieve a paginated list of all comments for a specific
    snippet.

    This resource works identical to commit and pull request comments.

    The default sorting is oldest to newest and can be overridden with
    the `sort` query parameter.

    Args:
        workspace (str):
        encoded_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PaginatedSnippetComments
    """

    return sync_detailed(
        workspace=workspace,
        encoded_id=encoded_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    encoded_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """List comments on a snippet

     Used to retrieve a paginated list of all comments for a specific
    snippet.

    This resource works identical to commit and pull request comments.

    The default sorting is oldest to newest and can be overridden with
    the `sort` query parameter.

    Args:
        workspace (str):
        encoded_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PaginatedSnippetComments]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        encoded_id=encoded_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    encoded_id: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    """List comments on a snippet

     Used to retrieve a paginated list of all comments for a specific
    snippet.

    This resource works identical to commit and pull request comments.

    The default sorting is oldest to newest and can be overridden with
    the `sort` query parameter.

    Args:
        workspace (str):
        encoded_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PaginatedSnippetComments
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            encoded_id=encoded_id,
            client=client,
        )
    ).parsed
