from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_avatar_response_401 import GetAvatarResponse401
from ...models.get_avatar_response_404 import GetAvatarResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    hook_key: str,
    *,
    version: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["version"] = version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/hooks/{hook_key}/avatar".format(
            hook_key=quote(str(hook_key), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetAvatarResponse401 | GetAvatarResponse404 | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 401:
        response_401 = GetAvatarResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetAvatarResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetAvatarResponse401 | GetAvatarResponse404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    hook_key: str,
    *,
    client: AuthenticatedClient | Client,
    version: str | Unset = UNSET,
) -> Response[Any | GetAvatarResponse401 | GetAvatarResponse404]:
    """Get project avatar

     Retrieve the avatar for the project matching the supplied <strong>moduleKey</strong>.

    Args:
        hook_key (str):
        version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAvatarResponse401 | GetAvatarResponse404]
    """

    kwargs = _get_kwargs(
        hook_key=hook_key,
        version=version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    hook_key: str,
    *,
    client: AuthenticatedClient | Client,
    version: str | Unset = UNSET,
) -> Any | GetAvatarResponse401 | GetAvatarResponse404 | None:
    """Get project avatar

     Retrieve the avatar for the project matching the supplied <strong>moduleKey</strong>.

    Args:
        hook_key (str):
        version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAvatarResponse401 | GetAvatarResponse404
    """

    return sync_detailed(
        hook_key=hook_key,
        client=client,
        version=version,
    ).parsed


async def asyncio_detailed(
    hook_key: str,
    *,
    client: AuthenticatedClient | Client,
    version: str | Unset = UNSET,
) -> Response[Any | GetAvatarResponse401 | GetAvatarResponse404]:
    """Get project avatar

     Retrieve the avatar for the project matching the supplied <strong>moduleKey</strong>.

    Args:
        hook_key (str):
        version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAvatarResponse401 | GetAvatarResponse404]
    """

    kwargs = _get_kwargs(
        hook_key=hook_key,
        version=version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    hook_key: str,
    *,
    client: AuthenticatedClient | Client,
    version: str | Unset = UNSET,
) -> Any | GetAvatarResponse401 | GetAvatarResponse404 | None:
    """Get project avatar

     Retrieve the avatar for the project matching the supplied <strong>moduleKey</strong>.

    Args:
        hook_key (str):
        version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAvatarResponse401 | GetAvatarResponse404
    """

    return (
        await asyncio_detailed(
            hook_key=hook_key,
            client=client,
            version=version,
        )
    ).parsed
