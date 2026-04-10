from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_webhook_response_401 import GetWebhookResponse401
from ...models.get_webhook_response_404 import GetWebhookResponse404
from ...models.rest_webhook import RestWebhook
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    webhook_id: str,
    *,
    statistics: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["statistics"] = statistics

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/webhooks/{webhook_id}".format(
            project_key=quote(str(project_key), safe=""),
            webhook_id=quote(str(webhook_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetWebhookResponse401 | GetWebhookResponse404 | RestWebhook | None:
    if response.status_code == 200:
        response_200 = RestWebhook.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetWebhookResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetWebhookResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetWebhookResponse401 | GetWebhookResponse404 | RestWebhook]:
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
    statistics: str | Unset = UNSET,
) -> Response[GetWebhookResponse401 | GetWebhookResponse404 | RestWebhook]:
    """Get webhook

     Get a webhook by ID.

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the specified project
    to call this resource.

    Args:
        project_key (str):
        webhook_id (str):
        statistics (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWebhookResponse401 | GetWebhookResponse404 | RestWebhook]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        webhook_id=webhook_id,
        statistics=statistics,
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
    statistics: str | Unset = UNSET,
) -> GetWebhookResponse401 | GetWebhookResponse404 | RestWebhook | None:
    """Get webhook

     Get a webhook by ID.

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the specified project
    to call this resource.

    Args:
        project_key (str):
        webhook_id (str):
        statistics (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWebhookResponse401 | GetWebhookResponse404 | RestWebhook
    """

    return sync_detailed(
        project_key=project_key,
        webhook_id=webhook_id,
        client=client,
        statistics=statistics,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    webhook_id: str,
    *,
    client: AuthenticatedClient | Client,
    statistics: str | Unset = UNSET,
) -> Response[GetWebhookResponse401 | GetWebhookResponse404 | RestWebhook]:
    """Get webhook

     Get a webhook by ID.

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the specified project
    to call this resource.

    Args:
        project_key (str):
        webhook_id (str):
        statistics (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWebhookResponse401 | GetWebhookResponse404 | RestWebhook]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        webhook_id=webhook_id,
        statistics=statistics,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    webhook_id: str,
    *,
    client: AuthenticatedClient | Client,
    statistics: str | Unset = UNSET,
) -> GetWebhookResponse401 | GetWebhookResponse404 | RestWebhook | None:
    """Get webhook

     Get a webhook by ID.

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the specified project
    to call this resource.

    Args:
        project_key (str):
        webhook_id (str):
        statistics (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWebhookResponse401 | GetWebhookResponse404 | RestWebhook
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            webhook_id=webhook_id,
            client=client,
            statistics=statistics,
        )
    ).parsed
