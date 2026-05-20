from __future__ import annotations
from typing import Any
from bb.cloud.models.deploy_key import DeployKey
from bb.cloud.models.deployment import Deployment
from bb.cloud.models.deployment_environment import DeploymentEnvironment
from bb.cloud.models.error import Error
from bb.cloud.sdk._client import BBClient
from bb.cloud.types import UNSET, Unset
from bb.cloud.sdk import deployments as _async
__all__ = ['list', 'get', 'envs', 'get_env', 'create_env', 'update_env', 'delete_env', 'deploy_keys', 'get_deploy_key', 'create_deploy_key', 'update_deploy_key', 'delete_deploy_key', 'env_variables', 'create_env_variable', 'update_env_variable', 'delete_env_variable']

def list(client: BBClient, workspace: str, repo_slug: str, *, pagelen: int=25) -> list[Deployment] | Error:
    """Return all deployments for a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.deployments.list`.

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
    result = deployments.list(client, workspace="myws", repo_slug="myrepo")
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/deployments
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-deployments/#api-repositories-workspace-repo-slug-deployments-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.deployments.list`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.list(client, workspace, repo_slug, pagelen=pagelen))

def get(client: BBClient, workspace: str, repo_slug: str, deployment_uuid: str) -> Deployment | Error | None:
    """Return a single deployment by UUID.

Synchronous wrapper around :func:`~bb.cloud.sdk.deployments.get`.

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
    deployment = deployments.get(
        client, workspace="myws", repo_slug="myrepo",
        deployment_uuid="{abc-123}"
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/deployments/{deployment_uuid}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-deployments/#api-repositories-workspace-repo-slug-deployments-deployment-uuid-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.deployments.get`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.get(client, workspace, repo_slug, deployment_uuid))

def envs(client: BBClient, workspace: str, repo_slug: str, *, pagelen: int=25) -> list[DeploymentEnvironment] | Error:
    """Return all deployment environments for a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.deployments.envs`.

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
    envs = deployments.envs(client, workspace="myws", repo_slug="myrepo")
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/environments
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-deployments/#api-repositories-workspace-repo-slug-environments-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.deployments.envs`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.envs(client, workspace, repo_slug, pagelen=pagelen))

def get_env(client: BBClient, workspace: str, repo_slug: str, environment_uuid: str) -> DeploymentEnvironment | Error | None:
    """Return a single deployment environment by UUID.

Synchronous wrapper around :func:`~bb.cloud.sdk.deployments.get_env`.

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
    env = deployments.get_env(
        client, workspace="myws", repo_slug="myrepo",
        environment_uuid="{env-uuid}"
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/environments/{environment_uuid}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-deployments/#api-repositories-workspace-repo-slug-environments-environment-uuid-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.deployments.get_env`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.get_env(client, workspace, repo_slug, environment_uuid))

def create_env(client: BBClient, workspace: str, repo_slug: str, *, body: DeploymentEnvironment | Unset=UNSET) -> DeploymentEnvironment | Error | None:
    """Create a deployment environment for a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.deployments.create_env`.

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
    env = deployments.create_env(
        client, workspace="myws", repo_slug="myrepo",
        body=DeploymentEnvironment(name="staging")
    )
    ```

References:
    `POST /2.0/repositories/{workspace}/{repo_slug}/environments
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-deployments/#api-repositories-workspace-repo-slug-environments-post>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.deployments.create_env`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.create_env(client, workspace, repo_slug, body=body))

def update_env(client: BBClient, workspace: str, repo_slug: str, environment_uuid: str, *, body: DeploymentEnvironment | Unset=UNSET) -> DeploymentEnvironment | Error | None:
    """Update a deployment environment.

Synchronous wrapper around :func:`~bb.cloud.sdk.deployments.update_env`.

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
    env = deployments.update_env(
        client, workspace="myws", repo_slug="myrepo",
        environment_uuid="{env-uuid}",
        body=DeploymentEnvironment(name="production")
    )
    ```

References:
    `POST /2.0/repositories/{workspace}/{repo_slug}/environments/{environment_uuid}/changes
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-deployments/#api-repositories-workspace-repo-slug-environments-environment-uuid-changes-post>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.deployments.update_env`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.update_env(client, workspace, repo_slug, environment_uuid, body=body))

def delete_env(client: BBClient, workspace: str, repo_slug: str, environment_uuid: str) -> None:
    """Delete a deployment environment.

Synchronous wrapper around :func:`~bb.cloud.sdk.deployments.delete_env`.

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
    deployments.delete_env(
        client, workspace="myws", repo_slug="myrepo",
        environment_uuid="{env-uuid}"
    )
    ```

References:
    `DELETE /2.0/repositories/{workspace}/{repo_slug}/environments/{environment_uuid}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-deployments/#api-repositories-workspace-repo-slug-environments-environment-uuid-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.deployments.delete_env`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.delete_env(client, workspace, repo_slug, environment_uuid))

def deploy_keys(client: BBClient, workspace: str, repo_slug: str, *, pagelen: int=25) -> list[Any] | Error:
    """Return all deploy keys for a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.deployments.deploy_keys`.

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
    keys = deployments.deploy_keys(client, workspace="myws", repo_slug="myrepo")
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/deploy-keys
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-deployments/#api-repositories-workspace-repo-slug-deploy-keys-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.deployments.deploy_keys`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.deploy_keys(client, workspace, repo_slug, pagelen=pagelen))

def get_deploy_key(client: BBClient, workspace: str, repo_slug: str, key_id: int) -> Any:
    """Return a single deploy key by ID.

Synchronous wrapper around :func:`~bb.cloud.sdk.deployments.get_deploy_key`.

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
    key = deployments.get_deploy_key(
        client, workspace="myws", repo_slug="myrepo", key_id=1234
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/deploy-keys/{key_id}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-deployments/#api-repositories-workspace-repo-slug-deploy-keys-key-id-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.deployments.get_deploy_key`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.get_deploy_key(client, workspace, repo_slug, key_id))

def create_deploy_key(client: BBClient, workspace: str, repo_slug: str, *, body: DeployKey | Unset=UNSET) -> Any:
    """Create a deploy key for a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.deployments.create_deploy_key`.

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
    key = deployments.create_deploy_key(
        client, workspace="myws", repo_slug="myrepo",
        body={"key": "ssh-rsa AAAA...", "label": "CI key"}
    )
    ```

References:
    `POST /2.0/repositories/{workspace}/{repo_slug}/deploy-keys
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-deployments/#api-repositories-workspace-repo-slug-deploy-keys-post>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.deployments.create_deploy_key`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.create_deploy_key(client, workspace, repo_slug, body=body))

