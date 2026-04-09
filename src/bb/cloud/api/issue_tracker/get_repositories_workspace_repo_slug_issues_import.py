from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...deprecation import deprecated_endpoint
from ...models.error import Error
from ...models.issue_job_status import IssueJobStatus
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
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/repositories/{workspace}/{repo_slug}/issues/import".format(
            workspace=quote(str(workspace), safe=""),
            repo_slug=quote(str(repo_slug), safe=""),
        ),
    }

    return _kwargs


type ParsedPayload = Error | IssueJobStatus
type ParseResult = Error | IssueJobStatus | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        response_200 = IssueJobStatus.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = IssueJobStatus.from_dict(response.json())

        return response_202

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 404:
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


@deprecated_endpoint(None)
def sync_detailed(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """Check issue import status

     When using GET, this endpoint reports the status of the current import task.

    After the job has been scheduled, but before it starts executing, the endpoint
    returns a 202 response with status `ACCEPTED`.

    Once it starts running, it is a 202 response with status `STARTED` and progress filled.

    After it is finished, it becomes a 200 response with status `SUCCESS` or `FAILURE`.

    Args:
        workspace (str):
        repo_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | IssueJobStatus]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated_endpoint(None)
def sync(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    """Check issue import status

     When using GET, this endpoint reports the status of the current import task.

    After the job has been scheduled, but before it starts executing, the endpoint
    returns a 202 response with status `ACCEPTED`.

    Once it starts running, it is a 202 response with status `STARTED` and progress filled.

    After it is finished, it becomes a 200 response with status `SUCCESS` or `FAILURE`.

    Args:
        workspace (str):
        repo_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | IssueJobStatus
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        client=client,
    ).parsed


@deprecated_endpoint(None)
async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """Check issue import status

     When using GET, this endpoint reports the status of the current import task.

    After the job has been scheduled, but before it starts executing, the endpoint
    returns a 202 response with status `ACCEPTED`.

    Once it starts running, it is a 202 response with status `STARTED` and progress filled.

    After it is finished, it becomes a 200 response with status `SUCCESS` or `FAILURE`.

    Args:
        workspace (str):
        repo_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | IssueJobStatus]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated_endpoint(None)
async def asyncio(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    """Check issue import status

     When using GET, this endpoint reports the status of the current import task.

    After the job has been scheduled, but before it starts executing, the endpoint
    returns a 202 response with status `ACCEPTED`.

    Once it starts running, it is a 202 response with status `STARTED` and progress filled.

    After it is finished, it becomes a 200 response with status `SUCCESS` or `FAILURE`.

    Args:
        workspace (str):
        repo_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | IssueJobStatus
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            client=client,
        )
    ).parsed
