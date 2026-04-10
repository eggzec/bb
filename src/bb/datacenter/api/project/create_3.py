from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_3_response_400 import Create3Response400
from ...models.create_3_response_401 import Create3Response401
from ...models.create_3_response_404 import Create3Response404
from ...models.create_3_response_409 import Create3Response409
from ...models.rest_project_settings_restriction import RestProjectSettingsRestriction
from ...models.rest_project_settings_restriction_request import RestProjectSettingsRestrictionRequest
from ...types import Response


def _get_kwargs(
    project_key: str,
    *,
    body: RestProjectSettingsRestrictionRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/latest/projects/{project_key}/settings-restriction".format(
            project_key=quote(str(project_key), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Create3Response400
    | Create3Response401
    | Create3Response404
    | Create3Response409
    | RestProjectSettingsRestriction
    | None
):
    if response.status_code == 200:
        response_200 = RestProjectSettingsRestriction.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Create3Response400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Create3Response401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = Create3Response404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = Create3Response409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Create3Response400 | Create3Response401 | Create3Response404 | Create3Response409 | RestProjectSettingsRestriction
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
    body: RestProjectSettingsRestrictionRequest,
) -> Response[
    Create3Response400 | Create3Response401 | Create3Response404 | Create3Response409 | RestProjectSettingsRestriction
]:
    """Enforce project restriction

     Create a new project settings restriction for the given project.

    The authenticated user must have **PROJECT_ADMIN** permission for the target project to create a
    settings restriction.

    Args:
        project_key (str):
        body (RestProjectSettingsRestrictionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Create3Response400 | Create3Response401 | Create3Response404 | Create3Response409 | RestProjectSettingsRestriction]
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
    body: RestProjectSettingsRestrictionRequest,
) -> (
    Create3Response400
    | Create3Response401
    | Create3Response404
    | Create3Response409
    | RestProjectSettingsRestriction
    | None
):
    """Enforce project restriction

     Create a new project settings restriction for the given project.

    The authenticated user must have **PROJECT_ADMIN** permission for the target project to create a
    settings restriction.

    Args:
        project_key (str):
        body (RestProjectSettingsRestrictionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Create3Response400 | Create3Response401 | Create3Response404 | Create3Response409 | RestProjectSettingsRestriction
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
    body: RestProjectSettingsRestrictionRequest,
) -> Response[
    Create3Response400 | Create3Response401 | Create3Response404 | Create3Response409 | RestProjectSettingsRestriction
]:
    """Enforce project restriction

     Create a new project settings restriction for the given project.

    The authenticated user must have **PROJECT_ADMIN** permission for the target project to create a
    settings restriction.

    Args:
        project_key (str):
        body (RestProjectSettingsRestrictionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Create3Response400 | Create3Response401 | Create3Response404 | Create3Response409 | RestProjectSettingsRestriction]
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
    body: RestProjectSettingsRestrictionRequest,
) -> (
    Create3Response400
    | Create3Response401
    | Create3Response404
    | Create3Response409
    | RestProjectSettingsRestriction
    | None
):
    """Enforce project restriction

     Create a new project settings restriction for the given project.

    The authenticated user must have **PROJECT_ADMIN** permission for the target project to create a
    settings restriction.

    Args:
        project_key (str):
        body (RestProjectSettingsRestrictionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Create3Response400 | Create3Response401 | Create3Response404 | Create3Response409 | RestProjectSettingsRestriction
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            client=client,
            body=body,
        )
    ).parsed
