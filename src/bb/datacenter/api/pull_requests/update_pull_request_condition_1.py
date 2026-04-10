from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_pull_request_condition import RestPullRequestCondition
from ...models.update_pull_request_condition_1_body import UpdatePullRequestCondition1Body
from ...models.update_pull_request_condition_1_response_400 import UpdatePullRequestCondition1Response400
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    id: str,
    *,
    body: UpdatePullRequestCondition1Body | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/default-reviewers/latest/projects/{project_key}/repos/{repository_slug}/condition/{id}".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
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
) -> RestPullRequestCondition | UpdatePullRequestCondition1Response400 | None:
    if response.status_code == 200:
        response_200 = RestPullRequestCondition.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UpdatePullRequestCondition1Response400.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RestPullRequestCondition | UpdatePullRequestCondition1Response400]:
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
    body: UpdatePullRequestCondition1Body | Unset = UNSET,
) -> Response[RestPullRequestCondition | UpdatePullRequestCondition1Response400]:
    """Update default reviewer condition

     Update the default reviewer pull request condition for the given ID.

    Args:
        project_key (str):
        repository_slug (str):
        id (str):
        body (UpdatePullRequestCondition1Body | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestPullRequestCondition | UpdatePullRequestCondition1Response400]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        id=id,
        body=body,
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
    body: UpdatePullRequestCondition1Body | Unset = UNSET,
) -> RestPullRequestCondition | UpdatePullRequestCondition1Response400 | None:
    """Update default reviewer condition

     Update the default reviewer pull request condition for the given ID.

    Args:
        project_key (str):
        repository_slug (str):
        id (str):
        body (UpdatePullRequestCondition1Body | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestPullRequestCondition | UpdatePullRequestCondition1Response400
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdatePullRequestCondition1Body | Unset = UNSET,
) -> Response[RestPullRequestCondition | UpdatePullRequestCondition1Response400]:
    """Update default reviewer condition

     Update the default reviewer pull request condition for the given ID.

    Args:
        project_key (str):
        repository_slug (str):
        id (str):
        body (UpdatePullRequestCondition1Body | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestPullRequestCondition | UpdatePullRequestCondition1Response400]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdatePullRequestCondition1Body | Unset = UNSET,
) -> RestPullRequestCondition | UpdatePullRequestCondition1Response400 | None:
    """Update default reviewer condition

     Update the default reviewer pull request condition for the given ID.

    Args:
        project_key (str):
        repository_slug (str):
        id (str):
        body (UpdatePullRequestCondition1Body | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestPullRequestCondition | UpdatePullRequestCondition1Response400
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            id=id,
            client=client,
            body=body,
        )
    ).parsed
