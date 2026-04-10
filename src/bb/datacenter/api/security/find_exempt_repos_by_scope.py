from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.find_exempt_repos_by_scope_order import FindExemptReposByScopeOrder
from ...models.find_exempt_repos_by_scope_response_200 import FindExemptReposByScopeResponse200
from ...models.find_exempt_repos_by_scope_response_401 import FindExemptReposByScopeResponse401
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    order: FindExemptReposByScopeOrder | Unset = UNSET,
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
        "url": "/api/latest/secret-scanning/exempt",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FindExemptReposByScopeResponse200 | FindExemptReposByScopeResponse401 | None:
    if response.status_code == 200:
        response_200 = FindExemptReposByScopeResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = FindExemptReposByScopeResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FindExemptReposByScopeResponse200 | FindExemptReposByScopeResponse401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    order: FindExemptReposByScopeOrder | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[FindExemptReposByScopeResponse200 | FindExemptReposByScopeResponse401]:
    """Find all repos exempt from secret scan

     Find all repositories exempt from secret scanning

    Args:
        order (FindExemptReposByScopeOrder | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FindExemptReposByScopeResponse200 | FindExemptReposByScopeResponse401]
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
    order: FindExemptReposByScopeOrder | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> FindExemptReposByScopeResponse200 | FindExemptReposByScopeResponse401 | None:
    """Find all repos exempt from secret scan

     Find all repositories exempt from secret scanning

    Args:
        order (FindExemptReposByScopeOrder | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FindExemptReposByScopeResponse200 | FindExemptReposByScopeResponse401
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
    order: FindExemptReposByScopeOrder | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[FindExemptReposByScopeResponse200 | FindExemptReposByScopeResponse401]:
    """Find all repos exempt from secret scan

     Find all repositories exempt from secret scanning

    Args:
        order (FindExemptReposByScopeOrder | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FindExemptReposByScopeResponse200 | FindExemptReposByScopeResponse401]
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
    order: FindExemptReposByScopeOrder | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> FindExemptReposByScopeResponse200 | FindExemptReposByScopeResponse401 | None:
    """Find all repos exempt from secret scan

     Find all repositories exempt from secret scanning

    Args:
        order (FindExemptReposByScopeOrder | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FindExemptReposByScopeResponse200 | FindExemptReposByScopeResponse401
    """

    return (
        await asyncio_detailed(
            client=client,
            order=order,
            start=start,
            limit=limit,
        )
    ).parsed
