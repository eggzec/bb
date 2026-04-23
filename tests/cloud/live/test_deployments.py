"""Live tests for ``bb.cloud.sdk.deployments``."""

from __future__ import annotations

import pytest

from bb.cloud.models.deployment import Deployment
from bb.cloud.models.deployment_environment import DeploymentEnvironment
from bb.cloud.models.error import Error
from bb.cloud.sdk import deployments
from bb.cloud.sdk._client import BBClient

pytestmark = pytest.mark.live


async def test_list_returns_deployments(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    result = await deployments.list(client, workspace, probe_repo_slug, pagelen=10)
    if isinstance(result, Error):
        pytest.skip(
            f"deployments.list not available: "
            f"{result.error.message if result.error else result!r}"
        )
    assert isinstance(result, list), (
        f"deployments.list must return list, got {type(result).__name__}"
    )
    for idx, d in enumerate(result):
        assert isinstance(d, Deployment), (
            f"deployments.list[{idx}] is {type(d).__name__}, expected Deployment"
        )


async def test_envs_returns_environments(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    result = await deployments.envs(client, workspace, probe_repo_slug, pagelen=10)
    if isinstance(result, Error):
        pytest.skip(
            f"deployments.envs not available: "
            f"{result.error.message if result.error else result!r}"
        )
    assert isinstance(result, list), (
        f"deployments.envs must return list, got {type(result).__name__}"
    )
    for idx, env in enumerate(result):
        assert isinstance(env, DeploymentEnvironment), (
            f"deployments.envs[{idx}] is {type(env).__name__}, expected DeploymentEnvironment"
        )
