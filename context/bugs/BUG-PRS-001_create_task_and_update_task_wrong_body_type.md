# BUG-PRS-001: `create_task` and `update_task` declare `body: Unset = UNSET` but generated API requires typed schema

**Status:** CONFIRMED (static analysis + spec inspection)
**Layer:** sdk-wrapper
**Module:** `bb.cloud.sdk.prs`
**Functions:** `create_task`, `update_task`
**Severity:** High (callers cannot pass a task body via the type system; UNSET sent to API will crash at `body.to_dict()`)

## Exact Mismatch

| SDK function | SDK wrapper declaration | Generated API `_get_kwargs` expects |
|---|---|---|
| `create_task` (line 1248) | `body: Unset = UNSET` | `body: PullRequestTaskCreate` (required, no default) |
| `update_task` (line 1338) | `body: Unset = UNSET` | `body: PullRequestTaskUpdate` (required, no default) |

Generated modules:
- `src/bb/cloud/api/pullrequests/post_repositories_workspace_repo_slug_pullrequests_pull_request_id_tasks.py` — line 27: `body: PullRequestTaskCreate`
- `src/bb/cloud/api/pullrequests/put_repositories_workspace_repo_slug_pullrequests_pull_request_id_tasks_task_id.py` — line 28: `body: PullRequestTaskUpdate`

Spec paths:
- `POST /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/tasks`
- `PUT /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/tasks/{task_id}`

## Spec Inspection

```json
// POST tasks — requestBody:
{
  "content": {
    "application/json": {
      "schema": { "$ref": "#/components/schemas/pullrequest_task_create" }
    }
  },
  "description": "The contents of the task",
  "required": true
}

// Schema: pullrequest_task_create
{
  "type": "object",
  "title": "Pull Request Task Create",
  "properties": {
    "content": {
      "type": "object",
      "properties": { "raw": { "type": "string" } },
      "required": ["raw"],
      "additionalProperties": false
    },
    "comment": { "$ref": "#/components/schemas/comment" },
    "pending": { "type": "boolean" }
  },
  "required": ["content"],
  "additionalProperties": false
}

// PUT tasks/{task_id} — requestBody:
{
  "content": {
    "application/json": {
      "schema": { "$ref": "#/components/schemas/pullrequest_task_update" }
    }
  },
  "description": "The updated state and content of the task.",
  "required": true
}

// Schema: pullrequest_task_update
{
  "type": "object",
  "title": "Pull Request Task Update",
  "properties": {
    "content": {
      "type": "object",
      "properties": { "raw": { "type": "string" } },
      "required": ["raw"],
      "additionalProperties": false
    },
    "state": { "type": "string", "enum": ["RESOLVED", "UNRESOLVED"] }
  },
  "additionalProperties": false
}
```

Both requestBodies are marked `"required": true`. The generated `_get_kwargs` calls `body.to_dict()` unconditionally — passing `UNSET` raises `AttributeError` at runtime.

The `create_task` docstring explicitly says _"Currently limited to :data:`~bb.cloud.types.UNSET` due to spec constraints"_ — this is incorrect; the spec defines a clear, required `pullrequest_task_create` schema.

## Models

```python
# PullRequestTaskCreate — content required, comment/pending optional
@_attrs_define
class PullRequestTaskCreate:
    content: PullRequestTaskCreateTaskRawContent  # required: raw str
    comment: Comment | Unset = UNSET
    pending: bool | Unset = UNSET

# PullRequestTaskUpdate — all fields optional
@_attrs_define
class PullRequestTaskUpdate:
    content: PullRequestTaskUpdateTaskRawContent | Unset = UNSET  # raw str
    state: PullRequestTaskUpdateState | Unset = UNSET  # "RESOLVED" | "UNRESOLVED"
```

## Impact

1. **Runtime crash** — `UNSET.to_dict()` → `AttributeError` on every call
2. **Type errors** — callers who pass `PullRequestTaskCreate` get a mypy/pyright error (Unset ≠ PullRequestTaskCreate)
3. **Impossible to create tasks** — task creation is the primary use case; without a body with `content.raw`, the API returns 400
4. **Misleading docstring** — the claim "Currently limited to UNSET due to spec constraints" is factually wrong

## Fix

### SDK wrapper fix — `src/bb/cloud/sdk/prs.py`

```python
# Add to imports at top of file:
from ..models.pull_request_task_create import PullRequestTaskCreate
from ..models.pull_request_task_update import PullRequestTaskUpdate
from ..models.pullrequest_comment_task import PullrequestCommentTask

# create_task — change lines 1242-1285:
# BEFORE:
async def create_task(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    *,
    body: Unset = UNSET,
) -> Any | Error | None:
    """...body: Task payload. Currently limited to :data:`~bb.cloud.types.UNSET` due to
    spec constraints..."""

# AFTER:
async def create_task(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    *,
    body: PullRequestTaskCreate,
) -> PullrequestCommentTask | Error | None:
    """...body: Task payload. Must include content.raw (the task text).
    Optionally attach to a comment via body.comment, or pre-resolve via body.pending=False..."""
    result = await post_repositories_workspace_repo_slug_pullrequests_pull_request_id_tasks.asyncio(
        workspace, repo_slug, pull_request_id, client=client.auth, body=body
    )
    if isinstance(result, (PullrequestCommentTask, Error)):
        return result
    return None

# update_task — change lines 1331-1377:
# BEFORE:
async def update_task(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    task_id: int,
    *,
    body: Unset = UNSET,
) -> Any | Error | None:

# AFTER:
async def update_task(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    task_id: int,
    *,
    body: PullRequestTaskUpdate,
) -> PullrequestCommentTask | Error | None:
    result = await put_repositories_workspace_repo_slug_pullrequests_pull_request_id_tasks_task_id.asyncio(
        workspace, repo_slug, pull_request_id, task_id, client=client.auth, body=body
    )
    if isinstance(result, (PullrequestCommentTask, Error)):
        return result
    return None
```

Note: `create_task` body should have no default (spec marks it required). `update_task` body could technically be optional since all `PullRequestTaskUpdate` fields are optional — but since the spec marks the requestBody required, no default is correct.

## Status

- [x] Confirmed via static analysis (generated `_get_kwargs` calls `body.to_dict()` unconditionally)
- [x] Confirmed via spec inspection (requestBody required: true for both POST and PUT)
- [ ] Confirmed via live test run