def update_deploy_key(client: BBClient, workspace: str, repo_slug: str, key_id: int, *, body: DeployKey | Unset=UNSET) -> Any:
    """Update a deploy key for a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.deployments.update_deploy_key`.

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
    key = deployments.update_deploy_key(
        client, workspace="myws", repo_slug="myrepo",
        key_id=1234, body={"label": "Updated CI key"}
    )
    ```

References:
    `PUT /2.0/repositories/{workspace}/{repo_slug}/deploy-keys/{key_id}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-deployments/#api-repositories-workspace-repo-slug-deploy-keys-key-id-put>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.deployments.update_deploy_key`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.update_deploy_key(client, workspace, repo_slug, key_id, body=body))

def delete_deploy_key(client: BBClient, workspace: str, repo_slug: str, key_id: int) -> None:
    """Delete a deploy key from a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.deployments.delete_deploy_key`.

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
    deployments.delete_deploy_key(
        client, workspace="myws", repo_slug="myrepo", key_id=1234
    )
    ```

References:
    `DELETE /2.0/repositories/{workspace}/{repo_slug}/deploy-keys/{key_id}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-deployments/#api-repositories-workspace-repo-slug-deploy-keys-key-id-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.deployments.delete_deploy_key`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.delete_deploy_key(client, workspace, repo_slug, key_id))

def env_variables(client: BBClient, workspace: str, repo_slug: str, environment_uuid: str, *, pagelen: int=25) -> list[Any] | Error:
    """Return all variables for a deployment environment.

Synchronous wrapper around :func:`~bb.cloud.sdk.deployments.env_variables`.

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
    variables = deployments.env_variables(
        client, workspace="myws", repo_slug="myrepo",
        environment_uuid="{env-uuid}"
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/deployments_config/environments/{environment_uuid}/variables
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-deployments-config-environments-environment-uuid-variables-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.deployments.env_variables`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.env_variables(client, workspace, repo_slug, environment_uuid, pagelen=pagelen))

def create_env_variable(client: BBClient, workspace: str, repo_slug: str, environment_uuid: str, *, body: Any | Unset=UNSET) -> Any:
    """Create a variable for a deployment environment.

Synchronous wrapper around :func:`~bb.cloud.sdk.deployments.create_env_variable`.

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
    var = deployments.create_env_variable(
        client, workspace="myws", repo_slug="myrepo",
        environment_uuid="{env-uuid}",
        body={"key": "MY_SECRET", "value": "abc123", "secured": True}
    )
    ```

References:
    `POST /2.0/repositories/{workspace}/{repo_slug}/deployments_config/environments/{environment_uuid}/variables
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-deployments-config-environments-environment-uuid-variables-post>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.deployments.create_env_variable`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.create_env_variable(client, workspace, repo_slug, environment_uuid, body=body))

def update_env_variable(client: BBClient, workspace: str, repo_slug: str, environment_uuid: str, variable_uuid: str, *, body: Any | Unset=UNSET) -> Any:
    """Update a variable for a deployment environment.

Synchronous wrapper around :func:`~bb.cloud.sdk.deployments.update_env_variable`.

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
    var = deployments.update_env_variable(
        client, workspace="myws", repo_slug="myrepo",
        environment_uuid="{env-uuid}", variable_uuid="{var-uuid}",
        body={"value": "new_value"}
    )
    ```

References:
    `PUT /2.0/repositories/{workspace}/{repo_slug}/deployments_config/environments/{environment_uuid}/variables/{variable_uuid}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-deployments-config-environments-environment-uuid-variables-variable-uuid-put>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.deployments.update_env_variable`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.update_env_variable(client, workspace, repo_slug, environment_uuid, variable_uuid, body=body))

def delete_env_variable(client: BBClient, workspace: str, repo_slug: str, environment_uuid: str, variable_uuid: str) -> None:
    """Delete a variable from a deployment environment.

Synchronous wrapper around :func:`~bb.cloud.sdk.deployments.delete_env_variable`.

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
    deployments.delete_env_variable(
        client, workspace="myws", repo_slug="myrepo",
        environment_uuid="{env-uuid}", variable_uuid="{var-uuid}"
    )
    ```

References:
    `DELETE /2.0/repositories/{workspace}/{repo_slug}/deployments_config/environments/{environment_uuid}/variables/{variable_uuid}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-deployments-config-environments-environment-uuid-variables-variable-uuid-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.deployments.delete_env_variable`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.delete_env_variable(client, workspace, repo_slug, environment_uuid, variable_uuid))
