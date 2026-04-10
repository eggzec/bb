from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_repository_hook_response_401 import GetRepositoryHookResponse401
from ...models.get_repository_hook_response_404 import GetRepositoryHookResponse404
from ...models.rest_repository_hook import RestRepositoryHook
from ...types import Response


def _get_kwargs(
    project_key: str,
    hook_key: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/settings/hooks/{hook_key}".format(
            project_key=quote(str(project_key), safe=""),
            hook_key=quote(str(hook_key), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetRepositoryHookResponse401 | GetRepositoryHookResponse404 | RestRepositoryHook | None:
    if response.status_code == 200:
        response_200 = RestRepositoryHook.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetRepositoryHookResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetRepositoryHookResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetRepositoryHookResponse401 | GetRepositoryHookResponse404 | RestRepositoryHook]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    hook_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetRepositoryHookResponse401 | GetRepositoryHookResponse404 | RestRepositoryHook]:
    """Get a repository hook

     Retrieve a repository hook for this project.

    The authenticated user must have <strong>PROJECT_READ</strong> permission for the specified project
    to call this resource.

    Args:
        project_key (str):
        hook_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRepositoryHookResponse401 | GetRepositoryHookResponse404 | RestRepositoryHook]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        hook_key=hook_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    hook_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetRepositoryHookResponse401 | GetRepositoryHookResponse404 | RestRepositoryHook | None:
    """Get a repository hook

     Retrieve a repository hook for this project.

    The authenticated user must have <strong>PROJECT_READ</strong> permission for the specified project
    to call this resource.

    Args:
        project_key (str):
        hook_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRepositoryHookResponse401 | GetRepositoryHookResponse404 | RestRepositoryHook
    """

    return sync_detailed(
        project_key=project_key,
        hook_key=hook_key,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    hook_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetRepositoryHookResponse401 | GetRepositoryHookResponse404 | RestRepositoryHook]:
    """Get a repository hook

     Retrieve a repository hook for this project.

    The authenticated user must have <strong>PROJECT_READ</strong> permission for the specified project
    to call this resource.

    Args:
        project_key (str):
        hook_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRepositoryHookResponse401 | GetRepositoryHookResponse404 | RestRepositoryHook]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        hook_key=hook_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    hook_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetRepositoryHookResponse401 | GetRepositoryHookResponse404 | RestRepositoryHook | None:
    """Get a repository hook

     Retrieve a repository hook for this project.

    The authenticated user must have <strong>PROJECT_READ</strong> permission for the specified project
    to call this resource.

    Args:
        project_key (str):
        hook_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRepositoryHookResponse401 | GetRepositoryHookResponse404 | RestRepositoryHook
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            hook_key=hook_key,
            client=client,
        )
    ).parsed
