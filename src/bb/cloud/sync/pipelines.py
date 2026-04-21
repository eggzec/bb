from __future__ import annotations

import asyncio
from typing import Any

from bb.cloud.models.error import Error
from bb.cloud.models.pipeline import Pipeline
from bb.cloud.models.pipeline_known_host import PipelineKnownHost
from bb.cloud.models.pipeline_schedule import PipelineSchedule
from bb.cloud.models.pipeline_ssh_key_pair import PipelineSshKeyPair
from bb.cloud.models.pipeline_variable import PipelineVariable
from bb.cloud.sdk import pipelines as _async
from bb.cloud.sdk._client import BBClient
from bb.cloud.types import UNSET, Unset

__all__ = [
    "list",
    "get",
    "run",
    "stop",
    "steps",
    "step",
    "step_log",
    "config",
    "update_config",
    "variables",
    "get_variable",
    "create_variable",
    "update_variable",
    "delete_variable",
    "schedules",
    "get_schedule",
    "create_schedule",
    "update_schedule",
    "delete_schedule",
    "known_hosts",
    "get_known_host",
    "create_known_host",
    "update_known_host",
    "delete_known_host",
    "ssh_key_pair",
    "update_ssh_key_pair",
    "delete_ssh_key_pair",
    "caches",
    "delete_cache",
    "oidc_config",
    "oidc_keys",
    "workspace_variables",
    "get_workspace_variable",
    "create_workspace_variable",
    "update_workspace_variable",
    "delete_workspace_variable",
    "runners",
    "get_runner",
    "create_runner",
    "update_runner",
    "delete_runner",
    "workspace_runners",
    "get_workspace_runner",
    "create_workspace_runner",
    "update_workspace_runner",
    "delete_workspace_runner",
    "test_reports",
    "test_cases",
    "test_case_reasons",
    "container_log",
    "cache_uri",
    "clear_caches",
    "schedule_executions",
    "update_build_number",
]


def list(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    pagelen: int = 10,
) -> list[Pipeline] | Error:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.list`."""
    return asyncio.run(_async.list(client, workspace, repo_slug, pagelen=pagelen))


def get(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    pipeline_uuid: str,
) -> Pipeline | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.get`."""
    return asyncio.run(_async.get(client, workspace, repo_slug, pipeline_uuid))


def run(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: Pipeline,
) -> Pipeline | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.run`."""
    return asyncio.run(_async.run(client, workspace, repo_slug, body=body))


def stop(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    pipeline_uuid: str,
) -> None:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.stop`."""
    asyncio.run(_async.stop(client, workspace, repo_slug, pipeline_uuid))


def steps(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    pipeline_uuid: str,
    *,
    pagelen: int = 25,
) -> list[Any] | Error:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.steps`."""
    return asyncio.run(_async.steps(client, workspace, repo_slug, pipeline_uuid, pagelen=pagelen))


def step(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    pipeline_uuid: str,
    step_uuid: str,
) -> Any:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.step`."""
    return asyncio.run(_async.step(client, workspace, repo_slug, pipeline_uuid, step_uuid))


def step_log(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    pipeline_uuid: str,
    step_uuid: str,
) -> str | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.step_log`."""
    return asyncio.run(_async.step_log(client, workspace, repo_slug, pipeline_uuid, step_uuid))


def config(
    client: BBClient,
    workspace: str,
    repo_slug: str,
) -> Any:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.config`."""
    return asyncio.run(_async.config(client, workspace, repo_slug))


def update_config(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: Unset = UNSET,
) -> Any:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.update_config`."""
    return asyncio.run(_async.update_config(client, workspace, repo_slug, body=body))


def variables(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    pagelen: int = 25,
) -> list[PipelineVariable] | Error:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.variables`."""
    return asyncio.run(_async.variables(client, workspace, repo_slug, pagelen=pagelen))


def get_variable(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    variable_uuid: str,
) -> PipelineVariable | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.get_variable`."""
    return asyncio.run(_async.get_variable(client, workspace, repo_slug, variable_uuid))


def create_variable(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: PipelineVariable | Unset = UNSET,
) -> PipelineVariable | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.create_variable`."""
    return asyncio.run(_async.create_variable(client, workspace, repo_slug, body=body))


def update_variable(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    variable_uuid: str,
    *,
    body: PipelineVariable | Unset = UNSET,
) -> PipelineVariable | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.update_variable`."""
    return asyncio.run(_async.update_variable(client, workspace, repo_slug, variable_uuid, body=body))


def delete_variable(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    variable_uuid: str,
) -> None:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.delete_variable`."""
    asyncio.run(_async.delete_variable(client, workspace, repo_slug, variable_uuid))


def schedules(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    pagelen: int = 25,
) -> list[PipelineSchedule] | Error:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.schedules`."""
    return asyncio.run(_async.schedules(client, workspace, repo_slug, pagelen=pagelen))


