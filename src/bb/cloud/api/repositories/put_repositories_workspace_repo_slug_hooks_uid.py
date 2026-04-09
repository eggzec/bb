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
    repo_slug: str,
    uid: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/repositories/{workspace}/{repo_slug}/hooks/{uid}".format(
            workspace=quote(str(workspace), safe=""),
            repo_slug=quote(str(repo_slug), safe=""),
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
    uid: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """Update a webhook for a repository

     Updates the specified webhook subscription.

    The following properties can be mutated:

    * `description`
    * `url`
    * `secret`
    * `active`
    * `events`

    The hook's secret is used as a key to generate the HMAC hex digest sent in the
    `X-Hub-Signature` header at delivery time. This signature is only generated
    when the hook has a secret.

    Set the hook's secret by passing the new value in the `secret` field. Passing a
    `null` value in the `secret` field will remove the secret from the hook. The
    hook's secret can be left unchanged by not passing the `secret` field in the
    request.

    Args:
        workspace (str):
        repo_slug (str):
        uid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | WebhookSubscription]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        uid=uid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    repo_slug: str,
    uid: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    """Update a webhook for a repository

     Updates the specified webhook subscription.

    The following properties can be mutated:

    * `description`
    * `url`
    * `secret`
    * `active`
    * `events`

    The hook's secret is used as a key to generate the HMAC hex digest sent in the
    `X-Hub-Signature` header at delivery time. This signature is only generated
    when the hook has a secret.

    Set the hook's secret by passing the new value in the `secret` field. Passing a
    `null` value in the `secret` field will remove the secret from the hook. The
    hook's secret can be left unchanged by not passing the `secret` field in the
    request.

    Args:
        workspace (str):
        repo_slug (str):
        uid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | WebhookSubscription
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        uid=uid,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    uid: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """Update a webhook for a repository

     Updates the specified webhook subscription.

    The following properties can be mutated:

    * `description`
    * `url`
    * `secret`
    * `active`
    * `events`

    The hook's secret is used as a key to generate the HMAC hex digest sent in the
    `X-Hub-Signature` header at delivery time. This signature is only generated
    when the hook has a secret.

    Set the hook's secret by passing the new value in the `secret` field. Passing a
    `null` value in the `secret` field will remove the secret from the hook. The
    hook's secret can be left unchanged by not passing the `secret` field in the
    request.

    Args:
        workspace (str):
        repo_slug (str):
        uid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | WebhookSubscription]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        uid=uid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    uid: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    """Update a webhook for a repository

     Updates the specified webhook subscription.

    The following properties can be mutated:

    * `description`
    * `url`
    * `secret`
    * `active`
    * `events`

    The hook's secret is used as a key to generate the HMAC hex digest sent in the
    `X-Hub-Signature` header at delivery time. This signature is only generated
    when the hook has a secret.

    Set the hook's secret by passing the new value in the `secret` field. Passing a
    `null` value in the `secret` field will remove the secret from the hook. The
    hook's secret can be left unchanged by not passing the `secret` field in the
    request.

    Args:
        workspace (str):
        repo_slug (str):
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
            repo_slug=repo_slug,
            uid=uid,
            client=client,
        )
    ).parsed
