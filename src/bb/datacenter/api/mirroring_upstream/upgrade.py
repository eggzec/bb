from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_mirror_server import RestMirrorServer
from ...models.rest_mirror_upgrade_request import RestMirrorUpgradeRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    mirror_id: str,
    *,
    body: RestMirrorUpgradeRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/mirroring/latest/mirrorServers/{mirror_id}".format(
            mirror_id=quote(str(mirror_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RestMirrorServer | None:
    if response.status_code == 200:
        response_200 = RestMirrorServer.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RestMirrorServer]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    mirror_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestMirrorUpgradeRequest | Unset = UNSET,
) -> Response[RestMirrorServer]:
    """Upgrade mirror server

     Upgrades the mirror server in question with the provided details.This endpoint can only be called by
    the mirror instance or system administrators<br>Since 5.8

    Args:
        mirror_id (str):
        body (RestMirrorUpgradeRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestMirrorServer]
    """

    kwargs = _get_kwargs(
        mirror_id=mirror_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    mirror_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestMirrorUpgradeRequest | Unset = UNSET,
) -> RestMirrorServer | None:
    """Upgrade mirror server

     Upgrades the mirror server in question with the provided details.This endpoint can only be called by
    the mirror instance or system administrators<br>Since 5.8

    Args:
        mirror_id (str):
        body (RestMirrorUpgradeRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestMirrorServer
    """

    return sync_detailed(
        mirror_id=mirror_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    mirror_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestMirrorUpgradeRequest | Unset = UNSET,
) -> Response[RestMirrorServer]:
    """Upgrade mirror server

     Upgrades the mirror server in question with the provided details.This endpoint can only be called by
    the mirror instance or system administrators<br>Since 5.8

    Args:
        mirror_id (str):
        body (RestMirrorUpgradeRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestMirrorServer]
    """

    kwargs = _get_kwargs(
        mirror_id=mirror_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    mirror_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestMirrorUpgradeRequest | Unset = UNSET,
) -> RestMirrorServer | None:
    """Upgrade mirror server

     Upgrades the mirror server in question with the provided details.This endpoint can only be called by
    the mirror instance or system administrators<br>Since 5.8

    Args:
        mirror_id (str):
        body (RestMirrorUpgradeRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestMirrorServer
    """

    return (
        await asyncio_detailed(
            mirror_id=mirror_id,
            client=client,
            body=body,
        )
    ).parsed
