from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_idps_response_200 import GetIdpsResponse200
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
        "url": "/authconfig/latest/idps",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetIdpsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetIdpsResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetIdpsResponse200]:
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
) -> Response[GetIdpsResponse200]:
    """Get all configured IdPs

     Returns a page of configured IdPs.

    This endpoint makes no guarantees to ordering besides the ordering being consistent.

    Args:
        start (float | Unset):
        limit (float | Unset):  Example: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetIdpsResponse200]
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
) -> GetIdpsResponse200 | None:
    """Get all configured IdPs

     Returns a page of configured IdPs.

    This endpoint makes no guarantees to ordering besides the ordering being consistent.

    Args:
        start (float | Unset):
        limit (float | Unset):  Example: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetIdpsResponse200
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
) -> Response[GetIdpsResponse200]:
    """Get all configured IdPs

     Returns a page of configured IdPs.

    This endpoint makes no guarantees to ordering besides the ordering being consistent.

    Args:
        start (float | Unset):
        limit (float | Unset):  Example: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetIdpsResponse200]
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
) -> GetIdpsResponse200 | None:
    """Get all configured IdPs

     Returns a page of configured IdPs.

    This endpoint makes no guarantees to ordering besides the ordering being consistent.

    Args:
        start (float | Unset):
        limit (float | Unset):  Example: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetIdpsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            start=start,
            limit=limit,
        )
    ).parsed
