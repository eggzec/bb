from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_backfill_sync_report_response_401 import GetBackfillSyncReportResponse401
from ...models.get_backfill_sync_report_response_409 import GetBackfillSyncReportResponse409
from ...models.rest_jira_backfill_report import RestJiraBackfillReport
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/jira-dev/latest/devinfo-backfill/report",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetBackfillSyncReportResponse401 | GetBackfillSyncReportResponse409 | RestJiraBackfillReport | None:
    if response.status_code == 200:
        response_200 = RestJiraBackfillReport.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetBackfillSyncReportResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 409:
        response_409 = GetBackfillSyncReportResponse409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetBackfillSyncReportResponse401 | GetBackfillSyncReportResponse409 | RestJiraBackfillReport]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetBackfillSyncReportResponse401 | GetBackfillSyncReportResponse409 | RestJiraBackfillReport]:
    """Get repository backfill tasks that failed and their associated errors

     Get the list of repositories that failed the latest backfill task and their associated errors

    The user must have the global **SYS_ADMIN** permission.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBackfillSyncReportResponse401 | GetBackfillSyncReportResponse409 | RestJiraBackfillReport]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> GetBackfillSyncReportResponse401 | GetBackfillSyncReportResponse409 | RestJiraBackfillReport | None:
    """Get repository backfill tasks that failed and their associated errors

     Get the list of repositories that failed the latest backfill task and their associated errors

    The user must have the global **SYS_ADMIN** permission.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBackfillSyncReportResponse401 | GetBackfillSyncReportResponse409 | RestJiraBackfillReport
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetBackfillSyncReportResponse401 | GetBackfillSyncReportResponse409 | RestJiraBackfillReport]:
    """Get repository backfill tasks that failed and their associated errors

     Get the list of repositories that failed the latest backfill task and their associated errors

    The user must have the global **SYS_ADMIN** permission.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBackfillSyncReportResponse401 | GetBackfillSyncReportResponse409 | RestJiraBackfillReport]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> GetBackfillSyncReportResponse401 | GetBackfillSyncReportResponse409 | RestJiraBackfillReport | None:
    """Get repository backfill tasks that failed and their associated errors

     Get the list of repositories that failed the latest backfill task and their associated errors

    The user must have the global **SYS_ADMIN** permission.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBackfillSyncReportResponse401 | GetBackfillSyncReportResponse409 | RestJiraBackfillReport
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
