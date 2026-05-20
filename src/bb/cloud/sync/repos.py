from __future__ import annotations
from typing import Any
from bb.cloud.models.error import Error
from bb.cloud.models.repository import Repository
from bb.cloud.sdk._client import BBClient
from bb.cloud.types import UNSET, Unset
from bb.cloud.sdk import repos as _async
__all__ = ['list', 'get', 'create', 'update', 'delete', 'fork', 'forks', 'watchers', 'override_settings', 'update_override_settings', 'group_permissions', 'get_group_permission', 'set_group_permission', 'delete_group_permission', 'user_permissions', 'get_user_permission', 'set_user_permission', 'delete_user_permission', 'my_permissions', 'workspace_user_permissions']

def list(client: BBClient, workspace: str, *, q: str | Unset=UNSET, sort: str | Unset=UNSET, pagelen: int=25) -> list[Repository] | Error:
    """List all repositories in a workspace across all pages.

Synchronous wrapper around :func:`~bb.cloud.sdk.repos.list`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    q: Query string to filter results. See Bitbucket filtering docs.
    sort: Field to sort results by, prefix with ``-`` for descending.
    pagelen: Number of results per page. Defaults to ``25``.

Returns:
    All repositories in the workspace across all pages, or an :class:`~bb.cloud.models.error.Error` on failure.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import repos

    client = BBClient.from_env()
    result = repos.list(client, workspace="myworkspace")
    ```

References:
    `GET /2.0/repositories/{workspace}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.repos.list`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.list(client, workspace, q=q, sort=sort, pagelen=pagelen))

def get(client: BBClient, workspace: str, repo_slug: str) -> Repository | Error | None:
    """Fetch a single repository by slug.

Synchronous wrapper around :func:`~bb.cloud.sdk.repos.get`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.

Returns:
    The :class:`~bb.cloud.models.repository.Repository` object, an :class:`~bb.cloud.models.error.Error` on API error, or ``None`` if the response is empty.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import repos

    client = BBClient.from_env()
    repo = repos.get(client, workspace="myworkspace", repo_slug="myrepo")
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.repos.get`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.get(client, workspace, repo_slug))

def create(client: BBClient, workspace: str, repo_slug: str, *, body: Repository | Unset=UNSET) -> Repository | Error | None:
    """Create a new repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.repos.create`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Slug for the new repository.
    body: Repository configuration. Use :class:`~bb.cloud.models.repository.Repository`.

Returns:
    The created :class:`~bb.cloud.models.repository.Repository`, an :class:`~bb.cloud.models.error.Error` on API error, or ``None`` if the response is empty.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.models.repository import Repository
    from bb.cloud.sdk import repos

    client = BBClient.from_env()
    repo = repos.create(
        client,
        workspace="myworkspace",
        repo_slug="newrepo",
        body=Repository(scm="git", is_private=True),
    )
    ```

References:
    `POST /2.0/repositories/{workspace}/{repo_slug}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-post>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.repos.create`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.create(client, workspace, repo_slug, body=body))

def update(client: BBClient, workspace: str, repo_slug: str, *, body: Repository | Unset=UNSET) -> Repository | Error | None:
    """Update an existing repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.repos.update`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    body: Fields to update. Use :class:`~bb.cloud.models.repository.Repository`.

Returns:
    The updated :class:`~bb.cloud.models.repository.Repository`, an :class:`~bb.cloud.models.error.Error` on API error, or ``None`` if the response is empty.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.models.repository import Repository
    from bb.cloud.sdk import repos

    client = BBClient.from_env()
    repo = repos.update(
        client,
        workspace="myworkspace",
        repo_slug="myrepo",
        body=Repository(description="Updated description"),
    )
    ```

References:
    `PUT /2.0/repositories/{workspace}/{repo_slug}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-put>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.repos.update`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.update(client, workspace, repo_slug, body=body))

def delete(client: BBClient, workspace: str, repo_slug: str) -> None:
    """Delete a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.repos.delete`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.

Returns:
    ``None``.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import repos

    client = BBClient.from_env()
    repos.delete(client, workspace="myworkspace", repo_slug="myrepo")
    ```

References:
    `DELETE /2.0/repositories/{workspace}/{repo_slug}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.repos.delete`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.delete(client, workspace, repo_slug))

def fork(client: BBClient, workspace: str, repo_slug: str, *, body: Repository | Unset=UNSET) -> Repository | Error | None:
    """Fork a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.repos.fork`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID to fork.
    body: Fork configuration. Use :class:`~bb.cloud.models.repository.Repository`.

