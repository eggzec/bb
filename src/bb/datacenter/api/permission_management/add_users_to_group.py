from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_users_to_group_response_401 import AddUsersToGroupResponse401
from ...models.add_users_to_group_response_403 import AddUsersToGroupResponse403
from ...models.add_users_to_group_response_404 import AddUsersToGroupResponse404
from ...models.group_and_users import GroupAndUsers
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: GroupAndUsers | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/latest/admin/groups/add-users",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AddUsersToGroupResponse401 | AddUsersToGroupResponse403 | AddUsersToGroupResponse404 | Any | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 401:
        response_401 = AddUsersToGroupResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = AddUsersToGroupResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = AddUsersToGroupResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AddUsersToGroupResponse401 | AddUsersToGroupResponse403 | AddUsersToGroupResponse404 | Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GroupAndUsers | Unset = UNSET,
) -> Response[AddUsersToGroupResponse401 | AddUsersToGroupResponse403 | AddUsersToGroupResponse404 | Any]:
    """Add multiple users to group

     Add multiple users to a group.

    The authenticated user must have the <strong>ADMIN</strong> permission to call this resource.

    Args:
        body (GroupAndUsers | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddUsersToGroupResponse401 | AddUsersToGroupResponse403 | AddUsersToGroupResponse404 | Any]
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
    body: GroupAndUsers | Unset = UNSET,
) -> AddUsersToGroupResponse401 | AddUsersToGroupResponse403 | AddUsersToGroupResponse404 | Any | None:
    """Add multiple users to group

     Add multiple users to a group.

    The authenticated user must have the <strong>ADMIN</strong> permission to call this resource.

    Args:
        body (GroupAndUsers | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddUsersToGroupResponse401 | AddUsersToGroupResponse403 | AddUsersToGroupResponse404 | Any
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GroupAndUsers | Unset = UNSET,
) -> Response[AddUsersToGroupResponse401 | AddUsersToGroupResponse403 | AddUsersToGroupResponse404 | Any]:
    """Add multiple users to group

     Add multiple users to a group.

    The authenticated user must have the <strong>ADMIN</strong> permission to call this resource.

    Args:
        body (GroupAndUsers | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddUsersToGroupResponse401 | AddUsersToGroupResponse403 | AddUsersToGroupResponse404 | Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: GroupAndUsers | Unset = UNSET,
) -> AddUsersToGroupResponse401 | AddUsersToGroupResponse403 | AddUsersToGroupResponse404 | Any | None:
    """Add multiple users to group

     Add multiple users to a group.

    The authenticated user must have the <strong>ADMIN</strong> permission to call this resource.

    Args:
        body (GroupAndUsers | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddUsersToGroupResponse401 | AddUsersToGroupResponse403 | AddUsersToGroupResponse404 | Any
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
