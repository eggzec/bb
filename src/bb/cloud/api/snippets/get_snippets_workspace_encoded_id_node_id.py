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
    encoded_id: str,
    node_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/snippets/{workspace}/{encoded_id}/{node_id}".format(
            workspace=quote(str(workspace), safe=""),
            encoded_id=quote(str(encoded_id), safe=""),
            node_id=quote(str(node_id), safe=""),
        ),
    }

    return _kwargs


type ParsedPayload = Error | Snippet
type ParseResult = Error | Snippet | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        response_200 = Snippet.from_dict(response.json())

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
    encoded_id: str,
    node_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """Get a previous revision of a snippet

     Identical to `GET /snippets/encoded_id`, except that this endpoint
    can be used to retrieve the contents of the snippet as it was at an
    older revision, while `/snippets/encoded_id` always returns the
    snippet's current revision.

    Note that only the snippet's file contents are versioned, not its
    meta data properties like the title.

    Other than that, the two endpoints are identical in behavior.

    Args:
        workspace (str):
        encoded_id (str):
        node_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Snippet]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        encoded_id=encoded_id,
        node_id=node_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    encoded_id: str,
    node_id: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    """Get a previous revision of a snippet

     Identical to `GET /snippets/encoded_id`, except that this endpoint
    can be used to retrieve the contents of the snippet as it was at an
    older revision, while `/snippets/encoded_id` always returns the
    snippet's current revision.

    Note that only the snippet's file contents are versioned, not its
    meta data properties like the title.

    Other than that, the two endpoints are identical in behavior.

    Args:
        workspace (str):
        encoded_id (str):
        node_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Snippet
    """

    return sync_detailed(
        workspace=workspace,
        encoded_id=encoded_id,
        node_id=node_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    encoded_id: str,
    node_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """Get a previous revision of a snippet

     Identical to `GET /snippets/encoded_id`, except that this endpoint
    can be used to retrieve the contents of the snippet as it was at an
    older revision, while `/snippets/encoded_id` always returns the
    snippet's current revision.

    Note that only the snippet's file contents are versioned, not its
    meta data properties like the title.

    Other than that, the two endpoints are identical in behavior.

    Args:
        workspace (str):
        encoded_id (str):
        node_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Snippet]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        encoded_id=encoded_id,
        node_id=node_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    encoded_id: str,
    node_id: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    """Get a previous revision of a snippet

     Identical to `GET /snippets/encoded_id`, except that this endpoint
    can be used to retrieve the contents of the snippet as it was at an
    older revision, while `/snippets/encoded_id` always returns the
    snippet's current revision.

    Note that only the snippet's file contents are versioned, not its
    meta data properties like the title.

    Other than that, the two endpoints are identical in behavior.

    Args:
        workspace (str):
        encoded_id (str):
        node_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Snippet
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            encoded_id=encoded_id,
            node_id=node_id,
            client=client,
        )
    ).parsed
