from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_group_response_400 import CreateGroupResponse400
from ...models.create_group_response_401 import CreateGroupResponse401
from ...models.create_group_response_409 import CreateGroupResponse409
from ...models.rest_detailed_group import RestDetailedGroup
from ...types import UNSET, Response


def _get_kwargs(
    *,
    name: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["name"] = name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/latest/admin/groups",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateGroupResponse400 | CreateGroupResponse401 | CreateGroupResponse409 | RestDetailedGroup | None:
    if response.status_code == 200:
        response_200 = RestDetailedGroup.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CreateGroupResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = CreateGroupResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 409:
        response_409 = CreateGroupResponse409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateGroupResponse400 | CreateGroupResponse401 | CreateGroupResponse409 | RestDetailedGroup]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    name: str,
) -> Response[CreateGroupResponse400 | CreateGroupResponse401 | CreateGroupResponse409 | RestDetailedGroup]:
    """Create group

     Create a new group.

    The authenticated user must have <strong>ADMIN</strong> permission or higher to call this resource.

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateGroupResponse400 | CreateGroupResponse401 | CreateGroupResponse409 | RestDetailedGroup]
    """

    kwargs = _get_kwargs(
        name=name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    name: str,
) -> CreateGroupResponse400 | CreateGroupResponse401 | CreateGroupResponse409 | RestDetailedGroup | None:
    """Create group

     Create a new group.

    The authenticated user must have <strong>ADMIN</strong> permission or higher to call this resource.

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateGroupResponse400 | CreateGroupResponse401 | CreateGroupResponse409 | RestDetailedGroup
    """

    return sync_detailed(
        client=client,
        name=name,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    name: str,
) -> Response[CreateGroupResponse400 | CreateGroupResponse401 | CreateGroupResponse409 | RestDetailedGroup]:
    """Create group

     Create a new group.

    The authenticated user must have <strong>ADMIN</strong> permission or higher to call this resource.

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateGroupResponse400 | CreateGroupResponse401 | CreateGroupResponse409 | RestDetailedGroup]
    """

    kwargs = _get_kwargs(
        name=name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    name: str,
) -> CreateGroupResponse400 | CreateGroupResponse401 | CreateGroupResponse409 | RestDetailedGroup | None:
    """Create group

     Create a new group.

    The authenticated user must have <strong>ADMIN</strong> permission or higher to call this resource.

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateGroupResponse400 | CreateGroupResponse401 | CreateGroupResponse409 | RestDetailedGroup
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
        )
    ).parsed