def get_schedule(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    schedule_uuid: str,
) -> PipelineSchedule | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.get_schedule`."""
    return asyncio.run(_async.get_schedule(client, workspace, repo_slug, schedule_uuid))


def create_schedule(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: PipelineSchedule | Unset = UNSET,
) -> PipelineSchedule | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.create_schedule`."""
    return asyncio.run(_async.create_schedule(client, workspace, repo_slug, body=body))


def update_schedule(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    schedule_uuid: str,
    *,
    body: PipelineSchedule | Unset = UNSET,
) -> PipelineSchedule | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.update_schedule`."""
    return asyncio.run(_async.update_schedule(client, workspace, repo_slug, schedule_uuid, body=body))


def delete_schedule(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    schedule_uuid: str,
) -> None:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.delete_schedule`."""
    asyncio.run(_async.delete_schedule(client, workspace, repo_slug, schedule_uuid))


def known_hosts(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    pagelen: int = 25,
) -> list[PipelineKnownHost] | Error:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.known_hosts`."""
    return asyncio.run(_async.known_hosts(client, workspace, repo_slug, pagelen=pagelen))


def get_known_host(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    known_host_uuid: str,
) -> PipelineKnownHost | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.get_known_host`."""
    return asyncio.run(_async.get_known_host(client, workspace, repo_slug, known_host_uuid))


def create_known_host(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: PipelineKnownHost | Unset = UNSET,
) -> PipelineKnownHost | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.create_known_host`."""
    return asyncio.run(_async.create_known_host(client, workspace, repo_slug, body=body))


def update_known_host(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    known_host_uuid: str,
    *,
    body: PipelineKnownHost | Unset = UNSET,
) -> PipelineKnownHost | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.update_known_host`."""
    return asyncio.run(_async.update_known_host(client, workspace, repo_slug, known_host_uuid, body=body))


def delete_known_host(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    known_host_uuid: str,
) -> None:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.delete_known_host`."""
    asyncio.run(_async.delete_known_host(client, workspace, repo_slug, known_host_uuid))


def ssh_key_pair(
    client: BBClient,
    workspace: str,
    repo_slug: str,
) -> PipelineSshKeyPair | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.ssh_key_pair`."""
    return asyncio.run(_async.ssh_key_pair(client, workspace, repo_slug))


def update_ssh_key_pair(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: PipelineSshKeyPair | Unset = UNSET,
) -> PipelineSshKeyPair | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.update_ssh_key_pair`."""
    return asyncio.run(_async.update_ssh_key_pair(client, workspace, repo_slug, body=body))


def delete_ssh_key_pair(
    client: BBClient,
    workspace: str,
    repo_slug: str,
) -> None:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.delete_ssh_key_pair`."""
    asyncio.run(_async.delete_ssh_key_pair(client, workspace, repo_slug))


def caches(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    pagelen: int = 25,
) -> list[Any] | Error:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.caches`."""
    return asyncio.run(_async.caches(client, workspace, repo_slug, pagelen=pagelen))


def delete_cache(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    cache_uuid: str,
) -> None:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.delete_cache`."""
    asyncio.run(_async.delete_cache(client, workspace, repo_slug, cache_uuid))


def oidc_config(
    client: BBClient,
    workspace: str,
    repo_slug: str,
) -> Any:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.oidc_config`."""
    return asyncio.run(_async.oidc_config(client, workspace, repo_slug))


def oidc_keys(
    client: BBClient,
    workspace: str,
    repo_slug: str,
) -> Any:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.oidc_keys`."""
    return asyncio.run(_async.oidc_keys(client, workspace, repo_slug))


def workspace_variables(
    client: BBClient,
    workspace: str,
    *,
    pagelen: int = 25,
) -> list[PipelineVariable] | Error:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.workspace_variables`."""
    return asyncio.run(_async.workspace_variables(client, workspace, pagelen=pagelen))


def get_workspace_variable(
    client: BBClient,
    workspace: str,
    variable_uuid: str,
) -> PipelineVariable | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.get_workspace_variable`."""
    return asyncio.run(_async.get_workspace_variable(client, workspace, variable_uuid))


