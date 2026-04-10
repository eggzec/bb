from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_repo_sync_status_response_200 import GetRepoSyncStatusResponse200
from ...models.get_repo_sync_status_response_401 import GetRepoSyncStatusResponse401
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["start"] = start

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/mirroring/latest/supportInfo/repoSyncStatus",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetRepoSyncStatusResponse200 | GetRepoSyncStatusResponse401 | None:
    if response.status_code == 200:
        response_200 = GetRepoSyncStatusResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetRepoSyncStatusResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetRepoSyncStatusResponse200 | GetRepoSyncStatusResponse401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GetRepoSyncStatusResponse200 | GetRepoSyncStatusResponse401]:
    """Get sync status of repositories

     Retrieves a page of sync statuses of the repositories on this mirror node

    Args:
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRepoSyncStatusResponse200 | GetRepoSyncStatusResponse401]
    """

    kwargs = _get_kwargs(
        start=start,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetRepoSyncStatusResponse200 | GetRepoSyncStatusResponse401 | None:
    """Get sync status of repositories

     Retrieves a page of sync statuses of the repositories on this mirror node

    Args:
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRepoSyncStatusResponse200 | GetRepoSyncStatusResponse401
    """

    return sync_detailed(
        client=client,
        start=start,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GetRepoSyncStatusResponse200 | GetRepoSyncStatusResponse401]:
    """Get sync status of repositories

     Retrieves a page of sync statuses of the repositories on this mirror node

    Args:
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRepoSyncStatusResponse200 | GetRepoSyncStatusResponse401]
    """

    kwargs = _get_kwargs(
        start=start,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetRepoSyncStatusResponse200 | GetRepoSyncStatusResponse401 | None:
    """Get sync status of repositories

     Retrieves a page of sync statuses of the repositories on this mirror node

    Args:
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRepoSyncStatusResponse200 | GetRepoSyncStatusResponse401
    """

    return (
        await asyncio_detailed(
            client=client,
            start=start,
            limit=limit,
        )
    ).parsed
