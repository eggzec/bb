from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.start_mirroring_projects_response_401 import StartMirroringProjectsResponse401
from ...models.start_mirroring_projects_response_404 import StartMirroringProjectsResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: list[str] | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/mirroring/latest/syncSettings/projects",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | StartMirroringProjectsResponse401 | StartMirroringProjectsResponse404 | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 401:
        response_401 = StartMirroringProjectsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = StartMirroringProjectsResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | StartMirroringProjectsResponse401 | StartMirroringProjectsResponse404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list[str] | Unset = UNSET,
) -> Response[Any | StartMirroringProjectsResponse401 | StartMirroringProjectsResponse404]:
    """Add multiple projects to be mirrored

     Configures the mirror to mirror the provided projects

    Args:
        body (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | StartMirroringProjectsResponse401 | StartMirroringProjectsResponse404]
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
    body: list[str] | Unset = UNSET,
) -> Any | StartMirroringProjectsResponse401 | StartMirroringProjectsResponse404 | None:
    """Add multiple projects to be mirrored

     Configures the mirror to mirror the provided projects

    Args:
        body (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | StartMirroringProjectsResponse401 | StartMirroringProjectsResponse404
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list[str] | Unset = UNSET,
) -> Response[Any | StartMirroringProjectsResponse401 | StartMirroringProjectsResponse404]:
    """Add multiple projects to be mirrored

     Configures the mirror to mirror the provided projects

    Args:
        body (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | StartMirroringProjectsResponse401 | StartMirroringProjectsResponse404]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: list[str] | Unset = UNSET,
) -> Any | StartMirroringProjectsResponse401 | StartMirroringProjectsResponse404 | None:
    """Add multiple projects to be mirrored

     Configures the mirror to mirror the provided projects

    Args:
        body (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | StartMirroringProjectsResponse401 | StartMirroringProjectsResponse404
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
