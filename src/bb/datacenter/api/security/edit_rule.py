from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.edit_rule_response_400 import EditRuleResponse400
from ...models.edit_rule_response_401 import EditRuleResponse401
from ...models.rest_secret_scanning_rule import RestSecretScanningRule
from ...models.rest_secret_scanning_rule_set_request import RestSecretScanningRuleSetRequest
from ...types import Response


def _get_kwargs(
    project_key: str,
    id: str,
    *,
    body: RestSecretScanningRuleSetRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/latest/projects/{project_key}/secret-scanning/rules/{id}".format(
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
) -> EditRuleResponse400 | EditRuleResponse401 | RestSecretScanningRule | None:
    if response.status_code == 200:
        response_200 = RestSecretScanningRule.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = EditRuleResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = EditRuleResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[EditRuleResponse400 | EditRuleResponse401 | RestSecretScanningRule]:
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
    body: RestSecretScanningRuleSetRequest,
) -> Response[EditRuleResponse400 | EditRuleResponse401 | RestSecretScanningRule]:
    """Edit an existing project secret scanning rule

     Edit a project secret scanning rule.

    Project **Admin** is required

    Args:
        project_key (str):
        id (str):
        body (RestSecretScanningRuleSetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EditRuleResponse400 | EditRuleResponse401 | RestSecretScanningRule]
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
    body: RestSecretScanningRuleSetRequest,
) -> EditRuleResponse400 | EditRuleResponse401 | RestSecretScanningRule | None:
    """Edit an existing project secret scanning rule

     Edit a project secret scanning rule.

    Project **Admin** is required

    Args:
        project_key (str):
        id (str):
        body (RestSecretScanningRuleSetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EditRuleResponse400 | EditRuleResponse401 | RestSecretScanningRule
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
    body: RestSecretScanningRuleSetRequest,
) -> Response[EditRuleResponse400 | EditRuleResponse401 | RestSecretScanningRule]:
    """Edit an existing project secret scanning rule

     Edit a project secret scanning rule.

    Project **Admin** is required

    Args:
        project_key (str):
        id (str):
        body (RestSecretScanningRuleSetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EditRuleResponse400 | EditRuleResponse401 | RestSecretScanningRule]
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
    body: RestSecretScanningRuleSetRequest,
) -> EditRuleResponse400 | EditRuleResponse401 | RestSecretScanningRule | None:
    """Edit an existing project secret scanning rule

     Edit a project secret scanning rule.

    Project **Admin** is required

    Args:
        project_key (str):
        id (str):
        body (RestSecretScanningRuleSetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EditRuleResponse400 | EditRuleResponse401 | RestSecretScanningRule
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            id=id,
            client=client,
            body=body,
        )
    ).parsed
