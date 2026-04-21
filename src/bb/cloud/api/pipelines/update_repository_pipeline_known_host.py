from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.pipeline_known_host import PipelineKnownHost
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
    known_host_uuid: str,
    *,
    body: PipelineKnownHost,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/repositories/{workspace}/{repo_slug}/pipelines_config/ssh/known_hosts/{known_host_uuid}".format(
            workspace=quote(str(workspace), safe=""),
            repo_slug=quote(str(repo_slug), safe=""),
            known_host_uuid=quote(str(known_host_uuid), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


type ParsedPayload = Error | PipelineKnownHost
type ParseResult = Error | PipelineKnownHost | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_200 = PipelineKnownHost.from_dict(response.json())

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
    repo_slug: str,
    known_host_uuid: str,
    *,
    client: AuthenticatedClient,
    body: PipelineKnownHost,
) -> Response[ParsedPayload]:
    """Update a known host

     Update a repository level known host.

    Args:
        workspace (str):
        repo_slug (str):
        known_host_uuid (str):
        body (PipelineKnownHost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PipelineKnownHost]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        known_host_uuid=known_host_uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    repo_slug: str,
    known_host_uuid: str,
    *,
    client: AuthenticatedClient,
    body: PipelineKnownHost,
) -> ParsedPayload | None:
    """Update a known host

     Update a repository level known host.

    Args:
        workspace (str):
        repo_slug (str):
        known_host_uuid (str):
        body (PipelineKnownHost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PipelineKnownHost
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        known_host_uuid=known_host_uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    known_host_uuid: str,
    *,
    client: AuthenticatedClient,
    body: PipelineKnownHost,
) -> Response[ParsedPayload]:
    """Update a known host

     Update a repository level known host.

    Args:
        workspace (str):
        repo_slug (str):
        known_host_uuid (str):
        body (PipelineKnownHost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PipelineKnownHost]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        known_host_uuid=known_host_uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    known_host_uuid: str,
    *,
    client: AuthenticatedClient,
    body: PipelineKnownHost,
) -> ParsedPayload | None:
    """Update a known host

     Update a repository level known host.

    Args:
        workspace (str):
        repo_slug (str):
        known_host_uuid (str):
        body (PipelineKnownHost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PipelineKnownHost
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            known_host_uuid=known_host_uuid,
            client=client,
            body=body,
        )
    ).parsed
