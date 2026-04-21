from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.paginated_pipeline_variables import PaginatedPipelineVariables
from ...types import Response

__all__ = [
    "sync_detailed",
    "asyncio_detailed",
    "sync",
    "asyncio",
]


def _get_kwargs(
    selected_user: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users/{selected_user}/pipelines_config/variables".format(
            selected_user=quote(str(selected_user), safe=""),
        ),
    }

    return _kwargs


type ParsedPayload = Error | PaginatedPipelineVariables
type ParseResult = Error | PaginatedPipelineVariables | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_200 = PaginatedPipelineVariables.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_403 = Error.from_dict(response.json())

        return response_403

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


def sync_detailed(
    selected_user: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """List variables for a user

     Find user level variables.
    This endpoint has been deprecated, and you should use the new workspaces endpoint. For more
    information, see [the announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-
    teams-deprecation/).

    Args:
        selected_user (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PaginatedPipelineVariables]
    """

    kwargs = _get_kwargs(
        selected_user=selected_user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    selected_user: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    """List variables for a user

     Find user level variables.
    This endpoint has been deprecated, and you should use the new workspaces endpoint. For more
    information, see [the announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-
    teams-deprecation/).

    Args:
        selected_user (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PaginatedPipelineVariables
    """

    return sync_detailed(
        selected_user=selected_user,
        client=client,
    ).parsed


async def asyncio_detailed(
    selected_user: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """List variables for a user

     Find user level variables.
    This endpoint has been deprecated, and you should use the new workspaces endpoint. For more
    information, see [the announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-
    teams-deprecation/).

    Args:
        selected_user (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PaginatedPipelineVariables]
    """

    kwargs = _get_kwargs(
        selected_user=selected_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    selected_user: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    """List variables for a user

     Find user level variables.
    This endpoint has been deprecated, and you should use the new workspaces endpoint. For more
    information, see [the announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-
    teams-deprecation/).

    Args:
        selected_user (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PaginatedPipelineVariables
    """

    return (
        await asyncio_detailed(
            selected_user=selected_user,
            client=client,
        )
    ).parsed
