from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.validate_erasable_response_400 import ValidateErasableResponse400
from ...models.validate_erasable_response_401 import ValidateErasableResponse401
from ...models.validate_erasable_response_404 import ValidateErasableResponse404
from ...models.validate_erasable_response_409 import ValidateErasableResponse409
from ...types import UNSET, Response


def _get_kwargs(
    *,
    name: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["name"] = name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/admin/users/erasure",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | ValidateErasableResponse400
    | ValidateErasableResponse401
    | ValidateErasableResponse404
    | ValidateErasableResponse409
    | None
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = ValidateErasableResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ValidateErasableResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ValidateErasableResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ValidateErasableResponse409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | ValidateErasableResponse400
    | ValidateErasableResponse401
    | ValidateErasableResponse404
    | ValidateErasableResponse409
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    name: str,
) -> Response[
    Any
    | ValidateErasableResponse400
    | ValidateErasableResponse401
    | ValidateErasableResponse404
    | ValidateErasableResponse409
]:
    """Check user removal

     Validate if a user can be erased.

    A username is only valid for erasure if it exists as the username of a deleted user. This endpoint
    will return an appropriate error response if the supplied username is invalid for erasure.

    This endpoint does <strong>not</strong> perform the actual user erasure, and will not modify the
    application in any way.

    The authenticated user must have the <strong>ADMIN</strong> permission to call this resource.

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ValidateErasableResponse400 | ValidateErasableResponse401 | ValidateErasableResponse404 | ValidateErasableResponse409]
    """

    kwargs = _get_kwargs(
        name=name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    name: str,
) -> (
    Any
    | ValidateErasableResponse400
    | ValidateErasableResponse401
    | ValidateErasableResponse404
    | ValidateErasableResponse409
    | None
):
    """Check user removal

     Validate if a user can be erased.

    A username is only valid for erasure if it exists as the username of a deleted user. This endpoint
    will return an appropriate error response if the supplied username is invalid for erasure.

    This endpoint does <strong>not</strong> perform the actual user erasure, and will not modify the
    application in any way.

    The authenticated user must have the <strong>ADMIN</strong> permission to call this resource.

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ValidateErasableResponse400 | ValidateErasableResponse401 | ValidateErasableResponse404 | ValidateErasableResponse409
    """

    return sync_detailed(
        client=client,
        name=name,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    name: str,
) -> Response[
    Any
    | ValidateErasableResponse400
    | ValidateErasableResponse401
    | ValidateErasableResponse404
    | ValidateErasableResponse409
]:
    """Check user removal

     Validate if a user can be erased.

    A username is only valid for erasure if it exists as the username of a deleted user. This endpoint
    will return an appropriate error response if the supplied username is invalid for erasure.

    This endpoint does <strong>not</strong> perform the actual user erasure, and will not modify the
    application in any way.

    The authenticated user must have the <strong>ADMIN</strong> permission to call this resource.

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ValidateErasableResponse400 | ValidateErasableResponse401 | ValidateErasableResponse404 | ValidateErasableResponse409]
    """

    kwargs = _get_kwargs(
        name=name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    name: str,
) -> (
    Any
    | ValidateErasableResponse400
    | ValidateErasableResponse401
    | ValidateErasableResponse404
    | ValidateErasableResponse409
    | None
):
    """Check user removal

     Validate if a user can be erased.

    A username is only valid for erasure if it exists as the username of a deleted user. This endpoint
    will return an appropriate error response if the supplied username is invalid for erasure.

    This endpoint does <strong>not</strong> perform the actual user erasure, and will not modify the
    application in any way.

    The authenticated user must have the <strong>ADMIN</strong> permission to call this resource.

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ValidateErasableResponse400 | ValidateErasableResponse401 | ValidateErasableResponse404 | ValidateErasableResponse409
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
        )
    ).parsed
