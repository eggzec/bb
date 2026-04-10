from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_attachment_response_401 import DeleteAttachmentResponse401
from ...models.delete_attachment_response_404 import DeleteAttachmentResponse404
from ...types import Response


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    attachment_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/attachments/{attachment_id}".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            attachment_id=quote(str(attachment_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteAttachmentResponse401 | DeleteAttachmentResponse404 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = DeleteAttachmentResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = DeleteAttachmentResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteAttachmentResponse401 | DeleteAttachmentResponse404]:
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
) -> Response[Any | DeleteAttachmentResponse401 | DeleteAttachmentResponse404]:
    """Delete an attachment

     Delete an attachment.

    The user must be authenticated and have <strong>REPO_ADMIN</strong> permission for the specified
    repository.

    Args:
        project_key (str):
        repository_slug (str):
        attachment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAttachmentResponse401 | DeleteAttachmentResponse404]
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
) -> Any | DeleteAttachmentResponse401 | DeleteAttachmentResponse404 | None:
    """Delete an attachment

     Delete an attachment.

    The user must be authenticated and have <strong>REPO_ADMIN</strong> permission for the specified
    repository.

    Args:
        project_key (str):
        repository_slug (str):
        attachment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAttachmentResponse401 | DeleteAttachmentResponse404
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
) -> Response[Any | DeleteAttachmentResponse401 | DeleteAttachmentResponse404]:
    """Delete an attachment

     Delete an attachment.

    The user must be authenticated and have <strong>REPO_ADMIN</strong> permission for the specified
    repository.

    Args:
        project_key (str):
        repository_slug (str):
        attachment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAttachmentResponse401 | DeleteAttachmentResponse404]
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
) -> Any | DeleteAttachmentResponse401 | DeleteAttachmentResponse404 | None:
    """Delete an attachment

     Delete an attachment.

    The user must be authenticated and have <strong>REPO_ADMIN</strong> permission for the specified
    repository.

    Args:
        project_key (str):
        repository_slug (str):
        attachment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAttachmentResponse401 | DeleteAttachmentResponse404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            attachment_id=attachment_id,
            client=client,
        )
    ).parsed
