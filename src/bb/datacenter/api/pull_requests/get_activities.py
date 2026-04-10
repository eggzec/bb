from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_activities_response_200 import GetActivitiesResponse200
from ...models.get_activities_response_400 import GetActivitiesResponse400
from ...models.get_activities_response_401 import GetActivitiesResponse401
from ...models.get_activities_response_404 import GetActivitiesResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    *,
    from_type: str | Unset = UNSET,
    from_id: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["fromType"] = from_type

    params["fromId"] = from_id

    params["start"] = start

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/pull-requests/{pull_request_id}/activities".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            pull_request_id=quote(str(pull_request_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetActivitiesResponse200 | GetActivitiesResponse400 | GetActivitiesResponse401 | GetActivitiesResponse404 | None:
    if response.status_code == 200:
        response_200 = GetActivitiesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetActivitiesResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetActivitiesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetActivitiesResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetActivitiesResponse200 | GetActivitiesResponse400 | GetActivitiesResponse401 | GetActivitiesResponse404
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
    pull_request_id: str,
    *,
    client: AuthenticatedClient | Client,
    from_type: str | Unset = UNSET,
    from_id: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[
    GetActivitiesResponse200 | GetActivitiesResponse400 | GetActivitiesResponse401 | GetActivitiesResponse404
]:
    """Get pull request activity

     Retrieve a page of activity associated with a pull request.

    Activity items include comments, approvals, rescopes (i.e. adding and removing of commits), merges
    and more.

    Different types of activity items may be introduced in newer versions of Stash or by user installed
    plugins, so clients should be flexible enough to handle unexpected entity shapes in the returned
    page.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        from_type (str | Unset):
        from_id (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetActivitiesResponse200 | GetActivitiesResponse400 | GetActivitiesResponse401 | GetActivitiesResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
        from_type=from_type,
        from_id=from_id,
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
    pull_request_id: str,
    *,
    client: AuthenticatedClient | Client,
    from_type: str | Unset = UNSET,
    from_id: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetActivitiesResponse200 | GetActivitiesResponse400 | GetActivitiesResponse401 | GetActivitiesResponse404 | None:
    """Get pull request activity

     Retrieve a page of activity associated with a pull request.

    Activity items include comments, approvals, rescopes (i.e. adding and removing of commits), merges
    and more.

    Different types of activity items may be introduced in newer versions of Stash or by user installed
    plugins, so clients should be flexible enough to handle unexpected entity shapes in the returned
    page.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        from_type (str | Unset):
        from_id (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetActivitiesResponse200 | GetActivitiesResponse400 | GetActivitiesResponse401 | GetActivitiesResponse404
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
        client=client,
        from_type=from_type,
        from_id=from_id,
        start=start,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    *,
    client: AuthenticatedClient | Client,
    from_type: str | Unset = UNSET,
    from_id: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[
    GetActivitiesResponse200 | GetActivitiesResponse400 | GetActivitiesResponse401 | GetActivitiesResponse404
]:
    """Get pull request activity

     Retrieve a page of activity associated with a pull request.

    Activity items include comments, approvals, rescopes (i.e. adding and removing of commits), merges
    and more.

    Different types of activity items may be introduced in newer versions of Stash or by user installed
    plugins, so clients should be flexible enough to handle unexpected entity shapes in the returned
    page.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        from_type (str | Unset):
        from_id (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetActivitiesResponse200 | GetActivitiesResponse400 | GetActivitiesResponse401 | GetActivitiesResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
        from_type=from_type,
        from_id=from_id,
        start=start,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    *,
    client: AuthenticatedClient | Client,
    from_type: str | Unset = UNSET,
    from_id: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetActivitiesResponse200 | GetActivitiesResponse400 | GetActivitiesResponse401 | GetActivitiesResponse404 | None:
    """Get pull request activity

     Retrieve a page of activity associated with a pull request.

    Activity items include comments, approvals, rescopes (i.e. adding and removing of commits), merges
    and more.

    Different types of activity items may be introduced in newer versions of Stash or by user installed
    plugins, so clients should be flexible enough to handle unexpected entity shapes in the returned
    page.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        from_type (str | Unset):
        from_id (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetActivitiesResponse200 | GetActivitiesResponse400 | GetActivitiesResponse401 | GetActivitiesResponse404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            pull_request_id=pull_request_id,
            client=client,
            from_type=from_type,
            from_id=from_id,
            start=start,
            limit=limit,
        )
    ).parsed
