from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_mesh_node import RestMeshNode
from ...models.update_mesh_node_response_400 import UpdateMeshNodeResponse400
from ...models.update_mesh_node_response_401 import UpdateMeshNodeResponse401
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: RestMeshNode | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/latest/admin/git/mesh/nodes/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RestMeshNode | UpdateMeshNodeResponse400 | UpdateMeshNodeResponse401 | None:
    if response.status_code == 200:
        response_200 = RestMeshNode.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UpdateMeshNodeResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UpdateMeshNodeResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RestMeshNode | UpdateMeshNodeResponse400 | UpdateMeshNodeResponse401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestMeshNode | Unset = UNSET,
) -> Response[RestMeshNode | UpdateMeshNodeResponse400 | UpdateMeshNodeResponse401]:
    """Update Mesh node

     Update a Mesh node.

    The authenticated user must have **SYS_ADMIN** permission.

    Args:
        id (str):
        body (RestMeshNode | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestMeshNode | UpdateMeshNodeResponse400 | UpdateMeshNodeResponse401]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestMeshNode | Unset = UNSET,
) -> RestMeshNode | UpdateMeshNodeResponse400 | UpdateMeshNodeResponse401 | None:
    """Update Mesh node

     Update a Mesh node.

    The authenticated user must have **SYS_ADMIN** permission.

    Args:
        id (str):
        body (RestMeshNode | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestMeshNode | UpdateMeshNodeResponse400 | UpdateMeshNodeResponse401
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestMeshNode | Unset = UNSET,
) -> Response[RestMeshNode | UpdateMeshNodeResponse400 | UpdateMeshNodeResponse401]:
    """Update Mesh node

     Update a Mesh node.

    The authenticated user must have **SYS_ADMIN** permission.

    Args:
        id (str):
        body (RestMeshNode | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestMeshNode | UpdateMeshNodeResponse400 | UpdateMeshNodeResponse401]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestMeshNode | Unset = UNSET,
) -> RestMeshNode | UpdateMeshNodeResponse400 | UpdateMeshNodeResponse401 | None:
    """Update Mesh node

     Update a Mesh node.

    The authenticated user must have **SYS_ADMIN** permission.

    Args:
        id (str):
        body (RestMeshNode | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestMeshNode | UpdateMeshNodeResponse400 | UpdateMeshNodeResponse401
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
