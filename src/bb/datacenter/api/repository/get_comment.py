from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_comment_response_401 import GetCommentResponse401
from ...models.get_comment_response_404 import GetCommentResponse404
from ...models.rest_comment import RestComment
from ...types import Response


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    comment_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/commits/{commit_id}/comments/{comment_id}".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            commit_id=quote(str(commit_id), safe=""),
            comment_id=quote(str(comment_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetCommentResponse401 | GetCommentResponse404 | RestComment | None:
    if response.status_code == 200:
        response_200 = RestComment.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetCommentResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetCommentResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetCommentResponse401 | GetCommentResponse404 | RestComment]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    comment_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetCommentResponse401 | GetCommentResponse404 | RestComment]:
    """Get a commit comment

     Retrieves a commit discussion comment.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that the
    commit is in to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        comment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCommentResponse401 | GetCommentResponse404 | RestComment]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        comment_id=comment_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    comment_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetCommentResponse401 | GetCommentResponse404 | RestComment | None:
    """Get a commit comment

     Retrieves a commit discussion comment.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that the
    commit is in to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        comment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCommentResponse401 | GetCommentResponse404 | RestComment
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        comment_id=comment_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    comment_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetCommentResponse401 | GetCommentResponse404 | RestComment]:
    """Get a commit comment

     Retrieves a commit discussion comment.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that the
    commit is in to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        comment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCommentResponse401 | GetCommentResponse404 | RestComment]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        comment_id=comment_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    comment_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetCommentResponse401 | GetCommentResponse404 | RestComment | None:
    """Get a commit comment

     Retrieves a commit discussion comment.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that the
    commit is in to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        comment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCommentResponse401 | GetCommentResponse404 | RestComment
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            commit_id=commit_id,
            comment_id=comment_id,
            client=client,
        )
    ).parsed
