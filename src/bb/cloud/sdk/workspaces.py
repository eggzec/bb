from __future__ import annotations

from typing import Any

from bb.cloud.api.workspaces import (
    get_user_permissions_workspaces,
    get_user_workspaces,
    get_user_workspaces_workspace_permission,
    get_workspaces,
    get_workspaces_workspace,
    get_workspaces_workspace_members,
    get_workspaces_workspace_members_member,
    get_workspaces_workspace_permissions,
    get_workspaces_workspace_permissions_repositories,
    get_workspaces_workspace_permissions_repositories_repo_slug,
    get_workspaces_workspace_pullrequests_selected_user,
    get_workspaces_workspace_settings_gpg_public_key,
)
from bb.cloud.models.error import Error
from bb.cloud.models.workspace import Workspace
from bb.cloud.sdk._auth_validation import AuthMethod, require_auth
from bb.cloud.sdk._client import BBClient
from bb.cloud.sdk._pagination import async_paginate

__all__ = [
    "list",
    "get",
    "members",
    "get_member",
    "permissions",
    "repo_permissions",
    "get_repo_permission",
    "user_prs",
    "gpg_key",
    "mine",
    "my_permissions",
    "my_permission",
]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def list(
    client: BBClient,
    *,
    pagelen: int = 25,
) -> list[Workspace] | Error:
    """List all workspaces the authenticated user belongs to.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        pagelen: Number of results per page. Defaults to ``25``.

    Returns:
        All workspaces the authenticated user is a member of, across all pages.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import workspaces

        client = BBClient.from_env()
        all_workspaces = await workspaces.list(client)
        ```

    References:
        `GET /2.0/workspaces
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-workspaces/#api-workspaces-get>`_
    """
    result = await async_paginate(
        get_workspaces.asyncio,
        client=client.auth,
        pagelen=pagelen,
    )

    if isinstance(result, Error):
        return result

    return [item for item in result if isinstance(item, Workspace)]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get(client: BBClient, workspace: str) -> Workspace | Error | None:
    """Fetch a single workspace by slug.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.

    Returns:
        The :class:`~bb.cloud.models.workspace.Workspace` object, or ``None`` if not found.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import workspaces

        client = BBClient.from_env()
        ws = await workspaces.get(client, workspace="myworkspace")
        ```

    References:
        `GET /2.0/workspaces/{workspace}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-workspaces/#api-workspaces-workspace-get>`_
    """
    result = await get_workspaces_workspace.asyncio(workspace, client=client.auth)
    if isinstance(result, (Workspace, Error)):
        return result
    return None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def members(client: BBClient, workspace: str, *, pagelen: int = 25) -> list[Any] | Error:
    """List all members of a workspace.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        pagelen: Number of results per page. Defaults to ``25``.

    Returns:
        All member entries for the workspace across all pages.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import workspaces

        client = BBClient.from_env()
        all_members = await workspaces.members(client, workspace="myworkspace")
        ```

    References:
        `GET /2.0/workspaces/{workspace}/members
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-workspaces/#api-workspaces-workspace-members-get>`_
    """
    result = await async_paginate(
        get_workspaces_workspace_members.asyncio,
        workspace,
        client=client.auth,
        pagelen=pagelen,
    )

    if isinstance(result, Error):
        return result

    return [x for x in result]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get_member(client: BBClient, workspace: str, member: str) -> Any | Error | None:
    """Fetch a specific member of a workspace.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        member: The member's account UUID (with surrounding braces, e.g. ``{abc-123}``).

    Returns:
        The member object, or ``None`` if not found.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import workspaces

        client = BBClient.from_env()
        member = await workspaces.get_member(client, workspace="myworkspace", member="{abc-123}")
        ```

    References:
        `GET /2.0/workspaces/{workspace}/members/{member}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-workspaces/#api-workspaces-workspace-members-member-get>`_
    """
    return await get_workspaces_workspace_members_member.asyncio(workspace, member, client=client.auth)


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def permissions(client: BBClient, workspace: str, *, pagelen: int = 25) -> list[Any] | Error:
    """List all member permissions for a workspace.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        pagelen: Number of results per page. Defaults to ``25``.

    Returns:
        All workspace permission entries across all pages.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import workspaces

        client = BBClient.from_env()
        perms = await workspaces.permissions(client, workspace="myworkspace")
        ```

    References:
        `GET /2.0/workspaces/{workspace}/permissions
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-workspaces/#api-workspaces-workspace-permissions-get>`_
    """
    result = await async_paginate(
        get_workspaces_workspace_permissions.asyncio,
        workspace,
        client=client.auth,
        pagelen=pagelen,
    )

    if isinstance(result, Error):
        return result

    return [x for x in result]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def repo_permissions(client: BBClient, workspace: str, *, pagelen: int = 25) -> list[Any] | Error:
    """List repository-level permissions for all members in a workspace.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        pagelen: Number of results per page. Defaults to ``25``.

    Returns:
        All repository permission entries for the workspace across all pages.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import workspaces

        client = BBClient.from_env()
        perms = await workspaces.repo_permissions(client, workspace="myworkspace")
        ```

    References:
        `GET /2.0/workspaces/{workspace}/permissions/repositories
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-workspaces/#api-workspaces-workspace-permissions-repositories-get>`_
    """
    result = await async_paginate(
        get_workspaces_workspace_permissions_repositories.asyncio,
        workspace,
        client=client.auth,
        pagelen=pagelen,
    )

    if isinstance(result, Error):
        return result

    return [x for x in result]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get_repo_permission(
    client: BBClient, workspace: str, repo_slug: str, *, pagelen: int = 25
) -> list[Any] | Error:
    """List all user permissions for a specific repository within a workspace.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        repo_slug: Repository slug or UUID.
        pagelen: Number of results per page. Defaults to ``25``.

    Returns:
        List of repository permission objects, or ``Error`` on failure.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import workspaces

        client = BBClient.from_env()
        perms = await workspaces.get_repo_permission(
            client, workspace="myworkspace", repo_slug="myrepo"
        )
        ```

    References:
        `GET /2.0/workspaces/{workspace}/permissions/repositories/{repo_slug}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-workspaces/#api-workspaces-workspace-permissions-repositories-repo-slug-get>`_
    """
    result = await async_paginate(
        get_workspaces_workspace_permissions_repositories_repo_slug.asyncio,
        workspace,
        repo_slug,
        client=client.auth,
        pagelen=pagelen,
    )
    if isinstance(result, Error):
        return result
    return [x for x in result]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def user_prs(client: BBClient, workspace: str, selected_user: str, *, pagelen: int = 25) -> list[Any] | Error:
    """List pull requests authored by a specific user in a workspace.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        selected_user: The user's account UUID (with surrounding braces, e.g. ``{abc-123}``)
            or username.
        pagelen: Number of results per page. Defaults to ``25``.

    Returns:
        All pull requests by the specified user in the workspace across all pages.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import workspaces

        client = BBClient.from_env()
        prs = await workspaces.user_prs(
            client, workspace="myworkspace", selected_user="{abc-123}"
        )
        ```

    References:
        `GET /2.0/workspaces/{workspace}/pullrequests/{selected_user}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-workspaces/#api-workspaces-workspace-pullrequests-selected-user-get>`_
    """
    result = await async_paginate(
        get_workspaces_workspace_pullrequests_selected_user.asyncio,
        workspace,
        selected_user,
        client=client.auth,
        pagelen=pagelen,
    )

    if isinstance(result, Error):
        return result

    return [x for x in result]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def gpg_key(client: BBClient, workspace: str) -> Any | Error | None:
    """Fetch the GPG public key for a workspace.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.

    Returns:
        The GPG public key object, or ``None`` if not configured.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import workspaces

        client = BBClient.from_env()
        key = await workspaces.gpg_key(client, workspace="myworkspace")
        ```

    References:
        `GET /2.0/workspaces/{workspace}/settings/gpg-public-key
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-workspaces/#api-workspaces-workspace-settings-gpg-public-key-get>`_
    """
    return await get_workspaces_workspace_settings_gpg_public_key.asyncio(workspace, client=client.auth)


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def mine(client: BBClient, *, pagelen: int = 25) -> list[Workspace] | Error:
    """List the authenticated user's workspaces via the /user endpoint.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        pagelen: Number of results per page. Defaults to ``25``.

    Returns:
        All workspaces belonging to the authenticated user across all pages.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import workspaces

        client = BBClient.from_env()
        my_workspaces = await workspaces.mine(client)
        ```

    References:
        `GET /2.0/user/workspaces
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-workspaces/#api-user-workspaces-get>`_
    """
    result = await async_paginate(
        get_user_workspaces.asyncio,
        client=client.auth,
        pagelen=pagelen,
    )

    if isinstance(result, Error):
        return result

    return [item for item in result if isinstance(item, Workspace)]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def my_permissions(client: BBClient, *, pagelen: int = 25) -> list[Any] | Error:
    """List the current user's permissions across all workspaces.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        pagelen: Number of results per page. Defaults to ``25``.

    Returns:
        All workspace permission entries for the current user across all pages.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import workspaces

        client = BBClient.from_env()
        perms = await workspaces.my_permissions(client)
        ```

    References:
        `GET /2.0/user/permissions/workspaces
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-workspaces/#api-user-permissions-workspaces-get>`_
    """
    result = await async_paginate(
        get_user_permissions_workspaces.asyncio,
        client=client.auth,
        pagelen=pagelen,
    )

    if isinstance(result, Error):
        return result

    return [x for x in result]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def my_permission(client: BBClient, workspace: str) -> Any | Error | None:
    """Fetch the current user's permission in a specific workspace.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.

    Returns:
        The current user's permission object for the workspace, or ``None`` if not found.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import workspaces

        client = BBClient.from_env()
        perm = await workspaces.my_permission(client, workspace="myworkspace")
        ```

    References:
        `GET /2.0/user/workspaces/{workspace}/permission
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-workspaces/#api-user-workspaces-workspace-permission-get>`_
    """
    return await get_user_workspaces_workspace_permission.asyncio(workspace, client=client.auth)
