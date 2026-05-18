from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.commit_comment import CommitComment
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
    commit: str,
    comment_id: int,
    *,
    body: CommitComment,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/repositories/{workspace}/{repo_slug}/commit/{commit}/comments/{comment_id}".format(
            workspace=quote(str(workspace), safe=""),
            repo_slug=quote(str(repo_slug), safe=""),
            commit=quote(str(commit), safe=""),
            comment_id=quote(str(comment_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


type ParsedPayload = Any | Error
type ParseResult = Any | Error | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 201:
        response_201 = cast(Any, None)
        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

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
    body: CommitComment,
) -> Response[ParsedPayload]:
    r""" Update a commit comment

     Used to update the contents of a comment. Only the content of the comment can be updated.

    ```
    $ curl https://api.bitbucket.org/2.0/repositories/atlassian/prlinks/commit/7f71b5/comments/5728901 \
      -X PUT -u evzijst \
      -H 'Content-Type: application/json' \
      -d '{\"content\": {\"raw\": \"One more thing!\"}'
    ```

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        comment_id (int):
        body (CommitComment):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
     """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        commit=commit,
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
    commit: str,
    comment_id: int,
    *,
    client: AuthenticatedClient,
    body: CommitComment,
) -> ParsedPayload | None:
    r""" Update a commit comment

     Used to update the contents of a comment. Only the content of the comment can be updated.

    ```
    $ curl https://api.bitbucket.org/2.0/repositories/atlassian/prlinks/commit/7f71b5/comments/5728901 \
      -X PUT -u evzijst \
      -H 'Content-Type: application/json' \
      -d '{\"content\": {\"raw\": \"One more thing!\"}'
    ```

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        comment_id (int):
        body (CommitComment):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        commit=commit,
        comment_id=comment_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    commit: str,
    comment_id: int,
    *,
    client: AuthenticatedClient,
    body: CommitComment,
) -> Response[ParsedPayload]:
    r""" Update a commit comment

     Used to update the contents of a comment. Only the content of the comment can be updated.

    ```
    $ curl https://api.bitbucket.org/2.0/repositories/atlassian/prlinks/commit/7f71b5/comments/5728901 \
      -X PUT -u evzijst \
      -H 'Content-Type: application/json' \
      -d '{\"content\": {\"raw\": \"One more thing!\"}'
    ```

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        comment_id (int):
        body (CommitComment):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
     """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        commit=commit,
        comment_id=comment_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    commit: str,
    comment_id: int,
    *,
    client: AuthenticatedClient,
    body: CommitComment,
) -> ParsedPayload | None:
    r""" Update a commit comment

     Used to update the contents of a comment. Only the content of the comment can be updated.

    ```
    $ curl https://api.bitbucket.org/2.0/repositories/atlassian/prlinks/commit/7f71b5/comments/5728901 \
      -X PUT -u evzijst \
      -H 'Content-Type: application/json' \
      -d '{\"content\": {\"raw\": \"One more thing!\"}'
    ```

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        comment_id (int):
        body (CommitComment):

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
            commit=commit,
            comment_id=comment_id,
            client=client,
            body=body,
        )
    ).parsed
