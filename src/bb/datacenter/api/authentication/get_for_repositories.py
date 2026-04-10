from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_for_repositories_response_404 import GetForRepositoriesResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    key_id: str,
    *,
    with_restrictions: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["withRestrictions"] = with_restrictions

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/keys/latest/ssh/{key_id}/repos".format(
            key_id=quote(str(key_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetForRepositoriesResponse404 | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 404:
        response_404 = GetForRepositoriesResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetForRepositoriesResponse404]:
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
    with_restrictions: str | Unset = UNSET,
) -> Response[Any | GetForRepositoriesResponse404]:
    """Get repository SSH key

     Retrieves all repository-related access keys for the SSH key with id <code>keyId</code>. If the
    current user is not an admin of any of the projects the key provides access to, none are returned.

    Args:
        key_id (str):
        with_restrictions (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetForRepositoriesResponse404]
    """

    kwargs = _get_kwargs(
        key_id=key_id,
        with_restrictions=with_restrictions,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    key_id: str,
    *,
    client: AuthenticatedClient | Client,
    with_restrictions: str | Unset = UNSET,
) -> Any | GetForRepositoriesResponse404 | None:
    """Get repository SSH key

     Retrieves all repository-related access keys for the SSH key with id <code>keyId</code>. If the
    current user is not an admin of any of the projects the key provides access to, none are returned.

    Args:
        key_id (str):
        with_restrictions (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetForRepositoriesResponse404
    """

    return sync_detailed(
        key_id=key_id,
        client=client,
        with_restrictions=with_restrictions,
    ).parsed


async def asyncio_detailed(
    key_id: str,
    *,
    client: AuthenticatedClient | Client,
    with_restrictions: str | Unset = UNSET,
) -> Response[Any | GetForRepositoriesResponse404]:
    """Get repository SSH key

     Retrieves all repository-related access keys for the SSH key with id <code>keyId</code>. If the
    current user is not an admin of any of the projects the key provides access to, none are returned.

    Args:
        key_id (str):
        with_restrictions (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetForRepositoriesResponse404]
    """

    kwargs = _get_kwargs(
        key_id=key_id,
        with_restrictions=with_restrictions,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    key_id: str,
    *,
    client: AuthenticatedClient | Client,
    with_restrictions: str | Unset = UNSET,
) -> Any | GetForRepositoriesResponse404 | None:
    """Get repository SSH key

     Retrieves all repository-related access keys for the SSH key with id <code>keyId</code>. If the
    current user is not an admin of any of the projects the key provides access to, none are returned.

    Args:
        key_id (str):
        with_restrictions (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetForRepositoriesResponse404
    """

    return (
        await asyncio_detailed(
            key_id=key_id,
            client=client,
            with_restrictions=with_restrictions,
        )
    ).parsed
