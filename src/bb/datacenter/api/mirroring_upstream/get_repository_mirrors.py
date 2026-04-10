from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_repository_mirrors_response_409 import GetRepositoryMirrorsResponse409
from ...models.rest_mirrored_repository_descriptor import RestMirroredRepositoryDescriptor
from ...types import UNSET, Response, Unset


def _get_kwargs(
    repo_id: str,
    *,
    pre_authorized: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["preAuthorized"] = pre_authorized

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/mirroring/latest/repos/{repo_id}/mirrors".format(
            repo_id=quote(str(repo_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetRepositoryMirrorsResponse409 | RestMirroredRepositoryDescriptor | None:
    if response.status_code == 200:
        response_200 = RestMirroredRepositoryDescriptor.from_dict(response.json())

        return response_200

    if response.status_code == 409:
        response_409 = GetRepositoryMirrorsResponse409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetRepositoryMirrorsResponse409 | RestMirroredRepositoryDescriptor]:
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
    pre_authorized: bool | Unset = UNSET,
) -> Response[GetRepositoryMirrorsResponse409 | RestMirroredRepositoryDescriptor]:
    """Get mirrors for repository

     Returns a page of mirrors for a repository. This resource will return <strong>all mirrors</strong>
    along with authorized links to the mirror's repository REST resource. To determine if a repository
    is available on the mirror, the returned URL needs to be called.

    Args:
        repo_id (str):
        pre_authorized (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRepositoryMirrorsResponse409 | RestMirroredRepositoryDescriptor]
    """

    kwargs = _get_kwargs(
        repo_id=repo_id,
        pre_authorized=pre_authorized,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    repo_id: str,
    *,
    client: AuthenticatedClient | Client,
    pre_authorized: bool | Unset = UNSET,
) -> GetRepositoryMirrorsResponse409 | RestMirroredRepositoryDescriptor | None:
    """Get mirrors for repository

     Returns a page of mirrors for a repository. This resource will return <strong>all mirrors</strong>
    along with authorized links to the mirror's repository REST resource. To determine if a repository
    is available on the mirror, the returned URL needs to be called.

    Args:
        repo_id (str):
        pre_authorized (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRepositoryMirrorsResponse409 | RestMirroredRepositoryDescriptor
    """

    return sync_detailed(
        repo_id=repo_id,
        client=client,
        pre_authorized=pre_authorized,
    ).parsed


async def asyncio_detailed(
    repo_id: str,
    *,
    client: AuthenticatedClient | Client,
    pre_authorized: bool | Unset = UNSET,
) -> Response[GetRepositoryMirrorsResponse409 | RestMirroredRepositoryDescriptor]:
    """Get mirrors for repository

     Returns a page of mirrors for a repository. This resource will return <strong>all mirrors</strong>
    along with authorized links to the mirror's repository REST resource. To determine if a repository
    is available on the mirror, the returned URL needs to be called.

    Args:
        repo_id (str):
        pre_authorized (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRepositoryMirrorsResponse409 | RestMirroredRepositoryDescriptor]
    """

    kwargs = _get_kwargs(
        repo_id=repo_id,
        pre_authorized=pre_authorized,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    repo_id: str,
    *,
    client: AuthenticatedClient | Client,
    pre_authorized: bool | Unset = UNSET,
) -> GetRepositoryMirrorsResponse409 | RestMirroredRepositoryDescriptor | None:
    """Get mirrors for repository

     Returns a page of mirrors for a repository. This resource will return <strong>all mirrors</strong>
    along with authorized links to the mirror's repository REST resource. To determine if a repository
    is available on the mirror, the returned URL needs to be called.

    Args:
        repo_id (str):
        pre_authorized (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRepositoryMirrorsResponse409 | RestMirroredRepositoryDescriptor
    """

    return (
        await asyncio_detailed(
            repo_id=repo_id,
            client=client,
            pre_authorized=pre_authorized,
        )
    ).parsed
