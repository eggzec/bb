from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_level_response_401 import GetLevelResponse401
from ...models.rest_log_level import RestLogLevel
from ...types import Response


def _get_kwargs(
    logger_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/logs/logger/{logger_name}".format(
            logger_name=quote(str(logger_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetLevelResponse401 | RestLogLevel | None:
    if response.status_code == 200:
        response_200 = RestLogLevel.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetLevelResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetLevelResponse401 | RestLogLevel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    logger_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetLevelResponse401 | RestLogLevel]:
    """Get current log level

     Retrieve the current log level for a given logger.

    The authenticated user must have <strong>SYS_ADMIN</strong> permission or higher to call this
    resource.

    Args:
        logger_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetLevelResponse401 | RestLogLevel]
    """

    kwargs = _get_kwargs(
        logger_name=logger_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    logger_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetLevelResponse401 | RestLogLevel | None:
    """Get current log level

     Retrieve the current log level for a given logger.

    The authenticated user must have <strong>SYS_ADMIN</strong> permission or higher to call this
    resource.

    Args:
        logger_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetLevelResponse401 | RestLogLevel
    """

    return sync_detailed(
        logger_name=logger_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    logger_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetLevelResponse401 | RestLogLevel]:
    """Get current log level

     Retrieve the current log level for a given logger.

    The authenticated user must have <strong>SYS_ADMIN</strong> permission or higher to call this
    resource.

    Args:
        logger_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetLevelResponse401 | RestLogLevel]
    """

    kwargs = _get_kwargs(
        logger_name=logger_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    logger_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetLevelResponse401 | RestLogLevel | None:
    """Get current log level

     Retrieve the current log level for a given logger.

    The authenticated user must have <strong>SYS_ADMIN</strong> permission or higher to call this
    resource.

    Args:
        logger_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetLevelResponse401 | RestLogLevel
    """

    return (
        await asyncio_detailed(
            logger_name=logger_name,
            client=client,
        )
    ).parsed
