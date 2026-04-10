from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...deprecation import deprecated_endpoint
from ...models.unassign_participant_role_1_response_401 import UnassignParticipantRole1Response401
from ...models.unassign_participant_role_1_response_404 import UnassignParticipantRole1Response404
from ...models.unassign_participant_role_1_response_409 import UnassignParticipantRole1Response409
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    *,
    username: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["username"] = username

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/pull-requests/{pull_request_id}/participants".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            pull_request_id=quote(str(pull_request_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | UnassignParticipantRole1Response401
    | UnassignParticipantRole1Response404
    | UnassignParticipantRole1Response409
    | None
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = UnassignParticipantRole1Response401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = UnassignParticipantRole1Response404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = UnassignParticipantRole1Response409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | UnassignParticipantRole1Response401
    | UnassignParticipantRole1Response404
    | UnassignParticipantRole1Response409
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
    username: str | Unset = UNSET,
) -> Response[
    Any
    | UnassignParticipantRole1Response401
    | UnassignParticipantRole1Response404
    | UnassignParticipantRole1Response409
]:
    """Unassign pull request participant

     Unassigns a participant from the REVIEWER role they may have been given in a pull request.

    If the participant has no explicit role this method has no effect.

    Afterwards, the user will still remain a participant in the pull request but their role will be
    reduced to PARTICIPANT. This is because once made a participant of a pull request, a user will
    forever remain a participant. Only their role may be altered.

    The authenticated user must have <strong>REPO_WRITE</strong> permission for the repository that this
    pull request targets to call this resource.

    <strong>Deprecated since 4.2</strong>. Use
    /rest/api/1.0/projects/{projectKey}/repos/{repositorySlug}/pull-
    requests/{pullRequestId}/participants/{userSlug} instead.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        username (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | UnassignParticipantRole1Response401 | UnassignParticipantRole1Response404 | UnassignParticipantRole1Response409]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
        username=username,
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
    username: str | Unset = UNSET,
) -> (
    Any
    | UnassignParticipantRole1Response401
    | UnassignParticipantRole1Response404
    | UnassignParticipantRole1Response409
    | None
):
    """Unassign pull request participant

     Unassigns a participant from the REVIEWER role they may have been given in a pull request.

    If the participant has no explicit role this method has no effect.

    Afterwards, the user will still remain a participant in the pull request but their role will be
    reduced to PARTICIPANT. This is because once made a participant of a pull request, a user will
    forever remain a participant. Only their role may be altered.

    The authenticated user must have <strong>REPO_WRITE</strong> permission for the repository that this
    pull request targets to call this resource.

    <strong>Deprecated since 4.2</strong>. Use
    /rest/api/1.0/projects/{projectKey}/repos/{repositorySlug}/pull-
    requests/{pullRequestId}/participants/{userSlug} instead.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        username (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | UnassignParticipantRole1Response401 | UnassignParticipantRole1Response404 | UnassignParticipantRole1Response409
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
        client=client,
        username=username,
    ).parsed


@deprecated_endpoint(None)
async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    *,
    client: AuthenticatedClient | Client,
    username: str | Unset = UNSET,
) -> Response[
    Any
    | UnassignParticipantRole1Response401
    | UnassignParticipantRole1Response404
    | UnassignParticipantRole1Response409
]:
    """Unassign pull request participant

     Unassigns a participant from the REVIEWER role they may have been given in a pull request.

    If the participant has no explicit role this method has no effect.

    Afterwards, the user will still remain a participant in the pull request but their role will be
    reduced to PARTICIPANT. This is because once made a participant of a pull request, a user will
    forever remain a participant. Only their role may be altered.

    The authenticated user must have <strong>REPO_WRITE</strong> permission for the repository that this
    pull request targets to call this resource.

    <strong>Deprecated since 4.2</strong>. Use
    /rest/api/1.0/projects/{projectKey}/repos/{repositorySlug}/pull-
    requests/{pullRequestId}/participants/{userSlug} instead.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        username (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | UnassignParticipantRole1Response401 | UnassignParticipantRole1Response404 | UnassignParticipantRole1Response409]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
        username=username,
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
    username: str | Unset = UNSET,
) -> (
    Any
    | UnassignParticipantRole1Response401
    | UnassignParticipantRole1Response404
    | UnassignParticipantRole1Response409
    | None
):
    """Unassign pull request participant

     Unassigns a participant from the REVIEWER role they may have been given in a pull request.

    If the participant has no explicit role this method has no effect.

    Afterwards, the user will still remain a participant in the pull request but their role will be
    reduced to PARTICIPANT. This is because once made a participant of a pull request, a user will
    forever remain a participant. Only their role may be altered.

    The authenticated user must have <strong>REPO_WRITE</strong> permission for the repository that this
    pull request targets to call this resource.

    <strong>Deprecated since 4.2</strong>. Use
    /rest/api/1.0/projects/{projectKey}/repos/{repositorySlug}/pull-
    requests/{pullRequestId}/participants/{userSlug} instead.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        username (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | UnassignParticipantRole1Response401 | UnassignParticipantRole1Response404 | UnassignParticipantRole1Response409
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            pull_request_id=pull_request_id,
            client=client,
            username=username,
        )
    ).parsed
