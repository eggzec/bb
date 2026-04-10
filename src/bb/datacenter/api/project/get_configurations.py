from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_configurations_response_200 import GetConfigurationsResponse200
from ...models.get_configurations_response_401 import GetConfigurationsResponse401
from ...models.get_configurations_response_404 import GetConfigurationsResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    *,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["start"] = start

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/hook-scripts".format(
            project_key=quote(str(project_key), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetConfigurationsResponse200 | GetConfigurationsResponse401 | GetConfigurationsResponse404 | None:
    if response.status_code == 200:
        response_200 = GetConfigurationsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetConfigurationsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetConfigurationsResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetConfigurationsResponse200 | GetConfigurationsResponse401 | GetConfigurationsResponse404]:
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
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GetConfigurationsResponse200 | GetConfigurationsResponse401 | GetConfigurationsResponse404]:
    """Get configured hook scripts

     Return a page of hook scripts configured for the specified project.

    This endpoint requires **PROJECT_ADMIN** permission.

    Args:
        project_key (str):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetConfigurationsResponse200 | GetConfigurationsResponse401 | GetConfigurationsResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
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
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetConfigurationsResponse200 | GetConfigurationsResponse401 | GetConfigurationsResponse404 | None:
    """Get configured hook scripts

     Return a page of hook scripts configured for the specified project.

    This endpoint requires **PROJECT_ADMIN** permission.

    Args:
        project_key (str):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetConfigurationsResponse200 | GetConfigurationsResponse401 | GetConfigurationsResponse404
    """

    return sync_detailed(
        project_key=project_key,
        client=client,
        start=start,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GetConfigurationsResponse200 | GetConfigurationsResponse401 | GetConfigurationsResponse404]:
    """Get configured hook scripts

     Return a page of hook scripts configured for the specified project.

    This endpoint requires **PROJECT_ADMIN** permission.

    Args:
        project_key (str):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetConfigurationsResponse200 | GetConfigurationsResponse401 | GetConfigurationsResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        start=start,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetConfigurationsResponse200 | GetConfigurationsResponse401 | GetConfigurationsResponse404 | None:
    """Get configured hook scripts

     Return a page of hook scripts configured for the specified project.

    This endpoint requires **PROJECT_ADMIN** permission.

    Args:
        project_key (str):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetConfigurationsResponse200 | GetConfigurationsResponse401 | GetConfigurationsResponse404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            client=client,
            start=start,
            limit=limit,
        )
    ).parsed
