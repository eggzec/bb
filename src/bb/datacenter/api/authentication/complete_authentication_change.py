from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.elevation_method_rest_dto import ElevationMethodRestDTO
from ...models.error_entity import ErrorEntity
from ...models.totp_code_verification_dto import TotpCodeVerificationDTO
from ...models.totp_user_enrollment_dto import TotpUserEnrollmentDTO
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: TotpCodeVerificationDTO | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/tsv/latest/totp/complete-enrollment-update",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ElevationMethodRestDTO | ErrorEntity | TotpUserEnrollmentDTO | None:
    if response.status_code == 200:
        response_200 = TotpUserEnrollmentDTO.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEntity.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ElevationMethodRestDTO.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ElevationMethodRestDTO | ErrorEntity | TotpUserEnrollmentDTO]:
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
) -> Response[ElevationMethodRestDTO | ErrorEntity | TotpUserEnrollmentDTO]:
    """Complete authentication app update for 2SV

     Complete update of the authentication app used for two-step verification by verifying the provided
    TOTP code.

    Args:
        body (TotpCodeVerificationDTO | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ElevationMethodRestDTO | ErrorEntity | TotpUserEnrollmentDTO]
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
) -> ElevationMethodRestDTO | ErrorEntity | TotpUserEnrollmentDTO | None:
    """Complete authentication app update for 2SV

     Complete update of the authentication app used for two-step verification by verifying the provided
    TOTP code.

    Args:
        body (TotpCodeVerificationDTO | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ElevationMethodRestDTO | ErrorEntity | TotpUserEnrollmentDTO
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TotpCodeVerificationDTO | Unset = UNSET,
) -> Response[ElevationMethodRestDTO | ErrorEntity | TotpUserEnrollmentDTO]:
    """Complete authentication app update for 2SV

     Complete update of the authentication app used for two-step verification by verifying the provided
    TOTP code.

    Args:
        body (TotpCodeVerificationDTO | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ElevationMethodRestDTO | ErrorEntity | TotpUserEnrollmentDTO]
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
) -> ElevationMethodRestDTO | ErrorEntity | TotpUserEnrollmentDTO | None:
    """Complete authentication app update for 2SV

     Complete update of the authentication app used for two-step verification by verifying the provided
    TOTP code.

    Args:
        body (TotpCodeVerificationDTO | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ElevationMethodRestDTO | ErrorEntity | TotpUserEnrollmentDTO
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
