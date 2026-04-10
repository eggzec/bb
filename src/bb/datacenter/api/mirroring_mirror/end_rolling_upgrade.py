from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.end_rolling_upgrade_response_401 import EndRollingUpgradeResponse401
from ...models.rest_rolling_upgrade_state import RestRollingUpgradeState
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/mirroring/latest/zdu/end",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EndRollingUpgradeResponse401 | RestRollingUpgradeState | None:
    if response.status_code == 200:
        response_200 = RestRollingUpgradeState.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = EndRollingUpgradeResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[EndRollingUpgradeResponse401 | RestRollingUpgradeState]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[EndRollingUpgradeResponse401 | RestRollingUpgradeState]:
    """End ZDU upgrade on mirror farm

     Finalizes the ZDU upgrade on the mirror farm denying heterogeneous cluster formation

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EndRollingUpgradeResponse401 | RestRollingUpgradeState]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> EndRollingUpgradeResponse401 | RestRollingUpgradeState | None:
    """End ZDU upgrade on mirror farm

     Finalizes the ZDU upgrade on the mirror farm denying heterogeneous cluster formation

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EndRollingUpgradeResponse401 | RestRollingUpgradeState
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[EndRollingUpgradeResponse401 | RestRollingUpgradeState]:
    """End ZDU upgrade on mirror farm

     Finalizes the ZDU upgrade on the mirror farm denying heterogeneous cluster formation

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EndRollingUpgradeResponse401 | RestRollingUpgradeState]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> EndRollingUpgradeResponse401 | RestRollingUpgradeState | None:
    """End ZDU upgrade on mirror farm

     Finalizes the ZDU upgrade on the mirror farm denying heterogeneous cluster formation

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EndRollingUpgradeResponse401 | RestRollingUpgradeState
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
