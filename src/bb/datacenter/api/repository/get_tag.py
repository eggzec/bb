from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_tag_response_401 import GetTagResponse401
from ...models.get_tag_response_404 import GetTagResponse404
from ...models.rest_tag import RestTag
from ...types import Response


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/tags/{name}".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            name=quote(str(name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetTagResponse401 | GetTagResponse404 | RestTag | None:
    if response.status_code == 200:
        response_200 = RestTag.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetTagResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetTagResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetTagResponse401 | GetTagResponse404 | RestTag]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    repository_slug: str,
    name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetTagResponse401 | GetTagResponse404 | RestTag]:
    """Get tag

     Retrieve a tag in the specified repository.

    The authenticated user must have <strong>REPO_READ</strong> permission for the context repository to
    call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTagResponse401 | GetTagResponse404 | RestTag]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        name=name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    repository_slug: str,
    name: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetTagResponse401 | GetTagResponse404 | RestTag | None:
    """Get tag

     Retrieve a tag in the specified repository.

    The authenticated user must have <strong>REPO_READ</strong> permission for the context repository to
    call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTagResponse401 | GetTagResponse404 | RestTag
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        name=name,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetTagResponse401 | GetTagResponse404 | RestTag]:
    """Get tag

     Retrieve a tag in the specified repository.

    The authenticated user must have <strong>REPO_READ</strong> permission for the context repository to
    call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTagResponse401 | GetTagResponse404 | RestTag]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        name=name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    name: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetTagResponse401 | GetTagResponse404 | RestTag | None:
    """Get tag

     Retrieve a tag in the specified repository.

    The authenticated user must have <strong>REPO_READ</strong> permission for the context repository to
    call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTagResponse401 | GetTagResponse404 | RestTag
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            name=name,
            client=client,
        )
    ).parsed
