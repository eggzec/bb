from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.example_settings_map import ExampleSettingsMap
from ...models.update_settings_response_401 import UpdateSettingsResponse401
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_slug: str,
    *,
    body: ExampleSettingsMap | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/latest/users/{user_slug}/settings".format(
            user_slug=quote(str(user_slug), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | UpdateSettingsResponse401 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = UpdateSettingsResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | UpdateSettingsResponse401]:
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
    body: ExampleSettingsMap | Unset = UNSET,
) -> Response[Any | UpdateSettingsResponse401]:
    """Update user settings

     Update the entries of a map of user setting key/values for a specific user identified by the user
    slug.

    Args:
        user_slug (str):
        body (ExampleSettingsMap | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | UpdateSettingsResponse401]
    """

    kwargs = _get_kwargs(
        user_slug=user_slug,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExampleSettingsMap | Unset = UNSET,
) -> Any | UpdateSettingsResponse401 | None:
    """Update user settings

     Update the entries of a map of user setting key/values for a specific user identified by the user
    slug.

    Args:
        user_slug (str):
        body (ExampleSettingsMap | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | UpdateSettingsResponse401
    """

    return sync_detailed(
        user_slug=user_slug,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    user_slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExampleSettingsMap | Unset = UNSET,
) -> Response[Any | UpdateSettingsResponse401]:
    """Update user settings

     Update the entries of a map of user setting key/values for a specific user identified by the user
    slug.

    Args:
        user_slug (str):
        body (ExampleSettingsMap | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | UpdateSettingsResponse401]
    """

    kwargs = _get_kwargs(
        user_slug=user_slug,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExampleSettingsMap | Unset = UNSET,
) -> Any | UpdateSettingsResponse401 | None:
    """Update user settings

     Update the entries of a map of user setting key/values for a specific user identified by the user
    slug.

    Args:
        user_slug (str):
        body (ExampleSettingsMap | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | UpdateSettingsResponse401
    """

    return (
        await asyncio_detailed(
            user_slug=user_slug,
            client=client,
            body=body,
        )
    ).parsed
