from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_latest_invocation_1_response_401 import GetLatestInvocation1Response401
from ...models.get_latest_invocation_1_response_404 import GetLatestInvocation1Response404
from ...models.rest_detailed_invocation import RestDetailedInvocation
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    webhook_id: str,
    *,
    event: str | Unset = UNSET,
    outcome: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["event"] = event

    params["outcome"] = outcome

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/webhooks/{webhook_id}/latest".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            webhook_id=quote(str(webhook_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetLatestInvocation1Response401 | GetLatestInvocation1Response404 | RestDetailedInvocation | None:
    if response.status_code == 200:
        response_200 = RestDetailedInvocation.from_dict(response.json())

        return response_200

    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = GetLatestInvocation1Response401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetLatestInvocation1Response404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetLatestInvocation1Response401 | GetLatestInvocation1Response404 | RestDetailedInvocation]:
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
    event: str | Unset = UNSET,
    outcome: str | Unset = UNSET,
) -> Response[Any | GetLatestInvocation1Response401 | GetLatestInvocation1Response404 | RestDetailedInvocation]:
    """Get last webhook invocation details

     Get the latest invocations for a specific webhook.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        webhook_id (str):
        event (str | Unset):
        outcome (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetLatestInvocation1Response401 | GetLatestInvocation1Response404 | RestDetailedInvocation]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        webhook_id=webhook_id,
        event=event,
        outcome=outcome,
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
    event: str | Unset = UNSET,
    outcome: str | Unset = UNSET,
) -> Any | GetLatestInvocation1Response401 | GetLatestInvocation1Response404 | RestDetailedInvocation | None:
    """Get last webhook invocation details

     Get the latest invocations for a specific webhook.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        webhook_id (str):
        event (str | Unset):
        outcome (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetLatestInvocation1Response401 | GetLatestInvocation1Response404 | RestDetailedInvocation
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        webhook_id=webhook_id,
        client=client,
        event=event,
        outcome=outcome,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    webhook_id: str,
    *,
    client: AuthenticatedClient | Client,
    event: str | Unset = UNSET,
    outcome: str | Unset = UNSET,
) -> Response[Any | GetLatestInvocation1Response401 | GetLatestInvocation1Response404 | RestDetailedInvocation]:
    """Get last webhook invocation details

     Get the latest invocations for a specific webhook.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        webhook_id (str):
        event (str | Unset):
        outcome (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetLatestInvocation1Response401 | GetLatestInvocation1Response404 | RestDetailedInvocation]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        webhook_id=webhook_id,
        event=event,
        outcome=outcome,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    webhook_id: str,
    *,
    client: AuthenticatedClient | Client,
    event: str | Unset = UNSET,
    outcome: str | Unset = UNSET,
) -> Any | GetLatestInvocation1Response401 | GetLatestInvocation1Response404 | RestDetailedInvocation | None:
    """Get last webhook invocation details

     Get the latest invocations for a specific webhook.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        webhook_id (str):
        event (str | Unset):
        outcome (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetLatestInvocation1Response401 | GetLatestInvocation1Response404 | RestDetailedInvocation
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            webhook_id=webhook_id,
            client=client,
            event=event,
            outcome=outcome,
        )
    ).parsed
