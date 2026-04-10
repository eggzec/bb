from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.authentication_entity import AuthenticationEntity
from ...models.authentication_response import AuthenticationResponse
from ...models.credentials_check_failed_dto import CredentialsCheckFailedDTO
from ...models.next_login_step_dto import NextLoginStepDTO
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: AuthenticationEntity | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/tsv/latest/authenticate",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AuthenticationResponse | CredentialsCheckFailedDTO | NextLoginStepDTO | None:
    if response.status_code == 200:
        response_200 = AuthenticationResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = CredentialsCheckFailedDTO.from_dict(response.json())

        return response_401

    if response.status_code == 412:
        response_412 = NextLoginStepDTO.from_dict(response.json())

        return response_412

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AuthenticationResponse | CredentialsCheckFailedDTO | NextLoginStepDTO]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AuthenticationEntity | Unset = UNSET,
) -> Response[AuthenticationResponse | CredentialsCheckFailedDTO | NextLoginStepDTO]:
    """Authenticate with 2SV

     Authenticates as the given user. This endpoint <strong>may</strong>:

    - Ask for two-step verification if the user has enrolled; or
    - Enforce enrollment in two-step verification if two-step verification enforcement is configured for
    the instance and the user is not yet enrolled.

    Args:
        body (AuthenticationEntity | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuthenticationResponse | CredentialsCheckFailedDTO | NextLoginStepDTO]
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
    body: AuthenticationEntity | Unset = UNSET,
) -> AuthenticationResponse | CredentialsCheckFailedDTO | NextLoginStepDTO | None:
    """Authenticate with 2SV

     Authenticates as the given user. This endpoint <strong>may</strong>:

    - Ask for two-step verification if the user has enrolled; or
    - Enforce enrollment in two-step verification if two-step verification enforcement is configured for
    the instance and the user is not yet enrolled.

    Args:
        body (AuthenticationEntity | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuthenticationResponse | CredentialsCheckFailedDTO | NextLoginStepDTO
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AuthenticationEntity | Unset = UNSET,
) -> Response[AuthenticationResponse | CredentialsCheckFailedDTO | NextLoginStepDTO]:
    """Authenticate with 2SV

     Authenticates as the given user. This endpoint <strong>may</strong>:

    - Ask for two-step verification if the user has enrolled; or
    - Enforce enrollment in two-step verification if two-step verification enforcement is configured for
    the instance and the user is not yet enrolled.

    Args:
        body (AuthenticationEntity | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuthenticationResponse | CredentialsCheckFailedDTO | NextLoginStepDTO]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: AuthenticationEntity | Unset = UNSET,
) -> AuthenticationResponse | CredentialsCheckFailedDTO | NextLoginStepDTO | None:
    """Authenticate with 2SV

     Authenticates as the given user. This endpoint <strong>may</strong>:

    - Ask for two-step verification if the user has enrolled; or
    - Enforce enrollment in two-step verification if two-step verification enforcement is configured for
    the instance and the user is not yet enrolled.

    Args:
        body (AuthenticationEntity | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuthenticationResponse | CredentialsCheckFailedDTO | NextLoginStepDTO
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
