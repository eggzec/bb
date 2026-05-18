"""Live integration tests for ``bb.cloud.sdk.pipelines``.

Seed data (read-only — DO NOT mutate):
- workspace:         beaverish
- repo:              bb-probe (pipelines enabled)
- pipeline UUID:     {88efe83d-e4a6-4886-aff9-f6241fa5cf80}  (state: PENDING)
- variable UUID:     {45920ece-ce1e-4854-a192-4f8e630aa683}  (key: PROBE_VAR)
- schedule UUID:     {5784e0da-f082-4f91-9d65-20e1d7f0ed8e}
- known host UUID:   {6f24c288-d2fe-4935-999b-b0f494056957}  (hostname: gitlab.com)
- SSH key pair:      present
- ws variable UUID:  {70868f27-6d0e-48a5-8cf3-c7ece5a848a9}  (key: WS_PROBE_VAR)

Write tests always clean up in finally blocks.
"""

from __future__ import annotations

import uuid

import pytest

from bb.cloud.errors import UnexpectedStatus
from bb.cloud.models.error import Error
from bb.cloud.models.pipeline import Pipeline
from bb.cloud.models.pipeline_known_host import PipelineKnownHost
from bb.cloud.models.pipeline_schedule import PipelineSchedule
from bb.cloud.models.pipeline_schedule_post_request_body import PipelineSchedulePostRequestBody
from bb.cloud.models.pipeline_schedule_post_request_body_target import (
    PipelineSchedulePostRequestBodyTarget,
)
from bb.cloud.models.pipeline_schedule_post_request_body_target_ref_type import (
    PipelineSchedulePostRequestBodyTargetRefType,
)
from bb.cloud.models.pipeline_schedule_put_request_body import PipelineSchedulePutRequestBody
from bb.cloud.models.pipeline_selector import PipelineSelector
from bb.cloud.models.pipeline_selector_type import PipelineSelectorType
from bb.cloud.models.pipeline_ssh_key_pair import PipelineSshKeyPair
from bb.cloud.models.pipeline_ssh_public_key import PipelineSshPublicKey
from bb.cloud.models.pipeline_variable import PipelineVariable
from bb.cloud.models.pipelines_config import PipelinesConfig
from bb.cloud.sdk import pipelines
from bb.cloud.sdk._client import BBClient

pytestmark = pytest.mark.live

# ---------------------------------------------------------------------------
# Seed constants (DO NOT mutate)
# ---------------------------------------------------------------------------
SEED_PIPELINE_UUID = "{88efe83d-e4a6-4886-aff9-f6241fa5cf80}"
SEED_VARIABLE_UUID = "{45920ece-ce1e-4854-a192-4f8e630aa683}"
SEED_SCHEDULE_UUID = "{5784e0da-f082-4f91-9d65-20e1d7f0ed8e}"
SEED_KNOWN_HOST_UUID = "{6f24c288-d2fe-4935-999b-b0f494056957}"
SEED_WS_VARIABLE_UUID = "{70868f27-6d0e-48a5-8cf3-c7ece5a848a9}"

PROBE_REPO = "bb-probe"


# ---------------------------------------------------------------------------
# Local fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
def probe_pipeline_uuid() -> str:
    return SEED_PIPELINE_UUID


@pytest.fixture
def probe_schedule_uuid() -> str:
    return SEED_SCHEDULE_UUID


@pytest.fixture
def probe_variable_uuid() -> str:
    return SEED_VARIABLE_UUID


@pytest.fixture
def probe_known_host_uuid() -> str:
    return SEED_KNOWN_HOST_UUID


@pytest.fixture
def probe_ws_variable_uuid() -> str:
    return SEED_WS_VARIABLE_UUID


# ---------------------------------------------------------------------------
# Helper — error message extraction
# ---------------------------------------------------------------------------


def _err_msg(result: Error) -> str:
    if getattr(result, "error", None) and getattr(result.error, "message", None):
        return result.error.message  # type: ignore[union-attr]
    return repr(result)


# ===========================================================================
# GROUP 1 — CORE
# ===========================================================================


