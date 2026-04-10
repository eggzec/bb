from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_attachment_metadata_response_401 import GetAttachmentMetadataResponse401
from ...models.get_attachment_metadata_response_404 import GetAttachmentMetadataResponse404
from ...models.rest_attachment_metadata import RestAttachmentMetadata
from ...types import Response


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    attachment_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/attachments/{attachment_id}/metadata".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            attachment_id=quote(str(attachment_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetAttachmentMetadataResponse401 | GetAttachmentMetadataResponse404 | RestAttachmentMetadata | None:
    if response.status_code == 200:
        response_200 = RestAttachmentMetadata.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetAttachmentMetadataResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetAttachmentMetadataResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetAttachmentMetadataResponse401 | GetAttachmentMetadataResponse404 | RestAttachmentMetadata]:
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
) -> Response[GetAttachmentMetadataResponse401 | GetAttachmentMetadataResponse404 | RestAttachmentMetadata]:
    """Get attachment metadata

     Retrieve the attachment metadata.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    that is associated to the attachment that has the attachment metadata.

    Args:
        project_key (str):
        repository_slug (str):
        attachment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAttachmentMetadataResponse401 | GetAttachmentMetadataResponse404 | RestAttachmentMetadata]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        attachment_id=attachment_id,
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
) -> GetAttachmentMetadataResponse401 | GetAttachmentMetadataResponse404 | RestAttachmentMetadata | None:
    """Get attachment metadata

     Retrieve the attachment metadata.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    that is associated to the attachment that has the attachment metadata.

    Args:
        project_key (str):
        repository_slug (str):
        attachment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAttachmentMetadataResponse401 | GetAttachmentMetadataResponse404 | RestAttachmentMetadata
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        attachment_id=attachment_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    attachment_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetAttachmentMetadataResponse401 | GetAttachmentMetadataResponse404 | RestAttachmentMetadata]:
    """Get attachment metadata

     Retrieve the attachment metadata.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    that is associated to the attachment that has the attachment metadata.

    Args:
        project_key (str):
        repository_slug (str):
        attachment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAttachmentMetadataResponse401 | GetAttachmentMetadataResponse404 | RestAttachmentMetadata]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        attachment_id=attachment_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    attachment_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetAttachmentMetadataResponse401 | GetAttachmentMetadataResponse404 | RestAttachmentMetadata | None:
    """Get attachment metadata

     Retrieve the attachment metadata.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    that is associated to the attachment that has the attachment metadata.

    Args:
        project_key (str):
        repository_slug (str):
        attachment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAttachmentMetadataResponse401 | GetAttachmentMetadataResponse404 | RestAttachmentMetadata
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            attachment_id=attachment_id,
            client=client,
        )
    ).parsed
