from __future__ import annotations

from typing import Any

from bb.cloud.api.repositories import (
    delete_repositories_workspace_repo_slug,
    delete_repositories_workspace_repo_slug_permissions_config_groups_group_slug,
    delete_repositories_workspace_repo_slug_permissions_config_users_selected_user_id,
    get_repositories,
    get_repositories_workspace,
    get_repositories_workspace_repo_slug,
    get_repositories_workspace_repo_slug_forks,
    get_repositories_workspace_repo_slug_override_settings,
    get_repositories_workspace_repo_slug_permissions_config_groups,
    get_repositories_workspace_repo_slug_permissions_config_groups_group_slug,
    get_repositories_workspace_repo_slug_permissions_config_users,
    get_repositories_workspace_repo_slug_permissions_config_users_selected_user_id,
    get_repositories_workspace_repo_slug_watchers,
    get_user_permissions_repositories,
    get_user_workspaces_workspace_permissions_repositories,
    post_repositories_workspace_repo_slug,
    post_repositories_workspace_repo_slug_forks,
    put_repositories_workspace_repo_slug,
    put_repositories_workspace_repo_slug_override_settings,
    put_repositories_workspace_repo_slug_permissions_config_groups_group_slug,
    put_repositories_workspace_repo_slug_permissions_config_users_selected_user_id,
)
from bb.cloud.models.repository import Repository
from bb.cloud.sdk._auth_validation import AuthMethod, require_auth
from bb.cloud.sdk._client import BBClient
from bb.cloud.sdk._pagination import async_paginate
from bb.cloud.types import UNSET, Unset

