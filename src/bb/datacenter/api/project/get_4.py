from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_4_response_401 import Get4Response401
from ...models.get_4_response_404 import Get4Response404
from ...models.rest_auto_merge_restricted_settings import RestAutoMergeRestrictedSettings
from ...types import Response


def _get_kwargs(
    project_key: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/settings/auto-merge".format(
            project_key=quote(str(project_key), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Get4Response401 | Get4Response404 | RestAutoMergeRestrictedSettings | None:
    if response.status_code == 200:
        response_200 = RestAutoMergeRestrictedSettings.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Get4Response401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = Get4Response404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Get4Response401 | Get4Response404 | RestAutoMergeRestrictedSettings]:
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
) -> Response[Get4Response401 | Get4Response404 | RestAutoMergeRestrictedSettings]:
    """Get pull request auto-merge settings

     Retrieves the pull request auto-merge settings for the supplied project. Default settings will be
    returned if no explicit settings have been set for the project

    The authenticated user must have <strong>PROJECT_VIEW</strong> permission for this project to call
    the resource.

    Args:
        project_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Get4Response401 | Get4Response404 | RestAutoMergeRestrictedSettings]
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
) -> Get4Response401 | Get4Response404 | RestAutoMergeRestrictedSettings | None:
    """Get pull request auto-merge settings

     Retrieves the pull request auto-merge settings for the supplied project. Default settings will be
    returned if no explicit settings have been set for the project

    The authenticated user must have <strong>PROJECT_VIEW</strong> permission for this project to call
    the resource.

    Args:
        project_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Get4Response401 | Get4Response404 | RestAutoMergeRestrictedSettings
    """

    return sync_detailed(
        project_key=project_key,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Get4Response401 | Get4Response404 | RestAutoMergeRestrictedSettings]:
    """Get pull request auto-merge settings

     Retrieves the pull request auto-merge settings for the supplied project. Default settings will be
    returned if no explicit settings have been set for the project

    The authenticated user must have <strong>PROJECT_VIEW</strong> permission for this project to call
    the resource.

    Args:
        project_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Get4Response401 | Get4Response404 | RestAutoMergeRestrictedSettings]
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
) -> Get4Response401 | Get4Response404 | RestAutoMergeRestrictedSettings | None:
    """Get pull request auto-merge settings

     Retrieves the pull request auto-merge settings for the supplied project. Default settings will be
    returned if no explicit settings have been set for the project

    The authenticated user must have <strong>PROJECT_VIEW</strong> permission for this project to call
    the resource.

    Args:
        project_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Get4Response401 | Get4Response404 | RestAutoMergeRestrictedSettings
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            client=client,
        )
    ).parsed
