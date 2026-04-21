from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.branching_model import BranchingModel
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
    repo_slug: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/repositories/{workspace}/{repo_slug}/branching-model".format(
            workspace=quote(str(workspace), safe=""),
            repo_slug=quote(str(repo_slug), safe=""),
        ),
    }

    return _kwargs


type ParsedPayload = BranchingModel | Error
type ParseResult = BranchingModel | Error | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_200 = BranchingModel.from_dict(response.json())

        return response_200

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
    repo_slug: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """Get the branching model for a repository

     Return the branching model as applied to the repository. This view is
    read-only. The branching model settings can be changed using the
    [settings](#api-repositories-workspace-repo-slug-branching-model-settings-get) API.

    The returned object:

    1. Always has a `development` property. `development.branch` contains
       the actual repository branch object that is considered to be the
       `development` branch. `development.branch` will not be present
       if it does not exist.
    2. Might have a `production` property. `production` will not
       be present when `production` is disabled.
       `production.branch` contains the actual branch object that is
       considered to be the `production` branch. `production.branch` will
       not be present if it does not exist.
    3. Always has a `branch_types` array which contains all enabled branch
       types.

    Args:
        workspace (str):
        repo_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BranchingModel | Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    """Get the branching model for a repository

     Return the branching model as applied to the repository. This view is
    read-only. The branching model settings can be changed using the
    [settings](#api-repositories-workspace-repo-slug-branching-model-settings-get) API.

    The returned object:

    1. Always has a `development` property. `development.branch` contains
       the actual repository branch object that is considered to be the
       `development` branch. `development.branch` will not be present
       if it does not exist.
    2. Might have a `production` property. `production` will not
       be present when `production` is disabled.
       `production.branch` contains the actual branch object that is
       considered to be the `production` branch. `production.branch` will
       not be present if it does not exist.
    3. Always has a `branch_types` array which contains all enabled branch
       types.

    Args:
        workspace (str):
        repo_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BranchingModel | Error
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """Get the branching model for a repository

     Return the branching model as applied to the repository. This view is
    read-only. The branching model settings can be changed using the
    [settings](#api-repositories-workspace-repo-slug-branching-model-settings-get) API.

    The returned object:

    1. Always has a `development` property. `development.branch` contains
       the actual repository branch object that is considered to be the
       `development` branch. `development.branch` will not be present
       if it does not exist.
    2. Might have a `production` property. `production` will not
       be present when `production` is disabled.
       `production.branch` contains the actual branch object that is
       considered to be the `production` branch. `production.branch` will
       not be present if it does not exist.
    3. Always has a `branch_types` array which contains all enabled branch
       types.

    Args:
        workspace (str):
        repo_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BranchingModel | Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    """Get the branching model for a repository

     Return the branching model as applied to the repository. This view is
    read-only. The branching model settings can be changed using the
    [settings](#api-repositories-workspace-repo-slug-branching-model-settings-get) API.

    The returned object:

    1. Always has a `development` property. `development.branch` contains
       the actual repository branch object that is considered to be the
       `development` branch. `development.branch` will not be present
       if it does not exist.
    2. Might have a `production` property. `production` will not
       be present when `production` is disabled.
       `production.branch` contains the actual branch object that is
       considered to be the `production` branch. `production.branch` will
       not be present if it does not exist.
    3. Always has a `branch_types` array which contains all enabled branch
       types.

    Args:
        workspace (str):
        repo_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BranchingModel | Error
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            client=client,
        )
    ).parsed
