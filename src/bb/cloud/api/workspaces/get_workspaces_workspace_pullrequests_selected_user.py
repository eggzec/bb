from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.get_workspaces_workspace_pullrequests_selected_user_state import (
    GetWorkspacesWorkspacePullrequestsSelectedUserState,
)
from ...models.paginated_pull_requests import PaginatedPullRequests
from ...types import UNSET, Response, Unset

__all__ = [
    "sync_detailed",
    "asyncio_detailed",
    "sync",
    "asyncio",
]


def _get_kwargs(
    workspace: str,
    selected_user: str,
    *,
    state: GetWorkspacesWorkspacePullrequestsSelectedUserState | Unset = UNSET,
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_state: str | Unset = UNSET
    if not isinstance(state, Unset):
        json_state = state.value

    params["state"] = json_state

    params["page"] = page

    params["pagelen"] = pagelen

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/workspaces/{workspace}/pullrequests/{selected_user}".format(
            workspace=quote(str(workspace), safe=""),
            selected_user=quote(str(selected_user), safe=""),
        ),
        "params": params,
    }

    return _kwargs


type ParsedPayload = Error | PaginatedPullRequests
type ParseResult = Error | PaginatedPullRequests | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_200 = PaginatedPullRequests.from_dict(response.json())

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


def sync_detailed(
    workspace: str,
    selected_user: str,
    *,
    client: AuthenticatedClient,
    state: GetWorkspacesWorkspacePullrequestsSelectedUserState | Unset = UNSET,
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> Response[ParsedPayload]:
    """List workspace pull requests for a user

     Returns all workspace pull requests authored by the specified user.

    By default only open pull requests are returned. This can be controlled
    using the `state` query parameter. To retrieve pull requests that are
    in one of multiple states, repeat the `state` parameter for each
    individual state.

    This endpoint also supports filtering and sorting of the results. See
    [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for more details.

    Args:
        workspace (str):
        selected_user (str):
        state (GetWorkspacesWorkspacePullrequestsSelectedUserState | Unset):
        page (int | Unset):  Default: 1.
        pagelen (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PaginatedPullRequests]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        selected_user=selected_user,
        state=state,
        page=page,
        pagelen=pagelen,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    selected_user: str,
    *,
    client: AuthenticatedClient,
    state: GetWorkspacesWorkspacePullrequestsSelectedUserState | Unset = UNSET,
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> ParsedPayload | None:
    """List workspace pull requests for a user

     Returns all workspace pull requests authored by the specified user.

    By default only open pull requests are returned. This can be controlled
    using the `state` query parameter. To retrieve pull requests that are
    in one of multiple states, repeat the `state` parameter for each
    individual state.

    This endpoint also supports filtering and sorting of the results. See
    [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for more details.

    Args:
        workspace (str):
        selected_user (str):
        state (GetWorkspacesWorkspacePullrequestsSelectedUserState | Unset):
        page (int | Unset):  Default: 1.
        pagelen (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PaginatedPullRequests
    """

    return sync_detailed(
        workspace=workspace,
        selected_user=selected_user,
        client=client,
        state=state,
        page=page,
        pagelen=pagelen,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    selected_user: str,
    *,
    client: AuthenticatedClient,
    state: GetWorkspacesWorkspacePullrequestsSelectedUserState | Unset = UNSET,
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> Response[ParsedPayload]:
    """List workspace pull requests for a user

     Returns all workspace pull requests authored by the specified user.

    By default only open pull requests are returned. This can be controlled
    using the `state` query parameter. To retrieve pull requests that are
    in one of multiple states, repeat the `state` parameter for each
    individual state.

    This endpoint also supports filtering and sorting of the results. See
    [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for more details.

    Args:
        workspace (str):
        selected_user (str):
        state (GetWorkspacesWorkspacePullrequestsSelectedUserState | Unset):
        page (int | Unset):  Default: 1.
        pagelen (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PaginatedPullRequests]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        selected_user=selected_user,
        state=state,
        page=page,
        pagelen=pagelen,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    selected_user: str,
    *,
    client: AuthenticatedClient,
    state: GetWorkspacesWorkspacePullrequestsSelectedUserState | Unset = UNSET,
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> ParsedPayload | None:
    """List workspace pull requests for a user

     Returns all workspace pull requests authored by the specified user.

    By default only open pull requests are returned. This can be controlled
    using the `state` query parameter. To retrieve pull requests that are
    in one of multiple states, repeat the `state` parameter for each
    individual state.

    This endpoint also supports filtering and sorting of the results. See
    [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for more details.

    Args:
        workspace (str):
        selected_user (str):
        state (GetWorkspacesWorkspacePullrequestsSelectedUserState | Unset):
        page (int | Unset):  Default: 1.
        pagelen (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PaginatedPullRequests
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            selected_user=selected_user,
            client=client,
            state=state,
            page=page,
            pagelen=pagelen,
        )
    ).parsed
