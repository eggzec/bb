from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_default_task import RestDefaultTask
from ...models.rest_default_task_request import RestDefaultTaskRequest
from ...models.update_default_task_1_response_400 import UpdateDefaultTask1Response400
from ...models.update_default_task_1_response_401 import UpdateDefaultTask1Response401
from ...models.update_default_task_1_response_404 import UpdateDefaultTask1Response404
from ...types import Response


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    task_id: str,
    *,
    body: RestDefaultTaskRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/default-tasks/latest/projects/{project_key}/repos/{repository_slug}/tasks/{task_id}".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
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
    RestDefaultTask
    | UpdateDefaultTask1Response400
    | UpdateDefaultTask1Response401
    | UpdateDefaultTask1Response404
    | None
):
    if response.status_code == 200:
        response_200 = RestDefaultTask.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UpdateDefaultTask1Response400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UpdateDefaultTask1Response401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = UpdateDefaultTask1Response404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    RestDefaultTask | UpdateDefaultTask1Response400 | UpdateDefaultTask1Response401 | UpdateDefaultTask1Response404
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
    task_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestDefaultTaskRequest,
) -> Response[
    RestDefaultTask | UpdateDefaultTask1Response400 | UpdateDefaultTask1Response401 | UpdateDefaultTask1Response404
]:
    """Update a default task

     Updates a default task for the supplied repository.

    The authenticated user must have **REPO_ADMIN** permission for this repository to call the resource.

    Args:
        project_key (str):
        repository_slug (str):
        task_id (str):
        body (RestDefaultTaskRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestDefaultTask | UpdateDefaultTask1Response400 | UpdateDefaultTask1Response401 | UpdateDefaultTask1Response404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        task_id=task_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    repository_slug: str,
    task_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestDefaultTaskRequest,
) -> (
    RestDefaultTask
    | UpdateDefaultTask1Response400
    | UpdateDefaultTask1Response401
    | UpdateDefaultTask1Response404
    | None
):
    """Update a default task

     Updates a default task for the supplied repository.

    The authenticated user must have **REPO_ADMIN** permission for this repository to call the resource.

    Args:
        project_key (str):
        repository_slug (str):
        task_id (str):
        body (RestDefaultTaskRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestDefaultTask | UpdateDefaultTask1Response400 | UpdateDefaultTask1Response401 | UpdateDefaultTask1Response404
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        task_id=task_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    task_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestDefaultTaskRequest,
) -> Response[
    RestDefaultTask | UpdateDefaultTask1Response400 | UpdateDefaultTask1Response401 | UpdateDefaultTask1Response404
]:
    """Update a default task

     Updates a default task for the supplied repository.

    The authenticated user must have **REPO_ADMIN** permission for this repository to call the resource.

    Args:
        project_key (str):
        repository_slug (str):
        task_id (str):
        body (RestDefaultTaskRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestDefaultTask | UpdateDefaultTask1Response400 | UpdateDefaultTask1Response401 | UpdateDefaultTask1Response404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        task_id=task_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    task_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestDefaultTaskRequest,
) -> (
    RestDefaultTask
    | UpdateDefaultTask1Response400
    | UpdateDefaultTask1Response401
    | UpdateDefaultTask1Response404
    | None
):
    """Update a default task

     Updates a default task for the supplied repository.

    The authenticated user must have **REPO_ADMIN** permission for this repository to call the resource.

    Args:
        project_key (str):
        repository_slug (str):
        task_id (str):
        body (RestDefaultTaskRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestDefaultTask | UpdateDefaultTask1Response400 | UpdateDefaultTask1Response401 | UpdateDefaultTask1Response404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            task_id=task_id,
            client=client,
            body=body,
        )
    ).parsed
