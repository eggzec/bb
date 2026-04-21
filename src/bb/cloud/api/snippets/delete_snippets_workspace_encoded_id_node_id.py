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
    encoded_id: str,
    node_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/snippets/{workspace}/{encoded_id}/{node_id}".format(
            workspace=quote(str(workspace), safe=""),
            encoded_id=quote(str(encoded_id), safe=""),
            node_id=quote(str(node_id), safe=""),
        ),
    }

    return _kwargs


type ParsedPayload = Any | Error
type ParseResult = Any | Error | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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

    if response.status_code == 405:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_405 = Error.from_dict(response.json())

        return response_405

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
    """Delete a previous revision of a snippet

     Deletes the snippet.

    Note that this only works for versioned URLs that point to the latest
    commit of the snippet. Pointing to an older commit results in a 405
    status code.

    To delete a snippet, regardless of whether or not concurrent changes
    are being made to it, use `DELETE /snippets/{encoded_id}` instead.

    Args:
        workspace (str):
        encoded_id (str):
        node_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
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
    """Delete a previous revision of a snippet

     Deletes the snippet.

    Note that this only works for versioned URLs that point to the latest
    commit of the snippet. Pointing to an older commit results in a 405
    status code.

    To delete a snippet, regardless of whether or not concurrent changes
    are being made to it, use `DELETE /snippets/{encoded_id}` instead.

    Args:
        workspace (str):
        encoded_id (str):
        node_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
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
    """Delete a previous revision of a snippet

     Deletes the snippet.

    Note that this only works for versioned URLs that point to the latest
    commit of the snippet. Pointing to an older commit results in a 405
    status code.

    To delete a snippet, regardless of whether or not concurrent changes
    are being made to it, use `DELETE /snippets/{encoded_id}` instead.

    Args:
        workspace (str):
        encoded_id (str):
        node_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
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
    """Delete a previous revision of a snippet

     Deletes the snippet.

    Note that this only works for versioned URLs that point to the latest
    commit of the snippet. Pointing to an older commit results in a 405
    status code.

    To delete a snippet, regardless of whether or not concurrent changes
    are being made to it, use `DELETE /snippets/{encoded_id}` instead.

    Args:
        workspace (str):
        encoded_id (str):
        node_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            encoded_id=encoded_id,
            node_id=node_id,
            client=client,
        )
    ).parsed
