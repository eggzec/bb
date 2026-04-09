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
    issue_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/repositories/{workspace}/{repo_slug}/issues/{issue_id}".format(
            workspace=quote(str(workspace), safe=""),
            repo_slug=quote(str(repo_slug), safe=""),
            issue_id=quote(str(issue_id), safe=""),
        ),
    }

    return _kwargs


type ParsedPayload = Error | Issue
type ParseResult = Error | Issue | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        response_200 = Issue.from_dict(response.json())

        return response_200

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
    issue_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    r""" Update an issue

     Modifies the issue.

    ```
    $ curl https://api.bitbucket.org/2.0/repostories/evzijst/dogslow/issues/123 \
      -u evzijst -s -X PUT -H 'Content-Type: application/json' \
      -d '{
      \"title\": \"Updated title\",
      \"assignee\": {
        \"account_id\": \"5d5355e8c6b9320d9ea5b28d\"
      },
      \"priority\": \"minor\",
      \"version\": {
        \"name\": \"1.0\"
      },
      \"component\": null
    }'
    ```

    This example changes the `title`, `assignee`, `priority` and the
    `version`. It also removes the value of the `component` from the issue
    by setting the field to `null`. Any field not present keeps its existing
    value.

    Each time an issue is edited in the UI or through the API, an immutable
    change record is created under the `/issues/123/changes` endpoint. It
    also has a comment associated with the change.

    Args:
        workspace (str):
        repo_slug (str):
        issue_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Issue]
     """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        issue_id=issue_id,
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
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    r""" Update an issue

     Modifies the issue.

    ```
    $ curl https://api.bitbucket.org/2.0/repostories/evzijst/dogslow/issues/123 \
      -u evzijst -s -X PUT -H 'Content-Type: application/json' \
      -d '{
      \"title\": \"Updated title\",
      \"assignee\": {
        \"account_id\": \"5d5355e8c6b9320d9ea5b28d\"
      },
      \"priority\": \"minor\",
      \"version\": {
        \"name\": \"1.0\"
      },
      \"component\": null
    }'
    ```

    This example changes the `title`, `assignee`, `priority` and the
    `version`. It also removes the value of the `component` from the issue
    by setting the field to `null`. Any field not present keeps its existing
    value.

    Each time an issue is edited in the UI or through the API, an immutable
    change record is created under the `/issues/123/changes` endpoint. It
    also has a comment associated with the change.

    Args:
        workspace (str):
        repo_slug (str):
        issue_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Issue
     """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        issue_id=issue_id,
        client=client,
    ).parsed


@deprecated_endpoint(None)
async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    issue_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    r""" Update an issue

     Modifies the issue.

    ```
    $ curl https://api.bitbucket.org/2.0/repostories/evzijst/dogslow/issues/123 \
      -u evzijst -s -X PUT -H 'Content-Type: application/json' \
      -d '{
      \"title\": \"Updated title\",
      \"assignee\": {
        \"account_id\": \"5d5355e8c6b9320d9ea5b28d\"
      },
      \"priority\": \"minor\",
      \"version\": {
        \"name\": \"1.0\"
      },
      \"component\": null
    }'
    ```

    This example changes the `title`, `assignee`, `priority` and the
    `version`. It also removes the value of the `component` from the issue
    by setting the field to `null`. Any field not present keeps its existing
    value.

    Each time an issue is edited in the UI or through the API, an immutable
    change record is created under the `/issues/123/changes` endpoint. It
    also has a comment associated with the change.

    Args:
        workspace (str):
        repo_slug (str):
        issue_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Issue]
     """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        issue_id=issue_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated_endpoint(None)
async def asyncio(
    workspace: str,
    repo_slug: str,
    issue_id: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    r""" Update an issue

     Modifies the issue.

    ```
    $ curl https://api.bitbucket.org/2.0/repostories/evzijst/dogslow/issues/123 \
      -u evzijst -s -X PUT -H 'Content-Type: application/json' \
      -d '{
      \"title\": \"Updated title\",
      \"assignee\": {
        \"account_id\": \"5d5355e8c6b9320d9ea5b28d\"
      },
      \"priority\": \"minor\",
      \"version\": {
        \"name\": \"1.0\"
      },
      \"component\": null
    }'
    ```

    This example changes the `title`, `assignee`, `priority` and the
    `version`. It also removes the value of the `component` from the issue
    by setting the field to `null`. Any field not present keeps its existing
    value.

    Each time an issue is edited in the UI or through the API, an immutable
    change record is created under the `/issues/123/changes` endpoint. It
    also has a comment associated with the change.

    Args:
        workspace (str):
        repo_slug (str):
        issue_id (str):

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
            issue_id=issue_id,
            client=client,
        )
    ).parsed
