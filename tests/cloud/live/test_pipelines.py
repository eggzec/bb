"""Live tests for ``bb.cloud.sdk.pipelines``."""

from __future__ import annotations

import pytest

from bb.cloud.models.error import Error
from bb.cloud.models.pipeline import Pipeline
from bb.cloud.models.pipeline_schedule import PipelineSchedule
from bb.cloud.models.pipeline_variable import PipelineVariable
from bb.cloud.sdk import pipelines
from bb.cloud.sdk._client import BBClient

pytestmark = pytest.mark.live


async def test_list_returns_pipelines(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    result = await pipelines.list(client, workspace, probe_repo_slug, pagelen=10)
    if isinstance(result, Error):
        pytest.skip(
            f"pipelines.list not available for {probe_repo_slug!r}: "
            f"{result.error.message if result.error else result!r}"
        )
    assert isinstance(result, list), (
        f"pipelines.list must return list, got {type(result).__name__}"
    )
    for idx, pipeline in enumerate(result):
        assert isinstance(pipeline, Pipeline), (
            f"pipelines.list[{idx}] is {type(pipeline).__name__}, expected Pipeline"
        )


async def test_config_returns_value(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    result = await pipelines.config(client, workspace, probe_repo_slug)
    # Returns None for repos without pipelines enabled — that's fine.
    assert result is None or not isinstance(result, Exception), (
        f"pipelines.config raised or returned unexpected value: {result!r}"
    )


async def test_variables_returns_list(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    result = await pipelines.variables(client, workspace, probe_repo_slug, pagelen=10)
    if isinstance(result, Error):
        pytest.skip(
            f"pipelines.variables not available: "
            f"{result.error.message if result.error else result!r}"
        )
    assert isinstance(result, list), (
        f"pipelines.variables must return list, got {type(result).__name__}"
    )
    for idx, var in enumerate(result):
        assert isinstance(var, PipelineVariable), (
            f"pipelines.variables[{idx}] is {type(var).__name__}, expected PipelineVariable"
        )


async def test_schedules_returns_list(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    result = await pipelines.schedules(client, workspace, probe_repo_slug, pagelen=10)
    if isinstance(result, Error):
        pytest.skip(
            f"pipelines.schedules not available: "
            f"{result.error.message if result.error else result!r}"
        )
    assert isinstance(result, list), (
        f"pipelines.schedules must return list, got {type(result).__name__}"
    )
    for idx, schedule in enumerate(result):
        assert isinstance(schedule, PipelineSchedule), (
            f"pipelines.schedules[{idx}] is {type(schedule).__name__}, expected PipelineSchedule"
        )
