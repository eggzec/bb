from __future__ import annotations

from typing import Any

from bb.cloud.api.deployments import (
    create_environment,
    delete_environment_for_repository,
    delete_repositories_workspace_repo_slug_deploy_keys_key_id,
    get_deployment_for_repository,
    get_deployments_for_repository,
    get_environment_for_repository,
    get_environments_for_repository,
    get_repositories_workspace_repo_slug_deploy_keys,
    get_repositories_workspace_repo_slug_deploy_keys_key_id,
    post_repositories_workspace_repo_slug_deploy_keys,
    put_repositories_workspace_repo_slug_deploy_keys_key_id,
    update_environment_for_repository,
)
from bb.cloud.api.pipelines import (
    create_deployment_variable,
    delete_deployment_variable,
    get_deployment_variables,
    update_deployment_variable,
)
from bb.cloud.models.deploy_key import DeployKey
from bb.cloud.models.deployment import Deployment
from bb.cloud.models.deployment_environment import DeploymentEnvironment
from bb.cloud.sdk._auth_validation import AuthMethod, require_auth
from bb.cloud.sdk._client import BBClient
from bb.cloud.sdk._pagination import async_paginate
from bb.cloud.types import UNSET, Unset

__all__ = [
    "list",
    "get",
    "envs",
    "get_env",
    "create_env",
    "update_env",
    "delete_env",
    "deploy_keys",
    "get_deploy_key",
    "create_deploy_key",
    "update_deploy_key",
    "delete_deploy_key",
    "env_variables",
    "create_env_variable",
    "update_env_variable",
    "delete_env_variable",
]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def list(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    pagelen: int = 25,
) -> list[Deployment]:
    """Return all deployments for a repository.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        repo_slug: Repository slug.
        pagelen: Number of results per page. Defaults to ``25``.

    Returns:
        List of :class:`~bb.cloud.models.deployment.Deployment` objects.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import deployments

        client = BBClient.from_env()
        result = await deployments.list(client, workspace="myws", repo_slug="myrepo")
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/deployments
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-deployments/#api-repositories-workspace-repo-slug-deployments-get>`_
    """
    return [
        d
        async for d in async_paginate(
            get_deployments_for_repository.asyncio,
            workspace,
            repo_slug,
            client=client.auth,
            pagelen=pagelen,
        )
        if isinstance(d, Deployment)
    ]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get(client: BBClient, workspace: str, repo_slug: str, deployment_uuid: str) -> Deployment | None:
    """Return a single deployment by UUID.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        repo_slug: Repository slug.
        deployment_uuid: UUID of the deployment.

    Returns:
        A :class:`~bb.cloud.models.deployment.Deployment` instance, or ``None`` if not found.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import deployments

        client = BBClient.from_env()
        deployment = await deployments.get(
            client, workspace="myws", repo_slug="myrepo",
            deployment_uuid="{abc-123}"
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/deployments/{deployment_uuid}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-deployments/#api-repositories-workspace-repo-slug-deployments-deployment-uuid-get>`_
    """
    result = await get_deployment_for_repository.asyncio(workspace, repo_slug, deployment_uuid, client=client.auth)
    return result if isinstance(result, Deployment) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def envs(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    pagelen: int = 25,
) -> list[DeploymentEnvironment]:
    """Return all deployment environments for a repository.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        repo_slug: Repository slug.
        pagelen: Number of results per page. Defaults to ``25``.

    Returns:
        List of :class:`~bb.cloud.models.deployment_environment.DeploymentEnvironment` objects.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import deployments

        client = BBClient.from_env()
        envs = await deployments.envs(client, workspace="myws", repo_slug="myrepo")
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/environments
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-deployments/#api-repositories-workspace-repo-slug-environments-get>`_
    """
    return [
        e
        async for e in async_paginate(
            get_environments_for_repository.asyncio,
            workspace,
            repo_slug,
            client=client.auth,
            pagelen=pagelen,
        )
        if isinstance(e, DeploymentEnvironment)
    ]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get_env(
    client: BBClient, workspace: str, repo_slug: str, environment_uuid: str
) -> DeploymentEnvironment | None:
    """Return a single deployment environment by UUID.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        repo_slug: Repository slug.
        environment_uuid: UUID of the deployment environment.

    Returns:
        A :class:`~bb.cloud.models.deployment_environment.DeploymentEnvironment` instance,
        or ``None`` if not found.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import deployments

        client = BBClient.from_env()
        env = await deployments.get_env(
            client, workspace="myws", repo_slug="myrepo",
            environment_uuid="{env-uuid}"
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/environments/{environment_uuid}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-deployments/#api-repositories-workspace-repo-slug-environments-environment-uuid-get>`_
    """
    result = await get_environment_for_repository.asyncio(workspace, repo_slug, environment_uuid, client=client.auth)
    return result if isinstance(result, DeploymentEnvironment) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def create_env(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: DeploymentEnvironment | Unset = UNSET,
) -> DeploymentEnvironment | None:
    """Create a deployment environment for a repository.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        repo_slug: Repository slug.
        body: Environment definition. Defaults to :data:`~bb.cloud.types.UNSET`.

    Returns:
        The created :class:`~bb.cloud.models.deployment_environment.DeploymentEnvironment`,
        or ``None`` if the API returned no body.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import deployments
        from bb.cloud.models.deployment_environment import DeploymentEnvironment

        client = BBClient.from_env()
        env = await deployments.create_env(
            client, workspace="myws", repo_slug="myrepo",
            body=DeploymentEnvironment(name="staging")
        )
        ```

    References:
        `POST /2.0/repositories/{workspace}/{repo_slug}/environments
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-deployments/#api-repositories-workspace-repo-slug-environments-post>`_
    """
    result = await create_environment.asyncio(workspace, repo_slug, client=client.auth, body=body)
    return result if isinstance(result, DeploymentEnvironment) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def update_env(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    environment_uuid: str,
    *,
    body: DeploymentEnvironment | Unset = UNSET,
) -> DeploymentEnvironment | None:
    """Update a deployment environment.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        repo_slug: Repository slug.
        environment_uuid: UUID of the deployment environment.
        body: Updated environment definition. Defaults to :data:`~bb.cloud.types.UNSET`.

    Returns:
        The updated :class:`~bb.cloud.models.deployment_environment.DeploymentEnvironment`,
        or ``None`` if the API returned no body.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import deployments
        from bb.cloud.models.deployment_environment import DeploymentEnvironment

        client = BBClient.from_env()
        env = await deployments.update_env(
            client, workspace="myws", repo_slug="myrepo",
            environment_uuid="{env-uuid}",
            body=DeploymentEnvironment(name="production")
        )
        ```

    References:
        `POST /2.0/repositories/{workspace}/{repo_slug}/environments/{environment_uuid}/changes
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-deployments/#api-repositories-workspace-repo-slug-environments-environment-uuid-changes-post>`_
    """
    result = await update_environment_for_repository.asyncio(
        workspace, repo_slug, environment_uuid, client=client.auth, body=body
    )
    return result if isinstance(result, DeploymentEnvironment) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def delete_env(client: BBClient, workspace: str, repo_slug: str, environment_uuid: str) -> None:
    """Delete a deployment environment.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        repo_slug: Repository slug.
        environment_uuid: UUID of the deployment environment to delete.

    Returns:
        ``None``

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import deployments

        client = BBClient.from_env()
        await deployments.delete_env(
            client, workspace="myws", repo_slug="myrepo",
            environment_uuid="{env-uuid}"
        )
        ```

    References:
        `DELETE /2.0/repositories/{workspace}/{repo_slug}/environments/{environment_uuid}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-deployments/#api-repositories-workspace-repo-slug-environments-environment-uuid-delete>`_
    """
    await delete_environment_for_repository.asyncio(workspace, repo_slug, environment_uuid, client=client.auth)


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def deploy_keys(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    pagelen: int = 25,
) -> list[Any]:
    """Return all deploy keys for a repository.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        repo_slug: Repository slug.
        pagelen: Number of results per page. Defaults to ``25``.

    Returns:
        List of deploy key objects.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import deployments

        client = BBClient.from_env()
        keys = await deployments.deploy_keys(client, workspace="myws", repo_slug="myrepo")
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/deploy-keys
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-deployments/#api-repositories-workspace-repo-slug-deploy-keys-get>`_
    """
    return [
        k
        async for k in async_paginate(
            get_repositories_workspace_repo_slug_deploy_keys.asyncio,
            workspace,
            repo_slug,
            client=client.auth,
            pagelen=pagelen,
        )
        if isinstance(k, DeployKey)
    ]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get_deploy_key(client: BBClient, workspace: str, repo_slug: str, key_id: int) -> Any:
    """Return a single deploy key by ID.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        repo_slug: Repository slug.
        key_id: Numeric ID of the deploy key.

    Returns:
        The deploy key object, or ``None`` if not found.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import deployments

        client = BBClient.from_env()
        key = await deployments.get_deploy_key(
            client, workspace="myws", repo_slug="myrepo", key_id=1234
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/deploy-keys/{key_id}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-deployments/#api-repositories-workspace-repo-slug-deploy-keys-key-id-get>`_
    """
    result = await get_repositories_workspace_repo_slug_deploy_keys_key_id.asyncio(
        workspace, repo_slug, key_id, client=client.auth
    )
    return result if isinstance(result, DeployKey) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def create_deploy_key(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: DeployKey | Unset = UNSET,
) -> Any:
    """Create a deploy key for a repository.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        repo_slug: Repository slug.
        body: Deploy key definition. Defaults to :data:`~bb.cloud.types.UNSET`.

    Returns:
        The created deploy key object, or ``None`` if the API returned no body.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import deployments

        client = BBClient.from_env()
        key = await deployments.create_deploy_key(
            client, workspace="myws", repo_slug="myrepo",
            body={"key": "ssh-rsa AAAA...", "label": "CI key"}
        )
        ```

    References:
        `POST /2.0/repositories/{workspace}/{repo_slug}/deploy-keys
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-deployments/#api-repositories-workspace-repo-slug-deploy-keys-post>`_
    """
    result = await post_repositories_workspace_repo_slug_deploy_keys.asyncio(
        workspace, repo_slug, client=client.auth, body=body
    )
    return result if isinstance(result, DeployKey) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def update_deploy_key(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    key_id: int,
    *,
    body: DeployKey | Unset = UNSET,
) -> Any:
    """Update a deploy key for a repository.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        repo_slug: Repository slug.
        key_id: Numeric ID of the deploy key.
        body: Updated deploy key definition. Defaults to :data:`~bb.cloud.types.UNSET`.

    Returns:
        The updated deploy key object, or ``None`` if the API returned no body.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import deployments

        client = BBClient.from_env()
        key = await deployments.update_deploy_key(
            client, workspace="myws", repo_slug="myrepo",
            key_id=1234, body={"label": "Updated CI key"}
        )
        ```

    References:
        `PUT /2.0/repositories/{workspace}/{repo_slug}/deploy-keys/{key_id}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-deployments/#api-repositories-workspace-repo-slug-deploy-keys-key-id-put>`_
    """
    result = await put_repositories_workspace_repo_slug_deploy_keys_key_id.asyncio(
        workspace, repo_slug, key_id, client=client.auth, body=body
    )
    return result if isinstance(result, DeployKey) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def delete_deploy_key(client: BBClient, workspace: str, repo_slug: str, key_id: int) -> None:
    """Delete a deploy key from a repository.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        repo_slug: Repository slug.
        key_id: Numeric ID of the deploy key to delete.

    Returns:
        ``None``

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import deployments

        client = BBClient.from_env()
        await deployments.delete_deploy_key(
            client, workspace="myws", repo_slug="myrepo", key_id=1234
        )
        ```

    References:
        `DELETE /2.0/repositories/{workspace}/{repo_slug}/deploy-keys/{key_id}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-deployments/#api-repositories-workspace-repo-slug-deploy-keys-key-id-delete>`_
    """
    await delete_repositories_workspace_repo_slug_deploy_keys_key_id.asyncio(
        workspace, repo_slug, key_id, client=client.auth
    )


