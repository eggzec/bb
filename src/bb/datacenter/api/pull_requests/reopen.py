from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.reopen_response_401 import ReopenResponse401
from ...models.reopen_response_404 import ReopenResponse404
from ...models.reopen_response_409 import ReopenResponse409
from ...models.rest_pull_request import RestPullRequest
from ...models.rest_pull_request_reopen_request import RestPullRequestReopenRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    *,
    body: RestPullRequestReopenRequest | Unset = UNSET,
    version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["version"] = version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/pull-requests/{pull_request_id}/reopen".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            pull_request_id=quote(str(pull_request_id), safe=""),
        ),
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ReopenResponse401 | ReopenResponse404 | ReopenResponse409 | RestPullRequest | None:
    if response.status_code == 200:
        response_200 = RestPullRequest.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ReopenResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ReopenResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ReopenResponse409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ReopenResponse401 | ReopenResponse404 | ReopenResponse409 | RestPullRequest]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestPullRequestReopenRequest | Unset = UNSET,
    version: str | Unset = UNSET,
) -> Response[ReopenResponse401 | ReopenResponse404 | ReopenResponse409 | RestPullRequest]:
    """Re-open pull request

     Re-open a declined pull request.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        version (str | Unset):
        body (RestPullRequestReopenRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReopenResponse401 | ReopenResponse404 | ReopenResponse409 | RestPullRequest]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
        body=body,
        version=version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestPullRequestReopenRequest | Unset = UNSET,
    version: str | Unset = UNSET,
) -> ReopenResponse401 | ReopenResponse404 | ReopenResponse409 | RestPullRequest | None:
    """Re-open pull request

     Re-open a declined pull request.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        version (str | Unset):
        body (RestPullRequestReopenRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReopenResponse401 | ReopenResponse404 | ReopenResponse409 | RestPullRequest
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
        client=client,
        body=body,
        version=version,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestPullRequestReopenRequest | Unset = UNSET,
    version: str | Unset = UNSET,
) -> Response[ReopenResponse401 | ReopenResponse404 | ReopenResponse409 | RestPullRequest]:
    """Re-open pull request

     Re-open a declined pull request.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        version (str | Unset):
        body (RestPullRequestReopenRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReopenResponse401 | ReopenResponse404 | ReopenResponse409 | RestPullRequest]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
        body=body,
        version=version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestPullRequestReopenRequest | Unset = UNSET,
    version: str | Unset = UNSET,
) -> ReopenResponse401 | ReopenResponse404 | ReopenResponse409 | RestPullRequest | None:
    """Re-open pull request

     Re-open a declined pull request.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        version (str | Unset):
        body (RestPullRequestReopenRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReopenResponse401 | ReopenResponse404 | ReopenResponse409 | RestPullRequest
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            pull_request_id=pull_request_id,
            client=client,
            body=body,
            version=version,
        )
    ).parsed
