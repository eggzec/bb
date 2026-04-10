from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_restriction_1_response_400 import GetRestriction1Response400
from ...models.get_restriction_1_response_401 import GetRestriction1Response401
from ...models.get_restriction_1_response_404 import GetRestriction1Response404
from ...models.rest_ref_restriction import RestRefRestriction
from ...types import Response


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/branch-permissions/latest/projects/{project_key}/repos/{repository_slug}/restrictions/{id}".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetRestriction1Response400 | GetRestriction1Response401 | GetRestriction1Response404 | RestRefRestriction | None:
    if response.status_code == 200:
        response_200 = RestRefRestriction.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetRestriction1Response400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetRestriction1Response401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetRestriction1Response404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetRestriction1Response400 | GetRestriction1Response401 | GetRestriction1Response404 | RestRefRestriction
]:
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
) -> Response[
    GetRestriction1Response400 | GetRestriction1Response401 | GetRestriction1Response404 | RestRefRestriction
]:
    """Get a ref restriction

     Returns a restriction as specified by a restriction id.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission or higher to call this
    resource. Only authenticated users may call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRestriction1Response400 | GetRestriction1Response401 | GetRestriction1Response404 | RestRefRestriction]
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
) -> GetRestriction1Response400 | GetRestriction1Response401 | GetRestriction1Response404 | RestRefRestriction | None:
    """Get a ref restriction

     Returns a restriction as specified by a restriction id.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission or higher to call this
    resource. Only authenticated users may call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRestriction1Response400 | GetRestriction1Response401 | GetRestriction1Response404 | RestRefRestriction
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
) -> Response[
    GetRestriction1Response400 | GetRestriction1Response401 | GetRestriction1Response404 | RestRefRestriction
]:
    """Get a ref restriction

     Returns a restriction as specified by a restriction id.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission or higher to call this
    resource. Only authenticated users may call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRestriction1Response400 | GetRestriction1Response401 | GetRestriction1Response404 | RestRefRestriction]
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
) -> GetRestriction1Response400 | GetRestriction1Response401 | GetRestriction1Response404 | RestRefRestriction | None:
    """Get a ref restriction

     Returns a restriction as specified by a restriction id.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission or higher to call this
    resource. Only authenticated users may call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRestriction1Response400 | GetRestriction1Response401 | GetRestriction1Response404 | RestRefRestriction
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            id=id,
            client=client,
        )
    ).parsed
