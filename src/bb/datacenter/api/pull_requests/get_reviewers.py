from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_errors import RestErrors
from ...models.rest_pull_request_condition import RestPullRequestCondition
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    *,
    target_repo_id: str | Unset = UNSET,
    source_repo_id: str | Unset = UNSET,
    source_ref_id: str | Unset = UNSET,
    target_ref_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["targetRepoId"] = target_repo_id

    params["sourceRepoId"] = source_repo_id

    params["sourceRefId"] = source_ref_id

    params["targetRefId"] = target_ref_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/default-reviewers/latest/projects/{project_key}/repos/{repository_slug}/reviewers".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RestErrors | list[RestPullRequestCondition] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RestPullRequestCondition.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = RestErrors.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RestErrors | list[RestPullRequestCondition]]:
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
    target_repo_id: str | Unset = UNSET,
    source_repo_id: str | Unset = UNSET,
    source_ref_id: str | Unset = UNSET,
    target_ref_id: str | Unset = UNSET,
) -> Response[RestErrors | list[RestPullRequestCondition]]:
    """Get required reviewers for PR creation

     Return a set of users who are required reviewers for pull requests created from the given source
    repository and ref to the given target ref in this repository.

    Args:
        project_key (str):
        repository_slug (str):
        target_repo_id (str | Unset):
        source_repo_id (str | Unset):
        source_ref_id (str | Unset):
        target_ref_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestErrors | list[RestPullRequestCondition]]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        target_repo_id=target_repo_id,
        source_repo_id=source_repo_id,
        source_ref_id=source_ref_id,
        target_ref_id=target_ref_id,
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
    target_repo_id: str | Unset = UNSET,
    source_repo_id: str | Unset = UNSET,
    source_ref_id: str | Unset = UNSET,
    target_ref_id: str | Unset = UNSET,
) -> RestErrors | list[RestPullRequestCondition] | None:
    """Get required reviewers for PR creation

     Return a set of users who are required reviewers for pull requests created from the given source
    repository and ref to the given target ref in this repository.

    Args:
        project_key (str):
        repository_slug (str):
        target_repo_id (str | Unset):
        source_repo_id (str | Unset):
        source_ref_id (str | Unset):
        target_ref_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestErrors | list[RestPullRequestCondition]
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        client=client,
        target_repo_id=target_repo_id,
        source_repo_id=source_repo_id,
        source_ref_id=source_ref_id,
        target_ref_id=target_ref_id,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    target_repo_id: str | Unset = UNSET,
    source_repo_id: str | Unset = UNSET,
    source_ref_id: str | Unset = UNSET,
    target_ref_id: str | Unset = UNSET,
) -> Response[RestErrors | list[RestPullRequestCondition]]:
    """Get required reviewers for PR creation

     Return a set of users who are required reviewers for pull requests created from the given source
    repository and ref to the given target ref in this repository.

    Args:
        project_key (str):
        repository_slug (str):
        target_repo_id (str | Unset):
        source_repo_id (str | Unset):
        source_ref_id (str | Unset):
        target_ref_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestErrors | list[RestPullRequestCondition]]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        target_repo_id=target_repo_id,
        source_repo_id=source_repo_id,
        source_ref_id=source_ref_id,
        target_ref_id=target_ref_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    target_repo_id: str | Unset = UNSET,
    source_repo_id: str | Unset = UNSET,
    source_ref_id: str | Unset = UNSET,
    target_ref_id: str | Unset = UNSET,
) -> RestErrors | list[RestPullRequestCondition] | None:
    """Get required reviewers for PR creation

     Return a set of users who are required reviewers for pull requests created from the given source
    repository and ref to the given target ref in this repository.

    Args:
        project_key (str):
        repository_slug (str):
        target_repo_id (str | Unset):
        source_repo_id (str | Unset):
        source_ref_id (str | Unset):
        target_ref_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestErrors | list[RestPullRequestCondition]
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            client=client,
            target_repo_id=target_repo_id,
            source_repo_id=source_repo_id,
            source_ref_id=source_ref_id,
            target_ref_id=target_ref_id,
        )
    ).parsed
