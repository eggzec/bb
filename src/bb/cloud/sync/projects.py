from __future__ import annotations
from typing import Any
from bb.cloud.models.error import Error
from bb.cloud.models.project import Project
from bb.cloud.sdk._client import BBClient
from bb.cloud.types import UNSET, Unset
from bb.cloud.sdk import projects as _async
__all__ = ['list', 'get', 'create', 'update', 'delete', 'default_reviewers', 'get_default_reviewer', 'add_default_reviewer', 'remove_default_reviewer', 'group_permissions', 'update_group_permission', 'delete_group_permission', 'user_permissions', 'update_user_permission', 'delete_user_permission']

def list(client: BBClient, workspace: str, *, pagelen: int=25) -> list[Project] | Error:
    """List all projects in a workspace.

Synchronous wrapper around :func:`~bb.cloud.sdk.projects.list`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    pagelen: Number of results per page. Defaults to ``25``.

Returns:
    All projects in the workspace across all pages.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import projects

    client = BBClient.from_env()
    all_projects = projects.list(client, workspace="myworkspace")
    ```

References:
    `GET /2.0/workspaces/{workspace}/projects
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-projects/#api-workspaces-workspace-projects-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.projects.list`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.list(client, workspace, pagelen=pagelen))

def get(client: BBClient, workspace: str, project_key: str) -> Project | Error | None:
    """Fetch a single project by key.

Synchronous wrapper around :func:`~bb.cloud.sdk.projects.get`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    project_key: The project's unique key (e.g. ``MYPROJ``).

Returns:
    The :class:`~bb.cloud.models.project.Project` object, or ``None`` if not found.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import projects

    client = BBClient.from_env()
    project = projects.get(client, workspace="myworkspace", project_key="MYPROJ")
    ```

References:
    `GET /2.0/workspaces/{workspace}/projects/{project_key}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-projects/#api-workspaces-workspace-projects-project-key-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.projects.get`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.get(client, workspace, project_key))

def create(client: BBClient, workspace: str, *, body: Project | Unset=UNSET) -> Project | Error | None:
    """Create a new project in a workspace.

Synchronous wrapper around :func:`~bb.cloud.sdk.projects.create`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    body: Project configuration. Use :class:`~bb.cloud.models.project.Project`.

Returns:
    The created :class:`~bb.cloud.models.project.Project`, or ``None`` on error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.models.project import Project
    from bb.cloud.sdk import projects

    client = BBClient.from_env()
    project = projects.create(
        client,
        workspace="myworkspace",
        body=Project(name="My Project", key="MYPROJ"),
    )
    ```

References:
    `POST /2.0/workspaces/{workspace}/projects
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-projects/#api-workspaces-workspace-projects-post>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.projects.create`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.create(client, workspace, body=body))

def update(client: BBClient, workspace: str, project_key: str, *, body: Project | Unset=UNSET) -> Project | Error | None:
    """Update an existing project.

Synchronous wrapper around :func:`~bb.cloud.sdk.projects.update`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    project_key: The project's unique key (e.g. ``MYPROJ``).
    body: Fields to update. Use :class:`~bb.cloud.models.project.Project`.

Returns:
    The updated :class:`~bb.cloud.models.project.Project`, or ``None`` on error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.models.project import Project
    from bb.cloud.sdk import projects

    client = BBClient.from_env()
    project = projects.update(
        client,
        workspace="myworkspace",
        project_key="MYPROJ",
        body=Project(description="Updated description"),
    )
    ```

References:
    `PUT /2.0/workspaces/{workspace}/projects/{project_key}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-projects/#api-workspaces-workspace-projects-project-key-put>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.projects.update`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.update(client, workspace, project_key, body=body))

def delete(client: BBClient, workspace: str, project_key: str) -> None:
    """Delete a project.

Synchronous wrapper around :func:`~bb.cloud.sdk.projects.delete`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    project_key: The project's unique key (e.g. ``MYPROJ``).

Returns:
    ``None``.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import projects

    client = BBClient.from_env()
    projects.delete(client, workspace="myworkspace", project_key="MYPROJ")
    ```

References:
    `DELETE /2.0/workspaces/{workspace}/projects/{project_key}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-projects/#api-workspaces-workspace-projects-project-key-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.projects.delete`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.delete(client, workspace, project_key))

def default_reviewers(client: BBClient, workspace: str, project_key: str, *, pagelen: int=25) -> list[Any] | Error:
    """List all default reviewers for a project.

