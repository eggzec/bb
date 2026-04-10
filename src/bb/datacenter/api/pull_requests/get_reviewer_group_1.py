from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_reviewer_group_1_response_401 import GetReviewerGroup1Response401
from ...models.get_reviewer_group_1_response_404 import GetReviewerGroup1Response404
from ...models.rest_reviewer_group import RestReviewerGroup
from ...types import Response


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/settings/reviewer-groups/{id}".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetReviewerGroup1Response401 | GetReviewerGroup1Response404 | RestReviewerGroup | None:
    if response.status_code == 200:
        response_200 = RestReviewerGroup.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetReviewerGroup1Response401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetReviewerGroup1Response404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetReviewerGroup1Response401 | GetReviewerGroup1Response404 | RestReviewerGroup]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    repository_slug: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetReviewerGroup1Response401 | GetReviewerGroup1Response404 | RestReviewerGroup]:
    """Get reviewer group

     Retrieve a reviewer group.

    The authenticated user must have <b>REPO_READ</b> permission for the specified repository to call
    this resource.

    Args:
        project_key (str):
        repository_slug (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetReviewerGroup1Response401 | GetReviewerGroup1Response404 | RestReviewerGroup]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    repository_slug: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetReviewerGroup1Response401 | GetReviewerGroup1Response404 | RestReviewerGroup | None:
    """Get reviewer group

     Retrieve a reviewer group.

    The authenticated user must have <b>REPO_READ</b> permission for the specified repository to call
    this resource.

    Args:
        project_key (str):
        repository_slug (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetReviewerGroup1Response401 | GetReviewerGroup1Response404 | RestReviewerGroup
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetReviewerGroup1Response401 | GetReviewerGroup1Response404 | RestReviewerGroup]:
    """Get reviewer group

     Retrieve a reviewer group.

    The authenticated user must have <b>REPO_READ</b> permission for the specified repository to call
    this resource.

    Args:
        project_key (str):
        repository_slug (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetReviewerGroup1Response401 | GetReviewerGroup1Response404 | RestReviewerGroup]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetReviewerGroup1Response401 | GetReviewerGroup1Response404 | RestReviewerGroup | None:
    """Get reviewer group

     Retrieve a reviewer group.

    The authenticated user must have <b>REPO_READ</b> permission for the specified repository to call
    this resource.

    Args:
        project_key (str):
        repository_slug (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetReviewerGroup1Response401 | GetReviewerGroup1Response404 | RestReviewerGroup
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            id=id,
            client=client,
        )
    ).parsed
