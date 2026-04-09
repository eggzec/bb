from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.webhook_subscription import WebhookSubscription
from ...types import Response

__all__ = [
    "sync_detailed",
    "asyncio_detailed",
    "sync",
    "asyncio",
]


def _get_kwargs(
    workspace: str,
    uid: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/workspaces/{workspace}/hooks/{uid}".format(
            workspace=quote(str(workspace), safe=""),
            uid=quote(str(uid), safe=""),
        ),
    }

    return _kwargs


type ParsedPayload = Error | WebhookSubscription
type ParseResult = Error | WebhookSubscription | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        response_200 = WebhookSubscription.from_dict(response.json())

        return response_200

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
    uid: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """Get a webhook for a workspace

     Returns the webhook with the specified id installed on the given
    workspace.

    Args:
        workspace (str):
        uid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | WebhookSubscription]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        uid=uid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    uid: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    """Get a webhook for a workspace

     Returns the webhook with the specified id installed on the given
    workspace.

    Args:
        workspace (str):
        uid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | WebhookSubscription
    """

    return sync_detailed(
        workspace=workspace,
        uid=uid,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    uid: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """Get a webhook for a workspace

     Returns the webhook with the specified id installed on the given
    workspace.

    Args:
        workspace (str):
        uid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | WebhookSubscription]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        uid=uid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    uid: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    """Get a webhook for a workspace

     Returns the webhook with the specified id installed on the given
    workspace.

    Args:
        workspace (str):
        uid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | WebhookSubscription
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            uid=uid,
            client=client,
        )
    ).parsed
