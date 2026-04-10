from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_reviewer_group import RestReviewerGroup
from ...models.update_1_response_400 import Update1Response400
from ...models.update_1_response_401 import Update1Response401
from ...models.update_1_response_404 import Update1Response404
from ...models.update_1_response_409 import Update1Response409
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    id: str,
    *,
    body: RestReviewerGroup | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/latest/projects/{project_key}/settings/reviewer-groups/{id}".format(
            project_key=quote(str(project_key), safe=""),
            id=quote(str(id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RestReviewerGroup | Update1Response400 | Update1Response401 | Update1Response404 | Update1Response409 | None:
    if response.status_code == 200:
        response_200 = RestReviewerGroup.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Update1Response400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Update1Response401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = Update1Response404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = Update1Response409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RestReviewerGroup | Update1Response400 | Update1Response401 | Update1Response404 | Update1Response409]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestReviewerGroup | Unset = UNSET,
) -> Response[RestReviewerGroup | Update1Response400 | Update1Response401 | Update1Response404 | Update1Response409]:
    """Update reviewer group attributes

     Update the attributes of a reviewer group.

    The authenticated user must have <b>PROJECT_READ</b> permission for the specified project to call
    this resource.

    Args:
        project_key (str):
        id (str):
        body (RestReviewerGroup | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestReviewerGroup | Update1Response400 | Update1Response401 | Update1Response404 | Update1Response409]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestReviewerGroup | Unset = UNSET,
) -> RestReviewerGroup | Update1Response400 | Update1Response401 | Update1Response404 | Update1Response409 | None:
    """Update reviewer group attributes

     Update the attributes of a reviewer group.

    The authenticated user must have <b>PROJECT_READ</b> permission for the specified project to call
    this resource.

    Args:
        project_key (str):
        id (str):
        body (RestReviewerGroup | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestReviewerGroup | Update1Response400 | Update1Response401 | Update1Response404 | Update1Response409
    """

    return sync_detailed(
        project_key=project_key,
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestReviewerGroup | Unset = UNSET,
) -> Response[RestReviewerGroup | Update1Response400 | Update1Response401 | Update1Response404 | Update1Response409]:
    """Update reviewer group attributes

     Update the attributes of a reviewer group.

    The authenticated user must have <b>PROJECT_READ</b> permission for the specified project to call
    this resource.

    Args:
        project_key (str):
        id (str):
        body (RestReviewerGroup | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestReviewerGroup | Update1Response400 | Update1Response401 | Update1Response404 | Update1Response409]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestReviewerGroup | Unset = UNSET,
) -> RestReviewerGroup | Update1Response400 | Update1Response401 | Update1Response404 | Update1Response409 | None:
    """Update reviewer group attributes

     Update the attributes of a reviewer group.

    The authenticated user must have <b>PROJECT_READ</b> permission for the specified project to call
    this resource.

    Args:
        project_key (str):
        id (str):
        body (RestReviewerGroup | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestReviewerGroup | Update1Response400 | Update1Response401 | Update1Response404 | Update1Response409
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            id=id,
            client=client,
            body=body,
        )
    ).parsed
