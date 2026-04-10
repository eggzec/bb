from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.search_webhooks_response_401 import SearchWebhooksResponse401
from ...models.search_webhooks_response_404 import SearchWebhooksResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    *,
    scope_type: str | Unset = UNSET,
    event: str | Unset = UNSET,
    statistics: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["scopeType"] = scope_type

    params["event"] = event

    params["statistics"] = statistics

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/webhooks/search".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | SearchWebhooksResponse401 | SearchWebhooksResponse404 | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 401:
        response_401 = SearchWebhooksResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = SearchWebhooksResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | SearchWebhooksResponse401 | SearchWebhooksResponse404]:
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
    scope_type: str | Unset = UNSET,
    event: str | Unset = UNSET,
    statistics: bool | Unset = UNSET,
) -> Response[Any | SearchWebhooksResponse401 | SearchWebhooksResponse404]:
    """Search webhooks

     Search webhooks in this repository and parent project. This endpoint returns a superset of the
    results returned by the /webhooks endpoint because it allows filtering by project scope too, not
    just repository webhooks.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        scope_type (str | Unset):
        event (str | Unset):
        statistics (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SearchWebhooksResponse401 | SearchWebhooksResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        scope_type=scope_type,
        event=event,
        statistics=statistics,
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
    scope_type: str | Unset = UNSET,
    event: str | Unset = UNSET,
    statistics: bool | Unset = UNSET,
) -> Any | SearchWebhooksResponse401 | SearchWebhooksResponse404 | None:
    """Search webhooks

     Search webhooks in this repository and parent project. This endpoint returns a superset of the
    results returned by the /webhooks endpoint because it allows filtering by project scope too, not
    just repository webhooks.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        scope_type (str | Unset):
        event (str | Unset):
        statistics (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SearchWebhooksResponse401 | SearchWebhooksResponse404
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        client=client,
        scope_type=scope_type,
        event=event,
        statistics=statistics,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    scope_type: str | Unset = UNSET,
    event: str | Unset = UNSET,
    statistics: bool | Unset = UNSET,
) -> Response[Any | SearchWebhooksResponse401 | SearchWebhooksResponse404]:
    """Search webhooks

     Search webhooks in this repository and parent project. This endpoint returns a superset of the
    results returned by the /webhooks endpoint because it allows filtering by project scope too, not
    just repository webhooks.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        scope_type (str | Unset):
        event (str | Unset):
        statistics (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SearchWebhooksResponse401 | SearchWebhooksResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        scope_type=scope_type,
        event=event,
        statistics=statistics,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    scope_type: str | Unset = UNSET,
    event: str | Unset = UNSET,
    statistics: bool | Unset = UNSET,
) -> Any | SearchWebhooksResponse401 | SearchWebhooksResponse404 | None:
    """Search webhooks

     Search webhooks in this repository and parent project. This endpoint returns a superset of the
    results returned by the /webhooks endpoint because it allows filtering by project scope too, not
    just repository webhooks.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        scope_type (str | Unset):
        event (str | Unset):
        statistics (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SearchWebhooksResponse401 | SearchWebhooksResponse404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            client=client,
            scope_type=scope_type,
            event=event,
            statistics=statistics,
        )
    ).parsed
