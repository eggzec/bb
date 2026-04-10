from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_all_default_tasks_response_401 import DeleteAllDefaultTasksResponse401
from ...models.delete_all_default_tasks_response_404 import DeleteAllDefaultTasksResponse404
from ...types import Response


def _get_kwargs(
    project_key: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/default-tasks/latest/projects/{project_key}/tasks".format(
            project_key=quote(str(project_key), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteAllDefaultTasksResponse401 | DeleteAllDefaultTasksResponse404 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = DeleteAllDefaultTasksResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = DeleteAllDefaultTasksResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteAllDefaultTasksResponse401 | DeleteAllDefaultTasksResponse404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteAllDefaultTasksResponse401 | DeleteAllDefaultTasksResponse404]:
    """Deletes all default tasks for the project

     Delete all the default tasks for the supplied project

    The authenticated user must have **PROJECT_ADMIN** permission for this project to call the resource.

    Args:
        project_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAllDefaultTasksResponse401 | DeleteAllDefaultTasksResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeleteAllDefaultTasksResponse401 | DeleteAllDefaultTasksResponse404 | None:
    """Deletes all default tasks for the project

     Delete all the default tasks for the supplied project

    The authenticated user must have **PROJECT_ADMIN** permission for this project to call the resource.

    Args:
        project_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAllDefaultTasksResponse401 | DeleteAllDefaultTasksResponse404
    """

    return sync_detailed(
        project_key=project_key,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteAllDefaultTasksResponse401 | DeleteAllDefaultTasksResponse404]:
    """Deletes all default tasks for the project

     Delete all the default tasks for the supplied project

    The authenticated user must have **PROJECT_ADMIN** permission for this project to call the resource.

    Args:
        project_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAllDefaultTasksResponse401 | DeleteAllDefaultTasksResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeleteAllDefaultTasksResponse401 | DeleteAllDefaultTasksResponse404 | None:
    """Deletes all default tasks for the project

     Delete all the default tasks for the supplied project

    The authenticated user must have **PROJECT_ADMIN** permission for this project to call the resource.

    Args:
        project_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAllDefaultTasksResponse401 | DeleteAllDefaultTasksResponse404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            client=client,
        )
    ).parsed
