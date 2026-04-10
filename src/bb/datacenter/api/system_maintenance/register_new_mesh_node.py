from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.register_new_mesh_node_response_400 import RegisterNewMeshNodeResponse400
from ...models.register_new_mesh_node_response_401 import RegisterNewMeshNodeResponse401
from ...models.rest_mesh_node import RestMeshNode
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RestMeshNode | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/latest/admin/git/mesh/nodes",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RegisterNewMeshNodeResponse400 | RegisterNewMeshNodeResponse401 | RestMeshNode | None:
    if response.status_code == 200:
        response_200 = RestMeshNode.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = RegisterNewMeshNodeResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = RegisterNewMeshNodeResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RegisterNewMeshNodeResponse400 | RegisterNewMeshNodeResponse401 | RestMeshNode]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RestMeshNode | Unset = UNSET,
) -> Response[RegisterNewMeshNodeResponse400 | RegisterNewMeshNodeResponse401 | RestMeshNode]:
    """Register new Mesh node

     Register a new Mesh node.

    The authenticated user must have **SYS_ADMIN** permission.

    Args:
        body (RestMeshNode | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RegisterNewMeshNodeResponse400 | RegisterNewMeshNodeResponse401 | RestMeshNode]
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
    body: RestMeshNode | Unset = UNSET,
) -> RegisterNewMeshNodeResponse400 | RegisterNewMeshNodeResponse401 | RestMeshNode | None:
    """Register new Mesh node

     Register a new Mesh node.

    The authenticated user must have **SYS_ADMIN** permission.

    Args:
        body (RestMeshNode | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RegisterNewMeshNodeResponse400 | RegisterNewMeshNodeResponse401 | RestMeshNode
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RestMeshNode | Unset = UNSET,
) -> Response[RegisterNewMeshNodeResponse400 | RegisterNewMeshNodeResponse401 | RestMeshNode]:
    """Register new Mesh node

     Register a new Mesh node.

    The authenticated user must have **SYS_ADMIN** permission.

    Args:
        body (RestMeshNode | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RegisterNewMeshNodeResponse400 | RegisterNewMeshNodeResponse401 | RestMeshNode]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RestMeshNode | Unset = UNSET,
) -> RegisterNewMeshNodeResponse400 | RegisterNewMeshNodeResponse401 | RestMeshNode | None:
    """Register new Mesh node

     Register a new Mesh node.

    The authenticated user must have **SYS_ADMIN** permission.

    Args:
        body (RestMeshNode | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RegisterNewMeshNodeResponse400 | RegisterNewMeshNodeResponse401 | RestMeshNode
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
