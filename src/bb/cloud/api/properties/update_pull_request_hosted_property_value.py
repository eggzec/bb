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
]


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    pullrequest_id: str,
    app_key: str,
    property_name: str,
    *,
    body: ApplicationProperty,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/repositories/{workspace}/{repo_slug}/pullrequests/{pullrequest_id}/properties/{app_key}/{property_name}".format(
            workspace=quote(str(workspace), safe=""),
            repo_slug=quote(str(repo_slug), safe=""),
            pullrequest_id=quote(str(pullrequest_id), safe=""),
            app_key=quote(str(app_key), safe=""),
            property_name=quote(str(property_name), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


type ParsedPayload = Any
type ParseResult = Any | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 204:
        return None

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
    pullrequest_id: str,
    app_key: str,
    property_name: str,
    *,
    client: AuthenticatedClient,
    body: ApplicationProperty,
) -> Response[ParsedPayload]:
    """Update a pull request application property

     Update an [application property](/cloud/bitbucket/application-properties/) value stored against a
    pull request.

    Args:
        workspace (str):
        repo_slug (str):
        pullrequest_id (str):
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
        Response[Any]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        pullrequest_id=pullrequest_id,
        app_key=app_key,
        property_name=property_name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    pullrequest_id: str,
    app_key: str,
    property_name: str,
    *,
    client: AuthenticatedClient,
    body: ApplicationProperty,
) -> Response[ParsedPayload]:
    """Update a pull request application property

     Update an [application property](/cloud/bitbucket/application-properties/) value stored against a
    pull request.

    Args:
        workspace (str):
        repo_slug (str):
        pullrequest_id (str):
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
        Response[Any]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        pullrequest_id=pullrequest_id,
        app_key=app_key,
        property_name=property_name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
