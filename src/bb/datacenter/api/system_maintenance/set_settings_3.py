from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_rate_limit_settings import RestRateLimitSettings
from ...models.set_settings_3_response_400 import SetSettings3Response400
from ...models.set_settings_3_response_401 import SetSettings3Response401
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RestRateLimitSettings | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/latest/admin/rate-limit/settings",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RestRateLimitSettings | SetSettings3Response400 | SetSettings3Response401 | None:
    if response.status_code == 200:
        response_200 = RestRateLimitSettings.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = SetSettings3Response400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = SetSettings3Response401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RestRateLimitSettings | SetSettings3Response400 | SetSettings3Response401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RestRateLimitSettings | Unset = UNSET,
) -> Response[RestRateLimitSettings | SetSettings3Response400 | SetSettings3Response401]:
    """Set rate limit

     Sets the rate limit settings for the instance.

    The authenticated user must have <strong>ADMIN</strong> permission to call this resource.

    Args:
        body (RestRateLimitSettings | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestRateLimitSettings | SetSettings3Response400 | SetSettings3Response401]
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
    body: RestRateLimitSettings | Unset = UNSET,
) -> RestRateLimitSettings | SetSettings3Response400 | SetSettings3Response401 | None:
    """Set rate limit

     Sets the rate limit settings for the instance.

    The authenticated user must have <strong>ADMIN</strong> permission to call this resource.

    Args:
        body (RestRateLimitSettings | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestRateLimitSettings | SetSettings3Response400 | SetSettings3Response401
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RestRateLimitSettings | Unset = UNSET,
) -> Response[RestRateLimitSettings | SetSettings3Response400 | SetSettings3Response401]:
    """Set rate limit

     Sets the rate limit settings for the instance.

    The authenticated user must have <strong>ADMIN</strong> permission to call this resource.

    Args:
        body (RestRateLimitSettings | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestRateLimitSettings | SetSettings3Response400 | SetSettings3Response401]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RestRateLimitSettings | Unset = UNSET,
) -> RestRateLimitSettings | SetSettings3Response400 | SetSettings3Response401 | None:
    """Set rate limit

     Sets the rate limit settings for the instance.

    The authenticated user must have <strong>ADMIN</strong> permission to call this resource.

    Args:
        body (RestRateLimitSettings | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestRateLimitSettings | SetSettings3Response400 | SetSettings3Response401
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
