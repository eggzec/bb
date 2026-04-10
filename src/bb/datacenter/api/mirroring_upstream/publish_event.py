from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.publish_event_response_404 import PublishEventResponse404
from ...models.rest_repository_mirror_event import RestRepositoryMirrorEvent
from ...types import UNSET, Response, Unset


def _get_kwargs(
    mirror_id: str,
    *,
    body: RestRepositoryMirrorEvent | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/mirroring/latest/mirrorServers/{mirror_id}/events".format(
            mirror_id=quote(str(mirror_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PublishEventResponse404 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 404:
        response_404 = PublishEventResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PublishEventResponse404]:
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
    body: RestRepositoryMirrorEvent | Unset = UNSET,
) -> Response[Any | PublishEventResponse404]:
    """Publish RepositoryMirrorEvent

     Publishes a RepositoryMirrorEvent on the event queue.

    Args:
        mirror_id (str):
        body (RestRepositoryMirrorEvent | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PublishEventResponse404]
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
    body: RestRepositoryMirrorEvent | Unset = UNSET,
) -> Any | PublishEventResponse404 | None:
    """Publish RepositoryMirrorEvent

     Publishes a RepositoryMirrorEvent on the event queue.

    Args:
        mirror_id (str):
        body (RestRepositoryMirrorEvent | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PublishEventResponse404
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
    body: RestRepositoryMirrorEvent | Unset = UNSET,
) -> Response[Any | PublishEventResponse404]:
    """Publish RepositoryMirrorEvent

     Publishes a RepositoryMirrorEvent on the event queue.

    Args:
        mirror_id (str):
        body (RestRepositoryMirrorEvent | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PublishEventResponse404]
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
    body: RestRepositoryMirrorEvent | Unset = UNSET,
) -> Any | PublishEventResponse404 | None:
    """Publish RepositoryMirrorEvent

     Publishes a RepositoryMirrorEvent on the event queue.

    Args:
        mirror_id (str):
        body (RestRepositoryMirrorEvent | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PublishEventResponse404
    """

    return (
        await asyncio_detailed(
            mirror_id=mirror_id,
            client=client,
            body=body,
        )
    ).parsed
