from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.get_hook_events_subject_type_subject_type import GetHookEventsSubjectTypeSubjectType
from ...models.paginated_hook_events import PaginatedHookEvents
from ...types import Response

__all__ = [
    "sync_detailed",
    "asyncio_detailed",
    "sync",
    "asyncio",
]


def _get_kwargs(
    subject_type: GetHookEventsSubjectTypeSubjectType,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/hook_events/{subject_type}".format(
            subject_type=quote(str(subject_type), safe=""),
        ),
    }

    return _kwargs


type ParsedPayload = Error | PaginatedHookEvents
type ParseResult = Error | PaginatedHookEvents | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        response_200 = PaginatedHookEvents.from_dict(response.json())

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
    subject_type: GetHookEventsSubjectTypeSubjectType,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """List subscribable webhook types

     Returns a paginated list of all valid webhook events for the
    specified entity.
    **The team and user webhooks are deprecated, and you should use workspace instead.
    For more information, see [the
    announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-teams-deprecation/).**

    This is public data that does not require any scopes or authentication.

    NOTE: The example response is a truncated response object for the `workspace` `subject_type`.
    We return the same structure for the other `subject_type` objects.

    Args:
        subject_type (GetHookEventsSubjectTypeSubjectType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PaginatedHookEvents]
    """

    kwargs = _get_kwargs(
        subject_type=subject_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    subject_type: GetHookEventsSubjectTypeSubjectType,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    """List subscribable webhook types

     Returns a paginated list of all valid webhook events for the
    specified entity.
    **The team and user webhooks are deprecated, and you should use workspace instead.
    For more information, see [the
    announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-teams-deprecation/).**

    This is public data that does not require any scopes or authentication.

    NOTE: The example response is a truncated response object for the `workspace` `subject_type`.
    We return the same structure for the other `subject_type` objects.

    Args:
        subject_type (GetHookEventsSubjectTypeSubjectType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PaginatedHookEvents
    """

    return sync_detailed(
        subject_type=subject_type,
        client=client,
    ).parsed


async def asyncio_detailed(
    subject_type: GetHookEventsSubjectTypeSubjectType,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """List subscribable webhook types

     Returns a paginated list of all valid webhook events for the
    specified entity.
    **The team and user webhooks are deprecated, and you should use workspace instead.
    For more information, see [the
    announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-teams-deprecation/).**

    This is public data that does not require any scopes or authentication.

    NOTE: The example response is a truncated response object for the `workspace` `subject_type`.
    We return the same structure for the other `subject_type` objects.

    Args:
        subject_type (GetHookEventsSubjectTypeSubjectType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PaginatedHookEvents]
    """

    kwargs = _get_kwargs(
        subject_type=subject_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    subject_type: GetHookEventsSubjectTypeSubjectType,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    """List subscribable webhook types

     Returns a paginated list of all valid webhook events for the
    specified entity.
    **The team and user webhooks are deprecated, and you should use workspace instead.
    For more information, see [the
    announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-teams-deprecation/).**

    This is public data that does not require any scopes or authentication.

    NOTE: The example response is a truncated response object for the `workspace` `subject_type`.
    We return the same structure for the other `subject_type` objects.

    Args:
        subject_type (GetHookEventsSubjectTypeSubjectType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PaginatedHookEvents
    """

    return (
        await asyncio_detailed(
            subject_type=subject_type,
            client=client,
        )
    ).parsed
