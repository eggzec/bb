# Test Plan — pipelines

**Workspace:** beaverish
**Probe repo:** bb-probe (pipelines enabled)
**Seed pipeline UUID:** {88efe83d-e4a6-4886-aff9-f6241fa5cf80} (state: PENDING)
**Seed pipeline step UUID:** {a763ede3-...} (name: Test, PENDING)
**Seed pipeline variable UUID:** {45920ece-ce1e-4854-a192-4f8e630aa683} (key: PROBE_VAR)
**Seed schedule UUID:** {5784e0da-f082-4f91-9d65-20e1d7f0ed8e}
**Seed known host UUID:** {6f24c288-d2fe-4935-999b-b0f494056957} (hostname: gitlab.com)
**Seed SSH key pair:** present
**Seed workspace variable UUID:** {70868f27-6d0e-48a5-8cf3-c7ece5a848a9} (key: WS_PROBE_VAR)

---

## Module: `bb.cloud.sdk.pipelines` (54 functions)

### Group 1 — Core

| # | Test ID | Function | Scenario | Expected | Status |
|---|---------|----------|----------|----------|--------|
| 1 | `test_list_returns_pipelines` | `list` | pagelen=10 on bb-probe | Returns `list[Pipeline]`; all items are Pipeline instances | - |
| 2 | `test_list_contains_seed_pipeline` | `list` | list all pipelines | Seed UUID {88efe83d-...} is present | - |
| 3 | `test_get_seed_pipeline` | `get` | UUID={88efe83d-...} | Returns `Pipeline`; uuid matches; state is PENDING | - |
| 4 | `test_get_missing_pipeline_returns_none_or_error` | `get` | UUID={00000000-0000-0000-0000-000000000000} | Returns `Error` or `None`, NOT Pipeline | - |
| 5 | `test_run_skipped` | `run` | — | SKIP — would consume runner quota | - |
| 6 | `test_stop_skipped_no_running` | `stop` | no running pipeline | SKIP — no running pipeline; only call if state==IN_PROGRESS | - |
| 7 | `test_steps_returns_list` | `steps` | seed pipeline UUID | Returns a list (may be empty for PENDING pipeline) | - |
| 8 | `test_step_returns_object` | `step` | seed pipeline + first step UUID from steps() | Returns step object; uuid is set | - |
| 9 | `test_step_log_returns_string_or_none` | `step_log` | seed pipeline + step UUID | Returns str or None (PENDING = empty log) | - |

### Group 2 — Config

| # | Test ID | Function | Scenario | Expected | Status |
|---|---------|----------|----------|----------|--------|
| 10 | `test_config_returns_pipelines_config` | `config` | bb-probe | Returns PipelinesConfig with enabled==True | - |
| 11 | `test_update_config_idempotent` | `update_config` | PUT enabled=True (already enabled) | Returns PipelinesConfig; enabled==True | NOTE: BUG-PIPELINES-002/003 — body type is `Unset` in SDK, must pass `PipelinesConfig` directly |

### Group 3 — Repository Variables (CRUD lifecycle)

| # | Test ID | Function | Scenario | Expected | Status |
|---|---------|----------|----------|----------|--------|
| 12 | `test_variables_returns_list` | `variables` | bb-probe | Returns `list[PipelineVariable]` | - |
| 13 | `test_variables_contains_probe_var` | `variables` | bb-probe | PROBE_VAR UUID {45920ece-...} is present | - |
| 14 | `test_get_variable_returns_probe_var` | `get_variable` | UUID={45920ece-...} | Returns PipelineVariable; key=="PROBE_VAR" | - |
| 15 | `test_create_update_delete_variable_roundtrip` | `create_variable` / `update_variable` / `delete_variable` | Create TEST_VAR_<uuid>, update value, delete, verify gone | Full lifecycle; variable absent after delete | - |

### Group 4 — Workspace Variables (CRUD lifecycle)

| # | Test ID | Function | Scenario | Expected | Status |
|---|---------|----------|----------|----------|--------|
| 16 | `test_workspace_variables_returns_list` | `workspace_variables` | beaverish | Returns `list[PipelineVariable]` | - |
| 17 | `test_workspace_variables_contains_ws_probe_var` | `workspace_variables` | beaverish | WS_PROBE_VAR UUID {70868f27-...} present | - |
| 18 | `test_get_workspace_variable_returns_ws_probe_var` | `get_workspace_variable` | UUID={70868f27-...} | Returns PipelineVariable; key=="WS_PROBE_VAR" | - |
| 19 | `test_create_update_delete_workspace_variable_roundtrip` | `create_workspace_variable` / `update_workspace_variable` / `delete_workspace_variable` | Create WS_TEST_<uuid>, update value, delete, verify gone | Full lifecycle completes cleanly | - |

### Group 5 — Schedules (CRUD lifecycle)

