from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_group_response_400 import DeleteGroupResponse400
from ...models.delete_group_response_401 import DeleteGroupResponse401
from ...models.delete_group_response_403 import DeleteGroupResponse403
from ...models.delete_group_response_404 import DeleteGroupResponse404
from ...models.delete_group_response_409 import DeleteGroupResponse409
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
        "method": "delete",
        "url": "/api/latest/admin/groups",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteGroupResponse400
    | DeleteGroupResponse401
    | DeleteGroupResponse403
    | DeleteGroupResponse404
    | DeleteGroupResponse409
    | RestDetailedGroup
    | None
):
    if response.status_code == 200:
        response_200 = RestDetailedGroup.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = DeleteGroupResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteGroupResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteGroupResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteGroupResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = DeleteGroupResponse409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteGroupResponse400
    | DeleteGroupResponse401
    | DeleteGroupResponse403
    | DeleteGroupResponse404
    | DeleteGroupResponse409
    | RestDetailedGroup
]:
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
) -> Response[
    DeleteGroupResponse400
    | DeleteGroupResponse401
    | DeleteGroupResponse403
    | DeleteGroupResponse404
    | DeleteGroupResponse409
    | RestDetailedGroup
]:
    """Remove group

     Deletes the specified group, removing them from the system. This also removes any permissions that
    may have been granted to the group.

    A user may not delete the last group that is granting them administrative permissions, or a group
    with greater permissions than themselves.

    The authenticated user must have the <strong>ADMIN</strong> permission to call this resource.

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteGroupResponse400 | DeleteGroupResponse401 | DeleteGroupResponse403 | DeleteGroupResponse404 | DeleteGroupResponse409 | RestDetailedGroup]
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
) -> (
    DeleteGroupResponse400
    | DeleteGroupResponse401
    | DeleteGroupResponse403
    | DeleteGroupResponse404
    | DeleteGroupResponse409
    | RestDetailedGroup
    | None
):
    """Remove group

     Deletes the specified group, removing them from the system. This also removes any permissions that
    may have been granted to the group.

    A user may not delete the last group that is granting them administrative permissions, or a group
    with greater permissions than themselves.

    The authenticated user must have the <strong>ADMIN</strong> permission to call this resource.

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteGroupResponse400 | DeleteGroupResponse401 | DeleteGroupResponse403 | DeleteGroupResponse404 | DeleteGroupResponse409 | RestDetailedGroup
    """

    return sync_detailed(
        client=client,
        name=name,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    name: str,
) -> Response[
    DeleteGroupResponse400
    | DeleteGroupResponse401
    | DeleteGroupResponse403
    | DeleteGroupResponse404
    | DeleteGroupResponse409
    | RestDetailedGroup
]:
    """Remove group

     Deletes the specified group, removing them from the system. This also removes any permissions that
    may have been granted to the group.

    A user may not delete the last group that is granting them administrative permissions, or a group
    with greater permissions than themselves.

    The authenticated user must have the <strong>ADMIN</strong> permission to call this resource.

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteGroupResponse400 | DeleteGroupResponse401 | DeleteGroupResponse403 | DeleteGroupResponse404 | DeleteGroupResponse409 | RestDetailedGroup]
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
) -> (
    DeleteGroupResponse400
    | DeleteGroupResponse401
    | DeleteGroupResponse403
    | DeleteGroupResponse404
    | DeleteGroupResponse409
    | RestDetailedGroup
    | None
):
    """Remove group

     Deletes the specified group, removing them from the system. This also removes any permissions that
    may have been granted to the group.

    A user may not delete the last group that is granting them administrative permissions, or a group
    with greater permissions than themselves.

    The authenticated user must have the <strong>ADMIN</strong> permission to call this resource.

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteGroupResponse400 | DeleteGroupResponse401 | DeleteGroupResponse403 | DeleteGroupResponse404 | DeleteGroupResponse409 | RestDetailedGroup
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
        )
    ).parsed
