# BUG-SCHEMA-035 — Deprecated Endpoints Return CHANGE-2770 Error at Runtime

**Status:** CONFIRMED  
**Layer:** sdk-wrapper  
**Severity:** P2 — deprecated endpoint silently breaks previously-working SDK functions  
**Discovered:** 2026-05-20 (live test run during test suite improvement pass)

---

## Affected SDK Functions

| SDK Function | Endpoint | Deprecated Since |
|---|---|---|
| `repos.my_permissions(client)` | `GET /2.0/user/permissions/repositories` | CHANGE-2770 |
| `sync.repos.my_permissions(client)` | same | CHANGE-2770 |
| `workspaces.list(client)` | `GET /2.0/workspaces` | CHANGE-2770 |
| `sync.workspaces.list(client)` | same | CHANGE-2770 |

`workspaces.my_permissions()`, `workspaces.repo_permissions()`, and other workspace endpoints are **not** affected — only the two above.

---

## Symptom

Calling either function returns `Error` instead of the expected list:

```python
result = await repos.my_permissions(client)
# result = Error(type_='error', error=ErrorError(
#     message='CHANGE-2770 - Functionality has been deprecated',
#     detail='Please read the changelog entry for more details.',
#     data={'announcement_url': 'https://developer.atlassian.com/cloud/bitbucket/changelog#CHANGE-2770'}
# ))
```

The SDK does not crash — the Error is correctly returned. But callers expecting a `list` silently receive an `Error` object.

---

## Root Cause

Bitbucket has deprecated two API endpoints as part of CHANGE-2770:

- `GET /2.0/workspaces` → replaced by workspace membership APIs
- `GET /2.0/user/permissions/repositories` → replaced by workspace-scoped repository permission APIs

These endpoints now return an error payload (HTTP 403 or 410) with the CHANGE-2770 message. The spec fix BUG-SCHEMA-018 already added `410 Gone` to `/user/permissions/repositories`, so the SDK correctly parses the response as `Error` rather than crashing.

---

## Impact

- `test_repos.py::test_my_permissions_returns_list` — now skips (graceful)
- `test_repos.py::test_my_permissions_pagination_integrity` — now skips (graceful)
- `test_sync_smoke.py::test_sync_workspaces_list_returns_list` — now skips (graceful)
- Any caller of `repos.my_permissions()` or `workspaces.list()` receives `Error` and must handle it

---

## Replacement Endpoints

| Deprecated | Replacement |
|---|---|
| `GET /2.0/user/permissions/repositories` | `GET /2.0/repositories/{workspace}` (filter by current user) or `workspaces.repo_permissions(client, workspace)` |
| `GET /2.0/workspaces` | `workspaces.mine(client)` — returns workspaces the authenticated user is a member of |

---

## Required Actions

### 1. Update SDK wrappers (sdk-wrapper fix)

**`repos.my_permissions()`** — deprecate the function, redirect callers:

```python
async def my_permissions(client: BBClient, *, pagelen: int = 25) -> list[Any] | Error:
    # CHANGE-2770: GET /user/permissions/repositories is deprecated.
    # Use workspaces.repo_permissions(client, workspace) per workspace instead.
    import warnings
    warnings.warn(
        "repos.my_permissions() is deprecated (CHANGE-2770). "
        "Use workspaces.repo_permissions(client, workspace) instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    result = await async_paginate(...)
    return result
```

**`workspaces.list()`** — deprecate and redirect to `workspaces.mine()`:

```python
async def list(client: BBClient, *, pagelen: int = 25) -> list[Workspace] | Error:
    # CHANGE-2770: GET /workspaces is deprecated. Use workspaces.mine() instead.
    import warnings
    warnings.warn(
        "workspaces.list() is deprecated (CHANGE-2770). "
        "Use workspaces.mine(client) instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    result = await async_paginate(...)
    return result
```

### 2. Update tests

- `test_repos.py::test_my_permissions_*` — update to use `workspaces.repo_permissions()` instead
- `test_workspaces.py::test_list_*` — verify these already use `workspaces.mine()` (they do; `test_list_returns_workspaces` uses `workspaces.list()` and may need the same treatment)
- `test_sync_smoke.py::test_sync_workspaces_list_returns_list` — already skips gracefully; update to test `sync.workspaces.mine()` instead

### 3. Update sync equivalents

Same deprecation warnings in `src/bb/cloud/sync/repos.py` and `src/bb/cloud/sync/workspaces.py`.

---

## Relation to Prior Bugs

- **BUG-SCHEMA-018** (FIXED) — added `410 Gone` to `/user/permissions/repositories`; this is why the SDK returns `Error` correctly instead of crashing on the deprecated response.
- **BUG-SCHEMA-034** (CLOSED) — investigated whether deprecated endpoints return 410; concluded they return 403 at the time. As of 2026-05-20, at least `/user/permissions/repositories` returns an error payload matching the CHANGE-2770 announcement. Re-evaluation may be needed.

---

## Workaround (immediate, no code change)

Callers can detect and handle the deprecation error:

```python
result = await repos.my_permissions(client)
if isinstance(result, Error) and "CHANGE-2770" in (result.error.message or ""):
    # Endpoint deprecated — use workspaces.repo_permissions() instead
    result = await workspaces.repo_permissions(client, workspace)
```
