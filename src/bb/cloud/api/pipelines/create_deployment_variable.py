from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.deployment_variable import DeploymentVariable
from ...models.error import Error
from ...types import Response

__all__ = [
    "sync_detailed",
    "asyncio_detailed",
    "sync",
    "asyncio",
]


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    environment_uuid: str,
    *,
    body: DeploymentVariable,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/repositories/{workspace}/{repo_slug}/deployments_config/environments/{environment_uuid}/variables".format(
            workspace=quote(str(workspace), safe=""),
            repo_slug=quote(str(repo_slug), safe=""),
            environment_uuid=quote(str(environment_uuid), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


type ParsedPayload = DeploymentVariable | Error
type ParseResult = DeploymentVariable | Error | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 201:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_201 = DeploymentVariable.from_dict(response.json())

        return response_201

    if response.status_code == 403:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_409 = Error.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ParsedPayload]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace: str,
    repo_slug: str,
    environment_uuid: str,
    *,
    client: AuthenticatedClient,
    body: DeploymentVariable,
) -> Response[ParsedPayload]:
    """Create a variable for an environment

     Create a deployment environment level variable.

    Args:
        workspace (str):
        repo_slug (str):
        environment_uuid (str):
        body (DeploymentVariable):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeploymentVariable | Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        environment_uuid=environment_uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    repo_slug: str,
    environment_uuid: str,
    *,
    client: AuthenticatedClient,
    body: DeploymentVariable,
) -> ParsedPayload | None:
    """Create a variable for an environment

     Create a deployment environment level variable.

    Args:
        workspace (str):
        repo_slug (str):
        environment_uuid (str):
        body (DeploymentVariable):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeploymentVariable | Error
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        environment_uuid=environment_uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    environment_uuid: str,
    *,
    client: AuthenticatedClient,
    body: DeploymentVariable,
) -> Response[ParsedPayload]:
    """Create a variable for an environment

     Create a deployment environment level variable.

    Args:
        workspace (str):
        repo_slug (str):
        environment_uuid (str):
        body (DeploymentVariable):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeploymentVariable | Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        environment_uuid=environment_uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    environment_uuid: str,
    *,
    client: AuthenticatedClient,
    body: DeploymentVariable,
) -> ParsedPayload | None:
    """Create a variable for an environment

     Create a deployment environment level variable.

    Args:
        workspace (str):
        repo_slug (str):
        environment_uuid (str):
        body (DeploymentVariable):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeploymentVariable | Error
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            environment_uuid=environment_uuid,
            client=client,
            body=body,
        )
    ).parsed
