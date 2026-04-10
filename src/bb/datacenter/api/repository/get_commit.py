from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_commit_response_400 import GetCommitResponse400
from ...models.get_commit_response_404 import GetCommitResponse404
from ...models.rest_commit import RestCommit
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    *,
    path: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["path"] = path

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/commits/{commit_id}".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            commit_id=quote(str(commit_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetCommitResponse400 | GetCommitResponse404 | RestCommit | None:
    if response.status_code == 200:
        response_200 = RestCommit.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetCommitResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = GetCommitResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetCommitResponse400 | GetCommitResponse404 | RestCommit]:
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
    path: str | Unset = UNSET,
) -> Response[GetCommitResponse400 | GetCommitResponse404 | RestCommit]:
    r"""Get commit by ID

     Retrieve a single commit <i>identified by its ID</i>. In general, that ID is a SHA1. <u>From 2.11,
    ref names like \"refs/heads/master\" are no longer accepted by this resource.</u>

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        path (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCommitResponse400 | GetCommitResponse404 | RestCommit]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        path=path,
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
    path: str | Unset = UNSET,
) -> GetCommitResponse400 | GetCommitResponse404 | RestCommit | None:
    r"""Get commit by ID

     Retrieve a single commit <i>identified by its ID</i>. In general, that ID is a SHA1. <u>From 2.11,
    ref names like \"refs/heads/master\" are no longer accepted by this resource.</u>

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        path (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCommitResponse400 | GetCommitResponse404 | RestCommit
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        client=client,
        path=path,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    *,
    client: AuthenticatedClient | Client,
    path: str | Unset = UNSET,
) -> Response[GetCommitResponse400 | GetCommitResponse404 | RestCommit]:
    r"""Get commit by ID

     Retrieve a single commit <i>identified by its ID</i>. In general, that ID is a SHA1. <u>From 2.11,
    ref names like \"refs/heads/master\" are no longer accepted by this resource.</u>

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        path (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCommitResponse400 | GetCommitResponse404 | RestCommit]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        path=path,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    *,
    client: AuthenticatedClient | Client,
    path: str | Unset = UNSET,
) -> GetCommitResponse400 | GetCommitResponse404 | RestCommit | None:
    r"""Get commit by ID

     Retrieve a single commit <i>identified by its ID</i>. In general, that ID is a SHA1. <u>From 2.11,
    ref names like \"refs/heads/master\" are no longer accepted by this resource.</u>

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        path (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCommitResponse400 | GetCommitResponse404 | RestCommit
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            commit_id=commit_id,
            client=client,
            path=path,
        )
    ).parsed
