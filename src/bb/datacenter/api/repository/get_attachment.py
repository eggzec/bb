from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_attachment_response_401 import GetAttachmentResponse401
from ...models.get_attachment_response_404 import GetAttachmentResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    attachment_id: str,
    *,
    user_agent: str | Unset = UNSET,
    range_: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(user_agent, Unset):
        headers["User-Agent"] = user_agent

    if not isinstance(range_, Unset):
        headers["Range"] = range_

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/attachments/{attachment_id}".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            attachment_id=quote(str(attachment_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetAttachmentResponse401 | GetAttachmentResponse404 | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 206:
        response_206 = cast(Any, None)
        return response_206

    if response.status_code == 401:
        response_401 = GetAttachmentResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetAttachmentResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetAttachmentResponse401 | GetAttachmentResponse404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    repository_slug: str,
    attachment_id: str,
    *,
    client: AuthenticatedClient | Client,
    user_agent: str | Unset = UNSET,
    range_: str | Unset = UNSET,
) -> Response[Any | GetAttachmentResponse401 | GetAttachmentResponse404]:
    """Get an attachment

     Retrieve the attachment.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    that is associated to the attachment.

    Range requests (see IETF RFC7233) are supported. However only a single range issupported. If
    multiple ranges are passed the ranges will be ignored and the entire content will be returned in the
    response.

    Args:
        project_key (str):
        repository_slug (str):
        attachment_id (str):
        user_agent (str | Unset):
        range_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAttachmentResponse401 | GetAttachmentResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        attachment_id=attachment_id,
        user_agent=user_agent,
        range_=range_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    repository_slug: str,
    attachment_id: str,
    *,
    client: AuthenticatedClient | Client,
    user_agent: str | Unset = UNSET,
    range_: str | Unset = UNSET,
) -> Any | GetAttachmentResponse401 | GetAttachmentResponse404 | None:
    """Get an attachment

     Retrieve the attachment.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    that is associated to the attachment.

    Range requests (see IETF RFC7233) are supported. However only a single range issupported. If
    multiple ranges are passed the ranges will be ignored and the entire content will be returned in the
    response.

    Args:
        project_key (str):
        repository_slug (str):
        attachment_id (str):
        user_agent (str | Unset):
        range_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAttachmentResponse401 | GetAttachmentResponse404
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        attachment_id=attachment_id,
        client=client,
        user_agent=user_agent,
        range_=range_,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    attachment_id: str,
    *,
    client: AuthenticatedClient | Client,
    user_agent: str | Unset = UNSET,
    range_: str | Unset = UNSET,
) -> Response[Any | GetAttachmentResponse401 | GetAttachmentResponse404]:
    """Get an attachment

     Retrieve the attachment.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    that is associated to the attachment.

    Range requests (see IETF RFC7233) are supported. However only a single range issupported. If
    multiple ranges are passed the ranges will be ignored and the entire content will be returned in the
    response.

    Args:
        project_key (str):
        repository_slug (str):
        attachment_id (str):
        user_agent (str | Unset):
        range_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAttachmentResponse401 | GetAttachmentResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        attachment_id=attachment_id,
        user_agent=user_agent,
        range_=range_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    attachment_id: str,
    *,
    client: AuthenticatedClient | Client,
    user_agent: str | Unset = UNSET,
    range_: str | Unset = UNSET,
) -> Any | GetAttachmentResponse401 | GetAttachmentResponse404 | None:
    """Get an attachment

     Retrieve the attachment.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    that is associated to the attachment.

    Range requests (see IETF RFC7233) are supported. However only a single range issupported. If
    multiple ranges are passed the ranges will be ignored and the entire content will be returned in the
    response.

    Args:
        project_key (str):
        repository_slug (str):
        attachment_id (str):
        user_agent (str | Unset):
        range_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAttachmentResponse401 | GetAttachmentResponse404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            attachment_id=attachment_id,
            client=client,
            user_agent=user_agent,
            range_=range_,
        )
    ).parsed
