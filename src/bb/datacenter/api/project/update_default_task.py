from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_default_task import RestDefaultTask
from ...models.rest_default_task_request import RestDefaultTaskRequest
from ...models.update_default_task_response_400 import UpdateDefaultTaskResponse400
from ...models.update_default_task_response_401 import UpdateDefaultTaskResponse401
from ...models.update_default_task_response_404 import UpdateDefaultTaskResponse404
from ...types import Response


def _get_kwargs(
    project_key: str,
    task_id: str,
    *,
    body: RestDefaultTaskRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/default-tasks/latest/projects/{project_key}/tasks/{task_id}".format(
            project_key=quote(str(project_key), safe=""),
            task_id=quote(str(task_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    RestDefaultTask | UpdateDefaultTaskResponse400 | UpdateDefaultTaskResponse401 | UpdateDefaultTaskResponse404 | None
):
    if response.status_code == 200:
        response_200 = RestDefaultTask.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UpdateDefaultTaskResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UpdateDefaultTaskResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = UpdateDefaultTaskResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    RestDefaultTask | UpdateDefaultTaskResponse400 | UpdateDefaultTaskResponse401 | UpdateDefaultTaskResponse404
]:
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
    body: RestDefaultTaskRequest,
) -> Response[
    RestDefaultTask | UpdateDefaultTaskResponse400 | UpdateDefaultTaskResponse401 | UpdateDefaultTaskResponse404
]:
    """Update a default task

     Updates a default task for the supplied project.

    The authenticated user must have **PROJECT_ADMIN** permission for this project to call the resource.

    Args:
        project_key (str):
        task_id (str):
        body (RestDefaultTaskRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestDefaultTask | UpdateDefaultTaskResponse400 | UpdateDefaultTaskResponse401 | UpdateDefaultTaskResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        task_id=task_id,
        body=body,
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
    body: RestDefaultTaskRequest,
) -> (
    RestDefaultTask | UpdateDefaultTaskResponse400 | UpdateDefaultTaskResponse401 | UpdateDefaultTaskResponse404 | None
):
    """Update a default task

     Updates a default task for the supplied project.

    The authenticated user must have **PROJECT_ADMIN** permission for this project to call the resource.

    Args:
        project_key (str):
        task_id (str):
        body (RestDefaultTaskRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestDefaultTask | UpdateDefaultTaskResponse400 | UpdateDefaultTaskResponse401 | UpdateDefaultTaskResponse404
    """

    return sync_detailed(
        project_key=project_key,
        task_id=task_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    task_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestDefaultTaskRequest,
) -> Response[
    RestDefaultTask | UpdateDefaultTaskResponse400 | UpdateDefaultTaskResponse401 | UpdateDefaultTaskResponse404
]:
    """Update a default task

     Updates a default task for the supplied project.

    The authenticated user must have **PROJECT_ADMIN** permission for this project to call the resource.

    Args:
        project_key (str):
        task_id (str):
        body (RestDefaultTaskRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestDefaultTask | UpdateDefaultTaskResponse400 | UpdateDefaultTaskResponse401 | UpdateDefaultTaskResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        task_id=task_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    task_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestDefaultTaskRequest,
) -> (
    RestDefaultTask | UpdateDefaultTaskResponse400 | UpdateDefaultTaskResponse401 | UpdateDefaultTaskResponse404 | None
):
    """Update a default task

     Updates a default task for the supplied project.

    The authenticated user must have **PROJECT_ADMIN** permission for this project to call the resource.

    Args:
        project_key (str):
        task_id (str):
        body (RestDefaultTaskRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestDefaultTask | UpdateDefaultTaskResponse400 | UpdateDefaultTaskResponse401 | UpdateDefaultTaskResponse404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            task_id=task_id,
            client=client,
            body=body,
        )
    ).parsed
