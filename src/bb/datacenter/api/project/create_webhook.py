from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_webhook_response_400 import CreateWebhookResponse400
from ...models.create_webhook_response_401 import CreateWebhookResponse401
from ...models.create_webhook_response_404 import CreateWebhookResponse404
from ...models.rest_webhook import RestWebhook
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    *,
    body: RestWebhook | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/latest/projects/{project_key}/webhooks".format(
            project_key=quote(str(project_key), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateWebhookResponse400 | CreateWebhookResponse401 | CreateWebhookResponse404 | RestWebhook | None:
    if response.status_code == 200:
        response_200 = RestWebhook.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CreateWebhookResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = CreateWebhookResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = CreateWebhookResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateWebhookResponse400 | CreateWebhookResponse401 | CreateWebhookResponse404 | RestWebhook]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestWebhook | Unset = UNSET,
) -> Response[CreateWebhookResponse400 | CreateWebhookResponse401 | CreateWebhookResponse404 | RestWebhook]:
    """Create webhook

     Create a webhook for the project specified via the URL.

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the specified project
    to call this resource.

    Args:
        project_key (str):
        body (RestWebhook | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateWebhookResponse400 | CreateWebhookResponse401 | CreateWebhookResponse404 | RestWebhook]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestWebhook | Unset = UNSET,
) -> CreateWebhookResponse400 | CreateWebhookResponse401 | CreateWebhookResponse404 | RestWebhook | None:
    """Create webhook

     Create a webhook for the project specified via the URL.

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the specified project
    to call this resource.

    Args:
        project_key (str):
        body (RestWebhook | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateWebhookResponse400 | CreateWebhookResponse401 | CreateWebhookResponse404 | RestWebhook
    """

    return sync_detailed(
        project_key=project_key,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestWebhook | Unset = UNSET,
) -> Response[CreateWebhookResponse400 | CreateWebhookResponse401 | CreateWebhookResponse404 | RestWebhook]:
    """Create webhook

     Create a webhook for the project specified via the URL.

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the specified project
    to call this resource.

    Args:
        project_key (str):
        body (RestWebhook | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateWebhookResponse400 | CreateWebhookResponse401 | CreateWebhookResponse404 | RestWebhook]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestWebhook | Unset = UNSET,
) -> CreateWebhookResponse400 | CreateWebhookResponse401 | CreateWebhookResponse404 | RestWebhook | None:
    """Create webhook

     Create a webhook for the project specified via the URL.

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the specified project
    to call this resource.

    Args:
        project_key (str):
        body (RestWebhook | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateWebhookResponse400 | CreateWebhookResponse401 | CreateWebhookResponse404 | RestWebhook
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            client=client,
            body=body,
        )
    ).parsed
