from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_build_status_stats_response_401 import GetBuildStatusStatsResponse401
from ...models.rest_build_stats import RestBuildStats
from ...types import UNSET, Response, Unset


def _get_kwargs(
    commit_id: str,
    *,
    include_unique: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["includeUnique"] = include_unique

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/build-status/latest/commits/stats/{commit_id}".format(
            commit_id=quote(str(commit_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetBuildStatusStatsResponse401 | RestBuildStats | None:
    if response.status_code == 200:
        response_200 = RestBuildStats.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetBuildStatusStatsResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetBuildStatusStatsResponse401 | RestBuildStats]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    commit_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_unique: bool | Unset = UNSET,
) -> Response[GetBuildStatusStatsResponse401 | RestBuildStats]:
    """Get build status statistics for commit

     Gets statistics regarding the builds associated with a commit

    Args:
        commit_id (str):
        include_unique (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBuildStatusStatsResponse401 | RestBuildStats]
    """

    kwargs = _get_kwargs(
        commit_id=commit_id,
        include_unique=include_unique,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    commit_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_unique: bool | Unset = UNSET,
) -> GetBuildStatusStatsResponse401 | RestBuildStats | None:
    """Get build status statistics for commit

     Gets statistics regarding the builds associated with a commit

    Args:
        commit_id (str):
        include_unique (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBuildStatusStatsResponse401 | RestBuildStats
    """

    return sync_detailed(
        commit_id=commit_id,
        client=client,
        include_unique=include_unique,
    ).parsed


async def asyncio_detailed(
    commit_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_unique: bool | Unset = UNSET,
) -> Response[GetBuildStatusStatsResponse401 | RestBuildStats]:
    """Get build status statistics for commit

     Gets statistics regarding the builds associated with a commit

    Args:
        commit_id (str):
        include_unique (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBuildStatusStatsResponse401 | RestBuildStats]
    """

    kwargs = _get_kwargs(
        commit_id=commit_id,
        include_unique=include_unique,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    commit_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_unique: bool | Unset = UNSET,
) -> GetBuildStatusStatsResponse401 | RestBuildStats | None:
    """Get build status statistics for commit

     Gets statistics regarding the builds associated with a commit

    Args:
        commit_id (str):
        include_unique (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBuildStatusStatsResponse401 | RestBuildStats
    """

    return (
        await asyncio_detailed(
            commit_id=commit_id,
            client=client,
            include_unique=include_unique,
        )
    ).parsed
