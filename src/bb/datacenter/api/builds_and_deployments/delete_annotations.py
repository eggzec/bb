from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_annotations_response_401 import DeleteAnnotationsResponse401
from ...models.delete_annotations_response_404 import DeleteAnnotationsResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    key: str,
    *,
    external_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["externalId"] = external_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/insights/latest/projects/{project_key}/repos/{repository_slug}/commits/{commit_id}/reports/{key}/annotations".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            commit_id=quote(str(commit_id), safe=""),
            key=quote(str(key), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteAnnotationsResponse401 | DeleteAnnotationsResponse404 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = DeleteAnnotationsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = DeleteAnnotationsResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteAnnotationsResponse401 | DeleteAnnotationsResponse404]:
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
    key: str,
    *,
    client: AuthenticatedClient | Client,
    external_id: str | Unset = UNSET,
) -> Response[Any | DeleteAnnotationsResponse401 | DeleteAnnotationsResponse404]:
    """Delete Code Insights annotations

     Delete annotations for a given report that match the given external IDs, or all annotations if no
    external IDs are provided.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        key (str):
        external_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAnnotationsResponse401 | DeleteAnnotationsResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        key=key,
        external_id=external_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    key: str,
    *,
    client: AuthenticatedClient | Client,
    external_id: str | Unset = UNSET,
) -> Any | DeleteAnnotationsResponse401 | DeleteAnnotationsResponse404 | None:
    """Delete Code Insights annotations

     Delete annotations for a given report that match the given external IDs, or all annotations if no
    external IDs are provided.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        key (str):
        external_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAnnotationsResponse401 | DeleteAnnotationsResponse404
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        key=key,
        client=client,
        external_id=external_id,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    key: str,
    *,
    client: AuthenticatedClient | Client,
    external_id: str | Unset = UNSET,
) -> Response[Any | DeleteAnnotationsResponse401 | DeleteAnnotationsResponse404]:
    """Delete Code Insights annotations

     Delete annotations for a given report that match the given external IDs, or all annotations if no
    external IDs are provided.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        key (str):
        external_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAnnotationsResponse401 | DeleteAnnotationsResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        key=key,
        external_id=external_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    key: str,
    *,
    client: AuthenticatedClient | Client,
    external_id: str | Unset = UNSET,
) -> Any | DeleteAnnotationsResponse401 | DeleteAnnotationsResponse404 | None:
    """Delete Code Insights annotations

     Delete annotations for a given report that match the given external IDs, or all annotations if no
    external IDs are provided.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        key (str):
        external_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAnnotationsResponse401 | DeleteAnnotationsResponse404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            commit_id=commit_id,
            key=key,
            client=client,
            external_id=external_id,
        )
    ).parsed
