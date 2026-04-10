from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_rule_1_response_400 import CreateRule1Response400
from ...models.create_rule_1_response_401 import CreateRule1Response401
from ...models.rest_secret_scanning_rule import RestSecretScanningRule
from ...models.rest_secret_scanning_rule_set_request import RestSecretScanningRuleSetRequest
from ...types import Response


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    *,
    body: RestSecretScanningRuleSetRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/secret-scanning/rules".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateRule1Response400 | CreateRule1Response401 | RestSecretScanningRule | None:
    if response.status_code == 200:
        response_200 = RestSecretScanningRule.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CreateRule1Response400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = CreateRule1Response401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateRule1Response400 | CreateRule1Response401 | RestSecretScanningRule]:
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
    body: RestSecretScanningRuleSetRequest,
) -> Response[CreateRule1Response400 | CreateRule1Response401 | RestSecretScanningRule]:
    """Create repository secret scanning rule

     Create a new repository secret scanning rule. Repository rules are used when scanning the given
    repository.

    Repository **Admin** is required

    Args:
        project_key (str):
        repository_slug (str):
        body (RestSecretScanningRuleSetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateRule1Response400 | CreateRule1Response401 | RestSecretScanningRule]
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
    body: RestSecretScanningRuleSetRequest,
) -> CreateRule1Response400 | CreateRule1Response401 | RestSecretScanningRule | None:
    """Create repository secret scanning rule

     Create a new repository secret scanning rule. Repository rules are used when scanning the given
    repository.

    Repository **Admin** is required

    Args:
        project_key (str):
        repository_slug (str):
        body (RestSecretScanningRuleSetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateRule1Response400 | CreateRule1Response401 | RestSecretScanningRule
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
    body: RestSecretScanningRuleSetRequest,
) -> Response[CreateRule1Response400 | CreateRule1Response401 | RestSecretScanningRule]:
    """Create repository secret scanning rule

     Create a new repository secret scanning rule. Repository rules are used when scanning the given
    repository.

    Repository **Admin** is required

    Args:
        project_key (str):
        repository_slug (str):
        body (RestSecretScanningRuleSetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateRule1Response400 | CreateRule1Response401 | RestSecretScanningRule]
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
    body: RestSecretScanningRuleSetRequest,
) -> CreateRule1Response400 | CreateRule1Response401 | RestSecretScanningRule | None:
    """Create repository secret scanning rule

     Create a new repository secret scanning rule. Repository rules are used when scanning the given
    repository.

    Repository **Admin** is required

    Args:
        project_key (str):
        repository_slug (str):
        body (RestSecretScanningRuleSetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateRule1Response400 | CreateRule1Response401 | RestSecretScanningRule
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            client=client,
            body=body,
        )
    ).parsed
