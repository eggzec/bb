from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_entity import ErrorEntity
from ...models.sso_config_entity import SsoConfigEntity
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SsoConfigEntity | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/authconfig/latest/sso",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEntity | SsoConfigEntity | None:
    if response.status_code == 200:
        response_200 = SsoConfigEntity.from_dict(response.json())

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
) -> Response[ErrorEntity | SsoConfigEntity]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SsoConfigEntity | Unset = UNSET,
) -> Response[ErrorEntity | SsoConfigEntity]:
    """Update SSO configuration

     Update the SSO configuration.

    Args:
        body (SsoConfigEntity | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEntity | SsoConfigEntity]
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
    body: SsoConfigEntity | Unset = UNSET,
) -> ErrorEntity | SsoConfigEntity | None:
    """Update SSO configuration

     Update the SSO configuration.

    Args:
        body (SsoConfigEntity | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEntity | SsoConfigEntity
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SsoConfigEntity | Unset = UNSET,
) -> Response[ErrorEntity | SsoConfigEntity]:
    """Update SSO configuration

     Update the SSO configuration.

    Args:
        body (SsoConfigEntity | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEntity | SsoConfigEntity]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SsoConfigEntity | Unset = UNSET,
) -> ErrorEntity | SsoConfigEntity | None:
    """Update SSO configuration

     Update the SSO configuration.

    Args:
        body (SsoConfigEntity | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEntity | SsoConfigEntity
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
