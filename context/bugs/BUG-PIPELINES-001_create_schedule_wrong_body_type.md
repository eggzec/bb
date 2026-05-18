# BUG-PIPELINES-001: `create_schedule` and `update_schedule` have wrong body type annotations

**Module:** `bb.cloud.sdk.pipelines`
**Functions:** `create_schedule`, `update_schedule`
**Severity:** Medium (type annotation bug; runtime works via duck-typing but callers get wrong guidance)

## Description

The SDK wrapper functions for schedule create/update declare `body: PipelineSchedule | Unset` but
the underlying generated API modules expect different, incompatible request body types:

| SDK function | SDK type annotation | Generated API expects |
|---|---|---|
| `create_schedule` | `PipelineSchedule \| Unset` | `PipelineSchedulePostRequestBody` |
| `update_schedule` | `PipelineSchedule \| Unset` | `PipelineSchedulePutRequestBody` |

## Evidence

**SDK wrapper** (`src/bb/cloud/sdk/pipelines.py`, line ~906):
```python
async def create_schedule(
    ...
    body: PipelineSchedule | Unset = UNSET,
) -> PipelineSchedule | Error | None:
```

**Generated API** (`src/bb/cloud/api/pipelines/create_repository_pipeline_schedule.py`, line ~22):
```python
def _get_kwargs(
    workspace: str,
    repo_slug: str,
    *,
    body: PipelineSchedulePostRequestBody,
) -> dict[str, Any]:
```

Similarly for `update_schedule` / `update_repository_pipeline_schedule.py` which expects `PipelineSchedulePutRequestBody`.

The SDK docstring for `create_schedule` already correctly mentions `PipelineSchedulePostRequestBody` in the example, but the function signature says `PipelineSchedule`.

## Impact

- Static type checkers (mypy, pyright) will accept `PipelineSchedule` when callers need to pass `PipelineSchedulePostRequestBody`
- `PipelineSchedule` does not have the mandatory fields (`target`, `cron_pattern`) required by `PipelineSchedulePostRequestBody`
- Passing `PipelineSchedule` at runtime will produce a malformed request body missing required fields
- Passing `PipelineSchedulePutRequestBody` at runtime works correctly (duck-typing `.to_dict()`)

## Recommended Fix

Update the SDK function signatures to use the correct request body types:

```python
from bb.cloud.models.pipeline_schedule_post_request_body import PipelineSchedulePostRequestBody
from bb.cloud.models.pipeline_schedule_put_request_body import PipelineSchedulePutRequestBody

async def create_schedule(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: PipelineSchedulePostRequestBody | Unset = UNSET,
) -> PipelineSchedule | Error | None:
    ...

async def update_schedule(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    schedule_uuid: str,
    *,
    body: PipelineSchedulePutRequestBody | Unset = UNSET,
) -> PipelineSchedule | Error | None:
    ...
```

## Additional Note

The spec marks the `create_schedule` requestBody as `"required": true` (schema: `pipeline_schedule_post_request_body`
with `target` and `cron_pattern` required fields). The SDK also needs to remove the `= UNSET` default
and make `body` required, since passing UNSET would crash at `body.to_dict()` in the generated `_get_kwargs`.

Similarly the `update_schedule` requestBody is `"required": true` with schema `pipeline_schedule_put_request_body`.

The correct signatures should be:
```python
async def create_schedule(..., *, body: PipelineSchedulePostRequestBody) -> PipelineSchedule | Error | None:
async def update_schedule(..., *, body: PipelineSchedulePutRequestBody) -> PipelineSchedule | Error | None:
```

## Status

- [x] Confirmed via static analysis
- [x] Confirmed via spec inspection (requestBody required: true; wrong model type in SDK)
- [ ] Confirmed via live test run
