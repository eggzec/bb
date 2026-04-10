from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.example_settings_map import ExampleSettingsMap
from ...models.get_user_settings_response_401 import GetUserSettingsResponse401
from ...models.get_user_settings_response_404 import GetUserSettingsResponse404
from ...types import Response


def _get_kwargs(
    user_slug: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/users/{user_slug}/settings".format(
            user_slug=quote(str(user_slug), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ExampleSettingsMap | GetUserSettingsResponse401 | GetUserSettingsResponse404 | None:
    if response.status_code == 200:
        response_200 = ExampleSettingsMap.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetUserSettingsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetUserSettingsResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ExampleSettingsMap | GetUserSettingsResponse401 | GetUserSettingsResponse404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_slug: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ExampleSettingsMap | GetUserSettingsResponse401 | GetUserSettingsResponse404]:
    """Get user settings

     Retrieve a map of user setting key values for a specific user identified by the user slug.

    Args:
        user_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExampleSettingsMap | GetUserSettingsResponse401 | GetUserSettingsResponse404]
    """

    kwargs = _get_kwargs(
        user_slug=user_slug,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_slug: str,
    *,
    client: AuthenticatedClient | Client,
) -> ExampleSettingsMap | GetUserSettingsResponse401 | GetUserSettingsResponse404 | None:
    """Get user settings

     Retrieve a map of user setting key values for a specific user identified by the user slug.

    Args:
        user_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExampleSettingsMap | GetUserSettingsResponse401 | GetUserSettingsResponse404
    """

    return sync_detailed(
        user_slug=user_slug,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_slug: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ExampleSettingsMap | GetUserSettingsResponse401 | GetUserSettingsResponse404]:
    """Get user settings

     Retrieve a map of user setting key values for a specific user identified by the user slug.

    Args:
        user_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExampleSettingsMap | GetUserSettingsResponse401 | GetUserSettingsResponse404]
    """

    kwargs = _get_kwargs(
        user_slug=user_slug,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_slug: str,
    *,
    client: AuthenticatedClient | Client,
) -> ExampleSettingsMap | GetUserSettingsResponse401 | GetUserSettingsResponse404 | None:
    """Get user settings

     Retrieve a map of user setting key values for a specific user identified by the user slug.

    Args:
        user_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExampleSettingsMap | GetUserSettingsResponse401 | GetUserSettingsResponse404
    """

    return (
        await asyncio_detailed(
            user_slug=user_slug,
            client=client,
        )
    ).parsed
