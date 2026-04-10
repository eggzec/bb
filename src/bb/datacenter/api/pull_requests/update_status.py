from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_pull_request_assign_status_request import RestPullRequestAssignStatusRequest
from ...models.rest_pull_request_participant import RestPullRequestParticipant
from ...models.update_status_response_400 import UpdateStatusResponse400
from ...models.update_status_response_401 import UpdateStatusResponse401
from ...models.update_status_response_404 import UpdateStatusResponse404
from ...models.update_status_response_409 import UpdateStatusResponse409
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    user_slug: str,
    *,
    body: RestPullRequestAssignStatusRequest,
    version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["version"] = version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/pull-requests/{pull_request_id}/participants/{user_slug}".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            pull_request_id=quote(str(pull_request_id), safe=""),
            user_slug=quote(str(user_slug), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    RestPullRequestParticipant
    | UpdateStatusResponse400
    | UpdateStatusResponse401
    | UpdateStatusResponse404
    | UpdateStatusResponse409
    | None
):
    if response.status_code == 200:
        response_200 = RestPullRequestParticipant.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UpdateStatusResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UpdateStatusResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = UpdateStatusResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = UpdateStatusResponse409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    RestPullRequestParticipant
    | UpdateStatusResponse400
    | UpdateStatusResponse401
    | UpdateStatusResponse404
    | UpdateStatusResponse409
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
    user_slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestPullRequestAssignStatusRequest,
    version: str | Unset = UNSET,
) -> Response[
    RestPullRequestParticipant
    | UpdateStatusResponse400
    | UpdateStatusResponse401
    | UpdateStatusResponse404
    | UpdateStatusResponse409
]:
    r"""Change pull request status

     Change the current user's status for a pull request. Implicitly adds the user as a participant if
    they are not already. If the current user is the author, this method will fail.

    The possible values for {@code status} are <strong>UNAPPROVED</strong>, <strong>NEEDS_WORK</strong>
    (which is referred to as \"Requested changes\" in the frontend from 8.10 onward), or
    <strong>APPROVED</strong>.

    If the new {@code status} is <strong>NEEDS_WORK</strong> or <strong>APPROVED</strong> then the
    {@code lastReviewedCommit} for the participant will be updated to the latest commit of the source
    branch of the pull request.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        user_slug (str):
        version (str | Unset):
        body (RestPullRequestAssignStatusRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestPullRequestParticipant | UpdateStatusResponse400 | UpdateStatusResponse401 | UpdateStatusResponse404 | UpdateStatusResponse409]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
        user_slug=user_slug,
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
    user_slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestPullRequestAssignStatusRequest,
    version: str | Unset = UNSET,
) -> (
    RestPullRequestParticipant
    | UpdateStatusResponse400
    | UpdateStatusResponse401
    | UpdateStatusResponse404
    | UpdateStatusResponse409
    | None
):
    r"""Change pull request status

     Change the current user's status for a pull request. Implicitly adds the user as a participant if
    they are not already. If the current user is the author, this method will fail.

    The possible values for {@code status} are <strong>UNAPPROVED</strong>, <strong>NEEDS_WORK</strong>
    (which is referred to as \"Requested changes\" in the frontend from 8.10 onward), or
    <strong>APPROVED</strong>.

    If the new {@code status} is <strong>NEEDS_WORK</strong> or <strong>APPROVED</strong> then the
    {@code lastReviewedCommit} for the participant will be updated to the latest commit of the source
    branch of the pull request.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        user_slug (str):
        version (str | Unset):
        body (RestPullRequestAssignStatusRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestPullRequestParticipant | UpdateStatusResponse400 | UpdateStatusResponse401 | UpdateStatusResponse404 | UpdateStatusResponse409
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
        user_slug=user_slug,
        client=client,
        body=body,
        version=version,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    user_slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestPullRequestAssignStatusRequest,
    version: str | Unset = UNSET,
) -> Response[
    RestPullRequestParticipant
    | UpdateStatusResponse400
    | UpdateStatusResponse401
    | UpdateStatusResponse404
    | UpdateStatusResponse409
]:
    r"""Change pull request status

     Change the current user's status for a pull request. Implicitly adds the user as a participant if
    they are not already. If the current user is the author, this method will fail.

    The possible values for {@code status} are <strong>UNAPPROVED</strong>, <strong>NEEDS_WORK</strong>
    (which is referred to as \"Requested changes\" in the frontend from 8.10 onward), or
    <strong>APPROVED</strong>.

    If the new {@code status} is <strong>NEEDS_WORK</strong> or <strong>APPROVED</strong> then the
    {@code lastReviewedCommit} for the participant will be updated to the latest commit of the source
    branch of the pull request.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        user_slug (str):
        version (str | Unset):
        body (RestPullRequestAssignStatusRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestPullRequestParticipant | UpdateStatusResponse400 | UpdateStatusResponse401 | UpdateStatusResponse404 | UpdateStatusResponse409]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
        user_slug=user_slug,
        body=body,
        version=version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    user_slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestPullRequestAssignStatusRequest,
    version: str | Unset = UNSET,
) -> (
    RestPullRequestParticipant
    | UpdateStatusResponse400
    | UpdateStatusResponse401
    | UpdateStatusResponse404
    | UpdateStatusResponse409
    | None
):
    r"""Change pull request status

     Change the current user's status for a pull request. Implicitly adds the user as a participant if
    they are not already. If the current user is the author, this method will fail.

    The possible values for {@code status} are <strong>UNAPPROVED</strong>, <strong>NEEDS_WORK</strong>
    (which is referred to as \"Requested changes\" in the frontend from 8.10 onward), or
    <strong>APPROVED</strong>.

    If the new {@code status} is <strong>NEEDS_WORK</strong> or <strong>APPROVED</strong> then the
    {@code lastReviewedCommit} for the participant will be updated to the latest commit of the source
    branch of the pull request.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        user_slug (str):
        version (str | Unset):
        body (RestPullRequestAssignStatusRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestPullRequestParticipant | UpdateStatusResponse400 | UpdateStatusResponse401 | UpdateStatusResponse404 | UpdateStatusResponse409
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            pull_request_id=pull_request_id,
            user_slug=user_slug,
            client=client,
            body=body,
            version=version,
        )
    ).parsed
