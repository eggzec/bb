from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.authentication_response import AuthenticationResponse
from ...models.error_entity import ErrorEntity
from ...models.totp_recovery_code_authentication_dto import TotpRecoveryCodeAuthenticationDTO
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: TotpRecoveryCodeAuthenticationDTO | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/tsv/latest/authenticate/recovery-code",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AuthenticationResponse | ErrorEntity | None:
    if response.status_code == 200:
        response_200 = AuthenticationResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEntity.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorEntity.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AuthenticationResponse | ErrorEntity]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TotpRecoveryCodeAuthenticationDTO | Unset = UNSET,
) -> Response[AuthenticationResponse | ErrorEntity]:
    """Authenticate using recovery code

     Authenticate as the given user using a recovery code.

    Args:
        body (TotpRecoveryCodeAuthenticationDTO | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuthenticationResponse | ErrorEntity]
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
    body: TotpRecoveryCodeAuthenticationDTO | Unset = UNSET,
) -> AuthenticationResponse | ErrorEntity | None:
    """Authenticate using recovery code

     Authenticate as the given user using a recovery code.

    Args:
        body (TotpRecoveryCodeAuthenticationDTO | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuthenticationResponse | ErrorEntity
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TotpRecoveryCodeAuthenticationDTO | Unset = UNSET,
) -> Response[AuthenticationResponse | ErrorEntity]:
    """Authenticate using recovery code

     Authenticate as the given user using a recovery code.

    Args:
        body (TotpRecoveryCodeAuthenticationDTO | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuthenticationResponse | ErrorEntity]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: TotpRecoveryCodeAuthenticationDTO | Unset = UNSET,
) -> AuthenticationResponse | ErrorEntity | None:
    """Authenticate using recovery code

     Authenticate as the given user using a recovery code.

    Args:
        body (TotpRecoveryCodeAuthenticationDTO | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuthenticationResponse | ErrorEntity
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
