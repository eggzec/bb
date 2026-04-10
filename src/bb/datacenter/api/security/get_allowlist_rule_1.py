from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_allowlist_rule_1_response_401 import GetAllowlistRule1Response401
from ...models.get_allowlist_rule_1_response_404 import GetAllowlistRule1Response404
from ...models.rest_secret_scanning_allowlist_rule import RestSecretScanningAllowlistRule
from ...types import Response


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/secret-scanning/allowlist/{id}".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetAllowlistRule1Response401 | GetAllowlistRule1Response404 | RestSecretScanningAllowlistRule | None:
    if response.status_code == 200:
        response_200 = RestSecretScanningAllowlistRule.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetAllowlistRule1Response401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetAllowlistRule1Response404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetAllowlistRule1Response401 | GetAllowlistRule1Response404 | RestSecretScanningAllowlistRule]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    repository_slug: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetAllowlistRule1Response401 | GetAllowlistRule1Response404 | RestSecretScanningAllowlistRule]:
    """Get a repository secret scanning allowlist rule

     Get a repository secret scanning allowlist rule by ID.

    Repository **Admin** is required

    Args:
        project_key (str):
        repository_slug (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAllowlistRule1Response401 | GetAllowlistRule1Response404 | RestSecretScanningAllowlistRule]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    repository_slug: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetAllowlistRule1Response401 | GetAllowlistRule1Response404 | RestSecretScanningAllowlistRule | None:
    """Get a repository secret scanning allowlist rule

     Get a repository secret scanning allowlist rule by ID.

    Repository **Admin** is required

    Args:
        project_key (str):
        repository_slug (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAllowlistRule1Response401 | GetAllowlistRule1Response404 | RestSecretScanningAllowlistRule
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetAllowlistRule1Response401 | GetAllowlistRule1Response404 | RestSecretScanningAllowlistRule]:
    """Get a repository secret scanning allowlist rule

     Get a repository secret scanning allowlist rule by ID.

    Repository **Admin** is required

    Args:
        project_key (str):
        repository_slug (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAllowlistRule1Response401 | GetAllowlistRule1Response404 | RestSecretScanningAllowlistRule]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetAllowlistRule1Response401 | GetAllowlistRule1Response404 | RestSecretScanningAllowlistRule | None:
    """Get a repository secret scanning allowlist rule

     Get a repository secret scanning allowlist rule by ID.

    Repository **Admin** is required

    Args:
        project_key (str):
        repository_slug (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAllowlistRule1Response401 | GetAllowlistRule1Response404 | RestSecretScanningAllowlistRule
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            id=id,
            client=client,
        )
    ).parsed
