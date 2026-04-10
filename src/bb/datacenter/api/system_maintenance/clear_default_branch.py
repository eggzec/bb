from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.clear_default_branch_response_401 import ClearDefaultBranchResponse401
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/latest/admin/default-branch",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ClearDefaultBranchResponse401 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = ClearDefaultBranchResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ClearDefaultBranchResponse401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | ClearDefaultBranchResponse401]:
    """Clear default branch

     Clears the global default branch, which is used when creating new repositories if an explicit
    default branch is not specified, if one has been configured.

    The authenticated user must have <strong>ADMIN</strong> permission to call this resource.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ClearDefaultBranchResponse401]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> Any | ClearDefaultBranchResponse401 | None:
    """Clear default branch

     Clears the global default branch, which is used when creating new repositories if an explicit
    default branch is not specified, if one has been configured.

    The authenticated user must have <strong>ADMIN</strong> permission to call this resource.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ClearDefaultBranchResponse401
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | ClearDefaultBranchResponse401]:
    """Clear default branch

     Clears the global default branch, which is used when creating new repositories if an explicit
    default branch is not specified, if one has been configured.

    The authenticated user must have <strong>ADMIN</strong> permission to call this resource.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ClearDefaultBranchResponse401]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> Any | ClearDefaultBranchResponse401 | None:
    """Clear default branch

     Clears the global default branch, which is used when creating new repositories if an explicit
    default branch is not specified, if one has been configured.

    The authenticated user must have <strong>ADMIN</strong> permission to call this resource.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ClearDefaultBranchResponse401
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
