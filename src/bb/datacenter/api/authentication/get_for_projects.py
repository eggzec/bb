from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_for_projects_response_404 import GetForProjectsResponse404
from ...types import Response


def _get_kwargs(
    key_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/keys/latest/ssh/{key_id}/projects".format(
            key_id=quote(str(key_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetForProjectsResponse404 | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 404:
        response_404 = GetForProjectsResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetForProjectsResponse404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    key_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetForProjectsResponse404]:
    """Get project SSH keys

     Retrieves all project-related access keys for the SSH key with id <code>keyId</code>. If the current
    user is not an admin any of the projects the key provides access to, none are returned.

    Args:
        key_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetForProjectsResponse404]
    """

    kwargs = _get_kwargs(
        key_id=key_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    key_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetForProjectsResponse404 | None:
    """Get project SSH keys

     Retrieves all project-related access keys for the SSH key with id <code>keyId</code>. If the current
    user is not an admin any of the projects the key provides access to, none are returned.

    Args:
        key_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetForProjectsResponse404
    """

    return sync_detailed(
        key_id=key_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    key_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetForProjectsResponse404]:
    """Get project SSH keys

     Retrieves all project-related access keys for the SSH key with id <code>keyId</code>. If the current
    user is not an admin any of the projects the key provides access to, none are returned.

    Args:
        key_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetForProjectsResponse404]
    """

    kwargs = _get_kwargs(
        key_id=key_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    key_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetForProjectsResponse404 | None:
    """Get project SSH keys

     Retrieves all project-related access keys for the SSH key with id <code>keyId</code>. If the current
    user is not an admin any of the projects the key provides access to, none are returned.

    Args:
        key_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetForProjectsResponse404
    """

    return (
        await asyncio_detailed(
            key_id=key_id,
            client=client,
        )
    ).parsed
