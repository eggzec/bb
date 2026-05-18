# BUG-PIPELINES-003: Multiple SDK wrapper functions have `body: Unset = UNSET` when they need a real model type

**Module:** `bb.cloud.sdk.pipelines`
**Severity:** High (callers cannot pass request bodies — effectively makes these write APIs unusable via typing)

## Description

Several SDK wrapper functions in `pipelines.py` declare `body: Unset = UNSET` but the underlying
generated API module requires a concrete model type. The `Unset` sentinel is for optional fields,
not for required or meaningful request bodies.

Two distinct sub-problems exist:

**Sub-problem A — body typed as Unset but generated API requires a real model (runtime crash):**
These functions call `body.to_dict()` in `_get_kwargs` unconditionally. Passing `UNSET` raises `AttributeError`.

| SDK function | SDK signature | Generated API expects |
|---|---|---|
| `update_config` (line 516) | `body: Unset = UNSET` | `body: PipelinesConfig` (required, no default) |
| `update_build_number` (line 2483) | `body: Unset = UNSET` | `body: PipelineBuildNumber` (required, no default) |
| `create_schedule` (line 906) | `body: PipelineSchedule \| Unset = UNSET` | `body: PipelineSchedulePostRequestBody` (required) |
| `update_schedule` (line 958) | `body: PipelineSchedule \| Unset = UNSET` | `body: PipelineSchedulePutRequestBody` (required) |

**Sub-problem B — body typed as Unset but generated API has NO body parameter (phantom param):**
The spec documents NO request body for runner endpoints. The generated modules have no `body` parameter.
The SDK passes `body=body` as a keyword arg that the generated `asyncio()` does not accept — this raises `TypeError: asyncio() got an unexpected keyword argument 'body'` at runtime.

| SDK function | SDK signature | Generated API expects | Spec path |
|---|---|---|---|
| `create_runner` (line 1890) | `body: Unset = UNSET` → passed as kwarg | NO body param | `POST /repos/.../pipelines-config/runners` — no requestBody |
| `update_runner` (line 1927) | `body: Unset = UNSET` → passed as kwarg | NO body param | `PUT /repos/.../pipelines-config/runners/{uuid}` — no requestBody |
| `create_workspace_runner` (line 2073) | `body: Unset = UNSET` → passed as kwarg | NO body param | `POST /workspaces/.../pipelines-config/runners` — no requestBody |
| `update_workspace_runner` (line 2108) | `body: Unset = UNSET` → passed as kwarg | NO body param | `PUT /workspaces/.../pipelines-config/runners/{uuid}` — no requestBody |

## Root Cause

When wrapping generated API functions, the SDK author left `body` typed as `Unset` (a placeholder)
instead of either: (A) updating it to the correct model type, or (B) removing it entirely where
the underlying endpoint has no request body.

## Impact

Sub-problem A:
1. **Runtime crash** — `UNSET.to_dict()` → `AttributeError` on every call where no body is provided
2. **Type checkers** will flag callers that pass the correct type as a type error
3. **IDE autocomplete** will not suggest the correct fields

Sub-problem B:
1. **Runtime crash** — `asyncio() got an unexpected keyword argument 'body'` → `TypeError`
2. The `body` parameter in the SDK is a phantom — the spec and generated code have no body

## Evidence for `update_config`

```python
# SDK (wrong):
async def update_config(client, workspace, repo_slug, *, body: Unset = UNSET) -> Any:
    return await update_repository_pipeline_config.asyncio(workspace, repo_slug, client=client.auth, body=body)

# Generated API (correct):
def _get_kwargs(..., *, body: PipelinesConfig) -> dict[str, Any]:
    _kwargs["json"] = body.to_dict()   # crashes if body is UNSET
```

## Evidence for `update_build_number`

```python
# SDK (wrong):
async def update_build_number(client, workspace, repo_slug, *, body: Unset = UNSET) -> Any:

# Generated API (correct):
def _get_kwargs(..., *, body: PipelineBuildNumber) -> dict[str, Any]:
    _kwargs["json"] = body.to_dict()   # crashes if body is UNSET
```

## Evidence for `create_runner` (Sub-problem B)

```python
# SDK (wrong):
async def create_runner(client, workspace, repo_slug, *, body: Unset = UNSET) -> Any:
    return await create_repository_runner.asyncio(workspace, repo_slug, client=client.auth, body=body)
    #                                                                                    ^^^^^^^^^^^^^ not accepted

# Generated API (correct — NO body):
async def asyncio(workspace: str, repo_slug: str, *, client: AuthenticatedClient) -> ParsedPayload | None:
```

## Recommended Fix

### Sub-problem A — update to correct model types

