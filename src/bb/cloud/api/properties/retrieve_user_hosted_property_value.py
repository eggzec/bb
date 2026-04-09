from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.application_property import ApplicationProperty
from ...types import Response

__all__ = [
    "sync_detailed",
    "asyncio_detailed",
    "sync",
    "asyncio",
]


def _get_kwargs(
    selected_user: str,
    app_key: str,
    property_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users/{selected_user}/properties/{app_key}/{property_name}".format(
            selected_user=quote(str(selected_user), safe=""),
            app_key=quote(str(app_key), safe=""),
            property_name=quote(str(property_name), safe=""),
        ),
    }

    return _kwargs


type ParsedPayload = ApplicationProperty
type ParseResult = ApplicationProperty | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        response_200 = ApplicationProperty.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ParsedPayload]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    selected_user: str,
    app_key: str,
    property_name: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """Get a user application property

     Retrieve an [application property](/cloud/bitbucket/application-properties/) value stored against a
    user.

    Args:
        selected_user (str):
        app_key (str):
        property_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApplicationProperty]
    """

    kwargs = _get_kwargs(
        selected_user=selected_user,
        app_key=app_key,
        property_name=property_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    selected_user: str,
    app_key: str,
    property_name: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    """Get a user application property

     Retrieve an [application property](/cloud/bitbucket/application-properties/) value stored against a
    user.

    Args:
        selected_user (str):
        app_key (str):
        property_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApplicationProperty
    """

    return sync_detailed(
        selected_user=selected_user,
        app_key=app_key,
        property_name=property_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    selected_user: str,
    app_key: str,
    property_name: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """Get a user application property

     Retrieve an [application property](/cloud/bitbucket/application-properties/) value stored against a
    user.

    Args:
        selected_user (str):
        app_key (str):
        property_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApplicationProperty]
    """

    kwargs = _get_kwargs(
        selected_user=selected_user,
        app_key=app_key,
        property_name=property_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    selected_user: str,
    app_key: str,
    property_name: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    """Get a user application property

     Retrieve an [application property](/cloud/bitbucket/application-properties/) value stored against a
    user.

    Args:
        selected_user (str):
        app_key (str):
        property_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApplicationProperty
    """

    return (
        await asyncio_detailed(
            selected_user=selected_user,
            app_key=app_key,
            property_name=property_name,
            client=client,
        )
    ).parsed
