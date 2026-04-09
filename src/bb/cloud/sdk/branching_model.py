from __future__ import annotations

from bb.cloud.api.branching_model import (
    get_repositories_workspace_repo_slug_branching_model,
    get_repositories_workspace_repo_slug_branching_model_settings,
    get_repositories_workspace_repo_slug_effective_branching_model,
    get_workspaces_workspace_projects_project_key_branching_model,
    get_workspaces_workspace_projects_project_key_branching_model_settings,
    put_repositories_workspace_repo_slug_branching_model_settings,
    put_workspaces_workspace_projects_project_key_branching_model_settings,
)
from bb.cloud.models.branching_model import BranchingModel
from bb.cloud.models.branching_model_settings import BranchingModelSettings
from bb.cloud.models.effective_repo_branching_model import EffectiveRepoBranchingModel
from bb.cloud.sdk._auth_validation import AuthMethod, require_auth
from bb.cloud.sdk._client import BBClient
from bb.cloud.types import UNSET, Unset

__all__ = [
    "get",
    "effective",
    "settings",
    "update_settings",
    "project_get",
    "project_settings",
    "update_project_settings",
]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get(client: BBClient, workspace: str, repo_slug: str) -> BranchingModel | None:
    """Retrieve the branching model configured for a repository.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        repo_slug: Repository slug or UUID.

    Returns:
        A :class:`~bb.cloud.models.branching_model.BranchingModel` object, or ``None`` if not found.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import branching_model

        client = BBClient.from_env()
        model = await branching_model.get(client, workspace="myws", repo_slug="myrepo")
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/branching-model
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-branching-model/#api-repositories-workspace-repo-slug-branching-model-get>`_
    """
    result = await get_repositories_workspace_repo_slug_branching_model.asyncio(
        workspace, repo_slug, client=client.auth
    )
    return result if isinstance(result, BranchingModel) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def effective(client: BBClient, workspace: str, repo_slug: str) -> EffectiveRepoBranchingModel | None:
    """Retrieve the effective branching model for a repository, including project inheritance.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        repo_slug: Repository slug or UUID.

    Returns:
        An :class:`~bb.cloud.models.effective_repo_branching_model.EffectiveRepoBranchingModel` object,
        or ``None`` if not found.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import branching_model

        client = BBClient.from_env()
        model = await branching_model.effective(client, workspace="myws", repo_slug="myrepo")
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/effective-branching-model
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-branching-model/#api-repositories-workspace-repo-slug-effective-branching-model-get>`_
    """
    result = await get_repositories_workspace_repo_slug_effective_branching_model.asyncio(
        workspace, repo_slug, client=client.auth
    )
    return result if isinstance(result, EffectiveRepoBranchingModel) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def settings(client: BBClient, workspace: str, repo_slug: str) -> BranchingModelSettings | None:
    """Retrieve the branching model settings for a repository.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        repo_slug: Repository slug or UUID.

    Returns:
        A :class:`~bb.cloud.models.branching_model_settings.BranchingModelSettings` object,
        or ``None`` if not found.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import branching_model

        client = BBClient.from_env()
        s = await branching_model.settings(client, workspace="myws", repo_slug="myrepo")
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/branching-model/settings
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-branching-model/#api-repositories-workspace-repo-slug-branching-model-settings-get>`_
    """
    result = await get_repositories_workspace_repo_slug_branching_model_settings.asyncio(
        workspace, repo_slug, client=client.auth
    )
    return result if isinstance(result, BranchingModelSettings) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def update_settings(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: BranchingModelSettings | Unset = UNSET,
) -> BranchingModelSettings | None:
    """Update the branching model settings for a repository.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        repo_slug: Repository slug or UUID.
        body: Updated branching model settings payload. Defaults to :data:`~bb.cloud.types.UNSET`.

    Returns:
        The updated :class:`~bb.cloud.models.branching_model_settings.BranchingModelSettings`,
        or ``None`` on error.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import branching_model

        client = BBClient.from_env()
        updated = await branching_model.update_settings(
            client, workspace="myws", repo_slug="myrepo", body=...
        )
        ```

    References:
        `PUT /2.0/repositories/{workspace}/{repo_slug}/branching-model/settings
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-branching-model/#api-repositories-workspace-repo-slug-branching-model-settings-put>`_
    """
    result = await put_repositories_workspace_repo_slug_branching_model_settings.asyncio(
        workspace, repo_slug, client=client.auth, body=body
    )
    return result if isinstance(result, BranchingModelSettings) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def project_get(client: BBClient, workspace: str, project_key: str) -> BranchingModel | None:
    """Retrieve the branching model configured for a project.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        project_key: Project key.

    Returns:
        A :class:`~bb.cloud.models.branching_model.BranchingModel` object, or ``None`` if not found.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import branching_model

        client = BBClient.from_env()
        model = await branching_model.project_get(client, workspace="myws", project_key="PROJ")
        ```

    References:
        `GET /2.0/workspaces/{workspace}/projects/{project_key}/branching-model
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-branching-model/#api-workspaces-workspace-projects-project-key-branching-model-get>`_
    """
    result = await get_workspaces_workspace_projects_project_key_branching_model.asyncio(
        workspace, project_key, client=client.auth
    )
    return result if isinstance(result, BranchingModel) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def project_settings(client: BBClient, workspace: str, project_key: str) -> BranchingModelSettings | None:
    """Retrieve the branching model settings for a project.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        project_key: Project key.

    Returns:
        A :class:`~bb.cloud.models.branching_model_settings.BranchingModelSettings` object,
        or ``None`` if not found.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import branching_model

        client = BBClient.from_env()
        s = await branching_model.project_settings(client, workspace="myws", project_key="PROJ")
        ```

    References:
        `GET /2.0/workspaces/{workspace}/projects/{project_key}/branching-model/settings
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-branching-model/#api-workspaces-workspace-projects-project-key-branching-model-settings-get>`_
    """
    result = await get_workspaces_workspace_projects_project_key_branching_model_settings.asyncio(
        workspace, project_key, client=client.auth
    )
    return result if isinstance(result, BranchingModelSettings) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def update_project_settings(
    client: BBClient,
    workspace: str,
    project_key: str,
    *,
    body: BranchingModelSettings | Unset = UNSET,
) -> BranchingModelSettings | None:
    """Update the branching model settings for a project.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        project_key: Project key.
        body: Updated branching model settings payload. Defaults to :data:`~bb.cloud.types.UNSET`.

    Returns:
        The updated :class:`~bb.cloud.models.branching_model_settings.BranchingModelSettings`,
        or ``None`` on error.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import branching_model

        client = BBClient.from_env()
        updated = await branching_model.update_project_settings(
            client, workspace="myws", project_key="PROJ", body=...
        )
        ```

    References:
        `PUT /2.0/workspaces/{workspace}/projects/{project_key}/branching-model/settings
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-branching-model/#api-workspaces-workspace-projects-project-key-branching-model-settings-put>`_
    """
    result = await put_workspaces_workspace_projects_project_key_branching_model_settings.asyncio(
        workspace, project_key, client=client.auth, body=body
    )
    return result if isinstance(result, BranchingModelSettings) else None
