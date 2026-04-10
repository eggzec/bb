from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_commits_by_issue_key_response_200 import GetCommitsByIssueKeyResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    issue_key: str,
    *,
    max_changes: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["maxChanges"] = max_changes

    params["start"] = start

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/jira/latest/issues/{issue_key}/commits".format(
            issue_key=quote(str(issue_key), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetCommitsByIssueKeyResponse200 | None:
    if response.status_code == 200:
        response_200 = GetCommitsByIssueKeyResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetCommitsByIssueKeyResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    issue_key: str,
    *,
    client: AuthenticatedClient | Client,
    max_changes: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GetCommitsByIssueKeyResponse200]:
    """Get changesets for issue key

     Retrieve a page of changesets associated with the given issue key.

    Args:
        issue_key (str):
        max_changes (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCommitsByIssueKeyResponse200]
    """

    kwargs = _get_kwargs(
        issue_key=issue_key,
        max_changes=max_changes,
        start=start,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    issue_key: str,
    *,
    client: AuthenticatedClient | Client,
    max_changes: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetCommitsByIssueKeyResponse200 | None:
    """Get changesets for issue key

     Retrieve a page of changesets associated with the given issue key.

    Args:
        issue_key (str):
        max_changes (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCommitsByIssueKeyResponse200
    """

    return sync_detailed(
        issue_key=issue_key,
        client=client,
        max_changes=max_changes,
        start=start,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    issue_key: str,
    *,
    client: AuthenticatedClient | Client,
    max_changes: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GetCommitsByIssueKeyResponse200]:
    """Get changesets for issue key

     Retrieve a page of changesets associated with the given issue key.

    Args:
        issue_key (str):
        max_changes (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCommitsByIssueKeyResponse200]
    """

    kwargs = _get_kwargs(
        issue_key=issue_key,
        max_changes=max_changes,
        start=start,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    issue_key: str,
    *,
    client: AuthenticatedClient | Client,
    max_changes: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetCommitsByIssueKeyResponse200 | None:
    """Get changesets for issue key

     Retrieve a page of changesets associated with the given issue key.

    Args:
        issue_key (str):
        max_changes (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCommitsByIssueKeyResponse200
    """

    return (
        await asyncio_detailed(
            issue_key=issue_key,
            client=client,
            max_changes=max_changes,
            start=start,
            limit=limit,
        )
    ).parsed
