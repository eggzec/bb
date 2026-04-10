from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_default_tasks_1_response_200 import GetDefaultTasks1Response200
from ...models.get_default_tasks_1_response_401 import GetDefaultTasks1Response401
from ...models.get_default_tasks_1_response_404 import GetDefaultTasks1Response404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    *,
    markup: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["markup"] = markup

    params["start"] = start

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/default-tasks/latest/projects/{project_key}/repos/{repository_slug}/tasks".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetDefaultTasks1Response200 | GetDefaultTasks1Response401 | GetDefaultTasks1Response404 | None:
    if response.status_code == 200:
        response_200 = GetDefaultTasks1Response200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetDefaultTasks1Response401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetDefaultTasks1Response404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetDefaultTasks1Response200 | GetDefaultTasks1Response401 | GetDefaultTasks1Response404]:
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
    markup: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GetDefaultTasks1Response200 | GetDefaultTasks1Response401 | GetDefaultTasks1Response404]:
    """Get a page of default tasks

     Retrieves the default tasks for the supplied repository.

    The authenticated user must have **REPO_VIEW** permission for this repository to call the resource.

    Args:
        project_key (str):
        repository_slug (str):
        markup (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetDefaultTasks1Response200 | GetDefaultTasks1Response401 | GetDefaultTasks1Response404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        markup=markup,
        start=start,
        limit=limit,
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
    markup: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetDefaultTasks1Response200 | GetDefaultTasks1Response401 | GetDefaultTasks1Response404 | None:
    """Get a page of default tasks

     Retrieves the default tasks for the supplied repository.

    The authenticated user must have **REPO_VIEW** permission for this repository to call the resource.

    Args:
        project_key (str):
        repository_slug (str):
        markup (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetDefaultTasks1Response200 | GetDefaultTasks1Response401 | GetDefaultTasks1Response404
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        client=client,
        markup=markup,
        start=start,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    markup: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GetDefaultTasks1Response200 | GetDefaultTasks1Response401 | GetDefaultTasks1Response404]:
    """Get a page of default tasks

     Retrieves the default tasks for the supplied repository.

    The authenticated user must have **REPO_VIEW** permission for this repository to call the resource.

    Args:
        project_key (str):
        repository_slug (str):
        markup (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetDefaultTasks1Response200 | GetDefaultTasks1Response401 | GetDefaultTasks1Response404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        markup=markup,
        start=start,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    markup: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetDefaultTasks1Response200 | GetDefaultTasks1Response401 | GetDefaultTasks1Response404 | None:
    """Get a page of default tasks

     Retrieves the default tasks for the supplied repository.

    The authenticated user must have **REPO_VIEW** permission for this repository to call the resource.

    Args:
        project_key (str):
        repository_slug (str):
        markup (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetDefaultTasks1Response200 | GetDefaultTasks1Response401 | GetDefaultTasks1Response404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            client=client,
            markup=markup,
            start=start,
            limit=limit,
        )
    ).parsed
