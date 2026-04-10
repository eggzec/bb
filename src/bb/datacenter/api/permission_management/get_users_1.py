from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_users_1_response_200 import GetUsers1Response200
from ...models.get_users_1_response_401 import GetUsers1Response401
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    filter_: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["filter"] = filter_

    params["start"] = start

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/admin/users",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetUsers1Response200 | GetUsers1Response401 | None:
    if response.status_code == 200:
        response_200 = GetUsers1Response200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetUsers1Response401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetUsers1Response200 | GetUsers1Response401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    filter_: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GetUsers1Response200 | GetUsers1Response401]:
    """Get users

     Retrieve a page of users.

     The authenticated user must have the <strong>LICENSED_USER</strong> permission to call this
    resource.

    Args:
        filter_ (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUsers1Response200 | GetUsers1Response401]
    """

    kwargs = _get_kwargs(
        filter_=filter_,
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
    filter_: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetUsers1Response200 | GetUsers1Response401 | None:
    """Get users

     Retrieve a page of users.

     The authenticated user must have the <strong>LICENSED_USER</strong> permission to call this
    resource.

    Args:
        filter_ (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUsers1Response200 | GetUsers1Response401
    """

    return sync_detailed(
        client=client,
        filter_=filter_,
        start=start,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    filter_: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GetUsers1Response200 | GetUsers1Response401]:
    """Get users

     Retrieve a page of users.

     The authenticated user must have the <strong>LICENSED_USER</strong> permission to call this
    resource.

    Args:
        filter_ (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUsers1Response200 | GetUsers1Response401]
    """

    kwargs = _get_kwargs(
        filter_=filter_,
        start=start,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    filter_: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetUsers1Response200 | GetUsers1Response401 | None:
    """Get users

     Retrieve a page of users.

     The authenticated user must have the <strong>LICENSED_USER</strong> permission to call this
    resource.

    Args:
        filter_ (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUsers1Response200 | GetUsers1Response401
    """

    return (
        await asyncio_detailed(
            client=client,
            filter_=filter_,
            start=start,
            limit=limit,
        )
    ).parsed
