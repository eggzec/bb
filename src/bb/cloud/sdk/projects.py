from __future__ import annotations

from typing import Any

from bb.cloud.api.projects import (
    delete_workspaces_workspace_projects_project_key,
    delete_workspaces_workspace_projects_project_key_default_reviewers_selected_user,
    delete_workspaces_workspace_projects_project_key_permissions_config_groups_group_slug,
    delete_workspaces_workspace_projects_project_key_permissions_config_users_selected_user_id,
    get_workspaces_workspace_projects_project_key,
    get_workspaces_workspace_projects_project_key_default_reviewers,
    get_workspaces_workspace_projects_project_key_default_reviewers_selected_user,
    get_workspaces_workspace_projects_project_key_permissions_config_groups,
    get_workspaces_workspace_projects_project_key_permissions_config_users,
    post_workspaces_workspace_projects,
    put_workspaces_workspace_projects_project_key,
    put_workspaces_workspace_projects_project_key_default_reviewers_selected_user,
    put_workspaces_workspace_projects_project_key_permissions_config_groups_group_slug,
    put_workspaces_workspace_projects_project_key_permissions_config_users_selected_user_id,
)
from bb.cloud.api.workspaces import get_workspaces_workspace_projects
from bb.cloud.models.project import Project
from bb.cloud.sdk._auth_validation import AuthMethod, require_auth
from bb.cloud.sdk._client import BBClient
from bb.cloud.sdk._pagination import async_paginate
from bb.cloud.types import UNSET, Unset

