from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.elevate_permissions_with_password_action_type import ElevatePermissionsWithPasswordActionType
from ...models.error_entity import ErrorEntity
from ...models.totp_elevation_rest_dto import TotpElevationRestDTO
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: TotpElevationRestDTO | Unset = UNSET,
    action_type: ElevatePermissionsWithPasswordActionType | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_action_type: str | Unset = UNSET
    if not isinstance(action_type, Unset):
        json_action_type = action_type.value

    params["actionType"] = json_action_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/tsv/latest/elevate-permissions/password",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ErrorEntity | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = ErrorEntity.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ErrorEntity]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TotpElevationRestDTO | Unset = UNSET,
    action_type: ElevatePermissionsWithPasswordActionType | Unset = UNSET,
) -> Response[Any | ErrorEntity]:
    """Create elevated session with password

     Elevate permissions by providing the password for the currently authenticated user. This will create
    an elevated session.

    Args:
        action_type (ElevatePermissionsWithPasswordActionType | Unset):
        body (TotpElevationRestDTO | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorEntity]
    """

    kwargs = _get_kwargs(
        body=body,
        action_type=action_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: TotpElevationRestDTO | Unset = UNSET,
    action_type: ElevatePermissionsWithPasswordActionType | Unset = UNSET,
) -> Any | ErrorEntity | None:
    """Create elevated session with password

     Elevate permissions by providing the password for the currently authenticated user. This will create
    an elevated session.

    Args:
        action_type (ElevatePermissionsWithPasswordActionType | Unset):
        body (TotpElevationRestDTO | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorEntity
    """

    return sync_detailed(
        client=client,
        body=body,
        action_type=action_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TotpElevationRestDTO | Unset = UNSET,
    action_type: ElevatePermissionsWithPasswordActionType | Unset = UNSET,
) -> Response[Any | ErrorEntity]:
    """Create elevated session with password

     Elevate permissions by providing the password for the currently authenticated user. This will create
    an elevated session.

    Args:
        action_type (ElevatePermissionsWithPasswordActionType | Unset):
        body (TotpElevationRestDTO | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorEntity]
    """

    kwargs = _get_kwargs(
        body=body,
        action_type=action_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: TotpElevationRestDTO | Unset = UNSET,
    action_type: ElevatePermissionsWithPasswordActionType | Unset = UNSET,
) -> Any | ErrorEntity | None:
    """Create elevated session with password

     Elevate permissions by providing the password for the currently authenticated user. This will create
    an elevated session.

    Args:
        action_type (ElevatePermissionsWithPasswordActionType | Unset):
        body (TotpElevationRestDTO | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorEntity
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            action_type=action_type,
        )
    ).parsed
