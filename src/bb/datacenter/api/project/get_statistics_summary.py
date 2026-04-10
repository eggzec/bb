from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_statistics_summary_response_401 import GetStatisticsSummaryResponse401
from ...models.get_statistics_summary_response_404 import GetStatisticsSummaryResponse404
from ...types import Response


def _get_kwargs(
    project_key: str,
    webhook_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/webhooks/{webhook_id}/statistics/summary".format(
            project_key=quote(str(project_key), safe=""),
            webhook_id=quote(str(webhook_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetStatisticsSummaryResponse401 | GetStatisticsSummaryResponse404 | None:
    if response.status_code == 200:
        response_200 = response.json()
        return response_200

    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = GetStatisticsSummaryResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetStatisticsSummaryResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetStatisticsSummaryResponse401 | GetStatisticsSummaryResponse404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    webhook_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetStatisticsSummaryResponse401 | GetStatisticsSummaryResponse404]:
    """Get webhook statistics summary

     Get the statistics summary for a specific webhook.

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the specified project
    to call this resource.

    Args:
        project_key (str):
        webhook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetStatisticsSummaryResponse401 | GetStatisticsSummaryResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        webhook_id=webhook_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    webhook_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetStatisticsSummaryResponse401 | GetStatisticsSummaryResponse404 | None:
    """Get webhook statistics summary

     Get the statistics summary for a specific webhook.

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the specified project
    to call this resource.

    Args:
        project_key (str):
        webhook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetStatisticsSummaryResponse401 | GetStatisticsSummaryResponse404
    """

    return sync_detailed(
        project_key=project_key,
        webhook_id=webhook_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    webhook_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetStatisticsSummaryResponse401 | GetStatisticsSummaryResponse404]:
    """Get webhook statistics summary

     Get the statistics summary for a specific webhook.

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the specified project
    to call this resource.

    Args:
        project_key (str):
        webhook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetStatisticsSummaryResponse401 | GetStatisticsSummaryResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        webhook_id=webhook_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    webhook_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetStatisticsSummaryResponse401 | GetStatisticsSummaryResponse404 | None:
    """Get webhook statistics summary

     Get the statistics summary for a specific webhook.

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the specified project
    to call this resource.

    Args:
        project_key (str):
        webhook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetStatisticsSummaryResponse401 | GetStatisticsSummaryResponse404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            webhook_id=webhook_id,
            client=client,
        )
    ).parsed