```python
# update_config
from bb.cloud.models.pipelines_config import PipelinesConfig

async def update_config(
    client: BBClient, workspace: str, repo_slug: str, *,
    body: PipelinesConfig,  # required — no default
) -> PipelinesConfig | Error | None:

# update_build_number
from bb.cloud.models.pipeline_build_number import PipelineBuildNumber

async def update_build_number(
    client: BBClient, workspace: str, repo_slug: str, *,
    body: PipelineBuildNumber,  # required — no default
) -> PipelineBuildNumber | Error | None:

# create_schedule
from bb.cloud.models.pipeline_schedule_post_request_body import PipelineSchedulePostRequestBody

async def create_schedule(
    client: BBClient, workspace: str, repo_slug: str, *,
    body: PipelineSchedulePostRequestBody,  # required — no default
) -> PipelineSchedule | Error | None:

# update_schedule
from bb.cloud.models.pipeline_schedule_put_request_body import PipelineSchedulePutRequestBody

async def update_schedule(
    client: BBClient, workspace: str, repo_slug: str, schedule_uuid: str, *,
    body: PipelineSchedulePutRequestBody,  # required — no default
) -> PipelineSchedule | Error | None:
```

### Sub-problem B — remove phantom `body` parameter entirely from runner functions

The runner endpoints have no request body per spec. Remove `body` from the SDK signatures
and stop passing it to the generated API:

```python
# create_runner — remove body param and kwarg
async def create_runner(client: BBClient, workspace: str, repo_slug: str) -> Any:
    return await create_repository_runner.asyncio(workspace, repo_slug, client=client.auth)

# update_runner — remove body param and kwarg
async def update_runner(client: BBClient, workspace: str, repo_slug: str, runner_uuid: str) -> Any:
    return await update_repository_runner.asyncio(workspace, repo_slug, runner_uuid, client=client.auth)

# create_workspace_runner — remove body param and kwarg
async def create_workspace_runner(client: BBClient, workspace: str) -> Any:
    return await _create_workspace_runner_api.asyncio(workspace, client=client.auth)

# update_workspace_runner — remove body param and kwarg
async def update_workspace_runner(client: BBClient, workspace: str, runner_uuid: str) -> Any:
    return await _update_workspace_runner_api.asyncio(workspace, runner_uuid, client=client.auth)
```

## Fix Applied

**File:** `src/bb/cloud/sdk/pipelines.py`

### Imports added (lines 71, 80 after fix)

```python
from bb.cloud.models.pipeline_build_number import PipelineBuildNumber  # line 71 (new)
from bb.cloud.models.pipelines_config import PipelinesConfig            # line 80 (new)
```

### Sub-problem A — update_build_number (line 2490 before fix → 2490 after fix)

**Before:**
```python
async def update_build_number(client: BBClient, workspace: str, repo_slug: str, *, body: Unset = UNSET) -> Any:
```

**After:**
```python
async def update_build_number(client: BBClient, workspace: str, repo_slug: str, *, body: PipelineBuildNumber) -> Any:
```

(For `update_config` see BUG-PIPELINES-002.)

### Sub-problem B — four runner functions

**create_runner (line 1892 before fix → 1894 after fix)**

Before:
```python
async def create_runner(client: BBClient, workspace: str, repo_slug: str, *, body: Unset = UNSET) -> Any:
    return await create_repository_runner.asyncio(workspace, repo_slug, client=client.auth, body=body)
```

After:
```python
async def create_runner(client: BBClient, workspace: str, repo_slug: str) -> Any:
    return await create_repository_runner.asyncio(workspace, repo_slug, client=client.auth)
```

**update_runner (line 1928 before fix → 1930 after fix)**

Before:
```python
async def update_runner(
    client: BBClient, workspace: str, repo_slug: str, runner_uuid: str, *, body: Unset = UNSET
) -> Any:
    return await update_repository_runner.asyncio(workspace, repo_slug, runner_uuid, client=client.auth, body=body)
```

After:
```python
async def update_runner(
    client: BBClient, workspace: str, repo_slug: str, runner_uuid: str
) -> Any:
    return await update_repository_runner.asyncio(workspace, repo_slug, runner_uuid, client=client.auth)
```

**create_workspace_runner (line 2075 before fix → 2077 after fix)**

Before:
```python
async def create_workspace_runner(client: BBClient, workspace: str, *, body: Unset = UNSET) -> Any:
    return await _create_workspace_runner_api.asyncio(workspace, client=client.auth, body=body)
```

After:
```python
async def create_workspace_runner(client: BBClient, workspace: str) -> Any:
    return await _create_workspace_runner_api.asyncio(workspace, client=client.auth)
```

**update_workspace_runner (line 2110 before fix → 2112 after fix)**

Before:
```python
async def update_workspace_runner(client: BBClient, workspace: str, runner_uuid: str, *, body: Unset = UNSET) -> Any:
    return await _update_workspace_runner_api.asyncio(workspace, runner_uuid, client=client.auth, body=body)
```

After:
```python
async def update_workspace_runner(client: BBClient, workspace: str, runner_uuid: str) -> Any:
    return await _update_workspace_runner_api.asyncio(workspace, runner_uuid, client=client.auth)
```

## Status

- [x] Confirmed via static analysis of SDK wrapper vs generated API signatures
- [x] Confirmed via spec inspection (runner endpoints have no requestBody; PipelinesConfig/PipelineBuildNumber are required bodies)
- [x] FIXED — all 6 functions corrected (see Fix Applied section above)
- [ ] Confirmed via live test run

**Status:** FIXED
