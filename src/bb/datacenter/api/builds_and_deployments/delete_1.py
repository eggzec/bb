from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_1_response_400 import Delete1Response400
from ...models.delete_1_response_401 import Delete1Response401
from ...models.delete_1_response_404 import Delete1Response404
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
        "method": "delete",
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
) -> Any | Delete1Response400 | Delete1Response401 | Delete1Response404 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = Delete1Response400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Delete1Response401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = Delete1Response404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | Delete1Response400 | Delete1Response401 | Delete1Response404]:
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
) -> Response[Any | Delete1Response400 | Delete1Response401 | Delete1Response404]:
    """Delete a deployment

     Delete the deployment matching the specified Repository, key, environmentKey and
    deploymentSequenceNumber.

    The user must have REPO_ADMIN.

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
        Response[Any | Delete1Response400 | Delete1Response401 | Delete1Response404]
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
) -> Any | Delete1Response400 | Delete1Response401 | Delete1Response404 | None:
    """Delete a deployment

     Delete the deployment matching the specified Repository, key, environmentKey and
    deploymentSequenceNumber.

    The user must have REPO_ADMIN.

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
        Any | Delete1Response400 | Delete1Response401 | Delete1Response404
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
) -> Response[Any | Delete1Response400 | Delete1Response401 | Delete1Response404]:
    """Delete a deployment

     Delete the deployment matching the specified Repository, key, environmentKey and
    deploymentSequenceNumber.

    The user must have REPO_ADMIN.

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
        Response[Any | Delete1Response400 | Delete1Response401 | Delete1Response404]
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
) -> Any | Delete1Response400 | Delete1Response401 | Delete1Response404 | None:
    """Delete a deployment

     Delete the deployment matching the specified Repository, key, environmentKey and
    deploymentSequenceNumber.

    The user must have REPO_ADMIN.

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
        Any | Delete1Response400 | Delete1Response401 | Delete1Response404
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