Returns:
    The forked :class:`~bb.cloud.models.repository.Repository`, an :class:`~bb.cloud.models.error.Error` on API error, or ``None`` if the response is empty.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import repos

    client = BBClient.from_env()
    fork = repos.fork(client, workspace="myworkspace", repo_slug="myrepo")
    ```

References:
    `POST /2.0/repositories/{workspace}/{repo_slug}/forks
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-forks-post>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.repos.fork`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.fork(client, workspace, repo_slug, body=body))

def forks(client: BBClient, workspace: str, repo_slug: str) -> list[Repository] | Error:
    """List all forks of a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.repos.forks`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.

Returns:
    All forks of the repository across all pages, or an :class:`~bb.cloud.models.error.Error` on failure.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import repos

    client = BBClient.from_env()
    all_forks = repos.forks(client, workspace="myworkspace", repo_slug="myrepo")
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/forks
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-forks-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.repos.forks`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.forks(client, workspace, repo_slug))

def watchers(client: BBClient, workspace: str, repo_slug: str) -> list[Repository] | Error:
    """List all accounts watching a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.repos.watchers`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.

Returns:
    All accounts watching the repository across all pages, or an :class:`~bb.cloud.models.error.Error` on failure.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import repos

    client = BBClient.from_env()
    all_watchers = repos.watchers(client, workspace="myworkspace", repo_slug="myrepo")
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/watchers
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-watchers-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.repos.watchers`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.watchers(client, workspace, repo_slug))

def override_settings(client: BBClient, workspace: str, repo_slug: str) -> Any | None:
    """Fetch the inheritance override settings for a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.repos.override_settings`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.

Returns:
    The override settings object, or ``None`` if not found.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import repos

    client = BBClient.from_env()
    settings = repos.override_settings(client, workspace="myworkspace", repo_slug="myrepo")
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/override-settings
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-override-settings-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.repos.override_settings`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.override_settings(client, workspace, repo_slug))

def update_override_settings(client: BBClient, workspace: str, repo_slug: str, *, body: Unset=UNSET) -> Any | None:
    """Update the inheritance override settings for a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.repos.update_override_settings`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    body: Override settings body.

Returns:
    The updated override settings object, or ``None`` on error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import repos

    client = BBClient.from_env()
    settings = repos.update_override_settings(
        client, workspace="myworkspace", repo_slug="myrepo"
    )
    ```

References:
    `PUT /2.0/repositories/{workspace}/{repo_slug}/override-settings
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-override-settings-put>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.repos.update_override_settings`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.update_override_settings(client, workspace, repo_slug, body=body))

def group_permissions(client: BBClient, workspace: str, repo_slug: str, *, pagelen: int=25) -> list[Any] | Error:
    """List all group permission configurations for a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.repos.group_permissions`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    pagelen: Number of results per page. Defaults to ``25``.

Returns:
    All group permission entries across all pages, or an :class:`~bb.cloud.models.error.Error` on failure.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import repos

    client = BBClient.from_env()
    perms = repos.group_permissions(client, workspace="myworkspace", repo_slug="myrepo")
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/permissions-config/groups
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-permissions-config-groups-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.repos.group_permissions`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.group_permissions(client, workspace, repo_slug, pagelen=pagelen))

def get_group_permission(client: BBClient, workspace: str, repo_slug: str, group_slug: str) -> Any | None:
    """Fetch a specific group's permission configuration for a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.repos.get_group_permission`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    group_slug: The group's slug identifier.

