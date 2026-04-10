from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rebase_response_401 import RebaseResponse401
from ...models.rebase_response_404 import RebaseResponse404
from ...models.rebase_response_409 import RebaseResponse409
from ...models.rest_pull_request_rebase_request import RestPullRequestRebaseRequest
from ...models.rest_pull_request_rebase_result import RestPullRequestRebaseResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    *,
    body: RestPullRequestRebaseRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/git/latest/projects/{project_key}/repos/{repository_slug}/pull-requests/{pull_request_id}/rebase".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            pull_request_id=quote(str(pull_request_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RebaseResponse401 | RebaseResponse404 | RebaseResponse409 | RestPullRequestRebaseResult | None:
    if response.status_code == 200:
        response_200 = RestPullRequestRebaseResult.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = RebaseResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = RebaseResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = RebaseResponse409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RebaseResponse401 | RebaseResponse404 | RebaseResponse409 | RestPullRequestRebaseResult]:
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
    body: RestPullRequestRebaseRequest | Unset = UNSET,
) -> Response[RebaseResponse401 | RebaseResponse404 | RebaseResponse409 | RestPullRequestRebaseResult]:
    """Rebase pull request

     Rebases the specified pull request, rewriting the incoming commits to start from the tip commit of
    the pull request's target branch. <i>This operation alters the pull request's source branch and
    cannot be undone.</i>

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets <i>and</i> <strong>REPO_WRITE</strong> permission for the pull request's source
    repository to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        body (RestPullRequestRebaseRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RebaseResponse401 | RebaseResponse404 | RebaseResponse409 | RestPullRequestRebaseResult]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
        body=body,
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
    body: RestPullRequestRebaseRequest | Unset = UNSET,
) -> RebaseResponse401 | RebaseResponse404 | RebaseResponse409 | RestPullRequestRebaseResult | None:
    """Rebase pull request

     Rebases the specified pull request, rewriting the incoming commits to start from the tip commit of
    the pull request's target branch. <i>This operation alters the pull request's source branch and
    cannot be undone.</i>

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets <i>and</i> <strong>REPO_WRITE</strong> permission for the pull request's source
    repository to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        body (RestPullRequestRebaseRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RebaseResponse401 | RebaseResponse404 | RebaseResponse409 | RestPullRequestRebaseResult
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestPullRequestRebaseRequest | Unset = UNSET,
) -> Response[RebaseResponse401 | RebaseResponse404 | RebaseResponse409 | RestPullRequestRebaseResult]:
    """Rebase pull request

     Rebases the specified pull request, rewriting the incoming commits to start from the tip commit of
    the pull request's target branch. <i>This operation alters the pull request's source branch and
    cannot be undone.</i>

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets <i>and</i> <strong>REPO_WRITE</strong> permission for the pull request's source
    repository to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        body (RestPullRequestRebaseRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RebaseResponse401 | RebaseResponse404 | RebaseResponse409 | RestPullRequestRebaseResult]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestPullRequestRebaseRequest | Unset = UNSET,
) -> RebaseResponse401 | RebaseResponse404 | RebaseResponse409 | RestPullRequestRebaseResult | None:
    """Rebase pull request

     Rebases the specified pull request, rewriting the incoming commits to start from the tip commit of
    the pull request's target branch. <i>This operation alters the pull request's source branch and
    cannot be undone.</i>

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets <i>and</i> <strong>REPO_WRITE</strong> permission for the pull request's source
    repository to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        body (RestPullRequestRebaseRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RebaseResponse401 | RebaseResponse404 | RebaseResponse409 | RestPullRequestRebaseResult
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            pull_request_id=pull_request_id,
            client=client,
            body=body,
        )
    ).parsed
