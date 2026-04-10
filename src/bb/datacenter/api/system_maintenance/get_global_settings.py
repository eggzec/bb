from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_global_settings_response_401 import GetGlobalSettingsResponse401
from ...models.rest_ssh_key_settings import RestSshKeySettings
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/admin",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetGlobalSettingsResponse401 | RestSshKeySettings | None:
    if response.status_code == 200:
        response_200 = RestSshKeySettings.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetGlobalSettingsResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetGlobalSettingsResponse401 | RestSshKeySettings]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetGlobalSettingsResponse401 | RestSshKeySettings]:
    """Get global SSH key settings

     Gets the global settings that enforce the maximum expiry of SSH keys and restrictions on SSH key
    types.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGlobalSettingsResponse401 | RestSshKeySettings]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> GetGlobalSettingsResponse401 | RestSshKeySettings | None:
    """Get global SSH key settings

     Gets the global settings that enforce the maximum expiry of SSH keys and restrictions on SSH key
    types.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGlobalSettingsResponse401 | RestSshKeySettings
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetGlobalSettingsResponse401 | RestSshKeySettings]:
    """Get global SSH key settings

     Gets the global settings that enforce the maximum expiry of SSH keys and restrictions on SSH key
    types.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGlobalSettingsResponse401 | RestSshKeySettings]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> GetGlobalSettingsResponse401 | RestSshKeySettings | None:
    """Get global SSH key settings

     Gets the global settings that enforce the maximum expiry of SSH keys and restrictions on SSH key
    types.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGlobalSettingsResponse401 | RestSshKeySettings
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
