from __future__ import annotations
import asyncio
from bb.cloud.models.branching_model import BranchingModel
from bb.cloud.models.branching_model_settings import BranchingModelSettings
from bb.cloud.models.effective_repo_branching_model import EffectiveRepoBranchingModel
from bb.cloud.sdk._client import BBClient
from bb.cloud.types import UNSET, Unset
from bb.cloud.sdk import branching_model as _async
__all__ = ['get', 'effective', 'settings', 'update_settings', 'project_get', 'project_settings', 'update_project_settings']

def get(client: BBClient, workspace: str, repo_slug: str) -> BranchingModel | None:
    """Retrieve the branching model configured for a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.branching_model.get`.

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
    model = branching_model.get(client, workspace="myws", repo_slug="myrepo")
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/branching-model
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-branching-model/#api-repositories-workspace-repo-slug-branching-model-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.branching_model.get`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.get(client, workspace, repo_slug))

def effective(client: BBClient, workspace: str, repo_slug: str) -> EffectiveRepoBranchingModel | None:
    """Retrieve the effective branching model for a repository, including project inheritance.

Synchronous wrapper around :func:`~bb.cloud.sdk.branching_model.effective`.

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
    model = branching_model.effective(client, workspace="myws", repo_slug="myrepo")
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/effective-branching-model
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-branching-model/#api-repositories-workspace-repo-slug-effective-branching-model-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.branching_model.effective`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.effective(client, workspace, repo_slug))

def settings(client: BBClient, workspace: str, repo_slug: str) -> BranchingModelSettings | None:
    """Retrieve the branching model settings for a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.branching_model.settings`.

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
    s = branching_model.settings(client, workspace="myws", repo_slug="myrepo")
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/branching-model/settings
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-branching-model/#api-repositories-workspace-repo-slug-branching-model-settings-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.branching_model.settings`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.settings(client, workspace, repo_slug))

def update_settings(client: BBClient, workspace: str, repo_slug: str, *, body: BranchingModelSettings | Unset=UNSET) -> BranchingModelSettings | None:
    """Update the branching model settings for a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.branching_model.update_settings`.

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
    updated = branching_model.update_settings(
        client, workspace="myws", repo_slug="myrepo", body=...
    )
    ```

References:
    `PUT /2.0/repositories/{workspace}/{repo_slug}/branching-model/settings
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-branching-model/#api-repositories-workspace-repo-slug-branching-model-settings-put>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.branching_model.update_settings`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.update_settings(client, workspace, repo_slug, body=body))

def project_get(client: BBClient, workspace: str, project_key: str) -> BranchingModel | None:
    """Retrieve the branching model configured for a project.

Synchronous wrapper around :func:`~bb.cloud.sdk.branching_model.project_get`.

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
    model = branching_model.project_get(client, workspace="myws", project_key="PROJ")
    ```

References:
    `GET /2.0/workspaces/{workspace}/projects/{project_key}/branching-model
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-branching-model/#api-workspaces-workspace-projects-project-key-branching-model-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.branching_model.project_get`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.project_get(client, workspace, project_key))

def project_settings(client: BBClient, workspace: str, project_key: str) -> BranchingModelSettings | None:
    """Retrieve the branching model settings for a project.

Synchronous wrapper around :func:`~bb.cloud.sdk.branching_model.project_settings`.

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
    s = branching_model.project_settings(client, workspace="myws", project_key="PROJ")
    ```

References:
    `GET /2.0/workspaces/{workspace}/projects/{project_key}/branching-model/settings
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-branching-model/#api-workspaces-workspace-projects-project-key-branching-model-settings-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.branching_model.project_settings`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.project_settings(client, workspace, project_key))

def update_project_settings(client: BBClient, workspace: str, project_key: str, *, body: BranchingModelSettings | Unset=UNSET) -> BranchingModelSettings | None:
    """Update the branching model settings for a project.

Synchronous wrapper around :func:`~bb.cloud.sdk.branching_model.update_project_settings`.

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
    updated = branching_model.update_project_settings(
        client, workspace="myws", project_key="PROJ", body=...
    )
    ```

References:
    `PUT /2.0/workspaces/{workspace}/projects/{project_key}/branching-model/settings
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-branching-model/#api-workspaces-workspace-projects-project-key-branching-model-settings-put>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.branching_model.update_project_settings`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.update_project_settings(client, workspace, project_key, body=body))
