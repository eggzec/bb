from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.edit_allowlist_rule_1_response_400 import EditAllowlistRule1Response400
from ...models.edit_allowlist_rule_1_response_401 import EditAllowlistRule1Response401
from ...models.rest_secret_scanning_allowlist_rule import RestSecretScanningAllowlistRule
from ...models.rest_secret_scanning_allowlist_rule_set_request import RestSecretScanningAllowlistRuleSetRequest
from ...types import Response


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    id: str,
    *,
    body: RestSecretScanningAllowlistRuleSetRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/secret-scanning/allowlist/{id}".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EditAllowlistRule1Response400 | EditAllowlistRule1Response401 | RestSecretScanningAllowlistRule | None:
    if response.status_code == 200:
        response_200 = RestSecretScanningAllowlistRule.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = EditAllowlistRule1Response400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = EditAllowlistRule1Response401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[EditAllowlistRule1Response400 | EditAllowlistRule1Response401 | RestSecretScanningAllowlistRule]:
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
    body: RestSecretScanningAllowlistRuleSetRequest,
) -> Response[EditAllowlistRule1Response400 | EditAllowlistRule1Response401 | RestSecretScanningAllowlistRule]:
    """Edit an existing repository secret scanning allowlist rule

     Edit a repository secret scanning allowlist rule.

    Repository **Admin** is required

    Args:
        project_key (str):
        repository_slug (str):
        id (str):
        body (RestSecretScanningAllowlistRuleSetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EditAllowlistRule1Response400 | EditAllowlistRule1Response401 | RestSecretScanningAllowlistRule]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        id=id,
        body=body,
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
    body: RestSecretScanningAllowlistRuleSetRequest,
) -> EditAllowlistRule1Response400 | EditAllowlistRule1Response401 | RestSecretScanningAllowlistRule | None:
    """Edit an existing repository secret scanning allowlist rule

     Edit a repository secret scanning allowlist rule.

    Repository **Admin** is required

    Args:
        project_key (str):
        repository_slug (str):
        id (str):
        body (RestSecretScanningAllowlistRuleSetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EditAllowlistRule1Response400 | EditAllowlistRule1Response401 | RestSecretScanningAllowlistRule
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestSecretScanningAllowlistRuleSetRequest,
) -> Response[EditAllowlistRule1Response400 | EditAllowlistRule1Response401 | RestSecretScanningAllowlistRule]:
    """Edit an existing repository secret scanning allowlist rule

     Edit a repository secret scanning allowlist rule.

    Repository **Admin** is required

    Args:
        project_key (str):
        repository_slug (str):
        id (str):
        body (RestSecretScanningAllowlistRuleSetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EditAllowlistRule1Response400 | EditAllowlistRule1Response401 | RestSecretScanningAllowlistRule]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestSecretScanningAllowlistRuleSetRequest,
) -> EditAllowlistRule1Response400 | EditAllowlistRule1Response401 | RestSecretScanningAllowlistRule | None:
    """Edit an existing repository secret scanning allowlist rule

     Edit a repository secret scanning allowlist rule.

    Repository **Admin** is required

    Args:
        project_key (str):
        repository_slug (str):
        id (str):
        body (RestSecretScanningAllowlistRuleSetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EditAllowlistRule1Response400 | EditAllowlistRule1Response401 | RestSecretScanningAllowlistRule
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            id=id,
            client=client,
            body=body,
        )
    ).parsed
