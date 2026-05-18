# BUG-PIPELINES-002: `update_config` has `body: Unset = UNSET` but API requires `PipelinesConfig`

**Module:** `bb.cloud.sdk.pipelines`
**Function:** `update_config`
**Severity:** Critical (runtime `AttributeError` on every real call — `UNSET.to_dict()` crashes; callers cannot pass a body)

## Description

The `update_config` SDK wrapper declares `body: Unset = UNSET`, which means callers can only pass
`UNSET` — it is impossible to pass an actual `PipelinesConfig` object through the type system.
The underlying generated API module expects `body: PipelinesConfig`.

## Evidence

**SDK wrapper** (`src/bb/cloud/sdk/pipelines.py`, line 518):
```python
async def update_config(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: Unset = UNSET,
) -> Any:
```

**Generated API** (`src/bb/cloud/api/pipelines/update_repository_pipeline_config.py`, line ~25):
```python
def _get_kwargs(
    workspace: str,
    repo_slug: str,
    *,
    body: PipelinesConfig,
) -> dict[str, Any]:
```

## Impact

- Callers following the type hint cannot meaningfully call `update_config` (always sends UNSET body)
- The API will receive an empty/malformed request body, likely returning 400
- Runtime duck-typing works if a `PipelinesConfig` is forced through (as our test does), because `PipelinesConfig.to_dict()` exists

## Recommended Fix

```python
from bb.cloud.models.pipelines_config import PipelinesConfig

async def update_config(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: PipelinesConfig | Unset = UNSET,
) -> PipelinesConfig | Error | None:
    result = await update_repository_pipeline_config.asyncio(
        workspace, repo_slug, client=client.auth, body=body
    )
    if isinstance(result, (PipelinesConfig, Error)):
        return result
    return None
```

## Spec Confirmation

```json
// PUT /repositories/{workspace}/{repo_slug}/pipelines_config — requestBody:
{
  "content": { "application/json": { "schema": { "$ref": "#/components/schemas/pipelines_config" } } },
  "description": "The updated repository pipelines configuration.",
  "required": true
}
```

The `required: true` means passing `UNSET` (which has no `.to_dict()`) will crash.
The fix must remove `= UNSET` default and make `body` required.

## Fix Applied

**File:** `src/bb/cloud/sdk/pipelines.py`

**Imports added** (lines 71, 80 after fix):
```python
from bb.cloud.models.pipeline_build_number import PipelineBuildNumber  # line 71
from bb.cloud.models.pipelines_config import PipelinesConfig            # line 80
```

**Before (line 518–523):**
```python
async def update_config(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: Unset = UNSET,
) -> Any:
```

**After (line 518–523):**
```python
async def update_config(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: PipelinesConfig,
) -> Any:
```

The `= UNSET` default was removed, making `body` required and correctly typed as `PipelinesConfig`.

## Status

- [x] Confirmed via static analysis
- [x] Confirmed via spec inspection (requestBody required: true, schema: pipelines_config)
- [x] FIXED — `body: Unset = UNSET` → `body: PipelinesConfig` (required, no default)
- [ ] Confirmed via live test run

**Status:** FIXED