# --- Deployment environment variables ---


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def env_variables(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    environment_uuid: str,
    *,
    pagelen: int = 25,
) -> list[Any]:
    """Return all variables for a deployment environment.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        repo_slug: Repository slug.
        environment_uuid: UUID of the deployment environment.
        pagelen: Number of results per page. Defaults to ``25``.

    Returns:
        List of deployment variable objects.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import deployments

        client = BBClient.from_env()
        variables = await deployments.env_variables(
            client, workspace="myws", repo_slug="myrepo",
            environment_uuid="{env-uuid}"
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/deployments_config/environments/{environment_uuid}/variables
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-deployments-config-environments-environment-uuid-variables-get>`_
    """
    return [
        v
        async for v in async_paginate(
            get_deployment_variables.asyncio,
            workspace,
            repo_slug,
            environment_uuid,
            client=client.auth,
            pagelen=pagelen,
        )
    ]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def create_env_variable(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    environment_uuid: str,
    *,
    body: Any | Unset = UNSET,
) -> Any:
    """Create a variable for a deployment environment.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        repo_slug: Repository slug.
        environment_uuid: UUID of the deployment environment.
        body: Variable definition. Defaults to :data:`~bb.cloud.types.UNSET`.

    Returns:
        The created variable object, or ``None`` if the API returned no body.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import deployments

        client = BBClient.from_env()
        var = await deployments.create_env_variable(
            client, workspace="myws", repo_slug="myrepo",
            environment_uuid="{env-uuid}",
            body={"key": "MY_SECRET", "value": "abc123", "secured": True}
        )
        ```

    References:
        `POST /2.0/repositories/{workspace}/{repo_slug}/deployments_config/environments/{environment_uuid}/variables
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-deployments-config-environments-environment-uuid-variables-post>`_
    """
    return await create_deployment_variable.asyncio(
        workspace, repo_slug, environment_uuid, client=client.auth, body=body
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def update_env_variable(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    environment_uuid: str,
    variable_uuid: str,
    *,
    body: Any | Unset = UNSET,
) -> Any:
    """Update a variable for a deployment environment.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        repo_slug: Repository slug.
        environment_uuid: UUID of the deployment environment.
        variable_uuid: UUID of the variable to update.
        body: Updated variable definition. Defaults to :data:`~bb.cloud.types.UNSET`.

    Returns:
        The updated variable object, or ``None`` if the API returned no body.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import deployments

        client = BBClient.from_env()
        var = await deployments.update_env_variable(
            client, workspace="myws", repo_slug="myrepo",
            environment_uuid="{env-uuid}", variable_uuid="{var-uuid}",
            body={"value": "new_value"}
        )
        ```

    References:
        `PUT /2.0/repositories/{workspace}/{repo_slug}/deployments_config/environments/{environment_uuid}/variables/{variable_uuid}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-deployments-config-environments-environment-uuid-variables-variable-uuid-put>`_
    """
    return await update_deployment_variable.asyncio(
        workspace, repo_slug, environment_uuid, variable_uuid, client=client.auth, body=body
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def delete_env_variable(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    environment_uuid: str,
    variable_uuid: str,
) -> None:
    """Delete a variable from a deployment environment.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        repo_slug: Repository slug.
        environment_uuid: UUID of the deployment environment.
        variable_uuid: UUID of the variable to delete.

    Returns:
        ``None``

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import deployments

        client = BBClient.from_env()
        await deployments.delete_env_variable(
            client, workspace="myws", repo_slug="myrepo",
            environment_uuid="{env-uuid}", variable_uuid="{var-uuid}"
        )
        ```

    References:
        `DELETE /2.0/repositories/{workspace}/{repo_slug}/deployments_config/environments/{environment_uuid}/variables/{variable_uuid}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-deployments-config-environments-environment-uuid-variables-variable-uuid-delete>`_
    """
    await delete_deployment_variable.asyncio(workspace, repo_slug, environment_uuid, variable_uuid, client=client.auth)
