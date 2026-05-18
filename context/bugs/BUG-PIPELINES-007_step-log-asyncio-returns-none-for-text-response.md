# BUG-PIPELINES-007: `step_log` always returns `None` — `asyncio()` not emitted for `text/plain` pipeline log responses

**Status:** FIXED
**Root cause:** sdk-wrapper — `asyncio()` returns `None` for `text/plain` responses; generator only emits typed `asyncio()` for JSON responses with schema
**Layer:** sdk-wrapper

---

## Affected functions
- `bb.cloud.sdk.pipelines.step_log`

---

## Description

`pipelines.step_log` called `get_pipeline_step_log_for_repository.asyncio()`. Pipeline step logs are returned as raw `text/plain` content — not JSON. The `openapi-python-client` generator only emits a typed `sync()`/`asyncio()` variant (returning a parsed model) when the response maps to a documented JSON schema. For endpoints that return binary or plain-text content, `_parse_response()` returns `None` for all status codes, so `asyncio()` always returns `None`.

The result: `step_log()` always returned `None`, silently discarding the actual log content regardless of whether the pipeline step had output.

This is the same root cause as BUG-SOURCE-001 (`source.get` returning `None` for `text/plain` files), which was already fixed by switching to `asyncio_detailed()`.

---

## Evidence

**SDK wrapper before fix** (`src/bb/cloud/sdk/pipelines.py`, ~line 467):

```python
async def step_log(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    pipeline_uuid: str,
    step_uuid: str,
) -> str | None:
    result = await get_pipeline_step_log_for_repository.asyncio(
        workspace, repo_slug, pipeline_uuid, step_uuid, client=client.auth
    )
    return result  # type: ignore[return-value]  # always None
```

**SDK wrapper after fix:**

```python
async def step_log(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    pipeline_uuid: str,
    step_uuid: str,
) -> str | None:
    response = await get_pipeline_step_log_for_repository.asyncio_detailed(
        workspace, repo_slug, pipeline_uuid, step_uuid, client=client.auth
    )
    if response.status_code == 200:
        return response.content.decode("utf-8", errors="replace")
    # 304, 404, 416, or any other non-200 → no log available
    return None
```

---

## Root Cause

The generator pattern: for endpoints whose 200 response is `text/plain` or `application/octet-stream`, `_parse_response()` has no branch to deserialize the content into a typed model and returns `None`. The `asyncio()` helper returns `response.parsed`, which is always `None` in this case.

Only `asyncio_detailed()` exposes `response.content` (raw bytes) and `response.status_code`. The fix uses `asyncio_detailed()` and manually decodes `response.content` as UTF-8. The `errors="replace"` argument ensures malformed bytes (e.g. from binary artifacts in logs) do not crash the decode.

The 416 (Range Not Satisfiable) and 304 (Not Modified) cases return `None`, matching the expected contract for partial/cached responses.

---

## Impact

- `pipelines.step_log()` returned `None` on every call, even for steps with substantial output
- Pipeline debugging via the SDK was entirely broken
- The `# type: ignore[return-value]` comment in the original code was a hint that the author noticed the type mismatch but did not address the root cause

---

## Fix Applied

Switched from `asyncio()` to `asyncio_detailed()` in `src/bb/cloud/sdk/pipelines.py`. Manually decode `response.content` for 200 responses; return `None` for all other status codes.

---

## Status

- [x] Confirmed via static analysis (generator emits no typed `asyncio()` for text/plain endpoints)
- [x] Fixed in `src/bb/cloud/sdk/pipelines.py`
