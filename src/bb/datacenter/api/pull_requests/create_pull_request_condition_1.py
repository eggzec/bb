from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_pull_request_condition_1_response_400 import CreatePullRequestCondition1Response400
from ...models.rest_default_reviewers_request import RestDefaultReviewersRequest
from ...models.rest_pull_request_condition import RestPullRequestCondition
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    *,
    body: RestDefaultReviewersRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/default-reviewers/latest/projects/{project_key}/repos/{repository_slug}/condition".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreatePullRequestCondition1Response400 | RestPullRequestCondition | None:
    if response.status_code == 200:
        response_200 = RestPullRequestCondition.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CreatePullRequestCondition1Response400.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreatePullRequestCondition1Response400 | RestPullRequestCondition]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestDefaultReviewersRequest | Unset = UNSET,
) -> Response[CreatePullRequestCondition1Response400 | RestPullRequestCondition]:
    """Create default reviewer condition

     Create a default reviewer pull request condition for the given repository.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestDefaultReviewersRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatePullRequestCondition1Response400 | RestPullRequestCondition]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestDefaultReviewersRequest | Unset = UNSET,
) -> CreatePullRequestCondition1Response400 | RestPullRequestCondition | None:
    """Create default reviewer condition

     Create a default reviewer pull request condition for the given repository.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestDefaultReviewersRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatePullRequestCondition1Response400 | RestPullRequestCondition
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestDefaultReviewersRequest | Unset = UNSET,
) -> Response[CreatePullRequestCondition1Response400 | RestPullRequestCondition]:
    """Create default reviewer condition

     Create a default reviewer pull request condition for the given repository.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestDefaultReviewersRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatePullRequestCondition1Response400 | RestPullRequestCondition]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestDefaultReviewersRequest | Unset = UNSET,
) -> CreatePullRequestCondition1Response400 | RestPullRequestCondition | None:
    """Create default reviewer condition

     Create a default reviewer pull request condition for the given repository.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestDefaultReviewersRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatePullRequestCondition1Response400 | RestPullRequestCondition
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            client=client,
            body=body,
        )
    ).parsed
