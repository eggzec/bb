from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.enriched_repository import EnrichedRepository
from ...models.get_all_content_hashes_include_default_branch import GetAllContentHashesIncludeDefaultBranch
from ...models.get_all_content_hashes_response_409 import GetAllContentHashesResponse409
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include_default_branch: GetAllContentHashesIncludeDefaultBranch
    | Unset = GetAllContentHashesIncludeDefaultBranch.FALSE,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_include_default_branch: str | Unset = UNSET
    if not isinstance(include_default_branch, Unset):
        json_include_default_branch = include_default_branch.value

    params["includeDefaultBranch"] = json_include_default_branch

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/mirroring/latest/repos",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EnrichedRepository | GetAllContentHashesResponse409 | None:
    if response.status_code == 200:
        response_200 = EnrichedRepository.from_dict(response.json())

        return response_200

    if response.status_code == 409:
        response_409 = GetAllContentHashesResponse409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[EnrichedRepository | GetAllContentHashesResponse409]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    include_default_branch: GetAllContentHashesIncludeDefaultBranch
    | Unset = GetAllContentHashesIncludeDefaultBranch.FALSE,
) -> Response[EnrichedRepository | GetAllContentHashesResponse409]:
    """Get content hashes for repositories

     Returns a page of repositories enriched with a content hash and default branch

    Args:
        include_default_branch (GetAllContentHashesIncludeDefaultBranch | Unset):  Default:
            GetAllContentHashesIncludeDefaultBranch.FALSE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EnrichedRepository | GetAllContentHashesResponse409]
    """

    kwargs = _get_kwargs(
        include_default_branch=include_default_branch,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    include_default_branch: GetAllContentHashesIncludeDefaultBranch
    | Unset = GetAllContentHashesIncludeDefaultBranch.FALSE,
) -> EnrichedRepository | GetAllContentHashesResponse409 | None:
    """Get content hashes for repositories

     Returns a page of repositories enriched with a content hash and default branch

    Args:
        include_default_branch (GetAllContentHashesIncludeDefaultBranch | Unset):  Default:
            GetAllContentHashesIncludeDefaultBranch.FALSE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EnrichedRepository | GetAllContentHashesResponse409
    """

    return sync_detailed(
        client=client,
        include_default_branch=include_default_branch,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    include_default_branch: GetAllContentHashesIncludeDefaultBranch
    | Unset = GetAllContentHashesIncludeDefaultBranch.FALSE,
) -> Response[EnrichedRepository | GetAllContentHashesResponse409]:
    """Get content hashes for repositories

     Returns a page of repositories enriched with a content hash and default branch

    Args:
        include_default_branch (GetAllContentHashesIncludeDefaultBranch | Unset):  Default:
            GetAllContentHashesIncludeDefaultBranch.FALSE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EnrichedRepository | GetAllContentHashesResponse409]
    """

    kwargs = _get_kwargs(
        include_default_branch=include_default_branch,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    include_default_branch: GetAllContentHashesIncludeDefaultBranch
    | Unset = GetAllContentHashesIncludeDefaultBranch.FALSE,
) -> EnrichedRepository | GetAllContentHashesResponse409 | None:
    """Get content hashes for repositories

     Returns a page of repositories enriched with a content hash and default branch

    Args:
        include_default_branch (GetAllContentHashesIncludeDefaultBranch | Unset):  Default:
            GetAllContentHashesIncludeDefaultBranch.FALSE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EnrichedRepository | GetAllContentHashesResponse409
    """

    return (
        await asyncio_detailed(
            client=client,
            include_default_branch=include_default_branch,
        )
    ).parsed
