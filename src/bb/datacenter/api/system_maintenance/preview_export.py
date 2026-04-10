from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.preview_export_response_400 import PreviewExportResponse400
from ...models.preview_export_response_401 import PreviewExportResponse401
from ...models.rest_export_request import RestExportRequest
from ...models.rest_scopes_example import RestScopesExample
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RestExportRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/latest/migration/exports/preview",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PreviewExportResponse400 | PreviewExportResponse401 | RestScopesExample | None:
    if response.status_code == 200:
        response_200 = RestScopesExample.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PreviewExportResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PreviewExportResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PreviewExportResponse400 | PreviewExportResponse401 | RestScopesExample]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RestExportRequest | Unset = UNSET,
) -> Response[PreviewExportResponse400 | PreviewExportResponse401 | RestScopesExample]:
    """Preview export

     Enumerates the projects and repositories that would be exported for a given export request.

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

    For a more detailed description of selectors, see the endpoint documentation for starting an export.

    The authenticated user must have **ADMIN** permission or higher to call this resource.

    Args:
        body (RestExportRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PreviewExportResponse400 | PreviewExportResponse401 | RestScopesExample]
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
    body: RestExportRequest | Unset = UNSET,
) -> PreviewExportResponse400 | PreviewExportResponse401 | RestScopesExample | None:
    """Preview export

     Enumerates the projects and repositories that would be exported for a given export request.

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

    For a more detailed description of selectors, see the endpoint documentation for starting an export.

    The authenticated user must have **ADMIN** permission or higher to call this resource.

    Args:
        body (RestExportRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PreviewExportResponse400 | PreviewExportResponse401 | RestScopesExample
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RestExportRequest | Unset = UNSET,
) -> Response[PreviewExportResponse400 | PreviewExportResponse401 | RestScopesExample]:
    """Preview export

     Enumerates the projects and repositories that would be exported for a given export request.

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

    For a more detailed description of selectors, see the endpoint documentation for starting an export.

    The authenticated user must have **ADMIN** permission or higher to call this resource.

    Args:
        body (RestExportRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PreviewExportResponse400 | PreviewExportResponse401 | RestScopesExample]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RestExportRequest | Unset = UNSET,
) -> PreviewExportResponse400 | PreviewExportResponse401 | RestScopesExample | None:
    """Preview export

     Enumerates the projects and repositories that would be exported for a given export request.

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

    For a more detailed description of selectors, see the endpoint documentation for starting an export.

    The authenticated user must have **ADMIN** permission or higher to call this resource.

    Args:
        body (RestExportRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PreviewExportResponse400 | PreviewExportResponse401 | RestScopesExample
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
