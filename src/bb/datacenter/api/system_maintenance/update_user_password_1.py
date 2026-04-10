from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_user_password_1_response_400 import UpdateUserPassword1Response400
from ...models.update_user_password_1_response_401 import UpdateUserPassword1Response401
from ...models.user_password_update import UserPasswordUpdate
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: UserPasswordUpdate | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/latest/users/credentials",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | UpdateUserPassword1Response400 | UpdateUserPassword1Response401 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = UpdateUserPassword1Response400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UpdateUserPassword1Response401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | UpdateUserPassword1Response400 | UpdateUserPassword1Response401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UserPasswordUpdate | Unset = UNSET,
) -> Response[Any | UpdateUserPassword1Response400 | UpdateUserPassword1Response401]:
    """Set password

     Update the currently authenticated user's password.

    Args:
        body (UserPasswordUpdate | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | UpdateUserPassword1Response400 | UpdateUserPassword1Response401]
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
    body: UserPasswordUpdate | Unset = UNSET,
) -> Any | UpdateUserPassword1Response400 | UpdateUserPassword1Response401 | None:
    """Set password

     Update the currently authenticated user's password.

    Args:
        body (UserPasswordUpdate | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | UpdateUserPassword1Response400 | UpdateUserPassword1Response401
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UserPasswordUpdate | Unset = UNSET,
) -> Response[Any | UpdateUserPassword1Response400 | UpdateUserPassword1Response401]:
    """Set password

     Update the currently authenticated user's password.

    Args:
        body (UserPasswordUpdate | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | UpdateUserPassword1Response400 | UpdateUserPassword1Response401]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: UserPasswordUpdate | Unset = UNSET,
) -> Any | UpdateUserPassword1Response400 | UpdateUserPassword1Response401 | None:
    """Set password

     Update the currently authenticated user's password.

    Args:
        body (UserPasswordUpdate | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | UpdateUserPassword1Response400 | UpdateUserPassword1Response401
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
