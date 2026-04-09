from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.project_branching_model import ProjectBranchingModel
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
        "method": "get",
        "url": "/workspaces/{workspace}/projects/{project_key}/branching-model".format(
            workspace=quote(str(workspace), safe=""),
            project_key=quote(str(project_key), safe=""),
        ),
    }

    return _kwargs


type ParsedPayload = Error | ProjectBranchingModel
type ParseResult = Error | ProjectBranchingModel | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        response_200 = ProjectBranchingModel.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 404:
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
    """Get the branching model for a project

     Return the branching model set at the project level. This view is
    read-only. The branching model settings can be changed using the
    [settings](#api-workspaces-workspace-projects-project-key-branching-model-settings-get)
    API.

    The returned object:

    1. Always has a `development` property. `development.name` is
       the user-specified branch that can be inherited by an individual repository's
       branching model.
    2. Might have a `production` property. `production` will not
       be present when `production` is disabled.
       `production.name` is the user-specified branch that can be
       inherited by an individual repository's branching model.
    3. Always has a `branch_types` array which contains all enabled branch
       types.

    Args:
        workspace (str):
        project_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ProjectBranchingModel]
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
    """Get the branching model for a project

     Return the branching model set at the project level. This view is
    read-only. The branching model settings can be changed using the
    [settings](#api-workspaces-workspace-projects-project-key-branching-model-settings-get)
    API.

    The returned object:

    1. Always has a `development` property. `development.name` is
       the user-specified branch that can be inherited by an individual repository's
       branching model.
    2. Might have a `production` property. `production` will not
       be present when `production` is disabled.
       `production.name` is the user-specified branch that can be
       inherited by an individual repository's branching model.
    3. Always has a `branch_types` array which contains all enabled branch
       types.

    Args:
        workspace (str):
        project_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ProjectBranchingModel
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
    """Get the branching model for a project

     Return the branching model set at the project level. This view is
    read-only. The branching model settings can be changed using the
    [settings](#api-workspaces-workspace-projects-project-key-branching-model-settings-get)
    API.

    The returned object:

    1. Always has a `development` property. `development.name` is
       the user-specified branch that can be inherited by an individual repository's
       branching model.
    2. Might have a `production` property. `production` will not
       be present when `production` is disabled.
       `production.name` is the user-specified branch that can be
       inherited by an individual repository's branching model.
    3. Always has a `branch_types` array which contains all enabled branch
       types.

    Args:
        workspace (str):
        project_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ProjectBranchingModel]
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
    """Get the branching model for a project

     Return the branching model set at the project level. This view is
    read-only. The branching model settings can be changed using the
    [settings](#api-workspaces-workspace-projects-project-key-branching-model-settings-get)
    API.

    The returned object:

    1. Always has a `development` property. `development.name` is
       the user-specified branch that can be inherited by an individual repository's
       branching model.
    2. Might have a `production` property. `production` will not
       be present when `production` is disabled.
       `production.name` is the user-specified branch that can be
       inherited by an individual repository's branching model.
    3. Always has a `branch_types` array which contains all enabled branch
       types.

    Args:
        workspace (str):
        project_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ProjectBranchingModel
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            project_key=project_key,
            client=client,
        )
    ).parsed
