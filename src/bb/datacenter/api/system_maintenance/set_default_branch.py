from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.set_default_branch_body import SetDefaultBranchBody
from ...models.set_default_branch_response_401 import SetDefaultBranchResponse401
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SetDefaultBranchBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/latest/admin/default-branch",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | SetDefaultBranchResponse401 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = SetDefaultBranchResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | SetDefaultBranchResponse401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SetDefaultBranchBody | Unset = UNSET,
) -> Response[Any | SetDefaultBranchResponse401]:
    """Update/Set default branch

     Configures the global default branch, which is used when creating new repositories if an explicit
    default branch is not specified.

    The authenticated user must have <strong>ADMIN</strong> permission to call this resource.

    Args:
        body (SetDefaultBranchBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SetDefaultBranchResponse401]
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
    body: SetDefaultBranchBody | Unset = UNSET,
) -> Any | SetDefaultBranchResponse401 | None:
    """Update/Set default branch

     Configures the global default branch, which is used when creating new repositories if an explicit
    default branch is not specified.

    The authenticated user must have <strong>ADMIN</strong> permission to call this resource.

    Args:
        body (SetDefaultBranchBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SetDefaultBranchResponse401
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SetDefaultBranchBody | Unset = UNSET,
) -> Response[Any | SetDefaultBranchResponse401]:
    """Update/Set default branch

     Configures the global default branch, which is used when creating new repositories if an explicit
    default branch is not specified.

    The authenticated user must have <strong>ADMIN</strong> permission to call this resource.

    Args:
        body (SetDefaultBranchBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SetDefaultBranchResponse401]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SetDefaultBranchBody | Unset = UNSET,
) -> Any | SetDefaultBranchResponse401 | None:
    """Update/Set default branch

     Configures the global default branch, which is used when creating new repositories if an explicit
    default branch is not specified.

    The authenticated user must have <strong>ADMIN</strong> permission to call this resource.

    Args:
        body (SetDefaultBranchBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SetDefaultBranchResponse401
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
