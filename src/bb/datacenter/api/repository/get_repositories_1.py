from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_repositories_1_permission import GetRepositories1Permission
from ...models.get_repositories_1_response_200 import GetRepositories1Response200
from ...models.get_repositories_1_response_400 import GetRepositories1Response400
from ...models.get_repositories_1_state import GetRepositories1State
from ...models.get_repositories_1_visibility import GetRepositories1Visibility
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    archived: str | Unset = UNSET,
    projectname: str | Unset = UNSET,
    projectkey: str | Unset = UNSET,
    visibility: GetRepositories1Visibility | Unset = UNSET,
    name: str | Unset = UNSET,
    permission: GetRepositories1Permission | Unset = UNSET,
    state: GetRepositories1State | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["archived"] = archived

    params["projectname"] = projectname

    params["projectkey"] = projectkey

    json_visibility: str | Unset = UNSET
    if not isinstance(visibility, Unset):
        json_visibility = visibility.value

    params["visibility"] = json_visibility

    params["name"] = name

    json_permission: str | Unset = UNSET
    if not isinstance(permission, Unset):
        json_permission = permission.value

    params["permission"] = json_permission

    json_state: str | Unset = UNSET
    if not isinstance(state, Unset):
        json_state = state.value

    params["state"] = json_state

    params["start"] = start

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/repos",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetRepositories1Response200 | GetRepositories1Response400 | None:
    if response.status_code == 200:
        response_200 = GetRepositories1Response200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetRepositories1Response400.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetRepositories1Response200 | GetRepositories1Response400]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    archived: str | Unset = UNSET,
    projectname: str | Unset = UNSET,
    projectkey: str | Unset = UNSET,
    visibility: GetRepositories1Visibility | Unset = UNSET,
    name: str | Unset = UNSET,
    permission: GetRepositories1Permission | Unset = UNSET,
    state: GetRepositories1State | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GetRepositories1Response200 | GetRepositories1Response400]:
    """Search for repositories

     Retrieve a page of repositories based on query parameters that control the search. See the
    documentation of the parameters for more details.

    This resource is anonymously accessible, if anonymous access is enabled.

    <b>Note on permissions.</b> In absence of the <code>permission</code> query parameter the implicit
    'read' permission is assumed. Please note that this permission is lower than the <tt>REPO_READ</tt>
    permission rather than being equal to it. The implicit 'read' permission for a given repository is
    assigned to any user that has any of the higher permissions, such as <tt>REPO_READ</tt>, as well as
    to anonymous users if the repository is marked as public. The important implication of the above is
    that an anonymous request to this resource with a permission level <tt>REPO_READ</tt> is guaranteed
    to receive an empty list of repositories as a result. For anonymous requests it is therefore
    recommended to not specify the <tt>permission</tt> parameter at all.

    Args:
        archived (str | Unset):
        projectname (str | Unset):
        projectkey (str | Unset):
        visibility (GetRepositories1Visibility | Unset):
        name (str | Unset):
        permission (GetRepositories1Permission | Unset):
        state (GetRepositories1State | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRepositories1Response200 | GetRepositories1Response400]
    """

    kwargs = _get_kwargs(
        archived=archived,
        projectname=projectname,
        projectkey=projectkey,
        visibility=visibility,
        name=name,
        permission=permission,
        state=state,
        start=start,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    archived: str | Unset = UNSET,
    projectname: str | Unset = UNSET,
    projectkey: str | Unset = UNSET,
    visibility: GetRepositories1Visibility | Unset = UNSET,
    name: str | Unset = UNSET,
    permission: GetRepositories1Permission | Unset = UNSET,
    state: GetRepositories1State | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetRepositories1Response200 | GetRepositories1Response400 | None:
    """Search for repositories

     Retrieve a page of repositories based on query parameters that control the search. See the
    documentation of the parameters for more details.

    This resource is anonymously accessible, if anonymous access is enabled.

    <b>Note on permissions.</b> In absence of the <code>permission</code> query parameter the implicit
    'read' permission is assumed. Please note that this permission is lower than the <tt>REPO_READ</tt>
    permission rather than being equal to it. The implicit 'read' permission for a given repository is
    assigned to any user that has any of the higher permissions, such as <tt>REPO_READ</tt>, as well as
    to anonymous users if the repository is marked as public. The important implication of the above is
    that an anonymous request to this resource with a permission level <tt>REPO_READ</tt> is guaranteed
    to receive an empty list of repositories as a result. For anonymous requests it is therefore
    recommended to not specify the <tt>permission</tt> parameter at all.

    Args:
        archived (str | Unset):
        projectname (str | Unset):
        projectkey (str | Unset):
        visibility (GetRepositories1Visibility | Unset):
        name (str | Unset):
        permission (GetRepositories1Permission | Unset):
        state (GetRepositories1State | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRepositories1Response200 | GetRepositories1Response400
    """

    return sync_detailed(
        client=client,
        archived=archived,
        projectname=projectname,
        projectkey=projectkey,
        visibility=visibility,
        name=name,
        permission=permission,
        state=state,
        start=start,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    archived: str | Unset = UNSET,
    projectname: str | Unset = UNSET,
    projectkey: str | Unset = UNSET,
    visibility: GetRepositories1Visibility | Unset = UNSET,
    name: str | Unset = UNSET,
    permission: GetRepositories1Permission | Unset = UNSET,
    state: GetRepositories1State | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GetRepositories1Response200 | GetRepositories1Response400]:
    """Search for repositories

     Retrieve a page of repositories based on query parameters that control the search. See the
    documentation of the parameters for more details.

    This resource is anonymously accessible, if anonymous access is enabled.

    <b>Note on permissions.</b> In absence of the <code>permission</code> query parameter the implicit
    'read' permission is assumed. Please note that this permission is lower than the <tt>REPO_READ</tt>
    permission rather than being equal to it. The implicit 'read' permission for a given repository is
    assigned to any user that has any of the higher permissions, such as <tt>REPO_READ</tt>, as well as
    to anonymous users if the repository is marked as public. The important implication of the above is
    that an anonymous request to this resource with a permission level <tt>REPO_READ</tt> is guaranteed
    to receive an empty list of repositories as a result. For anonymous requests it is therefore
    recommended to not specify the <tt>permission</tt> parameter at all.

    Args:
        archived (str | Unset):
        projectname (str | Unset):
        projectkey (str | Unset):
        visibility (GetRepositories1Visibility | Unset):
        name (str | Unset):
        permission (GetRepositories1Permission | Unset):
        state (GetRepositories1State | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRepositories1Response200 | GetRepositories1Response400]
    """

    kwargs = _get_kwargs(
        archived=archived,
        projectname=projectname,
        projectkey=projectkey,
        visibility=visibility,
        name=name,
        permission=permission,
        state=state,
        start=start,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    archived: str | Unset = UNSET,
    projectname: str | Unset = UNSET,
    projectkey: str | Unset = UNSET,
    visibility: GetRepositories1Visibility | Unset = UNSET,
    name: str | Unset = UNSET,
    permission: GetRepositories1Permission | Unset = UNSET,
    state: GetRepositories1State | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetRepositories1Response200 | GetRepositories1Response400 | None:
    """Search for repositories

     Retrieve a page of repositories based on query parameters that control the search. See the
    documentation of the parameters for more details.

    This resource is anonymously accessible, if anonymous access is enabled.

    <b>Note on permissions.</b> In absence of the <code>permission</code> query parameter the implicit
    'read' permission is assumed. Please note that this permission is lower than the <tt>REPO_READ</tt>
    permission rather than being equal to it. The implicit 'read' permission for a given repository is
    assigned to any user that has any of the higher permissions, such as <tt>REPO_READ</tt>, as well as
    to anonymous users if the repository is marked as public. The important implication of the above is
    that an anonymous request to this resource with a permission level <tt>REPO_READ</tt> is guaranteed
    to receive an empty list of repositories as a result. For anonymous requests it is therefore
    recommended to not specify the <tt>permission</tt> parameter at all.

    Args:
        archived (str | Unset):
        projectname (str | Unset):
        projectkey (str | Unset):
        visibility (GetRepositories1Visibility | Unset):
        name (str | Unset):
        permission (GetRepositories1Permission | Unset):
        state (GetRepositories1State | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRepositories1Response200 | GetRepositories1Response400
    """

    return (
        await asyncio_detailed(
            client=client,
            archived=archived,
            projectname=projectname,
            projectkey=projectkey,
            visibility=visibility,
            name=name,
            permission=permission,
            state=state,
            start=start,
            limit=limit,
        )
    ).parsed
