# BUG-ISSUES-003: `issues.update` requires `body` keyword argument but test calls it without `body`

**Status:** NEEDS-FIX (either add a default body to wrapper, or update test)
**Layer:** sdk-wrapper
**Module:** `bb.cloud.sdk.issues`
**Function:** `update`
**Severity:** Medium (test failure / API misuse — the function signature does not match expected call patterns)

---

## Symptom

```
TypeError: update() missing 1 required keyword-only argument: 'body'
```

Observed when the live test suite calls:
```python
result = await issues.update(client, workspace, repo_slug, issue_id)
```
to verify that a nonexistent issue returns `Error` or `None`. The test omits `body` because it expects a 404 or error response — the body content is irrelevant for the negative-path test.

---

## Current Wrapper Code

```python
# src/bb/cloud/sdk/issues.py, line ~236
async def update(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    issue_id: int,
    *,
    body: Issue,  # required — no default
) -> Issue | Error | None:
```

`body` has no default. The call `issues.update(client, ws, repo, id)` therefore raises `TypeError` before any HTTP call is made.

---

## Root Cause

The function was written with `body: Issue` (required, no default) — which is correct for a write operation — but the test was written expecting to call `update()` without a body to exercise the 404 path. These two assumptions are incompatible.

There are two valid ways to resolve this:

**Option A — Add a default body:**
```python
async def update(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    issue_id: int,
    *,
    body: Issue = Issue(),
) -> Issue | Error | None:
```
`Issue()` is a valid zero-argument default. This allows tests to call `update()` without a body.

**Option B — Fix the test:**
```python
# In the test — pass a minimal Issue body even for negative-path tests:
result = await issues.update(client, ws, repo_slug, nonexistent_id, body=Issue())
```
This keeps the wrapper signature strict (body required) and makes the test explicit about what body it sends.

---

## Spec Context

`PUT /repositories/{workspace}/{repo_slug}/issues/{issue_id}` has `requestBody: required: true` in the spec. The generated `_get_kwargs` calls `body.to_dict()` unconditionally. If Option A is chosen (default `Issue()`), the generated code will serialize an empty issue body and the API will return 404 — which is still the correct test outcome for a nonexistent issue.

---

## Current State

**Not fixed.** `src/bb/cloud/sdk/issues.py` line ~242 reads `body: Issue` with no default. Any call omitting `body=` raises `TypeError`.

---

## Recommended Resolution

**Option A** (add `body: Issue = Issue()`) is preferable for consistency with other write functions in this module (e.g., `add_change` uses `IssueChange(type_="issue_change")` as a default). It avoids requiring callers to construct a body for simple existence-check patterns.
