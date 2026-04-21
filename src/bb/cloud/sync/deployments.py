from __future__ import annotations

import asyncio
from typing import Any

from bb.cloud.models.deploy_key import DeployKey
from bb.cloud.models.deployment import Deployment
from bb.cloud.models.deployment_environment import DeploymentEnvironment
from bb.cloud.models.error import Error
from bb.cloud.sdk import deployments as _async
from bb.cloud.sdk._client import BBClient
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


def list(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    pagelen: int = 25,
) -> list[Deployment] | Error:
    """Sync version of :func:`~bb.cloud.sdk.deployments.list`."""
    return asyncio.run(_async.list(client, workspace, repo_slug, pagelen=pagelen))


def get(client: BBClient, workspace: str, repo_slug: str, deployment_uuid: str) -> Deployment | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.deployments.get`."""
    return asyncio.run(_async.get(client, workspace, repo_slug, deployment_uuid))


def envs(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    pagelen: int = 25,
) -> list[DeploymentEnvironment] | Error:
    """Sync version of :func:`~bb.cloud.sdk.deployments.envs`."""
    return asyncio.run(_async.envs(client, workspace, repo_slug, pagelen=pagelen))


def get_env(
    client: BBClient, workspace: str, repo_slug: str, environment_uuid: str
) -> DeploymentEnvironment | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.deployments.get_env`."""
    return asyncio.run(_async.get_env(client, workspace, repo_slug, environment_uuid))


def create_env(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: DeploymentEnvironment | Unset = UNSET,
) -> DeploymentEnvironment | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.deployments.create_env`."""
    return asyncio.run(_async.create_env(client, workspace, repo_slug, body=body))


def update_env(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    environment_uuid: str,
    *,
    body: DeploymentEnvironment | Unset = UNSET,
) -> DeploymentEnvironment | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.deployments.update_env`."""
    return asyncio.run(_async.update_env(client, workspace, repo_slug, environment_uuid, body=body))


def delete_env(client: BBClient, workspace: str, repo_slug: str, environment_uuid: str) -> None:
    """Sync version of :func:`~bb.cloud.sdk.deployments.delete_env`."""
    asyncio.run(_async.delete_env(client, workspace, repo_slug, environment_uuid))


def deploy_keys(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    pagelen: int = 25,
) -> list[Any] | Error:
    """Sync version of :func:`~bb.cloud.sdk.deployments.deploy_keys`."""
    return asyncio.run(_async.deploy_keys(client, workspace, repo_slug, pagelen=pagelen))


def get_deploy_key(client: BBClient, workspace: str, repo_slug: str, key_id: int) -> Any:
    """Sync version of :func:`~bb.cloud.sdk.deployments.get_deploy_key`."""
    return asyncio.run(_async.get_deploy_key(client, workspace, repo_slug, key_id))


def create_deploy_key(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: DeployKey | Unset = UNSET,
) -> Any:
    """Sync version of :func:`~bb.cloud.sdk.deployments.create_deploy_key`."""
    return asyncio.run(_async.create_deploy_key(client, workspace, repo_slug, body=body))


def update_deploy_key(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    key_id: int,
    *,
    body: DeployKey | Unset = UNSET,
) -> Any:
    """Sync version of :func:`~bb.cloud.sdk.deployments.update_deploy_key`."""
    return asyncio.run(_async.update_deploy_key(client, workspace, repo_slug, key_id, body=body))


def delete_deploy_key(client: BBClient, workspace: str, repo_slug: str, key_id: int) -> None:
    """Sync version of :func:`~bb.cloud.sdk.deployments.delete_deploy_key`."""
    asyncio.run(_async.delete_deploy_key(client, workspace, repo_slug, key_id))


def env_variables(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    environment_uuid: str,
    *,
    pagelen: int = 25,
) -> list[Any] | Error:
    """Sync version of :func:`~bb.cloud.sdk.deployments.env_variables`."""
    return asyncio.run(_async.env_variables(client, workspace, repo_slug, environment_uuid, pagelen=pagelen))


def create_env_variable(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    environment_uuid: str,
    *,
    body: Any | Unset = UNSET,
) -> Any:
    """Sync version of :func:`~bb.cloud.sdk.deployments.create_env_variable`."""
    return asyncio.run(_async.create_env_variable(client, workspace, repo_slug, environment_uuid, body=body))


def update_env_variable(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    environment_uuid: str,
    variable_uuid: str,
    *,
    body: Any | Unset = UNSET,
) -> Any:
    """Sync version of :func:`~bb.cloud.sdk.deployments.update_env_variable`."""
    return asyncio.run(
        _async.update_env_variable(client, workspace, repo_slug, environment_uuid, variable_uuid, body=body)
    )


def delete_env_variable(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    environment_uuid: str,
    variable_uuid: str,
) -> None:
    """Sync version of :func:`~bb.cloud.sdk.deployments.delete_env_variable`."""
    asyncio.run(_async.delete_env_variable(client, workspace, repo_slug, environment_uuid, variable_uuid))
