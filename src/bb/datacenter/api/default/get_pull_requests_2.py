from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    role: str | Unset = "reviewer",
    limit: int | Unset = 25,
    start: int | Unset = 0,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["role"] = role

    params["limit"] = limit

    params["start"] = start

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/inbox/pull-requests",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any:
    return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    role: str | Unset = "reviewer",
    limit: int | Unset = 25,
    start: int | Unset = 0,
) -> Response[Any]:
    """Get pull requests in inbox

     Returns a page of pull requests in the user's inbox.

    Args:
        role (str | Unset):  Default: 'reviewer'.
        limit (int | Unset):  Default: 25.
        start (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        role=role,
        limit=limit,
        start=start,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    role: str | Unset = "reviewer",
    limit: int | Unset = 25,
    start: int | Unset = 0,
) -> Response[Any]:
    """Get pull requests in inbox

     Returns a page of pull requests in the user's inbox.

    Args:
        role (str | Unset):  Default: 'reviewer'.
        limit (int | Unset):  Default: 25.
        start (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        role=role,
        limit=limit,
        start=start,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
