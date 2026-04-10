from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.erase_user_response_400 import EraseUserResponse400
from ...models.erase_user_response_401 import EraseUserResponse401
from ...models.erase_user_response_404 import EraseUserResponse404
from ...models.erase_user_response_409 import EraseUserResponse409
from ...models.rest_erased_user import RestErasedUser
from ...types import UNSET, Response


def _get_kwargs(
    *,
    name: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["name"] = name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/latest/admin/users/erasure",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EraseUserResponse400 | EraseUserResponse401 | EraseUserResponse404 | EraseUserResponse409 | RestErasedUser | None:
    if response.status_code == 200:
        response_200 = RestErasedUser.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = EraseUserResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = EraseUserResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = EraseUserResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = EraseUserResponse409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    EraseUserResponse400 | EraseUserResponse401 | EraseUserResponse404 | EraseUserResponse409 | RestErasedUser
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
    EraseUserResponse400 | EraseUserResponse401 | EraseUserResponse404 | EraseUserResponse409 | RestErasedUser
]:
    r"""Erase user information

     Erases personally identifying user data for a deleted user.

    References in the application to the original username will be either removed or updated to a new
    non-identifying username. Refer to the <a href=\"https://confluence.atlassian.com/gdpr/bitbucket-
    right-to-erasure-949770560.html\">support guide</a> for details about what data is and isn't erased.

    User erasure can only be performed on a deleted user. If the user has not been deleted first then
    this endpoint will return a bad request and no erasure will be performed.

    Erasing user data is <strong>irreversible</strong> and may lead to a degraded user experience. This
    method should not be used as part of a standard user deletion and cleanup process.

    Plugins can participate in user erasure by defining a <code>&lt;user-erasure-handler&gt;</code>
    module. If one or more plugin modules fail, an error summary of the failing modules is returned.

    The authenticated user must have the <strong>ADMIN</strong> permission to call this resource.

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EraseUserResponse400 | EraseUserResponse401 | EraseUserResponse404 | EraseUserResponse409 | RestErasedUser]
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
) -> EraseUserResponse400 | EraseUserResponse401 | EraseUserResponse404 | EraseUserResponse409 | RestErasedUser | None:
    r"""Erase user information

     Erases personally identifying user data for a deleted user.

    References in the application to the original username will be either removed or updated to a new
    non-identifying username. Refer to the <a href=\"https://confluence.atlassian.com/gdpr/bitbucket-
    right-to-erasure-949770560.html\">support guide</a> for details about what data is and isn't erased.

    User erasure can only be performed on a deleted user. If the user has not been deleted first then
    this endpoint will return a bad request and no erasure will be performed.

    Erasing user data is <strong>irreversible</strong> and may lead to a degraded user experience. This
    method should not be used as part of a standard user deletion and cleanup process.

    Plugins can participate in user erasure by defining a <code>&lt;user-erasure-handler&gt;</code>
    module. If one or more plugin modules fail, an error summary of the failing modules is returned.

    The authenticated user must have the <strong>ADMIN</strong> permission to call this resource.

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EraseUserResponse400 | EraseUserResponse401 | EraseUserResponse404 | EraseUserResponse409 | RestErasedUser
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
    EraseUserResponse400 | EraseUserResponse401 | EraseUserResponse404 | EraseUserResponse409 | RestErasedUser
]:
    r"""Erase user information

     Erases personally identifying user data for a deleted user.

    References in the application to the original username will be either removed or updated to a new
    non-identifying username. Refer to the <a href=\"https://confluence.atlassian.com/gdpr/bitbucket-
    right-to-erasure-949770560.html\">support guide</a> for details about what data is and isn't erased.

    User erasure can only be performed on a deleted user. If the user has not been deleted first then
    this endpoint will return a bad request and no erasure will be performed.

    Erasing user data is <strong>irreversible</strong> and may lead to a degraded user experience. This
    method should not be used as part of a standard user deletion and cleanup process.

    Plugins can participate in user erasure by defining a <code>&lt;user-erasure-handler&gt;</code>
    module. If one or more plugin modules fail, an error summary of the failing modules is returned.

    The authenticated user must have the <strong>ADMIN</strong> permission to call this resource.

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EraseUserResponse400 | EraseUserResponse401 | EraseUserResponse404 | EraseUserResponse409 | RestErasedUser]
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
) -> EraseUserResponse400 | EraseUserResponse401 | EraseUserResponse404 | EraseUserResponse409 | RestErasedUser | None:
    r"""Erase user information

     Erases personally identifying user data for a deleted user.

    References in the application to the original username will be either removed or updated to a new
    non-identifying username. Refer to the <a href=\"https://confluence.atlassian.com/gdpr/bitbucket-
    right-to-erasure-949770560.html\">support guide</a> for details about what data is and isn't erased.

    User erasure can only be performed on a deleted user. If the user has not been deleted first then
    this endpoint will return a bad request and no erasure will be performed.

    Erasing user data is <strong>irreversible</strong> and may lead to a degraded user experience. This
    method should not be used as part of a standard user deletion and cleanup process.

    Plugins can participate in user erasure by defining a <code>&lt;user-erasure-handler&gt;</code>
    module. If one or more plugin modules fail, an error summary of the failing modules is returned.

    The authenticated user must have the <strong>ADMIN</strong> permission to call this resource.

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EraseUserResponse400 | EraseUserResponse401 | EraseUserResponse404 | EraseUserResponse409 | RestErasedUser
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
        )
    ).parsed
