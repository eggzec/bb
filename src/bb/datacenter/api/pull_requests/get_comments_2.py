from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_comments_2_response_200 import GetComments2Response200
from ...models.get_comments_2_response_401 import GetComments2Response401
from ...models.get_comments_2_response_404 import GetComments2Response404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    *,
    path: str,
    from_hash: str | Unset = UNSET,
    anchor_state: str | Unset = UNSET,
    diff_type: list[str] | Unset = UNSET,
    to_hash: str | Unset = UNSET,
    state: list[str] | Unset = UNSET,
    diff_types: str | Unset = UNSET,
    states: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["path"] = path

    params["fromHash"] = from_hash

    params["anchorState"] = anchor_state

    json_diff_type: list[str] | Unset = UNSET
    if not isinstance(diff_type, Unset):
        json_diff_type = diff_type

    params["diffType"] = json_diff_type

    params["toHash"] = to_hash

    json_state: list[str] | Unset = UNSET
    if not isinstance(state, Unset):
        json_state = state

    params["state"] = json_state

    params["diffTypes"] = diff_types

    params["states"] = states

    params["start"] = start

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/pull-requests/{pull_request_id}/comments".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            pull_request_id=quote(str(pull_request_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetComments2Response200 | GetComments2Response401 | GetComments2Response404 | None:
    if response.status_code == 200:
        response_200 = GetComments2Response200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetComments2Response401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetComments2Response404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetComments2Response200 | GetComments2Response401 | GetComments2Response404]:
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
    path: str,
    from_hash: str | Unset = UNSET,
    anchor_state: str | Unset = UNSET,
    diff_type: list[str] | Unset = UNSET,
    to_hash: str | Unset = UNSET,
    state: list[str] | Unset = UNSET,
    diff_types: str | Unset = UNSET,
    states: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GetComments2Response200 | GetComments2Response401 | GetComments2Response404]:
    """Get pull request comments for path

     Gets comments for the specified pull request and path.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        path (str):
        from_hash (str | Unset):
        anchor_state (str | Unset):
        diff_type (list[str] | Unset):
        to_hash (str | Unset):
        state (list[str] | Unset):
        diff_types (str | Unset):
        states (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetComments2Response200 | GetComments2Response401 | GetComments2Response404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
        path=path,
        from_hash=from_hash,
        anchor_state=anchor_state,
        diff_type=diff_type,
        to_hash=to_hash,
        state=state,
        diff_types=diff_types,
        states=states,
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
    path: str,
    from_hash: str | Unset = UNSET,
    anchor_state: str | Unset = UNSET,
    diff_type: list[str] | Unset = UNSET,
    to_hash: str | Unset = UNSET,
    state: list[str] | Unset = UNSET,
    diff_types: str | Unset = UNSET,
    states: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetComments2Response200 | GetComments2Response401 | GetComments2Response404 | None:
    """Get pull request comments for path

     Gets comments for the specified pull request and path.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        path (str):
        from_hash (str | Unset):
        anchor_state (str | Unset):
        diff_type (list[str] | Unset):
        to_hash (str | Unset):
        state (list[str] | Unset):
        diff_types (str | Unset):
        states (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetComments2Response200 | GetComments2Response401 | GetComments2Response404
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
        client=client,
        path=path,
        from_hash=from_hash,
        anchor_state=anchor_state,
        diff_type=diff_type,
        to_hash=to_hash,
        state=state,
        diff_types=diff_types,
        states=states,
        start=start,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    *,
    client: AuthenticatedClient | Client,
    path: str,
    from_hash: str | Unset = UNSET,
    anchor_state: str | Unset = UNSET,
    diff_type: list[str] | Unset = UNSET,
    to_hash: str | Unset = UNSET,
    state: list[str] | Unset = UNSET,
    diff_types: str | Unset = UNSET,
    states: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GetComments2Response200 | GetComments2Response401 | GetComments2Response404]:
    """Get pull request comments for path

     Gets comments for the specified pull request and path.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        path (str):
        from_hash (str | Unset):
        anchor_state (str | Unset):
        diff_type (list[str] | Unset):
        to_hash (str | Unset):
        state (list[str] | Unset):
        diff_types (str | Unset):
        states (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetComments2Response200 | GetComments2Response401 | GetComments2Response404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
        path=path,
        from_hash=from_hash,
        anchor_state=anchor_state,
        diff_type=diff_type,
        to_hash=to_hash,
        state=state,
        diff_types=diff_types,
        states=states,
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
    path: str,
    from_hash: str | Unset = UNSET,
    anchor_state: str | Unset = UNSET,
    diff_type: list[str] | Unset = UNSET,
    to_hash: str | Unset = UNSET,
    state: list[str] | Unset = UNSET,
    diff_types: str | Unset = UNSET,
    states: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetComments2Response200 | GetComments2Response401 | GetComments2Response404 | None:
    """Get pull request comments for path

     Gets comments for the specified pull request and path.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        path (str):
        from_hash (str | Unset):
        anchor_state (str | Unset):
        diff_type (list[str] | Unset):
        to_hash (str | Unset):
        state (list[str] | Unset):
        diff_types (str | Unset):
        states (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetComments2Response200 | GetComments2Response401 | GetComments2Response404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            pull_request_id=pull_request_id,
            client=client,
            path=path,
            from_hash=from_hash,
            anchor_state=anchor_state,
            diff_type=diff_type,
            to_hash=to_hash,
            state=state,
            diff_types=diff_types,
            states=states,
            start=start,
            limit=limit,
        )
    ).parsed
