"""Tests for bb.cloud.sdk.deployments."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from bb.cloud.models.deploy_key import DeployKey
from bb.cloud.models.deployment import Deployment
from bb.cloud.models.deployment_environment import DeploymentEnvironment
from bb.cloud.sdk import deployments
from bb.cloud.sdk._errors import AuthenticationError

_DEP = "bb.cloud.api.deployments"
_PIP = "bb.cloud.api.pipelines"


async def test_list_returns_deployments(mock_client, make_page):
    item = MagicMock(spec=Deployment)
    with patch(f"{_DEP}.get_deployments_for_repository.asyncio", new=AsyncMock(return_value=make_page([item]))):
        result = await deployments.list(mock_client, "ws", "slug")
    assert result == [item]


async def test_get_returns_deployment(mock_client):
    dep = MagicMock(spec=Deployment)
    with patch(f"{_DEP}.get_deployment_for_repository.asyncio", new=AsyncMock(return_value=dep)):
        result = await deployments.get(mock_client, "ws", "slug", "{uuid}")
    assert result is dep


async def test_get_returns_none(mock_client):
    with patch(f"{_DEP}.get_deployment_for_repository.asyncio", new=AsyncMock(return_value=None)):
        result = await deployments.get(mock_client, "ws", "slug", "{uuid}")
    assert result is None


async def test_envs_returns_list(mock_client, make_page):
    item = MagicMock(spec=DeploymentEnvironment)
    with patch(f"{_DEP}.get_environments_for_repository.asyncio", new=AsyncMock(return_value=make_page([item]))):
        result = await deployments.envs(mock_client, "ws", "slug")
    assert result == [item]


async def test_get_env_returns_env(mock_client):
    env = MagicMock(spec=DeploymentEnvironment)
    with patch(f"{_DEP}.get_environment_for_repository.asyncio", new=AsyncMock(return_value=env)):
        result = await deployments.get_env(mock_client, "ws", "slug", "{uuid}")
    assert result is env


async def test_create_env_returns_env(mock_client):
    env = MagicMock(spec=DeploymentEnvironment)
    with patch(f"{_DEP}.create_environment.asyncio", new=AsyncMock(return_value=env)):
        result = await deployments.create_env(mock_client, "ws", "slug")
    assert result is env


async def test_delete_env_returns_none(mock_client):
    with patch(f"{_DEP}.delete_environment_for_repository.asyncio", new=AsyncMock(return_value=None)):
        result = await deployments.delete_env(mock_client, "ws", "slug", "{uuid}")
    assert result is None


async def test_deploy_keys_returns_list(mock_client, make_page):
    item = MagicMock(spec=DeployKey)
    with patch(
        f"{_DEP}.get_repositories_workspace_repo_slug_deploy_keys.asyncio",
        new=AsyncMock(return_value=make_page([item])),
    ):
        result = await deployments.deploy_keys(mock_client, "ws", "slug")
    assert result == [item]


async def test_env_variables_returns_list(mock_client, make_page):
    item = MagicMock()
    with patch(f"{_PIP}.get_deployment_variables.asyncio", new=AsyncMock(return_value=make_page([item]))):
        result = await deployments.env_variables(mock_client, "ws", "slug", "{env-uuid}")
    assert result == [item]


async def test_create_env_variable_returns_var(mock_client):
    var = MagicMock()
    with patch(f"{_PIP}.create_deployment_variable.asyncio", new=AsyncMock(return_value=var)):
        result = await deployments.create_env_variable(mock_client, "ws", "slug", "{env-uuid}")
    assert result is var


async def test_list_raises_on_bad_auth(bad_auth_client):
    with pytest.raises(AuthenticationError):
        await deployments.list(bad_auth_client, "ws", "slug")
