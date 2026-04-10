from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_auto_merge_project_settings_request import RestAutoMergeProjectSettingsRequest
from ...models.rest_auto_merge_restricted_settings import RestAutoMergeRestrictedSettings
from ...models.set_response_400 import SetResponse400
from ...models.set_response_401 import SetResponse401
from ...models.set_response_404 import SetResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    *,
    body: RestAutoMergeProjectSettingsRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/latest/projects/{project_key}/settings/auto-merge".format(
            project_key=quote(str(project_key), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RestAutoMergeRestrictedSettings | SetResponse400 | SetResponse401 | SetResponse404 | None:
    if response.status_code == 200:
        response_200 = RestAutoMergeRestrictedSettings.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = SetResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = SetResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = SetResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RestAutoMergeRestrictedSettings | SetResponse400 | SetResponse401 | SetResponse404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestAutoMergeProjectSettingsRequest | Unset = UNSET,
) -> Response[RestAutoMergeRestrictedSettings | SetResponse400 | SetResponse401 | SetResponse404]:
    """Create or update the pull request auto-merge settings

     Creates or updates the pull request auto-merge settings for the supplied project, and applies the
    restriction action specified in the request.

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for this project to call
    the resource.

    Args:
        project_key (str):
        body (RestAutoMergeProjectSettingsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestAutoMergeRestrictedSettings | SetResponse400 | SetResponse401 | SetResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestAutoMergeProjectSettingsRequest | Unset = UNSET,
) -> RestAutoMergeRestrictedSettings | SetResponse400 | SetResponse401 | SetResponse404 | None:
    """Create or update the pull request auto-merge settings

     Creates or updates the pull request auto-merge settings for the supplied project, and applies the
    restriction action specified in the request.

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for this project to call
    the resource.

    Args:
        project_key (str):
        body (RestAutoMergeProjectSettingsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestAutoMergeRestrictedSettings | SetResponse400 | SetResponse401 | SetResponse404
    """

    return sync_detailed(
        project_key=project_key,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestAutoMergeProjectSettingsRequest | Unset = UNSET,
) -> Response[RestAutoMergeRestrictedSettings | SetResponse400 | SetResponse401 | SetResponse404]:
    """Create or update the pull request auto-merge settings

     Creates or updates the pull request auto-merge settings for the supplied project, and applies the
    restriction action specified in the request.

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for this project to call
    the resource.

    Args:
        project_key (str):
        body (RestAutoMergeProjectSettingsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestAutoMergeRestrictedSettings | SetResponse400 | SetResponse401 | SetResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestAutoMergeProjectSettingsRequest | Unset = UNSET,
) -> RestAutoMergeRestrictedSettings | SetResponse400 | SetResponse401 | SetResponse404 | None:
    """Create or update the pull request auto-merge settings

     Creates or updates the pull request auto-merge settings for the supplied project, and applies the
    restriction action specified in the request.

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for this project to call
    the resource.

    Args:
        project_key (str):
        body (RestAutoMergeProjectSettingsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestAutoMergeRestrictedSettings | SetResponse400 | SetResponse401 | SetResponse404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            client=client,
            body=body,
        )
    ).parsed
