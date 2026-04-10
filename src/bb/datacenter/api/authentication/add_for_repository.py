from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_for_repository_response_400 import AddForRepositoryResponse400
from ...models.add_for_repository_response_401 import AddForRepositoryResponse401
from ...models.add_for_repository_response_404 import AddForRepositoryResponse404
from ...models.rest_ssh_access_key import RestSshAccessKey
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    *,
    body: RestSshAccessKey | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/keys/latest/projects/{project_key}/repos/{repository_slug}/ssh".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AddForRepositoryResponse400 | AddForRepositoryResponse401 | AddForRepositoryResponse404 | RestSshAccessKey | None:
    if response.status_code == 201:
        response_201 = RestSshAccessKey.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = AddForRepositoryResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = AddForRepositoryResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = AddForRepositoryResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AddForRepositoryResponse400 | AddForRepositoryResponse401 | AddForRepositoryResponse404 | RestSshAccessKey
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestSshAccessKey | Unset = UNSET,
) -> Response[
    AddForRepositoryResponse400 | AddForRepositoryResponse401 | AddForRepositoryResponse404 | RestSshAccessKey
]:
    """Add repository SSH key

     Register a new SSH key and grants access to the repository identified in the URL.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestSshAccessKey | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddForRepositoryResponse400 | AddForRepositoryResponse401 | AddForRepositoryResponse404 | RestSshAccessKey]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestSshAccessKey | Unset = UNSET,
) -> AddForRepositoryResponse400 | AddForRepositoryResponse401 | AddForRepositoryResponse404 | RestSshAccessKey | None:
    """Add repository SSH key

     Register a new SSH key and grants access to the repository identified in the URL.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestSshAccessKey | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddForRepositoryResponse400 | AddForRepositoryResponse401 | AddForRepositoryResponse404 | RestSshAccessKey
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestSshAccessKey | Unset = UNSET,
) -> Response[
    AddForRepositoryResponse400 | AddForRepositoryResponse401 | AddForRepositoryResponse404 | RestSshAccessKey
]:
    """Add repository SSH key

     Register a new SSH key and grants access to the repository identified in the URL.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestSshAccessKey | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddForRepositoryResponse400 | AddForRepositoryResponse401 | AddForRepositoryResponse404 | RestSshAccessKey]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestSshAccessKey | Unset = UNSET,
) -> AddForRepositoryResponse400 | AddForRepositoryResponse401 | AddForRepositoryResponse404 | RestSshAccessKey | None:
    """Add repository SSH key

     Register a new SSH key and grants access to the repository identified in the URL.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestSshAccessKey | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddForRepositoryResponse400 | AddForRepositoryResponse401 | AddForRepositoryResponse404 | RestSshAccessKey
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            client=client,
            body=body,
        )
    ).parsed
