from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_application_user import RestApplicationUser
from ...models.update_user_details_1_response_400 import UpdateUserDetails1Response400
from ...models.update_user_details_1_response_401 import UpdateUserDetails1Response401
from ...models.user_update_with_credentials import UserUpdateWithCredentials
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: UserUpdateWithCredentials | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/latest/users",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RestApplicationUser | UpdateUserDetails1Response400 | UpdateUserDetails1Response401 | None:
    if response.status_code == 200:
        response_200 = RestApplicationUser.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UpdateUserDetails1Response400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UpdateUserDetails1Response401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RestApplicationUser | UpdateUserDetails1Response400 | UpdateUserDetails1Response401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UserUpdateWithCredentials | Unset = UNSET,
) -> Response[RestApplicationUser | UpdateUserDetails1Response400 | UpdateUserDetails1Response401]:
    """Update user details

     Update the currently authenticated user's details. The update will always be applied to the
    currently authenticated user.

    Args:
        body (UserUpdateWithCredentials | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestApplicationUser | UpdateUserDetails1Response400 | UpdateUserDetails1Response401]
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
    body: UserUpdateWithCredentials | Unset = UNSET,
) -> RestApplicationUser | UpdateUserDetails1Response400 | UpdateUserDetails1Response401 | None:
    """Update user details

     Update the currently authenticated user's details. The update will always be applied to the
    currently authenticated user.

    Args:
        body (UserUpdateWithCredentials | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestApplicationUser | UpdateUserDetails1Response400 | UpdateUserDetails1Response401
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UserUpdateWithCredentials | Unset = UNSET,
) -> Response[RestApplicationUser | UpdateUserDetails1Response400 | UpdateUserDetails1Response401]:
    """Update user details

     Update the currently authenticated user's details. The update will always be applied to the
    currently authenticated user.

    Args:
        body (UserUpdateWithCredentials | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestApplicationUser | UpdateUserDetails1Response400 | UpdateUserDetails1Response401]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: UserUpdateWithCredentials | Unset = UNSET,
) -> RestApplicationUser | UpdateUserDetails1Response400 | UpdateUserDetails1Response401 | None:
    """Update user details

     Update the currently authenticated user's details. The update will always be applied to the
    currently authenticated user.

    Args:
        body (UserUpdateWithCredentials | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestApplicationUser | UpdateUserDetails1Response400 | UpdateUserDetails1Response401
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