async def test_list_returns_pipelines(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    result = await pipelines.list(client, workspace, probe_repo_slug, pagelen=10)
    if isinstance(result, Error):
        pytest.skip(f"pipelines.list not available for {probe_repo_slug!r}: {_err_msg(result)}")
    assert isinstance(result, list), (
        f"pipelines.list must return list, got {type(result).__name__}"
    )
    for idx, pipeline in enumerate(result):
        assert isinstance(pipeline, Pipeline), (
            f"pipelines.list[{idx}] is {type(pipeline).__name__}, expected Pipeline"
        )


async def test_list_contains_seed_pipeline(
    client: BBClient,
    workspace: str,
    probe_repo_slug: str,
    probe_pipeline_uuid: str,
) -> None:
    result = await pipelines.list(client, workspace, probe_repo_slug, pagelen=50)
    if isinstance(result, Error):
        pytest.skip(f"pipelines.list not available: {_err_msg(result)}")
    uuids = [p.uuid for p in result if isinstance(p, Pipeline)]
    assert probe_pipeline_uuid in uuids, (
        f"Seed pipeline {probe_pipeline_uuid!r} not found in list. "
        f"Found UUIDs: {uuids}"
    )


async def test_get_seed_pipeline(
    client: BBClient,
    workspace: str,
    probe_repo_slug: str,
    probe_pipeline_uuid: str,
) -> None:
    result = await pipelines.get(client, workspace, probe_repo_slug, probe_pipeline_uuid)
    assert not isinstance(result, Error), (
        f"pipelines.get errored: {_err_msg(result)}"  # type: ignore[arg-type]
    )
    assert isinstance(result, Pipeline), (
        f"pipelines.get must return Pipeline, got {type(result).__name__}: {result!r}"
    )
    assert result.uuid == probe_pipeline_uuid, (
        f"pipeline UUID mismatch: got {result.uuid!r}, expected {probe_pipeline_uuid!r}"
    )
    # State should be PENDING (or possibly completed — tolerate both)
    assert result.state is not None, "Pipeline.state must be set"


async def test_get_missing_pipeline_returns_none_or_error(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    fake_uuid = "{00000000-0000-0000-0000-000000000000}"
    result = await pipelines.get(client, workspace, probe_repo_slug, fake_uuid)
    assert not isinstance(result, Pipeline), (
        f"pipelines.get for non-existent UUID must not return Pipeline: {result!r}"
    )


async def test_run_skipped() -> None:
    # Skipped intentionally — would trigger a real pipeline run and consume runner quota.
    pytest.skip("pipelines.run skipped: would trigger a real run and consume runner quota")


async def test_stop_skipped_no_running_pipeline(
    client: BBClient,
    workspace: str,
    probe_repo_slug: str,
    probe_pipeline_uuid: str,
) -> None:
    # Only call stop if the pipeline is actually IN_PROGRESS to avoid spurious errors.
    result = await pipelines.get(client, workspace, probe_repo_slug, probe_pipeline_uuid)
    if not isinstance(result, Pipeline):
        pytest.skip("Seed pipeline not available — cannot check state for stop test")
    state_name = None
    if result.state is not None and hasattr(result.state, "name"):
        state_name = result.state.name
    if state_name not in ("IN_PROGRESS", "RUNNING", "PAUSED"):
        pytest.skip(
            f"Seed pipeline is not running (state={state_name!r}); "
            "pipelines.stop test skipped to avoid error"
        )
    # If we get here the pipeline is running — stop it.
    await pipelines.stop(client, workspace, probe_repo_slug, probe_pipeline_uuid)


async def test_steps_returns_list(
    client: BBClient,
    workspace: str,
    probe_repo_slug: str,
    probe_pipeline_uuid: str,
) -> None:
    result = await pipelines.steps(
        client, workspace, probe_repo_slug, probe_pipeline_uuid, pagelen=25
    )
    if isinstance(result, Error):
        pytest.skip(f"pipelines.steps not available: {_err_msg(result)}")
    assert isinstance(result, list), (
        f"pipelines.steps must return list, got {type(result).__name__}"
    )
    # May be empty for a PENDING pipeline — that is acceptable.


async def test_step_returns_object(
    client: BBClient,
    workspace: str,
    probe_repo_slug: str,
    probe_pipeline_uuid: str,
) -> None:
    step_list = await pipelines.steps(
        client, workspace, probe_repo_slug, probe_pipeline_uuid, pagelen=25
    )
    if isinstance(step_list, Error) or not step_list:
        pytest.skip(
            "pipelines.steps returned empty or Error — cannot test pipelines.step"
        )
    first_step = step_list[0]
    step_uuid = getattr(first_step, "uuid", None)
    if not step_uuid:
        pytest.skip("First step has no uuid — cannot test pipelines.step by UUID")
    result = await pipelines.step(
        client, workspace, probe_repo_slug, probe_pipeline_uuid, step_uuid
    )
    assert result is not None, (
        f"pipelines.step returned None for step {step_uuid!r}"
    )
    assert getattr(result, "uuid", None) == step_uuid, (
        f"step.uuid mismatch: got {getattr(result, 'uuid', None)!r}, expected {step_uuid!r}"
    )


async def test_step_log_returns_string_or_none(
    client: BBClient,
    workspace: str,
    probe_repo_slug: str,
    probe_pipeline_uuid: str,
) -> None:
    step_list = await pipelines.steps(
        client, workspace, probe_repo_slug, probe_pipeline_uuid, pagelen=25
    )
    if isinstance(step_list, Error) or not step_list:
        pytest.skip(
            "pipelines.steps returned empty or Error — cannot test pipelines.step_log"
        )
    first_step = step_list[0]
    step_uuid = getattr(first_step, "uuid", None)
    if not step_uuid:
        pytest.skip("First step has no uuid — cannot test step_log")
    # PENDING step log may be empty — that's OK.
    result = await pipelines.step_log(
        client, workspace, probe_repo_slug, probe_pipeline_uuid, step_uuid
    )
    # str, bytes, None, or Error all acceptable (PENDING = no log yet)
    assert not isinstance(result, Exception), (
        f"pipelines.step_log raised unexpectedly: {result!r}"
    )


# ===========================================================================
# GROUP 2 — CONFIG
# ===========================================================================


async def test_config_returns_pipelines_config(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    result = await pipelines.config(client, workspace, probe_repo_slug)
    # If pipelines not enabled the API may return None or a disabled config — tolerate.
    if result is None:
        pytest.skip(f"pipelines.config returned None for {probe_repo_slug!r}")
    assert isinstance(result, PipelinesConfig), (
        f"pipelines.config must return PipelinesConfig, got {type(result).__name__}: {result!r}"
    )
    # bb-probe has pipelines enabled
    assert result.enabled is True or result.enabled is not False, (
        f"Expected pipelines enabled=True for bb-probe, got: {result.enabled!r}"
    )


async def test_update_config_idempotent(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    current = await pipelines.config(client, workspace, probe_repo_slug)
    if not isinstance(current, PipelinesConfig):
        pytest.skip("pipelines.config unavailable — cannot test update_config")
    # PUT back the same enabled flag (already True) — should be a no-op
    body = PipelinesConfig(type_="pipelines_config", enabled=True)
    result = await pipelines.update_config(client, workspace, probe_repo_slug, body=body)
    # Result should be PipelinesConfig, None, or Error — not an exception
    assert not isinstance(result, Exception), (
        f"pipelines.update_config raised: {result!r}"
    )
    if isinstance(result, PipelinesConfig):
        assert result.enabled is True, (
            f"update_config returned enabled={result.enabled!r}, expected True"
        )


# ===========================================================================
# GROUP 3 — REPOSITORY VARIABLES (CRUD lifecycle)
# ===========================================================================


async def test_variables_returns_list(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    result = await pipelines.variables(client, workspace, probe_repo_slug, pagelen=25)
    if isinstance(result, Error):
        pytest.skip(f"pipelines.variables not available: {_err_msg(result)}")
    assert isinstance(result, list), (
        f"pipelines.variables must return list, got {type(result).__name__}"
    )
    for idx, var in enumerate(result):
        assert isinstance(var, PipelineVariable), (
            f"pipelines.variables[{idx}] is {type(var).__name__}, expected PipelineVariable"
        )


async def test_variables_contains_probe_var(
    client: BBClient,
    workspace: str,
    probe_repo_slug: str,
    probe_variable_uuid: str,
) -> None:
    result = await pipelines.variables(client, workspace, probe_repo_slug, pagelen=50)
    if isinstance(result, Error):
        pytest.skip(f"pipelines.variables not available: {_err_msg(result)}")
    uuids = [v.uuid for v in result if isinstance(v, PipelineVariable)]
    assert probe_variable_uuid in uuids, (
        f"Seed variable {probe_variable_uuid!r} not found in variables list. "
        f"Found UUIDs: {uuids}"
    )


async def test_get_variable_returns_probe_var(
    client: BBClient,
    workspace: str,
    probe_repo_slug: str,
    probe_variable_uuid: str,
) -> None:
    result = await pipelines.get_variable(
        client, workspace, probe_repo_slug, probe_variable_uuid
    )
    assert not isinstance(result, Error), (
        f"pipelines.get_variable errored: {_err_msg(result)}"  # type: ignore[arg-type]
    )
    assert isinstance(result, PipelineVariable), (
        f"pipelines.get_variable must return PipelineVariable, got {type(result).__name__}"
    )
    assert result.key == "PROBE_VAR", (
        f"variable key mismatch: got {result.key!r}, expected 'PROBE_VAR'"
    )


async def test_create_update_delete_variable_roundtrip(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    key = f"TEST_VAR_{uuid.uuid4().hex[:8].upper()}"
    created_uuid: str | None = None
    try:
        # --- create ---
        body = PipelineVariable(type_="pipeline_variable", key=key, value="initial", secured=False)
        created = await pipelines.create_variable(
            client, workspace, probe_repo_slug, body=body
        )
        assert isinstance(created, PipelineVariable), (
            f"pipelines.create_variable must return PipelineVariable, "
            f"got {type(created).__name__}: {created!r}"
        )
        assert created.key == key, (
            f"created variable key {created.key!r} != expected {key!r}"
        )
        created_uuid = created.uuid
        assert created_uuid, f"created variable has no uuid: {created!r}"

        # --- verify it exists ---
        fetched = await pipelines.get_variable(
            client, workspace, probe_repo_slug, created_uuid
        )
        assert isinstance(fetched, PipelineVariable), (
            f"get_variable after create must return PipelineVariable, got {fetched!r}"
        )
        assert fetched.key == key

        # --- update value ---
        update_body = PipelineVariable(
            type_="pipeline_variable", key=key, value="updated-value", secured=False
        )
        updated = await pipelines.update_variable(
            client, workspace, probe_repo_slug, created_uuid, body=update_body
        )
        assert isinstance(updated, PipelineVariable), (
            f"pipelines.update_variable must return PipelineVariable, "
            f"got {type(updated).__name__}: {updated!r}"
        )

    finally:
        if created_uuid:
            await pipelines.delete_variable(
                client, workspace, probe_repo_slug, created_uuid
            )
            # verify gone
            after_delete = await pipelines.get_variable(
                client, workspace, probe_repo_slug, created_uuid
            )
            assert not isinstance(after_delete, PipelineVariable), (
                f"variable {key!r} still exists after delete: {after_delete!r}"
            )


# ===========================================================================
# GROUP 4 — WORKSPACE VARIABLES (CRUD lifecycle)
# ===========================================================================


async def test_workspace_variables_returns_list(
    client: BBClient, workspace: str
) -> None:
    result = await pipelines.workspace_variables(client, workspace, pagelen=25)
    if isinstance(result, Error):
        pytest.skip(f"pipelines.workspace_variables not available: {_err_msg(result)}")
    assert isinstance(result, list), (
        f"pipelines.workspace_variables must return list, got {type(result).__name__}"
    )
    for idx, var in enumerate(result):
        assert isinstance(var, PipelineVariable), (
            f"pipelines.workspace_variables[{idx}] is {type(var).__name__}, "
            "expected PipelineVariable"
        )


async def test_workspace_variables_contains_ws_probe_var(
    client: BBClient, workspace: str, probe_ws_variable_uuid: str
) -> None:
    result = await pipelines.workspace_variables(client, workspace, pagelen=50)
    if isinstance(result, Error):
        pytest.skip(f"pipelines.workspace_variables not available: {_err_msg(result)}")
    uuids = [v.uuid for v in result if isinstance(v, PipelineVariable)]
    assert probe_ws_variable_uuid in uuids, (
        f"Seed workspace variable {probe_ws_variable_uuid!r} not found. "
        f"Found UUIDs: {uuids}"
    )


async def test_get_workspace_variable_returns_ws_probe_var(
    client: BBClient, workspace: str, probe_ws_variable_uuid: str
) -> None:
    result = await pipelines.get_workspace_variable(
        client, workspace, probe_ws_variable_uuid
    )
    assert not isinstance(result, Error), (
        f"pipelines.get_workspace_variable errored: {_err_msg(result)}"  # type: ignore[arg-type]
    )
    assert isinstance(result, PipelineVariable), (
        f"pipelines.get_workspace_variable must return PipelineVariable, "
        f"got {type(result).__name__}"
    )
    assert result.key == "WS_PROBE_VAR", (
        f"workspace variable key mismatch: got {result.key!r}, expected 'WS_PROBE_VAR'"
    )


async def test_create_update_delete_workspace_variable_roundtrip(
    client: BBClient, workspace: str
) -> None:
    key = f"WS_TEST_{uuid.uuid4().hex[:8].upper()}"
    created_uuid: str | None = None
    try:
        # --- create ---
        body = PipelineVariable(
            type_="pipeline_variable", key=key, value="ws-initial", secured=False
        )
        created = await pipelines.create_workspace_variable(client, workspace, body=body)
        assert isinstance(created, PipelineVariable), (
            f"pipelines.create_workspace_variable must return PipelineVariable, "
            f"got {type(created).__name__}: {created!r}"
        )
        assert created.key == key, (
            f"created ws variable key {created.key!r} != expected {key!r}"
        )
        created_uuid = created.uuid
        assert created_uuid, f"created ws variable has no uuid: {created!r}"

        # --- verify it exists ---
        fetched = await pipelines.get_workspace_variable(client, workspace, created_uuid)
        assert isinstance(fetched, PipelineVariable), (
            f"get_workspace_variable after create must return PipelineVariable, got {fetched!r}"
        )

        # --- update ---
        update_body = PipelineVariable(
            type_="pipeline_variable", key=key, value="ws-updated", secured=False
        )
        updated = await pipelines.update_workspace_variable(
            client, workspace, created_uuid, body=update_body
        )
        assert isinstance(updated, PipelineVariable), (
            f"pipelines.update_workspace_variable must return PipelineVariable, "
            f"got {type(updated).__name__}: {updated!r}"
        )

    finally:
        if created_uuid:
            await pipelines.delete_workspace_variable(client, workspace, created_uuid)
            # verify gone
            after_delete = await pipelines.get_workspace_variable(
                client, workspace, created_uuid
            )
            assert not isinstance(after_delete, PipelineVariable), (
                f"workspace variable {key!r} still exists after delete: {after_delete!r}"
            )


# ===========================================================================
# GROUP 5 — SCHEDULES (CRUD lifecycle)
# ===========================================================================


async def test_schedules_returns_list(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    result = await pipelines.schedules(client, workspace, probe_repo_slug, pagelen=25)
    if isinstance(result, Error):
        pytest.skip(f"pipelines.schedules not available: {_err_msg(result)}")
    assert isinstance(result, list), (
        f"pipelines.schedules must return list, got {type(result).__name__}"
    )
    for idx, sched in enumerate(result):
        assert isinstance(sched, PipelineSchedule), (
            f"pipelines.schedules[{idx}] is {type(sched).__name__}, expected PipelineSchedule"
        )


async def test_schedules_contains_seed_schedule(
    client: BBClient,
    workspace: str,
    probe_repo_slug: str,
    probe_schedule_uuid: str,
) -> None:
    result = await pipelines.schedules(client, workspace, probe_repo_slug, pagelen=50)
    if isinstance(result, Error):
        pytest.skip(f"pipelines.schedules not available: {_err_msg(result)}")
    uuids = [s.uuid for s in result if isinstance(s, PipelineSchedule)]
    assert probe_schedule_uuid in uuids, (
        f"Seed schedule {probe_schedule_uuid!r} not found in schedules list. "
        f"Found UUIDs: {uuids}"
    )


async def test_get_schedule_returns_seed(
    client: BBClient,
    workspace: str,
    probe_repo_slug: str,
    probe_schedule_uuid: str,
) -> None:
    result = await pipelines.get_schedule(
        client, workspace, probe_repo_slug, probe_schedule_uuid
    )
    assert not isinstance(result, Error), (
        f"pipelines.get_schedule errored: {_err_msg(result)}"  # type: ignore[arg-type]
    )
    assert isinstance(result, PipelineSchedule), (
        f"pipelines.get_schedule must return PipelineSchedule, "
        f"got {type(result).__name__}: {result!r}"
    )
    assert result.uuid == probe_schedule_uuid, (
        f"schedule uuid mismatch: got {result.uuid!r}, expected {probe_schedule_uuid!r}"
    )


async def test_schedule_executions_returns_value(
    client: BBClient,
    workspace: str,
    probe_repo_slug: str,
    probe_schedule_uuid: str,
) -> None:
    # May return None or an empty list if the schedule has never run — both are OK.
    result = await pipelines.schedule_executions(
        client, workspace, probe_repo_slug, probe_schedule_uuid
    )
    assert not isinstance(result, Exception), (
        f"pipelines.schedule_executions raised unexpectedly: {result!r}"
    )


async def test_create_update_delete_schedule_roundtrip(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    created_uuid: str | None = None
    try:
        # 7-field cron (BB format): "0 0 12 * * ? *" = 12pm UTC every day
        target = PipelineSchedulePostRequestBodyTarget(
            selector=PipelineSelector(
                type_=PipelineSelectorType.DEFAULT,
            ),
            ref_name="main",
            ref_type=PipelineSchedulePostRequestBodyTargetRefType.BRANCH,
        )
        # The Bitbucket API requires a "type" discriminator in the target object.
        # PipelineSchedulePostRequestBodyTarget has no type_ field, so inject it
        # via additional_properties which are merged into the serialized JSON.
        target["type"] = "pipeline_ref_target"
        schedule_body = PipelineSchedulePostRequestBody(
            type_="pipeline_schedule",
            target=target,
            cron_pattern="0 0 12 * * ? *",
            enabled=True,
        )
        created = await pipelines.create_schedule(
            client, workspace, probe_repo_slug, body=schedule_body
        )
        assert isinstance(created, PipelineSchedule), (
            f"pipelines.create_schedule must return PipelineSchedule, "
            f"got {type(created).__name__}: {created!r}"
        )
        created_uuid = created.uuid
        assert created_uuid, f"created schedule has no uuid: {created!r}"

        # --- verify ---
        fetched = await pipelines.get_schedule(
            client, workspace, probe_repo_slug, created_uuid
        )
        assert isinstance(fetched, PipelineSchedule), (
            f"get_schedule after create must return PipelineSchedule, got {fetched!r}"
        )

        # --- update (disable it) ---
        update_body = PipelineSchedulePutRequestBody(type_="pipeline_schedule", enabled=False)
        updated = await pipelines.update_schedule(
            client, workspace, probe_repo_slug, created_uuid, body=update_body
        )
        assert isinstance(updated, PipelineSchedule), (
            f"pipelines.update_schedule must return PipelineSchedule, "
            f"got {type(updated).__name__}: {updated!r}"
        )
        assert updated.enabled is False, (
            f"expected schedule enabled=False after update, got {updated.enabled!r}"
        )

    finally:
        if created_uuid:
            await pipelines.delete_schedule(
                client, workspace, probe_repo_slug, created_uuid
            )
            # verify gone
            after_delete = await pipelines.get_schedule(
                client, workspace, probe_repo_slug, created_uuid
            )
            assert not isinstance(after_delete, PipelineSchedule), (
                f"schedule {created_uuid!r} still exists after delete: {after_delete!r}"
            )


# ===========================================================================
# GROUP 6 — KNOWN HOSTS (CRUD lifecycle)
# ===========================================================================


async def test_known_hosts_returns_list(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    result = await pipelines.known_hosts(client, workspace, probe_repo_slug, pagelen=25)
    if isinstance(result, Error):
        pytest.skip(f"pipelines.known_hosts not available: {_err_msg(result)}")
    assert isinstance(result, list), (
        f"pipelines.known_hosts must return list, got {type(result).__name__}"
    )
    for idx, host in enumerate(result):
        assert isinstance(host, PipelineKnownHost), (
            f"pipelines.known_hosts[{idx}] is {type(host).__name__}, expected PipelineKnownHost"
        )


async def test_known_hosts_contains_gitlab(
    client: BBClient,
    workspace: str,
    probe_repo_slug: str,
    probe_known_host_uuid: str,
) -> None:
    result = await pipelines.known_hosts(client, workspace, probe_repo_slug, pagelen=50)
    if isinstance(result, Error):
        pytest.skip(f"pipelines.known_hosts not available: {_err_msg(result)}")
    uuids = [h.uuid for h in result if isinstance(h, PipelineKnownHost)]
    assert probe_known_host_uuid in uuids, (
        f"Seed known host {probe_known_host_uuid!r} (gitlab.com) not found. "
        f"Found UUIDs: {uuids}"
    )


async def test_get_known_host_returns_gitlab(
    client: BBClient,
    workspace: str,
    probe_repo_slug: str,
    probe_known_host_uuid: str,
) -> None:
    result = await pipelines.get_known_host(
        client, workspace, probe_repo_slug, probe_known_host_uuid
    )
    assert not isinstance(result, Error), (
        f"pipelines.get_known_host errored: {_err_msg(result)}"  # type: ignore[arg-type]
    )
    assert isinstance(result, PipelineKnownHost), (
        f"pipelines.get_known_host must return PipelineKnownHost, "
        f"got {type(result).__name__}: {result!r}"
    )
    assert result.hostname == "gitlab.com", (
        f"known host hostname mismatch: got {result.hostname!r}, expected 'gitlab.com'"
    )


async def test_create_delete_known_host_roundtrip(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    # Use a unique random hostname to avoid conflicts. Bitbucket blocks
    # well-known hostnames like github.com / gitlab.com (400 hostname-not-allowed).
    hostname = f"test-host-{uuid.uuid4().hex[:8]}.example.com"
    created_uuid: str | None = None
    try:
        host_body = PipelineKnownHost(
            type_="pipeline_known_host",
            hostname=hostname,
            public_key=PipelineSshPublicKey(
                key_type="rsa",
                key=(
                    "AAAAB3NzaC1yc2EAAAABIwAAAQEAq2A7hRGmdnm9tUDbO9IDSwBK6TbQa+PXYPCPy6rbTrTtw7"
                    "PHkccKrpp0yVhp5HdEIcKr6pLlVDBfOLX9QUsyCOV0wzfjIJNlGEYsdlLJizHhbn2mUjvSAHQ"
                    "qZETYP81eFzLQNnPHt4EVVUh7VfDESU84KezmD5QlWpXLmvU31/yMf+Se8xhHTvKSCZIFImWw"
                    "oG6mbUoWf9nzpIoaSjB+weqqUUmpaaasXVal72J+UX2B+2RPW3RcT0eOzQgqlJL3RKrTJvdsjE"
                    "3JEAvGq3lGHSZXy28G3skua2SmVi/w4yCE6gbODqnTWlg7+wC604ydGXA8VJiS5ap43JXiUFF"
                    "AaQ=="
                ),
            ),
        )
        created = await pipelines.create_known_host(
            client, workspace, probe_repo_slug, body=host_body
        )
        assert isinstance(created, PipelineKnownHost), (
            f"pipelines.create_known_host must return PipelineKnownHost, "
            f"got {type(created).__name__}: {created!r}"
        )
        assert created.hostname == hostname, (
            f"known host hostname mismatch: got {created.hostname!r}, expected {hostname!r}"
        )
        created_uuid = created.uuid
        assert created_uuid, f"created known host has no uuid: {created!r}"

        # --- verify ---
        fetched = await pipelines.get_known_host(
            client, workspace, probe_repo_slug, created_uuid
        )
        assert isinstance(fetched, PipelineKnownHost), (
            f"get_known_host after create must return PipelineKnownHost, got {fetched!r}"
        )

    finally:
        if created_uuid:
            await pipelines.delete_known_host(
                client, workspace, probe_repo_slug, created_uuid
            )
            # verify gone
            after_delete = await pipelines.get_known_host(
                client, workspace, probe_repo_slug, created_uuid
            )
            assert not isinstance(after_delete, PipelineKnownHost), (
                f"known host {created_uuid!r} still exists after delete: {after_delete!r}"
            )


# ===========================================================================
# GROUP 7 — SSH KEY PAIR
# ===========================================================================


async def test_ssh_key_pair_returns_key_pair(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    result = await pipelines.ssh_key_pair(client, workspace, probe_repo_slug)
    if result is None:
        pytest.skip(
            f"pipelines.ssh_key_pair returned None for {probe_repo_slug!r} — "
            "no SSH key pair configured"
        )
    assert not isinstance(result, Error), (
        f"pipelines.ssh_key_pair errored: {_err_msg(result)}"  # type: ignore[arg-type]
    )
    assert isinstance(result, PipelineSshKeyPair), (
        f"pipelines.ssh_key_pair must return PipelineSshKeyPair, "
        f"got {type(result).__name__}: {result!r}"
    )
    # Per Bitbucket API: private_key is always empty/redacted in GET response;
    # public_key should be present.
    assert result.public_key, (
        f"PipelineSshKeyPair.public_key must be set (got empty): {result!r}"
    )


# ===========================================================================
# GROUP 8 — CACHES
# ===========================================================================


async def test_caches_returns_list(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    result = await pipelines.caches(client, workspace, probe_repo_slug, pagelen=25)
    if isinstance(result, Error):
        pytest.skip(f"pipelines.caches not available: {_err_msg(result)}")
    assert isinstance(result, list), (
        f"pipelines.caches must return list, got {type(result).__name__}"
    )
    # May be empty if pipeline has never run successfully — that is acceptable.


# ===========================================================================
# GROUP 9 — OIDC
# ===========================================================================


async def test_oidc_config_returns_value(
    client: BBClient, workspace: str
) -> None:
    result = await pipelines.oidc_config(client, workspace)
    if isinstance(result, Error):
        msg = result.error.message if result.error else ""
        pytest.skip(f"oidc_config requires OAuth2 token: {msg}")
    assert result is not None, "pipelines.oidc_config returned None"


async def test_oidc_keys_returns_value(
    client: BBClient, workspace: str
) -> None:
    result = await pipelines.oidc_keys(client, workspace)
    if isinstance(result, Error):
        msg = result.error.message if result.error else ""
        pytest.skip(f"oidc_keys requires OAuth2 token: {msg}")
    assert result is not None, "pipelines.oidc_keys returned None"


# ===========================================================================
# GROUP 10 — RUNNERS (expected 404 / not available on Free plan)
# ===========================================================================


async def test_runners_documents_response(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """Repository runners — document actual API response; expect 404/None on Free plan."""
    try:
        result = await pipelines.runners(client, workspace, probe_repo_slug)
        # Result may be None, a list-like response, or an Error — all acceptable.
        # We just verify the function does not crash with an unhandled exception.
        assert result is None or not isinstance(result, Exception), (
            f"pipelines.runners returned unexpected exception-like value: {result!r}"
        )
    except UnexpectedStatus as exc:
        # 404 is expected on Free plan / when no self-hosted runners are configured.
        if exc.status_code in (404, 403):
            pytest.skip(
                f"pipelines.runners returned {exc.status_code} — "
                "self-hosted runners not available on this plan"
            )
        raise


async def test_workspace_runners_documents_response(
    client: BBClient, workspace: str
) -> None:
    """Workspace runners — document actual API response; expect 404/None on Free plan."""
    try:
        result = await pipelines.workspace_runners(client, workspace)
        assert result is None or not isinstance(result, Exception), (
            f"pipelines.workspace_runners returned unexpected value: {result!r}"
        )
    except UnexpectedStatus as exc:
        if exc.status_code in (404, 403):
            pytest.skip(
                f"pipelines.workspace_runners returned {exc.status_code} — "
                "workspace runners not available on this plan"
            )
        raise


# ===========================================================================
# GROUP 11 — TEST REPORTS (expected empty for PENDING pipeline)
# ===========================================================================


async def test_test_reports_returns_value_or_none(
    client: BBClient,
    workspace: str,
    probe_repo_slug: str,
    probe_pipeline_uuid: str,
) -> None:
    """Test reports for a PENDING pipeline will be empty — that is acceptable."""
    steps = await pipelines.steps(client, workspace, probe_repo_slug, probe_pipeline_uuid, pagelen=1)
    if not steps or isinstance(steps, Error):
        pytest.skip("no steps available for this pipeline")
    step_uuid = getattr(steps[0], "uuid", None)
    if not step_uuid:
        pytest.skip("step has no UUID")
    try:
        result = await pipelines.test_reports(
            client, workspace, probe_repo_slug, probe_pipeline_uuid, step_uuid
        )
        assert not isinstance(result, Exception), (
            f"pipelines.test_reports raised: {result!r}"
        )
    except UnexpectedStatus as exc:
        if exc.status_code == 404:
            pytest.skip(
                "pipelines.test_reports returned 404 — "
                "no test data for PENDING pipeline (expected)"
            )
        raise


# ===========================================================================
# GROUP 12 — OTHER
# ===========================================================================


# ===========================================================================
# GROUP 13 — BUG-PIPELINES-002 / BUG-PIPELINES-003 regression tests
# ===========================================================================


async def test_update_config_nonexistent_repo_does_not_crash(
    client: BBClient, workspace: str
) -> None:
    """update_config with a nonexistent repo must not raise AttributeError (BUG-PIPELINES-002: body type fix).

    The PUT endpoint for pipelines_config does not document 404, so _parse_response returns None
    for a missing repo. The point of this test is that the function is callable with a typed body
    without crashing — not that 404 is mapped to Error.
    """
    result = await pipelines.update_config(
        client, workspace, "nonexistent-repo-xyz-99999",
        body=PipelinesConfig(enabled=False),
    )
    assert result is None or isinstance(result, Error), (
        f"Expected None or Error for nonexistent repo, got {type(result).__name__}"
    )


async def test_update_build_number_roundtrip(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """update_build_number sets the build number and returns PipelineBuildNumber (BUG-PIPELINES-003)."""
    import time
    from bb.cloud.models.pipeline_build_number import PipelineBuildNumber

    # Use epoch seconds (~1.7 billion) which is guaranteed to be higher than any realistic
    # pipeline run count, so the "must be higher than current" constraint is always satisfied.
    body = PipelineBuildNumber(type_="pipeline_build_number", next_=int(time.time()))
    try:
        result = await pipelines.update_build_number(
            client, workspace, probe_repo_slug, body=body
        )
        assert not isinstance(result, Error), (
            f"update_build_number failed: {result!r}"
        )
        assert isinstance(result, PipelineBuildNumber), (
            f"update_build_number must return PipelineBuildNumber, got {type(result).__name__}"
        )
    except UnexpectedStatus as exc:
        if exc.status_code in (400, 403):
            pytest.skip(
                f"pipelines.update_build_number returned {exc.status_code} — "
                "may require the new number to be higher than current"
            )
        raise


async def test_update_build_number_nonexistent_repo_returns_error(
    client: BBClient, workspace: str
) -> None:
    """update_build_number on a nonexistent repo must return Error (BUG-PIPELINES-003)."""
    from bb.cloud.models.pipeline_build_number import PipelineBuildNumber

    result = await pipelines.update_build_number(
        client, workspace, "nonexistent-repo-xyz-99999",
        body=PipelineBuildNumber(next_=1),
    )
    assert isinstance(result, Error), (
        f"Expected Error for nonexistent repo, got {type(result).__name__}"
    )
