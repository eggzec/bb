from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.example_settings import ExampleSettings
from ...models.get_settings_1_response_401 import GetSettings1Response401
from ...models.get_settings_1_response_404 import GetSettings1Response404
from ...types import Response


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    hook_key: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/settings/hooks/{hook_key}/settings".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            hook_key=quote(str(hook_key), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ExampleSettings | GetSettings1Response401 | GetSettings1Response404 | None:
    if response.status_code == 200:
        response_200 = ExampleSettings.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetSettings1Response401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetSettings1Response404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ExampleSettings | GetSettings1Response401 | GetSettings1Response404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    repository_slug: str,
    hook_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ExampleSettings | GetSettings1Response401 | GetSettings1Response404]:
    """Get repository hook settings

     Retrieve the settings for a repository hook for this repository.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        hook_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExampleSettings | GetSettings1Response401 | GetSettings1Response404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        hook_key=hook_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    repository_slug: str,
    hook_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> ExampleSettings | GetSettings1Response401 | GetSettings1Response404 | None:
    """Get repository hook settings

     Retrieve the settings for a repository hook for this repository.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        hook_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExampleSettings | GetSettings1Response401 | GetSettings1Response404
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        hook_key=hook_key,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    hook_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ExampleSettings | GetSettings1Response401 | GetSettings1Response404]:
    """Get repository hook settings

     Retrieve the settings for a repository hook for this repository.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        hook_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExampleSettings | GetSettings1Response401 | GetSettings1Response404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        hook_key=hook_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    hook_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> ExampleSettings | GetSettings1Response401 | GetSettings1Response404 | None:
    """Get repository hook settings

     Retrieve the settings for a repository hook for this repository.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        hook_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExampleSettings | GetSettings1Response401 | GetSettings1Response404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            hook_key=hook_key,
            client=client,
        )
    ).parsed
