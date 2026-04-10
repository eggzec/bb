from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_pull_request import RestPullRequest
from ...models.update_response_400 import UpdateResponse400
from ...models.update_response_401 import UpdateResponse401
from ...models.update_response_404 import UpdateResponse404
from ...models.update_response_409 import UpdateResponse409
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    *,
    body: RestPullRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/pull-requests/{pull_request_id}".format(
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
) -> RestPullRequest | UpdateResponse400 | UpdateResponse401 | UpdateResponse404 | UpdateResponse409 | None:
    if response.status_code == 200:
        response_200 = RestPullRequest.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UpdateResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UpdateResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = UpdateResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = UpdateResponse409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RestPullRequest | UpdateResponse400 | UpdateResponse401 | UpdateResponse404 | UpdateResponse409]:
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
    body: RestPullRequest | Unset = UNSET,
) -> Response[RestPullRequest | UpdateResponse400 | UpdateResponse401 | UpdateResponse404 | UpdateResponse409]:
    """Update pull request metadata

     Update the title, description, reviewers, destination branch or draft status of an existing pull
    request.

    **Note:** the <em>reviewers</em> list may be updated using this resource. However the
    <em>author</em> and <em>participants</em> list may not.

    The authenticated user must either:

    - be the author of the pull request and have the <strong>REPO_READ</strong> permission for the
    repository that this pull request targets; or
    - have the <strong>REPO_WRITE</strong> permission for the repository that this pull request targets


    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        body (RestPullRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestPullRequest | UpdateResponse400 | UpdateResponse401 | UpdateResponse404 | UpdateResponse409]
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
    body: RestPullRequest | Unset = UNSET,
) -> RestPullRequest | UpdateResponse400 | UpdateResponse401 | UpdateResponse404 | UpdateResponse409 | None:
    """Update pull request metadata

     Update the title, description, reviewers, destination branch or draft status of an existing pull
    request.

    **Note:** the <em>reviewers</em> list may be updated using this resource. However the
    <em>author</em> and <em>participants</em> list may not.

    The authenticated user must either:

    - be the author of the pull request and have the <strong>REPO_READ</strong> permission for the
    repository that this pull request targets; or
    - have the <strong>REPO_WRITE</strong> permission for the repository that this pull request targets


    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        body (RestPullRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestPullRequest | UpdateResponse400 | UpdateResponse401 | UpdateResponse404 | UpdateResponse409
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
    body: RestPullRequest | Unset = UNSET,
) -> Response[RestPullRequest | UpdateResponse400 | UpdateResponse401 | UpdateResponse404 | UpdateResponse409]:
    """Update pull request metadata

     Update the title, description, reviewers, destination branch or draft status of an existing pull
    request.

    **Note:** the <em>reviewers</em> list may be updated using this resource. However the
    <em>author</em> and <em>participants</em> list may not.

    The authenticated user must either:

    - be the author of the pull request and have the <strong>REPO_READ</strong> permission for the
    repository that this pull request targets; or
    - have the <strong>REPO_WRITE</strong> permission for the repository that this pull request targets


    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        body (RestPullRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestPullRequest | UpdateResponse400 | UpdateResponse401 | UpdateResponse404 | UpdateResponse409]
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
    body: RestPullRequest | Unset = UNSET,
) -> RestPullRequest | UpdateResponse400 | UpdateResponse401 | UpdateResponse404 | UpdateResponse409 | None:
    """Update pull request metadata

     Update the title, description, reviewers, destination branch or draft status of an existing pull
    request.

    **Note:** the <em>reviewers</em> list may be updated using this resource. However the
    <em>author</em> and <em>participants</em> list may not.

    The authenticated user must either:

    - be the author of the pull request and have the <strong>REPO_READ</strong> permission for the
    repository that this pull request targets; or
    - have the <strong>REPO_WRITE</strong> permission for the repository that this pull request targets


    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        body (RestPullRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestPullRequest | UpdateResponse400 | UpdateResponse401 | UpdateResponse404 | UpdateResponse409
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
