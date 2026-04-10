from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_merge_base_response_400 import GetMergeBaseResponse400
from ...models.get_merge_base_response_404 import GetMergeBaseResponse404
from ...models.rest_commit import RestCommit
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    *,
    other_commit_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["otherCommitId"] = other_commit_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/commits/{commit_id}/merge-base".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            commit_id=quote(str(commit_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetMergeBaseResponse400 | GetMergeBaseResponse404 | RestCommit | None:
    if response.status_code == 200:
        response_200 = RestCommit.from_dict(response.json())

        return response_200

    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = GetMergeBaseResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = GetMergeBaseResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetMergeBaseResponse400 | GetMergeBaseResponse404 | RestCommit]:
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
    other_commit_id: str | Unset = UNSET,
) -> Response[Any | GetMergeBaseResponse400 | GetMergeBaseResponse404 | RestCommit]:
    """Get the common ancestor between two commits

     Returns the best common ancestor between two commits.

    If more than one best common ancestor exists, only one will be returned. It is unspecified which
    will be returned.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        other_commit_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetMergeBaseResponse400 | GetMergeBaseResponse404 | RestCommit]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        other_commit_id=other_commit_id,
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
    other_commit_id: str | Unset = UNSET,
) -> Any | GetMergeBaseResponse400 | GetMergeBaseResponse404 | RestCommit | None:
    """Get the common ancestor between two commits

     Returns the best common ancestor between two commits.

    If more than one best common ancestor exists, only one will be returned. It is unspecified which
    will be returned.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        other_commit_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetMergeBaseResponse400 | GetMergeBaseResponse404 | RestCommit
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        client=client,
        other_commit_id=other_commit_id,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    *,
    client: AuthenticatedClient | Client,
    other_commit_id: str | Unset = UNSET,
) -> Response[Any | GetMergeBaseResponse400 | GetMergeBaseResponse404 | RestCommit]:
    """Get the common ancestor between two commits

     Returns the best common ancestor between two commits.

    If more than one best common ancestor exists, only one will be returned. It is unspecified which
    will be returned.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        other_commit_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetMergeBaseResponse400 | GetMergeBaseResponse404 | RestCommit]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        other_commit_id=other_commit_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    *,
    client: AuthenticatedClient | Client,
    other_commit_id: str | Unset = UNSET,
) -> Any | GetMergeBaseResponse400 | GetMergeBaseResponse404 | RestCommit | None:
    """Get the common ancestor between two commits

     Returns the best common ancestor between two commits.

    If more than one best common ancestor exists, only one will be returned. It is unspecified which
    will be returned.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        other_commit_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetMergeBaseResponse400 | GetMergeBaseResponse404 | RestCommit
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            commit_id=commit_id,
            client=client,
            other_commit_id=other_commit_id,
        )
    ).parsed