Returns:
    The group permission object, or ``None`` if not found.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import repos

    client = BBClient.from_env()
    perm = repos.get_group_permission(
        client, workspace="myworkspace", repo_slug="myrepo", group_slug="devs"
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/permissions-config/groups/{group_slug}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-permissions-config-groups-group-slug-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.repos.get_group_permission`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.get_group_permission(client, workspace, repo_slug, group_slug))

def set_group_permission(client: BBClient, workspace: str, repo_slug: str, group_slug: str, *, body: Unset=UNSET) -> Any | None:
    """Set a group's permission on a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.repos.set_group_permission`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    group_slug: The group's slug identifier.
    body: Permission body.

Returns:
    The updated group permission object, or ``None`` on error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import repos

    client = BBClient.from_env()
    perm = repos.set_group_permission(
        client, workspace="myworkspace", repo_slug="myrepo", group_slug="devs"
    )
    ```

References:
    `PUT /2.0/repositories/{workspace}/{repo_slug}/permissions-config/groups/{group_slug}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-permissions-config-groups-group-slug-put>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.repos.set_group_permission`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.set_group_permission(client, workspace, repo_slug, group_slug, body=body))

def delete_group_permission(client: BBClient, workspace: str, repo_slug: str, group_slug: str) -> None:
    """Remove a group's permission from a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.repos.delete_group_permission`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    group_slug: The group's slug identifier.

Returns:
    ``None``.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import repos

    client = BBClient.from_env()
    repos.delete_group_permission(
        client, workspace="myworkspace", repo_slug="myrepo", group_slug="devs"
    )
    ```

References:
    `DELETE /2.0/repositories/{workspace}/{repo_slug}/permissions-config/groups/{group_slug}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-permissions-config-groups-group-slug-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.repos.delete_group_permission`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.delete_group_permission(client, workspace, repo_slug, group_slug))

def user_permissions(client: BBClient, workspace: str, repo_slug: str, *, pagelen: int=25) -> list[Any] | Error:
    """List all user permission configurations for a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.repos.user_permissions`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    pagelen: Number of results per page. Defaults to ``25``.

Returns:
    All user permission entries across all pages, or an :class:`~bb.cloud.models.error.Error` on failure.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import repos

    client = BBClient.from_env()
    perms = repos.user_permissions(client, workspace="myworkspace", repo_slug="myrepo")
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/permissions-config/users
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-permissions-config-users-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.repos.user_permissions`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.user_permissions(client, workspace, repo_slug, pagelen=pagelen))

def get_user_permission(client: BBClient, workspace: str, repo_slug: str, selected_user_id: str) -> Any | None:
    """Fetch a specific user's permission configuration for a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.repos.get_user_permission`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    selected_user_id: The user's account UUID (with surrounding braces, e.g. ``{abc-123}``).

Returns:
    The user permission object, or ``None`` if not found.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import repos

    client = BBClient.from_env()
    perm = repos.get_user_permission(
        client, workspace="myworkspace", repo_slug="myrepo", selected_user_id="{abc-123}"
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/permissions-config/users/{selected_user_id}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-permissions-config-users-selected-user-id-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.repos.get_user_permission`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.get_user_permission(client, workspace, repo_slug, selected_user_id))

def set_user_permission(client: BBClient, workspace: str, repo_slug: str, selected_user_id: str, *, body: Unset=UNSET) -> Any | None:
    """Set a user's permission on a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.repos.set_user_permission`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    selected_user_id: The user's account UUID (with surrounding braces, e.g. ``{abc-123}``).
    body: Permission body.

Returns:
    The updated user permission object, or ``None`` on error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import repos

    client = BBClient.from_env()
    perm = repos.set_user_permission(
        client,
        workspace="myworkspace",
        repo_slug="myrepo",
        selected_user_id="{abc-123}",
    )
    ```

References:
    `PUT /2.0/repositories/{workspace}/{repo_slug}/permissions-config/users/{selected_user_id}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-permissions-config-users-selected-user-id-put>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.repos.set_user_permission`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.set_user_permission(client, workspace, repo_slug, selected_user_id, body=body))

def delete_user_permission(client: BBClient, workspace: str, repo_slug: str, selected_user_id: str) -> None:
    """Remove a user's permission from a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.repos.delete_user_permission`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    selected_user_id: The user's account UUID (with surrounding braces, e.g. ``{abc-123}``).

Returns:
    ``None``.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import repos

    client = BBClient.from_env()
    repos.delete_user_permission(
        client,
        workspace="myworkspace",
        repo_slug="myrepo",
        selected_user_id="{abc-123}",
    )
    ```

References:
    `DELETE /2.0/repositories/{workspace}/{repo_slug}/permissions-config/users/{selected_user_id}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-permissions-config-users-selected-user-id-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.repos.delete_user_permission`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.delete_user_permission(client, workspace, repo_slug, selected_user_id))

def my_permissions(client: BBClient, *, pagelen: int=25) -> list[Any] | Error:
    """List the current user's permissions across all accessible repositories.

Synchronous wrapper around :func:`~bb.cloud.sdk.repos.my_permissions`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    pagelen: Number of results per page. Defaults to ``25``.

Returns:
    All repository permission entries for the current user across all pages, or an :class:`~bb.cloud.models.error.Error` on failure.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import repos

    client = BBClient.from_env()
    perms = repos.my_permissions(client)
    ```

References:
    `GET /2.0/user/permissions/repositories
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-user-permissions-repositories-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.repos.my_permissions`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.my_permissions(client, pagelen=pagelen))

def workspace_user_permissions(client: BBClient, workspace: str, *, pagelen: int=25) -> list[Any] | Error:
    """List the current user's repository permissions within a workspace.

Synchronous wrapper around :func:`~bb.cloud.sdk.repos.workspace_user_permissions`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    pagelen: Number of results per page. Defaults to ``25``.

Returns:
    All repository permission entries for the current user in the workspace across all pages, or an :class:`~bb.cloud.models.error.Error` on failure.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import repos

    client = BBClient.from_env()
    perms = repos.workspace_user_permissions(client, workspace="myworkspace")
    ```

References:
    `GET /2.0/user/workspaces/{workspace}/permissions/repositories
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-user-workspaces-workspace-permissions-repositories-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.repos.workspace_user_permissions`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.workspace_user_permissions(client, workspace, pagelen=pagelen))
