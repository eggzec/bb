from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_allowlist_rule_response_401 import GetAllowlistRuleResponse401
from ...models.get_allowlist_rule_response_404 import GetAllowlistRuleResponse404
from ...models.rest_secret_scanning_allowlist_rule import RestSecretScanningAllowlistRule
from ...types import Response


def _get_kwargs(
    project_key: str,
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/secret-scanning/allowlist/{id}".format(
            project_key=quote(str(project_key), safe=""),
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetAllowlistRuleResponse401 | GetAllowlistRuleResponse404 | RestSecretScanningAllowlistRule | None:
    if response.status_code == 200:
        response_200 = RestSecretScanningAllowlistRule.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetAllowlistRuleResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetAllowlistRuleResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetAllowlistRuleResponse401 | GetAllowlistRuleResponse404 | RestSecretScanningAllowlistRule]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetAllowlistRuleResponse401 | GetAllowlistRuleResponse404 | RestSecretScanningAllowlistRule]:
    """Get a project secret scanning allowlist rule

     Get a project secret scanning allowlist rule by ID.

    Project **Admin** is required

    Args:
        project_key (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAllowlistRuleResponse401 | GetAllowlistRuleResponse404 | RestSecretScanningAllowlistRule]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetAllowlistRuleResponse401 | GetAllowlistRuleResponse404 | RestSecretScanningAllowlistRule | None:
    """Get a project secret scanning allowlist rule

     Get a project secret scanning allowlist rule by ID.

    Project **Admin** is required

    Args:
        project_key (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAllowlistRuleResponse401 | GetAllowlistRuleResponse404 | RestSecretScanningAllowlistRule
    """

    return sync_detailed(
        project_key=project_key,
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetAllowlistRuleResponse401 | GetAllowlistRuleResponse404 | RestSecretScanningAllowlistRule]:
    """Get a project secret scanning allowlist rule

     Get a project secret scanning allowlist rule by ID.

    Project **Admin** is required

    Args:
        project_key (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAllowlistRuleResponse401 | GetAllowlistRuleResponse404 | RestSecretScanningAllowlistRule]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetAllowlistRuleResponse401 | GetAllowlistRuleResponse404 | RestSecretScanningAllowlistRule | None:
    """Get a project secret scanning allowlist rule

     Get a project secret scanning allowlist rule by ID.

    Project **Admin** is required

    Args:
        project_key (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAllowlistRuleResponse401 | GetAllowlistRuleResponse404 | RestSecretScanningAllowlistRule
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            id=id,
            client=client,
        )
    ).parsed
