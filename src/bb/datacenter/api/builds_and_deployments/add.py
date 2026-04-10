from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_response_400 import AddResponse400
from ...models.add_response_401 import AddResponse401
from ...models.add_response_404 import AddResponse404
from ...models.rest_build_status_set_request import RestBuildStatusSetRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    *,
    body: RestBuildStatusSetRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/commits/{commit_id}/builds".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            commit_id=quote(str(commit_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AddResponse400 | AddResponse401 | AddResponse404 | Any | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = AddResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = AddResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = AddResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AddResponse400 | AddResponse401 | AddResponse404 | Any]:
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
    body: RestBuildStatusSetRequest | Unset = UNSET,
) -> Response[AddResponse400 | AddResponse401 | AddResponse404 | Any]:
    """Store a build status

     Store a build status.


    The authenticated user must have **REPO_READ** permission for the repository that this build status
    is for. The request can also be made with anonymous 2-legged OAuth.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        body (RestBuildStatusSetRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddResponse400 | AddResponse401 | AddResponse404 | Any]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        body=body,
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
    body: RestBuildStatusSetRequest | Unset = UNSET,
) -> AddResponse400 | AddResponse401 | AddResponse404 | Any | None:
    """Store a build status

     Store a build status.


    The authenticated user must have **REPO_READ** permission for the repository that this build status
    is for. The request can also be made with anonymous 2-legged OAuth.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        body (RestBuildStatusSetRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddResponse400 | AddResponse401 | AddResponse404 | Any
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestBuildStatusSetRequest | Unset = UNSET,
) -> Response[AddResponse400 | AddResponse401 | AddResponse404 | Any]:
    """Store a build status

     Store a build status.


    The authenticated user must have **REPO_READ** permission for the repository that this build status
    is for. The request can also be made with anonymous 2-legged OAuth.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        body (RestBuildStatusSetRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddResponse400 | AddResponse401 | AddResponse404 | Any]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestBuildStatusSetRequest | Unset = UNSET,
) -> AddResponse400 | AddResponse401 | AddResponse404 | Any | None:
    """Store a build status

     Store a build status.


    The authenticated user must have **REPO_READ** permission for the repository that this build status
    is for. The request can also be made with anonymous 2-legged OAuth.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        body (RestBuildStatusSetRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddResponse400 | AddResponse401 | AddResponse404 | Any
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            commit_id=commit_id,
            client=client,
            body=body,
        )
    ).parsed
