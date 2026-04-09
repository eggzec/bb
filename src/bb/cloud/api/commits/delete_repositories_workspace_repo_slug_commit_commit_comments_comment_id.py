from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response

__all__ = [
    "sync_detailed",
    "asyncio_detailed",
]


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    commit: str,
    comment_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/repositories/{workspace}/{repo_slug}/commit/{commit}/comments/{comment_id}".format(
            workspace=quote(str(workspace), safe=""),
            repo_slug=quote(str(repo_slug), safe=""),
            commit=quote(str(commit), safe=""),
            comment_id=quote(str(comment_id), safe=""),
        ),
    }

    return _kwargs


type ParsedPayload = Any
type ParseResult = Any | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 204:
        return None

    if response.status_code == 404:
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
    commit: str,
    comment_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """Delete a commit comment

     Deletes the specified commit comment.

    Note that deleting comments that have visible replies that point to
    them will not really delete the resource. This is to retain the integrity
    of the original comment tree. Instead, the `deleted` element is set to
    `true` and the content is blanked out. The comment will continue to be
    returned by the collections and self endpoints.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        comment_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        commit=commit,
        comment_id=comment_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    commit: str,
    comment_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """Delete a commit comment

     Deletes the specified commit comment.

    Note that deleting comments that have visible replies that point to
    them will not really delete the resource. This is to retain the integrity
    of the original comment tree. Instead, the `deleted` element is set to
    `true` and the content is blanked out. The comment will continue to be
    returned by the collections and self endpoints.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        comment_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        commit=commit,
        comment_id=comment_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
