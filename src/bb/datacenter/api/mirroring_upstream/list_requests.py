from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_requests_response_200 import ListRequestsResponse200
from ...models.list_requests_state import ListRequestsState
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    state: ListRequestsState | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_state: str | Unset = UNSET
    if not isinstance(state, Unset):
        json_state = state.value

    params["state"] = json_state

    params["start"] = start

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/mirroring/latest/requests",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListRequestsResponse200 | None:
    if response.status_code == 200:
        response_200 = ListRequestsResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ListRequestsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    state: ListRequestsState | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[ListRequestsResponse200]:
    """Get mirroring requests

     Retrieves a mirroring request

    Args:
        state (ListRequestsState | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListRequestsResponse200]
    """

    kwargs = _get_kwargs(
        state=state,
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
    state: ListRequestsState | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> ListRequestsResponse200 | None:
    """Get mirroring requests

     Retrieves a mirroring request

    Args:
        state (ListRequestsState | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListRequestsResponse200
    """

    return sync_detailed(
        client=client,
        state=state,
        start=start,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    state: ListRequestsState | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[ListRequestsResponse200]:
    """Get mirroring requests

     Retrieves a mirroring request

    Args:
        state (ListRequestsState | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListRequestsResponse200]
    """

    kwargs = _get_kwargs(
        state=state,
        start=start,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    state: ListRequestsState | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> ListRequestsResponse200 | None:
    """Get mirroring requests

     Retrieves a mirroring request

    Args:
        state (ListRequestsState | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListRequestsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            state=state,
            start=start,
            limit=limit,
        )
    ).parsed
