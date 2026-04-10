from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_default_branch_2_response_401 import GetDefaultBranch2Response401
from ...models.get_default_branch_2_response_404 import GetDefaultBranch2Response404
from ...models.rest_minimal_ref import RestMinimalRef
from ...types import Response


def _get_kwargs(
    project_key: str,
    repository_slug: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/default-branch".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetDefaultBranch2Response401 | GetDefaultBranch2Response404 | RestMinimalRef | None:
    if response.status_code == 200:
        response_200 = RestMinimalRef.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetDefaultBranch2Response401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetDefaultBranch2Response404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetDefaultBranch2Response401 | GetDefaultBranch2Response404 | RestMinimalRef]:
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
) -> Response[GetDefaultBranch2Response401 | GetDefaultBranch2Response404 | RestMinimalRef]:
    """Get repository default branch

     Retrieves the repository's <i>configured</i> default branch.

    Every repository has a <i>configured</i> default branch, but that branch may not actually
    <i>exist</i> in the repository. For example, a newly-created repository will have a configured
    default branch even though no branches have been pushed yet.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetDefaultBranch2Response401 | GetDefaultBranch2Response404 | RestMinimalRef]
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
) -> GetDefaultBranch2Response401 | GetDefaultBranch2Response404 | RestMinimalRef | None:
    """Get repository default branch

     Retrieves the repository's <i>configured</i> default branch.

    Every repository has a <i>configured</i> default branch, but that branch may not actually
    <i>exist</i> in the repository. For example, a newly-created repository will have a configured
    default branch even though no branches have been pushed yet.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetDefaultBranch2Response401 | GetDefaultBranch2Response404 | RestMinimalRef
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
) -> Response[GetDefaultBranch2Response401 | GetDefaultBranch2Response404 | RestMinimalRef]:
    """Get repository default branch

     Retrieves the repository's <i>configured</i> default branch.

    Every repository has a <i>configured</i> default branch, but that branch may not actually
    <i>exist</i> in the repository. For example, a newly-created repository will have a configured
    default branch even though no branches have been pushed yet.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetDefaultBranch2Response401 | GetDefaultBranch2Response404 | RestMinimalRef]
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
) -> GetDefaultBranch2Response401 | GetDefaultBranch2Response404 | RestMinimalRef | None:
    """Get repository default branch

     Retrieves the repository's <i>configured</i> default branch.

    Every repository has a <i>configured</i> default branch, but that branch may not actually
    <i>exist</i> in the repository. For example, a newly-created repository will have a configured
    default branch even though no branches have been pushed yet.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetDefaultBranch2Response401 | GetDefaultBranch2Response404 | RestMinimalRef
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            client=client,
        )
    ).parsed
