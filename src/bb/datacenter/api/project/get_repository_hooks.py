from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_repository_hooks_response_200 import GetRepositoryHooksResponse200
from ...models.get_repository_hooks_response_401 import GetRepositoryHooksResponse401
from ...models.get_repository_hooks_response_404 import GetRepositoryHooksResponse404
from ...models.get_repository_hooks_type import GetRepositoryHooksType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    *,
    type_: GetRepositoryHooksType | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    params["start"] = start

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/settings/hooks".format(
            project_key=quote(str(project_key), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetRepositoryHooksResponse200 | GetRepositoryHooksResponse401 | GetRepositoryHooksResponse404 | None:
    if response.status_code == 200:
        response_200 = GetRepositoryHooksResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetRepositoryHooksResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetRepositoryHooksResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetRepositoryHooksResponse200 | GetRepositoryHooksResponse401 | GetRepositoryHooksResponse404]:
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
    type_: GetRepositoryHooksType | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GetRepositoryHooksResponse200 | GetRepositoryHooksResponse401 | GetRepositoryHooksResponse404]:
    """Get repository hooks

     Retrieve a page of repository hooks for this project.

    The authenticated user must have <strong>PROJECT_READ</strong> permission for the specified project
    to call this resource.

    Args:
        project_key (str):
        type_ (GetRepositoryHooksType | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRepositoryHooksResponse200 | GetRepositoryHooksResponse401 | GetRepositoryHooksResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        type_=type_,
        start=start,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    type_: GetRepositoryHooksType | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetRepositoryHooksResponse200 | GetRepositoryHooksResponse401 | GetRepositoryHooksResponse404 | None:
    """Get repository hooks

     Retrieve a page of repository hooks for this project.

    The authenticated user must have <strong>PROJECT_READ</strong> permission for the specified project
    to call this resource.

    Args:
        project_key (str):
        type_ (GetRepositoryHooksType | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRepositoryHooksResponse200 | GetRepositoryHooksResponse401 | GetRepositoryHooksResponse404
    """

    return sync_detailed(
        project_key=project_key,
        client=client,
        type_=type_,
        start=start,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    type_: GetRepositoryHooksType | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GetRepositoryHooksResponse200 | GetRepositoryHooksResponse401 | GetRepositoryHooksResponse404]:
    """Get repository hooks

     Retrieve a page of repository hooks for this project.

    The authenticated user must have <strong>PROJECT_READ</strong> permission for the specified project
    to call this resource.

    Args:
        project_key (str):
        type_ (GetRepositoryHooksType | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRepositoryHooksResponse200 | GetRepositoryHooksResponse401 | GetRepositoryHooksResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        type_=type_,
        start=start,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    type_: GetRepositoryHooksType | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetRepositoryHooksResponse200 | GetRepositoryHooksResponse401 | GetRepositoryHooksResponse404 | None:
    """Get repository hooks

     Retrieve a page of repository hooks for this project.

    The authenticated user must have <strong>PROJECT_READ</strong> permission for the specified project
    to call this resource.

    Args:
        project_key (str):
        type_ (GetRepositoryHooksType | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRepositoryHooksResponse200 | GetRepositoryHooksResponse401 | GetRepositoryHooksResponse404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            client=client,
            type_=type_,
            start=start,
            limit=limit,
        )
    ).parsed
