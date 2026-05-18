from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
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
    pipeline_uuid: str,
    step_uuid: str,
    log_uuid: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/logs/{log_uuid}".format(
            workspace=quote(str(workspace), safe=""),
            repo_slug=quote(str(repo_slug), safe=""),
            pipeline_uuid=quote(str(pipeline_uuid), safe=""),
            step_uuid=quote(str(step_uuid), safe=""),
            log_uuid=quote(str(log_uuid), safe=""),
        ),
    }

    return _kwargs


type ParsedPayload = Any | Error
type ParseResult = Any | Error | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 307:
        response_307 = cast(Any, None)
        return response_307

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
        response_404 = Error.from_dict(response.content)

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
    pipeline_uuid: str,
    step_uuid: str,
    log_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """Get the logs for the build container or a service container for a given step of a pipeline.

     Retrieve the log file for a build container or service container.

    This endpoint supports (and encourages!) the use of [HTTP Range
    requests](https://tools.ietf.org/html/rfc7233) to deal with potentially very large log files.

    Args:
        workspace (str):
        repo_slug (str):
        pipeline_uuid (str):
        step_uuid (str):
        log_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        pipeline_uuid=pipeline_uuid,
        step_uuid=step_uuid,
        log_uuid=log_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    repo_slug: str,
    pipeline_uuid: str,
    step_uuid: str,
    log_uuid: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    """Get the logs for the build container or a service container for a given step of a pipeline.

     Retrieve the log file for a build container or service container.

    This endpoint supports (and encourages!) the use of [HTTP Range
    requests](https://tools.ietf.org/html/rfc7233) to deal with potentially very large log files.

    Args:
        workspace (str):
        repo_slug (str):
        pipeline_uuid (str):
        step_uuid (str):
        log_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        pipeline_uuid=pipeline_uuid,
        step_uuid=step_uuid,
        log_uuid=log_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    pipeline_uuid: str,
    step_uuid: str,
    log_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """Get the logs for the build container or a service container for a given step of a pipeline.

     Retrieve the log file for a build container or service container.

    This endpoint supports (and encourages!) the use of [HTTP Range
    requests](https://tools.ietf.org/html/rfc7233) to deal with potentially very large log files.

    Args:
        workspace (str):
        repo_slug (str):
        pipeline_uuid (str):
        step_uuid (str):
        log_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        pipeline_uuid=pipeline_uuid,
        step_uuid=step_uuid,
        log_uuid=log_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    pipeline_uuid: str,
    step_uuid: str,
    log_uuid: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    """Get the logs for the build container or a service container for a given step of a pipeline.

     Retrieve the log file for a build container or service container.

    This endpoint supports (and encourages!) the use of [HTTP Range
    requests](https://tools.ietf.org/html/rfc7233) to deal with potentially very large log files.

    Args:
        workspace (str):
        repo_slug (str):
        pipeline_uuid (str):
        step_uuid (str):
        log_uuid (str):

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
            pipeline_uuid=pipeline_uuid,
            step_uuid=step_uuid,
            log_uuid=log_uuid,
            client=client,
        )
    ).parsed
