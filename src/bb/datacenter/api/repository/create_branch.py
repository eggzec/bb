from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_branch_response_400 import CreateBranchResponse400
from ...models.create_branch_response_401 import CreateBranchResponse401
from ...models.create_branch_response_409 import CreateBranchResponse409
from ...models.rest_branch import RestBranch
from ...models.rest_branch_create_request import RestBranchCreateRequest
from ...types import Response


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    *,
    body: RestBranchCreateRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/branch-utils/latest/projects/{project_key}/repos/{repository_slug}/branches".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateBranchResponse400 | CreateBranchResponse401 | CreateBranchResponse409 | RestBranch | None:
    if response.status_code == 201:
        response_201 = RestBranch.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = CreateBranchResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = CreateBranchResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 409:
        response_409 = CreateBranchResponse409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateBranchResponse400 | CreateBranchResponse401 | CreateBranchResponse409 | RestBranch]:
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
    body: RestBranchCreateRequest,
) -> Response[CreateBranchResponse400 | CreateBranchResponse401 | CreateBranchResponse409 | RestBranch]:
    """Create branch

      Creates a branch in the specified repository.


    The authenticated user must have an effective <strong>REPO_WRITE</strong> permission to call this
    resource. If
    branch permissions are set up in the repository, the authenticated user must also have access to the
    branch name
    that is to be created.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestBranchCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateBranchResponse400 | CreateBranchResponse401 | CreateBranchResponse409 | RestBranch]
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
    body: RestBranchCreateRequest,
) -> CreateBranchResponse400 | CreateBranchResponse401 | CreateBranchResponse409 | RestBranch | None:
    """Create branch

      Creates a branch in the specified repository.


    The authenticated user must have an effective <strong>REPO_WRITE</strong> permission to call this
    resource. If
    branch permissions are set up in the repository, the authenticated user must also have access to the
    branch name
    that is to be created.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestBranchCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateBranchResponse400 | CreateBranchResponse401 | CreateBranchResponse409 | RestBranch
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
    body: RestBranchCreateRequest,
) -> Response[CreateBranchResponse400 | CreateBranchResponse401 | CreateBranchResponse409 | RestBranch]:
    """Create branch

      Creates a branch in the specified repository.


    The authenticated user must have an effective <strong>REPO_WRITE</strong> permission to call this
    resource. If
    branch permissions are set up in the repository, the authenticated user must also have access to the
    branch name
    that is to be created.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestBranchCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateBranchResponse400 | CreateBranchResponse401 | CreateBranchResponse409 | RestBranch]
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
    body: RestBranchCreateRequest,
) -> CreateBranchResponse400 | CreateBranchResponse401 | CreateBranchResponse409 | RestBranch | None:
    """Create branch

      Creates a branch in the specified repository.


    The authenticated user must have an effective <strong>REPO_WRITE</strong> permission to call this
    resource. If
    branch permissions are set up in the repository, the authenticated user must also have access to the
    branch name
    that is to be created.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestBranchCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateBranchResponse400 | CreateBranchResponse401 | CreateBranchResponse409 | RestBranch
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            client=client,
            body=body,
        )
    ).parsed
