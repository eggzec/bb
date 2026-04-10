from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_commit_message_suggestion_response_401 import GetCommitMessageSuggestionResponse401
from ...models.get_commit_message_suggestion_response_404 import GetCommitMessageSuggestionResponse404
from ...models.rest_commit_message_suggestion import RestCommitMessageSuggestion
from ...types import Response


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/pull-requests/{pull_request_id}/commit-message-suggestion".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            pull_request_id=quote(str(pull_request_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetCommitMessageSuggestionResponse401 | GetCommitMessageSuggestionResponse404 | RestCommitMessageSuggestion | None:
    if response.status_code == 200:
        response_200 = RestCommitMessageSuggestion.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetCommitMessageSuggestionResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetCommitMessageSuggestionResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetCommitMessageSuggestionResponse401 | GetCommitMessageSuggestionResponse404 | RestCommitMessageSuggestion
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
    GetCommitMessageSuggestionResponse401 | GetCommitMessageSuggestionResponse404 | RestCommitMessageSuggestion
]:
    """Get commit message suggestion

     Retrieve a suggested commit message for the given Pull Request.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCommitMessageSuggestionResponse401 | GetCommitMessageSuggestionResponse404 | RestCommitMessageSuggestion]
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
) -> GetCommitMessageSuggestionResponse401 | GetCommitMessageSuggestionResponse404 | RestCommitMessageSuggestion | None:
    """Get commit message suggestion

     Retrieve a suggested commit message for the given Pull Request.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCommitMessageSuggestionResponse401 | GetCommitMessageSuggestionResponse404 | RestCommitMessageSuggestion
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
    GetCommitMessageSuggestionResponse401 | GetCommitMessageSuggestionResponse404 | RestCommitMessageSuggestion
]:
    """Get commit message suggestion

     Retrieve a suggested commit message for the given Pull Request.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCommitMessageSuggestionResponse401 | GetCommitMessageSuggestionResponse404 | RestCommitMessageSuggestion]
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
) -> GetCommitMessageSuggestionResponse401 | GetCommitMessageSuggestionResponse404 | RestCommitMessageSuggestion | None:
    """Get commit message suggestion

     Retrieve a suggested commit message for the given Pull Request.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCommitMessageSuggestionResponse401 | GetCommitMessageSuggestionResponse404 | RestCommitMessageSuggestion
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            pull_request_id=pull_request_id,
            client=client,
        )
    ).parsed
