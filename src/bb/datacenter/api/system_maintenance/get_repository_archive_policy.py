from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_repository_archive_policy_response_401 import GetRepositoryArchivePolicyResponse401
from ...models.rest_repository_policy import RestRepositoryPolicy
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/policies/latest/admin/repos/archive",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetRepositoryArchivePolicyResponse401 | RestRepositoryPolicy | None:
    if response.status_code == 200:
        response_200 = RestRepositoryPolicy.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetRepositoryArchivePolicyResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetRepositoryArchivePolicyResponse401 | RestRepositoryPolicy]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetRepositoryArchivePolicyResponse401 | RestRepositoryPolicy]:
    """Get repository archive policy

     Retrieves the repository archive policy for the instance.

    The user must be authenticated to access this resource.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRepositoryArchivePolicyResponse401 | RestRepositoryPolicy]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> GetRepositoryArchivePolicyResponse401 | RestRepositoryPolicy | None:
    """Get repository archive policy

     Retrieves the repository archive policy for the instance.

    The user must be authenticated to access this resource.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRepositoryArchivePolicyResponse401 | RestRepositoryPolicy
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetRepositoryArchivePolicyResponse401 | RestRepositoryPolicy]:
    """Get repository archive policy

     Retrieves the repository archive policy for the instance.

    The user must be authenticated to access this resource.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRepositoryArchivePolicyResponse401 | RestRepositoryPolicy]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> GetRepositoryArchivePolicyResponse401 | RestRepositoryPolicy | None:
    """Get repository archive policy

     Retrieves the repository archive policy for the instance.

    The user must be authenticated to access this resource.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRepositoryArchivePolicyResponse401 | RestRepositoryPolicy
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
