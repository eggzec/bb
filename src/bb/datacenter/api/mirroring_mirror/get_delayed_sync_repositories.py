from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_delayed_sync_repository import RestDelayedSyncRepository
from ...models.rest_errors import RestErrors
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    delay_threshold: str | Unset = UNSET,
    limit: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["delayThreshold"] = delay_threshold

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/mirroring/latest/mirrorRepos/delayed-sync",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RestErrors | list[RestDelayedSyncRepository] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RestDelayedSyncRepository.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 401:
        response_401 = RestErrors.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RestErrors | list[RestDelayedSyncRepository]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    delay_threshold: str | Unset = UNSET,
    limit: str | Unset = UNSET,
) -> Response[RestErrors | list[RestDelayedSyncRepository]]:
    """Get delayed sync repositories

     Retrieves a list of repositories which have not synced on one or more mirror nodes for at least the
    threshold time limit after the content was changed in the corresponding upstream repositories. The
    threshold time limit is defined by a configuration property
    <code>plugin.mirroring.repository.diagnostics.sync.tolerance</code>. The detection of out of sync
    repositories is dependent on the timing of a scheduled job which is controlled by a configuration
    property <code>plugin.mirroring.synchronization.interval</code> which means in worst case it can
    take upto <code>plugin.mirroring.repository.diagnostics.sync.tolerance</code> +
    <code>plugin.mirroring.synchronization.interval</code> time to detect an out-of-sync
    repository.<p>Note: If <code>plugin.mirroring.repository.diagnostics.sync.enabled=false</code> is
    set on any of the mirror farm nodes, results will not be reported from that node.

    Args:
        delay_threshold (str | Unset):
        limit (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestErrors | list[RestDelayedSyncRepository]]
    """

    kwargs = _get_kwargs(
        delay_threshold=delay_threshold,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    delay_threshold: str | Unset = UNSET,
    limit: str | Unset = UNSET,
) -> RestErrors | list[RestDelayedSyncRepository] | None:
    """Get delayed sync repositories

     Retrieves a list of repositories which have not synced on one or more mirror nodes for at least the
    threshold time limit after the content was changed in the corresponding upstream repositories. The
    threshold time limit is defined by a configuration property
    <code>plugin.mirroring.repository.diagnostics.sync.tolerance</code>. The detection of out of sync
    repositories is dependent on the timing of a scheduled job which is controlled by a configuration
    property <code>plugin.mirroring.synchronization.interval</code> which means in worst case it can
    take upto <code>plugin.mirroring.repository.diagnostics.sync.tolerance</code> +
    <code>plugin.mirroring.synchronization.interval</code> time to detect an out-of-sync
    repository.<p>Note: If <code>plugin.mirroring.repository.diagnostics.sync.enabled=false</code> is
    set on any of the mirror farm nodes, results will not be reported from that node.

    Args:
        delay_threshold (str | Unset):
        limit (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestErrors | list[RestDelayedSyncRepository]
    """

    return sync_detailed(
        client=client,
        delay_threshold=delay_threshold,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    delay_threshold: str | Unset = UNSET,
    limit: str | Unset = UNSET,
) -> Response[RestErrors | list[RestDelayedSyncRepository]]:
    """Get delayed sync repositories

     Retrieves a list of repositories which have not synced on one or more mirror nodes for at least the
    threshold time limit after the content was changed in the corresponding upstream repositories. The
    threshold time limit is defined by a configuration property
    <code>plugin.mirroring.repository.diagnostics.sync.tolerance</code>. The detection of out of sync
    repositories is dependent on the timing of a scheduled job which is controlled by a configuration
    property <code>plugin.mirroring.synchronization.interval</code> which means in worst case it can
    take upto <code>plugin.mirroring.repository.diagnostics.sync.tolerance</code> +
    <code>plugin.mirroring.synchronization.interval</code> time to detect an out-of-sync
    repository.<p>Note: If <code>plugin.mirroring.repository.diagnostics.sync.enabled=false</code> is
    set on any of the mirror farm nodes, results will not be reported from that node.

    Args:
        delay_threshold (str | Unset):
        limit (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestErrors | list[RestDelayedSyncRepository]]
    """

    kwargs = _get_kwargs(
        delay_threshold=delay_threshold,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    delay_threshold: str | Unset = UNSET,
    limit: str | Unset = UNSET,
) -> RestErrors | list[RestDelayedSyncRepository] | None:
    """Get delayed sync repositories

     Retrieves a list of repositories which have not synced on one or more mirror nodes for at least the
    threshold time limit after the content was changed in the corresponding upstream repositories. The
    threshold time limit is defined by a configuration property
    <code>plugin.mirroring.repository.diagnostics.sync.tolerance</code>. The detection of out of sync
    repositories is dependent on the timing of a scheduled job which is controlled by a configuration
    property <code>plugin.mirroring.synchronization.interval</code> which means in worst case it can
    take upto <code>plugin.mirroring.repository.diagnostics.sync.tolerance</code> +
    <code>plugin.mirroring.synchronization.interval</code> time to detect an out-of-sync
    repository.<p>Note: If <code>plugin.mirroring.repository.diagnostics.sync.enabled=false</code> is
    set on any of the mirror farm nodes, results will not be reported from that node.

    Args:
        delay_threshold (str | Unset):
        limit (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestErrors | list[RestDelayedSyncRepository]
    """

    return (
        await asyncio_detailed(
            client=client,
            delay_threshold=delay_threshold,
            limit=limit,
        )
    ).parsed
