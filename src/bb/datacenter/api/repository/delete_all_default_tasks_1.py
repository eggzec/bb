from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_all_default_tasks_1_response_401 import DeleteAllDefaultTasks1Response401
from ...models.delete_all_default_tasks_1_response_404 import DeleteAllDefaultTasks1Response404
from ...types import Response


def _get_kwargs(
    project_key: str,
    repository_slug: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/default-tasks/latest/projects/{project_key}/repos/{repository_slug}/tasks".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteAllDefaultTasks1Response401 | DeleteAllDefaultTasks1Response404 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = DeleteAllDefaultTasks1Response401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = DeleteAllDefaultTasks1Response404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteAllDefaultTasks1Response401 | DeleteAllDefaultTasks1Response404]:
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
) -> Response[Any | DeleteAllDefaultTasks1Response401 | DeleteAllDefaultTasks1Response404]:
    """Deletes all default tasks for the repository

     Delete all the default tasks for the supplied repository

    The authenticated user must have **REPO_ADMIN** permission for this repository to call the resource.

    Args:
        project_key (str):
        repository_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAllDefaultTasks1Response401 | DeleteAllDefaultTasks1Response404]
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
) -> Any | DeleteAllDefaultTasks1Response401 | DeleteAllDefaultTasks1Response404 | None:
    """Deletes all default tasks for the repository

     Delete all the default tasks for the supplied repository

    The authenticated user must have **REPO_ADMIN** permission for this repository to call the resource.

    Args:
        project_key (str):
        repository_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAllDefaultTasks1Response401 | DeleteAllDefaultTasks1Response404
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
) -> Response[Any | DeleteAllDefaultTasks1Response401 | DeleteAllDefaultTasks1Response404]:
    """Deletes all default tasks for the repository

     Delete all the default tasks for the supplied repository

    The authenticated user must have **REPO_ADMIN** permission for this repository to call the resource.

    Args:
        project_key (str):
        repository_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAllDefaultTasks1Response401 | DeleteAllDefaultTasks1Response404]
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
) -> Any | DeleteAllDefaultTasks1Response401 | DeleteAllDefaultTasks1Response404 | None:
    """Deletes all default tasks for the repository

     Delete all the default tasks for the supplied repository

    The authenticated user must have **REPO_ADMIN** permission for this repository to call the resource.

    Args:
        project_key (str):
        repository_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAllDefaultTasks1Response401 | DeleteAllDefaultTasks1Response404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            client=client,
        )
    ).parsed
