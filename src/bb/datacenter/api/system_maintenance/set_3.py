from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_user_rate_limit_settings import RestUserRateLimitSettings
from ...models.rest_user_rate_limit_settings_update_request import RestUserRateLimitSettingsUpdateRequest
from ...models.set_3_response_400 import Set3Response400
from ...models.set_3_response_401 import Set3Response401
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_slug: str,
    *,
    body: RestUserRateLimitSettingsUpdateRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/latest/admin/rate-limit/settings/users/{user_slug}".format(
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
) -> RestUserRateLimitSettings | Set3Response400 | Set3Response401 | None:
    if response.status_code == 200:
        response_200 = RestUserRateLimitSettings.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Set3Response400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Set3Response401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RestUserRateLimitSettings | Set3Response400 | Set3Response401]:
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
    body: RestUserRateLimitSettingsUpdateRequest | Unset = UNSET,
) -> Response[RestUserRateLimitSettings | Set3Response400 | Set3Response401]:
    """Set rate limit settings for user

     Sets the given rate limit settings for the given user.

    The authenticated user must have <strong>ADMIN</strong> permission to call this resource.

    Args:
        user_slug (str):
        body (RestUserRateLimitSettingsUpdateRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestUserRateLimitSettings | Set3Response400 | Set3Response401]
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
    body: RestUserRateLimitSettingsUpdateRequest | Unset = UNSET,
) -> RestUserRateLimitSettings | Set3Response400 | Set3Response401 | None:
    """Set rate limit settings for user

     Sets the given rate limit settings for the given user.

    The authenticated user must have <strong>ADMIN</strong> permission to call this resource.

    Args:
        user_slug (str):
        body (RestUserRateLimitSettingsUpdateRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestUserRateLimitSettings | Set3Response400 | Set3Response401
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
    body: RestUserRateLimitSettingsUpdateRequest | Unset = UNSET,
) -> Response[RestUserRateLimitSettings | Set3Response400 | Set3Response401]:
    """Set rate limit settings for user

     Sets the given rate limit settings for the given user.

    The authenticated user must have <strong>ADMIN</strong> permission to call this resource.

    Args:
        user_slug (str):
        body (RestUserRateLimitSettingsUpdateRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestUserRateLimitSettings | Set3Response400 | Set3Response401]
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
    body: RestUserRateLimitSettingsUpdateRequest | Unset = UNSET,
) -> RestUserRateLimitSettings | Set3Response400 | Set3Response401 | None:
    """Set rate limit settings for user

     Sets the given rate limit settings for the given user.

    The authenticated user must have <strong>ADMIN</strong> permission to call this resource.

    Args:
        user_slug (str):
        body (RestUserRateLimitSettingsUpdateRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestUserRateLimitSettings | Set3Response400 | Set3Response401
    """

    return (
        await asyncio_detailed(
            user_slug=user_slug,
            client=client,
            body=body,
        )
    ).parsed
