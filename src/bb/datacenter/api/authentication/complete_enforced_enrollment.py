from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_entity import ErrorEntity
from ...models.totp_code_verification_dto import TotpCodeVerificationDTO
from ...models.totp_recovery_code_dto import TotpRecoveryCodeDTO
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: TotpCodeVerificationDTO | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/tsv/latest/totp/complete-enforced-enrollment",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEntity | TotpRecoveryCodeDTO | None:
    if response.status_code == 200:
        response_200 = TotpRecoveryCodeDTO.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEntity.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEntity | TotpRecoveryCodeDTO]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TotpCodeVerificationDTO | Unset = UNSET,
) -> Response[ErrorEntity | TotpRecoveryCodeDTO]:
    """Complete enforced enrollment in 2SV

     Complete enforced enrollment in two-step verification by verifying the provided TOTP code and
    creating a new session for the given user.

    Args:
        body (TotpCodeVerificationDTO | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEntity | TotpRecoveryCodeDTO]
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
    body: TotpCodeVerificationDTO | Unset = UNSET,
) -> ErrorEntity | TotpRecoveryCodeDTO | None:
    """Complete enforced enrollment in 2SV

     Complete enforced enrollment in two-step verification by verifying the provided TOTP code and
    creating a new session for the given user.

    Args:
        body (TotpCodeVerificationDTO | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEntity | TotpRecoveryCodeDTO
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TotpCodeVerificationDTO | Unset = UNSET,
) -> Response[ErrorEntity | TotpRecoveryCodeDTO]:
    """Complete enforced enrollment in 2SV

     Complete enforced enrollment in two-step verification by verifying the provided TOTP code and
    creating a new session for the given user.

    Args:
        body (TotpCodeVerificationDTO | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEntity | TotpRecoveryCodeDTO]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: TotpCodeVerificationDTO | Unset = UNSET,
) -> ErrorEntity | TotpRecoveryCodeDTO | None:
    """Complete enforced enrollment in 2SV

     Complete enforced enrollment in two-step verification by verifying the provided TOTP code and
    creating a new session for the given user.

    Args:
        body (TotpCodeVerificationDTO | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEntity | TotpRecoveryCodeDTO
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
