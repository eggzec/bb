# BUG-BRANCHING-001: `update_settings` / `update_project_settings` crash — body defaults to UNSET, spec missing requestBody

**Status:** FIXED
**Root cause:** sdk-wrapper + spec — `body: BranchingModelSettings | Unset = UNSET` crashes `to_dict()` on default; spec also missing `requestBody` for both PUT branching-model-settings endpoints
**Layer:** sdk-wrapper, spec

---

## Affected functions
- `bb.cloud.sdk.branching_model.update_settings`
- `bb.cloud.sdk.branching_model.update_project_settings`

---

## Description

Two independent defects compound into the same failure.

**Part 1 — SDK wrapper:** Both `update_settings` and `update_project_settings` declared `body: BranchingModelSettings | Unset = UNSET`. The generated `_get_kwargs` for each endpoint calls `body.to_dict()` unconditionally (the generated code assumes `body` is always a concrete model). Calling either function without an explicit body (using the UNSET default) raises:

```
AttributeError: 'Unset' object has no attribute 'to_dict'
```

This is the same pattern as BUG-SNIPPETS-002, BUG-ISSUES-002/003, and BUG-WEBHOOKS-001.

**Part 2 — Spec:** The OpenAPI spec was missing `requestBody` for the two PUT endpoints:
- `PUT /repositories/{workspace}/{repo_slug}/branching-model/settings`
- `PUT /workspaces/{workspace}/projects/{project_key}/branching-model/settings`

Without `requestBody` in the spec, the generator produces `_get_kwargs` without a `body` parameter — so even when a caller passes a valid body, it is silently discarded and the request is sent with no payload, causing a 400 from the API.

---

## Evidence

**SDK wrapper before fix** (`src/bb/cloud/sdk/branching_model.py`):

```python
# update_settings (~line 143)
async def update_settings(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: BranchingModelSettings | Unset = UNSET,
) -> BranchingModelSettings | Error | None:
    ...

# update_project_settings (~line 262)
async def update_project_settings(
    client: BBClient,
    workspace: str,
    project_key: str,
    *,
    body: BranchingModelSettings | Unset = UNSET,
) -> BranchingModelSettings | Error | None:
    ...
```

**SDK wrapper after fix:**

```python
# update_settings
async def update_settings(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: BranchingModelSettings,
) -> BranchingModelSettings | Error | None:
    ...

# update_project_settings
async def update_project_settings(
    client: BBClient,
    workspace: str,
    project_key: str,
    *,
    body: BranchingModelSettings,
) -> BranchingModelSettings | Error | None:
    ...
```

**Spec fix** — `requestBody` added to both PUT endpoints in `bb_cloud_fixed.openapi.json`:

```json
"requestBody": {
  "required": true,
  "content": {
    "application/json": {
      "schema": { "$ref": "#/components/schemas/branching_model_settings" }
    }
  }
}
```

---

## Generated code impact

Before the spec fix, `_get_kwargs` in both generated modules had no `body` parameter and did not inject `_kwargs["json"]`. After the spec fix and regeneration, `_get_kwargs` gains `body: BranchingModelSettings` and injects `_kwargs["json"] = body.to_dict()`.

---

## Impact

- `branching_model.update_settings()` crashes with `AttributeError` when called without an explicit body (the only possible call given the UNSET default)
- Even calls with a valid body silently sent no payload (spec bug) → HTTP 400 from the API
- Both the repo-scoped and project-scoped settings update functions are entirely non-functional

---

## Fix Applied

1. Spec: added `requestBody` to both PUT branching-model-settings endpoints in `bb_cloud_fixed.openapi.json`
2. Regenerated: `make generate-cloud && make diff-cloud`
3. SDK: changed `body: BranchingModelSettings | Unset = UNSET` → `body: BranchingModelSettings` (required, no default) in both functions

---

## Status

- [x] Confirmed via static analysis (signature mismatch + spec inspection)
- [x] Fixed in `src/bb/cloud/sdk/branching_model.py` and `bb_cloud_fixed.openapi.json`
