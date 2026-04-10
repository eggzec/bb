from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.stream_commits_response_200 import StreamCommitsResponse200
from ...models.stream_commits_response_404 import StreamCommitsResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    *,
    from_repo: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["fromRepo"] = from_repo

    params["from"] = from_

    params["to"] = to

    params["start"] = start

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/compare/commits".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> StreamCommitsResponse200 | StreamCommitsResponse404 | None:
    if response.status_code == 200:
        response_200 = StreamCommitsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = StreamCommitsResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[StreamCommitsResponse200 | StreamCommitsResponse404]:
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
    from_repo: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[StreamCommitsResponse200 | StreamCommitsResponse404]:
    """Get accessible commits

     Gets the commits accessible from the <code>from</code> commit but not in the <code>to</code> commit.

    If either the <code>from</code> or <code>to</code> commit are not specified, they will be replaced
    by the default branch of their containing repository.

    Args:
        project_key (str):
        repository_slug (str):
        from_repo (str | Unset):
        from_ (str | Unset):
        to (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StreamCommitsResponse200 | StreamCommitsResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        from_repo=from_repo,
        from_=from_,
        to=to,
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
    *,
    client: AuthenticatedClient | Client,
    from_repo: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> StreamCommitsResponse200 | StreamCommitsResponse404 | None:
    """Get accessible commits

     Gets the commits accessible from the <code>from</code> commit but not in the <code>to</code> commit.

    If either the <code>from</code> or <code>to</code> commit are not specified, they will be replaced
    by the default branch of their containing repository.

    Args:
        project_key (str):
        repository_slug (str):
        from_repo (str | Unset):
        from_ (str | Unset):
        to (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StreamCommitsResponse200 | StreamCommitsResponse404
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        client=client,
        from_repo=from_repo,
        from_=from_,
        to=to,
        start=start,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    from_repo: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[StreamCommitsResponse200 | StreamCommitsResponse404]:
    """Get accessible commits

     Gets the commits accessible from the <code>from</code> commit but not in the <code>to</code> commit.

    If either the <code>from</code> or <code>to</code> commit are not specified, they will be replaced
    by the default branch of their containing repository.

    Args:
        project_key (str):
        repository_slug (str):
        from_repo (str | Unset):
        from_ (str | Unset):
        to (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StreamCommitsResponse200 | StreamCommitsResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        from_repo=from_repo,
        from_=from_,
        to=to,
        start=start,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    from_repo: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> StreamCommitsResponse200 | StreamCommitsResponse404 | None:
    """Get accessible commits

     Gets the commits accessible from the <code>from</code> commit but not in the <code>to</code> commit.

    If either the <code>from</code> or <code>to</code> commit are not specified, they will be replaced
    by the default branch of their containing repository.

    Args:
        project_key (str):
        repository_slug (str):
        from_repo (str | Unset):
        from_ (str | Unset):
        to (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StreamCommitsResponse200 | StreamCommitsResponse404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            client=client,
            from_repo=from_repo,
            from_=from_,
            to=to,
            start=start,
            limit=limit,
        )
    ).parsed
