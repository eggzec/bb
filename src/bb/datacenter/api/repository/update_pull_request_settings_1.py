from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_repository_pull_request_settings import RestRepositoryPullRequestSettings
from ...models.update_pull_request_settings_1_response_400 import UpdatePullRequestSettings1Response400
from ...models.update_pull_request_settings_1_response_401 import UpdatePullRequestSettings1Response401
from ...models.update_pull_request_settings_1_response_404 import UpdatePullRequestSettings1Response404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    *,
    body: RestRepositoryPullRequestSettings | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/settings/pull-requests".format(
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
) -> (
    RestRepositoryPullRequestSettings
    | UpdatePullRequestSettings1Response400
    | UpdatePullRequestSettings1Response401
    | UpdatePullRequestSettings1Response404
    | None
):
    if response.status_code == 200:
        response_200 = RestRepositoryPullRequestSettings.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UpdatePullRequestSettings1Response400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UpdatePullRequestSettings1Response401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = UpdatePullRequestSettings1Response404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    RestRepositoryPullRequestSettings
    | UpdatePullRequestSettings1Response400
    | UpdatePullRequestSettings1Response401
    | UpdatePullRequestSettings1Response404
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
    body: RestRepositoryPullRequestSettings | Unset = UNSET,
) -> Response[
    RestRepositoryPullRequestSettings
    | UpdatePullRequestSettings1Response400
    | UpdatePullRequestSettings1Response401
    | UpdatePullRequestSettings1Response404
]:
    r"""Update pull request settings

     Update the pull request settings for the context repository.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the context repository
    to call this resource.

    This resource will call all RestFragments that are registered with the key
    <strong>bitbucket.repository.settings.pullRequests</strong>. If any fragment fails validations by
    returning a non-empty Map of errors, then no fragments will execute.

    Only the settings that should be updated need to be included in the request.

    The property keys for the settings that are bundled with the application are

    - mergeConfig - the merge strategy configuration for pull requests
    - requiredApprovers - (Deprecated, please use com.atlassian.bitbucket.server.bundled-
    hooks.requiredApproversMergeHook instead) the number of approvals required on a pull request for it
    to be mergeable, or 0 to disable the merge check
    - com.atlassian.bitbucket.server.bundled-hooks.requiredApproversMergeHook - a json map containing
    the keys 'enabled' (a boolean to enable or disable this merge check) and 'count' (an integer to set
    the number of required approvals)
    - requiredAllApprovers - whether or not all approvers must approve a pull request for it to be
    mergeable
    - requiredAllTasksComplete - whether or not all tasks on a pull request need to be completed for it
    to be mergeable
    - requiredSuccessfulBuilds - (Deprecated, please use com.atlassian.bitbucket.server.bitbucket-
    build.requiredBuildsMergeCheck instead) the number of successful builds on a pull request for it to
    be mergeable, or 0 to disable the merge check
    - com.atlassian.bitbucket.server.bitbucket-build.requiredBuildsMergeCheck - a json map containing
    the keys 'enabled' (a boolean to enable or disable this merge check) and 'count' (an integer to set
    the number of required builds)


    <strong>Merge strategy configuration deletion:</strong>

    An explicitly set pull request merge strategy configuration can be deleted by POSTing a document
    with an empty \"mergeConfig\" attribute. i.e:


    ```{
        \"mergeConfig\": {
        }
    }
    ```

    Upon completion of this request, the effective configuration will be:

    - The configuration set for this repository's SCM type as set at the project level, if present,
    otherwise
    - the configuration set for this repository's SCM type as set at the instance level, if present,
    otherwise
    - the default configuration for this repository's SCM type



    Args:
        project_key (str):
        repository_slug (str):
        body (RestRepositoryPullRequestSettings | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestRepositoryPullRequestSettings | UpdatePullRequestSettings1Response400 | UpdatePullRequestSettings1Response401 | UpdatePullRequestSettings1Response404]
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
    body: RestRepositoryPullRequestSettings | Unset = UNSET,
) -> (
    RestRepositoryPullRequestSettings
    | UpdatePullRequestSettings1Response400
    | UpdatePullRequestSettings1Response401
    | UpdatePullRequestSettings1Response404
    | None
):
    r"""Update pull request settings

     Update the pull request settings for the context repository.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the context repository
    to call this resource.

    This resource will call all RestFragments that are registered with the key
    <strong>bitbucket.repository.settings.pullRequests</strong>. If any fragment fails validations by
    returning a non-empty Map of errors, then no fragments will execute.

    Only the settings that should be updated need to be included in the request.

    The property keys for the settings that are bundled with the application are

    - mergeConfig - the merge strategy configuration for pull requests
    - requiredApprovers - (Deprecated, please use com.atlassian.bitbucket.server.bundled-
    hooks.requiredApproversMergeHook instead) the number of approvals required on a pull request for it
    to be mergeable, or 0 to disable the merge check
    - com.atlassian.bitbucket.server.bundled-hooks.requiredApproversMergeHook - a json map containing
    the keys 'enabled' (a boolean to enable or disable this merge check) and 'count' (an integer to set
    the number of required approvals)
    - requiredAllApprovers - whether or not all approvers must approve a pull request for it to be
    mergeable
    - requiredAllTasksComplete - whether or not all tasks on a pull request need to be completed for it
    to be mergeable
    - requiredSuccessfulBuilds - (Deprecated, please use com.atlassian.bitbucket.server.bitbucket-
    build.requiredBuildsMergeCheck instead) the number of successful builds on a pull request for it to
    be mergeable, or 0 to disable the merge check
    - com.atlassian.bitbucket.server.bitbucket-build.requiredBuildsMergeCheck - a json map containing
    the keys 'enabled' (a boolean to enable or disable this merge check) and 'count' (an integer to set
    the number of required builds)


    <strong>Merge strategy configuration deletion:</strong>

    An explicitly set pull request merge strategy configuration can be deleted by POSTing a document
    with an empty \"mergeConfig\" attribute. i.e:


    ```{
        \"mergeConfig\": {
        }
    }
    ```

    Upon completion of this request, the effective configuration will be:

    - The configuration set for this repository's SCM type as set at the project level, if present,
    otherwise
    - the configuration set for this repository's SCM type as set at the instance level, if present,
    otherwise
    - the default configuration for this repository's SCM type



    Args:
        project_key (str):
        repository_slug (str):
        body (RestRepositoryPullRequestSettings | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestRepositoryPullRequestSettings | UpdatePullRequestSettings1Response400 | UpdatePullRequestSettings1Response401 | UpdatePullRequestSettings1Response404
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
    body: RestRepositoryPullRequestSettings | Unset = UNSET,
) -> Response[
    RestRepositoryPullRequestSettings
    | UpdatePullRequestSettings1Response400
    | UpdatePullRequestSettings1Response401
    | UpdatePullRequestSettings1Response404
]:
    r"""Update pull request settings

     Update the pull request settings for the context repository.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the context repository
    to call this resource.

    This resource will call all RestFragments that are registered with the key
    <strong>bitbucket.repository.settings.pullRequests</strong>. If any fragment fails validations by
    returning a non-empty Map of errors, then no fragments will execute.

    Only the settings that should be updated need to be included in the request.

    The property keys for the settings that are bundled with the application are

    - mergeConfig - the merge strategy configuration for pull requests
    - requiredApprovers - (Deprecated, please use com.atlassian.bitbucket.server.bundled-
    hooks.requiredApproversMergeHook instead) the number of approvals required on a pull request for it
    to be mergeable, or 0 to disable the merge check
    - com.atlassian.bitbucket.server.bundled-hooks.requiredApproversMergeHook - a json map containing
    the keys 'enabled' (a boolean to enable or disable this merge check) and 'count' (an integer to set
    the number of required approvals)
    - requiredAllApprovers - whether or not all approvers must approve a pull request for it to be
    mergeable
    - requiredAllTasksComplete - whether or not all tasks on a pull request need to be completed for it
    to be mergeable
    - requiredSuccessfulBuilds - (Deprecated, please use com.atlassian.bitbucket.server.bitbucket-
    build.requiredBuildsMergeCheck instead) the number of successful builds on a pull request for it to
    be mergeable, or 0 to disable the merge check
    - com.atlassian.bitbucket.server.bitbucket-build.requiredBuildsMergeCheck - a json map containing
    the keys 'enabled' (a boolean to enable or disable this merge check) and 'count' (an integer to set
    the number of required builds)


    <strong>Merge strategy configuration deletion:</strong>

    An explicitly set pull request merge strategy configuration can be deleted by POSTing a document
    with an empty \"mergeConfig\" attribute. i.e:


    ```{
        \"mergeConfig\": {
        }
    }
    ```

    Upon completion of this request, the effective configuration will be:

    - The configuration set for this repository's SCM type as set at the project level, if present,
    otherwise
    - the configuration set for this repository's SCM type as set at the instance level, if present,
    otherwise
    - the default configuration for this repository's SCM type



    Args:
        project_key (str):
        repository_slug (str):
        body (RestRepositoryPullRequestSettings | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestRepositoryPullRequestSettings | UpdatePullRequestSettings1Response400 | UpdatePullRequestSettings1Response401 | UpdatePullRequestSettings1Response404]
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
    body: RestRepositoryPullRequestSettings | Unset = UNSET,
) -> (
    RestRepositoryPullRequestSettings
    | UpdatePullRequestSettings1Response400
    | UpdatePullRequestSettings1Response401
    | UpdatePullRequestSettings1Response404
    | None
):
    r"""Update pull request settings

     Update the pull request settings for the context repository.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the context repository
    to call this resource.

    This resource will call all RestFragments that are registered with the key
    <strong>bitbucket.repository.settings.pullRequests</strong>. If any fragment fails validations by
    returning a non-empty Map of errors, then no fragments will execute.

    Only the settings that should be updated need to be included in the request.

    The property keys for the settings that are bundled with the application are

    - mergeConfig - the merge strategy configuration for pull requests
    - requiredApprovers - (Deprecated, please use com.atlassian.bitbucket.server.bundled-
    hooks.requiredApproversMergeHook instead) the number of approvals required on a pull request for it
    to be mergeable, or 0 to disable the merge check
    - com.atlassian.bitbucket.server.bundled-hooks.requiredApproversMergeHook - a json map containing
    the keys 'enabled' (a boolean to enable or disable this merge check) and 'count' (an integer to set
    the number of required approvals)
    - requiredAllApprovers - whether or not all approvers must approve a pull request for it to be
    mergeable
    - requiredAllTasksComplete - whether or not all tasks on a pull request need to be completed for it
    to be mergeable
    - requiredSuccessfulBuilds - (Deprecated, please use com.atlassian.bitbucket.server.bitbucket-
    build.requiredBuildsMergeCheck instead) the number of successful builds on a pull request for it to
    be mergeable, or 0 to disable the merge check
    - com.atlassian.bitbucket.server.bitbucket-build.requiredBuildsMergeCheck - a json map containing
    the keys 'enabled' (a boolean to enable or disable this merge check) and 'count' (an integer to set
    the number of required builds)


    <strong>Merge strategy configuration deletion:</strong>

    An explicitly set pull request merge strategy configuration can be deleted by POSTing a document
    with an empty \"mergeConfig\" attribute. i.e:


    ```{
        \"mergeConfig\": {
        }
    }
    ```

    Upon completion of this request, the effective configuration will be:

    - The configuration set for this repository's SCM type as set at the project level, if present,
    otherwise
    - the configuration set for this repository's SCM type as set at the instance level, if present,
    otherwise
    - the default configuration for this repository's SCM type



    Args:
        project_key (str):
        repository_slug (str):
        body (RestRepositoryPullRequestSettings | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestRepositoryPullRequestSettings | UpdatePullRequestSettings1Response400 | UpdatePullRequestSettings1Response401 | UpdatePullRequestSettings1Response404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            client=client,
            body=body,
        )
    ).parsed
