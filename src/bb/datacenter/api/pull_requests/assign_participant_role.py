from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.assign_participant_role_response_400 import AssignParticipantRoleResponse400
from ...models.assign_participant_role_response_401 import AssignParticipantRoleResponse401
from ...models.assign_participant_role_response_404 import AssignParticipantRoleResponse404
from ...models.assign_participant_role_response_409 import AssignParticipantRoleResponse409
from ...models.rest_pull_request_assign_participant_role_request import RestPullRequestAssignParticipantRoleRequest
from ...models.rest_pull_request_participant import RestPullRequestParticipant
from ...types import Response


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    *,
    body: RestPullRequestAssignParticipantRoleRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/pull-requests/{pull_request_id}/participants".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            pull_request_id=quote(str(pull_request_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AssignParticipantRoleResponse400
    | AssignParticipantRoleResponse401
    | AssignParticipantRoleResponse404
    | AssignParticipantRoleResponse409
    | RestPullRequestParticipant
    | None
):
    if response.status_code == 200:
        response_200 = RestPullRequestParticipant.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = AssignParticipantRoleResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = AssignParticipantRoleResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = AssignParticipantRoleResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = AssignParticipantRoleResponse409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AssignParticipantRoleResponse400
    | AssignParticipantRoleResponse401
    | AssignParticipantRoleResponse404
    | AssignParticipantRoleResponse409
    | RestPullRequestParticipant
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
    body: RestPullRequestAssignParticipantRoleRequest,
) -> Response[
    AssignParticipantRoleResponse400
    | AssignParticipantRoleResponse401
    | AssignParticipantRoleResponse404
    | AssignParticipantRoleResponse409
    | RestPullRequestParticipant
]:
    """Assign pull request participant role

     Assigns a participant to an explicit role in pull request. Currently only the REVIEWER role may be
    assigned.

    If the user is not yet a participant in the pull request, they are made one and assigned the
    supplied role.

    If the user is already a participant in the pull request, their previous role is replaced with the
    supplied role unless they are already assigned the AUTHOR role which cannot be changed and will
    result in a Bad Request (400) response code.

    The authenticated user must have <strong>REPO_WRITE</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        body (RestPullRequestAssignParticipantRoleRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssignParticipantRoleResponse400 | AssignParticipantRoleResponse401 | AssignParticipantRoleResponse404 | AssignParticipantRoleResponse409 | RestPullRequestParticipant]
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
    body: RestPullRequestAssignParticipantRoleRequest,
) -> (
    AssignParticipantRoleResponse400
    | AssignParticipantRoleResponse401
    | AssignParticipantRoleResponse404
    | AssignParticipantRoleResponse409
    | RestPullRequestParticipant
    | None
):
    """Assign pull request participant role

     Assigns a participant to an explicit role in pull request. Currently only the REVIEWER role may be
    assigned.

    If the user is not yet a participant in the pull request, they are made one and assigned the
    supplied role.

    If the user is already a participant in the pull request, their previous role is replaced with the
    supplied role unless they are already assigned the AUTHOR role which cannot be changed and will
    result in a Bad Request (400) response code.

    The authenticated user must have <strong>REPO_WRITE</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        body (RestPullRequestAssignParticipantRoleRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssignParticipantRoleResponse400 | AssignParticipantRoleResponse401 | AssignParticipantRoleResponse404 | AssignParticipantRoleResponse409 | RestPullRequestParticipant
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
    body: RestPullRequestAssignParticipantRoleRequest,
) -> Response[
    AssignParticipantRoleResponse400
    | AssignParticipantRoleResponse401
    | AssignParticipantRoleResponse404
    | AssignParticipantRoleResponse409
    | RestPullRequestParticipant
]:
    """Assign pull request participant role

     Assigns a participant to an explicit role in pull request. Currently only the REVIEWER role may be
    assigned.

    If the user is not yet a participant in the pull request, they are made one and assigned the
    supplied role.

    If the user is already a participant in the pull request, their previous role is replaced with the
    supplied role unless they are already assigned the AUTHOR role which cannot be changed and will
    result in a Bad Request (400) response code.

    The authenticated user must have <strong>REPO_WRITE</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        body (RestPullRequestAssignParticipantRoleRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssignParticipantRoleResponse400 | AssignParticipantRoleResponse401 | AssignParticipantRoleResponse404 | AssignParticipantRoleResponse409 | RestPullRequestParticipant]
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
    body: RestPullRequestAssignParticipantRoleRequest,
) -> (
    AssignParticipantRoleResponse400
    | AssignParticipantRoleResponse401
    | AssignParticipantRoleResponse404
    | AssignParticipantRoleResponse409
    | RestPullRequestParticipant
    | None
):
    """Assign pull request participant role

     Assigns a participant to an explicit role in pull request. Currently only the REVIEWER role may be
    assigned.

    If the user is not yet a participant in the pull request, they are made one and assigned the
    supplied role.

    If the user is already a participant in the pull request, their previous role is replaced with the
    supplied role unless they are already assigned the AUTHOR role which cannot be changed and will
    result in a Bad Request (400) response code.

    The authenticated user must have <strong>REPO_WRITE</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        body (RestPullRequestAssignParticipantRoleRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssignParticipantRoleResponse400 | AssignParticipantRoleResponse401 | AssignParticipantRoleResponse404 | AssignParticipantRoleResponse409 | RestPullRequestParticipant
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
