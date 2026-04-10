from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_annotations_1_response_401 import GetAnnotations1Response401
from ...models.get_annotations_1_response_404 import GetAnnotations1Response404
from ...models.rest_insight_annotations_response import RestInsightAnnotationsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    *,
    severity: str | Unset = UNSET,
    path: str | Unset = UNSET,
    external_id: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    key: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["severity"] = severity

    params["path"] = path

    params["externalId"] = external_id

    params["type"] = type_

    params["key"] = key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/insights/latest/projects/{project_key}/repos/{repository_slug}/commits/{commit_id}/annotations".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            commit_id=quote(str(commit_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetAnnotations1Response401 | GetAnnotations1Response404 | RestInsightAnnotationsResponse | None:
    if response.status_code == 200:
        response_200 = RestInsightAnnotationsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetAnnotations1Response401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetAnnotations1Response404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetAnnotations1Response401 | GetAnnotations1Response404 | RestInsightAnnotationsResponse]:
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
    severity: str | Unset = UNSET,
    path: str | Unset = UNSET,
    external_id: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    key: str | Unset = UNSET,
) -> Response[GetAnnotations1Response401 | GetAnnotations1Response404 | RestInsightAnnotationsResponse]:
    """Get Code Insights annotations for a commit

     Get annotations for the given commit ID, filtered by any query parameters given.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        severity (str | Unset):
        path (str | Unset):
        external_id (str | Unset):
        type_ (str | Unset):
        key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAnnotations1Response401 | GetAnnotations1Response404 | RestInsightAnnotationsResponse]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        severity=severity,
        path=path,
        external_id=external_id,
        type_=type_,
        key=key,
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
    severity: str | Unset = UNSET,
    path: str | Unset = UNSET,
    external_id: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    key: str | Unset = UNSET,
) -> GetAnnotations1Response401 | GetAnnotations1Response404 | RestInsightAnnotationsResponse | None:
    """Get Code Insights annotations for a commit

     Get annotations for the given commit ID, filtered by any query parameters given.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        severity (str | Unset):
        path (str | Unset):
        external_id (str | Unset):
        type_ (str | Unset):
        key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAnnotations1Response401 | GetAnnotations1Response404 | RestInsightAnnotationsResponse
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        client=client,
        severity=severity,
        path=path,
        external_id=external_id,
        type_=type_,
        key=key,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    *,
    client: AuthenticatedClient | Client,
    severity: str | Unset = UNSET,
    path: str | Unset = UNSET,
    external_id: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    key: str | Unset = UNSET,
) -> Response[GetAnnotations1Response401 | GetAnnotations1Response404 | RestInsightAnnotationsResponse]:
    """Get Code Insights annotations for a commit

     Get annotations for the given commit ID, filtered by any query parameters given.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        severity (str | Unset):
        path (str | Unset):
        external_id (str | Unset):
        type_ (str | Unset):
        key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAnnotations1Response401 | GetAnnotations1Response404 | RestInsightAnnotationsResponse]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        severity=severity,
        path=path,
        external_id=external_id,
        type_=type_,
        key=key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    *,
    client: AuthenticatedClient | Client,
    severity: str | Unset = UNSET,
    path: str | Unset = UNSET,
    external_id: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    key: str | Unset = UNSET,
) -> GetAnnotations1Response401 | GetAnnotations1Response404 | RestInsightAnnotationsResponse | None:
    """Get Code Insights annotations for a commit

     Get annotations for the given commit ID, filtered by any query parameters given.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        severity (str | Unset):
        path (str | Unset):
        external_id (str | Unset):
        type_ (str | Unset):
        key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAnnotations1Response401 | GetAnnotations1Response404 | RestInsightAnnotationsResponse
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            commit_id=commit_id,
            client=client,
            severity=severity,
            path=path,
            external_id=external_id,
            type_=type_,
            key=key,
        )
    ).parsed
