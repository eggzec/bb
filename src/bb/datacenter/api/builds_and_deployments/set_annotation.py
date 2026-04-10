from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_single_add_insight_annotation_request import RestSingleAddInsightAnnotationRequest
from ...models.set_annotation_response_401 import SetAnnotationResponse401
from ...models.set_annotation_response_404 import SetAnnotationResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    key: str,
    external_id: str,
    *,
    body: RestSingleAddInsightAnnotationRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/insights/latest/projects/{project_key}/repos/{repository_slug}/commits/{commit_id}/reports/{key}/annotations/{external_id}".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            commit_id=quote(str(commit_id), safe=""),
            key=quote(str(key), safe=""),
            external_id=quote(str(external_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | SetAnnotationResponse401 | SetAnnotationResponse404 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = SetAnnotationResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = SetAnnotationResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | SetAnnotationResponse401 | SetAnnotationResponse404]:
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
    external_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestSingleAddInsightAnnotationRequest | Unset = UNSET,
) -> Response[Any | SetAnnotationResponse401 | SetAnnotationResponse404]:
    """Create or replace a Code Insights annotation

     Create an annotation with the given external ID, or replace it if it already exists. A request to
    replace an existing annotation will be rejected if the authenticated user was not the creator of the
    specified report.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        key (str):
        external_id (str):
        body (RestSingleAddInsightAnnotationRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SetAnnotationResponse401 | SetAnnotationResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        key=key,
        external_id=external_id,
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
    key: str,
    external_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestSingleAddInsightAnnotationRequest | Unset = UNSET,
) -> Any | SetAnnotationResponse401 | SetAnnotationResponse404 | None:
    """Create or replace a Code Insights annotation

     Create an annotation with the given external ID, or replace it if it already exists. A request to
    replace an existing annotation will be rejected if the authenticated user was not the creator of the
    specified report.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        key (str):
        external_id (str):
        body (RestSingleAddInsightAnnotationRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SetAnnotationResponse401 | SetAnnotationResponse404
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        key=key,
        external_id=external_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    key: str,
    external_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestSingleAddInsightAnnotationRequest | Unset = UNSET,
) -> Response[Any | SetAnnotationResponse401 | SetAnnotationResponse404]:
    """Create or replace a Code Insights annotation

     Create an annotation with the given external ID, or replace it if it already exists. A request to
    replace an existing annotation will be rejected if the authenticated user was not the creator of the
    specified report.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        key (str):
        external_id (str):
        body (RestSingleAddInsightAnnotationRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SetAnnotationResponse401 | SetAnnotationResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        key=key,
        external_id=external_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    key: str,
    external_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestSingleAddInsightAnnotationRequest | Unset = UNSET,
) -> Any | SetAnnotationResponse401 | SetAnnotationResponse404 | None:
    """Create or replace a Code Insights annotation

     Create an annotation with the given external ID, or replace it if it already exists. A request to
    replace an existing annotation will be rejected if the authenticated user was not the creator of the
    specified report.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        key (str):
        external_id (str):
        body (RestSingleAddInsightAnnotationRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SetAnnotationResponse401 | SetAnnotationResponse404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            commit_id=commit_id,
            key=key,
            external_id=external_id,
            client=client,
            body=body,
        )
    ).parsed
