# BUG-SNIPPETS-002: Multiple snippet write functions had `body: Unset = UNSET` causing `AttributeError: 'Unset' object has no attribute 'to_dict'`

**Status:** FIXED
**Layer:** sdk-wrapper
**Module:** `bb.cloud.sdk.snippets`
**Functions:** `create`, `create_default`, `update`, `add_comment`, `update_comment`, `update_node`
**Severity:** High (all snippet write operations crash at the generated `_get_kwargs` call)

---

## Symptom

```
AttributeError: 'Unset' object has no attribute 'to_dict'
```

Triggered on any call to the affected functions where the caller relied on the default body — and on every call where `body=UNSET` was passed (explicitly or by omission).

---

## Affected Functions

| Function | Old default | New default (fixed) |
|---|---|---|
| `create` | `body: Snippet \| Unset = UNSET` | `body: Snippet = Snippet()` |
| `create_default` | `body: Snippet \| Unset = UNSET` | `body: Snippet = Snippet()` |
| `update` | `body: Snippet \| Unset = UNSET` | `body: Snippet = Snippet()` |
| `add_comment` | `body: SnippetComment \| Unset = UNSET` | `body: SnippetComment = SnippetComment()` |
| `update_comment` | `body: SnippetComment \| Unset = UNSET` | `body: SnippetComment = SnippetComment()` |
| `update_node` | `body: Snippet \| Unset = UNSET` | `body: Snippet = Snippet()` |

---

## Root Cause

Same root cause as BUG-PRS-001 and BUG-REPOS-001. Each of these endpoints has a `requestBody` in the spec (required or optional), and the generated `_get_kwargs` calls `body.to_dict()` unconditionally. The SDK wrappers were written with `Unset = UNSET` as a permissive default, not accounting for the unconditional `to_dict()` call.

`Snippet` and `SnippetComment` are attrs `@define` classes with all optional fields (no required positional arguments), so `Snippet()` and `SnippetComment()` are valid zero-argument constructors and serve as correct empty-body defaults.

---

## Fix Applied

Changed all six function signatures from `body: Model | Unset = UNSET` to `body: Model = Model()`:

```python
# BEFORE (broken — all six functions):
async def create(..., body: Snippet | Unset = UNSET) -> Snippet | Error | None:
async def create_default(..., body: Snippet | Unset = UNSET) -> Snippet | Error | None:
async def update(..., body: Snippet | Unset = UNSET) -> Snippet | Error | None:
async def add_comment(..., body: SnippetComment | Unset = UNSET) -> SnippetComment | Error | None:
async def update_comment(..., body: SnippetComment | Unset = UNSET) -> SnippetComment | Error | None:
async def update_node(..., body: Snippet | Unset = UNSET) -> ...:

# AFTER (fixed):
async def create(..., body: Snippet = Snippet()) -> Snippet | Error | None:
async def create_default(..., body: Snippet = Snippet()) -> Snippet | Error | None:
async def update(..., body: Snippet = Snippet()) -> Snippet | Error | None:
async def add_comment(..., body: SnippetComment = SnippetComment()) -> SnippetComment | Error | None:
async def update_comment(..., body: SnippetComment = SnippetComment()) -> SnippetComment | Error | None:
async def update_node(..., body: Snippet = Snippet()) -> ...:
```

---

## Current State

Fixed. All six functions in `src/bb/cloud/sdk/snippets.py` now use `Model = Model()` defaults (confirmed by code inspection at lines 159, 205, 334, 615, 702, 905).

---

## Note on `Snippet()` and `SnippetComment()` as Defaults

Using a mutable default (`Snippet()`) in a function signature is technically a Python anti-pattern (shared mutable default). However, since these are attrs `@define` classes and the generated `to_dict()` call only reads from the object (no mutation), this is safe in practice. The real fix would be to make `body` a required argument for write operations — but using `Model()` is a pragmatic interim fix that eliminates the crash.
