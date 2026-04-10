from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_auto_decline_settings import RestAutoDeclineSettings
from ...models.rest_auto_decline_settings_request import RestAutoDeclineSettingsRequest
from ...models.set_auto_decline_settings_response_400 import SetAutoDeclineSettingsResponse400
from ...models.set_auto_decline_settings_response_401 import SetAutoDeclineSettingsResponse401
from ...models.set_auto_decline_settings_response_404 import SetAutoDeclineSettingsResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    *,
    body: RestAutoDeclineSettingsRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/latest/projects/{project_key}/settings/auto-decline".format(
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
) -> (
    RestAutoDeclineSettings
    | SetAutoDeclineSettingsResponse400
    | SetAutoDeclineSettingsResponse401
    | SetAutoDeclineSettingsResponse404
    | None
):
    if response.status_code == 200:
        response_200 = RestAutoDeclineSettings.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = SetAutoDeclineSettingsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = SetAutoDeclineSettingsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = SetAutoDeclineSettingsResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    RestAutoDeclineSettings
    | SetAutoDeclineSettingsResponse400
    | SetAutoDeclineSettingsResponse401
    | SetAutoDeclineSettingsResponse404
]:
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
    body: RestAutoDeclineSettingsRequest | Unset = UNSET,
) -> Response[
    RestAutoDeclineSettings
    | SetAutoDeclineSettingsResponse400
    | SetAutoDeclineSettingsResponse401
    | SetAutoDeclineSettingsResponse404
]:
    """Create/Update auto decline settings

     Creates or updates the auto decline settings for the supplied project.

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for this project to call
    the resource.

    Args:
        project_key (str):
        body (RestAutoDeclineSettingsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestAutoDeclineSettings | SetAutoDeclineSettingsResponse400 | SetAutoDeclineSettingsResponse401 | SetAutoDeclineSettingsResponse404]
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
    body: RestAutoDeclineSettingsRequest | Unset = UNSET,
) -> (
    RestAutoDeclineSettings
    | SetAutoDeclineSettingsResponse400
    | SetAutoDeclineSettingsResponse401
    | SetAutoDeclineSettingsResponse404
    | None
):
    """Create/Update auto decline settings

     Creates or updates the auto decline settings for the supplied project.

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for this project to call
    the resource.

    Args:
        project_key (str):
        body (RestAutoDeclineSettingsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestAutoDeclineSettings | SetAutoDeclineSettingsResponse400 | SetAutoDeclineSettingsResponse401 | SetAutoDeclineSettingsResponse404
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
    body: RestAutoDeclineSettingsRequest | Unset = UNSET,
) -> Response[
    RestAutoDeclineSettings
    | SetAutoDeclineSettingsResponse400
    | SetAutoDeclineSettingsResponse401
    | SetAutoDeclineSettingsResponse404
]:
    """Create/Update auto decline settings

     Creates or updates the auto decline settings for the supplied project.

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for this project to call
    the resource.

    Args:
        project_key (str):
        body (RestAutoDeclineSettingsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestAutoDeclineSettings | SetAutoDeclineSettingsResponse400 | SetAutoDeclineSettingsResponse401 | SetAutoDeclineSettingsResponse404]
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
    body: RestAutoDeclineSettingsRequest | Unset = UNSET,
) -> (
    RestAutoDeclineSettings
    | SetAutoDeclineSettingsResponse400
    | SetAutoDeclineSettingsResponse401
    | SetAutoDeclineSettingsResponse404
    | None
):
    """Create/Update auto decline settings

     Creates or updates the auto decline settings for the supplied project.

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for this project to call
    the resource.

    Args:
        project_key (str):
        body (RestAutoDeclineSettingsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestAutoDeclineSettings | SetAutoDeclineSettingsResponse400 | SetAutoDeclineSettingsResponse401 | SetAutoDeclineSettingsResponse404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            client=client,
            body=body,
        )
    ).parsed
