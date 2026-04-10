from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_auto_merge_processing_result import RestAutoMergeProcessingResult
from ...models.try_auto_merge_response_400 import TryAutoMergeResponse400
from ...models.try_auto_merge_response_401 import TryAutoMergeResponse401
from ...models.try_auto_merge_response_403 import TryAutoMergeResponse403
from ...models.try_auto_merge_response_404 import TryAutoMergeResponse404
from ...types import Response


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/pull-requests/{pull_request_id}/auto-merge".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            pull_request_id=quote(str(pull_request_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    RestAutoMergeProcessingResult
    | TryAutoMergeResponse400
    | TryAutoMergeResponse401
    | TryAutoMergeResponse403
    | TryAutoMergeResponse404
    | None
):
    if response.status_code == 200:
        response_200 = RestAutoMergeProcessingResult.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = TryAutoMergeResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = TryAutoMergeResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = TryAutoMergeResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = TryAutoMergeResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    RestAutoMergeProcessingResult
    | TryAutoMergeResponse400
    | TryAutoMergeResponse401
    | TryAutoMergeResponse403
    | TryAutoMergeResponse404
]:
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
) -> Response[
    RestAutoMergeProcessingResult
    | TryAutoMergeResponse400
    | TryAutoMergeResponse401
    | TryAutoMergeResponse403
    | TryAutoMergeResponse404
]:
    """Auto-merge pull request

     Requests the system to try merging the pull request if auto-merge was requested on it.

    The authenticated user must have <strong>REPO_WRITE</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestAutoMergeProcessingResult | TryAutoMergeResponse400 | TryAutoMergeResponse401 | TryAutoMergeResponse403 | TryAutoMergeResponse404]
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
) -> (
    RestAutoMergeProcessingResult
    | TryAutoMergeResponse400
    | TryAutoMergeResponse401
    | TryAutoMergeResponse403
    | TryAutoMergeResponse404
    | None
):
    """Auto-merge pull request

     Requests the system to try merging the pull request if auto-merge was requested on it.

    The authenticated user must have <strong>REPO_WRITE</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestAutoMergeProcessingResult | TryAutoMergeResponse400 | TryAutoMergeResponse401 | TryAutoMergeResponse403 | TryAutoMergeResponse404
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
) -> Response[
    RestAutoMergeProcessingResult
    | TryAutoMergeResponse400
    | TryAutoMergeResponse401
    | TryAutoMergeResponse403
    | TryAutoMergeResponse404
]:
    """Auto-merge pull request

     Requests the system to try merging the pull request if auto-merge was requested on it.

    The authenticated user must have <strong>REPO_WRITE</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestAutoMergeProcessingResult | TryAutoMergeResponse400 | TryAutoMergeResponse401 | TryAutoMergeResponse403 | TryAutoMergeResponse404]
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
) -> (
    RestAutoMergeProcessingResult
    | TryAutoMergeResponse400
    | TryAutoMergeResponse401
    | TryAutoMergeResponse403
    | TryAutoMergeResponse404
    | None
):
    """Auto-merge pull request

     Requests the system to try merging the pull request if auto-merge was requested on it.

    The authenticated user must have <strong>REPO_WRITE</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestAutoMergeProcessingResult | TryAutoMergeResponse400 | TryAutoMergeResponse401 | TryAutoMergeResponse403 | TryAutoMergeResponse404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            pull_request_id=pull_request_id,
            client=client,
        )
    ).parsed
