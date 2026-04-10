from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_response_400 import DeleteResponse400
from ...models.delete_response_401 import DeleteResponse401
from ...models.delete_response_404 import DeleteResponse404
from ...types import UNSET, Response


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    *,
    key: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["key"] = key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/commits/{commit_id}/builds".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            commit_id=quote(str(commit_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteResponse400 | DeleteResponse401 | DeleteResponse404 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = DeleteResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = DeleteResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteResponse400 | DeleteResponse401 | DeleteResponse404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    *,
    client: AuthenticatedClient | Client,
    key: str,
) -> Response[Any | DeleteResponse400 | DeleteResponse401 | DeleteResponse404]:
    """Delete a specific build status

     Delete a specific build status.

    The authenticated user must have **REPO_ADMIN** permission for the provided repository.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteResponse400 | DeleteResponse401 | DeleteResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        key=key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    *,
    client: AuthenticatedClient | Client,
    key: str,
) -> Any | DeleteResponse400 | DeleteResponse401 | DeleteResponse404 | None:
    """Delete a specific build status

     Delete a specific build status.

    The authenticated user must have **REPO_ADMIN** permission for the provided repository.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteResponse400 | DeleteResponse401 | DeleteResponse404
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        client=client,
        key=key,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    *,
    client: AuthenticatedClient | Client,
    key: str,
) -> Response[Any | DeleteResponse400 | DeleteResponse401 | DeleteResponse404]:
    """Delete a specific build status

     Delete a specific build status.

    The authenticated user must have **REPO_ADMIN** permission for the provided repository.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteResponse400 | DeleteResponse401 | DeleteResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        key=key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    *,
    client: AuthenticatedClient | Client,
    key: str,
) -> Any | DeleteResponse400 | DeleteResponse401 | DeleteResponse404 | None:
    """Delete a specific build status

     Delete a specific build status.

    The authenticated user must have **REPO_ADMIN** permission for the provided repository.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteResponse400 | DeleteResponse401 | DeleteResponse404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            commit_id=commit_id,
            client=client,
            key=key,
        )
    ).parsed
