from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_comment_response_401 import DeleteCommentResponse401
from ...models.delete_comment_response_404 import DeleteCommentResponse404
from ...models.delete_comment_response_409 import DeleteCommentResponse409
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    comment_id: str,
    *,
    version: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["version"] = version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/commits/{commit_id}/comments/{comment_id}".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            commit_id=quote(str(commit_id), safe=""),
            comment_id=quote(str(comment_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteCommentResponse401 | DeleteCommentResponse404 | DeleteCommentResponse409 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = DeleteCommentResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = DeleteCommentResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = DeleteCommentResponse409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteCommentResponse401 | DeleteCommentResponse404 | DeleteCommentResponse409]:
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
    version: str | Unset = UNSET,
) -> Response[Any | DeleteCommentResponse401 | DeleteCommentResponse404 | DeleteCommentResponse409]:
    """Delete a commit comment

     Delete a commit comment. Anyone can delete their own comment. Only users with
    <strong>REPO_ADMIN</strong> and above may delete comments created by other users. Comments which
    have replies <i>may not be deleted</i>, regardless of the user's granted permissions.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that the
    commit is in to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        comment_id (str):
        version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteCommentResponse401 | DeleteCommentResponse404 | DeleteCommentResponse409]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        comment_id=comment_id,
        version=version,
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
    version: str | Unset = UNSET,
) -> Any | DeleteCommentResponse401 | DeleteCommentResponse404 | DeleteCommentResponse409 | None:
    """Delete a commit comment

     Delete a commit comment. Anyone can delete their own comment. Only users with
    <strong>REPO_ADMIN</strong> and above may delete comments created by other users. Comments which
    have replies <i>may not be deleted</i>, regardless of the user's granted permissions.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that the
    commit is in to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        comment_id (str):
        version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteCommentResponse401 | DeleteCommentResponse404 | DeleteCommentResponse409
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        comment_id=comment_id,
        client=client,
        version=version,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    comment_id: str,
    *,
    client: AuthenticatedClient | Client,
    version: str | Unset = UNSET,
) -> Response[Any | DeleteCommentResponse401 | DeleteCommentResponse404 | DeleteCommentResponse409]:
    """Delete a commit comment

     Delete a commit comment. Anyone can delete their own comment. Only users with
    <strong>REPO_ADMIN</strong> and above may delete comments created by other users. Comments which
    have replies <i>may not be deleted</i>, regardless of the user's granted permissions.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that the
    commit is in to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        comment_id (str):
        version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteCommentResponse401 | DeleteCommentResponse404 | DeleteCommentResponse409]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        comment_id=comment_id,
        version=version,
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
    version: str | Unset = UNSET,
) -> Any | DeleteCommentResponse401 | DeleteCommentResponse404 | DeleteCommentResponse409 | None:
    """Delete a commit comment

     Delete a commit comment. Anyone can delete their own comment. Only users with
    <strong>REPO_ADMIN</strong> and above may delete comments created by other users. Comments which
    have replies <i>may not be deleted</i>, regardless of the user's granted permissions.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that the
    commit is in to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        comment_id (str):
        version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteCommentResponse401 | DeleteCommentResponse404 | DeleteCommentResponse409
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            commit_id=commit_id,
            comment_id=comment_id,
            client=client,
            version=version,
        )
    ).parsed
