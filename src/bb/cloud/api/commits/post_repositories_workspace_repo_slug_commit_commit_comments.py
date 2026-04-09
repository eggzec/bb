from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.commit_comment import CommitComment
from ...types import Response

__all__ = [
    "sync_detailed",
    "asyncio_detailed",
]


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    commit: str,
    *,
    body: CommitComment,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/repositories/{workspace}/{repo_slug}/commit/{commit}/comments".format(
            workspace=quote(str(workspace), safe=""),
            repo_slug=quote(str(repo_slug), safe=""),
            commit=quote(str(commit), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


type ParsedPayload = Any
type ParseResult = Any | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 201:
        return None

    if response.status_code == 400:
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
    *,
    client: AuthenticatedClient,
    body: CommitComment,
) -> Response[ParsedPayload]:
    r""" Create comment for a commit

     Creates new comment on the specified commit.

    To post a reply to an existing comment, include the `parent.id` field:

    ```
    $ curl https://api.bitbucket.org/2.0/repositories/atlassian/prlinks/commit/db9ba1e031d07a02603eae0e5
    59a7adc010257fc/comments/ \
      -X POST -u evzijst \
      -H 'Content-Type: application/json' \
      -d '{\"content\": {\"raw\": \"One more thing!\"},
           \"parent\": {\"id\": 5728901}}'
    ```

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        body (CommitComment):

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
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    commit: str,
    *,
    client: AuthenticatedClient,
    body: CommitComment,
) -> Response[ParsedPayload]:
    r""" Create comment for a commit

     Creates new comment on the specified commit.

    To post a reply to an existing comment, include the `parent.id` field:

    ```
    $ curl https://api.bitbucket.org/2.0/repositories/atlassian/prlinks/commit/db9ba1e031d07a02603eae0e5
    59a7adc010257fc/comments/ \
      -X POST -u evzijst \
      -H 'Content-Type: application/json' \
      -d '{\"content\": {\"raw\": \"One more thing!\"},
           \"parent\": {\"id\": 5728901}}'
    ```

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        body (CommitComment):

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
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
