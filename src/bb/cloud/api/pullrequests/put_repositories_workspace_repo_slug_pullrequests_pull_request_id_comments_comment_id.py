from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.pullrequest_comment import PullrequestComment
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
    pull_request_id: int,
    comment_id: int,
    *,
    body: PullrequestComment,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments/{comment_id}".format(
            workspace=quote(str(workspace), safe=""),
            repo_slug=quote(str(repo_slug), safe=""),
            pull_request_id=quote(str(pull_request_id), safe=""),
            comment_id=quote(str(comment_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


type ParsedPayload = Error | PullrequestComment
type ParseResult = Error | PullrequestComment | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_200 = PullrequestComment.from_dict(response.json())

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
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    comment_id: int,
    *,
    client: AuthenticatedClient,
    body: PullrequestComment,
) -> Response[ParsedPayload]:
    """Update a comment on a pull request

     Updates a specific pull request comment.

    Args:
        workspace (str):
        repo_slug (str):
        pull_request_id (int):
        comment_id (int):
        body (PullrequestComment):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PullrequestComment]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        pull_request_id=pull_request_id,
        comment_id=comment_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    comment_id: int,
    *,
    client: AuthenticatedClient,
    body: PullrequestComment,
) -> ParsedPayload | None:
    """Update a comment on a pull request

     Updates a specific pull request comment.

    Args:
        workspace (str):
        repo_slug (str):
        pull_request_id (int):
        comment_id (int):
        body (PullrequestComment):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PullrequestComment
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        pull_request_id=pull_request_id,
        comment_id=comment_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    comment_id: int,
    *,
    client: AuthenticatedClient,
    body: PullrequestComment,
) -> Response[ParsedPayload]:
    """Update a comment on a pull request

     Updates a specific pull request comment.

    Args:
        workspace (str):
        repo_slug (str):
        pull_request_id (int):
        comment_id (int):
        body (PullrequestComment):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PullrequestComment]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        pull_request_id=pull_request_id,
        comment_id=comment_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    comment_id: int,
    *,
    client: AuthenticatedClient,
    body: PullrequestComment,
) -> ParsedPayload | None:
    """Update a comment on a pull request

     Updates a specific pull request comment.

    Args:
        workspace (str):
        repo_slug (str):
        pull_request_id (int):
        comment_id (int):
        body (PullrequestComment):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PullrequestComment
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            pull_request_id=pull_request_id,
            comment_id=comment_id,
            client=client,
            body=body,
        )
    ).parsed
