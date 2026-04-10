from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_tag_response_400 import DeleteTagResponse400
from ...models.delete_tag_response_401 import DeleteTagResponse401
from ...models.delete_tag_response_404 import DeleteTagResponse404
from ...types import Response


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/git/latest/projects/{project_key}/repos/{repository_slug}/tags/{name}".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            name=quote(str(name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteTagResponse400 | DeleteTagResponse401 | DeleteTagResponse404 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = DeleteTagResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteTagResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = DeleteTagResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteTagResponse400 | DeleteTagResponse401 | DeleteTagResponse404]:
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
) -> Response[Any | DeleteTagResponse400 | DeleteTagResponse401 | DeleteTagResponse404]:
    """Delete tag

     Deletes a tag in the specified repository.

    The authenticated user must have an effective <strong>REPO_WRITE</strong> permission to call this
    resource.

    Args:
        project_key (str):
        repository_slug (str):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteTagResponse400 | DeleteTagResponse401 | DeleteTagResponse404]
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
) -> Any | DeleteTagResponse400 | DeleteTagResponse401 | DeleteTagResponse404 | None:
    """Delete tag

     Deletes a tag in the specified repository.

    The authenticated user must have an effective <strong>REPO_WRITE</strong> permission to call this
    resource.

    Args:
        project_key (str):
        repository_slug (str):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteTagResponse400 | DeleteTagResponse401 | DeleteTagResponse404
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
) -> Response[Any | DeleteTagResponse400 | DeleteTagResponse401 | DeleteTagResponse404]:
    """Delete tag

     Deletes a tag in the specified repository.

    The authenticated user must have an effective <strong>REPO_WRITE</strong> permission to call this
    resource.

    Args:
        project_key (str):
        repository_slug (str):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteTagResponse400 | DeleteTagResponse401 | DeleteTagResponse404]
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
) -> Any | DeleteTagResponse400 | DeleteTagResponse401 | DeleteTagResponse404 | None:
    """Delete tag

     Deletes a tag in the specified repository.

    The authenticated user must have an effective <strong>REPO_WRITE</strong> permission to call this
    resource.

    Args:
        project_key (str):
        repository_slug (str):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteTagResponse400 | DeleteTagResponse401 | DeleteTagResponse404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            name=name,
            client=client,
        )
    ).parsed
