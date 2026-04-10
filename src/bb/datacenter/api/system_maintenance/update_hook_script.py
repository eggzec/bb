from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.example_put_multipart_form_data import ExamplePutMultipartFormData
from ...models.rest_hook_script import RestHookScript
from ...models.update_hook_script_response_401 import UpdateHookScriptResponse401
from ...models.update_hook_script_response_404 import UpdateHookScriptResponse404
from ...models.update_hook_script_response_409 import UpdateHookScriptResponse409
from ...models.update_hook_script_response_422 import UpdateHookScriptResponse422
from ...types import UNSET, Response, Unset


def _get_kwargs(
    script_id: str,
    *,
    body: ExamplePutMultipartFormData | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/latest/hook-scripts/{script_id}".format(
            script_id=quote(str(script_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    RestHookScript
    | UpdateHookScriptResponse401
    | UpdateHookScriptResponse404
    | UpdateHookScriptResponse409
    | UpdateHookScriptResponse422
    | None
):
    if response.status_code == 200:
        response_200 = RestHookScript.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = UpdateHookScriptResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = UpdateHookScriptResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = UpdateHookScriptResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = UpdateHookScriptResponse422.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    RestHookScript
    | UpdateHookScriptResponse401
    | UpdateHookScriptResponse404
    | UpdateHookScriptResponse409
    | UpdateHookScriptResponse422
]:
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
    body: ExamplePutMultipartFormData | Unset = UNSET,
) -> Response[
    RestHookScript
    | UpdateHookScriptResponse401
    | UpdateHookScriptResponse404
    | UpdateHookScriptResponse409
    | UpdateHookScriptResponse422
]:
    """Update a hook script

     Updates a hook script.

    This endpoint requires **SYS_ADMIN** permission.

    Args:
        script_id (str):
        body (ExamplePutMultipartFormData | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestHookScript | UpdateHookScriptResponse401 | UpdateHookScriptResponse404 | UpdateHookScriptResponse409 | UpdateHookScriptResponse422]
    """

    kwargs = _get_kwargs(
        script_id=script_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    script_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExamplePutMultipartFormData | Unset = UNSET,
) -> (
    RestHookScript
    | UpdateHookScriptResponse401
    | UpdateHookScriptResponse404
    | UpdateHookScriptResponse409
    | UpdateHookScriptResponse422
    | None
):
    """Update a hook script

     Updates a hook script.

    This endpoint requires **SYS_ADMIN** permission.

    Args:
        script_id (str):
        body (ExamplePutMultipartFormData | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestHookScript | UpdateHookScriptResponse401 | UpdateHookScriptResponse404 | UpdateHookScriptResponse409 | UpdateHookScriptResponse422
    """

    return sync_detailed(
        script_id=script_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    script_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExamplePutMultipartFormData | Unset = UNSET,
) -> Response[
    RestHookScript
    | UpdateHookScriptResponse401
    | UpdateHookScriptResponse404
    | UpdateHookScriptResponse409
    | UpdateHookScriptResponse422
]:
    """Update a hook script

     Updates a hook script.

    This endpoint requires **SYS_ADMIN** permission.

    Args:
        script_id (str):
        body (ExamplePutMultipartFormData | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestHookScript | UpdateHookScriptResponse401 | UpdateHookScriptResponse404 | UpdateHookScriptResponse409 | UpdateHookScriptResponse422]
    """

    kwargs = _get_kwargs(
        script_id=script_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    script_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExamplePutMultipartFormData | Unset = UNSET,
) -> (
    RestHookScript
    | UpdateHookScriptResponse401
    | UpdateHookScriptResponse404
    | UpdateHookScriptResponse409
    | UpdateHookScriptResponse422
    | None
):
    """Update a hook script

     Updates a hook script.

    This endpoint requires **SYS_ADMIN** permission.

    Args:
        script_id (str):
        body (ExamplePutMultipartFormData | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestHookScript | UpdateHookScriptResponse401 | UpdateHookScriptResponse404 | UpdateHookScriptResponse409 | UpdateHookScriptResponse422
    """

    return (
        await asyncio_detailed(
            script_id=script_id,
            client=client,
            body=body,
        )
    ).parsed
