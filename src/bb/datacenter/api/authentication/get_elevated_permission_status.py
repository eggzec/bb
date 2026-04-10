from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.elevation_method_rest_dto import ElevationMethodRestDTO
from ...models.get_elevated_permission_status_action_type import GetElevatedPermissionStatusActionType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    action_type: GetElevatedPermissionStatusActionType | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_action_type: str | Unset = UNSET
    if not isinstance(action_type, Unset):
        json_action_type = action_type.value

    params["actionType"] = json_action_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/tsv/latest/elevate-permissions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ElevationMethodRestDTO | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = ElevationMethodRestDTO.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ElevationMethodRestDTO]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    action_type: GetElevatedPermissionStatusActionType | Unset = UNSET,
) -> Response[Any | ElevationMethodRestDTO]:
    """Get elevated session status

     Checks the state of an elevated session for the currently authenticated user.

    Args:
        action_type (GetElevatedPermissionStatusActionType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ElevationMethodRestDTO]
    """

    kwargs = _get_kwargs(
        action_type=action_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    action_type: GetElevatedPermissionStatusActionType | Unset = UNSET,
) -> Any | ElevationMethodRestDTO | None:
    """Get elevated session status

     Checks the state of an elevated session for the currently authenticated user.

    Args:
        action_type (GetElevatedPermissionStatusActionType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ElevationMethodRestDTO
    """

    return sync_detailed(
        client=client,
        action_type=action_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    action_type: GetElevatedPermissionStatusActionType | Unset = UNSET,
) -> Response[Any | ElevationMethodRestDTO]:
    """Get elevated session status

     Checks the state of an elevated session for the currently authenticated user.

    Args:
        action_type (GetElevatedPermissionStatusActionType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ElevationMethodRestDTO]
    """

    kwargs = _get_kwargs(
        action_type=action_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    action_type: GetElevatedPermissionStatusActionType | Unset = UNSET,
) -> Any | ElevationMethodRestDTO | None:
    """Get elevated session status

     Checks the state of an elevated session for the currently authenticated user.

    Args:
        action_type (GetElevatedPermissionStatusActionType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ElevationMethodRestDTO
    """

    return (
        await asyncio_detailed(
            client=client,
            action_type=action_type,
        )
    ).parsed
