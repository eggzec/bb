from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.group_picker_context import GroupPickerContext
from ...models.remove_group_from_user_response_401 import RemoveGroupFromUserResponse401
from ...models.remove_group_from_user_response_403 import RemoveGroupFromUserResponse403
from ...models.remove_group_from_user_response_404 import RemoveGroupFromUserResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: GroupPickerContext | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/latest/admin/users/remove-group",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RemoveGroupFromUserResponse401 | RemoveGroupFromUserResponse403 | RemoveGroupFromUserResponse404 | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 401:
        response_401 = RemoveGroupFromUserResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = RemoveGroupFromUserResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = RemoveGroupFromUserResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RemoveGroupFromUserResponse401 | RemoveGroupFromUserResponse403 | RemoveGroupFromUserResponse404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GroupPickerContext | Unset = UNSET,
) -> Response[Any | RemoveGroupFromUserResponse401 | RemoveGroupFromUserResponse403 | RemoveGroupFromUserResponse404]:
    """Remove user from group

     Remove a user from a group. This is very similar to <code>groups/remove-user</code>, but with the
    <em>context</em> and <em>itemName</em> attributes of the supplied request entity reversed. On the
    face of it this may appear redundant, but it facilitates a specific UI component in the application.

    In the request entity, the <em>context</em> attribute is the user and the <em>itemName</em> is the
    group.

    The authenticated user must have the <strong>ADMIN</strong> permission to call this resource.

    Args:
        body (GroupPickerContext | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RemoveGroupFromUserResponse401 | RemoveGroupFromUserResponse403 | RemoveGroupFromUserResponse404]
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
    body: GroupPickerContext | Unset = UNSET,
) -> Any | RemoveGroupFromUserResponse401 | RemoveGroupFromUserResponse403 | RemoveGroupFromUserResponse404 | None:
    """Remove user from group

     Remove a user from a group. This is very similar to <code>groups/remove-user</code>, but with the
    <em>context</em> and <em>itemName</em> attributes of the supplied request entity reversed. On the
    face of it this may appear redundant, but it facilitates a specific UI component in the application.

    In the request entity, the <em>context</em> attribute is the user and the <em>itemName</em> is the
    group.

    The authenticated user must have the <strong>ADMIN</strong> permission to call this resource.

    Args:
        body (GroupPickerContext | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RemoveGroupFromUserResponse401 | RemoveGroupFromUserResponse403 | RemoveGroupFromUserResponse404
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GroupPickerContext | Unset = UNSET,
) -> Response[Any | RemoveGroupFromUserResponse401 | RemoveGroupFromUserResponse403 | RemoveGroupFromUserResponse404]:
    """Remove user from group

     Remove a user from a group. This is very similar to <code>groups/remove-user</code>, but with the
    <em>context</em> and <em>itemName</em> attributes of the supplied request entity reversed. On the
    face of it this may appear redundant, but it facilitates a specific UI component in the application.

    In the request entity, the <em>context</em> attribute is the user and the <em>itemName</em> is the
    group.

    The authenticated user must have the <strong>ADMIN</strong> permission to call this resource.

    Args:
        body (GroupPickerContext | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RemoveGroupFromUserResponse401 | RemoveGroupFromUserResponse403 | RemoveGroupFromUserResponse404]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: GroupPickerContext | Unset = UNSET,
) -> Any | RemoveGroupFromUserResponse401 | RemoveGroupFromUserResponse403 | RemoveGroupFromUserResponse404 | None:
    """Remove user from group

     Remove a user from a group. This is very similar to <code>groups/remove-user</code>, but with the
    <em>context</em> and <em>itemName</em> attributes of the supplied request entity reversed. On the
    face of it this may appear redundant, but it facilitates a specific UI component in the application.

    In the request entity, the <em>context</em> attribute is the user and the <em>itemName</em> is the
    group.

    The authenticated user must have the <strong>ADMIN</strong> permission to call this resource.

    Args:
        body (GroupPickerContext | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RemoveGroupFromUserResponse401 | RemoveGroupFromUserResponse403 | RemoveGroupFromUserResponse404
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
