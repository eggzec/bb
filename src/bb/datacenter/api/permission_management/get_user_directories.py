from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_user_directories_response_401 import GetUserDirectoriesResponse401
from ...models.rest_user_directory import RestUserDirectory
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include_inactive: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["includeInactive"] = include_inactive

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/admin/user-directories",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetUserDirectoriesResponse401 | RestUserDirectory | None:
    if response.status_code == 200:
        response_200 = RestUserDirectory.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetUserDirectoriesResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetUserDirectoriesResponse401 | RestUserDirectory]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    include_inactive: str | Unset = UNSET,
) -> Response[GetUserDirectoriesResponse401 | RestUserDirectory]:
    """Get directories

     Retrieve a list of active directories.

     The authenticated user must have the <strong>ADMIN</strong> permission to call this resource.

    Args:
        include_inactive (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUserDirectoriesResponse401 | RestUserDirectory]
    """

    kwargs = _get_kwargs(
        include_inactive=include_inactive,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    include_inactive: str | Unset = UNSET,
) -> GetUserDirectoriesResponse401 | RestUserDirectory | None:
    """Get directories

     Retrieve a list of active directories.

     The authenticated user must have the <strong>ADMIN</strong> permission to call this resource.

    Args:
        include_inactive (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUserDirectoriesResponse401 | RestUserDirectory
    """

    return sync_detailed(
        client=client,
        include_inactive=include_inactive,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    include_inactive: str | Unset = UNSET,
) -> Response[GetUserDirectoriesResponse401 | RestUserDirectory]:
    """Get directories

     Retrieve a list of active directories.

     The authenticated user must have the <strong>ADMIN</strong> permission to call this resource.

    Args:
        include_inactive (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUserDirectoriesResponse401 | RestUserDirectory]
    """

    kwargs = _get_kwargs(
        include_inactive=include_inactive,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    include_inactive: str | Unset = UNSET,
) -> GetUserDirectoriesResponse401 | RestUserDirectory | None:
    """Get directories

     Retrieve a list of active directories.

     The authenticated user must have the <strong>ADMIN</strong> permission to call this resource.

    Args:
        include_inactive (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUserDirectoriesResponse401 | RestUserDirectory
    """

    return (
        await asyncio_detailed(
            client=client,
            include_inactive=include_inactive,
        )
    ).parsed
