from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_or_update_deployment_response_400 import CreateOrUpdateDeploymentResponse400
from ...models.create_or_update_deployment_response_401 import CreateOrUpdateDeploymentResponse401
from ...models.create_or_update_deployment_response_404 import CreateOrUpdateDeploymentResponse404
from ...models.rest_deployment import RestDeployment
from ...models.rest_deployment_set_request import RestDeploymentSetRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    *,
    body: RestDeploymentSetRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/commits/{commit_id}/deployments".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            commit_id=quote(str(commit_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CreateOrUpdateDeploymentResponse400
    | CreateOrUpdateDeploymentResponse401
    | CreateOrUpdateDeploymentResponse404
    | RestDeployment
    | None
):
    if response.status_code == 200:
        response_200 = RestDeployment.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CreateOrUpdateDeploymentResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = CreateOrUpdateDeploymentResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = CreateOrUpdateDeploymentResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CreateOrUpdateDeploymentResponse400
    | CreateOrUpdateDeploymentResponse401
    | CreateOrUpdateDeploymentResponse404
    | RestDeployment
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
    commit_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestDeploymentSetRequest | Unset = UNSET,
) -> Response[
    CreateOrUpdateDeploymentResponse400
    | CreateOrUpdateDeploymentResponse401
    | CreateOrUpdateDeploymentResponse404
    | RestDeployment
]:
    """Create or update a deployment

     Create or update a deployment.

     The authenticated user must have REPO_READ permission for the repository.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        body (RestDeploymentSetRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateOrUpdateDeploymentResponse400 | CreateOrUpdateDeploymentResponse401 | CreateOrUpdateDeploymentResponse404 | RestDeployment]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestDeploymentSetRequest | Unset = UNSET,
) -> (
    CreateOrUpdateDeploymentResponse400
    | CreateOrUpdateDeploymentResponse401
    | CreateOrUpdateDeploymentResponse404
    | RestDeployment
    | None
):
    """Create or update a deployment

     Create or update a deployment.

     The authenticated user must have REPO_READ permission for the repository.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        body (RestDeploymentSetRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateOrUpdateDeploymentResponse400 | CreateOrUpdateDeploymentResponse401 | CreateOrUpdateDeploymentResponse404 | RestDeployment
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestDeploymentSetRequest | Unset = UNSET,
) -> Response[
    CreateOrUpdateDeploymentResponse400
    | CreateOrUpdateDeploymentResponse401
    | CreateOrUpdateDeploymentResponse404
    | RestDeployment
]:
    """Create or update a deployment

     Create or update a deployment.

     The authenticated user must have REPO_READ permission for the repository.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        body (RestDeploymentSetRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateOrUpdateDeploymentResponse400 | CreateOrUpdateDeploymentResponse401 | CreateOrUpdateDeploymentResponse404 | RestDeployment]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestDeploymentSetRequest | Unset = UNSET,
) -> (
    CreateOrUpdateDeploymentResponse400
    | CreateOrUpdateDeploymentResponse401
    | CreateOrUpdateDeploymentResponse404
    | RestDeployment
    | None
):
    """Create or update a deployment

     Create or update a deployment.

     The authenticated user must have REPO_READ permission for the repository.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        body (RestDeploymentSetRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateOrUpdateDeploymentResponse400 | CreateOrUpdateDeploymentResponse401 | CreateOrUpdateDeploymentResponse404 | RestDeployment
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            commit_id=commit_id,
            client=client,
            body=body,
        )
    ).parsed
