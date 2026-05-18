from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.pipeline_variable import PipelineVariable
from ...types import Response

__all__ = [
    "sync_detailed",
    "asyncio_detailed",
    "sync",
    "asyncio",
]


def _get_kwargs(
    selected_user: str,
    variable_uuid: str,
    *,
    body: PipelineVariable,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/users/{selected_user}/pipelines_config/variables/{variable_uuid}".format(
            selected_user=quote(str(selected_user), safe=""),
            variable_uuid=quote(str(variable_uuid), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


type ParsedPayload = Error | PipelineVariable
type ParseResult = Error | PipelineVariable | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_200 = PipelineVariable.from_dict(response.json())

        return response_200

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

    if response.status_code == 404:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_404 = Error.from_dict(response.json())

        return response_404

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
    variable_uuid: str,
    *,
    client: AuthenticatedClient,
    body: PipelineVariable,
) -> Response[ParsedPayload]:
    """Update a variable for a user

     Update a user level variable.
    This endpoint has been deprecated, and you should use the new workspaces endpoint. For more
    information, see [the announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-
    teams-deprecation/).

    Args:
        selected_user (str):
        variable_uuid (str):
        body (PipelineVariable):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PipelineVariable]
    """

    kwargs = _get_kwargs(
        selected_user=selected_user,
        variable_uuid=variable_uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    selected_user: str,
    variable_uuid: str,
    *,
    client: AuthenticatedClient,
    body: PipelineVariable,
) -> ParsedPayload | None:
    """Update a variable for a user

     Update a user level variable.
    This endpoint has been deprecated, and you should use the new workspaces endpoint. For more
    information, see [the announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-
    teams-deprecation/).

    Args:
        selected_user (str):
        variable_uuid (str):
        body (PipelineVariable):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PipelineVariable
    """

    return sync_detailed(
        selected_user=selected_user,
        variable_uuid=variable_uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    selected_user: str,
    variable_uuid: str,
    *,
    client: AuthenticatedClient,
    body: PipelineVariable,
) -> Response[ParsedPayload]:
    """Update a variable for a user

     Update a user level variable.
    This endpoint has been deprecated, and you should use the new workspaces endpoint. For more
    information, see [the announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-
    teams-deprecation/).

    Args:
        selected_user (str):
        variable_uuid (str):
        body (PipelineVariable):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PipelineVariable]
    """

    kwargs = _get_kwargs(
        selected_user=selected_user,
        variable_uuid=variable_uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    selected_user: str,
    variable_uuid: str,
    *,
    client: AuthenticatedClient,
    body: PipelineVariable,
) -> ParsedPayload | None:
    """Update a variable for a user

     Update a user level variable.
    This endpoint has been deprecated, and you should use the new workspaces endpoint. For more
    information, see [the announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-
    teams-deprecation/).

    Args:
        selected_user (str):
        variable_uuid (str):
        body (PipelineVariable):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PipelineVariable
    """

    return (
        await asyncio_detailed(
            selected_user=selected_user,
            variable_uuid=variable_uuid,
            client=client,
            body=body,
        )
    ).parsed
