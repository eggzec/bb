"""Tests for bb.cloud.sdk.pipelines."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from bb.cloud.models.pipeline import Pipeline
from bb.cloud.models.pipeline_known_host import PipelineKnownHost
from bb.cloud.models.pipeline_schedule import PipelineSchedule
from bb.cloud.models.pipeline_ssh_key_pair import PipelineSshKeyPair
from bb.cloud.models.pipeline_variable import PipelineVariable
from bb.cloud.sdk import pipelines
from bb.cloud.sdk._errors import AuthenticationError

_API = "bb.cloud.api.pipelines"


async def test_list_returns_pipelines(mock_client, make_page):
    item = MagicMock(spec=Pipeline)
    with patch(f"{_API}.get_pipelines_for_repository.asyncio", new=AsyncMock(return_value=make_page([item]))):
        result = await pipelines.list(mock_client, "ws", "slug")
    assert result == [item]


async def test_list_empty(mock_client, make_page):
    with patch(f"{_API}.get_pipelines_for_repository.asyncio", new=AsyncMock(return_value=make_page([]))):
        result = await pipelines.list(mock_client, "ws", "slug")
    assert result == []


async def test_get_returns_pipeline(mock_client):
    pipeline = MagicMock(spec=Pipeline)
    with patch(f"{_API}.get_pipeline_for_repository.asyncio", new=AsyncMock(return_value=pipeline)):
        result = await pipelines.get(mock_client, "ws", "slug", "{uuid}")
    assert result is pipeline


async def test_get_returns_none(mock_client):
    with patch(f"{_API}.get_pipeline_for_repository.asyncio", new=AsyncMock(return_value=None)):
        result = await pipelines.get(mock_client, "ws", "slug", "{uuid}")
    assert result is None


async def test_run_returns_pipeline(mock_client):
    pipeline = MagicMock(spec=Pipeline)
    with patch(f"{_API}.create_pipeline_for_repository.asyncio", new=AsyncMock(return_value=pipeline)):
        result = await pipelines.run(mock_client, "ws", "slug", body=MagicMock(spec=Pipeline))
    assert result is pipeline


async def test_stop_returns_none(mock_client):
    with patch(f"{_API}.stop_pipeline.asyncio", new=AsyncMock(return_value=None)):
        result = await pipelines.stop(mock_client, "ws", "slug", "{uuid}")
    assert result is None


async def test_steps_returns_list(mock_client, make_page):
    item = MagicMock()
    with patch(f"{_API}.get_pipeline_steps_for_repository.asyncio", new=AsyncMock(return_value=make_page([item]))):
        result = await pipelines.steps(mock_client, "ws", "slug", "{uuid}")
    assert result == [item]


async def test_step_returns_step(mock_client):
    step = MagicMock()
    with patch(f"{_API}.get_pipeline_step_for_repository.asyncio", new=AsyncMock(return_value=step)):
        result = await pipelines.step(mock_client, "ws", "slug", "{uuid}", "{step-uuid}")
    assert result is step


async def test_step_log_returns_log(mock_client):
    log = MagicMock()
    with patch(f"{_API}.get_pipeline_step_log_for_repository.asyncio", new=AsyncMock(return_value=log)):
        result = await pipelines.step_log(mock_client, "ws", "slug", "{uuid}", "{step-uuid}")
    assert result is log


async def test_config_returns_config(mock_client):
    config = MagicMock()
    with patch(f"{_API}.get_repository_pipeline_config.asyncio", new=AsyncMock(return_value=config)):
        result = await pipelines.config(mock_client, "ws", "slug")
    assert result is config


async def test_update_config_returns_config(mock_client):
    config = MagicMock()
    with patch(f"{_API}.update_repository_pipeline_config.asyncio", new=AsyncMock(return_value=config)):
        result = await pipelines.update_config(mock_client, "ws", "slug")
    assert result is config


async def test_variables_returns_list(mock_client, make_page):
    item = MagicMock(spec=PipelineVariable)
    with patch(f"{_API}.get_repository_pipeline_variables.asyncio", new=AsyncMock(return_value=make_page([item]))):
        result = await pipelines.variables(mock_client, "ws", "slug")
    assert result == [item]


async def test_get_variable_returns_variable(mock_client):
    var = MagicMock(spec=PipelineVariable)
    with patch(f"{_API}.get_repository_pipeline_variable.asyncio", new=AsyncMock(return_value=var)):
        result = await pipelines.get_variable(mock_client, "ws", "slug", "{uuid}")
    assert result is var


async def test_create_variable_returns_variable(mock_client):
    var = MagicMock(spec=PipelineVariable)
    with patch(f"{_API}.create_repository_pipeline_variable.asyncio", new=AsyncMock(return_value=var)):
        result = await pipelines.create_variable(mock_client, "ws", "slug")
    assert result is var


async def test_delete_variable_returns_none(mock_client):
    with patch(f"{_API}.delete_repository_pipeline_variable.asyncio", new=AsyncMock(return_value=None)):
        result = await pipelines.delete_variable(mock_client, "ws", "slug", "{uuid}")
    assert result is None


async def test_schedules_returns_list(mock_client, make_page):
    item = MagicMock(spec=PipelineSchedule)
    with patch(f"{_API}.get_repository_pipeline_schedules.asyncio", new=AsyncMock(return_value=make_page([item]))):
        result = await pipelines.schedules(mock_client, "ws", "slug")
    assert result == [item]


async def test_get_schedule_returns_schedule(mock_client):
    sched = MagicMock(spec=PipelineSchedule)
    with patch(f"{_API}.get_repository_pipeline_schedule.asyncio", new=AsyncMock(return_value=sched)):
        result = await pipelines.get_schedule(mock_client, "ws", "slug", "{uuid}")
    assert result is sched


async def test_create_schedule_returns_schedule(mock_client):
    sched = MagicMock(spec=PipelineSchedule)
    with patch(f"{_API}.create_repository_pipeline_schedule.asyncio", new=AsyncMock(return_value=sched)):
        result = await pipelines.create_schedule(mock_client, "ws", "slug")
    assert result is sched


async def test_delete_schedule_returns_none(mock_client):
    with patch(f"{_API}.delete_repository_pipeline_schedule.asyncio", new=AsyncMock(return_value=None)):
        result = await pipelines.delete_schedule(mock_client, "ws", "slug", "{uuid}")
    assert result is None


async def test_ssh_key_pair_returns_keypair(mock_client):
    keypair = MagicMock(spec=PipelineSshKeyPair)
    with patch(f"{_API}.get_repository_pipeline_ssh_key_pair.asyncio", new=AsyncMock(return_value=keypair)):
        result = await pipelines.ssh_key_pair(mock_client, "ws", "slug")
    assert result is keypair


async def test_known_hosts_returns_list(mock_client, make_page):
    item = MagicMock(spec=PipelineKnownHost)
    with patch(f"{_API}.get_repository_pipeline_known_hosts.asyncio", new=AsyncMock(return_value=make_page([item]))):
        result = await pipelines.known_hosts(mock_client, "ws", "slug")
    assert result == [item]


async def test_workspace_variables_returns_list(mock_client, make_page):
    item = MagicMock(spec=PipelineVariable)
    with patch(f"{_API}.get_pipeline_variables_for_workspace.asyncio", new=AsyncMock(return_value=make_page([item]))):
        result = await pipelines.workspace_variables(mock_client, "ws")
    assert result == [item]


async def test_list_raises_on_bad_auth(bad_auth_client):
    with pytest.raises(AuthenticationError):
        await pipelines.list(bad_auth_client, "ws", "slug")