__all__ = [
    "list",
    "get",
    "create",
    "update",
    "delete",
    "default_reviewers",
    "get_default_reviewer",
    "add_default_reviewer",
    "remove_default_reviewer",
    "group_permissions",
    "update_group_permission",
    "delete_group_permission",
    "user_permissions",
    "update_user_permission",
    "delete_user_permission",
]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def list(client: BBClient, workspace: str, *, pagelen: int = 25) -> list[Project]:
    """List all projects in a workspace.

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
        all_projects = await projects.list(client, workspace="myworkspace")
        ```

    References:
        `GET /2.0/workspaces/{workspace}/projects
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-projects/#api-workspaces-workspace-projects-get>`_
    """
    return [
        p
        async for p in async_paginate(
            get_workspaces_workspace_projects.asyncio,
            workspace,
            client=client.auth,
            pagelen=pagelen,
        )
        if isinstance(p, Project)
    ]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get(client: BBClient, workspace: str, project_key: str) -> Project | None:
    """Fetch a single project by key.

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
        project = await projects.get(client, workspace="myworkspace", project_key="MYPROJ")
        ```

    References:
        `GET /2.0/workspaces/{workspace}/projects/{project_key}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-projects/#api-workspaces-workspace-projects-project-key-get>`_
    """
    result = await get_workspaces_workspace_projects_project_key.asyncio(workspace, project_key, client=client.auth)
    return result if isinstance(result, Project) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def create(
    client: BBClient,
    workspace: str,
    *,
    body: Project | Unset = UNSET,
) -> Project | None:
    """Create a new project in a workspace.

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
        project = await projects.create(
            client,
            workspace="myworkspace",
            body=Project(name="My Project", key="MYPROJ"),
        )
        ```

    References:
        `POST /2.0/workspaces/{workspace}/projects
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-projects/#api-workspaces-workspace-projects-post>`_
    """
    result = await post_workspaces_workspace_projects.asyncio(workspace, client=client.auth, body=body)
    return result if isinstance(result, Project) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def update(
    client: BBClient,
    workspace: str,
    project_key: str,
    *,
    body: Project | Unset = UNSET,
) -> Project | None:
    """Update an existing project.

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
        project = await projects.update(
            client,
            workspace="myworkspace",
            project_key="MYPROJ",
            body=Project(description="Updated description"),
        )
        ```

    References:
        `PUT /2.0/workspaces/{workspace}/projects/{project_key}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-projects/#api-workspaces-workspace-projects-project-key-put>`_
    """
    result = await put_workspaces_workspace_projects_project_key.asyncio(
        workspace, project_key, client=client.auth, body=body
    )
    return result if isinstance(result, Project) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def delete(client: BBClient, workspace: str, project_key: str) -> None:
    """Delete a project.

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
        await projects.delete(client, workspace="myworkspace", project_key="MYPROJ")
        ```

    References:
        `DELETE /2.0/workspaces/{workspace}/projects/{project_key}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-projects/#api-workspaces-workspace-projects-project-key-delete>`_
    """
    await delete_workspaces_workspace_projects_project_key.asyncio(workspace, project_key, client=client.auth)


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def default_reviewers(client: BBClient, workspace: str, project_key: str, *, pagelen: int = 25) -> list[Any]:
    """List all default reviewers for a project.

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
        reviewers = await projects.default_reviewers(
            client, workspace="myworkspace", project_key="MYPROJ"
        )
        ```

    References:
        `GET /2.0/workspaces/{workspace}/projects/{project_key}/default-reviewers
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-projects/#api-workspaces-workspace-projects-project-key-default-reviewers-get>`_
    """
    return [
        r
        async for r in async_paginate(
            get_workspaces_workspace_projects_project_key_default_reviewers.asyncio,
            workspace,
            project_key,
            client=client.auth,
            pagelen=pagelen,
        )
    ]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get_default_reviewer(client: BBClient, workspace: str, project_key: str, selected_user: str) -> Any | None:
    """Fetch a specific default reviewer for a project.

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
        reviewer = await projects.get_default_reviewer(
            client, workspace="myworkspace", project_key="MYPROJ", selected_user="{abc-123}"
        )
        ```

    References:
        `GET /2.0/workspaces/{workspace}/projects/{project_key}/default-reviewers/{selected_user}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-projects/#api-workspaces-workspace-projects-project-key-default-reviewers-selected-user-get>`_
    """
    return await get_workspaces_workspace_projects_project_key_default_reviewers_selected_user.asyncio(
        workspace, project_key, selected_user, client=client.auth
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def add_default_reviewer(client: BBClient, workspace: str, project_key: str, selected_user: str) -> None:
    """Add a user as a default reviewer for a project.

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
        await projects.add_default_reviewer(
            client, workspace="myworkspace", project_key="MYPROJ", selected_user="{abc-123}"
        )
        ```

    References:
        `PUT /2.0/workspaces/{workspace}/projects/{project_key}/default-reviewers/{selected_user}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-projects/#api-workspaces-workspace-projects-project-key-default-reviewers-selected-user-put>`_
    """
    await put_workspaces_workspace_projects_project_key_default_reviewers_selected_user.asyncio(
        workspace, project_key, selected_user, client=client.auth
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def remove_default_reviewer(client: BBClient, workspace: str, project_key: str, selected_user: str) -> None:
    """Remove a user from the default reviewers for a project.

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
        await projects.remove_default_reviewer(
            client, workspace="myworkspace", project_key="MYPROJ", selected_user="{abc-123}"
        )
        ```

    References:
        `DELETE /2.0/workspaces/{workspace}/projects/{project_key}/default-reviewers/{selected_user}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-projects/#api-workspaces-workspace-projects-project-key-default-reviewers-selected-user-delete>`_
    """
    await delete_workspaces_workspace_projects_project_key_default_reviewers_selected_user.asyncio(
        workspace, project_key, selected_user, client=client.auth
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def group_permissions(client: BBClient, workspace: str, project_key: str, *, pagelen: int = 25) -> list[Any]:
    """List all group permission configurations for a project.

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
        perms = await projects.group_permissions(
            client, workspace="myworkspace", project_key="MYPROJ"
        )
        ```

    References:
        `GET /2.0/workspaces/{workspace}/projects/{project_key}/permissions-config/groups
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-projects/#api-workspaces-workspace-projects-project-key-permissions-config-groups-get>`_
    """
    return [
        p
        async for p in async_paginate(
            get_workspaces_workspace_projects_project_key_permissions_config_groups.asyncio,
            workspace,
            project_key,
            client=client.auth,
            pagelen=pagelen,
        )
    ]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def update_group_permission(
    client: BBClient,
    workspace: str,
    project_key: str,
    group_slug: str,
    *,
    body: Unset = UNSET,
) -> Any | None:
    """Update a group's permission on a project.

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
        perm = await projects.update_group_permission(
            client, workspace="myworkspace", project_key="MYPROJ", group_slug="devs"
        )
        ```

    References:
        `PUT /2.0/workspaces/{workspace}/projects/{project_key}/permissions-config/groups/{group_slug}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-projects/#api-workspaces-workspace-projects-project-key-permissions-config-groups-group-slug-put>`_
    """
    return await put_workspaces_workspace_projects_project_key_permissions_config_groups_group_slug.asyncio(
        workspace, project_key, group_slug, client=client.auth, body=body
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def delete_group_permission(client: BBClient, workspace: str, project_key: str, group_slug: str) -> None:
    """Remove a group's permission from a project.

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
        await projects.delete_group_permission(
            client, workspace="myworkspace", project_key="MYPROJ", group_slug="devs"
        )
        ```

    References:
        `DELETE /2.0/workspaces/{workspace}/projects/{project_key}/permissions-config/groups/{group_slug}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-projects/#api-workspaces-workspace-projects-project-key-permissions-config-groups-group-slug-delete>`_
    """
    await delete_workspaces_workspace_projects_project_key_permissions_config_groups_group_slug.asyncio(
        workspace, project_key, group_slug, client=client.auth
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def user_permissions(client: BBClient, workspace: str, project_key: str, *, pagelen: int = 25) -> list[Any]:
    """List all user permission configurations for a project.

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
        perms = await projects.user_permissions(
            client, workspace="myworkspace", project_key="MYPROJ"
        )
        ```

    References:
        `GET /2.0/workspaces/{workspace}/projects/{project_key}/permissions-config/users
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-projects/#api-workspaces-workspace-projects-project-key-permissions-config-users-get>`_
    """
    return [
        p
        async for p in async_paginate(
            get_workspaces_workspace_projects_project_key_permissions_config_users.asyncio,
            workspace,
            project_key,
            client=client.auth,
            pagelen=pagelen,
        )
    ]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def update_user_permission(
    client: BBClient,
    workspace: str,
    project_key: str,
    selected_user_id: str,
    *,
    body: Unset = UNSET,
) -> Any | None:
    """Update a user's permission on a project.

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
        perm = await projects.update_user_permission(
            client,
            workspace="myworkspace",
            project_key="MYPROJ",
            selected_user_id="{abc-123}",
        )
        ```

    References:
        `PUT /2.0/workspaces/{workspace}/projects/{project_key}/permissions-config/users/{selected_user_id}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-projects/#api-workspaces-workspace-projects-project-key-permissions-config-users-selected-user-id-put>`_
    """
    return await put_workspaces_workspace_projects_project_key_permissions_config_users_selected_user_id.asyncio(
        workspace, project_key, selected_user_id, client=client.auth, body=body
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def delete_user_permission(client: BBClient, workspace: str, project_key: str, selected_user_id: str) -> None:
    """Remove a user's permission from a project.

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
        await projects.delete_user_permission(
            client,
            workspace="myworkspace",
            project_key="MYPROJ",
            selected_user_id="{abc-123}",
        )
        ```

    References:
        `DELETE /2.0/workspaces/{workspace}/projects/{project_key}/permissions-config/users/{selected_user_id}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-projects/#api-workspaces-workspace-projects-project-key-permissions-config-users-selected-user-id-delete>`_
    """
    await delete_workspaces_workspace_projects_project_key_permissions_config_users_selected_user_id.asyncio(
        workspace, project_key, selected_user_id, client=client.auth
    )
