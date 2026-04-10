from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_pull_request_settings_1_response_401 import GetPullRequestSettings1Response401
from ...models.get_pull_request_settings_1_response_404 import GetPullRequestSettings1Response404
from ...models.rest_repository_pull_request_settings import RestRepositoryPullRequestSettings
from ...types import Response


def _get_kwargs(
    project_key: str,
    repository_slug: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/settings/pull-requests".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetPullRequestSettings1Response401 | GetPullRequestSettings1Response404 | RestRepositoryPullRequestSettings | None:
    if response.status_code == 200:
        response_200 = RestRepositoryPullRequestSettings.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetPullRequestSettings1Response401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetPullRequestSettings1Response404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetPullRequestSettings1Response401 | GetPullRequestSettings1Response404 | RestRepositoryPullRequestSettings
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
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetPullRequestSettings1Response401 | GetPullRequestSettings1Response404 | RestRepositoryPullRequestSettings
]:
    """Get pull request settings

     Retrieve the pull request settings for the context repository.

    The authenticated user must have <strong>REPO_READ</strong> permission for the context repository to
    call this resource.

    This resource will call all RestFragments that are registered with the key
    <strong>bitbucket.repository.settings.pullRequests</strong>. If any fragment fails validations by
    returning a non-empty Map of errors, then no fragments will execute.

    The property keys for the settings that are bundled with the application are

    - mergeConfig - the merge strategy configuration for pull requests
    - requiredApprovers - (Deprecated, please use com.atlassian.bitbucket.server.bundled-
    hooks.requiredApproversMergeHook instead) the number of approvals required on a pull request for it
    to be mergeable, or 0 if the merge check is disabled
    - com.atlassian.bitbucket.server.bundled-hooks.requiredApproversMergeHook - the merge check
    configuration for required approvers
    - requiredAllApprovers - whether or not all approvers must approve a pull request for it to be
    mergeable
    - requiredAllTasksComplete - whether or not all tasks on a pull request need to be completed for it
    to be mergeable
    - requiredSuccessfulBuilds - (Deprecated, please use com.atlassian.bitbucket.server.bitbucket-
    build.requiredBuildsMergeCheck instead) the number of successful builds on a pull request for it to
    be mergeable, or 0 if the merge check is disabled
    - com.atlassian.bitbucket.server.bitbucket-build.requiredBuildsMergeCheck - the merge check
    configuration for required builds



    Args:
        project_key (str):
        repository_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPullRequestSettings1Response401 | GetPullRequestSettings1Response404 | RestRepositoryPullRequestSettings]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
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
) -> GetPullRequestSettings1Response401 | GetPullRequestSettings1Response404 | RestRepositoryPullRequestSettings | None:
    """Get pull request settings

     Retrieve the pull request settings for the context repository.

    The authenticated user must have <strong>REPO_READ</strong> permission for the context repository to
    call this resource.

    This resource will call all RestFragments that are registered with the key
    <strong>bitbucket.repository.settings.pullRequests</strong>. If any fragment fails validations by
    returning a non-empty Map of errors, then no fragments will execute.

    The property keys for the settings that are bundled with the application are

    - mergeConfig - the merge strategy configuration for pull requests
    - requiredApprovers - (Deprecated, please use com.atlassian.bitbucket.server.bundled-
    hooks.requiredApproversMergeHook instead) the number of approvals required on a pull request for it
    to be mergeable, or 0 if the merge check is disabled
    - com.atlassian.bitbucket.server.bundled-hooks.requiredApproversMergeHook - the merge check
    configuration for required approvers
    - requiredAllApprovers - whether or not all approvers must approve a pull request for it to be
    mergeable
    - requiredAllTasksComplete - whether or not all tasks on a pull request need to be completed for it
    to be mergeable
    - requiredSuccessfulBuilds - (Deprecated, please use com.atlassian.bitbucket.server.bitbucket-
    build.requiredBuildsMergeCheck instead) the number of successful builds on a pull request for it to
    be mergeable, or 0 if the merge check is disabled
    - com.atlassian.bitbucket.server.bitbucket-build.requiredBuildsMergeCheck - the merge check
    configuration for required builds



    Args:
        project_key (str):
        repository_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPullRequestSettings1Response401 | GetPullRequestSettings1Response404 | RestRepositoryPullRequestSettings
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetPullRequestSettings1Response401 | GetPullRequestSettings1Response404 | RestRepositoryPullRequestSettings
]:
    """Get pull request settings

     Retrieve the pull request settings for the context repository.

    The authenticated user must have <strong>REPO_READ</strong> permission for the context repository to
    call this resource.

    This resource will call all RestFragments that are registered with the key
    <strong>bitbucket.repository.settings.pullRequests</strong>. If any fragment fails validations by
    returning a non-empty Map of errors, then no fragments will execute.

    The property keys for the settings that are bundled with the application are

    - mergeConfig - the merge strategy configuration for pull requests
    - requiredApprovers - (Deprecated, please use com.atlassian.bitbucket.server.bundled-
    hooks.requiredApproversMergeHook instead) the number of approvals required on a pull request for it
    to be mergeable, or 0 if the merge check is disabled
    - com.atlassian.bitbucket.server.bundled-hooks.requiredApproversMergeHook - the merge check
    configuration for required approvers
    - requiredAllApprovers - whether or not all approvers must approve a pull request for it to be
    mergeable
    - requiredAllTasksComplete - whether or not all tasks on a pull request need to be completed for it
    to be mergeable
    - requiredSuccessfulBuilds - (Deprecated, please use com.atlassian.bitbucket.server.bitbucket-
    build.requiredBuildsMergeCheck instead) the number of successful builds on a pull request for it to
    be mergeable, or 0 if the merge check is disabled
    - com.atlassian.bitbucket.server.bitbucket-build.requiredBuildsMergeCheck - the merge check
    configuration for required builds



    Args:
        project_key (str):
        repository_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPullRequestSettings1Response401 | GetPullRequestSettings1Response404 | RestRepositoryPullRequestSettings]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetPullRequestSettings1Response401 | GetPullRequestSettings1Response404 | RestRepositoryPullRequestSettings | None:
    """Get pull request settings

     Retrieve the pull request settings for the context repository.

    The authenticated user must have <strong>REPO_READ</strong> permission for the context repository to
    call this resource.

    This resource will call all RestFragments that are registered with the key
    <strong>bitbucket.repository.settings.pullRequests</strong>. If any fragment fails validations by
    returning a non-empty Map of errors, then no fragments will execute.

    The property keys for the settings that are bundled with the application are

    - mergeConfig - the merge strategy configuration for pull requests
    - requiredApprovers - (Deprecated, please use com.atlassian.bitbucket.server.bundled-
    hooks.requiredApproversMergeHook instead) the number of approvals required on a pull request for it
    to be mergeable, or 0 if the merge check is disabled
    - com.atlassian.bitbucket.server.bundled-hooks.requiredApproversMergeHook - the merge check
    configuration for required approvers
    - requiredAllApprovers - whether or not all approvers must approve a pull request for it to be
    mergeable
    - requiredAllTasksComplete - whether or not all tasks on a pull request need to be completed for it
    to be mergeable
    - requiredSuccessfulBuilds - (Deprecated, please use com.atlassian.bitbucket.server.bitbucket-
    build.requiredBuildsMergeCheck instead) the number of successful builds on a pull request for it to
    be mergeable, or 0 if the merge check is disabled
    - com.atlassian.bitbucket.server.bitbucket-build.requiredBuildsMergeCheck - the merge check
    configuration for required builds



    Args:
        project_key (str):
        repository_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPullRequestSettings1Response401 | GetPullRequestSettings1Response404 | RestRepositoryPullRequestSettings
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            client=client,
        )
    ).parsed
