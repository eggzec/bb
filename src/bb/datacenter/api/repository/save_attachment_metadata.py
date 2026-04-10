from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.save_attachment_metadata_response_400 import SaveAttachmentMetadataResponse400
from ...models.save_attachment_metadata_response_401 import SaveAttachmentMetadataResponse401
from ...models.save_attachment_metadata_response_404 import SaveAttachmentMetadataResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    attachment_id: str,
    *,
    body: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/attachments/{attachment_id}/metadata".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            attachment_id=quote(str(attachment_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | SaveAttachmentMetadataResponse400
    | SaveAttachmentMetadataResponse401
    | SaveAttachmentMetadataResponse404
    | None
):
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 400:
        response_400 = SaveAttachmentMetadataResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = SaveAttachmentMetadataResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = SaveAttachmentMetadataResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | SaveAttachmentMetadataResponse400 | SaveAttachmentMetadataResponse401 | SaveAttachmentMetadataResponse404
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
    attachment_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: str | Unset = UNSET,
) -> Response[
    Any | SaveAttachmentMetadataResponse400 | SaveAttachmentMetadataResponse401 | SaveAttachmentMetadataResponse404
]:
    """Save attachment metadata

     Save attachment metadata.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    that is associated to the attachment that has the attachment metadata.

    Args:
        project_key (str):
        repository_slug (str):
        attachment_id (str):
        body (str | Unset): any valid JSON content

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SaveAttachmentMetadataResponse400 | SaveAttachmentMetadataResponse401 | SaveAttachmentMetadataResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        attachment_id=attachment_id,
        body=body,
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
    body: str | Unset = UNSET,
) -> (
    Any
    | SaveAttachmentMetadataResponse400
    | SaveAttachmentMetadataResponse401
    | SaveAttachmentMetadataResponse404
    | None
):
    """Save attachment metadata

     Save attachment metadata.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    that is associated to the attachment that has the attachment metadata.

    Args:
        project_key (str):
        repository_slug (str):
        attachment_id (str):
        body (str | Unset): any valid JSON content

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SaveAttachmentMetadataResponse400 | SaveAttachmentMetadataResponse401 | SaveAttachmentMetadataResponse404
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        attachment_id=attachment_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    attachment_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: str | Unset = UNSET,
) -> Response[
    Any | SaveAttachmentMetadataResponse400 | SaveAttachmentMetadataResponse401 | SaveAttachmentMetadataResponse404
]:
    """Save attachment metadata

     Save attachment metadata.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    that is associated to the attachment that has the attachment metadata.

    Args:
        project_key (str):
        repository_slug (str):
        attachment_id (str):
        body (str | Unset): any valid JSON content

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SaveAttachmentMetadataResponse400 | SaveAttachmentMetadataResponse401 | SaveAttachmentMetadataResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        attachment_id=attachment_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    attachment_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: str | Unset = UNSET,
) -> (
    Any
    | SaveAttachmentMetadataResponse400
    | SaveAttachmentMetadataResponse401
    | SaveAttachmentMetadataResponse404
    | None
):
    """Save attachment metadata

     Save attachment metadata.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    that is associated to the attachment that has the attachment metadata.

    Args:
        project_key (str):
        repository_slug (str):
        attachment_id (str):
        body (str | Unset): any valid JSON content

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SaveAttachmentMetadataResponse400 | SaveAttachmentMetadataResponse401 | SaveAttachmentMetadataResponse404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            attachment_id=attachment_id,
            client=client,
            body=body,
        )
    ).parsed
