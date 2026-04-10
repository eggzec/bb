from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.set_level_response_400 import SetLevelResponse400
from ...models.set_level_response_401 import SetLevelResponse401
from ...types import Response


def _get_kwargs(
    logger_name: str,
    level_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/latest/logs/logger/{logger_name}/{level_name}".format(
            logger_name=quote(str(logger_name), safe=""),
            level_name=quote(str(level_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | SetLevelResponse400 | SetLevelResponse401 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = SetLevelResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = SetLevelResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | SetLevelResponse400 | SetLevelResponse401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    logger_name: str,
    level_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | SetLevelResponse400 | SetLevelResponse401]:
    """Set log level

     Set the current log level for a given logger.

    The authenticated user must have <strong>SYS_ADMIN</strong> permission or higher to call this
    resource.

    Args:
        logger_name (str):
        level_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SetLevelResponse400 | SetLevelResponse401]
    """

    kwargs = _get_kwargs(
        logger_name=logger_name,
        level_name=level_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    logger_name: str,
    level_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | SetLevelResponse400 | SetLevelResponse401 | None:
    """Set log level

     Set the current log level for a given logger.

    The authenticated user must have <strong>SYS_ADMIN</strong> permission or higher to call this
    resource.

    Args:
        logger_name (str):
        level_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SetLevelResponse400 | SetLevelResponse401
    """

    return sync_detailed(
        logger_name=logger_name,
        level_name=level_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    logger_name: str,
    level_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | SetLevelResponse400 | SetLevelResponse401]:
    """Set log level

     Set the current log level for a given logger.

    The authenticated user must have <strong>SYS_ADMIN</strong> permission or higher to call this
    resource.

    Args:
        logger_name (str):
        level_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SetLevelResponse400 | SetLevelResponse401]
    """

    kwargs = _get_kwargs(
        logger_name=logger_name,
        level_name=level_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    logger_name: str,
    level_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | SetLevelResponse400 | SetLevelResponse401 | None:
    """Set log level

     Set the current log level for a given logger.

    The authenticated user must have <strong>SYS_ADMIN</strong> permission or higher to call this
    resource.

    Args:
        logger_name (str):
        level_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SetLevelResponse400 | SetLevelResponse401
    """

    return (
        await asyncio_detailed(
            logger_name=logger_name,
            level_name=level_name,
            client=client,
        )
    ).parsed
