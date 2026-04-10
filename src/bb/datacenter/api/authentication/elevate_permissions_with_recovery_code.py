from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.elevate_permissions_with_recovery_code_action_type import ElevatePermissionsWithRecoveryCodeActionType
from ...models.error_entity import ErrorEntity
from ...models.totp_recovery_code_dto import TotpRecoveryCodeDTO
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: TotpRecoveryCodeDTO | Unset = UNSET,
    action_type: ElevatePermissionsWithRecoveryCodeActionType | Unset = UNSET,
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
        "url": "/tsv/latest/elevate-permissions/recovery-code",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorEntity | TotpRecoveryCodeDTO | None:
    if response.status_code == 200:
        response_200 = TotpRecoveryCodeDTO.from_dict(response.json())

        return response_200

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


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ErrorEntity | TotpRecoveryCodeDTO]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TotpRecoveryCodeDTO | Unset = UNSET,
    action_type: ElevatePermissionsWithRecoveryCodeActionType | Unset = UNSET,
) -> Response[Any | ErrorEntity | TotpRecoveryCodeDTO]:
    """Create elevated session with recovery code

     Elevate permissions by providing a recovery code for the currently authenticated user. This will
    create an elevated session.

    Args:
        action_type (ElevatePermissionsWithRecoveryCodeActionType | Unset):
        body (TotpRecoveryCodeDTO | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorEntity | TotpRecoveryCodeDTO]
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
    body: TotpRecoveryCodeDTO | Unset = UNSET,
    action_type: ElevatePermissionsWithRecoveryCodeActionType | Unset = UNSET,
) -> Any | ErrorEntity | TotpRecoveryCodeDTO | None:
    """Create elevated session with recovery code

     Elevate permissions by providing a recovery code for the currently authenticated user. This will
    create an elevated session.

    Args:
        action_type (ElevatePermissionsWithRecoveryCodeActionType | Unset):
        body (TotpRecoveryCodeDTO | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorEntity | TotpRecoveryCodeDTO
    """

    return sync_detailed(
        client=client,
        body=body,
        action_type=action_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TotpRecoveryCodeDTO | Unset = UNSET,
    action_type: ElevatePermissionsWithRecoveryCodeActionType | Unset = UNSET,
) -> Response[Any | ErrorEntity | TotpRecoveryCodeDTO]:
    """Create elevated session with recovery code

     Elevate permissions by providing a recovery code for the currently authenticated user. This will
    create an elevated session.

    Args:
        action_type (ElevatePermissionsWithRecoveryCodeActionType | Unset):
        body (TotpRecoveryCodeDTO | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorEntity | TotpRecoveryCodeDTO]
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
    body: TotpRecoveryCodeDTO | Unset = UNSET,
    action_type: ElevatePermissionsWithRecoveryCodeActionType | Unset = UNSET,
) -> Any | ErrorEntity | TotpRecoveryCodeDTO | None:
    """Create elevated session with recovery code

     Elevate permissions by providing a recovery code for the currently authenticated user. This will
    create an elevated session.

    Args:
        action_type (ElevatePermissionsWithRecoveryCodeActionType | Unset):
        body (TotpRecoveryCodeDTO | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorEntity | TotpRecoveryCodeDTO
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            action_type=action_type,
        )
    ).parsed