Synchronous wrapper around :func:`~bb.cloud.sdk.projects.default_reviewers`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    project_key: The project's unique key (e.g. ``MYPROJ``).
    pagelen: Number of results per page. Defaults to ``25``.

Returns:
    All default reviewer entries for the project across all pages.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import projects

    client = BBClient.from_env()
    reviewers = projects.default_reviewers(
        client, workspace="myworkspace", project_key="MYPROJ"
    )
    ```

References:
    `GET /2.0/workspaces/{workspace}/projects/{project_key}/default-reviewers
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-projects/#api-workspaces-workspace-projects-project-key-default-reviewers-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.projects.default_reviewers`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.default_reviewers(client, workspace, project_key, pagelen=pagelen))

def get_default_reviewer(client: BBClient, workspace: str, project_key: str, selected_user: str) -> Any | Error | None:
    """Fetch a specific default reviewer for a project.

Synchronous wrapper around :func:`~bb.cloud.sdk.projects.get_default_reviewer`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    project_key: The project's unique key (e.g. ``MYPROJ``).
    selected_user: The user's account UUID (with surrounding braces, e.g. ``{abc-123}``)
        or username.

Returns:
    The default reviewer object, or ``None`` if not found.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import projects

    client = BBClient.from_env()
    reviewer = projects.get_default_reviewer(
        client, workspace="myworkspace", project_key="MYPROJ", selected_user="{abc-123}"
    )
    ```

References:
    `GET /2.0/workspaces/{workspace}/projects/{project_key}/default-reviewers/{selected_user}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-projects/#api-workspaces-workspace-projects-project-key-default-reviewers-selected-user-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.projects.get_default_reviewer`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.get_default_reviewer(client, workspace, project_key, selected_user))

def add_default_reviewer(client: BBClient, workspace: str, project_key: str, selected_user: str) -> None:
    """Add a user as a default reviewer for a project.

Synchronous wrapper around :func:`~bb.cloud.sdk.projects.add_default_reviewer`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    project_key: The project's unique key (e.g. ``MYPROJ``).
    selected_user: The user's account UUID (with surrounding braces, e.g. ``{abc-123}``)
        or username.

Returns:
    ``None``.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import projects

    client = BBClient.from_env()
    projects.add_default_reviewer(
        client, workspace="myworkspace", project_key="MYPROJ", selected_user="{abc-123}"
    )
    ```

References:
    `PUT /2.0/workspaces/{workspace}/projects/{project_key}/default-reviewers/{selected_user}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-projects/#api-workspaces-workspace-projects-project-key-default-reviewers-selected-user-put>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.projects.add_default_reviewer`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.add_default_reviewer(client, workspace, project_key, selected_user))

def remove_default_reviewer(client: BBClient, workspace: str, project_key: str, selected_user: str) -> None:
    """Remove a user from the default reviewers for a project.

Synchronous wrapper around :func:`~bb.cloud.sdk.projects.remove_default_reviewer`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    project_key: The project's unique key (e.g. ``MYPROJ``).
    selected_user: The user's account UUID (with surrounding braces, e.g. ``{abc-123}``)
        or username.

Returns:
    ``None``.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import projects

    client = BBClient.from_env()
    projects.remove_default_reviewer(
        client, workspace="myworkspace", project_key="MYPROJ", selected_user="{abc-123}"
    )
    ```

References:
    `DELETE /2.0/workspaces/{workspace}/projects/{project_key}/default-reviewers/{selected_user}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-projects/#api-workspaces-workspace-projects-project-key-default-reviewers-selected-user-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.projects.remove_default_reviewer`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.remove_default_reviewer(client, workspace, project_key, selected_user))

def group_permissions(client: BBClient, workspace: str, project_key: str, *, pagelen: int=25) -> list[Any] | Error:
    """List all group permission configurations for a project.

Synchronous wrapper around :func:`~bb.cloud.sdk.projects.group_permissions`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    project_key: The project's unique key (e.g. ``MYPROJ``).
    pagelen: Number of results per page. Defaults to ``25``.

Returns:
    All group permission entries for the project across all pages.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import projects

    client = BBClient.from_env()
    perms = projects.group_permissions(
        client, workspace="myworkspace", project_key="MYPROJ"
    )
    ```

References:
    `GET /2.0/workspaces/{workspace}/projects/{project_key}/permissions-config/groups
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-projects/#api-workspaces-workspace-projects-project-key-permissions-config-groups-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.projects.group_permissions`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.group_permissions(client, workspace, project_key, pagelen=pagelen))

