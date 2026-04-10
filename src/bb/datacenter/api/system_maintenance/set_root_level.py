from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.set_root_level_response_400 import SetRootLevelResponse400
from ...models.set_root_level_response_401 import SetRootLevelResponse401
from ...types import Response


def _get_kwargs(
    level_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/latest/logs/rootLogger/{level_name}".format(
            level_name=quote(str(level_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | SetRootLevelResponse400 | SetRootLevelResponse401 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = SetRootLevelResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = SetRootLevelResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | SetRootLevelResponse400 | SetRootLevelResponse401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    level_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | SetRootLevelResponse400 | SetRootLevelResponse401]:
    """Set root log level

     Set the current log level for the root logger.

    The authenticated user must have <strong>SYS_ADMIN</strong> permission or higher to call this
    resource.

    Args:
        level_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SetRootLevelResponse400 | SetRootLevelResponse401]
    """

    kwargs = _get_kwargs(
        level_name=level_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    level_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | SetRootLevelResponse400 | SetRootLevelResponse401 | None:
    """Set root log level

     Set the current log level for the root logger.

    The authenticated user must have <strong>SYS_ADMIN</strong> permission or higher to call this
    resource.

    Args:
        level_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SetRootLevelResponse400 | SetRootLevelResponse401
    """

    return sync_detailed(
        level_name=level_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    level_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | SetRootLevelResponse400 | SetRootLevelResponse401]:
    """Set root log level

     Set the current log level for the root logger.

    The authenticated user must have <strong>SYS_ADMIN</strong> permission or higher to call this
    resource.

    Args:
        level_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SetRootLevelResponse400 | SetRootLevelResponse401]
    """

    kwargs = _get_kwargs(
        level_name=level_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    level_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | SetRootLevelResponse400 | SetRootLevelResponse401 | None:
    """Set root log level

     Set the current log level for the root logger.

    The authenticated user must have <strong>SYS_ADMIN</strong> permission or higher to call this
    resource.

    Args:
        level_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SetRootLevelResponse400 | SetRootLevelResponse401
    """

    return (
        await asyncio_detailed(
            level_name=level_name,
            client=client,
        )
    ).parsed
