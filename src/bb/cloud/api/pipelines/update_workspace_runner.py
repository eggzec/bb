from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.pipeline_runner import PipelineRunner
from ...types import Response

__all__ = [
    "sync_detailed",
    "asyncio_detailed",
    "sync",
    "asyncio",
]


def _get_kwargs(
    workspace: str,
    runner_uuid: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/workspaces/{workspace}/pipelines-config/runners/{runner_uuid}".format(
            workspace=quote(str(workspace), safe=""),
            runner_uuid=quote(str(runner_uuid), safe=""),
        ),
    }

    return _kwargs


type ParsedPayload = Error | PipelineRunner
type ParseResult = Error | PipelineRunner | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_200 = PipelineRunner.from_dict(response.json())

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
    runner_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """Update workspace runner

     Update workspace runner.

    Args:
        workspace (str):
        runner_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PipelineRunner]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        runner_uuid=runner_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    runner_uuid: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    """Update workspace runner

     Update workspace runner.

    Args:
        workspace (str):
        runner_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PipelineRunner
    """

    return sync_detailed(
        workspace=workspace,
        runner_uuid=runner_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    runner_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """Update workspace runner

     Update workspace runner.

    Args:
        workspace (str):
        runner_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PipelineRunner]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        runner_uuid=runner_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    runner_uuid: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    """Update workspace runner

     Update workspace runner.

    Args:
        workspace (str):
        runner_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PipelineRunner
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            runner_uuid=runner_uuid,
            client=client,
        )
    ).parsed
