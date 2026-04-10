from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.find_webhooks_response_401 import FindWebhooksResponse401
from ...models.find_webhooks_response_404 import FindWebhooksResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    *,
    event: str | Unset = UNSET,
    statistics: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["event"] = event

    params["statistics"] = statistics

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/webhooks".format(
            project_key=quote(str(project_key), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | FindWebhooksResponse401 | FindWebhooksResponse404 | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 401:
        response_401 = FindWebhooksResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = FindWebhooksResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | FindWebhooksResponse401 | FindWebhooksResponse404]:
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
    event: str | Unset = UNSET,
    statistics: bool | Unset = UNSET,
) -> Response[Any | FindWebhooksResponse401 | FindWebhooksResponse404]:
    """Find webhooks

     Find webhooks in this project.

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the specified project
    to call this resource.

    Args:
        project_key (str):
        event (str | Unset):
        statistics (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FindWebhooksResponse401 | FindWebhooksResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        event=event,
        statistics=statistics,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    event: str | Unset = UNSET,
    statistics: bool | Unset = UNSET,
) -> Any | FindWebhooksResponse401 | FindWebhooksResponse404 | None:
    """Find webhooks

     Find webhooks in this project.

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the specified project
    to call this resource.

    Args:
        project_key (str):
        event (str | Unset):
        statistics (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FindWebhooksResponse401 | FindWebhooksResponse404
    """

    return sync_detailed(
        project_key=project_key,
        client=client,
        event=event,
        statistics=statistics,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    event: str | Unset = UNSET,
    statistics: bool | Unset = UNSET,
) -> Response[Any | FindWebhooksResponse401 | FindWebhooksResponse404]:
    """Find webhooks

     Find webhooks in this project.

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the specified project
    to call this resource.

    Args:
        project_key (str):
        event (str | Unset):
        statistics (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FindWebhooksResponse401 | FindWebhooksResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        event=event,
        statistics=statistics,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    event: str | Unset = UNSET,
    statistics: bool | Unset = UNSET,
) -> Any | FindWebhooksResponse401 | FindWebhooksResponse404 | None:
    """Find webhooks

     Find webhooks in this project.

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the specified project
    to call this resource.

    Args:
        project_key (str):
        event (str | Unset):
        statistics (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FindWebhooksResponse401 | FindWebhooksResponse404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            client=client,
            event=event,
            statistics=statistics,
        )
    ).parsed
