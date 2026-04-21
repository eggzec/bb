from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...deprecation import deprecated_endpoint
from ...models.error import Error
from ...models.paginated_log_entries import PaginatedLogEntries
from ...types import UNSET, Response, Unset

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
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["q"] = q

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/repositories/{workspace}/{repo_slug}/issues/{issue_id}/changes".format(
            workspace=quote(str(workspace), safe=""),
            repo_slug=quote(str(repo_slug), safe=""),
            issue_id=quote(str(issue_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


type ParsedPayload = Error | PaginatedLogEntries
type ParseResult = Error | PaginatedLogEntries | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_200 = PaginatedLogEntries.from_dict(response.json())

        return response_200

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
    issue_id: str,
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Response[ParsedPayload]:
    r""" List changes on an issue

     Returns the list of all changes that have been made to the specified
    issue. Changes are returned in chronological order with the oldest
    change first.

    Each time an issue is edited in the UI or through the API, an immutable
    change record is created under the `/issues/123/changes` endpoint. It
    also has a comment associated with the change.

    Note that this operation is changing significantly, due to privacy changes.
    See the [announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-changes-
    gdpr/#changes-to-the-issue-changes-api)
    for details.

    Changes support [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) that
    can be used to search for specific changes. For instance, to see
    when an issue transitioned to \"resolved\":

    ```
    $ curl -s https://api.bitbucket.org/2.0/repositories/site/master/issues/1/changes \
       -G --data-urlencode='q=changes.state.new = \"resolved\"'
    ```

    This resource is only available on repositories that have the issue
    tracker enabled.

    N.B.

    The `changes.assignee` and `changes.assignee_account_id` fields are not
    a `user` object. Instead, they contain the raw `username` and
    `account_id` of the user. This is to protect the integrity of the audit
    log even after a user account gets deleted.

    The `changes.assignee` field is deprecated will disappear in the
    future. Use `changes.assignee_account_id` instead.

    Args:
        workspace (str):
        repo_slug (str):
        issue_id (str):
        q (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PaginatedLogEntries]
     """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        issue_id=issue_id,
        q=q,
        sort=sort,
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
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> ParsedPayload | None:
    r""" List changes on an issue

     Returns the list of all changes that have been made to the specified
    issue. Changes are returned in chronological order with the oldest
    change first.

    Each time an issue is edited in the UI or through the API, an immutable
    change record is created under the `/issues/123/changes` endpoint. It
    also has a comment associated with the change.

    Note that this operation is changing significantly, due to privacy changes.
    See the [announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-changes-
    gdpr/#changes-to-the-issue-changes-api)
    for details.

    Changes support [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) that
    can be used to search for specific changes. For instance, to see
    when an issue transitioned to \"resolved\":

    ```
    $ curl -s https://api.bitbucket.org/2.0/repositories/site/master/issues/1/changes \
       -G --data-urlencode='q=changes.state.new = \"resolved\"'
    ```

    This resource is only available on repositories that have the issue
    tracker enabled.

    N.B.

    The `changes.assignee` and `changes.assignee_account_id` fields are not
    a `user` object. Instead, they contain the raw `username` and
    `account_id` of the user. This is to protect the integrity of the audit
    log even after a user account gets deleted.

    The `changes.assignee` field is deprecated will disappear in the
    future. Use `changes.assignee_account_id` instead.

    Args:
        workspace (str):
        repo_slug (str):
        issue_id (str):
        q (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PaginatedLogEntries
     """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        issue_id=issue_id,
        client=client,
        q=q,
        sort=sort,
    ).parsed


@deprecated_endpoint(None)
async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    issue_id: str,
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Response[ParsedPayload]:
    r""" List changes on an issue

     Returns the list of all changes that have been made to the specified
    issue. Changes are returned in chronological order with the oldest
    change first.

    Each time an issue is edited in the UI or through the API, an immutable
    change record is created under the `/issues/123/changes` endpoint. It
    also has a comment associated with the change.

    Note that this operation is changing significantly, due to privacy changes.
    See the [announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-changes-
    gdpr/#changes-to-the-issue-changes-api)
    for details.

    Changes support [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) that
    can be used to search for specific changes. For instance, to see
    when an issue transitioned to \"resolved\":

    ```
    $ curl -s https://api.bitbucket.org/2.0/repositories/site/master/issues/1/changes \
       -G --data-urlencode='q=changes.state.new = \"resolved\"'
    ```

    This resource is only available on repositories that have the issue
    tracker enabled.

    N.B.

    The `changes.assignee` and `changes.assignee_account_id` fields are not
    a `user` object. Instead, they contain the raw `username` and
    `account_id` of the user. This is to protect the integrity of the audit
    log even after a user account gets deleted.

    The `changes.assignee` field is deprecated will disappear in the
    future. Use `changes.assignee_account_id` instead.

    Args:
        workspace (str):
        repo_slug (str):
        issue_id (str):
        q (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PaginatedLogEntries]
     """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        issue_id=issue_id,
        q=q,
        sort=sort,
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
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> ParsedPayload | None:
    r""" List changes on an issue

     Returns the list of all changes that have been made to the specified
    issue. Changes are returned in chronological order with the oldest
    change first.

    Each time an issue is edited in the UI or through the API, an immutable
    change record is created under the `/issues/123/changes` endpoint. It
    also has a comment associated with the change.

    Note that this operation is changing significantly, due to privacy changes.
    See the [announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-changes-
    gdpr/#changes-to-the-issue-changes-api)
    for details.

    Changes support [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) that
    can be used to search for specific changes. For instance, to see
    when an issue transitioned to \"resolved\":

    ```
    $ curl -s https://api.bitbucket.org/2.0/repositories/site/master/issues/1/changes \
       -G --data-urlencode='q=changes.state.new = \"resolved\"'
    ```

    This resource is only available on repositories that have the issue
    tracker enabled.

    N.B.

    The `changes.assignee` and `changes.assignee_account_id` fields are not
    a `user` object. Instead, they contain the raw `username` and
    `account_id` of the user. This is to protect the integrity of the audit
    log even after a user account gets deleted.

    The `changes.assignee` field is deprecated will disappear in the
    future. Use `changes.assignee_account_id` instead.

    Args:
        workspace (str):
        repo_slug (str):
        issue_id (str):
        q (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PaginatedLogEntries
     """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            issue_id=issue_id,
            client=client,
            q=q,
            sort=sort,
        )
    ).parsed
