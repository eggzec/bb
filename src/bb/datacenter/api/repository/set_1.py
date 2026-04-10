from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_auto_merge_restricted_settings import RestAutoMergeRestrictedSettings
from ...models.rest_auto_merge_settings_request import RestAutoMergeSettingsRequest
from ...models.set_1_response_400 import Set1Response400
from ...models.set_1_response_401 import Set1Response401
from ...models.set_1_response_403 import Set1Response403
from ...models.set_1_response_404 import Set1Response404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    *,
    body: RestAutoMergeSettingsRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/settings/auto-merge".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RestAutoMergeRestrictedSettings | Set1Response400 | Set1Response401 | Set1Response403 | Set1Response404 | None:
    if response.status_code == 200:
        response_200 = RestAutoMergeRestrictedSettings.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Set1Response400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Set1Response401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Set1Response403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Set1Response404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RestAutoMergeRestrictedSettings | Set1Response400 | Set1Response401 | Set1Response403 | Set1Response404]:
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
    body: RestAutoMergeSettingsRequest | Unset = UNSET,
) -> Response[RestAutoMergeRestrictedSettings | Set1Response400 | Set1Response401 | Set1Response403 | Set1Response404]:
    """Create or update the pull request auto-merge settings

     Creates or updates the pull request auto-merge settings for the supplied repository.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for this repository to call
    the resource.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestAutoMergeSettingsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestAutoMergeRestrictedSettings | Set1Response400 | Set1Response401 | Set1Response403 | Set1Response404]
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
    body: RestAutoMergeSettingsRequest | Unset = UNSET,
) -> RestAutoMergeRestrictedSettings | Set1Response400 | Set1Response401 | Set1Response403 | Set1Response404 | None:
    """Create or update the pull request auto-merge settings

     Creates or updates the pull request auto-merge settings for the supplied repository.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for this repository to call
    the resource.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestAutoMergeSettingsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestAutoMergeRestrictedSettings | Set1Response400 | Set1Response401 | Set1Response403 | Set1Response404
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
    body: RestAutoMergeSettingsRequest | Unset = UNSET,
) -> Response[RestAutoMergeRestrictedSettings | Set1Response400 | Set1Response401 | Set1Response403 | Set1Response404]:
    """Create or update the pull request auto-merge settings

     Creates or updates the pull request auto-merge settings for the supplied repository.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for this repository to call
    the resource.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestAutoMergeSettingsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestAutoMergeRestrictedSettings | Set1Response400 | Set1Response401 | Set1Response403 | Set1Response404]
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
    body: RestAutoMergeSettingsRequest | Unset = UNSET,
) -> RestAutoMergeRestrictedSettings | Set1Response400 | Set1Response401 | Set1Response403 | Set1Response404 | None:
    """Create or update the pull request auto-merge settings

     Creates or updates the pull request auto-merge settings for the supplied repository.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for this repository to call
    the resource.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestAutoMergeSettingsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestAutoMergeRestrictedSettings | Set1Response400 | Set1Response401 | Set1Response403 | Set1Response404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            client=client,
            body=body,
        )
    ).parsed
