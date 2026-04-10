from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.finish_review_response_400 import FinishReviewResponse400
from ...models.finish_review_response_401 import FinishReviewResponse401
from ...models.finish_review_response_404 import FinishReviewResponse404
from ...models.finish_review_response_409 import FinishReviewResponse409
from ...models.rest_pull_request_finish_review_request import RestPullRequestFinishReviewRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    *,
    body: RestPullRequestFinishReviewRequest | Unset = UNSET,
    version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["version"] = version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/pull-requests/{pull_request_id}/review".format(
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
) -> Any | FinishReviewResponse400 | FinishReviewResponse401 | FinishReviewResponse404 | FinishReviewResponse409 | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 400:
        response_400 = FinishReviewResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FinishReviewResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = FinishReviewResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = FinishReviewResponse409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | FinishReviewResponse400 | FinishReviewResponse401 | FinishReviewResponse404 | FinishReviewResponse409
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
    body: RestPullRequestFinishReviewRequest | Unset = UNSET,
    version: str | Unset = UNSET,
) -> Response[
    Any | FinishReviewResponse400 | FinishReviewResponse401 | FinishReviewResponse404 | FinishReviewResponse409
]:
    """Complete pull request review

     Complete a review on a pull request.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        version (str | Unset):
        body (RestPullRequestFinishReviewRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FinishReviewResponse400 | FinishReviewResponse401 | FinishReviewResponse404 | FinishReviewResponse409]
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
    body: RestPullRequestFinishReviewRequest | Unset = UNSET,
    version: str | Unset = UNSET,
) -> Any | FinishReviewResponse400 | FinishReviewResponse401 | FinishReviewResponse404 | FinishReviewResponse409 | None:
    """Complete pull request review

     Complete a review on a pull request.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        version (str | Unset):
        body (RestPullRequestFinishReviewRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FinishReviewResponse400 | FinishReviewResponse401 | FinishReviewResponse404 | FinishReviewResponse409
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
    body: RestPullRequestFinishReviewRequest | Unset = UNSET,
    version: str | Unset = UNSET,
) -> Response[
    Any | FinishReviewResponse400 | FinishReviewResponse401 | FinishReviewResponse404 | FinishReviewResponse409
]:
    """Complete pull request review

     Complete a review on a pull request.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        version (str | Unset):
        body (RestPullRequestFinishReviewRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FinishReviewResponse400 | FinishReviewResponse401 | FinishReviewResponse404 | FinishReviewResponse409]
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
    body: RestPullRequestFinishReviewRequest | Unset = UNSET,
    version: str | Unset = UNSET,
) -> Any | FinishReviewResponse400 | FinishReviewResponse401 | FinishReviewResponse404 | FinishReviewResponse409 | None:
    """Complete pull request review

     Complete a review on a pull request.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        version (str | Unset):
        body (RestPullRequestFinishReviewRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FinishReviewResponse400 | FinishReviewResponse401 | FinishReviewResponse404 | FinishReviewResponse409
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
