from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.branching_model_settings import BranchingModelSettings
from ...models.error import Error
from ...types import Response

__all__ = [
    "sync_detailed",
    "asyncio_detailed",
    "sync",
    "asyncio",
]


def _get_kwargs(
    workspace: str,
    project_key: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/workspaces/{workspace}/projects/{project_key}/branching-model/settings".format(
            workspace=quote(str(workspace), safe=""),
            project_key=quote(str(project_key), safe=""),
        ),
    }

    return _kwargs


type ParsedPayload = BranchingModelSettings | Error
type ParseResult = BranchingModelSettings | Error | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_200 = BranchingModelSettings.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_404 = Error.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ParsedPayload]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace: str,
    project_key: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """Update the branching model config for a project

     Update the branching model configuration for a project.

    The `development` branch can be configured to a specific branch or to
    track the main branch. Any branch name can be supplied, but will only
    successfully be applied to a repository via inheritance if that branch
    exists for that repository. Only the passed properties will be updated. The
    properties not passed will be left unchanged. A request without a
    `development` property will leave the development branch unchanged.

    The `production` branch can be a specific branch, the main
    branch or disabled. Any branch name can be supplied, but will only
    successfully be applied to a repository via inheritance if that branch
    exists for that repository. The `enabled` property can be used to enable (`true`)
    or disable (`false`) it. Only the passed properties will be updated. The
    properties not passed will be left unchanged. A request without a
    `production` property will leave the production branch unchanged.

    The `branch_types` property contains the branch types to be updated.
    Only the branch types passed will be updated. All updates will be
    rejected if it would leave the branching model in an invalid state.
    For branch types this means that:

    1. The prefixes for all enabled branch types are valid. For example,
       it is not possible to use '*' inside a Git prefix.
    2. A prefix of an enabled branch type must not be a prefix of another
       enabled branch type. This is to ensure that a branch can be easily
       classified by its prefix unambiguously.

    It is possible to store an invalid prefix if that branch type would be
    left disabled. Only the passed properties will be updated. The
    properties not passed will be left unchanged. Each branch type must
    have a `kind` property to identify it.

    The `default_branch_deletion` property is a string. The value of `true`
    indicates to delete branches by default. The value of `false` indicates
    that branches will not be deleted by default. A request without a
    `default_branch_deletion` property will leave it unchanged. Other values
    would be ignored.

    Args:
        workspace (str):
        project_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BranchingModelSettings | Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        project_key=project_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    project_key: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    """Update the branching model config for a project

     Update the branching model configuration for a project.

    The `development` branch can be configured to a specific branch or to
    track the main branch. Any branch name can be supplied, but will only
    successfully be applied to a repository via inheritance if that branch
    exists for that repository. Only the passed properties will be updated. The
    properties not passed will be left unchanged. A request without a
    `development` property will leave the development branch unchanged.

    The `production` branch can be a specific branch, the main
    branch or disabled. Any branch name can be supplied, but will only
    successfully be applied to a repository via inheritance if that branch
    exists for that repository. The `enabled` property can be used to enable (`true`)
    or disable (`false`) it. Only the passed properties will be updated. The
    properties not passed will be left unchanged. A request without a
    `production` property will leave the production branch unchanged.

    The `branch_types` property contains the branch types to be updated.
    Only the branch types passed will be updated. All updates will be
    rejected if it would leave the branching model in an invalid state.
    For branch types this means that:

    1. The prefixes for all enabled branch types are valid. For example,
       it is not possible to use '*' inside a Git prefix.
    2. A prefix of an enabled branch type must not be a prefix of another
       enabled branch type. This is to ensure that a branch can be easily
       classified by its prefix unambiguously.

    It is possible to store an invalid prefix if that branch type would be
    left disabled. Only the passed properties will be updated. The
    properties not passed will be left unchanged. Each branch type must
    have a `kind` property to identify it.

    The `default_branch_deletion` property is a string. The value of `true`
    indicates to delete branches by default. The value of `false` indicates
    that branches will not be deleted by default. A request without a
    `default_branch_deletion` property will leave it unchanged. Other values
    would be ignored.

    Args:
        workspace (str):
        project_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BranchingModelSettings | Error
    """

    return sync_detailed(
        workspace=workspace,
        project_key=project_key,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    project_key: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """Update the branching model config for a project

     Update the branching model configuration for a project.

    The `development` branch can be configured to a specific branch or to
    track the main branch. Any branch name can be supplied, but will only
    successfully be applied to a repository via inheritance if that branch
    exists for that repository. Only the passed properties will be updated. The
    properties not passed will be left unchanged. A request without a
    `development` property will leave the development branch unchanged.

    The `production` branch can be a specific branch, the main
    branch or disabled. Any branch name can be supplied, but will only
    successfully be applied to a repository via inheritance if that branch
    exists for that repository. The `enabled` property can be used to enable (`true`)
    or disable (`false`) it. Only the passed properties will be updated. The
    properties not passed will be left unchanged. A request without a
    `production` property will leave the production branch unchanged.

    The `branch_types` property contains the branch types to be updated.
    Only the branch types passed will be updated. All updates will be
    rejected if it would leave the branching model in an invalid state.
    For branch types this means that:

    1. The prefixes for all enabled branch types are valid. For example,
       it is not possible to use '*' inside a Git prefix.
    2. A prefix of an enabled branch type must not be a prefix of another
       enabled branch type. This is to ensure that a branch can be easily
       classified by its prefix unambiguously.

    It is possible to store an invalid prefix if that branch type would be
    left disabled. Only the passed properties will be updated. The
    properties not passed will be left unchanged. Each branch type must
    have a `kind` property to identify it.

    The `default_branch_deletion` property is a string. The value of `true`
    indicates to delete branches by default. The value of `false` indicates
    that branches will not be deleted by default. A request without a
    `default_branch_deletion` property will leave it unchanged. Other values
    would be ignored.

    Args:
        workspace (str):
        project_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BranchingModelSettings | Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        project_key=project_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    project_key: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    """Update the branching model config for a project

     Update the branching model configuration for a project.

    The `development` branch can be configured to a specific branch or to
    track the main branch. Any branch name can be supplied, but will only
    successfully be applied to a repository via inheritance if that branch
    exists for that repository. Only the passed properties will be updated. The
    properties not passed will be left unchanged. A request without a
    `development` property will leave the development branch unchanged.

    The `production` branch can be a specific branch, the main
    branch or disabled. Any branch name can be supplied, but will only
    successfully be applied to a repository via inheritance if that branch
    exists for that repository. The `enabled` property can be used to enable (`true`)
    or disable (`false`) it. Only the passed properties will be updated. The
    properties not passed will be left unchanged. A request without a
    `production` property will leave the production branch unchanged.

    The `branch_types` property contains the branch types to be updated.
    Only the branch types passed will be updated. All updates will be
    rejected if it would leave the branching model in an invalid state.
    For branch types this means that:

    1. The prefixes for all enabled branch types are valid. For example,
       it is not possible to use '*' inside a Git prefix.
    2. A prefix of an enabled branch type must not be a prefix of another
       enabled branch type. This is to ensure that a branch can be easily
       classified by its prefix unambiguously.

    It is possible to store an invalid prefix if that branch type would be
    left disabled. Only the passed properties will be updated. The
    properties not passed will be left unchanged. Each branch type must
    have a `kind` property to identify it.

    The `default_branch_deletion` property is a string. The value of `true`
    indicates to delete branches by default. The value of `false` indicates
    that branches will not be deleted by default. A request without a
    `default_branch_deletion` property will leave it unchanged. Other values
    would be ignored.

    Args:
        workspace (str):
        project_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BranchingModelSettings | Error
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            project_key=project_key,
            client=client,
        )
    ).parsed
