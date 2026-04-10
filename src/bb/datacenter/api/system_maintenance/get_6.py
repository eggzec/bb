from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_6_response_401 import Get6Response401
from ...models.get_6_response_404 import Get6Response404
from ...models.rest_user_rate_limit_settings import RestUserRateLimitSettings
from ...types import Response


def _get_kwargs(
    user_slug: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/admin/rate-limit/settings/users/{user_slug}".format(
            user_slug=quote(str(user_slug), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Get6Response401 | Get6Response404 | RestUserRateLimitSettings | None:
    if response.status_code == 200:
        response_200 = RestUserRateLimitSettings.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Get6Response401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = Get6Response404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Get6Response401 | Get6Response404 | RestUserRateLimitSettings]:
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
) -> Response[Get6Response401 | Get6Response404 | RestUserRateLimitSettings]:
    """Get user specific rate limit settings

     Retrieves the user-specific rate limit settings for the given user.

    To call this resource, the user must be authenticated and either have <strong>ADMIN</strong>
    permission or be the same user as the one whose settings are requested. A user with
    <strong>ADMIN</strong> permission cannot get the settings of a user with <strong>SYS_ADMIN</strong>
    permission.

    Args:
        user_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Get6Response401 | Get6Response404 | RestUserRateLimitSettings]
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
) -> Get6Response401 | Get6Response404 | RestUserRateLimitSettings | None:
    """Get user specific rate limit settings

     Retrieves the user-specific rate limit settings for the given user.

    To call this resource, the user must be authenticated and either have <strong>ADMIN</strong>
    permission or be the same user as the one whose settings are requested. A user with
    <strong>ADMIN</strong> permission cannot get the settings of a user with <strong>SYS_ADMIN</strong>
    permission.

    Args:
        user_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Get6Response401 | Get6Response404 | RestUserRateLimitSettings
    """

    return sync_detailed(
        user_slug=user_slug,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_slug: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Get6Response401 | Get6Response404 | RestUserRateLimitSettings]:
    """Get user specific rate limit settings

     Retrieves the user-specific rate limit settings for the given user.

    To call this resource, the user must be authenticated and either have <strong>ADMIN</strong>
    permission or be the same user as the one whose settings are requested. A user with
    <strong>ADMIN</strong> permission cannot get the settings of a user with <strong>SYS_ADMIN</strong>
    permission.

    Args:
        user_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Get6Response401 | Get6Response404 | RestUserRateLimitSettings]
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
) -> Get6Response401 | Get6Response404 | RestUserRateLimitSettings | None:
    """Get user specific rate limit settings

     Retrieves the user-specific rate limit settings for the given user.

    To call this resource, the user must be authenticated and either have <strong>ADMIN</strong>
    permission or be the same user as the one whose settings are requested. A user with
    <strong>ADMIN</strong> permission cannot get the settings of a user with <strong>SYS_ADMIN</strong>
    permission.

    Args:
        user_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Get6Response401 | Get6Response404 | RestUserRateLimitSettings
    """

    return (
        await asyncio_detailed(
            user_slug=user_slug,
            client=client,
        )
    ).parsed
