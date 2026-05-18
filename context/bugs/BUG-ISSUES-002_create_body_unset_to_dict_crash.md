# BUG-ISSUES-002: `issues.create` passes `UNSET` to generated code that calls `body.to_dict()` unconditionally

**Status:** NEEDS-FIX (not yet applied)
**Layer:** sdk-wrapper
**Module:** `bb.cloud.sdk.issues`
**Function:** `create`
**Severity:** High (runtime `AttributeError` on every call using the default body)

---

## Symptom

```
AttributeError: 'Unset' object has no attribute 'to_dict'
```

Triggered at runtime when `issues.create()` is called without an explicit `body=` argument, or when `body=UNSET` is passed.

---

## Current Wrapper Code (unfixed)

```python
# src/bb/cloud/sdk/issues.py, line ~193
async def create(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: Issue | Unset = UNSET,  # ← UNSET is the default
) -> Issue | Error | None:
    result = await post_repositories_workspace_repo_slug_issues.asyncio(
        workspace, repo_slug, client=client.auth, body=body
    )
```

When `body=UNSET`, the generated `_get_kwargs` calls `body.to_dict()` → `AttributeError`.

---

## Root Cause

Same pattern as BUG-PRS-001, BUG-REPOS-001, and BUG-SNIPPETS-002. The Bitbucket spec marks `POST /repositories/{workspace}/{repo_slug}/issues` `requestBody` as `required: true`. The generated `_get_kwargs` therefore calls `body.to_dict()` unconditionally with no guard.

The `Issue` model (generated, attrs `@define`) has several optional fields and can be constructed with `Issue()` (no required positional arguments), making `Issue()` a valid zero-argument default.

---

## Fix Required

Change the signature from `body: Issue | Unset = UNSET` to `body: Issue = Issue()`:

```python
async def create(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: Issue = Issue(),  # or make body required (no default)
) -> Issue | Error | None:
    result = await post_repositories_workspace_repo_slug_issues.asyncio(
        workspace, repo_slug, client=client.auth, body=body
    )
    if isinstance(result, (Issue, Error)):
        return result
    return None
```

Alternatively, make `body` a required argument (no default) since creating an issue without any fields is not useful.

---

## Current State

**Not fixed.** `src/bb/cloud/sdk/issues.py` line ~193 still reads `body: Issue | Unset = UNSET`. The function will crash with `AttributeError` at runtime.
