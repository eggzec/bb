# BUG-ISSUES-004: `add_comment` / `update_comment` crash — `body` defaults to UNSET, `to_dict()` raises `AttributeError`

**Status:** FIXED
**Root cause:** sdk-wrapper — `body: IssueComment | Unset = UNSET` causes `body.to_dict()` to raise `AttributeError` when body is not explicitly provided
**Layer:** sdk-wrapper

---

## Affected functions
- `bb.cloud.sdk.issues.add_comment`
- `bb.cloud.sdk.issues.update_comment`

---

## Description

Both `add_comment` and `update_comment` declared `body: IssueComment | Unset = UNSET`. The generated `_get_kwargs` for the issue comment POST/PUT endpoints calls `body.to_dict()` unconditionally (the spec correctly documents a required requestBody for these endpoints). Calling either function without an explicit body uses the `UNSET` default and raises:

```
AttributeError: 'Unset' object has no attribute 'to_dict'
```

This is the same pattern as BUG-SNIPPETS-002, BUG-ISSUES-002 (`create`), BUG-ISSUES-003 (`update`), and BUG-ISSUES-001 (`add_change`). The four issues comment-related functions in `issues.py` all had the same defect; this bug covers the two that were not previously reported.

---

## Evidence

**SDK wrapper before fix** (`src/bb/cloud/sdk/issues.py`):

```python
# add_comment (~line 383)
async def add_comment(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    issue_id: int,
    *,
    body: IssueComment | Unset = UNSET,
) -> IssueComment | Error | None:
    ...

# update_comment (~line 813)
async def update_comment(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    issue_id: int,
    comment_id: int,
    *,
    body: IssueComment | Unset = UNSET,
) -> IssueComment | Error | None:
    ...
```

**SDK wrapper after fix:**

```python
# add_comment
async def add_comment(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    issue_id: int,
    *,
    body: IssueComment = IssueComment(),
) -> IssueComment | Error | None:
    ...

# update_comment
async def update_comment(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    issue_id: int,
    comment_id: int,
    *,
    body: IssueComment = IssueComment(),
) -> IssueComment | Error | None:
    ...
```

The default `IssueComment()` constructs an empty comment model (all fields `UNSET`). This satisfies `body.to_dict()` without crashing. In practice, callers should always supply a populated `IssueComment` with at least a `content` field.

---

## Impact

- `issues.add_comment()` and `issues.update_comment()` raise `AttributeError` immediately before any HTTP call whenever called without an explicit body
- Since the type hint showed `| Unset = UNSET`, callers following the hint would naturally omit the body and crash
- Issue commenting was entirely non-functional through the SDK

---

## Fix Applied

Changed `body: IssueComment | Unset = UNSET` → `body: IssueComment = IssueComment()` for both functions in `src/bb/cloud/sdk/issues.py`.

---

## Status

- [x] Confirmed via static analysis (signature mismatch is unambiguous)
- [x] Fixed in `src/bb/cloud/sdk/issues.py`
