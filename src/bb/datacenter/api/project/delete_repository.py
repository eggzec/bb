from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_repository_response_204 import DeleteRepositoryResponse204
from ...models.delete_repository_response_401 import DeleteRepositoryResponse401
from ...types import Response


def _get_kwargs(
    project_key: str,
    repository_slug: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteRepositoryResponse204 | DeleteRepositoryResponse401 | None:
    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    if response.status_code == 204:
        response_204 = DeleteRepositoryResponse204.from_dict(response.json())

        return response_204

    if response.status_code == 401:
        response_401 = DeleteRepositoryResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteRepositoryResponse204 | DeleteRepositoryResponse401]:
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
) -> Response[Any | DeleteRepositoryResponse204 | DeleteRepositoryResponse401]:
    """Delete repository

     Schedule the repository matching the supplied <strong>projectKey</strong> and
    <strong>repositorySlug</strong> to be deleted.

    The authenticated user must have sufficient permissions specified by the repository delete policy to
    call this resource. The default permission required is <strong>REPO_ADMIN</strong> permission.

    Args:
        project_key (str):
        repository_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteRepositoryResponse204 | DeleteRepositoryResponse401]
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
) -> Any | DeleteRepositoryResponse204 | DeleteRepositoryResponse401 | None:
    """Delete repository

     Schedule the repository matching the supplied <strong>projectKey</strong> and
    <strong>repositorySlug</strong> to be deleted.

    The authenticated user must have sufficient permissions specified by the repository delete policy to
    call this resource. The default permission required is <strong>REPO_ADMIN</strong> permission.

    Args:
        project_key (str):
        repository_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteRepositoryResponse204 | DeleteRepositoryResponse401
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
) -> Response[Any | DeleteRepositoryResponse204 | DeleteRepositoryResponse401]:
    """Delete repository

     Schedule the repository matching the supplied <strong>projectKey</strong> and
    <strong>repositorySlug</strong> to be deleted.

    The authenticated user must have sufficient permissions specified by the repository delete policy to
    call this resource. The default permission required is <strong>REPO_ADMIN</strong> permission.

    Args:
        project_key (str):
        repository_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteRepositoryResponse204 | DeleteRepositoryResponse401]
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
) -> Any | DeleteRepositoryResponse204 | DeleteRepositoryResponse401 | None:
    """Delete repository

     Schedule the repository matching the supplied <strong>projectKey</strong> and
    <strong>repositorySlug</strong> to be deleted.

    The authenticated user must have sufficient permissions specified by the repository delete policy to
    call this resource. The default permission required is <strong>REPO_ADMIN</strong> permission.

    Args:
        project_key (str):
        repository_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteRepositoryResponse204 | DeleteRepositoryResponse401
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            client=client,
        )
    ).parsed
