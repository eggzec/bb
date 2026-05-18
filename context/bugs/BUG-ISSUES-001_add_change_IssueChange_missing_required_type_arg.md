# BUG-ISSUES-001: `issues.add_change` default `IssueChange()` fails at module import — `type_` is a required positional argument

**Status:** FIXED
**Layer:** sdk-wrapper
**Module:** `bb.cloud.sdk.issues`
**Function:** `add_change`
**Severity:** Critical (crashes Python at module import time — all of `bb.cloud.sdk.issues` becomes unimportable)

---

## Symptom

```
TypeError: IssueChange.__init__() missing 1 required positional argument: 'type_'
```

This exception is raised **at module load time** (when Python evaluates the default argument expression `IssueChange()` in the function signature), not at call time. As a result, the entire `bb.cloud.sdk.issues` module fails to import, making all issue SDK functions inaccessible.

---

## Root Cause

The `IssueChange` attrs model (generated) has `type_: str` as a **required** field with no default:

```python
# src/bb/cloud/models/issue_change.py (generated)
@_attrs_define
class IssueChange:
    type_: str  # required — no UNSET default
    changes: IssueChangeChanges | Unset = UNSET
    created_on: datetime.datetime | Unset = UNSET
    issue: Issue | Unset = UNSET
    links: IssueChangeLinks | Unset = UNSET
    message: IssueChangeMessage | Unset = UNSET
    name: str | Unset = UNSET
    user: Account | Unset = UNSET
```

The SDK wrapper for `add_change` used `IssueChange()` as a function-signature default:

```python
# BEFORE (broken):
async def add_change(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    issue_id: int,
    *,
    body: IssueChange = IssueChange(),  # ← evaluated at module load; IssueChange() → TypeError
) -> IssueChange | Error | None:
```

Python evaluates default argument expressions when the `def` statement is executed (module import). `IssueChange()` raises `TypeError` immediately because `type_` has no default.

---

## Impact

1. `import bb.cloud.sdk.issues` → `TypeError` — module never loads
2. All issue-related CLI commands or SDK calls fail at import, not just `add_change`
3. Any code doing `from bb.cloud.sdk import issues` similarly fails

---

## Fix Applied

Changed the default to `IssueChange(type_="issue_change")`, supplying the required field:

```python
# AFTER (fixed):
async def add_change(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    issue_id: int,
    *,
    body: IssueChange = IssueChange(type_="issue_change"),
) -> IssueChange | Error | None:
```

`"issue_change"` is the correct literal type discriminator value for this model, consistent with the Bitbucket API's object typing convention.

---

## Current State

Fixed. `src/bb/cloud/sdk/issues.py` line ~953 reads `body: IssueChange = IssueChange(type_="issue_change")` (confirmed by code inspection).

---

## General Rule

> When using a model as a function-signature default (`body: Model = Model()`), always verify that the model's `__init__` accepts zero arguments. If any field is required (no `| Unset = UNSET`), the default expression `Model()` will raise `TypeError` at import time. Supply all required fields explicitly or make `body` a required parameter with no default.
