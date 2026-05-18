# BUG-REPOS-001: `set_group_permission` and `set_user_permission` declare `body: Unset = UNSET` but generated API requires typed schema

**Status:** CONFIRMED (static analysis + spec inspection)
**Layer:** sdk-wrapper
**Module:** `bb.cloud.sdk.repos`
**Functions:** `set_group_permission`, `set_user_permission`
**Severity:** High (callers cannot pass a permission body via the type system; UNSET sent to API will crash)

## Exact Mismatch

| SDK function | SDK wrapper declaration | Generated API `_get_kwargs` expects |
|---|---|---|
| `set_group_permission` (line 564) | `body: Unset = UNSET` | `body: BitbucketAppsPermissionsSerializersRepoPermissionUpdateSchema` (required, no default) |
| `set_user_permission` (line 724) | `body: Unset = UNSET` | `body: BitbucketAppsPermissionsSerializersRepoPermissionUpdateSchema` (required, no default) |

Generated modules:
- `src/bb/cloud/api/repositories/put_repositories_workspace_repo_slug_permissions_config_groups_group_slug.py` — line 27: `body: BitbucketAppsPermissionsSerializersRepoPermissionUpdateSchema`
- `src/bb/cloud/api/repositories/put_repositories_workspace_repo_slug_permissions_config_users_selected_user_id.py` — line 28: `body: BitbucketAppsPermissionsSerializersRepoPermissionUpdateSchema`

Spec paths:
- `PUT /repositories/{workspace}/{repo_slug}/permissions-config/groups/{group_slug}`
- `PUT /repositories/{workspace}/{repo_slug}/permissions-config/users/{selected_user_id}`

## Spec Inspection

```json
// requestBody for both group and user permission PUT:
{
  "$ref": "#/components/requestBodies/bitbucket.apps.permissions.serializers.RepoPermissionUpdateSchema"
}

// Resolved schema:
{
  "type": "object",
  "properties": {
    "permission": {
      "type": "string",
      "enum": ["read", "write", "admin"]
    }
  },
  "required": ["permission"],
  "additionalProperties": false
}
```

The request body is marked `"required": true` in the requestBody definition. A bare `UNSET` cannot satisfy this — the generated `_get_kwargs` calls `body.to_dict()` unconditionally, which will raise `AttributeError: 'Unset' object has no attribute 'to_dict'` at runtime.

## Model

The generated model is `BitbucketAppsPermissionsSerializersRepoPermissionUpdateSchema` with a single required field:

```python
@_attrs_define
class BitbucketAppsPermissionsSerializersRepoPermissionUpdateSchema:
    permission: BitbucketAppsPermissionsSerializersRepoPermissionUpdateSchemaPermission
    # enum values: ADMIN = "admin", READ = "read", WRITE = "write"
```

## Impact

1. **Runtime crash** — `UNSET.to_dict()` → `AttributeError` on every call where no body is provided
2. **Type checker accepts invalid calls** — callers who pass a `BitbucketAppsPermissionsSerializersRepoPermissionUpdateSchema` get a type error (Unset ≠ that type)
3. **Impossible to use** — these are write endpoints; the body IS the permission level. There is no valid use case that sends UNSET.

## Fix

### Option 1 (SDK wrapper fix — immediate)

In `src/bb/cloud/sdk/repos.py`:

```python
# Add to imports at top of file:
from ..models.bitbucket_apps_permissions_serializers_repo_permission_update_schema import (
    BitbucketAppsPermissionsSerializersRepoPermissionUpdateSchema,
)

# set_group_permission — change line 564:
# BEFORE:
async def set_group_permission(
    client: BBClient, workspace: str, repo_slug: str, group_slug: str, *, body: Unset = UNSET
) -> Any | None:

# AFTER:
async def set_group_permission(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    group_slug: str,
    *,
    body: BitbucketAppsPermissionsSerializersRepoPermissionUpdateSchema,
) -> Any | None:

# set_user_permission — change line 724:
# BEFORE:
async def set_user_permission(
    client: BBClient, workspace: str, repo_slug: str, selected_user_id: str, *, body: Unset = UNSET
) -> Any | None:

# AFTER:
async def set_user_permission(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    selected_user_id: str,
    *,
    body: BitbucketAppsPermissionsSerializersRepoPermissionUpdateSchema,
) -> Any | None:
```

Note: `body` should NOT have a default (`= UNSET`) since the spec marks the request body required. The generated module's `_get_kwargs` calls `body.to_dict()` without a guard — passing `UNSET` will raise `AttributeError`.

### Also update the return type annotation

Both functions return `Any | None` but the generated module returns `Error | RepositoryGroupPermission` (or `RepositoryUserPermission`). Update accordingly:

```python
# set_group_permission:
) -> RepositoryGroupPermission | Error | None:

# set_user_permission:
) -> RepositoryUserPermission | Error | None:
```

## Status

- [x] Confirmed via static analysis (signature mismatch is unambiguous — generated `_get_kwargs` calls `body.to_dict()` unconditionally)
- [x] Confirmed via spec inspection (requestBody required: true, schema: permission enum)
- [ ] Confirmed via live test run
