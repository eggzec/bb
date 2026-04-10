from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_status_response_401 import GetStatusResponse401
from ...models.get_status_response_404 import GetStatusResponse404
from ...models.rest_ref_sync_status import RestRefSyncStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    *,
    at: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["at"] = at

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/sync/latest/projects/{project_key}/repos/{repository_slug}".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetStatusResponse401 | GetStatusResponse404 | RestRefSyncStatus | None:
    if response.status_code == 200:
        response_200 = RestRefSyncStatus.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetStatusResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetStatusResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetStatusResponse401 | GetStatusResponse404 | RestRefSyncStatus]:
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
    at: str | Unset = UNSET,
) -> Response[GetStatusResponse401 | GetStatusResponse404 | RestRefSyncStatus]:
    r"""Get synchronization status

     Retrieves the synchronization status for the specified repository. In addition to listing refs which
    cannot be synchronized, if any, the status also provides the timestamp for the most recent
    synchronization and indicates whether synchronization is available and enabled. If \"?at\" is
    specified in the URL, the synchronization status for the specified ref is returned, rather than the
    complete repository status.

    The authenticated user must have <b>REPO_READ</b> permission for the repository, or it must be
    public if the request is anonymous. Additionally, after synchronization is enabled for a repository,
    meaning synchronization was available at that time, permission changes and other actions can cause
    it to become unavailable. Even when synchronization is enabled, if it is no longer available for the
    repository it will not be performed.

    Args:
        project_key (str):
        repository_slug (str):
        at (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetStatusResponse401 | GetStatusResponse404 | RestRefSyncStatus]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        at=at,
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
    at: str | Unset = UNSET,
) -> GetStatusResponse401 | GetStatusResponse404 | RestRefSyncStatus | None:
    r"""Get synchronization status

     Retrieves the synchronization status for the specified repository. In addition to listing refs which
    cannot be synchronized, if any, the status also provides the timestamp for the most recent
    synchronization and indicates whether synchronization is available and enabled. If \"?at\" is
    specified in the URL, the synchronization status for the specified ref is returned, rather than the
    complete repository status.

    The authenticated user must have <b>REPO_READ</b> permission for the repository, or it must be
    public if the request is anonymous. Additionally, after synchronization is enabled for a repository,
    meaning synchronization was available at that time, permission changes and other actions can cause
    it to become unavailable. Even when synchronization is enabled, if it is no longer available for the
    repository it will not be performed.

    Args:
        project_key (str):
        repository_slug (str):
        at (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetStatusResponse401 | GetStatusResponse404 | RestRefSyncStatus
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        client=client,
        at=at,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    at: str | Unset = UNSET,
) -> Response[GetStatusResponse401 | GetStatusResponse404 | RestRefSyncStatus]:
    r"""Get synchronization status

     Retrieves the synchronization status for the specified repository. In addition to listing refs which
    cannot be synchronized, if any, the status also provides the timestamp for the most recent
    synchronization and indicates whether synchronization is available and enabled. If \"?at\" is
    specified in the URL, the synchronization status for the specified ref is returned, rather than the
    complete repository status.

    The authenticated user must have <b>REPO_READ</b> permission for the repository, or it must be
    public if the request is anonymous. Additionally, after synchronization is enabled for a repository,
    meaning synchronization was available at that time, permission changes and other actions can cause
    it to become unavailable. Even when synchronization is enabled, if it is no longer available for the
    repository it will not be performed.

    Args:
        project_key (str):
        repository_slug (str):
        at (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetStatusResponse401 | GetStatusResponse404 | RestRefSyncStatus]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        at=at,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    at: str | Unset = UNSET,
) -> GetStatusResponse401 | GetStatusResponse404 | RestRefSyncStatus | None:
    r"""Get synchronization status

     Retrieves the synchronization status for the specified repository. In addition to listing refs which
    cannot be synchronized, if any, the status also provides the timestamp for the most recent
    synchronization and indicates whether synchronization is available and enabled. If \"?at\" is
    specified in the URL, the synchronization status for the specified ref is returned, rather than the
    complete repository status.

    The authenticated user must have <b>REPO_READ</b> permission for the repository, or it must be
    public if the request is anonymous. Additionally, after synchronization is enabled for a repository,
    meaning synchronization was available at that time, permission changes and other actions can cause
    it to become unavailable. Even when synchronization is enabled, if it is no longer available for the
    repository it will not be performed.

    Args:
        project_key (str):
        repository_slug (str):
        at (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetStatusResponse401 | GetStatusResponse404 | RestRefSyncStatus
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            client=client,
            at=at,
        )
    ).parsed
