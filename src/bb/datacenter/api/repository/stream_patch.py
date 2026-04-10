from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.stream_patch_response_400 import StreamPatchResponse400
from ...models.stream_patch_response_401 import StreamPatchResponse401
from ...models.stream_patch_response_404 import StreamPatchResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    *,
    until: str | Unset = UNSET,
    all_ancestors: str | Unset = UNSET,
    since: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["until"] = until

    params["allAncestors"] = all_ancestors

    params["since"] = since

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/patch".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | StreamPatchResponse400 | StreamPatchResponse401 | StreamPatchResponse404 | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 400:
        response_400 = StreamPatchResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = StreamPatchResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = StreamPatchResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | StreamPatchResponse400 | StreamPatchResponse401 | StreamPatchResponse404]:
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
    until: str | Unset = UNSET,
    all_ancestors: str | Unset = UNSET,
    since: str | Unset = UNSET,
) -> Response[Any | StreamPatchResponse400 | StreamPatchResponse401 | StreamPatchResponse404]:
    """Get patch content at revision

     Retrieve the patch content for a repository at a specified revision.

    Cache headers are added to the response (only if full commit hashes are used, not in the case of
    short hashes).

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        until (str | Unset):
        all_ancestors (str | Unset):
        since (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | StreamPatchResponse400 | StreamPatchResponse401 | StreamPatchResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        until=until,
        all_ancestors=all_ancestors,
        since=since,
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
    until: str | Unset = UNSET,
    all_ancestors: str | Unset = UNSET,
    since: str | Unset = UNSET,
) -> Any | StreamPatchResponse400 | StreamPatchResponse401 | StreamPatchResponse404 | None:
    """Get patch content at revision

     Retrieve the patch content for a repository at a specified revision.

    Cache headers are added to the response (only if full commit hashes are used, not in the case of
    short hashes).

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        until (str | Unset):
        all_ancestors (str | Unset):
        since (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | StreamPatchResponse400 | StreamPatchResponse401 | StreamPatchResponse404
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        client=client,
        until=until,
        all_ancestors=all_ancestors,
        since=since,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    until: str | Unset = UNSET,
    all_ancestors: str | Unset = UNSET,
    since: str | Unset = UNSET,
) -> Response[Any | StreamPatchResponse400 | StreamPatchResponse401 | StreamPatchResponse404]:
    """Get patch content at revision

     Retrieve the patch content for a repository at a specified revision.

    Cache headers are added to the response (only if full commit hashes are used, not in the case of
    short hashes).

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        until (str | Unset):
        all_ancestors (str | Unset):
        since (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | StreamPatchResponse400 | StreamPatchResponse401 | StreamPatchResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        until=until,
        all_ancestors=all_ancestors,
        since=since,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    until: str | Unset = UNSET,
    all_ancestors: str | Unset = UNSET,
    since: str | Unset = UNSET,
) -> Any | StreamPatchResponse400 | StreamPatchResponse401 | StreamPatchResponse404 | None:
    """Get patch content at revision

     Retrieve the patch content for a repository at a specified revision.

    Cache headers are added to the response (only if full commit hashes are used, not in the case of
    short hashes).

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        until (str | Unset):
        all_ancestors (str | Unset):
        since (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | StreamPatchResponse400 | StreamPatchResponse401 | StreamPatchResponse404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            client=client,
            until=until,
            all_ancestors=all_ancestors,
            since=since,
        )
    ).parsed
