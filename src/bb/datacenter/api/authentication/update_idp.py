from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_entity import ErrorEntity
from ...models.idp_config_entity import IdpConfigEntity
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: IdpConfigEntity | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/authconfig/latest/idps/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEntity | IdpConfigEntity | None:
    if response.status_code == 200:
        response_200 = IdpConfigEntity.from_dict(response.json())

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
) -> Response[ErrorEntity | IdpConfigEntity]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: IdpConfigEntity | Unset = UNSET,
) -> Response[ErrorEntity | IdpConfigEntity]:
    """Update IdP configuration

     Updates the configuration for the IdP that matches the given ID.

    Only the provided properties will be applied to the IdP configuration.

    Args:
        id (str):
        body (IdpConfigEntity | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEntity | IdpConfigEntity]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: IdpConfigEntity | Unset = UNSET,
) -> ErrorEntity | IdpConfigEntity | None:
    """Update IdP configuration

     Updates the configuration for the IdP that matches the given ID.

    Only the provided properties will be applied to the IdP configuration.

    Args:
        id (str):
        body (IdpConfigEntity | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEntity | IdpConfigEntity
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: IdpConfigEntity | Unset = UNSET,
) -> Response[ErrorEntity | IdpConfigEntity]:
    """Update IdP configuration

     Updates the configuration for the IdP that matches the given ID.

    Only the provided properties will be applied to the IdP configuration.

    Args:
        id (str):
        body (IdpConfigEntity | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEntity | IdpConfigEntity]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: IdpConfigEntity | Unset = UNSET,
) -> ErrorEntity | IdpConfigEntity | None:
    """Update IdP configuration

     Updates the configuration for the IdP that matches the given ID.

    Only the provided properties will be applied to the IdP configuration.

    Args:
        id (str):
        body (IdpConfigEntity | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEntity | IdpConfigEntity
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
