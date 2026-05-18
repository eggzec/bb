from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...deprecation import deprecated_endpoint
from ...models.error import Error
from ...models.paginated_accounts import PaginatedAccounts
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
        "url": "/snippets/{workspace}/{encoded_id}/watchers".format(
            workspace=quote(str(workspace), safe=""),
            encoded_id=quote(str(encoded_id), safe=""),
        ),
    }

    return _kwargs


type ParsedPayload = Error | PaginatedAccounts
type ParseResult = Error | PaginatedAccounts | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_200 = PaginatedAccounts.from_dict(response.json())

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


@deprecated_endpoint(None)
def sync_detailed(
    workspace: str,
    encoded_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """List users watching a snippet

     Returns a paginated list of all users watching a specific snippet.

    Args:
        workspace (str):
        encoded_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PaginatedAccounts]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        encoded_id=encoded_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated_endpoint(None)
def sync(
    workspace: str,
    encoded_id: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    """List users watching a snippet

     Returns a paginated list of all users watching a specific snippet.

    Args:
        workspace (str):
        encoded_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PaginatedAccounts
    """

    return sync_detailed(
        workspace=workspace,
        encoded_id=encoded_id,
        client=client,
    ).parsed


@deprecated_endpoint(None)
async def asyncio_detailed(
    workspace: str,
    encoded_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """List users watching a snippet

     Returns a paginated list of all users watching a specific snippet.

    Args:
        workspace (str):
        encoded_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PaginatedAccounts]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        encoded_id=encoded_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated_endpoint(None)
async def asyncio(
    workspace: str,
    encoded_id: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    """List users watching a snippet

     Returns a paginated list of all users watching a specific snippet.

    Args:
        workspace (str):
        encoded_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PaginatedAccounts
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            encoded_id=encoded_id,
            client=client,
        )
    ).parsed
