from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_all_repos_for_project_include_default_branch import GetAllReposForProjectIncludeDefaultBranch
from ...models.get_all_repos_for_project_response_200 import GetAllReposForProjectResponse200
from ...models.get_all_repos_for_project_response_409 import GetAllReposForProjectResponse409
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    include_default_branch: GetAllReposForProjectIncludeDefaultBranch
    | Unset = GetAllReposForProjectIncludeDefaultBranch.FALSE,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_include_default_branch: str | Unset = UNSET
    if not isinstance(include_default_branch, Unset):
        json_include_default_branch = include_default_branch.value

    params["includeDefaultBranch"] = json_include_default_branch

    params["start"] = start

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/mirroring/latest/projects/{project_id}/repos".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetAllReposForProjectResponse200 | GetAllReposForProjectResponse409 | None:
    if response.status_code == 200:
        response_200 = GetAllReposForProjectResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 409:
        response_409 = GetAllReposForProjectResponse409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetAllReposForProjectResponse200 | GetAllReposForProjectResponse409]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_default_branch: GetAllReposForProjectIncludeDefaultBranch
    | Unset = GetAllReposForProjectIncludeDefaultBranch.FALSE,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GetAllReposForProjectResponse200 | GetAllReposForProjectResponse409]:
    """Get hashes for repositories in project

     Returns a page of repositories for a given project, enriched with a content hash

    Args:
        project_id (str):
        include_default_branch (GetAllReposForProjectIncludeDefaultBranch | Unset):  Default:
            GetAllReposForProjectIncludeDefaultBranch.FALSE.
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAllReposForProjectResponse200 | GetAllReposForProjectResponse409]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        include_default_branch=include_default_branch,
        start=start,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_default_branch: GetAllReposForProjectIncludeDefaultBranch
    | Unset = GetAllReposForProjectIncludeDefaultBranch.FALSE,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetAllReposForProjectResponse200 | GetAllReposForProjectResponse409 | None:
    """Get hashes for repositories in project

     Returns a page of repositories for a given project, enriched with a content hash

    Args:
        project_id (str):
        include_default_branch (GetAllReposForProjectIncludeDefaultBranch | Unset):  Default:
            GetAllReposForProjectIncludeDefaultBranch.FALSE.
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAllReposForProjectResponse200 | GetAllReposForProjectResponse409
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        include_default_branch=include_default_branch,
        start=start,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_default_branch: GetAllReposForProjectIncludeDefaultBranch
    | Unset = GetAllReposForProjectIncludeDefaultBranch.FALSE,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GetAllReposForProjectResponse200 | GetAllReposForProjectResponse409]:
    """Get hashes for repositories in project

     Returns a page of repositories for a given project, enriched with a content hash

    Args:
        project_id (str):
        include_default_branch (GetAllReposForProjectIncludeDefaultBranch | Unset):  Default:
            GetAllReposForProjectIncludeDefaultBranch.FALSE.
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAllReposForProjectResponse200 | GetAllReposForProjectResponse409]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        include_default_branch=include_default_branch,
        start=start,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_default_branch: GetAllReposForProjectIncludeDefaultBranch
    | Unset = GetAllReposForProjectIncludeDefaultBranch.FALSE,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetAllReposForProjectResponse200 | GetAllReposForProjectResponse409 | None:
    """Get hashes for repositories in project

     Returns a page of repositories for a given project, enriched with a content hash

    Args:
        project_id (str):
        include_default_branch (GetAllReposForProjectIncludeDefaultBranch | Unset):  Default:
            GetAllReposForProjectIncludeDefaultBranch.FALSE.
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAllReposForProjectResponse200 | GetAllReposForProjectResponse409
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            include_default_branch=include_default_branch,
            start=start,
            limit=limit,
        )
    ).parsed
