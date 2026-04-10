from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_annotations_response_401 import GetAnnotationsResponse401
from ...models.get_annotations_response_404 import GetAnnotationsResponse404
from ...models.rest_insight_annotations_response import RestInsightAnnotationsResponse
from ...types import Response


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    key: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/insights/latest/projects/{project_key}/repos/{repository_slug}/commits/{commit_id}/reports/{key}/annotations".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            commit_id=quote(str(commit_id), safe=""),
            key=quote(str(key), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetAnnotationsResponse401 | GetAnnotationsResponse404 | RestInsightAnnotationsResponse | None:
    if response.status_code == 200:
        response_200 = RestInsightAnnotationsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetAnnotationsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetAnnotationsResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetAnnotationsResponse401 | GetAnnotationsResponse404 | RestInsightAnnotationsResponse]:
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
) -> Response[GetAnnotationsResponse401 | GetAnnotationsResponse404 | RestInsightAnnotationsResponse]:
    """Get Code Insights annotations for a report

     Retrieve the specified report's annotations.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAnnotationsResponse401 | GetAnnotationsResponse404 | RestInsightAnnotationsResponse]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
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
    key: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetAnnotationsResponse401 | GetAnnotationsResponse404 | RestInsightAnnotationsResponse | None:
    """Get Code Insights annotations for a report

     Retrieve the specified report's annotations.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAnnotationsResponse401 | GetAnnotationsResponse404 | RestInsightAnnotationsResponse
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        key=key,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    key: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetAnnotationsResponse401 | GetAnnotationsResponse404 | RestInsightAnnotationsResponse]:
    """Get Code Insights annotations for a report

     Retrieve the specified report's annotations.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAnnotationsResponse401 | GetAnnotationsResponse404 | RestInsightAnnotationsResponse]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        key=key,
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
) -> GetAnnotationsResponse401 | GetAnnotationsResponse404 | RestInsightAnnotationsResponse | None:
    """Get Code Insights annotations for a report

     Retrieve the specified report's annotations.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAnnotationsResponse401 | GetAnnotationsResponse404 | RestInsightAnnotationsResponse
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            commit_id=commit_id,
            key=key,
            client=client,
        )
    ).parsed
