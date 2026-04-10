from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.enriched_repository import EnrichedRepository
from ...models.get_content_hash_by_id_response_404 import GetContentHashByIdResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    repo_id: str,
    *,
    include_default_branch: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["includeDefaultBranch"] = include_default_branch

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/mirroring/latest/repos/{repo_id}".format(
            repo_id=quote(str(repo_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EnrichedRepository | GetContentHashByIdResponse404 | None:
    if response.status_code == 200:
        response_200 = EnrichedRepository.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = GetContentHashByIdResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[EnrichedRepository | GetContentHashByIdResponse404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    repo_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_default_branch: bool | Unset = False,
) -> Response[EnrichedRepository | GetContentHashByIdResponse404]:
    """Get content hash for a repository

     Returns a repository enriched with a content hash and default branch

    Args:
        repo_id (str):
        include_default_branch (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EnrichedRepository | GetContentHashByIdResponse404]
    """

    kwargs = _get_kwargs(
        repo_id=repo_id,
        include_default_branch=include_default_branch,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    repo_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_default_branch: bool | Unset = False,
) -> EnrichedRepository | GetContentHashByIdResponse404 | None:
    """Get content hash for a repository

     Returns a repository enriched with a content hash and default branch

    Args:
        repo_id (str):
        include_default_branch (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EnrichedRepository | GetContentHashByIdResponse404
    """

    return sync_detailed(
        repo_id=repo_id,
        client=client,
        include_default_branch=include_default_branch,
    ).parsed


async def asyncio_detailed(
    repo_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_default_branch: bool | Unset = False,
) -> Response[EnrichedRepository | GetContentHashByIdResponse404]:
    """Get content hash for a repository

     Returns a repository enriched with a content hash and default branch

    Args:
        repo_id (str):
        include_default_branch (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EnrichedRepository | GetContentHashByIdResponse404]
    """

    kwargs = _get_kwargs(
        repo_id=repo_id,
        include_default_branch=include_default_branch,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    repo_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_default_branch: bool | Unset = False,
) -> EnrichedRepository | GetContentHashByIdResponse404 | None:
    """Get content hash for a repository

     Returns a repository enriched with a content hash and default branch

    Args:
        repo_id (str):
        include_default_branch (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EnrichedRepository | GetContentHashByIdResponse404
    """

    return (
        await asyncio_detailed(
            repo_id=repo_id,
            client=client,
            include_default_branch=include_default_branch,
        )
    ).parsed
