# BUG-REPOS-002: `override_settings` crashes — `body` defaults to UNSET; also resolves BUG-REPOS-001 (`set_group_permission` / `set_user_permission`)

**Status:** FIXED
**Root cause:** sdk-wrapper — `body: Unset = UNSET` or wrong type defaults cause `AttributeError` before any HTTP call
**Layer:** sdk-wrapper

---

## Affected functions
- `bb.cloud.sdk.repos.override_settings` (new bug, previously undocumented)
- `bb.cloud.sdk.repos.set_group_permission` (resolves BUG-REPOS-001)
- `bb.cloud.sdk.repos.set_user_permission` (resolves BUG-REPOS-001)

---

## Description

### `override_settings` (new — BUG-REPOS-002)

`repos.override_settings` declared `body: Unset = UNSET` as a keyword-only argument. The underlying endpoint `PUT /repositories/{workspace}/{repo_slug}/override-settings` requires a `RepositoryInheritanceState` body. The generated `_get_kwargs` calls `body.to_dict()` unconditionally. With `UNSET` as the value, this raises:

```
AttributeError: 'Unset' object has no attribute 'to_dict'
```

### `set_group_permission` / `set_user_permission` (resolves BUG-REPOS-001)

Both permission-setter functions also had `body: Unset = UNSET` instead of the required `BitbucketAppsPermissionsSerializersRepoPermissionUpdateSchema` type. This was previously documented as BUG-REPOS-001 (CONFIRMED). The fix applied here resolves that open bug.

---

## Evidence

**SDK wrapper before fix** (`src/bb/cloud/sdk/repos.py`):

```python
# override_settings (~line 438)
async def override_settings(
    client: BBClient, workspace: str, repo_slug: str, *, body: Unset = UNSET
) -> RepositoryInheritanceState | Error | None:
    ...

# set_group_permission (~line 561)
async def set_group_permission(
    client: BBClient, workspace: str, repo_slug: str, group_slug: str, *, body: Unset = UNSET
) -> Any | Error | None:
    ...

# set_user_permission (~line 721)
async def set_user_permission(
    client: BBClient, workspace: str, repo_slug: str, selected_user_id: str, *, body: Unset = UNSET
) -> Any | Error | None:
    ...
```

**SDK wrapper after fix:**

```python
# override_settings
async def override_settings(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: RepositoryInheritanceState = RepositoryInheritanceState(),
) -> RepositoryInheritanceState | Error | None:
    ...

# set_group_permission
async def set_group_permission(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    group_slug: str,
    *,
    body: BitbucketAppsPermissionsSerializersRepoPermissionUpdateSchema,
) -> Any | Error | None:
    ...

# set_user_permission
async def set_user_permission(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    selected_user_id: str,
    *,
    body: BitbucketAppsPermissionsSerializersRepoPermissionUpdateSchema,
) -> Any | Error | None:
    ...
```

The fix also adds the necessary imports:

```python
from bb.cloud.models.bitbucket_apps_permissions_serializers_repo_permission_update_schema import (
    BitbucketAppsPermissionsSerializersRepoPermissionUpdateSchema,
)
from bb.cloud.models.repository_inheritance_state import RepositoryInheritanceState
```

---

## Design note — `override_settings` default

`override_settings` uses `RepositoryInheritanceState()` as its default (all fields `UNSET`) to maintain a callable interface without a required body, since the spec for this endpoint may be called to reset settings to workspace defaults with an empty/minimal payload. `set_group_permission` and `set_user_permission` use required bodies (no default) because the permission schema requires a specific role value.

---

## Impact

- `repos.override_settings()` raised `AttributeError` on every call — repository inheritance settings were entirely unmodifiable via the SDK
- `repos.set_group_permission()` and `repos.set_user_permission()` raised `AttributeError` on every call — repository group/user permission management was entirely non-functional (BUG-REPOS-001)

---

## Fix Applied

Updated all three function signatures in `src/bb/cloud/sdk/repos.py` with correct body types. Added required imports. `override_settings` uses `RepositoryInheritanceState()` as default; the two permission setters use required (no-default) `BitbucketAppsPermissionsSerializersRepoPermissionUpdateSchema` parameters.

---

## Status

- [x] Confirmed via static analysis (signature mismatch is unambiguous)
- [x] Fixed in `src/bb/cloud/sdk/repos.py`
- [x] Resolves BUG-REPOS-001 (`set_group_permission` / `set_user_permission`)
