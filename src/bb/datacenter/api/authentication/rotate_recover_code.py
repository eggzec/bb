from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.elevation_method_rest_dto import ElevationMethodRestDTO
from ...models.error_entity import ErrorEntity
from ...models.totp_recovery_code_dto import TotpRecoveryCodeDTO
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/tsv/latest/totp/recovery-code/rotate",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ElevationMethodRestDTO | ErrorEntity | TotpRecoveryCodeDTO | None:
    if response.status_code == 200:
        response_200 = TotpRecoveryCodeDTO.from_dict(response.json())

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
) -> Response[ElevationMethodRestDTO | ErrorEntity | TotpRecoveryCodeDTO]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[ElevationMethodRestDTO | ErrorEntity | TotpRecoveryCodeDTO]:
    """Rotate recovery code

     Rotates the recovery code for the currently authentication user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ElevationMethodRestDTO | ErrorEntity | TotpRecoveryCodeDTO]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> ElevationMethodRestDTO | ErrorEntity | TotpRecoveryCodeDTO | None:
    """Rotate recovery code

     Rotates the recovery code for the currently authentication user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ElevationMethodRestDTO | ErrorEntity | TotpRecoveryCodeDTO
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[ElevationMethodRestDTO | ErrorEntity | TotpRecoveryCodeDTO]:
    """Rotate recovery code

     Rotates the recovery code for the currently authentication user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ElevationMethodRestDTO | ErrorEntity | TotpRecoveryCodeDTO]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> ElevationMethodRestDTO | ErrorEntity | TotpRecoveryCodeDTO | None:
    """Rotate recovery code

     Rotates the recovery code for the currently authentication user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ElevationMethodRestDTO | ErrorEntity | TotpRecoveryCodeDTO
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