| # | Test ID | Function | Scenario | Expected | Status |
|---|---------|----------|----------|----------|--------|
| 20 | `test_schedules_returns_list` | `schedules` | bb-probe | Returns `list[PipelineSchedule]` | - |
| 21 | `test_schedules_contains_seed_schedule` | `schedules` | bb-probe | Seed UUID {5784e0da-...} present | - |
| 22 | `test_get_schedule_returns_seed` | `get_schedule` | UUID={5784e0da-...} | Returns PipelineSchedule; uuid matches | - |
| 23 | `test_schedule_executions_returns_value` | `schedule_executions` | seed schedule UUID | Returns value (may be None/empty — OK for schedule that hasn't run) | - |
| 24 | `test_create_update_delete_schedule_roundtrip` | `create_schedule` / `update_schedule` / `delete_schedule` | Create schedule on branch, update enabled=False, delete | Full lifecycle completes cleanly | NOTE: BUG-PIPELINES-001 — SDK body type wrong; test uses correct types directly |

### Group 6 — Known Hosts (CRUD lifecycle)

| # | Test ID | Function | Scenario | Expected | Status |
|---|---------|----------|----------|----------|--------|
| 25 | `test_known_hosts_returns_list` | `known_hosts` | bb-probe | Returns `list[PipelineKnownHost]` | - |
| 26 | `test_known_hosts_contains_gitlab` | `known_hosts` | bb-probe | gitlab.com UUID {6f24c288-...} present | - |
| 27 | `test_get_known_host_returns_gitlab` | `get_known_host` | UUID={6f24c288-...} | Returns PipelineKnownHost; hostname=="gitlab.com" | - |
| 28 | `test_create_delete_known_host_roundtrip` | `create_known_host` / `delete_known_host` | Create github.com host, delete | Full lifecycle (no update—immutable hostname) | - |

### Group 7 — SSH Key Pair

| # | Test ID | Function | Scenario | Expected | Status |
|---|---------|----------|----------|----------|--------|
| 29 | `test_ssh_key_pair_returns_key_pair` | `ssh_key_pair` | bb-probe | Returns PipelineSshKeyPair; public_key is set (private_key redacted/empty per API) | - |

### Group 8 — Caches

| # | Test ID | Function | Scenario | Expected | Status |
|---|---------|----------|----------|----------|--------|
| 30 | `test_caches_returns_list` | `caches` | bb-probe | Returns list (may be empty — no successful run yet) | - |

### Group 9 — OIDC

| # | Test ID | Function | Scenario | Expected | Status |
|---|---------|----------|----------|----------|--------|
| 31 | `test_oidc_config_returns_value` | `oidc_config` | beaverish, bb-probe | Returns a value (OIDC config doc or None) — not an Error | FAIL (BUG-PIPELINES-004: extra positional arg — TypeError) |
| 32 | `test_oidc_keys_returns_value` | `oidc_keys` | beaverish, bb-probe | Returns a value (JWKS or None) — not an Error | FAIL (BUG-PIPELINES-004: extra positional arg — TypeError) |

### Group 10 — Runners (expected 404 / not available on Free plan)

| # | Test ID | Function | Scenario | Expected | Status |
|---|---------|----------|----------|----------|--------|
| 33 | `test_runners_documents_response` | `runners` | bb-probe | Documents actual response (404/403/None/empty); does NOT raise unexpectedly | - |
| 34 | `test_workspace_runners_documents_response` | `workspace_runners` | beaverish | Documents actual response (404/403/None/empty); does NOT raise unexpectedly | - |

### Group 11 — Test Reports (expected empty for PENDING pipeline)

| # | Test ID | Function | Scenario | Expected | Status |
|---|---------|----------|----------|----------|--------|
| 35 | `test_test_reports_returns_value_or_none` | `test_reports` | seed pipeline UUID | Returns value or None; PENDING = no test data | FAIL (BUG-PIPELINES-005: missing step_uuid arg — TypeError) |

### Group 12 — Other

| # | Test ID | Function | Scenario | Expected | Status |
|---|---------|----------|----------|----------|--------|
| 36 | `test_update_build_number_returns_value` | `update_build_number` | set next=<current+100> | Returns PipelineBuildNumber or None; does NOT raise | NOTE: BUG-PIPELINES-003 — SDK body type is `Unset`; test forces `PipelineBuildNumber` |

---

## Functions not individually tested (require live run to exercise)

| Function | Reason not tested |
|----------|-------------------|
| `run` | Would trigger a new pipeline and consume runner quota |
| `stop` | No running pipeline available; only call if state==IN_PROGRESS |
| `delete_cache` | No caches available (pipeline never ran successfully) |
| `clear_caches` | No caches to clear |
| `cache_uri` | Requires a live cache UUID |
| `container_log` | Requires a running/completed container |
| `test_cases` | Requires a test report UUID (pipeline never ran) |
| `test_case_reasons` | Requires test case UUID |
| `get_runner` | No self-hosted runners configured |
| `create_runner` | Would require Atlassian runner setup |
| `update_runner` | No runner to update |
| `delete_runner` | No runner to delete |
| `get_workspace_runner` | No workspace runners configured |
| `create_workspace_runner` | Would require Atlassian runner setup |
| `update_workspace_runner` | No workspace runner to update |
| `delete_workspace_runner` | No workspace runner to delete |
| `delete_ssh_key_pair` | Would destroy seed SSH config |
| `update_ssh_key_pair` | Would replace seed SSH config |
| `update_known_host` | API likely 400/immutable after creation |
| `step` | Depends on steps() returning items (may be empty for PENDING) |
| `step_log` | Depends on step being available |

---

## Cross-cutting concerns

- All SDK functions return typed objects; never raise raw `httpx` or `UnexpectedStatus` in normal operation
- Throwaway resources always cleaned up in `finally` blocks
- Unique key names use `uuid.uuid4().hex[:8]` prefix to avoid collisions
- Runner endpoints expected to return 404 or be unavailable on Free plan — document, do not fail
- Schedules use 7-field cron format (e.g. "0 0 12 * * ? *")
- PENDING pipeline may have 0 steps — step/step_log tests must handle empty steps list gracefully
