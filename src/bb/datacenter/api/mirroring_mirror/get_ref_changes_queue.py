from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_errors import RestErrors
from ...models.rest_ref_sync_queue import RestRefSyncQueue
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/mirroring/latest/supportInfo/refChangesQueue",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RestErrors | RestRefSyncQueue | None:
    if response.status_code == 200:
        response_200 = RestRefSyncQueue.from_dict(response.json())

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
) -> Response[RestErrors | RestRefSyncQueue]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[RestErrors | RestRefSyncQueue]:
    """Get items in ref changes queue

     Retrieves a list of up to <code>plugin.mirroring.farm.max.ref.change.queue.dump.size</code> items
    currently in the ref changes queue. The ref changes queue is an internal component of every mirror
    farm, and is shared between all nodes. When the contents of an upstream repository changes, an item
    is added to this queue so that the mirror farm nodes know to synchronize. The mirror farm constantly
    polls and removes items from this queue for processing, so it is empty most of the time.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestErrors | RestRefSyncQueue]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> RestErrors | RestRefSyncQueue | None:
    """Get items in ref changes queue

     Retrieves a list of up to <code>plugin.mirroring.farm.max.ref.change.queue.dump.size</code> items
    currently in the ref changes queue. The ref changes queue is an internal component of every mirror
    farm, and is shared between all nodes. When the contents of an upstream repository changes, an item
    is added to this queue so that the mirror farm nodes know to synchronize. The mirror farm constantly
    polls and removes items from this queue for processing, so it is empty most of the time.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestErrors | RestRefSyncQueue
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[RestErrors | RestRefSyncQueue]:
    """Get items in ref changes queue

     Retrieves a list of up to <code>plugin.mirroring.farm.max.ref.change.queue.dump.size</code> items
    currently in the ref changes queue. The ref changes queue is an internal component of every mirror
    farm, and is shared between all nodes. When the contents of an upstream repository changes, an item
    is added to this queue so that the mirror farm nodes know to synchronize. The mirror farm constantly
    polls and removes items from this queue for processing, so it is empty most of the time.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestErrors | RestRefSyncQueue]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> RestErrors | RestRefSyncQueue | None:
    """Get items in ref changes queue

     Retrieves a list of up to <code>plugin.mirroring.farm.max.ref.change.queue.dump.size</code> items
    currently in the ref changes queue. The ref changes queue is an internal component of every mirror
    farm, and is shared between all nodes. When the contents of an upstream repository changes, an item
    is added to this queue so that the mirror farm nodes know to synchronize. The mirror farm constantly
    polls and removes items from this queue for processing, so it is empty most of the time.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestErrors | RestRefSyncQueue
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
