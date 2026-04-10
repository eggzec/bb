from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_history_order import GetHistoryOrder
from ...models.get_history_response_200 import GetHistoryResponse200
from ...models.get_history_response_400 import GetHistoryResponse400
from ...models.get_history_response_401 import GetHistoryResponse401
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    order: GetHistoryOrder | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_order: str | Unset = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params["start"] = start

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/admin/rate-limit/history",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetHistoryResponse200 | GetHistoryResponse400 | GetHistoryResponse401 | None:
    if response.status_code == 200:
        response_200 = GetHistoryResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetHistoryResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetHistoryResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetHistoryResponse200 | GetHistoryResponse400 | GetHistoryResponse401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    order: GetHistoryOrder | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GetHistoryResponse200 | GetHistoryResponse400 | GetHistoryResponse401]:
    """Get rate limit history

     Retrieves the recent rate limit history for the instance.

    The authenticated user must have the <strong>ADMIN</strong> permission to call this resource.

    Args:
        order (GetHistoryOrder | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetHistoryResponse200 | GetHistoryResponse400 | GetHistoryResponse401]
    """

    kwargs = _get_kwargs(
        order=order,
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
    order: GetHistoryOrder | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetHistoryResponse200 | GetHistoryResponse400 | GetHistoryResponse401 | None:
    """Get rate limit history

     Retrieves the recent rate limit history for the instance.

    The authenticated user must have the <strong>ADMIN</strong> permission to call this resource.

    Args:
        order (GetHistoryOrder | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetHistoryResponse200 | GetHistoryResponse400 | GetHistoryResponse401
    """

    return sync_detailed(
        client=client,
        order=order,
        start=start,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    order: GetHistoryOrder | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GetHistoryResponse200 | GetHistoryResponse400 | GetHistoryResponse401]:
    """Get rate limit history

     Retrieves the recent rate limit history for the instance.

    The authenticated user must have the <strong>ADMIN</strong> permission to call this resource.

    Args:
        order (GetHistoryOrder | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetHistoryResponse200 | GetHistoryResponse400 | GetHistoryResponse401]
    """

    kwargs = _get_kwargs(
        order=order,
        start=start,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    order: GetHistoryOrder | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetHistoryResponse200 | GetHistoryResponse400 | GetHistoryResponse401 | None:
    """Get rate limit history

     Retrieves the recent rate limit history for the instance.

    The authenticated user must have the <strong>ADMIN</strong> permission to call this resource.

    Args:
        order (GetHistoryOrder | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetHistoryResponse200 | GetHistoryResponse400 | GetHistoryResponse401
    """

    return (
        await asyncio_detailed(
            client=client,
            order=order,
            start=start,
            limit=limit,
        )
    ).parsed
