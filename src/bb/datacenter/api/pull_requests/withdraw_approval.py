from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...deprecation import deprecated_endpoint
from ...models.rest_pull_request_participant import RestPullRequestParticipant
from ...models.withdraw_approval_response_401 import WithdrawApprovalResponse401
from ...models.withdraw_approval_response_404 import WithdrawApprovalResponse404
from ...models.withdraw_approval_response_409 import WithdrawApprovalResponse409
from ...types import Response


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/pull-requests/{pull_request_id}/approve".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            pull_request_id=quote(str(pull_request_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    RestPullRequestParticipant
    | WithdrawApprovalResponse401
    | WithdrawApprovalResponse404
    | WithdrawApprovalResponse409
    | None
):
    if response.status_code == 200:
        response_200 = RestPullRequestParticipant.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = WithdrawApprovalResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = WithdrawApprovalResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = WithdrawApprovalResponse409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    RestPullRequestParticipant | WithdrawApprovalResponse401 | WithdrawApprovalResponse404 | WithdrawApprovalResponse409
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated_endpoint(None)
def sync_detailed(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    RestPullRequestParticipant | WithdrawApprovalResponse401 | WithdrawApprovalResponse404 | WithdrawApprovalResponse409
]:
    """Unapprove pull request

     Remove approval from a pull request as the current user. This does not remove the user as a
    participant.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets to call this resource.

    <strong>Deprecated since 4.2</strong>. Use
    /rest/api/1.0/projects/{projectKey}/repos/{repositorySlug}/pull-
    requests/{pullRequestId}/participants/{userSlug} instead

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestPullRequestParticipant | WithdrawApprovalResponse401 | WithdrawApprovalResponse404 | WithdrawApprovalResponse409]
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


@deprecated_endpoint(None)
def sync(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    RestPullRequestParticipant
    | WithdrawApprovalResponse401
    | WithdrawApprovalResponse404
    | WithdrawApprovalResponse409
    | None
):
    """Unapprove pull request

     Remove approval from a pull request as the current user. This does not remove the user as a
    participant.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets to call this resource.

    <strong>Deprecated since 4.2</strong>. Use
    /rest/api/1.0/projects/{projectKey}/repos/{repositorySlug}/pull-
    requests/{pullRequestId}/participants/{userSlug} instead

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestPullRequestParticipant | WithdrawApprovalResponse401 | WithdrawApprovalResponse404 | WithdrawApprovalResponse409
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
        client=client,
    ).parsed


@deprecated_endpoint(None)
async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    RestPullRequestParticipant | WithdrawApprovalResponse401 | WithdrawApprovalResponse404 | WithdrawApprovalResponse409
]:
    """Unapprove pull request

     Remove approval from a pull request as the current user. This does not remove the user as a
    participant.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets to call this resource.

    <strong>Deprecated since 4.2</strong>. Use
    /rest/api/1.0/projects/{projectKey}/repos/{repositorySlug}/pull-
    requests/{pullRequestId}/participants/{userSlug} instead

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestPullRequestParticipant | WithdrawApprovalResponse401 | WithdrawApprovalResponse404 | WithdrawApprovalResponse409]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated_endpoint(None)
async def asyncio(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    RestPullRequestParticipant
    | WithdrawApprovalResponse401
    | WithdrawApprovalResponse404
    | WithdrawApprovalResponse409
    | None
):
    """Unapprove pull request

     Remove approval from a pull request as the current user. This does not remove the user as a
    participant.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets to call this resource.

    <strong>Deprecated since 4.2</strong>. Use
    /rest/api/1.0/projects/{projectKey}/repos/{repositorySlug}/pull-
    requests/{pullRequestId}/participants/{userSlug} instead

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestPullRequestParticipant | WithdrawApprovalResponse401 | WithdrawApprovalResponse404 | WithdrawApprovalResponse409
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            pull_request_id=pull_request_id,
            client=client,
        )
    ).parsed
