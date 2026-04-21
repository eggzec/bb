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
    workspace: str,
    variable_uuid: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/workspaces/{workspace}/pipelines-config/variables/{variable_uuid}".format(
            workspace=quote(str(workspace), safe=""),
            variable_uuid=quote(str(variable_uuid), safe=""),
        ),
    }

    return _kwargs


type ParsedPayload = Error | PipelineVariable
type ParseResult = Error | PipelineVariable | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_200 = PipelineVariable.from_dict(response.json())

        return response_200

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
    workspace: str,
    variable_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """Get variable for a workspace

     Retrieve a workspace level variable.

    Args:
        workspace (str):
        variable_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PipelineVariable]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        variable_uuid=variable_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    variable_uuid: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    """Get variable for a workspace

     Retrieve a workspace level variable.

    Args:
        workspace (str):
        variable_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PipelineVariable
    """

    return sync_detailed(
        workspace=workspace,
        variable_uuid=variable_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    variable_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """Get variable for a workspace

     Retrieve a workspace level variable.

    Args:
        workspace (str):
        variable_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PipelineVariable]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        variable_uuid=variable_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    variable_uuid: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    """Get variable for a workspace

     Retrieve a workspace level variable.

    Args:
        workspace (str):
        variable_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PipelineVariable
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            variable_uuid=variable_uuid,
            client=client,
        )
    ).parsed
