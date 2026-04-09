from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.subject_types import SubjectTypes
from ...types import Response

__all__ = [
    "sync_detailed",
    "asyncio_detailed",
    "sync",
    "asyncio",
]


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/hook_events",
    }

    return _kwargs


type ParsedPayload = SubjectTypes
type ParseResult = SubjectTypes | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        response_200 = SubjectTypes.from_dict(response.json())

        return response_200

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
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """Get a webhook resource

     Returns the webhook resource or subject types on which webhooks can
    be registered.

    Each resource/subject type contains an `events` link that returns the
    paginated list of specific events each individual subject type can
    emit.

    This endpoint is publicly accessible and does not require
    authentication or scopes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SubjectTypes]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    """Get a webhook resource

     Returns the webhook resource or subject types on which webhooks can
    be registered.

    Each resource/subject type contains an `events` link that returns the
    paginated list of specific events each individual subject type can
    emit.

    This endpoint is publicly accessible and does not require
    authentication or scopes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SubjectTypes
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """Get a webhook resource

     Returns the webhook resource or subject types on which webhooks can
    be registered.

    Each resource/subject type contains an `events` link that returns the
    paginated list of specific events each individual subject type can
    emit.

    This endpoint is publicly accessible and does not require
    authentication or scopes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SubjectTypes]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    """Get a webhook resource

     Returns the webhook resource or subject types on which webhooks can
    be registered.

    Each resource/subject type contains an `events` link that returns the
    paginated list of specific events each individual subject type can
    emit.

    This endpoint is publicly accessible and does not require
    authentication or scopes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SubjectTypes
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
