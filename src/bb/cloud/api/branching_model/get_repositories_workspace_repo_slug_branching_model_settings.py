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
    repo_slug: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/repositories/{workspace}/{repo_slug}/branching-model/settings".format(
            workspace=quote(str(workspace), safe=""),
            repo_slug=quote(str(repo_slug), safe=""),
        ),
    }

    return _kwargs


type ParsedPayload = BranchingModelSettings | Error
type ParseResult = BranchingModelSettings | Error | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        response_200 = BranchingModelSettings.from_dict(response.json())

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
    repo_slug: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """Get the branching model config for a repository

     Return the branching model configuration for a repository. The returned
    object:

    1. Always has a `development` property for the development branch.
    2. Always a `production` property for the production branch. The
       production branch can be disabled.
    3. The `branch_types` contains all the branch types.
    4. `default_branch_deletion` indicates whether branches will be
        deleted by default on merge.

    This is the raw configuration for the branching model. A client
    wishing to see the branching model with its actual current branches may
    find the [active model API](/cloud/bitbucket/rest/api-group-branching-model/#api-repositories-
    workspace-repo-slug-branching-model-get) more useful.

    Args:
        workspace (str):
        repo_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BranchingModelSettings | Error]
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
    """Get the branching model config for a repository

     Return the branching model configuration for a repository. The returned
    object:

    1. Always has a `development` property for the development branch.
    2. Always a `production` property for the production branch. The
       production branch can be disabled.
    3. The `branch_types` contains all the branch types.
    4. `default_branch_deletion` indicates whether branches will be
        deleted by default on merge.

    This is the raw configuration for the branching model. A client
    wishing to see the branching model with its actual current branches may
    find the [active model API](/cloud/bitbucket/rest/api-group-branching-model/#api-repositories-
    workspace-repo-slug-branching-model-get) more useful.

    Args:
        workspace (str):
        repo_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BranchingModelSettings | Error
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
    """Get the branching model config for a repository

     Return the branching model configuration for a repository. The returned
    object:

    1. Always has a `development` property for the development branch.
    2. Always a `production` property for the production branch. The
       production branch can be disabled.
    3. The `branch_types` contains all the branch types.
    4. `default_branch_deletion` indicates whether branches will be
        deleted by default on merge.

    This is the raw configuration for the branching model. A client
    wishing to see the branching model with its actual current branches may
    find the [active model API](/cloud/bitbucket/rest/api-group-branching-model/#api-repositories-
    workspace-repo-slug-branching-model-get) more useful.

    Args:
        workspace (str):
        repo_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BranchingModelSettings | Error]
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
    """Get the branching model config for a repository

     Return the branching model configuration for a repository. The returned
    object:

    1. Always has a `development` property for the development branch.
    2. Always a `production` property for the production branch. The
       production branch can be disabled.
    3. The `branch_types` contains all the branch types.
    4. `default_branch_deletion` indicates whether branches will be
        deleted by default on merge.

    This is the raw configuration for the branching model. A client
    wishing to see the branching model with its actual current branches may
    find the [active model API](/cloud/bitbucket/rest/api-group-branching-model/#api-repositories-
    workspace-repo-slug-branching-model-get) more useful.

    Args:
        workspace (str):
        repo_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BranchingModelSettings | Error
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            client=client,
        )
    ).parsed
