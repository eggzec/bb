from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.example_preview_migration import ExamplePreviewMigration
from ...models.preview_mesh_migration_response_400 import PreviewMeshMigrationResponse400
from ...models.preview_mesh_migration_response_401 import PreviewMeshMigrationResponse401
from ...models.rest_mesh_migration_request import RestMeshMigrationRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RestMeshMigrationRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/latest/migration/mesh/preview",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ExamplePreviewMigration | PreviewMeshMigrationResponse400 | PreviewMeshMigrationResponse401 | None:
    if response.status_code == 200:
        response_200 = ExamplePreviewMigration.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PreviewMeshMigrationResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PreviewMeshMigrationResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ExamplePreviewMigration | PreviewMeshMigrationResponse400 | PreviewMeshMigrationResponse401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RestMeshMigrationRequest | Unset = UNSET,
) -> Response[ExamplePreviewMigration | PreviewMeshMigrationResponse400 | PreviewMeshMigrationResponse401]:
    """Preview Mesh migration

     Enumerates the projects and repositories that would be migrated for a given request.

    All affected repositories will be enumerated explicitly, and while projects are listed as individual
    items in responses from this endpoint, their presence does not imply that all their repositories are
    included.

    While this endpoint can be used to verify that all selectors in the request apply as intended, it
    should be noted that a subsequent, actual export might contain a different set of repositories, as
    they might have been added or deleted in the meantime.

    Note that the overall response from this endpoint can become very large when a lot of repositories
    end up in the selection. This is why the server is streaming the response while it is being
    generated (as opposed to creating it in memory and then sending it all at once) and it can be
    consumed in a streaming way, too.

    Also, due to the potential size of the response, projects and repositories are listed with fewer
    details than in other REST responses.

    The authenticated user must have **SYS_ADMIN** permission to call this resource.

    Args:
        body (RestMeshMigrationRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExamplePreviewMigration | PreviewMeshMigrationResponse400 | PreviewMeshMigrationResponse401]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: RestMeshMigrationRequest | Unset = UNSET,
) -> ExamplePreviewMigration | PreviewMeshMigrationResponse400 | PreviewMeshMigrationResponse401 | None:
    """Preview Mesh migration

     Enumerates the projects and repositories that would be migrated for a given request.

    All affected repositories will be enumerated explicitly, and while projects are listed as individual
    items in responses from this endpoint, their presence does not imply that all their repositories are
    included.

    While this endpoint can be used to verify that all selectors in the request apply as intended, it
    should be noted that a subsequent, actual export might contain a different set of repositories, as
    they might have been added or deleted in the meantime.

    Note that the overall response from this endpoint can become very large when a lot of repositories
    end up in the selection. This is why the server is streaming the response while it is being
    generated (as opposed to creating it in memory and then sending it all at once) and it can be
    consumed in a streaming way, too.

    Also, due to the potential size of the response, projects and repositories are listed with fewer
    details than in other REST responses.

    The authenticated user must have **SYS_ADMIN** permission to call this resource.

    Args:
        body (RestMeshMigrationRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExamplePreviewMigration | PreviewMeshMigrationResponse400 | PreviewMeshMigrationResponse401
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RestMeshMigrationRequest | Unset = UNSET,
) -> Response[ExamplePreviewMigration | PreviewMeshMigrationResponse400 | PreviewMeshMigrationResponse401]:
    """Preview Mesh migration

     Enumerates the projects and repositories that would be migrated for a given request.

    All affected repositories will be enumerated explicitly, and while projects are listed as individual
    items in responses from this endpoint, their presence does not imply that all their repositories are
    included.

    While this endpoint can be used to verify that all selectors in the request apply as intended, it
    should be noted that a subsequent, actual export might contain a different set of repositories, as
    they might have been added or deleted in the meantime.

    Note that the overall response from this endpoint can become very large when a lot of repositories
    end up in the selection. This is why the server is streaming the response while it is being
    generated (as opposed to creating it in memory and then sending it all at once) and it can be
    consumed in a streaming way, too.

    Also, due to the potential size of the response, projects and repositories are listed with fewer
    details than in other REST responses.

    The authenticated user must have **SYS_ADMIN** permission to call this resource.

    Args:
        body (RestMeshMigrationRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExamplePreviewMigration | PreviewMeshMigrationResponse400 | PreviewMeshMigrationResponse401]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RestMeshMigrationRequest | Unset = UNSET,
) -> ExamplePreviewMigration | PreviewMeshMigrationResponse400 | PreviewMeshMigrationResponse401 | None:
    """Preview Mesh migration

     Enumerates the projects and repositories that would be migrated for a given request.

    All affected repositories will be enumerated explicitly, and while projects are listed as individual
    items in responses from this endpoint, their presence does not imply that all their repositories are
    included.

    While this endpoint can be used to verify that all selectors in the request apply as intended, it
    should be noted that a subsequent, actual export might contain a different set of repositories, as
    they might have been added or deleted in the meantime.

    Note that the overall response from this endpoint can become very large when a lot of repositories
    end up in the selection. This is why the server is streaming the response while it is being
    generated (as opposed to creating it in memory and then sending it all at once) and it can be
    consumed in a streaming way, too.

    Also, due to the potential size of the response, projects and repositories are listed with fewer
    details than in other REST responses.

    The authenticated user must have **SYS_ADMIN** permission to call this resource.

    Args:
        body (RestMeshMigrationRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExamplePreviewMigration | PreviewMeshMigrationResponse400 | PreviewMeshMigrationResponse401
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
