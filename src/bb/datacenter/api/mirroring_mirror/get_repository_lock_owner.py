from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_repository_lock_owner_response_401 import GetRepositoryLockOwnerResponse401
from ...models.get_repository_lock_owner_response_404 import GetRepositoryLockOwnerResponse404
from ...models.rest_repository_lock_owner import RestRepositoryLockOwner
from ...types import Response


def _get_kwargs(
    project_key: str,
    repository_slug: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/mirroring/latest/supportInfo/projects/{project_key}/repos/{repository_slug}/repo-lock-owner".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetRepositoryLockOwnerResponse401 | GetRepositoryLockOwnerResponse404 | RestRepositoryLockOwner | None:
    if response.status_code == 200:
        response_200 = RestRepositoryLockOwner.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetRepositoryLockOwnerResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetRepositoryLockOwnerResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetRepositoryLockOwnerResponse401 | GetRepositoryLockOwnerResponse404 | RestRepositoryLockOwner]:
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
) -> Response[GetRepositoryLockOwnerResponse401 | GetRepositoryLockOwnerResponse404 | RestRepositoryLockOwner]:
    """Get the repository lock owner for the syncing process

     Retrieves the information about the process owning the sync lock for this repository. The process
    owning the lock could be running on any of the nodes in the mirror farm

    Args:
        project_key (str):
        repository_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRepositoryLockOwnerResponse401 | GetRepositoryLockOwnerResponse404 | RestRepositoryLockOwner]
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
) -> GetRepositoryLockOwnerResponse401 | GetRepositoryLockOwnerResponse404 | RestRepositoryLockOwner | None:
    """Get the repository lock owner for the syncing process

     Retrieves the information about the process owning the sync lock for this repository. The process
    owning the lock could be running on any of the nodes in the mirror farm

    Args:
        project_key (str):
        repository_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRepositoryLockOwnerResponse401 | GetRepositoryLockOwnerResponse404 | RestRepositoryLockOwner
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
) -> Response[GetRepositoryLockOwnerResponse401 | GetRepositoryLockOwnerResponse404 | RestRepositoryLockOwner]:
    """Get the repository lock owner for the syncing process

     Retrieves the information about the process owning the sync lock for this repository. The process
    owning the lock could be running on any of the nodes in the mirror farm

    Args:
        project_key (str):
        repository_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRepositoryLockOwnerResponse401 | GetRepositoryLockOwnerResponse404 | RestRepositoryLockOwner]
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
) -> GetRepositoryLockOwnerResponse401 | GetRepositoryLockOwnerResponse404 | RestRepositoryLockOwner | None:
    """Get the repository lock owner for the syncing process

     Retrieves the information about the process owning the sync lock for this repository. The process
    owning the lock could be running on any of the nodes in the mirror farm

    Args:
        project_key (str):
        repository_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRepositoryLockOwnerResponse401 | GetRepositoryLockOwnerResponse404 | RestRepositoryLockOwner
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            client=client,
        )
    ).parsed