def update_group_permission(client: BBClient, workspace: str, project_key: str, group_slug: str, *, body: Unset=UNSET) -> Any | Error | None:
    """Update a group's permission on a project.

Synchronous wrapper around :func:`~bb.cloud.sdk.projects.update_group_permission`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    project_key: The project's unique key (e.g. ``MYPROJ``).
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
    from bb.cloud.sdk import projects

    client = BBClient.from_env()
    perm = projects.update_group_permission(
        client, workspace="myworkspace", project_key="MYPROJ", group_slug="devs"
    )
    ```

References:
    `PUT /2.0/workspaces/{workspace}/projects/{project_key}/permissions-config/groups/{group_slug}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-projects/#api-workspaces-workspace-projects-project-key-permissions-config-groups-group-slug-put>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.projects.update_group_permission`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.update_group_permission(client, workspace, project_key, group_slug, body=body))

def delete_group_permission(client: BBClient, workspace: str, project_key: str, group_slug: str) -> None:
    """Remove a group's permission from a project.

Synchronous wrapper around :func:`~bb.cloud.sdk.projects.delete_group_permission`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    project_key: The project's unique key (e.g. ``MYPROJ``).
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
    from bb.cloud.sdk import projects

    client = BBClient.from_env()
    projects.delete_group_permission(
        client, workspace="myworkspace", project_key="MYPROJ", group_slug="devs"
    )
    ```

References:
    `DELETE /2.0/workspaces/{workspace}/projects/{project_key}/permissions-config/groups/{group_slug}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-projects/#api-workspaces-workspace-projects-project-key-permissions-config-groups-group-slug-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.projects.delete_group_permission`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.delete_group_permission(client, workspace, project_key, group_slug))

def user_permissions(client: BBClient, workspace: str, project_key: str, *, pagelen: int=25) -> list[Any] | Error:
    """List all user permission configurations for a project.

Synchronous wrapper around :func:`~bb.cloud.sdk.projects.user_permissions`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    project_key: The project's unique key (e.g. ``MYPROJ``).
    pagelen: Number of results per page. Defaults to ``25``.

Returns:
    All user permission entries for the project across all pages.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import projects

    client = BBClient.from_env()
    perms = projects.user_permissions(
        client, workspace="myworkspace", project_key="MYPROJ"
    )
    ```

References:
    `GET /2.0/workspaces/{workspace}/projects/{project_key}/permissions-config/users
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-projects/#api-workspaces-workspace-projects-project-key-permissions-config-users-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.projects.user_permissions`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.user_permissions(client, workspace, project_key, pagelen=pagelen))

def update_user_permission(client: BBClient, workspace: str, project_key: str, selected_user_id: str, *, body: Unset=UNSET) -> Any | Error | None:
    """Update a user's permission on a project.

Synchronous wrapper around :func:`~bb.cloud.sdk.projects.update_user_permission`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    project_key: The project's unique key (e.g. ``MYPROJ``).
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
    from bb.cloud.sdk import projects

    client = BBClient.from_env()
    perm = projects.update_user_permission(
        client,
        workspace="myworkspace",
        project_key="MYPROJ",
        selected_user_id="{abc-123}",
    )
    ```

References:
    `PUT /2.0/workspaces/{workspace}/projects/{project_key}/permissions-config/users/{selected_user_id}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-projects/#api-workspaces-workspace-projects-project-key-permissions-config-users-selected-user-id-put>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.projects.update_user_permission`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.update_user_permission(client, workspace, project_key, selected_user_id, body=body))

def delete_user_permission(client: BBClient, workspace: str, project_key: str, selected_user_id: str) -> None:
    """Remove a user's permission from a project.

Synchronous wrapper around :func:`~bb.cloud.sdk.projects.delete_user_permission`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    project_key: The project's unique key (e.g. ``MYPROJ``).
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
    from bb.cloud.sdk import projects

    client = BBClient.from_env()
    projects.delete_user_permission(
        client,
        workspace="myworkspace",
        project_key="MYPROJ",
        selected_user_id="{abc-123}",
    )
    ```

References:
    `DELETE /2.0/workspaces/{workspace}/projects/{project_key}/permissions-config/users/{selected_user_id}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-projects/#api-workspaces-workspace-projects-project-key-permissions-config-users-selected-user-id-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.projects.delete_user_permission`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.delete_user_permission(client, workspace, project_key, selected_user_id))
