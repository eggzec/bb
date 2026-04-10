from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_statistics_summary_1_response_401 import GetStatisticsSummary1Response401
from ...models.get_statistics_summary_1_response_404 import GetStatisticsSummary1Response404
from ...types import Response


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    webhook_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/webhooks/{webhook_id}/statistics/summary".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            webhook_id=quote(str(webhook_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetStatisticsSummary1Response401 | GetStatisticsSummary1Response404 | None:
    if response.status_code == 200:
        response_200 = response.json()
        return response_200

    if response.status_code == 401:
        response_401 = GetStatisticsSummary1Response401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetStatisticsSummary1Response404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetStatisticsSummary1Response401 | GetStatisticsSummary1Response404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    repository_slug: str,
    webhook_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetStatisticsSummary1Response401 | GetStatisticsSummary1Response404]:
    """Get webhook statistics summary

     Get the statistics summary for a specific webhook.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        webhook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetStatisticsSummary1Response401 | GetStatisticsSummary1Response404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        webhook_id=webhook_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    repository_slug: str,
    webhook_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetStatisticsSummary1Response401 | GetStatisticsSummary1Response404 | None:
    """Get webhook statistics summary

     Get the statistics summary for a specific webhook.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        webhook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetStatisticsSummary1Response401 | GetStatisticsSummary1Response404
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        webhook_id=webhook_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    webhook_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetStatisticsSummary1Response401 | GetStatisticsSummary1Response404]:
    """Get webhook statistics summary

     Get the statistics summary for a specific webhook.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        webhook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetStatisticsSummary1Response401 | GetStatisticsSummary1Response404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        webhook_id=webhook_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    webhook_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetStatisticsSummary1Response401 | GetStatisticsSummary1Response404 | None:
    """Get webhook statistics summary

     Get the statistics summary for a specific webhook.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        webhook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetStatisticsSummary1Response401 | GetStatisticsSummary1Response404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            webhook_id=webhook_id,
            client=client,
        )
    ).parsed
