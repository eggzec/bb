from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_settings_2_response_401 import GetSettings2Response401
from ...models.rest_logging_settings import RestLoggingSettings
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/logs/settings",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetSettings2Response401 | RestLoggingSettings | None:
    if response.status_code == 200:
        response_200 = RestLoggingSettings.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetSettings2Response401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetSettings2Response401 | RestLoggingSettings]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetSettings2Response401 | RestLoggingSettings]:
    """Get debug logging and profiling

     Returns whether debug logging and profiling are enabled.

    The authenticated user must have <strong>SYS_ADMIN</strong> permission to call this resource.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSettings2Response401 | RestLoggingSettings]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> GetSettings2Response401 | RestLoggingSettings | None:
    """Get debug logging and profiling

     Returns whether debug logging and profiling are enabled.

    The authenticated user must have <strong>SYS_ADMIN</strong> permission to call this resource.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSettings2Response401 | RestLoggingSettings
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetSettings2Response401 | RestLoggingSettings]:
    """Get debug logging and profiling

     Returns whether debug logging and profiling are enabled.

    The authenticated user must have <strong>SYS_ADMIN</strong> permission to call this resource.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSettings2Response401 | RestLoggingSettings]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> GetSettings2Response401 | RestLoggingSettings | None:
    """Get debug logging and profiling

     Returns whether debug logging and profiling are enabled.

    The authenticated user must have <strong>SYS_ADMIN</strong> permission to call this resource.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSettings2Response401 | RestLoggingSettings
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