__all__ = [
    "list",
    "list_all",
    "get",
    "create",
    "update",
    "delete",
    "fork",
    "forks",
    "watchers",
    "override_settings",
    "update_override_settings",
    "group_permissions",
    "get_group_permission",
    "set_group_permission",
    "delete_group_permission",
    "user_permissions",
    "get_user_permission",
    "set_user_permission",
    "delete_user_permission",
    "my_permissions",
    "workspace_user_permissions",
]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def list(
    client: BBClient,
    workspace: str,
    *,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    pagelen: int = 25,
) -> list[Repository]:
    """List all repositories in a workspace across all pages.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        q: Query string to filter results. See Bitbucket filtering docs.
        sort: Field to sort results by, prefix with ``-`` for descending.
        pagelen: Number of results per page. Defaults to ``25``.

    Returns:
        All repositories in the workspace across all pages.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import repos

        client = BBClient.from_env()
        result = await repos.list(client, workspace="myworkspace")
        ```

    References:
        `GET /2.0/repositories/{workspace}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-get>`_
    """
    return [
        r
        async for r in async_paginate(
            get_repositories_workspace.asyncio,
            workspace,
            client=client.auth,
            q=q,
            sort=sort,
            pagelen=pagelen,
        )
        if isinstance(r, Repository)
    ]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def list_all(
    client: BBClient,
    *,
    after: str | Unset = UNSET,
    role: str | Unset = UNSET,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    pagelen: int = 25,
) -> list[Repository]:
    """List public repositories across all of Bitbucket Cloud.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        after: Filter repositories created after the given date string.
        role: Filters repositories by the authenticated user's role. E.g. ``owner``,
            ``member``, ``contributor``.
        q: Query string to filter results. See Bitbucket filtering docs.
        sort: Field to sort results by, prefix with ``-`` for descending.
        pagelen: Number of results per page. Defaults to ``25``.

    Returns:
        All matching repositories across all pages.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import repos

        client = BBClient.from_env()
        result = await repos.list_all(client, role="owner")
        ```

    References:
        `GET /2.0/repositories
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-get>`_
    """
    return [
        r
        async for r in async_paginate(
            get_repositories.asyncio,
            client=client.auth,
            after=after,
            role=role,
            q=q,
            sort=sort,
            pagelen=pagelen,
        )
        if isinstance(r, Repository)
    ]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get(client: BBClient, workspace: str, repo_slug: str) -> Repository | None:
    """Fetch a single repository by slug.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        repo_slug: Repository slug or UUID.

    Returns:
        The :class:`~bb.cloud.models.repository.Repository` object, or ``None`` if not found.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import repos

        client = BBClient.from_env()
        repo = await repos.get(client, workspace="myworkspace", repo_slug="myrepo")
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-get>`_
    """
    result = await get_repositories_workspace_repo_slug.asyncio(workspace, repo_slug, client=client.auth)
    return result if isinstance(result, Repository) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def create(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: Repository | Unset = UNSET,
) -> Repository | None:
    """Create a new repository.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        repo_slug: Slug for the new repository.
        body: Repository configuration. Use :class:`~bb.cloud.models.repository.Repository`.

    Returns:
        The created :class:`~bb.cloud.models.repository.Repository`, or ``None`` on error.

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
        repo = await repos.create(
            client,
            workspace="myworkspace",
            repo_slug="newrepo",
            body=Repository(scm="git", is_private=True),
        )
        ```

    References:
        `POST /2.0/repositories/{workspace}/{repo_slug}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-post>`_
    """
    result = await post_repositories_workspace_repo_slug.asyncio(workspace, repo_slug, client=client.auth, body=body)
    return result if isinstance(result, Repository) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def update(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: Repository | Unset = UNSET,
) -> Repository | None:
    """Update an existing repository.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        repo_slug: Repository slug or UUID.
        body: Fields to update. Use :class:`~bb.cloud.models.repository.Repository`.

    Returns:
        The updated :class:`~bb.cloud.models.repository.Repository`, or ``None`` on error.

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
        repo = await repos.update(
            client,
            workspace="myworkspace",
            repo_slug="myrepo",
            body=Repository(description="Updated description"),
        )
        ```

    References:
        `PUT /2.0/repositories/{workspace}/{repo_slug}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-put>`_
    """
    result = await put_repositories_workspace_repo_slug.asyncio(workspace, repo_slug, client=client.auth, body=body)
    return result if isinstance(result, Repository) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def delete(client: BBClient, workspace: str, repo_slug: str) -> None:
    """Delete a repository.

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
        await repos.delete(client, workspace="myworkspace", repo_slug="myrepo")
        ```

    References:
        `DELETE /2.0/repositories/{workspace}/{repo_slug}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-delete>`_
    """
    await delete_repositories_workspace_repo_slug.asyncio(workspace, repo_slug, client=client.auth)


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def fork(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: Repository | Unset = UNSET,
) -> Repository | None:
    """Fork a repository.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        repo_slug: Repository slug or UUID to fork.
        body: Fork configuration. Use :class:`~bb.cloud.models.repository.Repository`.

    Returns:
        The forked :class:`~bb.cloud.models.repository.Repository`, or ``None`` on error.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import repos

        client = BBClient.from_env()
        fork = await repos.fork(client, workspace="myworkspace", repo_slug="myrepo")
        ```

    References:
        `POST /2.0/repositories/{workspace}/{repo_slug}/forks
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-forks-post>`_
    """
    result = await post_repositories_workspace_repo_slug_forks.asyncio(
        workspace, repo_slug, client=client.auth, body=body
    )
    return result if isinstance(result, Repository) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def forks(client: BBClient, workspace: str, repo_slug: str) -> list[Repository]:
    """List all forks of a repository.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        repo_slug: Repository slug or UUID.

    Returns:
        All forks of the repository across all pages.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import repos

        client = BBClient.from_env()
        all_forks = await repos.forks(client, workspace="myworkspace", repo_slug="myrepo")
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/forks
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-forks-get>`_
    """
    return [
        r
        async for r in async_paginate(
            get_repositories_workspace_repo_slug_forks.asyncio,
            workspace,
            repo_slug,
            client=client.auth,
        )
        if isinstance(r, Repository)
    ]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def watchers(client: BBClient, workspace: str, repo_slug: str) -> list[Repository]:
    """List all accounts watching a repository.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        repo_slug: Repository slug or UUID.

    Returns:
        All accounts watching the repository across all pages.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import repos

        client = BBClient.from_env()
        all_watchers = await repos.watchers(client, workspace="myworkspace", repo_slug="myrepo")
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/watchers
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-watchers-get>`_
    """
    return [
        r
        async for r in async_paginate(
            get_repositories_workspace_repo_slug_watchers.asyncio,
            workspace,
            repo_slug,
            client=client.auth,
        )
        if isinstance(r, Repository)
    ]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def override_settings(client: BBClient, workspace: str, repo_slug: str) -> Any | None:
    """Fetch the inheritance override settings for a repository.

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
        settings = await repos.override_settings(client, workspace="myworkspace", repo_slug="myrepo")
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/override-settings
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-override-settings-get>`_
    """
    return await get_repositories_workspace_repo_slug_override_settings.asyncio(
        workspace, repo_slug, client=client.auth
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def update_override_settings(
    client: BBClient, workspace: str, repo_slug: str, *, body: Unset = UNSET
) -> Any | None:
    """Update the inheritance override settings for a repository.

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
        settings = await repos.update_override_settings(
            client, workspace="myworkspace", repo_slug="myrepo"
        )
        ```

    References:
        `PUT /2.0/repositories/{workspace}/{repo_slug}/override-settings
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-override-settings-put>`_
    """
    return await put_repositories_workspace_repo_slug_override_settings.asyncio(
        workspace, repo_slug, client=client.auth, body=body
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def group_permissions(client: BBClient, workspace: str, repo_slug: str, *, pagelen: int = 25) -> list[Any]:
    """List all group permission configurations for a repository.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        repo_slug: Repository slug or UUID.
        pagelen: Number of results per page. Defaults to ``25``.

    Returns:
        All group permission entries across all pages.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import repos

        client = BBClient.from_env()
        perms = await repos.group_permissions(client, workspace="myworkspace", repo_slug="myrepo")
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/permissions-config/groups
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-permissions-config-groups-get>`_
    """
    return [
        p
        async for p in async_paginate(
            get_repositories_workspace_repo_slug_permissions_config_groups.asyncio,
            workspace,
            repo_slug,
            client=client.auth,
            pagelen=pagelen,
        )
    ]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get_group_permission(client: BBClient, workspace: str, repo_slug: str, group_slug: str) -> Any | None:
    """Fetch a specific group's permission configuration for a repository.

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
        perm = await repos.get_group_permission(
            client, workspace="myworkspace", repo_slug="myrepo", group_slug="devs"
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/permissions-config/groups/{group_slug}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-permissions-config-groups-group-slug-get>`_
    """
    return await get_repositories_workspace_repo_slug_permissions_config_groups_group_slug.asyncio(
        workspace, repo_slug, group_slug, client=client.auth
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def set_group_permission(
    client: BBClient, workspace: str, repo_slug: str, group_slug: str, *, body: Unset = UNSET
) -> Any | None:
    """Set a group's permission on a repository.

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
        perm = await repos.set_group_permission(
            client, workspace="myworkspace", repo_slug="myrepo", group_slug="devs"
        )
        ```

    References:
        `PUT /2.0/repositories/{workspace}/{repo_slug}/permissions-config/groups/{group_slug}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-permissions-config-groups-group-slug-put>`_
    """
    return await put_repositories_workspace_repo_slug_permissions_config_groups_group_slug.asyncio(
        workspace, repo_slug, group_slug, client=client.auth, body=body
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def delete_group_permission(client: BBClient, workspace: str, repo_slug: str, group_slug: str) -> None:
    """Remove a group's permission from a repository.

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
        await repos.delete_group_permission(
            client, workspace="myworkspace", repo_slug="myrepo", group_slug="devs"
        )
        ```

    References:
        `DELETE /2.0/repositories/{workspace}/{repo_slug}/permissions-config/groups/{group_slug}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-permissions-config-groups-group-slug-delete>`_
    """
    await delete_repositories_workspace_repo_slug_permissions_config_groups_group_slug.asyncio(
        workspace, repo_slug, group_slug, client=client.auth
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def user_permissions(client: BBClient, workspace: str, repo_slug: str, *, pagelen: int = 25) -> list[Any]:
    """List all user permission configurations for a repository.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        repo_slug: Repository slug or UUID.
        pagelen: Number of results per page. Defaults to ``25``.

    Returns:
        All user permission entries across all pages.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import repos

        client = BBClient.from_env()
        perms = await repos.user_permissions(client, workspace="myworkspace", repo_slug="myrepo")
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/permissions-config/users
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-permissions-config-users-get>`_
    """
    return [
        p
        async for p in async_paginate(
            get_repositories_workspace_repo_slug_permissions_config_users.asyncio,
            workspace,
            repo_slug,
            client=client.auth,
            pagelen=pagelen,
        )
    ]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get_user_permission(client: BBClient, workspace: str, repo_slug: str, selected_user_id: str) -> Any | None:
    """Fetch a specific user's permission configuration for a repository.

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
        perm = await repos.get_user_permission(
            client, workspace="myworkspace", repo_slug="myrepo", selected_user_id="{abc-123}"
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/permissions-config/users/{selected_user_id}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-permissions-config-users-selected-user-id-get>`_
    """
    return await get_repositories_workspace_repo_slug_permissions_config_users_selected_user_id.asyncio(
        workspace, repo_slug, selected_user_id, client=client.auth
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def set_user_permission(
    client: BBClient, workspace: str, repo_slug: str, selected_user_id: str, *, body: Unset = UNSET
) -> Any | None:
    """Set a user's permission on a repository.

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
        perm = await repos.set_user_permission(
            client,
            workspace="myworkspace",
            repo_slug="myrepo",
            selected_user_id="{abc-123}",
        )
        ```

    References:
        `PUT /2.0/repositories/{workspace}/{repo_slug}/permissions-config/users/{selected_user_id}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-permissions-config-users-selected-user-id-put>`_
    """
    return await put_repositories_workspace_repo_slug_permissions_config_users_selected_user_id.asyncio(
        workspace, repo_slug, selected_user_id, client=client.auth, body=body
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def delete_user_permission(client: BBClient, workspace: str, repo_slug: str, selected_user_id: str) -> None:
    """Remove a user's permission from a repository.

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
        await repos.delete_user_permission(
            client,
            workspace="myworkspace",
            repo_slug="myrepo",
            selected_user_id="{abc-123}",
        )
        ```

    References:
        `DELETE /2.0/repositories/{workspace}/{repo_slug}/permissions-config/users/{selected_user_id}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-permissions-config-users-selected-user-id-delete>`_
    """
    await delete_repositories_workspace_repo_slug_permissions_config_users_selected_user_id.asyncio(
        workspace, repo_slug, selected_user_id, client=client.auth
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def my_permissions(client: BBClient, *, pagelen: int = 25) -> list[Any]:
    """List the current user's permissions across all accessible repositories.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        pagelen: Number of results per page. Defaults to ``25``.

    Returns:
        All repository permission entries for the current user across all pages.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import repos

        client = BBClient.from_env()
        perms = await repos.my_permissions(client)
        ```

    References:
        `GET /2.0/user/permissions/repositories
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-user-permissions-repositories-get>`_
    """
    return [
        p
        async for p in async_paginate(
            get_user_permissions_repositories.asyncio,
            client=client.auth,
            pagelen=pagelen,
        )
    ]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def workspace_user_permissions(client: BBClient, workspace: str, *, pagelen: int = 25) -> list[Any]:
    """List the current user's repository permissions within a workspace.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        pagelen: Number of results per page. Defaults to ``25``.

    Returns:
        All repository permission entries for the current user in the workspace across all pages.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import repos

        client = BBClient.from_env()
        perms = await repos.workspace_user_permissions(client, workspace="myworkspace")
        ```

    References:
        `GET /2.0/user/workspaces/{workspace}/permissions/repositories
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-user-workspaces-workspace-permissions-repositories-get>`_
    """
    return [
        p
        async for p in async_paginate(
            get_user_workspaces_workspace_permissions_repositories.asyncio,
            workspace,
            client=client.auth,
            pagelen=pagelen,
        )
    ]
