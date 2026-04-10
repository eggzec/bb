from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_bulk_user_rate_limit_settings_update_request import RestBulkUserRateLimitSettingsUpdateRequest
from ...models.rest_user_rate_limit_settings import RestUserRateLimitSettings
from ...models.set_2_response_400 import Set2Response400
from ...models.set_2_response_401 import Set2Response401
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RestBulkUserRateLimitSettingsUpdateRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/latest/admin/rate-limit/settings/users",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RestUserRateLimitSettings | Set2Response400 | Set2Response401 | None:
    if response.status_code == 200:
        response_200 = RestUserRateLimitSettings.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Set2Response400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Set2Response401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RestUserRateLimitSettings | Set2Response400 | Set2Response401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RestBulkUserRateLimitSettingsUpdateRequest | Unset = UNSET,
) -> Response[RestUserRateLimitSettings | Set2Response400 | Set2Response401]:
    """Set rate limit settings for users

     Sets the given rate limit settings for the given users.

    The authenticated user must have <strong>ADMIN</strong> permission to call this resource.

    Args:
        body (RestBulkUserRateLimitSettingsUpdateRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestUserRateLimitSettings | Set2Response400 | Set2Response401]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: RestBulkUserRateLimitSettingsUpdateRequest | Unset = UNSET,
) -> RestUserRateLimitSettings | Set2Response400 | Set2Response401 | None:
    """Set rate limit settings for users

     Sets the given rate limit settings for the given users.

    The authenticated user must have <strong>ADMIN</strong> permission to call this resource.

    Args:
        body (RestBulkUserRateLimitSettingsUpdateRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestUserRateLimitSettings | Set2Response400 | Set2Response401
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RestBulkUserRateLimitSettingsUpdateRequest | Unset = UNSET,
) -> Response[RestUserRateLimitSettings | Set2Response400 | Set2Response401]:
    """Set rate limit settings for users

     Sets the given rate limit settings for the given users.

    The authenticated user must have <strong>ADMIN</strong> permission to call this resource.

    Args:
        body (RestBulkUserRateLimitSettingsUpdateRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestUserRateLimitSettings | Set2Response400 | Set2Response401]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RestBulkUserRateLimitSettingsUpdateRequest | Unset = UNSET,
) -> RestUserRateLimitSettings | Set2Response400 | Set2Response401 | None:
    """Set rate limit settings for users

     Sets the given rate limit settings for the given users.

    The authenticated user must have <strong>ADMIN</strong> permission to call this resource.

    Args:
        body (RestBulkUserRateLimitSettingsUpdateRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestUserRateLimitSettings | Set2Response400 | Set2Response401
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
