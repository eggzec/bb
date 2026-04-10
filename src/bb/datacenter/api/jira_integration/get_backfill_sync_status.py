from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_backfill_sync_status_response_401 import GetBackfillSyncStatusResponse401
from ...models.get_backfill_sync_status_response_409 import GetBackfillSyncStatusResponse409
from ...models.rest_jira_backfill_status import RestJiraBackfillStatus
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/jira-dev/latest/devinfo-backfill/status",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetBackfillSyncStatusResponse401 | GetBackfillSyncStatusResponse409 | RestJiraBackfillStatus | None:
    if response.status_code == 200:
        response_200 = RestJiraBackfillStatus.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetBackfillSyncStatusResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 409:
        response_409 = GetBackfillSyncStatusResponse409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetBackfillSyncStatusResponse401 | GetBackfillSyncStatusResponse409 | RestJiraBackfillStatus]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetBackfillSyncStatusResponse401 | GetBackfillSyncStatusResponse409 | RestJiraBackfillStatus]:
    """Get Jira development information backfill status

     Returns the status of the Jira development information backfill task, either the one currently
    running or the most recently completed. The response shows aggregated counts per status for
    repositories to sync. Possible statuses: NOT_STARTED, QUEUED, SYNCING, SYNCED, CANCELED and ERROR.

    The user must have the global **SYS_ADMIN** permission.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBackfillSyncStatusResponse401 | GetBackfillSyncStatusResponse409 | RestJiraBackfillStatus]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> GetBackfillSyncStatusResponse401 | GetBackfillSyncStatusResponse409 | RestJiraBackfillStatus | None:
    """Get Jira development information backfill status

     Returns the status of the Jira development information backfill task, either the one currently
    running or the most recently completed. The response shows aggregated counts per status for
    repositories to sync. Possible statuses: NOT_STARTED, QUEUED, SYNCING, SYNCED, CANCELED and ERROR.

    The user must have the global **SYS_ADMIN** permission.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBackfillSyncStatusResponse401 | GetBackfillSyncStatusResponse409 | RestJiraBackfillStatus
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetBackfillSyncStatusResponse401 | GetBackfillSyncStatusResponse409 | RestJiraBackfillStatus]:
    """Get Jira development information backfill status

     Returns the status of the Jira development information backfill task, either the one currently
    running or the most recently completed. The response shows aggregated counts per status for
    repositories to sync. Possible statuses: NOT_STARTED, QUEUED, SYNCING, SYNCED, CANCELED and ERROR.

    The user must have the global **SYS_ADMIN** permission.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBackfillSyncStatusResponse401 | GetBackfillSyncStatusResponse409 | RestJiraBackfillStatus]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> GetBackfillSyncStatusResponse401 | GetBackfillSyncStatusResponse409 | RestJiraBackfillStatus | None:
    """Get Jira development information backfill status

     Returns the status of the Jira development information backfill task, either the one currently
    running or the most recently completed. The response shows aggregated counts per status for
    repositories to sync. Possible statuses: NOT_STARTED, QUEUED, SYNCING, SYNCED, CANCELED and ERROR.

    The user must have the global **SYS_ADMIN** permission.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBackfillSyncStatusResponse401 | GetBackfillSyncStatusResponse409 | RestJiraBackfillStatus
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
