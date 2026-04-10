from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_user_response_400 import CreateUserResponse400
from ...models.create_user_response_401 import CreateUserResponse401
from ...models.create_user_response_403 import CreateUserResponse403
from ...models.create_user_response_409 import CreateUserResponse409
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    email_address: str,
    password: str | Unset = UNSET,
    add_to_default_group: bool | Unset = True,
    display_name: str,
    name: str,
    notify: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["emailAddress"] = email_address

    params["password"] = password

    params["addToDefaultGroup"] = add_to_default_group

    params["displayName"] = display_name

    params["name"] = name

    params["notify"] = notify

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/latest/admin/users",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CreateUserResponse400 | CreateUserResponse401 | CreateUserResponse403 | CreateUserResponse409 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = CreateUserResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = CreateUserResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = CreateUserResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 409:
        response_409 = CreateUserResponse409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CreateUserResponse400 | CreateUserResponse401 | CreateUserResponse403 | CreateUserResponse409]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    email_address: str,
    password: str | Unset = UNSET,
    add_to_default_group: bool | Unset = True,
    display_name: str,
    name: str,
    notify: bool | Unset = UNSET,
) -> Response[Any | CreateUserResponse400 | CreateUserResponse401 | CreateUserResponse403 | CreateUserResponse409]:
    """Create user

     Creates a new user from the assembled query parameters.

    The default group can be used to control initial permissions for new users, such as granting users
    the ability to login or providing read access to certain projects or repositories. If the user is
    not added to the default group, they may not be able to login after their account is created until
    explicit permissions are configured.

    The authenticated user must have the <strong>ADMIN</strong> permission to call this resource.

    Args:
        email_address (str):
        password (str | Unset):
        add_to_default_group (bool | Unset):  Default: True.
        display_name (str):
        name (str):
        notify (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateUserResponse400 | CreateUserResponse401 | CreateUserResponse403 | CreateUserResponse409]
    """

    kwargs = _get_kwargs(
        email_address=email_address,
        password=password,
        add_to_default_group=add_to_default_group,
        display_name=display_name,
        name=name,
        notify=notify,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    email_address: str,
    password: str | Unset = UNSET,
    add_to_default_group: bool | Unset = True,
    display_name: str,
    name: str,
    notify: bool | Unset = UNSET,
) -> Any | CreateUserResponse400 | CreateUserResponse401 | CreateUserResponse403 | CreateUserResponse409 | None:
    """Create user

     Creates a new user from the assembled query parameters.

    The default group can be used to control initial permissions for new users, such as granting users
    the ability to login or providing read access to certain projects or repositories. If the user is
    not added to the default group, they may not be able to login after their account is created until
    explicit permissions are configured.

    The authenticated user must have the <strong>ADMIN</strong> permission to call this resource.

    Args:
        email_address (str):
        password (str | Unset):
        add_to_default_group (bool | Unset):  Default: True.
        display_name (str):
        name (str):
        notify (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateUserResponse400 | CreateUserResponse401 | CreateUserResponse403 | CreateUserResponse409
    """

    return sync_detailed(
        client=client,
        email_address=email_address,
        password=password,
        add_to_default_group=add_to_default_group,
        display_name=display_name,
        name=name,
        notify=notify,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    email_address: str,
    password: str | Unset = UNSET,
    add_to_default_group: bool | Unset = True,
    display_name: str,
    name: str,
    notify: bool | Unset = UNSET,
) -> Response[Any | CreateUserResponse400 | CreateUserResponse401 | CreateUserResponse403 | CreateUserResponse409]:
    """Create user

     Creates a new user from the assembled query parameters.

    The default group can be used to control initial permissions for new users, such as granting users
    the ability to login or providing read access to certain projects or repositories. If the user is
    not added to the default group, they may not be able to login after their account is created until
    explicit permissions are configured.

    The authenticated user must have the <strong>ADMIN</strong> permission to call this resource.

    Args:
        email_address (str):
        password (str | Unset):
        add_to_default_group (bool | Unset):  Default: True.
        display_name (str):
        name (str):
        notify (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateUserResponse400 | CreateUserResponse401 | CreateUserResponse403 | CreateUserResponse409]
    """

    kwargs = _get_kwargs(
        email_address=email_address,
        password=password,
        add_to_default_group=add_to_default_group,
        display_name=display_name,
        name=name,
        notify=notify,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    email_address: str,
    password: str | Unset = UNSET,
    add_to_default_group: bool | Unset = True,
    display_name: str,
    name: str,
    notify: bool | Unset = UNSET,
) -> Any | CreateUserResponse400 | CreateUserResponse401 | CreateUserResponse403 | CreateUserResponse409 | None:
    """Create user

     Creates a new user from the assembled query parameters.

    The default group can be used to control initial permissions for new users, such as granting users
    the ability to login or providing read access to certain projects or repositories. If the user is
    not added to the default group, they may not be able to login after their account is created until
    explicit permissions are configured.

    The authenticated user must have the <strong>ADMIN</strong> permission to call this resource.

    Args:
        email_address (str):
        password (str | Unset):
        add_to_default_group (bool | Unset):  Default: True.
        display_name (str):
        name (str):
        notify (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateUserResponse400 | CreateUserResponse401 | CreateUserResponse403 | CreateUserResponse409
    """

    return (
        await asyncio_detailed(
            client=client,
            email_address=email_address,
            password=password,
            add_to_default_group=add_to_default_group,
            display_name=display_name,
            name=name,
            notify=notify,
        )
    ).parsed
