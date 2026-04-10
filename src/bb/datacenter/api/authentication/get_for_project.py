from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_for_project_response_401 import GetForProjectResponse401
from ...models.get_for_project_response_404 import GetForProjectResponse404
from ...models.rest_ssh_access_key import RestSshAccessKey
from ...types import Response


def _get_kwargs(
    project_key: str,
    key_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/keys/latest/projects/{project_key}/ssh/{key_id}".format(
            project_key=quote(str(project_key), safe=""),
            key_id=quote(str(key_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetForProjectResponse401 | GetForProjectResponse404 | RestSshAccessKey | None:
    if response.status_code == 200:
        response_200 = RestSshAccessKey.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetForProjectResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetForProjectResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetForProjectResponse401 | GetForProjectResponse404 | RestSshAccessKey]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    key_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetForProjectResponse401 | GetForProjectResponse404 | RestSshAccessKey]:
    """Get project SSH key

     Retrieves the access key for the SSH key with id <code>keyId</code> on the project identified in the
    URL.

    Args:
        project_key (str):
        key_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetForProjectResponse401 | GetForProjectResponse404 | RestSshAccessKey]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        key_id=key_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    key_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetForProjectResponse401 | GetForProjectResponse404 | RestSshAccessKey | None:
    """Get project SSH key

     Retrieves the access key for the SSH key with id <code>keyId</code> on the project identified in the
    URL.

    Args:
        project_key (str):
        key_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetForProjectResponse401 | GetForProjectResponse404 | RestSshAccessKey
    """

    return sync_detailed(
        project_key=project_key,
        key_id=key_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    key_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetForProjectResponse401 | GetForProjectResponse404 | RestSshAccessKey]:
    """Get project SSH key

     Retrieves the access key for the SSH key with id <code>keyId</code> on the project identified in the
    URL.

    Args:
        project_key (str):
        key_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetForProjectResponse401 | GetForProjectResponse404 | RestSshAccessKey]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        key_id=key_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    key_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetForProjectResponse401 | GetForProjectResponse404 | RestSshAccessKey | None:
    """Get project SSH key

     Retrieves the access key for the SSH key with id <code>keyId</code> on the project identified in the
    URL.

    Args:
        project_key (str):
        key_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetForProjectResponse401 | GetForProjectResponse404 | RestSshAccessKey
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            key_id=key_id,
            client=client,
        )
    ).parsed
