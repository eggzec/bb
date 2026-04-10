from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_2_response_400 import Create2Response400
from ...models.create_2_response_401 import Create2Response401
from ...models.create_2_response_404 import Create2Response404
from ...models.create_2_response_409 import Create2Response409
from ...models.rest_reviewer_group import RestReviewerGroup
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    *,
    body: RestReviewerGroup | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/settings/reviewer-groups".format(
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
) -> Create2Response400 | Create2Response401 | Create2Response404 | Create2Response409 | RestReviewerGroup | None:
    if response.status_code == 201:
        response_201 = RestReviewerGroup.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = Create2Response400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Create2Response401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = Create2Response404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = Create2Response409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Create2Response400 | Create2Response401 | Create2Response404 | Create2Response409 | RestReviewerGroup]:
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
    body: RestReviewerGroup | Unset = UNSET,
) -> Response[Create2Response400 | Create2Response401 | Create2Response404 | Create2Response409 | RestReviewerGroup]:
    """Create reviewer group

     Create a reviewer group.

    The authenticated user must have <b>REPO_ADMIN</b> permission for the specified repository to call
    this resource.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestReviewerGroup | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Create2Response400 | Create2Response401 | Create2Response404 | Create2Response409 | RestReviewerGroup]
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
    body: RestReviewerGroup | Unset = UNSET,
) -> Create2Response400 | Create2Response401 | Create2Response404 | Create2Response409 | RestReviewerGroup | None:
    """Create reviewer group

     Create a reviewer group.

    The authenticated user must have <b>REPO_ADMIN</b> permission for the specified repository to call
    this resource.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestReviewerGroup | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Create2Response400 | Create2Response401 | Create2Response404 | Create2Response409 | RestReviewerGroup
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
    body: RestReviewerGroup | Unset = UNSET,
) -> Response[Create2Response400 | Create2Response401 | Create2Response404 | Create2Response409 | RestReviewerGroup]:
    """Create reviewer group

     Create a reviewer group.

    The authenticated user must have <b>REPO_ADMIN</b> permission for the specified repository to call
    this resource.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestReviewerGroup | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Create2Response400 | Create2Response401 | Create2Response404 | Create2Response409 | RestReviewerGroup]
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
    body: RestReviewerGroup | Unset = UNSET,
) -> Create2Response400 | Create2Response401 | Create2Response404 | Create2Response409 | RestReviewerGroup | None:
    """Create reviewer group

     Create a reviewer group.

    The authenticated user must have <b>REPO_ADMIN</b> permission for the specified repository to call
    this resource.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestReviewerGroup | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Create2Response400 | Create2Response401 | Create2Response404 | Create2Response409 | RestReviewerGroup
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            client=client,
            body=body,
        )
    ).parsed
