from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...deprecation import deprecated_endpoint
from ...models.get_default_branch_1_response_401 import GetDefaultBranch1Response401
from ...models.get_default_branch_1_response_404 import GetDefaultBranch1Response404
from ...models.rest_branch import RestBranch
from ...types import Response


def _get_kwargs(
    project_key: str,
    repository_slug: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/branches/default".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetDefaultBranch1Response401 | GetDefaultBranch1Response404 | RestBranch | None:
    if response.status_code == 200:
        response_200 = RestBranch.from_dict(response.json())

        return response_200

    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = GetDefaultBranch1Response401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetDefaultBranch1Response404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetDefaultBranch1Response401 | GetDefaultBranch1Response404 | RestBranch]:
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
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetDefaultBranch1Response401 | GetDefaultBranch1Response404 | RestBranch]:
    """Get default branch

     Retrieves the repository's default branch, if it has been created. If the repository is empty, 204
    No Content will be returned. For non-empty repositories, if the configured default branch has not
    yet been created a 404 Not Found will be returned.

    This URL is deprecated. Callers should use <code>GET /projects/{key}/repos/{slug}/default-
    branch</code> instead, which allows retrieving the <i>configured</i> default branch even if the ref
    has not been created yet.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetDefaultBranch1Response401 | GetDefaultBranch1Response404 | RestBranch]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated_endpoint(None)
def sync(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetDefaultBranch1Response401 | GetDefaultBranch1Response404 | RestBranch | None:
    """Get default branch

     Retrieves the repository's default branch, if it has been created. If the repository is empty, 204
    No Content will be returned. For non-empty repositories, if the configured default branch has not
    yet been created a 404 Not Found will be returned.

    This URL is deprecated. Callers should use <code>GET /projects/{key}/repos/{slug}/default-
    branch</code> instead, which allows retrieving the <i>configured</i> default branch even if the ref
    has not been created yet.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetDefaultBranch1Response401 | GetDefaultBranch1Response404 | RestBranch
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        client=client,
    ).parsed


@deprecated_endpoint(None)
async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetDefaultBranch1Response401 | GetDefaultBranch1Response404 | RestBranch]:
    """Get default branch

     Retrieves the repository's default branch, if it has been created. If the repository is empty, 204
    No Content will be returned. For non-empty repositories, if the configured default branch has not
    yet been created a 404 Not Found will be returned.

    This URL is deprecated. Callers should use <code>GET /projects/{key}/repos/{slug}/default-
    branch</code> instead, which allows retrieving the <i>configured</i> default branch even if the ref
    has not been created yet.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetDefaultBranch1Response401 | GetDefaultBranch1Response404 | RestBranch]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated_endpoint(None)
async def asyncio(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetDefaultBranch1Response401 | GetDefaultBranch1Response404 | RestBranch | None:
    """Get default branch

     Retrieves the repository's default branch, if it has been created. If the repository is empty, 204
    No Content will be returned. For non-empty repositories, if the configured default branch has not
    yet been created a 404 Not Found will be returned.

    This URL is deprecated. Callers should use <code>GET /projects/{key}/repos/{slug}/default-
    branch</code> instead, which allows retrieving the <i>configured</i> default branch even if the ref
    has not been created yet.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetDefaultBranch1Response401 | GetDefaultBranch1Response404 | RestBranch
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            client=client,
        )
    ).parsed
