from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.find_by_commit_response_200 import FindByCommitResponse200
from ...models.find_by_commit_response_500 import FindByCommitResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    *,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["start"] = start

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/branch-utils/latest/projects/{project_key}/repos/{repository_slug}/branches/info/{commit_id}".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            commit_id=quote(str(commit_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FindByCommitResponse200 | FindByCommitResponse500 | None:
    if response.status_code == 200:
        response_200 = FindByCommitResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 500:
        response_500 = FindByCommitResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FindByCommitResponse200 | FindByCommitResponse500]:
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
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[FindByCommitResponse200 | FindByCommitResponse500]:
    """Get branch

     Gets the branch information associated with a single commit from a given repository.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FindByCommitResponse200 | FindByCommitResponse500]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        start=start,
        limit=limit,
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
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> FindByCommitResponse200 | FindByCommitResponse500 | None:
    """Get branch

     Gets the branch information associated with a single commit from a given repository.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FindByCommitResponse200 | FindByCommitResponse500
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        client=client,
        start=start,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    *,
    client: AuthenticatedClient | Client,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[FindByCommitResponse200 | FindByCommitResponse500]:
    """Get branch

     Gets the branch information associated with a single commit from a given repository.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FindByCommitResponse200 | FindByCommitResponse500]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        start=start,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    *,
    client: AuthenticatedClient | Client,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> FindByCommitResponse200 | FindByCommitResponse500 | None:
    """Get branch

     Gets the branch information associated with a single commit from a given repository.

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FindByCommitResponse200 | FindByCommitResponse500
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            commit_id=commit_id,
            client=client,
            start=start,
            limit=limit,
        )
    ).parsed
