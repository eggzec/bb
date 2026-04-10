from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_mirrored_projects_response_401 import GetMirroredProjectsResponse401
from ...models.get_mirrored_projects_response_404 import GetMirroredProjectsResponse404
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/mirroring/latest/syncSettings/projects",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetMirroredProjectsResponse401 | GetMirroredProjectsResponse404 | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 401:
        response_401 = GetMirroredProjectsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetMirroredProjectsResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetMirroredProjectsResponse401 | GetMirroredProjectsResponse404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetMirroredProjectsResponse401 | GetMirroredProjectsResponse404]:
    """Get mirrored project IDs

     Returns the IDs of the projects that the mirror is configured to mirror

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetMirroredProjectsResponse401 | GetMirroredProjectsResponse404]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetMirroredProjectsResponse401 | GetMirroredProjectsResponse404 | None:
    """Get mirrored project IDs

     Returns the IDs of the projects that the mirror is configured to mirror

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetMirroredProjectsResponse401 | GetMirroredProjectsResponse404
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetMirroredProjectsResponse401 | GetMirroredProjectsResponse404]:
    """Get mirrored project IDs

     Returns the IDs of the projects that the mirror is configured to mirror

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetMirroredProjectsResponse401 | GetMirroredProjectsResponse404]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetMirroredProjectsResponse401 | GetMirroredProjectsResponse404 | None:
    """Get mirrored project IDs

     Returns the IDs of the projects that the mirror is configured to mirror

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetMirroredProjectsResponse401 | GetMirroredProjectsResponse404
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
