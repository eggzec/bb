from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.stream_contributing_response_401 import StreamContributingResponse401
from ...models.stream_contributing_response_404 import StreamContributingResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
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
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/contributing".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> StreamContributingResponse401 | StreamContributingResponse404 | str | None:
    if response.status_code == 200:
        response_200 = response.text
        return response_200

    if response.status_code == 401:
        response_401 = StreamContributingResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = StreamContributingResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[StreamContributingResponse401 | StreamContributingResponse404 | str]:
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
    at: str | Unset = UNSET,
    markup: str | Unset = UNSET,
    html_escape: str | Unset = UNSET,
    include_heading_id: str | Unset = UNSET,
    hardwrap: str | Unset = UNSET,
) -> Response[StreamContributingResponse401 | StreamContributingResponse404 | str]:
    """Get repository contributing guidelines

     Retrieves the contributing guidelines for the repository, if they've been defined.

    This checks the repository for a CONTRIBUTING file, optionally with an md or txt extension, and, if
    found, streams it. By default, the <i>raw content</i> of the file is streamed. Appending
    <code>?markup</code> to the URL will stream an HTML-rendered version instead.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        at (str | Unset):
        markup (str | Unset):
        html_escape (str | Unset):
        include_heading_id (str | Unset):
        hardwrap (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StreamContributingResponse401 | StreamContributingResponse404 | str]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
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
    *,
    client: AuthenticatedClient | Client,
    at: str | Unset = UNSET,
    markup: str | Unset = UNSET,
    html_escape: str | Unset = UNSET,
    include_heading_id: str | Unset = UNSET,
    hardwrap: str | Unset = UNSET,
) -> StreamContributingResponse401 | StreamContributingResponse404 | str | None:
    """Get repository contributing guidelines

     Retrieves the contributing guidelines for the repository, if they've been defined.

    This checks the repository for a CONTRIBUTING file, optionally with an md or txt extension, and, if
    found, streams it. By default, the <i>raw content</i> of the file is streamed. Appending
    <code>?markup</code> to the URL will stream an HTML-rendered version instead.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        at (str | Unset):
        markup (str | Unset):
        html_escape (str | Unset):
        include_heading_id (str | Unset):
        hardwrap (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StreamContributingResponse401 | StreamContributingResponse404 | str
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
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
    *,
    client: AuthenticatedClient | Client,
    at: str | Unset = UNSET,
    markup: str | Unset = UNSET,
    html_escape: str | Unset = UNSET,
    include_heading_id: str | Unset = UNSET,
    hardwrap: str | Unset = UNSET,
) -> Response[StreamContributingResponse401 | StreamContributingResponse404 | str]:
    """Get repository contributing guidelines

     Retrieves the contributing guidelines for the repository, if they've been defined.

    This checks the repository for a CONTRIBUTING file, optionally with an md or txt extension, and, if
    found, streams it. By default, the <i>raw content</i> of the file is streamed. Appending
    <code>?markup</code> to the URL will stream an HTML-rendered version instead.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        at (str | Unset):
        markup (str | Unset):
        html_escape (str | Unset):
        include_heading_id (str | Unset):
        hardwrap (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StreamContributingResponse401 | StreamContributingResponse404 | str]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
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
    *,
    client: AuthenticatedClient | Client,
    at: str | Unset = UNSET,
    markup: str | Unset = UNSET,
    html_escape: str | Unset = UNSET,
    include_heading_id: str | Unset = UNSET,
    hardwrap: str | Unset = UNSET,
) -> StreamContributingResponse401 | StreamContributingResponse404 | str | None:
    """Get repository contributing guidelines

     Retrieves the contributing guidelines for the repository, if they've been defined.

    This checks the repository for a CONTRIBUTING file, optionally with an md or txt extension, and, if
    found, streams it. By default, the <i>raw content</i> of the file is streamed. Appending
    <code>?markup</code> to the URL will stream an HTML-rendered version instead.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        at (str | Unset):
        markup (str | Unset):
        html_escape (str | Unset):
        include_heading_id (str | Unset):
        hardwrap (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StreamContributingResponse401 | StreamContributingResponse404 | str
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            client=client,
            at=at,
            markup=markup,
            html_escape=html_escape,
            include_heading_id=include_heading_id,
            hardwrap=hardwrap,
        )
    ).parsed
