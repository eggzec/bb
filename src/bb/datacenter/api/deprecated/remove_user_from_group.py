from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...deprecation import deprecated_endpoint
from ...models.remove_user_from_group_response_401 import RemoveUserFromGroupResponse401
from ...models.remove_user_from_group_response_403 import RemoveUserFromGroupResponse403
from ...models.remove_user_from_group_response_404 import RemoveUserFromGroupResponse404
from ...models.user_picker_context import UserPickerContext
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: UserPickerContext | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/latest/admin/groups/remove-user",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RemoveUserFromGroupResponse401 | RemoveUserFromGroupResponse403 | RemoveUserFromGroupResponse404 | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 401:
        response_401 = RemoveUserFromGroupResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = RemoveUserFromGroupResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = RemoveUserFromGroupResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RemoveUserFromGroupResponse401 | RemoveUserFromGroupResponse403 | RemoveUserFromGroupResponse404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated_endpoint(None)
def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UserPickerContext | Unset = UNSET,
) -> Response[Any | RemoveUserFromGroupResponse401 | RemoveUserFromGroupResponse403 | RemoveUserFromGroupResponse404]:
    """Remove user from group

     <strong>Deprecated since 2.10</strong>. Use /rest/users/remove-groups instead.

    Remove a user from a group.

    The authenticated user must have the <strong>ADMIN</strong> permission to call this resource.

    In the request entity, the <em>context</em> attribute is the group and the <em>itemName</em> is the
    user.

    Args:
        body (UserPickerContext | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RemoveUserFromGroupResponse401 | RemoveUserFromGroupResponse403 | RemoveUserFromGroupResponse404]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated_endpoint(None)
def sync(
    *,
    client: AuthenticatedClient | Client,
    body: UserPickerContext | Unset = UNSET,
) -> Any | RemoveUserFromGroupResponse401 | RemoveUserFromGroupResponse403 | RemoveUserFromGroupResponse404 | None:
    """Remove user from group

     <strong>Deprecated since 2.10</strong>. Use /rest/users/remove-groups instead.

    Remove a user from a group.

    The authenticated user must have the <strong>ADMIN</strong> permission to call this resource.

    In the request entity, the <em>context</em> attribute is the group and the <em>itemName</em> is the
    user.

    Args:
        body (UserPickerContext | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RemoveUserFromGroupResponse401 | RemoveUserFromGroupResponse403 | RemoveUserFromGroupResponse404
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


@deprecated_endpoint(None)
async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UserPickerContext | Unset = UNSET,
) -> Response[Any | RemoveUserFromGroupResponse401 | RemoveUserFromGroupResponse403 | RemoveUserFromGroupResponse404]:
    """Remove user from group

     <strong>Deprecated since 2.10</strong>. Use /rest/users/remove-groups instead.

    Remove a user from a group.

    The authenticated user must have the <strong>ADMIN</strong> permission to call this resource.

    In the request entity, the <em>context</em> attribute is the group and the <em>itemName</em> is the
    user.

    Args:
        body (UserPickerContext | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RemoveUserFromGroupResponse401 | RemoveUserFromGroupResponse403 | RemoveUserFromGroupResponse404]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated_endpoint(None)
async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: UserPickerContext | Unset = UNSET,
) -> Any | RemoveUserFromGroupResponse401 | RemoveUserFromGroupResponse403 | RemoveUserFromGroupResponse404 | None:
    """Remove user from group

     <strong>Deprecated since 2.10</strong>. Use /rest/users/remove-groups instead.

    Remove a user from a group.

    The authenticated user must have the <strong>ADMIN</strong> permission to call this resource.

    In the request entity, the <em>context</em> attribute is the group and the <em>itemName</em> is the
    user.

    Args:
        body (UserPickerContext | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RemoveUserFromGroupResponse401 | RemoveUserFromGroupResponse403 | RemoveUserFromGroupResponse404
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
