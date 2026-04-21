from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...deprecation import deprecated_endpoint
from ...models.error import Error
from ...models.issue import Issue
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
    *,
    body: Issue,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/repositories/{workspace}/{repo_slug}/issues".format(
            workspace=quote(str(workspace), safe=""),
            repo_slug=quote(str(repo_slug), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


type ParsedPayload = Error | Issue
type ParseResult = Error | Issue | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 201:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_201 = Issue.from_dict(response.json())

        return response_201

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


@deprecated_endpoint(None)
def sync_detailed(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
    body: Issue,
) -> Response[ParsedPayload]:
    """Create an issue

     Creates a new issue.

    This call requires authentication. Private repositories or private
    issue trackers require the caller to authenticate with an account that
    has appropriate authorization.

    The authenticated user is used for the issue's `reporter` field.

    Args:
        workspace (str):
        repo_slug (str):
        body (Issue):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Issue]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        body=body,
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
    body: Issue,
) -> ParsedPayload | None:
    """Create an issue

     Creates a new issue.

    This call requires authentication. Private repositories or private
    issue trackers require the caller to authenticate with an account that
    has appropriate authorization.

    The authenticated user is used for the issue's `reporter` field.

    Args:
        workspace (str):
        repo_slug (str):
        body (Issue):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Issue
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        client=client,
        body=body,
    ).parsed


@deprecated_endpoint(None)
async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
    body: Issue,
) -> Response[ParsedPayload]:
    """Create an issue

     Creates a new issue.

    This call requires authentication. Private repositories or private
    issue trackers require the caller to authenticate with an account that
    has appropriate authorization.

    The authenticated user is used for the issue's `reporter` field.

    Args:
        workspace (str):
        repo_slug (str):
        body (Issue):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Issue]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated_endpoint(None)
async def asyncio(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
    body: Issue,
) -> ParsedPayload | None:
    """Create an issue

     Creates a new issue.

    This call requires authentication. Private repositories or private
    issue trackers require the caller to authenticate with an account that
    has appropriate authorization.

    The authenticated user is used for the issue's `reporter` field.

    Args:
        workspace (str):
        repo_slug (str):
        body (Issue):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Issue
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            client=client,
            body=body,
        )
    ).parsed
