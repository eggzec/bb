from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...deprecation import deprecated_endpoint
from ...models.component import Component
from ...models.error import Error
from ...types import Response

__all__ = [
    "sync_detailed",
    "asyncio_detailed",
    "sync",
    "asyncio",
]


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    component_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/repositories/{workspace}/{repo_slug}/components/{component_id}".format(
            workspace=quote(str(workspace), safe=""),
            repo_slug=quote(str(repo_slug), safe=""),
            component_id=quote(str(component_id), safe=""),
        ),
    }

    return _kwargs


type ParsedPayload = Component | Error
type ParseResult = Component | Error | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_200 = Component.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_404 = Error.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ParsedPayload]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated_endpoint(None)
def sync_detailed(
    workspace: str,
    repo_slug: str,
    component_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """Get a component for issues

     Returns the specified issue tracker component object.

    Args:
        workspace (str):
        repo_slug (str):
        component_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Component | Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        component_id=component_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated_endpoint(None)
def sync(
    workspace: str,
    repo_slug: str,
    component_id: int,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    """Get a component for issues

     Returns the specified issue tracker component object.

    Args:
        workspace (str):
        repo_slug (str):
        component_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Component | Error
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        component_id=component_id,
        client=client,
    ).parsed


@deprecated_endpoint(None)
async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    component_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """Get a component for issues

     Returns the specified issue tracker component object.

    Args:
        workspace (str):
        repo_slug (str):
        component_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Component | Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        component_id=component_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated_endpoint(None)
async def asyncio(
    workspace: str,
    repo_slug: str,
    component_id: int,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    """Get a component for issues

     Returns the specified issue tracker component object.

    Args:
        workspace (str):
        repo_slug (str):
        component_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Component | Error
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            component_id=component_id,
            client=client,
        )
    ).parsed
