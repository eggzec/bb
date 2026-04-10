from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_users_2_response_400 import GetUsers2Response400
from ...models.get_users_2_response_401 import GetUsers2Response401
from ...models.rest_application_user import RestApplicationUser
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    filter_: str | Unset = UNSET,
    permission_n: str | Unset = UNSET,
    permission: str | Unset = UNSET,
    group: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["filter"] = filter_

    params["permission.N"] = permission_n

    params["permission"] = permission

    params["group"] = group

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/users",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetUsers2Response400 | GetUsers2Response401 | RestApplicationUser | None:
    if response.status_code == 200:
        response_200 = RestApplicationUser.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetUsers2Response400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetUsers2Response401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetUsers2Response400 | GetUsers2Response401 | RestApplicationUser]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    filter_: str | Unset = UNSET,
    permission_n: str | Unset = UNSET,
    permission: str | Unset = UNSET,
    group: str | Unset = UNSET,
) -> Response[GetUsers2Response400 | GetUsers2Response401 | RestApplicationUser]:
    """Get all users

     Retrieve a page of users, optionally run through provided filters.


    Only authenticated users may call this resource.
    ### Permission Filters


    The following three sub-sections list parameters supported for permission filters (where
    <code>[root]</code> is
    the root permission filter name, e.g. <code>permission</code>, <code>permission.1</code> etc.)
    depending on the
    permission resource. The system determines which filter to apply (Global, Project or Repository
    permission)
    based on the `[root]` permission value. E.g. <code>ADMIN</code> is a global permission,
    <code>PROJECT_ADMIN</code> is a project permission and <code>REPO_ADMIN</code> is a repository
    permission. Note
    that the parameters for a given resource will be looked up in the order as they are listed below,
    that is e.g.
    for a project resource, if both <code>projectId</code> and <code>projectKey</code> are provided, the
    system will
    use <code>projectId</code> for the lookup.
    <h4>Global permissions</h4>


    The permission value under <code>[root]</code> is the only required and recognized parameter, as
    global
    permissions do not apply to a specific resource.


    Example valid filter: <code>permission=ADMIN</code>.
    <h4>Project permissions</h4>


    - <code>[root]</code>- specifies the project permission
    - <code>[root].projectId</code> - specifies the project ID to lookup the project by
    - <code>[root].projectKey</code> - specifies the project key to lookup the project by


    Example valid filter:
    <code>permission.1=PROJECT_ADMIN&amp;permission.1.projectKey=TEST_PROJECT</code>.
    #### Repository permissions


    - <code>[root]</code>- specifies the repository permission
    - <code>[root].projectId</code> - specifies the repository ID to lookup the repository by
    - <code>[root].projectKey</code> and <code>[root].repositorySlug</code>- specifies the project key
    and     repository slug to lookup the repository by; both values <i>need to</i> be provided for this
    look up to be     triggered


    Example valid filter: <code>permission.2=REPO_ADMIN&amp;permission.2.projectKey=TEST_PROJECT&amp;per
    mission.2.repositorySlug=test_repo</code>.

    Args:
        filter_ (str | Unset):
        permission_n (str | Unset):
        permission (str | Unset):
        group (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUsers2Response400 | GetUsers2Response401 | RestApplicationUser]
    """

    kwargs = _get_kwargs(
        filter_=filter_,
        permission_n=permission_n,
        permission=permission,
        group=group,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    filter_: str | Unset = UNSET,
    permission_n: str | Unset = UNSET,
    permission: str | Unset = UNSET,
    group: str | Unset = UNSET,
) -> GetUsers2Response400 | GetUsers2Response401 | RestApplicationUser | None:
    """Get all users

     Retrieve a page of users, optionally run through provided filters.


    Only authenticated users may call this resource.
    ### Permission Filters


    The following three sub-sections list parameters supported for permission filters (where
    <code>[root]</code> is
    the root permission filter name, e.g. <code>permission</code>, <code>permission.1</code> etc.)
    depending on the
    permission resource. The system determines which filter to apply (Global, Project or Repository
    permission)
    based on the `[root]` permission value. E.g. <code>ADMIN</code> is a global permission,
    <code>PROJECT_ADMIN</code> is a project permission and <code>REPO_ADMIN</code> is a repository
    permission. Note
    that the parameters for a given resource will be looked up in the order as they are listed below,
    that is e.g.
    for a project resource, if both <code>projectId</code> and <code>projectKey</code> are provided, the
    system will
    use <code>projectId</code> for the lookup.
    <h4>Global permissions</h4>


    The permission value under <code>[root]</code> is the only required and recognized parameter, as
    global
    permissions do not apply to a specific resource.


    Example valid filter: <code>permission=ADMIN</code>.
    <h4>Project permissions</h4>


    - <code>[root]</code>- specifies the project permission
    - <code>[root].projectId</code> - specifies the project ID to lookup the project by
    - <code>[root].projectKey</code> - specifies the project key to lookup the project by


    Example valid filter:
    <code>permission.1=PROJECT_ADMIN&amp;permission.1.projectKey=TEST_PROJECT</code>.
    #### Repository permissions


    - <code>[root]</code>- specifies the repository permission
    - <code>[root].projectId</code> - specifies the repository ID to lookup the repository by
    - <code>[root].projectKey</code> and <code>[root].repositorySlug</code>- specifies the project key
    and     repository slug to lookup the repository by; both values <i>need to</i> be provided for this
    look up to be     triggered


    Example valid filter: <code>permission.2=REPO_ADMIN&amp;permission.2.projectKey=TEST_PROJECT&amp;per
    mission.2.repositorySlug=test_repo</code>.

    Args:
        filter_ (str | Unset):
        permission_n (str | Unset):
        permission (str | Unset):
        group (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUsers2Response400 | GetUsers2Response401 | RestApplicationUser
    """

    return sync_detailed(
        client=client,
        filter_=filter_,
        permission_n=permission_n,
        permission=permission,
        group=group,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    filter_: str | Unset = UNSET,
    permission_n: str | Unset = UNSET,
    permission: str | Unset = UNSET,
    group: str | Unset = UNSET,
) -> Response[GetUsers2Response400 | GetUsers2Response401 | RestApplicationUser]:
    """Get all users

     Retrieve a page of users, optionally run through provided filters.


    Only authenticated users may call this resource.
    ### Permission Filters


    The following three sub-sections list parameters supported for permission filters (where
    <code>[root]</code> is
    the root permission filter name, e.g. <code>permission</code>, <code>permission.1</code> etc.)
    depending on the
    permission resource. The system determines which filter to apply (Global, Project or Repository
    permission)
    based on the `[root]` permission value. E.g. <code>ADMIN</code> is a global permission,
    <code>PROJECT_ADMIN</code> is a project permission and <code>REPO_ADMIN</code> is a repository
    permission. Note
    that the parameters for a given resource will be looked up in the order as they are listed below,
    that is e.g.
    for a project resource, if both <code>projectId</code> and <code>projectKey</code> are provided, the
    system will
    use <code>projectId</code> for the lookup.
    <h4>Global permissions</h4>


    The permission value under <code>[root]</code> is the only required and recognized parameter, as
    global
    permissions do not apply to a specific resource.


    Example valid filter: <code>permission=ADMIN</code>.
    <h4>Project permissions</h4>


    - <code>[root]</code>- specifies the project permission
    - <code>[root].projectId</code> - specifies the project ID to lookup the project by
    - <code>[root].projectKey</code> - specifies the project key to lookup the project by


    Example valid filter:
    <code>permission.1=PROJECT_ADMIN&amp;permission.1.projectKey=TEST_PROJECT</code>.
    #### Repository permissions


    - <code>[root]</code>- specifies the repository permission
    - <code>[root].projectId</code> - specifies the repository ID to lookup the repository by
    - <code>[root].projectKey</code> and <code>[root].repositorySlug</code>- specifies the project key
    and     repository slug to lookup the repository by; both values <i>need to</i> be provided for this
    look up to be     triggered


    Example valid filter: <code>permission.2=REPO_ADMIN&amp;permission.2.projectKey=TEST_PROJECT&amp;per
    mission.2.repositorySlug=test_repo</code>.

    Args:
        filter_ (str | Unset):
        permission_n (str | Unset):
        permission (str | Unset):
        group (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUsers2Response400 | GetUsers2Response401 | RestApplicationUser]
    """

    kwargs = _get_kwargs(
        filter_=filter_,
        permission_n=permission_n,
        permission=permission,
        group=group,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    filter_: str | Unset = UNSET,
    permission_n: str | Unset = UNSET,
    permission: str | Unset = UNSET,
    group: str | Unset = UNSET,
) -> GetUsers2Response400 | GetUsers2Response401 | RestApplicationUser | None:
    """Get all users

     Retrieve a page of users, optionally run through provided filters.


    Only authenticated users may call this resource.
    ### Permission Filters


    The following three sub-sections list parameters supported for permission filters (where
    <code>[root]</code> is
    the root permission filter name, e.g. <code>permission</code>, <code>permission.1</code> etc.)
    depending on the
    permission resource. The system determines which filter to apply (Global, Project or Repository
    permission)
    based on the `[root]` permission value. E.g. <code>ADMIN</code> is a global permission,
    <code>PROJECT_ADMIN</code> is a project permission and <code>REPO_ADMIN</code> is a repository
    permission. Note
    that the parameters for a given resource will be looked up in the order as they are listed below,
    that is e.g.
    for a project resource, if both <code>projectId</code> and <code>projectKey</code> are provided, the
    system will
    use <code>projectId</code> for the lookup.
    <h4>Global permissions</h4>


    The permission value under <code>[root]</code> is the only required and recognized parameter, as
    global
    permissions do not apply to a specific resource.


    Example valid filter: <code>permission=ADMIN</code>.
    <h4>Project permissions</h4>


    - <code>[root]</code>- specifies the project permission
    - <code>[root].projectId</code> - specifies the project ID to lookup the project by
    - <code>[root].projectKey</code> - specifies the project key to lookup the project by


    Example valid filter:
    <code>permission.1=PROJECT_ADMIN&amp;permission.1.projectKey=TEST_PROJECT</code>.
    #### Repository permissions


    - <code>[root]</code>- specifies the repository permission
    - <code>[root].projectId</code> - specifies the repository ID to lookup the repository by
    - <code>[root].projectKey</code> and <code>[root].repositorySlug</code>- specifies the project key
    and     repository slug to lookup the repository by; both values <i>need to</i> be provided for this
    look up to be     triggered


    Example valid filter: <code>permission.2=REPO_ADMIN&amp;permission.2.projectKey=TEST_PROJECT&amp;per
    mission.2.repositorySlug=test_repo</code>.

    Args:
        filter_ (str | Unset):
        permission_n (str | Unset):
        permission (str | Unset):
        group (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUsers2Response400 | GetUsers2Response401 | RestApplicationUser
    """

    return (
        await asyncio_detailed(
            client=client,
            filter_=filter_,
            permission_n=permission_n,
            permission=permission,
            group=group,
        )
    ).parsed
