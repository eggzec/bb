from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_issue_response_400 import CreateIssueResponse400
from ...models.create_issue_response_401 import CreateIssueResponse401
from ...models.rest_comment_jira_issue import RestCommentJiraIssue
from ...types import UNSET, Response, Unset


def _get_kwargs(
    comment_id: str,
    *,
    body: str | Unset = UNSET,
    application_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["applicationId"] = application_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/jira/latest/comments/{comment_id}/issues".format(
            comment_id=quote(str(comment_id), safe=""),
        ),
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateIssueResponse400 | CreateIssueResponse401 | RestCommentJiraIssue | None:
    if response.status_code == 200:
        response_200 = RestCommentJiraIssue.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CreateIssueResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = CreateIssueResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateIssueResponse400 | CreateIssueResponse401 | RestCommentJiraIssue]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    comment_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: str | Unset = UNSET,
    application_id: str | Unset = UNSET,
) -> Response[CreateIssueResponse400 | CreateIssueResponse401 | RestCommentJiraIssue]:
    """Create Jira Issue

     Create a Jira issue and associate it with a comment on a pull request.

    This resource can only be used with comments on a pull request. Attempting to call this resource
    with a different type of comment (for example, a comment on a commit) will result in an error.

     The authenticated user must have <strong>REPO_READ</strong> permission for the repository
    containing the comment to call this resource.

    The JSON structure for the create issue format is specified by Jira's REST v2 API.

    Args:
        comment_id (str):
        application_id (str | Unset):
        body (str | Unset): application/json

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateIssueResponse400 | CreateIssueResponse401 | RestCommentJiraIssue]
    """

    kwargs = _get_kwargs(
        comment_id=comment_id,
        body=body,
        application_id=application_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    comment_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: str | Unset = UNSET,
    application_id: str | Unset = UNSET,
) -> CreateIssueResponse400 | CreateIssueResponse401 | RestCommentJiraIssue | None:
    """Create Jira Issue

     Create a Jira issue and associate it with a comment on a pull request.

    This resource can only be used with comments on a pull request. Attempting to call this resource
    with a different type of comment (for example, a comment on a commit) will result in an error.

     The authenticated user must have <strong>REPO_READ</strong> permission for the repository
    containing the comment to call this resource.

    The JSON structure for the create issue format is specified by Jira's REST v2 API.

    Args:
        comment_id (str):
        application_id (str | Unset):
        body (str | Unset): application/json

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateIssueResponse400 | CreateIssueResponse401 | RestCommentJiraIssue
    """

    return sync_detailed(
        comment_id=comment_id,
        client=client,
        body=body,
        application_id=application_id,
    ).parsed


async def asyncio_detailed(
    comment_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: str | Unset = UNSET,
    application_id: str | Unset = UNSET,
) -> Response[CreateIssueResponse400 | CreateIssueResponse401 | RestCommentJiraIssue]:
    """Create Jira Issue

     Create a Jira issue and associate it with a comment on a pull request.

    This resource can only be used with comments on a pull request. Attempting to call this resource
    with a different type of comment (for example, a comment on a commit) will result in an error.

     The authenticated user must have <strong>REPO_READ</strong> permission for the repository
    containing the comment to call this resource.

    The JSON structure for the create issue format is specified by Jira's REST v2 API.

    Args:
        comment_id (str):
        application_id (str | Unset):
        body (str | Unset): application/json

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateIssueResponse400 | CreateIssueResponse401 | RestCommentJiraIssue]
    """

    kwargs = _get_kwargs(
        comment_id=comment_id,
        body=body,
        application_id=application_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    comment_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: str | Unset = UNSET,
    application_id: str | Unset = UNSET,
) -> CreateIssueResponse400 | CreateIssueResponse401 | RestCommentJiraIssue | None:
    """Create Jira Issue

     Create a Jira issue and associate it with a comment on a pull request.

    This resource can only be used with comments on a pull request. Attempting to call this resource
    with a different type of comment (for example, a comment on a commit) will result in an error.

     The authenticated user must have <strong>REPO_READ</strong> permission for the repository
    containing the comment to call this resource.

    The JSON structure for the create issue format is specified by Jira's REST v2 API.

    Args:
        comment_id (str):
        application_id (str | Unset):
        body (str | Unset): application/json

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateIssueResponse400 | CreateIssueResponse401 | RestCommentJiraIssue
    """

    return (
        await asyncio_detailed(
            comment_id=comment_id,
            client=client,
            body=body,
            application_id=application_id,
        )
    ).parsed
