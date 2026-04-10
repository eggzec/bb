from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_groups_with_any_permission_response_200 import GetGroupsWithAnyPermissionResponse200
from ...models.get_groups_with_any_permission_response_401 import GetGroupsWithAnyPermissionResponse401
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
        "url": "/api/latest/admin/permissions/groups",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetGroupsWithAnyPermissionResponse200 | GetGroupsWithAnyPermissionResponse401 | None:
    if response.status_code == 200:
        response_200 = GetGroupsWithAnyPermissionResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetGroupsWithAnyPermissionResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetGroupsWithAnyPermissionResponse200 | GetGroupsWithAnyPermissionResponse401]:
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
) -> Response[GetGroupsWithAnyPermissionResponse200 | GetGroupsWithAnyPermissionResponse401]:
    """Get groups with a global permission

     Retrieve a page of groups that have been granted at least one global permission.


    The authenticated user must have <strong>ADMIN</strong> permission or higher to call this resource.

    Args:
        filter_ (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGroupsWithAnyPermissionResponse200 | GetGroupsWithAnyPermissionResponse401]
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
) -> GetGroupsWithAnyPermissionResponse200 | GetGroupsWithAnyPermissionResponse401 | None:
    """Get groups with a global permission

     Retrieve a page of groups that have been granted at least one global permission.


    The authenticated user must have <strong>ADMIN</strong> permission or higher to call this resource.

    Args:
        filter_ (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGroupsWithAnyPermissionResponse200 | GetGroupsWithAnyPermissionResponse401
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
) -> Response[GetGroupsWithAnyPermissionResponse200 | GetGroupsWithAnyPermissionResponse401]:
    """Get groups with a global permission

     Retrieve a page of groups that have been granted at least one global permission.


    The authenticated user must have <strong>ADMIN</strong> permission or higher to call this resource.

    Args:
        filter_ (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGroupsWithAnyPermissionResponse200 | GetGroupsWithAnyPermissionResponse401]
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
) -> GetGroupsWithAnyPermissionResponse200 | GetGroupsWithAnyPermissionResponse401 | None:
    """Get groups with a global permission

     Retrieve a page of groups that have been granted at least one global permission.


    The authenticated user must have <strong>ADMIN</strong> permission or higher to call this resource.

    Args:
        filter_ (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGroupsWithAnyPermissionResponse200 | GetGroupsWithAnyPermissionResponse401
    """

    return (
        await asyncio_detailed(
            client=client,
            filter_=filter_,
            start=start,
            limit=limit,
        )
    ).parsed
