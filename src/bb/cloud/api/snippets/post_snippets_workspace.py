from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.snippet import Snippet
from ...types import Response

__all__ = [
    "sync_detailed",
    "asyncio_detailed",
    "sync",
    "asyncio",
]


def _get_kwargs(
    workspace: str,
    *,
    body: Snippet,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/snippets/{workspace}".format(
            workspace=quote(str(workspace), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


type ParsedPayload = Error | Snippet
type ParseResult = Error | Snippet | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 201:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_201 = Snippet.from_dict(response.json())

        return response_201

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
    *,
    client: AuthenticatedClient,
    body: Snippet,
) -> Response[ParsedPayload]:
    """Create a snippet for a workspace

     Identical to [`/snippets`](/cloud/bitbucket/rest/api-group-snippets/#api-snippets-post), except that
    the new snippet will be
    created under the workspace specified in the path parameter
    `{workspace}`.

    Args:
        workspace (str):
        body (Snippet):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Snippet]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    *,
    client: AuthenticatedClient,
    body: Snippet,
) -> ParsedPayload | None:
    """Create a snippet for a workspace

     Identical to [`/snippets`](/cloud/bitbucket/rest/api-group-snippets/#api-snippets-post), except that
    the new snippet will be
    created under the workspace specified in the path parameter
    `{workspace}`.

    Args:
        workspace (str):
        body (Snippet):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Snippet
    """

    return sync_detailed(
        workspace=workspace,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    *,
    client: AuthenticatedClient,
    body: Snippet,
) -> Response[ParsedPayload]:
    """Create a snippet for a workspace

     Identical to [`/snippets`](/cloud/bitbucket/rest/api-group-snippets/#api-snippets-post), except that
    the new snippet will be
    created under the workspace specified in the path parameter
    `{workspace}`.

    Args:
        workspace (str):
        body (Snippet):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Snippet]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    *,
    client: AuthenticatedClient,
    body: Snippet,
) -> ParsedPayload | None:
    """Create a snippet for a workspace

     Identical to [`/snippets`](/cloud/bitbucket/rest/api-group-snippets/#api-snippets-post), except that
    the new snippet will be
    created under the workspace specified in the path parameter
    `{workspace}`.

    Args:
        workspace (str):
        body (Snippet):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Snippet
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            client=client,
            body=body,
        )
    ).parsed
