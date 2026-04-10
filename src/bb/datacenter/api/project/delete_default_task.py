from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_default_task_response_401 import DeleteDefaultTaskResponse401
from ...models.delete_default_task_response_404 import DeleteDefaultTaskResponse404
from ...types import Response


def _get_kwargs(
    project_key: str,
    task_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/default-tasks/latest/projects/{project_key}/tasks/{task_id}".format(
            project_key=quote(str(project_key), safe=""),
            task_id=quote(str(task_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteDefaultTaskResponse401 | DeleteDefaultTaskResponse404 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = DeleteDefaultTaskResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = DeleteDefaultTaskResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteDefaultTaskResponse401 | DeleteDefaultTaskResponse404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    task_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteDefaultTaskResponse401 | DeleteDefaultTaskResponse404]:
    """Delete a specific default task

     Delete a specific default task for a project.

    The authenticated user must have **PROJECT_ADMIN** permission for this project to call the resource.

    Args:
        project_key (str):
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteDefaultTaskResponse401 | DeleteDefaultTaskResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        task_id=task_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    task_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeleteDefaultTaskResponse401 | DeleteDefaultTaskResponse404 | None:
    """Delete a specific default task

     Delete a specific default task for a project.

    The authenticated user must have **PROJECT_ADMIN** permission for this project to call the resource.

    Args:
        project_key (str):
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteDefaultTaskResponse401 | DeleteDefaultTaskResponse404
    """

    return sync_detailed(
        project_key=project_key,
        task_id=task_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    task_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteDefaultTaskResponse401 | DeleteDefaultTaskResponse404]:
    """Delete a specific default task

     Delete a specific default task for a project.

    The authenticated user must have **PROJECT_ADMIN** permission for this project to call the resource.

    Args:
        project_key (str):
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteDefaultTaskResponse401 | DeleteDefaultTaskResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        task_id=task_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    task_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeleteDefaultTaskResponse401 | DeleteDefaultTaskResponse404 | None:
    """Delete a specific default task

     Delete a specific default task for a project.

    The authenticated user must have **PROJECT_ADMIN** permission for this project to call the resource.

    Args:
        project_key (str):
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteDefaultTaskResponse401 | DeleteDefaultTaskResponse404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            task_id=task_id,
            client=client,
        )
    ).parsed
