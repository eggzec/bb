from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.stream_raw_response_400 import StreamRawResponse400
from ...models.stream_raw_response_401 import StreamRawResponse401
from ...models.stream_raw_response_404 import StreamRawResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    path: str,
    *,
    at: str | Unset = UNSET,
    markup: str | Unset = UNSET,
    html_escape: str | Unset = UNSET,
    include_heading_id: str | Unset = UNSET,
    hardwrap: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["at"] = at

    params["markup"] = markup

    params["htmlEscape"] = html_escape

    params["includeHeadingId"] = include_heading_id

    params["hardwrap"] = hardwrap

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/raw/{path}".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            path=quote(str(path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | StreamRawResponse400 | StreamRawResponse401 | StreamRawResponse404 | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 400:
        response_400 = StreamRawResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = StreamRawResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = StreamRawResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | StreamRawResponse400 | StreamRawResponse401 | StreamRawResponse404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    repository_slug: str,
    path: str,
    *,
    client: AuthenticatedClient | Client,
    at: str | Unset = UNSET,
    markup: str | Unset = UNSET,
    html_escape: str | Unset = UNSET,
    include_heading_id: str | Unset = UNSET,
    hardwrap: str | Unset = UNSET,
) -> Response[Any | StreamRawResponse400 | StreamRawResponse401 | StreamRawResponse404]:
    """Get raw content of a file at revision

     Retrieve the raw content for a file path at a specified revision.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        path (str):
        at (str | Unset):
        markup (str | Unset):
        html_escape (str | Unset):
        include_heading_id (str | Unset):
        hardwrap (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | StreamRawResponse400 | StreamRawResponse401 | StreamRawResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        path=path,
        at=at,
        markup=markup,
        html_escape=html_escape,
        include_heading_id=include_heading_id,
        hardwrap=hardwrap,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    repository_slug: str,
    path: str,
    *,
    client: AuthenticatedClient | Client,
    at: str | Unset = UNSET,
    markup: str | Unset = UNSET,
    html_escape: str | Unset = UNSET,
    include_heading_id: str | Unset = UNSET,
    hardwrap: str | Unset = UNSET,
) -> Any | StreamRawResponse400 | StreamRawResponse401 | StreamRawResponse404 | None:
    """Get raw content of a file at revision

     Retrieve the raw content for a file path at a specified revision.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        path (str):
        at (str | Unset):
        markup (str | Unset):
        html_escape (str | Unset):
        include_heading_id (str | Unset):
        hardwrap (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | StreamRawResponse400 | StreamRawResponse401 | StreamRawResponse404
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        path=path,
        client=client,
        at=at,
        markup=markup,
        html_escape=html_escape,
        include_heading_id=include_heading_id,
        hardwrap=hardwrap,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    path: str,
    *,
    client: AuthenticatedClient | Client,
    at: str | Unset = UNSET,
    markup: str | Unset = UNSET,
    html_escape: str | Unset = UNSET,
    include_heading_id: str | Unset = UNSET,
    hardwrap: str | Unset = UNSET,
) -> Response[Any | StreamRawResponse400 | StreamRawResponse401 | StreamRawResponse404]:
    """Get raw content of a file at revision

     Retrieve the raw content for a file path at a specified revision.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        path (str):
        at (str | Unset):
        markup (str | Unset):
        html_escape (str | Unset):
        include_heading_id (str | Unset):
        hardwrap (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | StreamRawResponse400 | StreamRawResponse401 | StreamRawResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        path=path,
        at=at,
        markup=markup,
        html_escape=html_escape,
        include_heading_id=include_heading_id,
        hardwrap=hardwrap,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    path: str,
    *,
    client: AuthenticatedClient | Client,
    at: str | Unset = UNSET,
    markup: str | Unset = UNSET,
    html_escape: str | Unset = UNSET,
    include_heading_id: str | Unset = UNSET,
    hardwrap: str | Unset = UNSET,
) -> Any | StreamRawResponse400 | StreamRawResponse401 | StreamRawResponse404 | None:
    """Get raw content of a file at revision

     Retrieve the raw content for a file path at a specified revision.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        path (str):
        at (str | Unset):
        markup (str | Unset):
        html_escape (str | Unset):
        include_heading_id (str | Unset):
        hardwrap (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | StreamRawResponse400 | StreamRawResponse401 | StreamRawResponse404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            path=path,
            client=client,
            at=at,
            markup=markup,
            html_escape=html_escape,
            include_heading_id=include_heading_id,
            hardwrap=hardwrap,
        )
    ).parsed
