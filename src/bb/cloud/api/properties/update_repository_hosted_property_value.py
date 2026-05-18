from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.application_property import ApplicationProperty
from ...models.error import Error
from ...types import Response

__all__ = [
    "sync_detailed",
    "asyncio_detailed",
    "sync",
    "asyncio",
]


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    app_key: str,
    property_name: str,
    *,
    body: ApplicationProperty,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/repositories/{workspace}/{repo_slug}/properties/{app_key}/{property_name}".format(
            workspace=quote(str(workspace), safe=""),
            repo_slug=quote(str(repo_slug), safe=""),
            app_key=quote(str(app_key), safe=""),
            property_name=quote(str(property_name), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


type ParsedPayload = Any | Error
type ParseResult = Any | Error | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_403 = Error.from_dict(response.json())

        return response_403

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
    workspace: str,
    repo_slug: str,
    app_key: str,
    property_name: str,
    *,
    client: AuthenticatedClient,
    body: ApplicationProperty,
) -> Response[ParsedPayload]:
    """Update a repository application property

     Update an [application property](/cloud/bitbucket/application-properties/) value stored against a
    repository.

    Args:
        workspace (str):
        repo_slug (str):
        app_key (str):
        property_name (str):
        body (ApplicationProperty): An application property. It is a caller defined JSON object
            that Bitbucket will store and return.
            The `_attributes` field at its top level can be used to control who is allowed to read and
            update the property.
            The keys of the JSON object must match an allowed pattern. For details,
            see [Application properties](/cloud/bitbucket/application-properties/).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        app_key=app_key,
        property_name=property_name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    repo_slug: str,
    app_key: str,
    property_name: str,
    *,
    client: AuthenticatedClient,
    body: ApplicationProperty,
) -> ParsedPayload | None:
    """Update a repository application property

     Update an [application property](/cloud/bitbucket/application-properties/) value stored against a
    repository.

    Args:
        workspace (str):
        repo_slug (str):
        app_key (str):
        property_name (str):
        body (ApplicationProperty): An application property. It is a caller defined JSON object
            that Bitbucket will store and return.
            The `_attributes` field at its top level can be used to control who is allowed to read and
            update the property.
            The keys of the JSON object must match an allowed pattern. For details,
            see [Application properties](/cloud/bitbucket/application-properties/).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        app_key=app_key,
        property_name=property_name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    app_key: str,
    property_name: str,
    *,
    client: AuthenticatedClient,
    body: ApplicationProperty,
) -> Response[ParsedPayload]:
    """Update a repository application property

     Update an [application property](/cloud/bitbucket/application-properties/) value stored against a
    repository.

    Args:
        workspace (str):
        repo_slug (str):
        app_key (str):
        property_name (str):
        body (ApplicationProperty): An application property. It is a caller defined JSON object
            that Bitbucket will store and return.
            The `_attributes` field at its top level can be used to control who is allowed to read and
            update the property.
            The keys of the JSON object must match an allowed pattern. For details,
            see [Application properties](/cloud/bitbucket/application-properties/).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        app_key=app_key,
        property_name=property_name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    app_key: str,
    property_name: str,
    *,
    client: AuthenticatedClient,
    body: ApplicationProperty,
) -> ParsedPayload | None:
    """Update a repository application property

     Update an [application property](/cloud/bitbucket/application-properties/) value stored against a
    repository.

    Args:
        workspace (str):
        repo_slug (str):
        app_key (str):
        property_name (str):
        body (ApplicationProperty): An application property. It is a caller defined JSON object
            that Bitbucket will store and return.
            The `_attributes` field at its top level can be used to control who is allowed to read and
            update the property.
            The keys of the JSON object must match an allowed pattern. For details,
            see [Application properties](/cloud/bitbucket/application-properties/).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            app_key=app_key,
            property_name=property_name,
            client=client,
            body=body,
        )
    ).parsed