def create_workspace_variable(
    client: BBClient,
    workspace: str,
    *,
    body: PipelineVariable | Unset = UNSET,
) -> PipelineVariable | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.create_workspace_variable`."""
    return asyncio.run(_async.create_workspace_variable(client, workspace, body=body))


def update_workspace_variable(
    client: BBClient,
    workspace: str,
    variable_uuid: str,
    *,
    body: PipelineVariable | Unset = UNSET,
) -> PipelineVariable | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.update_workspace_variable`."""
    return asyncio.run(_async.update_workspace_variable(client, workspace, variable_uuid, body=body))


def delete_workspace_variable(
    client: BBClient,
    workspace: str,
    variable_uuid: str,
) -> None:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.delete_workspace_variable`."""
    asyncio.run(_async.delete_workspace_variable(client, workspace, variable_uuid))


def runners(
    client: BBClient,
    workspace: str,
    repo_slug: str,
) -> Any:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.runners`."""
    return asyncio.run(_async.runners(client, workspace, repo_slug))


def get_runner(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    runner_uuid: str,
) -> Any:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.get_runner`."""
    return asyncio.run(_async.get_runner(client, workspace, repo_slug, runner_uuid))


def create_runner(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: Unset = UNSET,
) -> Any:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.create_runner`."""
    return asyncio.run(_async.create_runner(client, workspace, repo_slug, body=body))


def update_runner(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    runner_uuid: str,
    *,
    body: Unset = UNSET,
) -> Any:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.update_runner`."""
    return asyncio.run(_async.update_runner(client, workspace, repo_slug, runner_uuid, body=body))


def delete_runner(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    runner_uuid: str,
) -> None:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.delete_runner`."""
    asyncio.run(_async.delete_runner(client, workspace, repo_slug, runner_uuid))


def workspace_runners(
    client: BBClient,
    workspace: str,
) -> Any:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.workspace_runners`."""
    return asyncio.run(_async.workspace_runners(client, workspace))


def get_workspace_runner(
    client: BBClient,
    workspace: str,
    runner_uuid: str,
) -> Any:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.get_workspace_runner`."""
    return asyncio.run(_async.get_workspace_runner(client, workspace, runner_uuid))


def create_workspace_runner(
    client: BBClient,
    workspace: str,
    *,
    body: Unset = UNSET,
) -> Any:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.create_workspace_runner`."""
    return asyncio.run(_async.create_workspace_runner(client, workspace, body=body))


def update_workspace_runner(
    client: BBClient,
    workspace: str,
    runner_uuid: str,
    *,
    body: Unset = UNSET,
) -> Any:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.update_workspace_runner`."""
    return asyncio.run(_async.update_workspace_runner(client, workspace, runner_uuid, body=body))


def delete_workspace_runner(
    client: BBClient,
    workspace: str,
    runner_uuid: str,
) -> None:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.delete_workspace_runner`."""
    asyncio.run(_async.delete_workspace_runner(client, workspace, runner_uuid))


def test_reports(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    pipeline_uuid: str,
) -> Any:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.test_reports`."""
    return asyncio.run(_async.test_reports(client, workspace, repo_slug, pipeline_uuid))


def test_cases(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    pipeline_uuid: str,
    report_uuid: str,
) -> Any:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.test_cases`."""
    return asyncio.run(_async.test_cases(client, workspace, repo_slug, pipeline_uuid, report_uuid))


def test_case_reasons(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    pipeline_uuid: str,
    report_uuid: str,
    test_case_uuid: str,
) -> Any:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.test_case_reasons`."""
    return asyncio.run(
        _async.test_case_reasons(client, workspace, repo_slug, pipeline_uuid, report_uuid, test_case_uuid)
    )


def container_log(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    pipeline_uuid: str,
    step_uuid: str,
    service_name: str,
) -> Any:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.container_log`."""
    return asyncio.run(_async.container_log(client, workspace, repo_slug, pipeline_uuid, step_uuid, service_name))


def cache_uri(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    cache_uuid: str,
) -> Any:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.cache_uri`."""
    return asyncio.run(_async.cache_uri(client, workspace, repo_slug, cache_uuid))


def clear_caches(
    client: BBClient,
    workspace: str,
    repo_slug: str,
) -> None:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.clear_caches`."""
    asyncio.run(_async.clear_caches(client, workspace, repo_slug))


def schedule_executions(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    schedule_uuid: str,
) -> Any:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.schedule_executions`."""
    return asyncio.run(_async.schedule_executions(client, workspace, repo_slug, schedule_uuid))


def update_build_number(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: Unset = UNSET,
) -> Any:
    """Sync version of :func:`~bb.cloud.sdk.pipelines.update_build_number`."""
    return asyncio.run(_async.update_build_number(client, workspace, repo_slug, body=body))
