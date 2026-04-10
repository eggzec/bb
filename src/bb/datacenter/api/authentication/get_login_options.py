from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_login_options_response_200 import GetLoginOptionsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["start"] = start

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/authconfig/latest/login-options",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetLoginOptionsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetLoginOptionsResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetLoginOptionsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GetLoginOptionsResponse200]:
    """Get available login options

     Returns a list of available login options, which contains details about the metadata required for
    the login page.

    Only enabled login options will be returned. Login options can either be the native login form or
    the configured IdPs.

    Args:
        start (float | Unset):
        limit (float | Unset):  Example: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetLoginOptionsResponse200]
    """

    kwargs = _get_kwargs(
        start=start,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetLoginOptionsResponse200 | None:
    """Get available login options

     Returns a list of available login options, which contains details about the metadata required for
    the login page.

    Only enabled login options will be returned. Login options can either be the native login form or
    the configured IdPs.

    Args:
        start (float | Unset):
        limit (float | Unset):  Example: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetLoginOptionsResponse200
    """

    return sync_detailed(
        client=client,
        start=start,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GetLoginOptionsResponse200]:
    """Get available login options

     Returns a list of available login options, which contains details about the metadata required for
    the login page.

    Only enabled login options will be returned. Login options can either be the native login form or
    the configured IdPs.

    Args:
        start (float | Unset):
        limit (float | Unset):  Example: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetLoginOptionsResponse200]
    """

    kwargs = _get_kwargs(
        start=start,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetLoginOptionsResponse200 | None:
    """Get available login options

     Returns a list of available login options, which contains details about the metadata required for
    the login page.

    Only enabled login options will be returned. Login options can either be the native login form or
    the configured IdPs.

    Args:
        start (float | Unset):
        limit (float | Unset):  Example: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetLoginOptionsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            start=start,
            limit=limit,
        )
    ).parsed
