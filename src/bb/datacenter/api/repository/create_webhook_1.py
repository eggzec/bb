from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_webhook_1_response_400 import CreateWebhook1Response400
from ...models.create_webhook_1_response_401 import CreateWebhook1Response401
from ...models.create_webhook_1_response_404 import CreateWebhook1Response404
from ...models.rest_webhook import RestWebhook
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    *,
    body: RestWebhook | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/webhooks".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateWebhook1Response400 | CreateWebhook1Response401 | CreateWebhook1Response404 | RestWebhook | None:
    if response.status_code == 200:
        response_200 = RestWebhook.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CreateWebhook1Response400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = CreateWebhook1Response401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = CreateWebhook1Response404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateWebhook1Response400 | CreateWebhook1Response401 | CreateWebhook1Response404 | RestWebhook]:
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
    body: RestWebhook | Unset = UNSET,
) -> Response[CreateWebhook1Response400 | CreateWebhook1Response401 | CreateWebhook1Response404 | RestWebhook]:
    """Create webhook

     Create a webhook for the repository specified via the URL.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestWebhook | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateWebhook1Response400 | CreateWebhook1Response401 | CreateWebhook1Response404 | RestWebhook]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        body=body,
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
    body: RestWebhook | Unset = UNSET,
) -> CreateWebhook1Response400 | CreateWebhook1Response401 | CreateWebhook1Response404 | RestWebhook | None:
    """Create webhook

     Create a webhook for the repository specified via the URL.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestWebhook | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateWebhook1Response400 | CreateWebhook1Response401 | CreateWebhook1Response404 | RestWebhook
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestWebhook | Unset = UNSET,
) -> Response[CreateWebhook1Response400 | CreateWebhook1Response401 | CreateWebhook1Response404 | RestWebhook]:
    """Create webhook

     Create a webhook for the repository specified via the URL.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestWebhook | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateWebhook1Response400 | CreateWebhook1Response401 | CreateWebhook1Response404 | RestWebhook]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestWebhook | Unset = UNSET,
) -> CreateWebhook1Response400 | CreateWebhook1Response401 | CreateWebhook1Response404 | RestWebhook | None:
    """Create webhook

     Create a webhook for the repository specified via the URL.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestWebhook | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateWebhook1Response400 | CreateWebhook1Response401 | CreateWebhook1Response404 | RestWebhook
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            client=client,
            body=body,
        )
    ).parsed
