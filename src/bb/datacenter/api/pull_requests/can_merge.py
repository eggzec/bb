from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.can_merge_response_401 import CanMergeResponse401
from ...models.can_merge_response_404 import CanMergeResponse404
from ...models.can_merge_response_409 import CanMergeResponse409
from ...models.rest_pull_request_mergeability import RestPullRequestMergeability
from ...types import Response


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/pull-requests/{pull_request_id}/merge".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            pull_request_id=quote(str(pull_request_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CanMergeResponse401 | CanMergeResponse404 | CanMergeResponse409 | RestPullRequestMergeability | None:
    if response.status_code == 200:
        response_200 = RestPullRequestMergeability.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = CanMergeResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = CanMergeResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = CanMergeResponse409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CanMergeResponse401 | CanMergeResponse404 | CanMergeResponse409 | RestPullRequestMergeability]:
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
) -> Response[CanMergeResponse401 | CanMergeResponse404 | CanMergeResponse409 | RestPullRequestMergeability]:
    """Test if pull request can be merged

     Test whether a pull request can be merged.

    A pull request may not be merged if:

    - there are conflicts that need to be manually resolved before merging; and/or
    - one or more merge checks have vetoed the merge.


    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CanMergeResponse401 | CanMergeResponse404 | CanMergeResponse409 | RestPullRequestMergeability]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
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
) -> CanMergeResponse401 | CanMergeResponse404 | CanMergeResponse409 | RestPullRequestMergeability | None:
    """Test if pull request can be merged

     Test whether a pull request can be merged.

    A pull request may not be merged if:

    - there are conflicts that need to be manually resolved before merging; and/or
    - one or more merge checks have vetoed the merge.


    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CanMergeResponse401 | CanMergeResponse404 | CanMergeResponse409 | RestPullRequestMergeability
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[CanMergeResponse401 | CanMergeResponse404 | CanMergeResponse409 | RestPullRequestMergeability]:
    """Test if pull request can be merged

     Test whether a pull request can be merged.

    A pull request may not be merged if:

    - there are conflicts that need to be manually resolved before merging; and/or
    - one or more merge checks have vetoed the merge.


    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CanMergeResponse401 | CanMergeResponse404 | CanMergeResponse409 | RestPullRequestMergeability]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> CanMergeResponse401 | CanMergeResponse404 | CanMergeResponse409 | RestPullRequestMergeability | None:
    """Test if pull request can be merged

     Test whether a pull request can be merged.

    A pull request may not be merged if:

    - there are conflicts that need to be manually resolved before merging; and/or
    - one or more merge checks have vetoed the merge.


    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CanMergeResponse401 | CanMergeResponse404 | CanMergeResponse409 | RestPullRequestMergeability
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            pull_request_id=pull_request_id,
            client=client,
        )
    ).parsed
