from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_jira_dev_info_backfill_request import RestJiraDevInfoBackfillRequest
from ...models.start_backfill_sync_response_400 import StartBackfillSyncResponse400
from ...models.start_backfill_sync_response_401 import StartBackfillSyncResponse401
from ...models.start_backfill_sync_response_404 import StartBackfillSyncResponse404
from ...models.start_backfill_sync_response_409 import StartBackfillSyncResponse409
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RestJiraDevInfoBackfillRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/jira-dev/latest/devinfo-backfill",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | StartBackfillSyncResponse400
    | StartBackfillSyncResponse401
    | StartBackfillSyncResponse404
    | StartBackfillSyncResponse409
    | None
):
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 400:
        response_400 = StartBackfillSyncResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = StartBackfillSyncResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = StartBackfillSyncResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = StartBackfillSyncResponse409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | StartBackfillSyncResponse400
    | StartBackfillSyncResponse401
    | StartBackfillSyncResponse404
    | StartBackfillSyncResponse409
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RestJiraDevInfoBackfillRequest | Unset = UNSET,
) -> Response[
    Any
    | StartBackfillSyncResponse400
    | StartBackfillSyncResponse401
    | StartBackfillSyncResponse404
    | StartBackfillSyncResponse409
]:
    """Start a Jira development information backfill sync

     Starts an asynchronous repository data backfill to the provided Jira sites. The backfilled data will
    be available when viewing issues in Jira. Providing a list of repositories or Jira site IDs are
    optional. If no repositories are provided then all repositories will be backfilled. If no Jira site
    IDs are provided then data will be sent to all currently configured Jira sites.

    The user must have the global **SYS_ADMIN** permission.

    Args:
        body (RestJiraDevInfoBackfillRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | StartBackfillSyncResponse400 | StartBackfillSyncResponse401 | StartBackfillSyncResponse404 | StartBackfillSyncResponse409]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: RestJiraDevInfoBackfillRequest | Unset = UNSET,
) -> (
    Any
    | StartBackfillSyncResponse400
    | StartBackfillSyncResponse401
    | StartBackfillSyncResponse404
    | StartBackfillSyncResponse409
    | None
):
    """Start a Jira development information backfill sync

     Starts an asynchronous repository data backfill to the provided Jira sites. The backfilled data will
    be available when viewing issues in Jira. Providing a list of repositories or Jira site IDs are
    optional. If no repositories are provided then all repositories will be backfilled. If no Jira site
    IDs are provided then data will be sent to all currently configured Jira sites.

    The user must have the global **SYS_ADMIN** permission.

    Args:
        body (RestJiraDevInfoBackfillRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | StartBackfillSyncResponse400 | StartBackfillSyncResponse401 | StartBackfillSyncResponse404 | StartBackfillSyncResponse409
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RestJiraDevInfoBackfillRequest | Unset = UNSET,
) -> Response[
    Any
    | StartBackfillSyncResponse400
    | StartBackfillSyncResponse401
    | StartBackfillSyncResponse404
    | StartBackfillSyncResponse409
]:
    """Start a Jira development information backfill sync

     Starts an asynchronous repository data backfill to the provided Jira sites. The backfilled data will
    be available when viewing issues in Jira. Providing a list of repositories or Jira site IDs are
    optional. If no repositories are provided then all repositories will be backfilled. If no Jira site
    IDs are provided then data will be sent to all currently configured Jira sites.

    The user must have the global **SYS_ADMIN** permission.

    Args:
        body (RestJiraDevInfoBackfillRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | StartBackfillSyncResponse400 | StartBackfillSyncResponse401 | StartBackfillSyncResponse404 | StartBackfillSyncResponse409]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RestJiraDevInfoBackfillRequest | Unset = UNSET,
) -> (
    Any
    | StartBackfillSyncResponse400
    | StartBackfillSyncResponse401
    | StartBackfillSyncResponse404
    | StartBackfillSyncResponse409
    | None
):
    """Start a Jira development information backfill sync

     Starts an asynchronous repository data backfill to the provided Jira sites. The backfilled data will
    be available when viewing issues in Jira. Providing a list of repositories or Jira site IDs are
    optional. If no repositories are provided then all repositories will be backfilled. If no Jira site
    IDs are provided then data will be sent to all currently configured Jira sites.

    The user must have the global **SYS_ADMIN** permission.

    Args:
        body (RestJiraDevInfoBackfillRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | StartBackfillSyncResponse400 | StartBackfillSyncResponse401 | StartBackfillSyncResponse404 | StartBackfillSyncResponse409
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
