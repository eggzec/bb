from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...deprecation import deprecated_endpoint
from ...models.error import Error
from ...models.issue_comment import IssueComment
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
    issue_id: str,
    comment_id: int,
    *,
    body: IssueComment,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/repositories/{workspace}/{repo_slug}/issues/{issue_id}/comments/{comment_id}".format(
            workspace=quote(str(workspace), safe=""),
            repo_slug=quote(str(repo_slug), safe=""),
            issue_id=quote(str(issue_id), safe=""),
            comment_id=quote(str(comment_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


type ParsedPayload = Error | IssueComment
type ParseResult = Error | IssueComment | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_200 = IssueComment.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_400 = Error.from_dict(response.json())

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


@deprecated_endpoint(None)
def sync_detailed(
    workspace: str,
    repo_slug: str,
    issue_id: str,
    comment_id: int,
    *,
    client: AuthenticatedClient,
    body: IssueComment,
) -> Response[ParsedPayload]:
    r""" Update a comment on an issue

     Updates the content of the specified issue comment. Note that only
    the `content.raw` field can be modified.

    ```
    $ curl https://api.bitbucket.org/2.0/repositories/atlassian/prlinks/issues/42/comments/5728901 \
      -X PUT -u evzijst \
      -H 'Content-Type: application/json' \
      -d '{\"content\": {\"raw\": \"Lorem ipsum.\"}'
    ```

    Args:
        workspace (str):
        repo_slug (str):
        issue_id (str):
        comment_id (int):
        body (IssueComment):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | IssueComment]
     """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        issue_id=issue_id,
        comment_id=comment_id,
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
    issue_id: str,
    comment_id: int,
    *,
    client: AuthenticatedClient,
    body: IssueComment,
) -> ParsedPayload | None:
    r""" Update a comment on an issue

     Updates the content of the specified issue comment. Note that only
    the `content.raw` field can be modified.

    ```
    $ curl https://api.bitbucket.org/2.0/repositories/atlassian/prlinks/issues/42/comments/5728901 \
      -X PUT -u evzijst \
      -H 'Content-Type: application/json' \
      -d '{\"content\": {\"raw\": \"Lorem ipsum.\"}'
    ```

    Args:
        workspace (str):
        repo_slug (str):
        issue_id (str):
        comment_id (int):
        body (IssueComment):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | IssueComment
     """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        issue_id=issue_id,
        comment_id=comment_id,
        client=client,
        body=body,
    ).parsed


@deprecated_endpoint(None)
async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    issue_id: str,
    comment_id: int,
    *,
    client: AuthenticatedClient,
    body: IssueComment,
) -> Response[ParsedPayload]:
    r""" Update a comment on an issue

     Updates the content of the specified issue comment. Note that only
    the `content.raw` field can be modified.

    ```
    $ curl https://api.bitbucket.org/2.0/repositories/atlassian/prlinks/issues/42/comments/5728901 \
      -X PUT -u evzijst \
      -H 'Content-Type: application/json' \
      -d '{\"content\": {\"raw\": \"Lorem ipsum.\"}'
    ```

    Args:
        workspace (str):
        repo_slug (str):
        issue_id (str):
        comment_id (int):
        body (IssueComment):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | IssueComment]
     """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        issue_id=issue_id,
        comment_id=comment_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated_endpoint(None)
async def asyncio(
    workspace: str,
    repo_slug: str,
    issue_id: str,
    comment_id: int,
    *,
    client: AuthenticatedClient,
    body: IssueComment,
) -> ParsedPayload | None:
    r""" Update a comment on an issue

     Updates the content of the specified issue comment. Note that only
    the `content.raw` field can be modified.

    ```
    $ curl https://api.bitbucket.org/2.0/repositories/atlassian/prlinks/issues/42/comments/5728901 \
      -X PUT -u evzijst \
      -H 'Content-Type: application/json' \
      -d '{\"content\": {\"raw\": \"Lorem ipsum.\"}'
    ```

    Args:
        workspace (str):
        repo_slug (str):
        issue_id (str):
        comment_id (int):
        body (IssueComment):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | IssueComment
     """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            issue_id=issue_id,
            comment_id=comment_id,
            client=client,
            body=body,
        )
    ).parsed
