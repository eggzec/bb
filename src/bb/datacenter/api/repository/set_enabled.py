from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_ref_sync_status import RestRefSyncStatus
from ...models.set_enabled_response_400 import SetEnabledResponse400
from ...models.set_enabled_response_401 import SetEnabledResponse401
from ...models.set_enabled_response_404 import SetEnabledResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    *,
    body: RestRefSyncStatus | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/sync/latest/projects/{project_key}/repos/{repository_slug}".format(
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
) -> Any | RestRefSyncStatus | SetEnabledResponse400 | SetEnabledResponse401 | SetEnabledResponse404 | None:
    if response.status_code == 200:
        response_200 = RestRefSyncStatus.from_dict(response.json())

        return response_200

    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = SetEnabledResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = SetEnabledResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = SetEnabledResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RestRefSyncStatus | SetEnabledResponse400 | SetEnabledResponse401 | SetEnabledResponse404]:
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
    body: RestRefSyncStatus | Unset = UNSET,
) -> Response[Any | RestRefSyncStatus | SetEnabledResponse400 | SetEnabledResponse401 | SetEnabledResponse404]:
    """Disable synchronization

     Enables or disables synchronization for the specified repository. When synchronization is enabled,
    branches within the repository are immediately synchronized and the status is updated with the
    outcome. That initial synchronization is performed before the REST request returns, allowing it to
    return the updated status.

    The authenticated user must have <b>REPO_ADMIN</b> permission for the specified repository.
    Anonymous users cannot manage synchronization, even on public repositories. Additionally,
    synchronization must be available for the specified repository. Synchronization is only available
    if:

    - The repository is a fork, since its origin is used as upstream
    - The owning user still has access to the fork's origin,  if the repository is a <i>personalfork</i>

    Args:
        project_key (str):
        repository_slug (str):
        body (RestRefSyncStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RestRefSyncStatus | SetEnabledResponse400 | SetEnabledResponse401 | SetEnabledResponse404]
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
    body: RestRefSyncStatus | Unset = UNSET,
) -> Any | RestRefSyncStatus | SetEnabledResponse400 | SetEnabledResponse401 | SetEnabledResponse404 | None:
    """Disable synchronization

     Enables or disables synchronization for the specified repository. When synchronization is enabled,
    branches within the repository are immediately synchronized and the status is updated with the
    outcome. That initial synchronization is performed before the REST request returns, allowing it to
    return the updated status.

    The authenticated user must have <b>REPO_ADMIN</b> permission for the specified repository.
    Anonymous users cannot manage synchronization, even on public repositories. Additionally,
    synchronization must be available for the specified repository. Synchronization is only available
    if:

    - The repository is a fork, since its origin is used as upstream
    - The owning user still has access to the fork's origin,  if the repository is a <i>personalfork</i>

    Args:
        project_key (str):
        repository_slug (str):
        body (RestRefSyncStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RestRefSyncStatus | SetEnabledResponse400 | SetEnabledResponse401 | SetEnabledResponse404
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
    body: RestRefSyncStatus | Unset = UNSET,
) -> Response[Any | RestRefSyncStatus | SetEnabledResponse400 | SetEnabledResponse401 | SetEnabledResponse404]:
    """Disable synchronization

     Enables or disables synchronization for the specified repository. When synchronization is enabled,
    branches within the repository are immediately synchronized and the status is updated with the
    outcome. That initial synchronization is performed before the REST request returns, allowing it to
    return the updated status.

    The authenticated user must have <b>REPO_ADMIN</b> permission for the specified repository.
    Anonymous users cannot manage synchronization, even on public repositories. Additionally,
    synchronization must be available for the specified repository. Synchronization is only available
    if:

    - The repository is a fork, since its origin is used as upstream
    - The owning user still has access to the fork's origin,  if the repository is a <i>personalfork</i>

    Args:
        project_key (str):
        repository_slug (str):
        body (RestRefSyncStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RestRefSyncStatus | SetEnabledResponse400 | SetEnabledResponse401 | SetEnabledResponse404]
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
    body: RestRefSyncStatus | Unset = UNSET,
) -> Any | RestRefSyncStatus | SetEnabledResponse400 | SetEnabledResponse401 | SetEnabledResponse404 | None:
    """Disable synchronization

     Enables or disables synchronization for the specified repository. When synchronization is enabled,
    branches within the repository are immediately synchronized and the status is updated with the
    outcome. That initial synchronization is performed before the REST request returns, allowing it to
    return the updated status.

    The authenticated user must have <b>REPO_ADMIN</b> permission for the specified repository.
    Anonymous users cannot manage synchronization, even on public repositories. Additionally,
    synchronization must be available for the specified repository. Synchronization is only available
    if:

    - The repository is a fork, since its origin is used as upstream
    - The owning user still has access to the fork's origin,  if the repository is a <i>personalfork</i>

    Args:
        project_key (str):
        repository_slug (str):
        body (RestRefSyncStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RestRefSyncStatus | SetEnabledResponse400 | SetEnabledResponse401 | SetEnabledResponse404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            client=client,
            body=body,
        )
    ).parsed
