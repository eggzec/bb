from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_csp_settings import RestCspSettings
from ...models.settings_response_401 import SettingsResponse401
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RestCspSettings | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/csp/latest/settings",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | SettingsResponse401 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = SettingsResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | SettingsResponse401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RestCspSettings | Unset = UNSET,
) -> Response[Any | SettingsResponse401]:
    r"""Change CSP strictness setting

     Change the Content-Security-Policy header that is returned on all Bitbucket responses between
    \"Content-Security-Policy\" and \"Content-Security-Policy-Report-Only\".

    Args:
        body (RestCspSettings | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SettingsResponse401]
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
    body: RestCspSettings | Unset = UNSET,
) -> Any | SettingsResponse401 | None:
    r"""Change CSP strictness setting

     Change the Content-Security-Policy header that is returned on all Bitbucket responses between
    \"Content-Security-Policy\" and \"Content-Security-Policy-Report-Only\".

    Args:
        body (RestCspSettings | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SettingsResponse401
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RestCspSettings | Unset = UNSET,
) -> Response[Any | SettingsResponse401]:
    r"""Change CSP strictness setting

     Change the Content-Security-Policy header that is returned on all Bitbucket responses between
    \"Content-Security-Policy\" and \"Content-Security-Policy-Report-Only\".

    Args:
        body (RestCspSettings | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SettingsResponse401]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RestCspSettings | Unset = UNSET,
) -> Any | SettingsResponse401 | None:
    r"""Change CSP strictness setting

     Change the Content-Security-Policy header that is returned on all Bitbucket responses between
    \"Content-Security-Policy\" and \"Content-Security-Policy-Report-Only\".

    Args:
        body (RestCspSettings | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SettingsResponse401
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
