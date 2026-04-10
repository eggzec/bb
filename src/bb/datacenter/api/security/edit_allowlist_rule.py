from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.edit_allowlist_rule_response_400 import EditAllowlistRuleResponse400
from ...models.edit_allowlist_rule_response_401 import EditAllowlistRuleResponse401
from ...models.rest_secret_scanning_allowlist_rule import RestSecretScanningAllowlistRule
from ...models.rest_secret_scanning_allowlist_rule_set_request import RestSecretScanningAllowlistRuleSetRequest
from ...types import Response


def _get_kwargs(
    project_key: str,
    id: str,
    *,
    body: RestSecretScanningAllowlistRuleSetRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/latest/projects/{project_key}/secret-scanning/allowlist/{id}".format(
            project_key=quote(str(project_key), safe=""),
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EditAllowlistRuleResponse400 | EditAllowlistRuleResponse401 | RestSecretScanningAllowlistRule | None:
    if response.status_code == 200:
        response_200 = RestSecretScanningAllowlistRule.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = EditAllowlistRuleResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = EditAllowlistRuleResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[EditAllowlistRuleResponse400 | EditAllowlistRuleResponse401 | RestSecretScanningAllowlistRule]:
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
    body: RestSecretScanningAllowlistRuleSetRequest,
) -> Response[EditAllowlistRuleResponse400 | EditAllowlistRuleResponse401 | RestSecretScanningAllowlistRule]:
    """Edit an existing project secret scanning allowlist rule

     Edit a project secret scanning allowlist rule.

    Project **Admin** is required

    Args:
        project_key (str):
        id (str):
        body (RestSecretScanningAllowlistRuleSetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EditAllowlistRuleResponse400 | EditAllowlistRuleResponse401 | RestSecretScanningAllowlistRule]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        id=id,
        body=body,
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
    body: RestSecretScanningAllowlistRuleSetRequest,
) -> EditAllowlistRuleResponse400 | EditAllowlistRuleResponse401 | RestSecretScanningAllowlistRule | None:
    """Edit an existing project secret scanning allowlist rule

     Edit a project secret scanning allowlist rule.

    Project **Admin** is required

    Args:
        project_key (str):
        id (str):
        body (RestSecretScanningAllowlistRuleSetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EditAllowlistRuleResponse400 | EditAllowlistRuleResponse401 | RestSecretScanningAllowlistRule
    """

    return sync_detailed(
        project_key=project_key,
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestSecretScanningAllowlistRuleSetRequest,
) -> Response[EditAllowlistRuleResponse400 | EditAllowlistRuleResponse401 | RestSecretScanningAllowlistRule]:
    """Edit an existing project secret scanning allowlist rule

     Edit a project secret scanning allowlist rule.

    Project **Admin** is required

    Args:
        project_key (str):
        id (str):
        body (RestSecretScanningAllowlistRuleSetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EditAllowlistRuleResponse400 | EditAllowlistRuleResponse401 | RestSecretScanningAllowlistRule]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestSecretScanningAllowlistRuleSetRequest,
) -> EditAllowlistRuleResponse400 | EditAllowlistRuleResponse401 | RestSecretScanningAllowlistRule | None:
    """Edit an existing project secret scanning allowlist rule

     Edit a project secret scanning allowlist rule.

    Project **Admin** is required

    Args:
        project_key (str):
        id (str):
        body (RestSecretScanningAllowlistRuleSetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EditAllowlistRuleResponse400 | EditAllowlistRuleResponse401 | RestSecretScanningAllowlistRule
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            id=id,
            client=client,
            body=body,
        )
    ).parsed
