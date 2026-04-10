from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_hook_script_response_401 import GetHookScriptResponse401
from ...models.get_hook_script_response_404 import GetHookScriptResponse404
from ...models.rest_hook_script import RestHookScript
from ...types import Response


def _get_kwargs(
    script_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/hook-scripts/{script_id}".format(
            script_id=quote(str(script_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetHookScriptResponse401 | GetHookScriptResponse404 | RestHookScript | None:
    if response.status_code == 200:
        response_200 = RestHookScript.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetHookScriptResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetHookScriptResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetHookScriptResponse401 | GetHookScriptResponse404 | RestHookScript]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    script_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetHookScriptResponse401 | GetHookScriptResponse404 | RestHookScript]:
    """Get a hook script

     Retrieves a hook script by ID.

    Args:
        script_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetHookScriptResponse401 | GetHookScriptResponse404 | RestHookScript]
    """

    kwargs = _get_kwargs(
        script_id=script_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    script_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetHookScriptResponse401 | GetHookScriptResponse404 | RestHookScript | None:
    """Get a hook script

     Retrieves a hook script by ID.

    Args:
        script_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetHookScriptResponse401 | GetHookScriptResponse404 | RestHookScript
    """

    return sync_detailed(
        script_id=script_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    script_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetHookScriptResponse401 | GetHookScriptResponse404 | RestHookScript]:
    """Get a hook script

     Retrieves a hook script by ID.

    Args:
        script_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetHookScriptResponse401 | GetHookScriptResponse404 | RestHookScript]
    """

    kwargs = _get_kwargs(
        script_id=script_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    script_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetHookScriptResponse401 | GetHookScriptResponse404 | RestHookScript | None:
    """Get a hook script

     Retrieves a hook script by ID.

    Args:
        script_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetHookScriptResponse401 | GetHookScriptResponse404 | RestHookScript
    """

    return (
        await asyncio_detailed(
            script_id=script_id,
            client=client,
        )
    ).parsed
