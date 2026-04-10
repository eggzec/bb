from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.read_response_401 import ReadResponse401
from ...models.read_response_404 import ReadResponse404
from ...types import Response


def _get_kwargs(
    script_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/hook-scripts/{script_id}/content".format(
            script_id=quote(str(script_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ReadResponse401 | ReadResponse404 | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 401:
        response_401 = ReadResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ReadResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ReadResponse401 | ReadResponse404]:
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
) -> Response[Any | ReadResponse401 | ReadResponse404]:
    """Get hook script content

     Retrieves the hook script content.

    This endpoint requires **SYS_ADMIN** permission.

    Args:
        script_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ReadResponse401 | ReadResponse404]
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
) -> Any | ReadResponse401 | ReadResponse404 | None:
    """Get hook script content

     Retrieves the hook script content.

    This endpoint requires **SYS_ADMIN** permission.

    Args:
        script_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ReadResponse401 | ReadResponse404
    """

    return sync_detailed(
        script_id=script_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    script_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | ReadResponse401 | ReadResponse404]:
    """Get hook script content

     Retrieves the hook script content.

    This endpoint requires **SYS_ADMIN** permission.

    Args:
        script_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ReadResponse401 | ReadResponse404]
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
) -> Any | ReadResponse401 | ReadResponse404 | None:
    """Get hook script content

     Retrieves the hook script content.

    This endpoint requires **SYS_ADMIN** permission.

    Args:
        script_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ReadResponse401 | ReadResponse404
    """

    return (
        await asyncio_detailed(
            script_id=script_id,
            client=client,
        )
    ).parsed
