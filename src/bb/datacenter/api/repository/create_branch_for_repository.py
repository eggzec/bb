from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_branch_for_repository_response_401 import CreateBranchForRepositoryResponse401
from ...models.create_branch_for_repository_response_404 import CreateBranchForRepositoryResponse404
from ...models.rest_branch import RestBranch
from ...models.rest_create_branch_request import RestCreateBranchRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    *,
    body: RestCreateBranchRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/branches".format(
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
) -> CreateBranchForRepositoryResponse401 | CreateBranchForRepositoryResponse404 | RestBranch | None:
    if response.status_code == 200:
        response_200 = RestBranch.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = CreateBranchForRepositoryResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = CreateBranchForRepositoryResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateBranchForRepositoryResponse401 | CreateBranchForRepositoryResponse404 | RestBranch]:
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
    body: RestCreateBranchRequest | Unset = UNSET,
) -> Response[CreateBranchForRepositoryResponse401 | CreateBranchForRepositoryResponse404 | RestBranch]:
    """Create branch

     Creates a branch using the information provided in the RestCreateBranchRequest request

    The authenticated user must have <strong>REPO_WRITE</strong> permission for the context repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestCreateBranchRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateBranchForRepositoryResponse401 | CreateBranchForRepositoryResponse404 | RestBranch]
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
    body: RestCreateBranchRequest | Unset = UNSET,
) -> CreateBranchForRepositoryResponse401 | CreateBranchForRepositoryResponse404 | RestBranch | None:
    """Create branch

     Creates a branch using the information provided in the RestCreateBranchRequest request

    The authenticated user must have <strong>REPO_WRITE</strong> permission for the context repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestCreateBranchRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateBranchForRepositoryResponse401 | CreateBranchForRepositoryResponse404 | RestBranch
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
    body: RestCreateBranchRequest | Unset = UNSET,
) -> Response[CreateBranchForRepositoryResponse401 | CreateBranchForRepositoryResponse404 | RestBranch]:
    """Create branch

     Creates a branch using the information provided in the RestCreateBranchRequest request

    The authenticated user must have <strong>REPO_WRITE</strong> permission for the context repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestCreateBranchRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateBranchForRepositoryResponse401 | CreateBranchForRepositoryResponse404 | RestBranch]
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
    body: RestCreateBranchRequest | Unset = UNSET,
) -> CreateBranchForRepositoryResponse401 | CreateBranchForRepositoryResponse404 | RestBranch | None:
    """Create branch

     Creates a branch using the information provided in the RestCreateBranchRequest request

    The authenticated user must have <strong>REPO_WRITE</strong> permission for the context repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestCreateBranchRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateBranchForRepositoryResponse401 | CreateBranchForRepositoryResponse404 | RestBranch
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            client=client,
            body=body,
        )
    ).parsed
