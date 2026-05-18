# BUG-PRS-002: `diff`, `patch`, `diffstat`, `merge_task_status` called `.asyncio()` which does not exist

**Status:** FIXED
**Layer:** sdk-wrapper
**Module:** `bb.cloud.sdk.prs`
**Functions:** `diff`, `patch`, `diffstat`, `merge_task_status`
**Severity:** High (runtime `AttributeError` — functions completely unusable)

---

## Symptom

```
AttributeError: module 'bb.cloud.api.pullrequests.get_repositories_workspace_repo_slug_pullrequests_pull_request_id_diff' has no attribute 'asyncio'
```

Same error for the `_patch`, `_diffstat`, and `_merge_task_status_task_id` endpoint modules.

---

## Root Cause

The `openapi-python-client` generator only emits the `asyncio()` shorthand helper when the endpoint has a **parseable typed response** (i.e., `_parse_response` returns a typed model). For endpoints that return:

- **Binary content** (diff/patch — `application/octet-stream` or `text/plain` redirect)
- **Redirect-only** (302 with no body)
- **JSON not mapped to a model** (diffstat)

the generator emits **only** `asyncio_detailed()` — the `asyncio()` shorthand is absent. The SDK wrappers for these four functions called the non-existent `asyncio()` attribute.

| Function | Endpoint | Response type | `asyncio()` exists? |
|---|---|---|---|
| `diff` | `GET .../pullrequests/{id}/diff` | redirect/plain-text | No — binary redirect |
| `patch` | `GET .../pullrequests/{id}/patch` | redirect/plain-text | No — binary redirect |
| `diffstat` | `GET .../pullrequests/{id}/diffstat` | JSON (no model) | No — unmapped JSON |
| `merge_task_status` | `GET .../pullrequests/{id}/merge/task-status/{task_id}` | JSON (no model) | No — unmapped JSON |

---

## Generated Code Evidence

```python
# get_repositories_workspace_repo_slug_pullrequests_pull_request_id_diff.py
# Only defines:
def sync_detailed(...) -> Response[Any]: ...
async def asyncio_detailed(...) -> Response[Any]: ...
# NO sync() or asyncio() — because _parse_response always returns None
```

---

## Fix Applied

Changed all four functions to use `asyncio_detailed()` and extract content from `response.content` or `response.parsed`.

**`diff` — extract decoded bytes:**
```python
# BEFORE (broken):
result = await get_..._diff.asyncio(workspace, repo_slug, pull_request_id, client=client.auth)

# AFTER (fixed):
response = await get_..._diff.asyncio_detailed(workspace, repo_slug, pull_request_id, client=client.auth)
if response.status_code.value in (200, 302):
    return response.content.decode()
return None
```

**`patch` — same pattern as `diff`:**
```python
response = await get_..._patch.asyncio_detailed(workspace, repo_slug, pull_request_id, client=client.auth)
if response.status_code.value in (200, 302):
    return response.content.decode()
return None
```

**`diffstat` — JSON-decode raw bytes:**
```python
response = await get_..._diffstat.asyncio_detailed(workspace, repo_slug, pull_request_id, client=client.auth)
if response.status_code.value == 200:
    import json as _json
    return _json.loads(response.content)
return response.parsed
```

**`merge_task_status` — return `.parsed`:**
```python
response = await get_..._merge_task_status_task_id.asyncio_detailed(
    workspace, repo_slug, pull_request_id, task_id, client=client.auth
)
return response.parsed
```

---

## Current State

Fixed. All four functions use `asyncio_detailed()` as of the current codebase state (confirmed at lines 691, 1549, 1591, 1737 of `src/bb/cloud/sdk/prs.py`).

---

## General Rule

> For any generated endpoint module where `_parse_response` always returns `None` (binary content, redirects, or unmapped JSON), the generator will not emit `asyncio()` or `sync()`. SDK wrappers must always use `asyncio_detailed()` and work with `response.content`, `response.headers`, and `response.status_code` directly.
