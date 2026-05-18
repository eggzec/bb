# BUG-PRS-003: `add_comment` declares `body: PullRequestComment | Unset = UNSET` but generated code calls `body.to_dict()` unconditionally

**Status:** NEEDS-FIX (not yet applied as of current codebase)
**Layer:** sdk-wrapper
**Module:** `bb.cloud.sdk.prs`
**Function:** `add_comment`
**Severity:** High (runtime `AttributeError` on every call with the default `UNSET` body)

---

## Symptom

```
AttributeError: 'Unset' object has no attribute 'to_dict'
```

Triggered any time `add_comment` is called without an explicit `body=` argument — or whenever the generated `_get_kwargs` executes before a valid `PullRequestComment` is passed (e.g., defensive coding that passes `UNSET`).

---

## Exact Mismatch

| Layer | Declaration |
|---|---|
| SDK wrapper (`prs.py`, line ~613) | `body: PullRequestComment \| Unset = UNSET` |
| Generated `_get_kwargs` (post...comments.py) | `body: PullRequestComment` — required, no default; calls `body.to_dict()` unconditionally |

**Current wrapper code (unfixed):**
```python
async def add_comment(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    *,
    body: PullRequestComment | Unset = UNSET,
) -> PullRequestComment | Error | None:
    result = await post_repositories_workspace_repo_slug_pullrequests_pull_request_id_comments.asyncio(
        workspace, repo_slug, pull_request_id, client=client.auth, body=body
    )
```

When `body=UNSET` (the default), the generated `_get_kwargs` calls `body.to_dict()` → `AttributeError`.

---

## Root Cause

Same pattern as BUG-PRS-001 (`create_task`/`update_task`). The wrapper was generated/written with `Unset = UNSET` as a catch-all default without checking whether the generated endpoint's `requestBody` is marked `required: true`.

The Bitbucket spec marks the `POST /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments` `requestBody` as `required: true` with schema `pullrequest_comment`. The generated module's `_get_kwargs` therefore has no guard and calls `body.to_dict()` unconditionally.

---

## Spec

```json
// POST .../pullrequests/{id}/comments
"requestBody": {
  "required": true,
  "content": {
    "application/json": {
      "schema": { "$ref": "#/components/schemas/pullrequest_comment" }
    }
  }
}
```

The `pullrequest_comment` schema defines:
- `content` — required object with `raw: str`
- `parent`, `inline` — optional

---

## Fix Required

Change the signature to require a `PullRequestComment` (no `UNSET` default):

```python
# In src/bb/cloud/sdk/prs.py

async def add_comment(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    *,
    body: PullRequestComment,  # required; remove UNSET default
) -> PullRequestComment | Error | None:
    result = await post_repositories_workspace_repo_slug_pullrequests_pull_request_id_comments.asyncio(
        workspace, repo_slug, pull_request_id, client=client.auth, body=body
    )
    if isinstance(result, (PullRequestComment, Error)):
        return result
    return None
```

The `PullRequestComment` import is already present in `prs.py`.

---

## Current State

**Not fixed.** The wrapper at `src/bb/cloud/sdk/prs.py` line ~613 still reads:
```python
body: PullRequestComment | Unset = UNSET,
```

This will crash at runtime when called with the default body. The call to `asyncio()` at line 650–651 passes `body=UNSET` directly to the generated API.
