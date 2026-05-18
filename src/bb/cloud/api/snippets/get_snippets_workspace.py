from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.get_snippets_workspace_role import GetSnippetsWorkspaceRole
from ...models.paginated_snippets import PaginatedSnippets
from ...types import UNSET, Response, Unset

__all__ = [
    "sync_detailed",
    "asyncio_detailed",
    "sync",
    "asyncio",
]


def _get_kwargs(
    workspace: str,
    *,
    role: GetSnippetsWorkspaceRole | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_role: str | Unset = UNSET
    if not isinstance(role, Unset):
        json_role = role.value

    params["role"] = json_role

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/snippets/{workspace}".format(
            workspace=quote(str(workspace), safe=""),
        ),
        "params": params,
    }

    return _kwargs


type ParsedPayload = Error | PaginatedSnippets
type ParseResult = Error | PaginatedSnippets | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_200 = PaginatedSnippets.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_403 = Error.from_dict(response.json())

        return response_403

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


def sync_detailed(
    workspace: str,
    *,
    client: AuthenticatedClient,
    role: GetSnippetsWorkspaceRole | Unset = UNSET,
) -> Response[ParsedPayload]:
    """List snippets in a workspace

     Identical to [`/snippets`](/cloud/bitbucket/rest/api-group-snippets/#api-snippets-get), except that
    the result is further filtered
    by the snippet owner and only those that are owned by `{workspace}` are
    returned.

    Args:
        workspace (str):
        role (GetSnippetsWorkspaceRole | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PaginatedSnippets]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        role=role,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    *,
    client: AuthenticatedClient,
    role: GetSnippetsWorkspaceRole | Unset = UNSET,
) -> ParsedPayload | None:
    """List snippets in a workspace

     Identical to [`/snippets`](/cloud/bitbucket/rest/api-group-snippets/#api-snippets-get), except that
    the result is further filtered
    by the snippet owner and only those that are owned by `{workspace}` are
    returned.

    Args:
        workspace (str):
        role (GetSnippetsWorkspaceRole | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PaginatedSnippets
    """

    return sync_detailed(
        workspace=workspace,
        client=client,
        role=role,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    *,
    client: AuthenticatedClient,
    role: GetSnippetsWorkspaceRole | Unset = UNSET,
) -> Response[ParsedPayload]:
    """List snippets in a workspace

     Identical to [`/snippets`](/cloud/bitbucket/rest/api-group-snippets/#api-snippets-get), except that
    the result is further filtered
    by the snippet owner and only those that are owned by `{workspace}` are
    returned.

    Args:
        workspace (str):
        role (GetSnippetsWorkspaceRole | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PaginatedSnippets]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        role=role,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    *,
    client: AuthenticatedClient,
    role: GetSnippetsWorkspaceRole | Unset = UNSET,
) -> ParsedPayload | None:
    """List snippets in a workspace

     Identical to [`/snippets`](/cloud/bitbucket/rest/api-group-snippets/#api-snippets-get), except that
    the result is further filtered
    by the snippet owner and only those that are owned by `{workspace}` are
    returned.

    Args:
        workspace (str):
        role (GetSnippetsWorkspaceRole | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PaginatedSnippets
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            client=client,
            role=role,
        )
    ).parsed
