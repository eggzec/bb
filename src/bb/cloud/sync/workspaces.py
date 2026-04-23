from __future__ import annotations
import asyncio
from typing import Any
from bb.cloud.models.error import Error
from bb.cloud.models.workspace import Workspace
from bb.cloud.sdk._client import BBClient
from bb.cloud.sdk import workspaces as _async
__all__ = ['list', 'get', 'members', 'get_member', 'permissions', 'repo_permissions', 'get_repo_permission', 'user_prs', 'gpg_key', 'mine', 'my_permissions', 'my_permission']

def list(client: BBClient, *, pagelen: int=25) -> list[Workspace] | Error:
    """List all workspaces the authenticated user belongs to.

Synchronous wrapper around :func:`~bb.cloud.sdk.workspaces.list`.

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
    all_workspaces = workspaces.list(client)
    ```

References:
    `GET /2.0/workspaces
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-workspaces/#api-workspaces-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.workspaces.list`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.list(client, pagelen=pagelen))

def get(client: BBClient, workspace: str) -> Workspace | Error | None:
    """Fetch a single workspace by slug.

Synchronous wrapper around :func:`~bb.cloud.sdk.workspaces.get`.

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
    ws = workspaces.get(client, workspace="myworkspace")
    ```

References:
    `GET /2.0/workspaces/{workspace}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-workspaces/#api-workspaces-workspace-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.workspaces.get`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.get(client, workspace))

def members(client: BBClient, workspace: str, *, pagelen: int=25) -> list[Any] | Error:
    """List all members of a workspace.

Synchronous wrapper around :func:`~bb.cloud.sdk.workspaces.members`.

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
    all_members = workspaces.members(client, workspace="myworkspace")
    ```

References:
    `GET /2.0/workspaces/{workspace}/members
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-workspaces/#api-workspaces-workspace-members-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.workspaces.members`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.members(client, workspace, pagelen=pagelen))

def get_member(client: BBClient, workspace: str, member: str) -> Any | Error | None:
    """Fetch a specific member of a workspace.

Synchronous wrapper around :func:`~bb.cloud.sdk.workspaces.get_member`.

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
    member = workspaces.get_member(client, workspace="myworkspace", member="{abc-123}")
    ```

References:
    `GET /2.0/workspaces/{workspace}/members/{member}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-workspaces/#api-workspaces-workspace-members-member-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.workspaces.get_member`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.get_member(client, workspace, member))

def permissions(client: BBClient, workspace: str, *, pagelen: int=25) -> list[Any] | Error:
    """List all member permissions for a workspace.

Synchronous wrapper around :func:`~bb.cloud.sdk.workspaces.permissions`.

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
    perms = workspaces.permissions(client, workspace="myworkspace")
    ```

References:
    `GET /2.0/workspaces/{workspace}/permissions
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-workspaces/#api-workspaces-workspace-permissions-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.workspaces.permissions`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.permissions(client, workspace, pagelen=pagelen))

def repo_permissions(client: BBClient, workspace: str, *, pagelen: int=25) -> list[Any] | Error:
    """List repository-level permissions for all members in a workspace.

Synchronous wrapper around :func:`~bb.cloud.sdk.workspaces.repo_permissions`.

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
    perms = workspaces.repo_permissions(client, workspace="myworkspace")
    ```

References:
    `GET /2.0/workspaces/{workspace}/permissions/repositories
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-workspaces/#api-workspaces-workspace-permissions-repositories-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.workspaces.repo_permissions`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.repo_permissions(client, workspace, pagelen=pagelen))

def get_repo_permission(client: BBClient, workspace: str, repo_slug: str) -> Any | Error | None:
    """Fetch the permission configuration for a specific repository within a workspace.

Synchronous wrapper around :func:`~bb.cloud.sdk.workspaces.get_repo_permission`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.

Returns:
    The repository permission object, or ``None`` if not found.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import workspaces

    client = BBClient.from_env()
    perm = workspaces.get_repo_permission(
        client, workspace="myworkspace", repo_slug="myrepo"
    )
    ```

References:
    `GET /2.0/workspaces/{workspace}/permissions/repositories/{repo_slug}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-workspaces/#api-workspaces-workspace-permissions-repositories-repo-slug-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.workspaces.get_repo_permission`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.get_repo_permission(client, workspace, repo_slug))

def user_prs(client: BBClient, workspace: str, selected_user: str, *, pagelen: int=25) -> list[Any] | Error:
    """List pull requests authored by a specific user in a workspace.

Synchronous wrapper around :func:`~bb.cloud.sdk.workspaces.user_prs`.

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
    prs = workspaces.user_prs(
        client, workspace="myworkspace", selected_user="{abc-123}"
    )
    ```

References:
    `GET /2.0/workspaces/{workspace}/pullrequests/{selected_user}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-workspaces/#api-workspaces-workspace-pullrequests-selected-user-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.workspaces.user_prs`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.user_prs(client, workspace, selected_user, pagelen=pagelen))

def gpg_key(client: BBClient, workspace: str) -> Any | Error | None:
    """Fetch the GPG public key for a workspace.

Synchronous wrapper around :func:`~bb.cloud.sdk.workspaces.gpg_key`.

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
    key = workspaces.gpg_key(client, workspace="myworkspace")
    ```

References:
    `GET /2.0/workspaces/{workspace}/settings/gpg-public-key
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-workspaces/#api-workspaces-workspace-settings-gpg-public-key-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.workspaces.gpg_key`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.gpg_key(client, workspace))

def mine(client: BBClient, *, pagelen: int=25) -> list[Workspace] | Error:
    """List the authenticated user's workspaces via the /user endpoint.

Synchronous wrapper around :func:`~bb.cloud.sdk.workspaces.mine`.

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
    my_workspaces = workspaces.mine(client)
    ```

References:
    `GET /2.0/user/workspaces
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-workspaces/#api-user-workspaces-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.workspaces.mine`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.mine(client, pagelen=pagelen))

def my_permissions(client: BBClient, *, pagelen: int=25) -> list[Any] | Error:
    """List the current user's permissions across all workspaces.

Synchronous wrapper around :func:`~bb.cloud.sdk.workspaces.my_permissions`.

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
    perms = workspaces.my_permissions(client)
    ```

References:
    `GET /2.0/user/permissions/workspaces
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-workspaces/#api-user-permissions-workspaces-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.workspaces.my_permissions`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.my_permissions(client, pagelen=pagelen))

def my_permission(client: BBClient, workspace: str) -> Any | Error | None:
    """Fetch the current user's permission in a specific workspace.

Synchronous wrapper around :func:`~bb.cloud.sdk.workspaces.my_permission`.

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
    perm = workspaces.my_permission(client, workspace="myworkspace")
    ```

References:
    `GET /2.0/user/workspaces/{workspace}/permission
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-workspaces/#api-user-workspaces-workspace-permission-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.workspaces.my_permission`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.my_permission(client, workspace))
