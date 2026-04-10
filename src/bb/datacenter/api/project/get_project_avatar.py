from http import HTTPStatus
from io import BytesIO
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_project_avatar_response_401 import GetProjectAvatarResponse401
from ...models.get_project_avatar_response_404 import GetProjectAvatarResponse404
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    project_key: str,
    *,
    s: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["s"] = s

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/avatar.png".format(
            project_key=quote(str(project_key), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> File | GetProjectAvatarResponse401 | GetProjectAvatarResponse404 | None:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.content))

        return response_200

    if response.status_code == 401:
        response_401 = GetProjectAvatarResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetProjectAvatarResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[File | GetProjectAvatarResponse401 | GetProjectAvatarResponse404]:
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
    s: str | Unset = UNSET,
) -> Response[File | GetProjectAvatarResponse401 | GetProjectAvatarResponse404]:
    """Get avatar for project

     Retrieve the avatar for the project matching the supplied <strong>projectKey</strong>.

    The authenticated user must have <strong>PROJECT_VIEW</strong> permission for the specified project
    to call this resource.

    Args:
        project_key (str):
        s (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File | GetProjectAvatarResponse401 | GetProjectAvatarResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        s=s,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    s: str | Unset = UNSET,
) -> File | GetProjectAvatarResponse401 | GetProjectAvatarResponse404 | None:
    """Get avatar for project

     Retrieve the avatar for the project matching the supplied <strong>projectKey</strong>.

    The authenticated user must have <strong>PROJECT_VIEW</strong> permission for the specified project
    to call this resource.

    Args:
        project_key (str):
        s (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File | GetProjectAvatarResponse401 | GetProjectAvatarResponse404
    """

    return sync_detailed(
        project_key=project_key,
        client=client,
        s=s,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    s: str | Unset = UNSET,
) -> Response[File | GetProjectAvatarResponse401 | GetProjectAvatarResponse404]:
    """Get avatar for project

     Retrieve the avatar for the project matching the supplied <strong>projectKey</strong>.

    The authenticated user must have <strong>PROJECT_VIEW</strong> permission for the specified project
    to call this resource.

    Args:
        project_key (str):
        s (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File | GetProjectAvatarResponse401 | GetProjectAvatarResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        s=s,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    s: str | Unset = UNSET,
) -> File | GetProjectAvatarResponse401 | GetProjectAvatarResponse404 | None:
    """Get avatar for project

     Retrieve the avatar for the project matching the supplied <strong>projectKey</strong>.

    The authenticated user must have <strong>PROJECT_VIEW</strong> permission for the specified project
    to call this resource.

    Args:
        project_key (str):
        s (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File | GetProjectAvatarResponse401 | GetProjectAvatarResponse404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            client=client,
            s=s,
        )
    ).parsed
