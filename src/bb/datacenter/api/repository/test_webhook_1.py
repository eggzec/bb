from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_webhook_credentials import RestWebhookCredentials
from ...models.test_webhook_1_response_401 import TestWebhook1Response401
from ...models.test_webhook_1_response_404 import TestWebhook1Response404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    *,
    body: RestWebhookCredentials | Unset = UNSET,
    webhook_id: int | Unset = UNSET,
    ssl_verification_required: str | Unset = UNSET,
    url_query: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["webhookId"] = webhook_id

    params["sslVerificationRequired"] = ssl_verification_required

    params["url"] = url_query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/webhooks/test".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
        ),
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | TestWebhook1Response401 | TestWebhook1Response404 | None:
    if response.status_code == 200:
        response_200 = response.json()
        return response_200

    if response.status_code == 401:
        response_401 = TestWebhook1Response401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = TestWebhook1Response404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | TestWebhook1Response401 | TestWebhook1Response404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestWebhookCredentials | Unset = UNSET,
    webhook_id: int | Unset = UNSET,
    ssl_verification_required: str | Unset = UNSET,
    url_query: str | Unset = UNSET,
) -> Response[Any | TestWebhook1Response401 | TestWebhook1Response404]:
    """Test webhook

     Test connectivity to a specific endpoint.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        webhook_id (int | Unset):
        ssl_verification_required (str | Unset):
        url_query (str | Unset):
        body (RestWebhookCredentials | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TestWebhook1Response401 | TestWebhook1Response404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        body=body,
        webhook_id=webhook_id,
        ssl_verification_required=ssl_verification_required,
        url_query=url_query,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestWebhookCredentials | Unset = UNSET,
    webhook_id: int | Unset = UNSET,
    ssl_verification_required: str | Unset = UNSET,
    url_query: str | Unset = UNSET,
) -> Any | TestWebhook1Response401 | TestWebhook1Response404 | None:
    """Test webhook

     Test connectivity to a specific endpoint.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        webhook_id (int | Unset):
        ssl_verification_required (str | Unset):
        url_query (str | Unset):
        body (RestWebhookCredentials | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TestWebhook1Response401 | TestWebhook1Response404
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        client=client,
        body=body,
        webhook_id=webhook_id,
        ssl_verification_required=ssl_verification_required,
        url_query=url_query,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestWebhookCredentials | Unset = UNSET,
    webhook_id: int | Unset = UNSET,
    ssl_verification_required: str | Unset = UNSET,
    url_query: str | Unset = UNSET,
) -> Response[Any | TestWebhook1Response401 | TestWebhook1Response404]:
    """Test webhook

     Test connectivity to a specific endpoint.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        webhook_id (int | Unset):
        ssl_verification_required (str | Unset):
        url_query (str | Unset):
        body (RestWebhookCredentials | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TestWebhook1Response401 | TestWebhook1Response404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        body=body,
        webhook_id=webhook_id,
        ssl_verification_required=ssl_verification_required,
        url_query=url_query,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestWebhookCredentials | Unset = UNSET,
    webhook_id: int | Unset = UNSET,
    ssl_verification_required: str | Unset = UNSET,
    url_query: str | Unset = UNSET,
) -> Any | TestWebhook1Response401 | TestWebhook1Response404 | None:
    """Test webhook

     Test connectivity to a specific endpoint.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        webhook_id (int | Unset):
        ssl_verification_required (str | Unset):
        url_query (str | Unset):
        body (RestWebhookCredentials | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TestWebhook1Response401 | TestWebhook1Response404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            client=client,
            body=body,
            webhook_id=webhook_id,
            ssl_verification_required=ssl_verification_required,
            url_query=url_query,
        )
    ).parsed
