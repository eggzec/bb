from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_repository import RestRepository
from ...models.update_repository_response_400 import UpdateRepositoryResponse400
from ...models.update_repository_response_401 import UpdateRepositoryResponse401
from ...models.update_repository_response_403 import UpdateRepositoryResponse403
from ...models.update_repository_response_404 import UpdateRepositoryResponse404
from ...models.update_repository_response_409 import UpdateRepositoryResponse409
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    *,
    body: RestRepository | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    RestRepository
    | UpdateRepositoryResponse400
    | UpdateRepositoryResponse401
    | UpdateRepositoryResponse403
    | UpdateRepositoryResponse404
    | UpdateRepositoryResponse409
    | None
):
    if response.status_code == 201:
        response_201 = RestRepository.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = UpdateRepositoryResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UpdateRepositoryResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = UpdateRepositoryResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = UpdateRepositoryResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = UpdateRepositoryResponse409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    RestRepository
    | UpdateRepositoryResponse400
    | UpdateRepositoryResponse401
    | UpdateRepositoryResponse403
    | UpdateRepositoryResponse404
    | UpdateRepositoryResponse409
]:
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
    body: RestRepository | Unset = UNSET,
) -> Response[
    RestRepository
    | UpdateRepositoryResponse400
    | UpdateRepositoryResponse401
    | UpdateRepositoryResponse403
    | UpdateRepositoryResponse404
    | UpdateRepositoryResponse409
]:
    r"""Update repository

     Update the repository matching the <strong>repositorySlug</strong> supplied in the resource path.

    The repository's slug is derived from its name. If the name changes the slug may also change.

    This resource can be used to change the repository's default branch by specifying a new default
    branch in the request. For example: <code>\"defaultBranch\":\"main\"</code>

    This resource can be used to move the repository to a different project by specifying a new project
    in the request. For example: <code>\"project\":{\"key\":\"NEW_KEY\"}</code>

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestRepository | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestRepository | UpdateRepositoryResponse400 | UpdateRepositoryResponse401 | UpdateRepositoryResponse403 | UpdateRepositoryResponse404 | UpdateRepositoryResponse409]
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
    body: RestRepository | Unset = UNSET,
) -> (
    RestRepository
    | UpdateRepositoryResponse400
    | UpdateRepositoryResponse401
    | UpdateRepositoryResponse403
    | UpdateRepositoryResponse404
    | UpdateRepositoryResponse409
    | None
):
    r"""Update repository

     Update the repository matching the <strong>repositorySlug</strong> supplied in the resource path.

    The repository's slug is derived from its name. If the name changes the slug may also change.

    This resource can be used to change the repository's default branch by specifying a new default
    branch in the request. For example: <code>\"defaultBranch\":\"main\"</code>

    This resource can be used to move the repository to a different project by specifying a new project
    in the request. For example: <code>\"project\":{\"key\":\"NEW_KEY\"}</code>

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestRepository | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestRepository | UpdateRepositoryResponse400 | UpdateRepositoryResponse401 | UpdateRepositoryResponse403 | UpdateRepositoryResponse404 | UpdateRepositoryResponse409
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
    body: RestRepository | Unset = UNSET,
) -> Response[
    RestRepository
    | UpdateRepositoryResponse400
    | UpdateRepositoryResponse401
    | UpdateRepositoryResponse403
    | UpdateRepositoryResponse404
    | UpdateRepositoryResponse409
]:
    r"""Update repository

     Update the repository matching the <strong>repositorySlug</strong> supplied in the resource path.

    The repository's slug is derived from its name. If the name changes the slug may also change.

    This resource can be used to change the repository's default branch by specifying a new default
    branch in the request. For example: <code>\"defaultBranch\":\"main\"</code>

    This resource can be used to move the repository to a different project by specifying a new project
    in the request. For example: <code>\"project\":{\"key\":\"NEW_KEY\"}</code>

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestRepository | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestRepository | UpdateRepositoryResponse400 | UpdateRepositoryResponse401 | UpdateRepositoryResponse403 | UpdateRepositoryResponse404 | UpdateRepositoryResponse409]
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
    body: RestRepository | Unset = UNSET,
) -> (
    RestRepository
    | UpdateRepositoryResponse400
    | UpdateRepositoryResponse401
    | UpdateRepositoryResponse403
    | UpdateRepositoryResponse404
    | UpdateRepositoryResponse409
    | None
):
    r"""Update repository

     Update the repository matching the <strong>repositorySlug</strong> supplied in the resource path.

    The repository's slug is derived from its name. If the name changes the slug may also change.

    This resource can be used to change the repository's default branch by specifying a new default
    branch in the request. For example: <code>\"defaultBranch\":\"main\"</code>

    This resource can be used to move the repository to a different project by specifying a new project
    in the request. For example: <code>\"project\":{\"key\":\"NEW_KEY\"}</code>

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestRepository | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestRepository | UpdateRepositoryResponse400 | UpdateRepositoryResponse401 | UpdateRepositoryResponse403 | UpdateRepositoryResponse404 | UpdateRepositoryResponse409
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            client=client,
            body=body,
        )
    ).parsed
