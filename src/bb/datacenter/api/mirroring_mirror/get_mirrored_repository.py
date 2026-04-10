from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_mirrored_repository_response_404 import GetMirroredRepositoryResponse404
from ...models.rest_mirrored_repository import RestMirroredRepository
from ...types import Response


def _get_kwargs(
    external_repository_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/mirroring/latest/mirrorRepos/{external_repository_id}".format(
            external_repository_id=quote(str(external_repository_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetMirroredRepositoryResponse404 | RestMirroredRepository | None:
    if response.status_code == 200:
        response_200 = RestMirroredRepository.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = GetMirroredRepositoryResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetMirroredRepositoryResponse404 | RestMirroredRepository]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    external_repository_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetMirroredRepositoryResponse404 | RestMirroredRepository]:
    """Get clone URLs

     Retrieves all available clone urls for the specified repository.

    Args:
        external_repository_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMirroredRepositoryResponse404 | RestMirroredRepository]
    """

    kwargs = _get_kwargs(
        external_repository_id=external_repository_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    external_repository_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetMirroredRepositoryResponse404 | RestMirroredRepository | None:
    """Get clone URLs

     Retrieves all available clone urls for the specified repository.

    Args:
        external_repository_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMirroredRepositoryResponse404 | RestMirroredRepository
    """

    return sync_detailed(
        external_repository_id=external_repository_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    external_repository_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetMirroredRepositoryResponse404 | RestMirroredRepository]:
    """Get clone URLs

     Retrieves all available clone urls for the specified repository.

    Args:
        external_repository_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMirroredRepositoryResponse404 | RestMirroredRepository]
    """

    kwargs = _get_kwargs(
        external_repository_id=external_repository_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    external_repository_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetMirroredRepositoryResponse404 | RestMirroredRepository | None:
    """Get clone URLs

     Retrieves all available clone urls for the specified repository.

    Args:
        external_repository_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMirroredRepositoryResponse404 | RestMirroredRepository
    """

    return (
        await asyncio_detailed(
            external_repository_id=external_repository_id,
            client=client,
        )
    ).parsed
