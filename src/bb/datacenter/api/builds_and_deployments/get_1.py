from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_1_response_400 import Get1Response400
from ...models.get_1_response_401 import Get1Response401
from ...models.get_1_response_404 import Get1Response404
from ...models.rest_deployment import RestDeployment
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    *,
    deployment_sequence_number: str | Unset = UNSET,
    key: str | Unset = UNSET,
    environment_key: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["deploymentSequenceNumber"] = deployment_sequence_number

    params["key"] = key

    params["environmentKey"] = environment_key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/commits/{commit_id}/deployments".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            commit_id=quote(str(commit_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Get1Response400 | Get1Response401 | Get1Response404 | RestDeployment | None:
    if response.status_code == 200:
        response_200 = RestDeployment.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Get1Response400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Get1Response401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = Get1Response404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Get1Response400 | Get1Response401 | Get1Response404 | RestDeployment]:
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
    deployment_sequence_number: str | Unset = UNSET,
    key: str | Unset = UNSET,
    environment_key: str | Unset = UNSET,
) -> Response[Get1Response400 | Get1Response401 | Get1Response404 | RestDeployment]:
    """Get a deployment

     Get the deployment matching the specified Repository, key, environmentKey and
    deploymentSequenceNumber.

    The user must have REPO_READ.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        deployment_sequence_number (str | Unset):
        key (str | Unset):
        environment_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Get1Response400 | Get1Response401 | Get1Response404 | RestDeployment]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        deployment_sequence_number=deployment_sequence_number,
        key=key,
        environment_key=environment_key,
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
    deployment_sequence_number: str | Unset = UNSET,
    key: str | Unset = UNSET,
    environment_key: str | Unset = UNSET,
) -> Get1Response400 | Get1Response401 | Get1Response404 | RestDeployment | None:
    """Get a deployment

     Get the deployment matching the specified Repository, key, environmentKey and
    deploymentSequenceNumber.

    The user must have REPO_READ.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        deployment_sequence_number (str | Unset):
        key (str | Unset):
        environment_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Get1Response400 | Get1Response401 | Get1Response404 | RestDeployment
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        client=client,
        deployment_sequence_number=deployment_sequence_number,
        key=key,
        environment_key=environment_key,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    *,
    client: AuthenticatedClient | Client,
    deployment_sequence_number: str | Unset = UNSET,
    key: str | Unset = UNSET,
    environment_key: str | Unset = UNSET,
) -> Response[Get1Response400 | Get1Response401 | Get1Response404 | RestDeployment]:
    """Get a deployment

     Get the deployment matching the specified Repository, key, environmentKey and
    deploymentSequenceNumber.

    The user must have REPO_READ.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        deployment_sequence_number (str | Unset):
        key (str | Unset):
        environment_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Get1Response400 | Get1Response401 | Get1Response404 | RestDeployment]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        deployment_sequence_number=deployment_sequence_number,
        key=key,
        environment_key=environment_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    *,
    client: AuthenticatedClient | Client,
    deployment_sequence_number: str | Unset = UNSET,
    key: str | Unset = UNSET,
    environment_key: str | Unset = UNSET,
) -> Get1Response400 | Get1Response401 | Get1Response404 | RestDeployment | None:
    """Get a deployment

     Get the deployment matching the specified Repository, key, environmentKey and
    deploymentSequenceNumber.

    The user must have REPO_READ.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        deployment_sequence_number (str | Unset):
        key (str | Unset):
        environment_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Get1Response400 | Get1Response401 | Get1Response404 | RestDeployment
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            commit_id=commit_id,
            client=client,
            deployment_sequence_number=deployment_sequence_number,
            key=key,
            environment_key=environment_key,
        )
    ).parsed
