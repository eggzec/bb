from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_hook_script_response_400 import CreateHookScriptResponse400
from ...models.create_hook_script_response_401 import CreateHookScriptResponse401
from ...models.example_post_multipart_form_data import ExamplePostMultipartFormData
from ...models.rest_hook_script import RestHookScript
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ExamplePostMultipartFormData | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/latest/hook-scripts",
    }

    if not isinstance(body, Unset):
        _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateHookScriptResponse400 | CreateHookScriptResponse401 | RestHookScript | None:
    if response.status_code == 200:
        response_200 = RestHookScript.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CreateHookScriptResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = CreateHookScriptResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateHookScriptResponse400 | CreateHookScriptResponse401 | RestHookScript]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ExamplePostMultipartFormData | Unset = UNSET,
) -> Response[CreateHookScriptResponse400 | CreateHookScriptResponse401 | RestHookScript]:
    """Create a new hook script

     Create a new hook script.

    This endpoint requires **SYS_ADMIN** permission.

    Args:
        body (ExamplePostMultipartFormData | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateHookScriptResponse400 | CreateHookScriptResponse401 | RestHookScript]
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
    body: ExamplePostMultipartFormData | Unset = UNSET,
) -> CreateHookScriptResponse400 | CreateHookScriptResponse401 | RestHookScript | None:
    """Create a new hook script

     Create a new hook script.

    This endpoint requires **SYS_ADMIN** permission.

    Args:
        body (ExamplePostMultipartFormData | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateHookScriptResponse400 | CreateHookScriptResponse401 | RestHookScript
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ExamplePostMultipartFormData | Unset = UNSET,
) -> Response[CreateHookScriptResponse400 | CreateHookScriptResponse401 | RestHookScript]:
    """Create a new hook script

     Create a new hook script.

    This endpoint requires **SYS_ADMIN** permission.

    Args:
        body (ExamplePostMultipartFormData | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateHookScriptResponse400 | CreateHookScriptResponse401 | RestHookScript]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ExamplePostMultipartFormData | Unset = UNSET,
) -> CreateHookScriptResponse400 | CreateHookScriptResponse401 | RestHookScript | None:
    """Create a new hook script

     Create a new hook script.

    This endpoint requires **SYS_ADMIN** permission.

    Args:
        body (ExamplePostMultipartFormData | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateHookScriptResponse400 | CreateHookScriptResponse401 | RestHookScript
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
