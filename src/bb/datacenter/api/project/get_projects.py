from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_projects_response_200 import GetProjectsResponse200
from ...models.get_projects_response_400 import GetProjectsResponse400
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    name: str | Unset = UNSET,
    permission: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["name"] = name

    params["permission"] = permission

    params["start"] = start

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetProjectsResponse200 | GetProjectsResponse400 | None:
    if response.status_code == 200:
        response_200 = GetProjectsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetProjectsResponse400.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetProjectsResponse200 | GetProjectsResponse400]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    name: str | Unset = UNSET,
    permission: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GetProjectsResponse200 | GetProjectsResponse400]:
    """Get projects

     Retrieve a page of projects.

    Only projects for which the authenticated user has the <strong>PROJECT_VIEW</strong> permission will
    be returned.

    Args:
        name (str | Unset):
        permission (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProjectsResponse200 | GetProjectsResponse400]
    """

    kwargs = _get_kwargs(
        name=name,
        permission=permission,
        start=start,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    name: str | Unset = UNSET,
    permission: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetProjectsResponse200 | GetProjectsResponse400 | None:
    """Get projects

     Retrieve a page of projects.

    Only projects for which the authenticated user has the <strong>PROJECT_VIEW</strong> permission will
    be returned.

    Args:
        name (str | Unset):
        permission (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProjectsResponse200 | GetProjectsResponse400
    """

    return sync_detailed(
        client=client,
        name=name,
        permission=permission,
        start=start,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    name: str | Unset = UNSET,
    permission: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GetProjectsResponse200 | GetProjectsResponse400]:
    """Get projects

     Retrieve a page of projects.

    Only projects for which the authenticated user has the <strong>PROJECT_VIEW</strong> permission will
    be returned.

    Args:
        name (str | Unset):
        permission (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProjectsResponse200 | GetProjectsResponse400]
    """

    kwargs = _get_kwargs(
        name=name,
        permission=permission,
        start=start,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    name: str | Unset = UNSET,
    permission: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetProjectsResponse200 | GetProjectsResponse400 | None:
    """Get projects

     Retrieve a page of projects.

    Only projects for which the authenticated user has the <strong>PROJECT_VIEW</strong> permission will
    be returned.

    Args:
        name (str | Unset):
        permission (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProjectsResponse200 | GetProjectsResponse400
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
            permission=permission,
            start=start,
            limit=limit,
        )
    ).parsed
