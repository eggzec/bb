from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_webhook import RestWebhook
from ...models.update_webhook_1_response_401 import UpdateWebhook1Response401
from ...models.update_webhook_1_response_404 import UpdateWebhook1Response404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    webhook_id: str,
    *,
    body: RestWebhook | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/webhooks/{webhook_id}".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            webhook_id=quote(str(webhook_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RestWebhook | UpdateWebhook1Response401 | UpdateWebhook1Response404 | None:
    if response.status_code == 200:
        response_200 = RestWebhook.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = UpdateWebhook1Response401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = UpdateWebhook1Response404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RestWebhook | UpdateWebhook1Response401 | UpdateWebhook1Response404]:
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
    body: RestWebhook | Unset = UNSET,
) -> Response[RestWebhook | UpdateWebhook1Response401 | UpdateWebhook1Response404]:
    """Update webhook

     Update an existing webhook.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        webhook_id (str):
        body (RestWebhook | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestWebhook | UpdateWebhook1Response401 | UpdateWebhook1Response404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        webhook_id=webhook_id,
        body=body,
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
    body: RestWebhook | Unset = UNSET,
) -> RestWebhook | UpdateWebhook1Response401 | UpdateWebhook1Response404 | None:
    """Update webhook

     Update an existing webhook.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        webhook_id (str):
        body (RestWebhook | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestWebhook | UpdateWebhook1Response401 | UpdateWebhook1Response404
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        webhook_id=webhook_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    webhook_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestWebhook | Unset = UNSET,
) -> Response[RestWebhook | UpdateWebhook1Response401 | UpdateWebhook1Response404]:
    """Update webhook

     Update an existing webhook.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        webhook_id (str):
        body (RestWebhook | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestWebhook | UpdateWebhook1Response401 | UpdateWebhook1Response404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        webhook_id=webhook_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    webhook_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestWebhook | Unset = UNSET,
) -> RestWebhook | UpdateWebhook1Response401 | UpdateWebhook1Response404 | None:
    """Update webhook

     Update an existing webhook.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        webhook_id (str):
        body (RestWebhook | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestWebhook | UpdateWebhook1Response401 | UpdateWebhook1Response404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            webhook_id=webhook_id,
            client=client,
            body=body,
        )
    ).parsed
