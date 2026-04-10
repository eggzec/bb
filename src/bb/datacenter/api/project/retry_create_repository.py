from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_repository import RestRepository
from ...models.retry_create_repository_response_400 import RetryCreateRepositoryResponse400
from ...models.retry_create_repository_response_401 import RetryCreateRepositoryResponse401
from ...models.retry_create_repository_response_404 import RetryCreateRepositoryResponse404
from ...types import Response


def _get_kwargs(
    project_key: str,
    repository_slug: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/recreate".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    RestRepository
    | RetryCreateRepositoryResponse400
    | RetryCreateRepositoryResponse401
    | RetryCreateRepositoryResponse404
    | None
):
    if response.status_code == 200:
        response_200 = RestRepository.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = RetryCreateRepositoryResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = RetryCreateRepositoryResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = RetryCreateRepositoryResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    RestRepository
    | RetryCreateRepositoryResponse400
    | RetryCreateRepositoryResponse401
    | RetryCreateRepositoryResponse404
]:
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
) -> Response[
    RestRepository
    | RetryCreateRepositoryResponse400
    | RetryCreateRepositoryResponse401
    | RetryCreateRepositoryResponse404
]:
    """Retry repository creation

     If a create or fork operation fails, calling this method will clean up the broken repository and try
    again. The repository must be in an INITIALISATION_FAILED state.

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the specified project
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestRepository | RetryCreateRepositoryResponse400 | RetryCreateRepositoryResponse401 | RetryCreateRepositoryResponse404]
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
) -> (
    RestRepository
    | RetryCreateRepositoryResponse400
    | RetryCreateRepositoryResponse401
    | RetryCreateRepositoryResponse404
    | None
):
    """Retry repository creation

     If a create or fork operation fails, calling this method will clean up the broken repository and try
    again. The repository must be in an INITIALISATION_FAILED state.

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the specified project
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestRepository | RetryCreateRepositoryResponse400 | RetryCreateRepositoryResponse401 | RetryCreateRepositoryResponse404
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
) -> Response[
    RestRepository
    | RetryCreateRepositoryResponse400
    | RetryCreateRepositoryResponse401
    | RetryCreateRepositoryResponse404
]:
    """Retry repository creation

     If a create or fork operation fails, calling this method will clean up the broken repository and try
    again. The repository must be in an INITIALISATION_FAILED state.

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the specified project
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestRepository | RetryCreateRepositoryResponse400 | RetryCreateRepositoryResponse401 | RetryCreateRepositoryResponse404]
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
) -> (
    RestRepository
    | RetryCreateRepositoryResponse400
    | RetryCreateRepositoryResponse401
    | RetryCreateRepositoryResponse404
    | None
):
    """Retry repository creation

     If a create or fork operation fails, calling this method will clean up the broken repository and try
    again. The repository must be in an INITIALISATION_FAILED state.

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the specified project
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestRepository | RetryCreateRepositoryResponse400 | RetryCreateRepositoryResponse401 | RetryCreateRepositoryResponse404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            client=client,
        )
    ).parsed
