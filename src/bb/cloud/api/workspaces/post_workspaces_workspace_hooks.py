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
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/workspaces/{workspace}/hooks".format(
            workspace=quote(str(workspace), safe=""),
        ),
    }

    return _kwargs


type ParsedPayload = Error | WebhookSubscription
type ParseResult = Error | WebhookSubscription | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 201:
        response_201 = WebhookSubscription.from_dict(response.json())

        return response_201

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
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    r"""Create a webhook for a workspace

     Creates a new webhook on the specified workspace.

    Workspace webhooks are fired for events from all repositories contained
    by that workspace.

    Example:

    ```
    $ curl -X POST -u credentials -H 'Content-Type: application/json'
      https://api.bitbucket.org/2.0/workspaces/my-workspace/hooks
      -d '
        {
          \"description\": \"Webhook Description\",
          \"url\": \"https://example.com/\",
          \"active\": true,
          \"secret\": \"this is a really bad secret\",
          \"events\": [
            \"repo:push\",
            \"issue:created\",
            \"issue:updated\"
          ]
        }'
    ```

    When the `secret` is provided it will be used as the key to generate a HMAC
    digest value sent in the `X-Hub-Signature` header at delivery time. Passing
    a `null` or empty `secret` or not passing a `secret` will leave the webhook's
    secret unset. Bitbucket only generates the `X-Hub-Signature` when the webhook's
    secret is set.

    This call requires the webhook scope, as well as any scope
    that applies to the events that the webhook subscribes to. In the
    example above that means: `webhook`, `repository` and `issue`.

    The `url` must properly resolve and cannot be an internal, non-routed address.

    Only workspace owners can install webhooks on workspaces.

    Args:
        workspace (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | WebhookSubscription]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    r"""Create a webhook for a workspace

     Creates a new webhook on the specified workspace.

    Workspace webhooks are fired for events from all repositories contained
    by that workspace.

    Example:

    ```
    $ curl -X POST -u credentials -H 'Content-Type: application/json'
      https://api.bitbucket.org/2.0/workspaces/my-workspace/hooks
      -d '
        {
          \"description\": \"Webhook Description\",
          \"url\": \"https://example.com/\",
          \"active\": true,
          \"secret\": \"this is a really bad secret\",
          \"events\": [
            \"repo:push\",
            \"issue:created\",
            \"issue:updated\"
          ]
        }'
    ```

    When the `secret` is provided it will be used as the key to generate a HMAC
    digest value sent in the `X-Hub-Signature` header at delivery time. Passing
    a `null` or empty `secret` or not passing a `secret` will leave the webhook's
    secret unset. Bitbucket only generates the `X-Hub-Signature` when the webhook's
    secret is set.

    This call requires the webhook scope, as well as any scope
    that applies to the events that the webhook subscribes to. In the
    example above that means: `webhook`, `repository` and `issue`.

    The `url` must properly resolve and cannot be an internal, non-routed address.

    Only workspace owners can install webhooks on workspaces.

    Args:
        workspace (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | WebhookSubscription
    """

    return sync_detailed(
        workspace=workspace,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    r"""Create a webhook for a workspace

     Creates a new webhook on the specified workspace.

    Workspace webhooks are fired for events from all repositories contained
    by that workspace.

    Example:

    ```
    $ curl -X POST -u credentials -H 'Content-Type: application/json'
      https://api.bitbucket.org/2.0/workspaces/my-workspace/hooks
      -d '
        {
          \"description\": \"Webhook Description\",
          \"url\": \"https://example.com/\",
          \"active\": true,
          \"secret\": \"this is a really bad secret\",
          \"events\": [
            \"repo:push\",
            \"issue:created\",
            \"issue:updated\"
          ]
        }'
    ```

    When the `secret` is provided it will be used as the key to generate a HMAC
    digest value sent in the `X-Hub-Signature` header at delivery time. Passing
    a `null` or empty `secret` or not passing a `secret` will leave the webhook's
    secret unset. Bitbucket only generates the `X-Hub-Signature` when the webhook's
    secret is set.

    This call requires the webhook scope, as well as any scope
    that applies to the events that the webhook subscribes to. In the
    example above that means: `webhook`, `repository` and `issue`.

    The `url` must properly resolve and cannot be an internal, non-routed address.

    Only workspace owners can install webhooks on workspaces.

    Args:
        workspace (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | WebhookSubscription]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    r"""Create a webhook for a workspace

     Creates a new webhook on the specified workspace.

    Workspace webhooks are fired for events from all repositories contained
    by that workspace.

    Example:

    ```
    $ curl -X POST -u credentials -H 'Content-Type: application/json'
      https://api.bitbucket.org/2.0/workspaces/my-workspace/hooks
      -d '
        {
          \"description\": \"Webhook Description\",
          \"url\": \"https://example.com/\",
          \"active\": true,
          \"secret\": \"this is a really bad secret\",
          \"events\": [
            \"repo:push\",
            \"issue:created\",
            \"issue:updated\"
          ]
        }'
    ```

    When the `secret` is provided it will be used as the key to generate a HMAC
    digest value sent in the `X-Hub-Signature` header at delivery time. Passing
    a `null` or empty `secret` or not passing a `secret` will leave the webhook's
    secret unset. Bitbucket only generates the `X-Hub-Signature` when the webhook's
    secret is set.

    This call requires the webhook scope, as well as any scope
    that applies to the events that the webhook subscribes to. In the
    example above that means: `webhook`, `repository` and `issue`.

    The `url` must properly resolve and cannot be an internal, non-routed address.

    Only workspace owners can install webhooks on workspaces.

    Args:
        workspace (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | WebhookSubscription
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            client=client,
        )
    ).parsed
