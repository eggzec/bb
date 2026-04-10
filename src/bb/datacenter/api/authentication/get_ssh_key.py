from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_ssh_key_response_401 import GetSshKeyResponse401
from ...models.get_ssh_key_response_404 import GetSshKeyResponse404
from ...models.rest_ssh_key import RestSshKey
from ...types import Response


def _get_kwargs(
    key_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/ssh/latest/keys/{key_id}".format(
            key_id=quote(str(key_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetSshKeyResponse401 | GetSshKeyResponse404 | RestSshKey | None:
    if response.status_code == 200:
        response_200 = RestSshKey.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetSshKeyResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetSshKeyResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetSshKeyResponse401 | GetSshKeyResponse404 | RestSshKey]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    key_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetSshKeyResponse401 | GetSshKeyResponse404 | RestSshKey]:
    """Get SSH key for user by keyId

     Retrieve an SSH key by keyId

    The authenticated user must have <strong>ADMIN</strong> permission or higher to call this resource.

    Args:
        key_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSshKeyResponse401 | GetSshKeyResponse404 | RestSshKey]
    """

    kwargs = _get_kwargs(
        key_id=key_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    key_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetSshKeyResponse401 | GetSshKeyResponse404 | RestSshKey | None:
    """Get SSH key for user by keyId

     Retrieve an SSH key by keyId

    The authenticated user must have <strong>ADMIN</strong> permission or higher to call this resource.

    Args:
        key_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSshKeyResponse401 | GetSshKeyResponse404 | RestSshKey
    """

    return sync_detailed(
        key_id=key_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    key_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetSshKeyResponse401 | GetSshKeyResponse404 | RestSshKey]:
    """Get SSH key for user by keyId

     Retrieve an SSH key by keyId

    The authenticated user must have <strong>ADMIN</strong> permission or higher to call this resource.

    Args:
        key_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSshKeyResponse401 | GetSshKeyResponse404 | RestSshKey]
    """

    kwargs = _get_kwargs(
        key_id=key_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    key_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetSshKeyResponse401 | GetSshKeyResponse404 | RestSshKey | None:
    """Get SSH key for user by keyId

     Retrieve an SSH key by keyId

    The authenticated user must have <strong>ADMIN</strong> permission or higher to call this resource.

    Args:
        key_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSshKeyResponse401 | GetSshKeyResponse404 | RestSshKey
    """

    return (
        await asyncio_detailed(
            key_id=key_id,
            client=client,
        )
    ).parsed
