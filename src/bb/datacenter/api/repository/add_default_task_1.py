from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_default_task_1_response_400 import AddDefaultTask1Response400
from ...models.add_default_task_1_response_401 import AddDefaultTask1Response401
from ...models.add_default_task_1_response_404 import AddDefaultTask1Response404
from ...models.rest_default_task import RestDefaultTask
from ...models.rest_default_task_request import RestDefaultTaskRequest
from ...types import Response


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    *,
    body: RestDefaultTaskRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/default-tasks/latest/projects/{project_key}/repos/{repository_slug}/tasks".format(
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
) -> AddDefaultTask1Response400 | AddDefaultTask1Response401 | AddDefaultTask1Response404 | RestDefaultTask | None:
    if response.status_code == 200:
        response_200 = RestDefaultTask.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = AddDefaultTask1Response400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = AddDefaultTask1Response401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = AddDefaultTask1Response404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AddDefaultTask1Response400 | AddDefaultTask1Response401 | AddDefaultTask1Response404 | RestDefaultTask]:
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
    body: RestDefaultTaskRequest,
) -> Response[AddDefaultTask1Response400 | AddDefaultTask1Response401 | AddDefaultTask1Response404 | RestDefaultTask]:
    """Add a default task

     Creates a default task for the supplied repository.

    The authenticated user must have **REPO_ADMIN** permission for this repository to call the resource.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestDefaultTaskRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddDefaultTask1Response400 | AddDefaultTask1Response401 | AddDefaultTask1Response404 | RestDefaultTask]
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
    body: RestDefaultTaskRequest,
) -> AddDefaultTask1Response400 | AddDefaultTask1Response401 | AddDefaultTask1Response404 | RestDefaultTask | None:
    """Add a default task

     Creates a default task for the supplied repository.

    The authenticated user must have **REPO_ADMIN** permission for this repository to call the resource.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestDefaultTaskRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddDefaultTask1Response400 | AddDefaultTask1Response401 | AddDefaultTask1Response404 | RestDefaultTask
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
    body: RestDefaultTaskRequest,
) -> Response[AddDefaultTask1Response400 | AddDefaultTask1Response401 | AddDefaultTask1Response404 | RestDefaultTask]:
    """Add a default task

     Creates a default task for the supplied repository.

    The authenticated user must have **REPO_ADMIN** permission for this repository to call the resource.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestDefaultTaskRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddDefaultTask1Response400 | AddDefaultTask1Response401 | AddDefaultTask1Response404 | RestDefaultTask]
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
    body: RestDefaultTaskRequest,
) -> AddDefaultTask1Response400 | AddDefaultTask1Response401 | AddDefaultTask1Response404 | RestDefaultTask | None:
    """Add a default task

     Creates a default task for the supplied repository.

    The authenticated user must have **REPO_ADMIN** permission for this repository to call the resource.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestDefaultTaskRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddDefaultTask1Response400 | AddDefaultTask1Response401 | AddDefaultTask1Response404 | RestDefaultTask
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            client=client,
            body=body,
        )
    ).parsed
