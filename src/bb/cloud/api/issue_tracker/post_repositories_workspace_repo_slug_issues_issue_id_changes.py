from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...deprecation import deprecated_endpoint
from ...models.error import Error
from ...models.issue_change import IssueChange
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
    *,
    body: IssueChange,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/repositories/{workspace}/{repo_slug}/issues/{issue_id}/changes".format(
            workspace=quote(str(workspace), safe=""),
            repo_slug=quote(str(repo_slug), safe=""),
            issue_id=quote(str(issue_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


type ParsedPayload = Error | IssueChange
type ParseResult = Error | IssueChange | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 201:
        response_201 = IssueChange.from_dict(response.json())

        return response_201

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
    issue_id: str,
    *,
    client: AuthenticatedClient,
    body: IssueChange,
) -> Response[ParsedPayload]:
    r""" Modify the state of an issue

     Makes a change to the specified issue.

    For example, to change an issue's state and assignee, create a new
    change object that modifies these fields:

    ```
    curl https://api.bitbucket.org/2.0/site/master/issues/1234/changes \
      -s -u evzijst -X POST -H \"Content-Type: application/json\" \
      -d '{
        \"changes\": {
          \"assignee_account_id\": {
            \"new\": \"557058:c0b72ad0-1cb5-4018-9cdc-0cde8492c443\"
          },
          \"state\": {
            \"new\": 'resolved\"
          }
        }
        \"message\": {
          \"raw\": \"This is now resolved.\"
        }
      }'
    ```

    The above example also includes a custom comment to go alongside the
    change. This comment will also be visible on the issue page in the UI.

    The fields of the `changes` object are strings, not objects. This
    allows for immutable change log records, even after user accounts,
    milestones, or other objects recorded in a change entry, get renamed or
    deleted.

    The `assignee_account_id` field stores the account id. When POSTing a
    new change and changing the assignee, the client should therefore use
    the user's account_id in the `changes.assignee_account_id.new` field.

    This call requires authentication. Private repositories or private
    issue trackers require the caller to authenticate with an account that
    has appropriate authorization.

    Args:
        workspace (str):
        repo_slug (str):
        issue_id (str):
        body (IssueChange): An issue change.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | IssueChange]
     """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        issue_id=issue_id,
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
    *,
    client: AuthenticatedClient,
    body: IssueChange,
) -> ParsedPayload | None:
    r""" Modify the state of an issue

     Makes a change to the specified issue.

    For example, to change an issue's state and assignee, create a new
    change object that modifies these fields:

    ```
    curl https://api.bitbucket.org/2.0/site/master/issues/1234/changes \
      -s -u evzijst -X POST -H \"Content-Type: application/json\" \
      -d '{
        \"changes\": {
          \"assignee_account_id\": {
            \"new\": \"557058:c0b72ad0-1cb5-4018-9cdc-0cde8492c443\"
          },
          \"state\": {
            \"new\": 'resolved\"
          }
        }
        \"message\": {
          \"raw\": \"This is now resolved.\"
        }
      }'
    ```

    The above example also includes a custom comment to go alongside the
    change. This comment will also be visible on the issue page in the UI.

    The fields of the `changes` object are strings, not objects. This
    allows for immutable change log records, even after user accounts,
    milestones, or other objects recorded in a change entry, get renamed or
    deleted.

    The `assignee_account_id` field stores the account id. When POSTing a
    new change and changing the assignee, the client should therefore use
    the user's account_id in the `changes.assignee_account_id.new` field.

    This call requires authentication. Private repositories or private
    issue trackers require the caller to authenticate with an account that
    has appropriate authorization.

    Args:
        workspace (str):
        repo_slug (str):
        issue_id (str):
        body (IssueChange): An issue change.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | IssueChange
     """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        issue_id=issue_id,
        client=client,
        body=body,
    ).parsed


@deprecated_endpoint(None)
async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    issue_id: str,
    *,
    client: AuthenticatedClient,
    body: IssueChange,
) -> Response[ParsedPayload]:
    r""" Modify the state of an issue

     Makes a change to the specified issue.

    For example, to change an issue's state and assignee, create a new
    change object that modifies these fields:

    ```
    curl https://api.bitbucket.org/2.0/site/master/issues/1234/changes \
      -s -u evzijst -X POST -H \"Content-Type: application/json\" \
      -d '{
        \"changes\": {
          \"assignee_account_id\": {
            \"new\": \"557058:c0b72ad0-1cb5-4018-9cdc-0cde8492c443\"
          },
          \"state\": {
            \"new\": 'resolved\"
          }
        }
        \"message\": {
          \"raw\": \"This is now resolved.\"
        }
      }'
    ```

    The above example also includes a custom comment to go alongside the
    change. This comment will also be visible on the issue page in the UI.

    The fields of the `changes` object are strings, not objects. This
    allows for immutable change log records, even after user accounts,
    milestones, or other objects recorded in a change entry, get renamed or
    deleted.

    The `assignee_account_id` field stores the account id. When POSTing a
    new change and changing the assignee, the client should therefore use
    the user's account_id in the `changes.assignee_account_id.new` field.

    This call requires authentication. Private repositories or private
    issue trackers require the caller to authenticate with an account that
    has appropriate authorization.

    Args:
        workspace (str):
        repo_slug (str):
        issue_id (str):
        body (IssueChange): An issue change.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | IssueChange]
     """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        issue_id=issue_id,
        body=body,
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
    body: IssueChange,
) -> ParsedPayload | None:
    r""" Modify the state of an issue

     Makes a change to the specified issue.

    For example, to change an issue's state and assignee, create a new
    change object that modifies these fields:

    ```
    curl https://api.bitbucket.org/2.0/site/master/issues/1234/changes \
      -s -u evzijst -X POST -H \"Content-Type: application/json\" \
      -d '{
        \"changes\": {
          \"assignee_account_id\": {
            \"new\": \"557058:c0b72ad0-1cb5-4018-9cdc-0cde8492c443\"
          },
          \"state\": {
            \"new\": 'resolved\"
          }
        }
        \"message\": {
          \"raw\": \"This is now resolved.\"
        }
      }'
    ```

    The above example also includes a custom comment to go alongside the
    change. This comment will also be visible on the issue page in the UI.

    The fields of the `changes` object are strings, not objects. This
    allows for immutable change log records, even after user accounts,
    milestones, or other objects recorded in a change entry, get renamed or
    deleted.

    The `assignee_account_id` field stores the account id. When POSTing a
    new change and changing the assignee, the client should therefore use
    the user's account_id in the `changes.assignee_account_id.new` field.

    This call requires authentication. Private repositories or private
    issue trackers require the caller to authenticate with an account that
    has appropriate authorization.

    Args:
        workspace (str):
        repo_slug (str):
        issue_id (str):
        body (IssueChange): An issue change.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | IssueChange
     """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            issue_id=issue_id,
            client=client,
            body=body,
        )
    ).parsed
