# BUG-WORKSPACES-001: `get_repo_permission` returns paginated envelope object instead of list of permission items

**Status:** FIXED
**Root cause:** sdk-wrapper — used `asyncio()` returning the raw paginated response model instead of `async_paginate()` to extract the `values[]` items
**Layer:** sdk-wrapper

---

## Affected functions
- `bb.cloud.sdk.workspaces.get_repo_permission`

---

## Description

`workspaces.get_repo_permission` was implemented as a single-object fetch using `asyncio()`. The underlying endpoint `GET /workspaces/{workspace}/permissions/repositories/{repo_slug}` returns a **paginated list** of repository permission objects — the same paginated structure as the related `repo_permissions()` endpoint. The original implementation returned whatever `asyncio()` resolved: the raw `PaginatedRepositoryPermissions` envelope object rather than the list of items within its `values[]` field.

Callers expecting a list of permission objects would instead receive the envelope model (or `None` if the response was unmapped), causing `TypeError` when iterating or silent type corruption.

---

## Evidence

**SDK wrapper before fix** (`src/bb/cloud/sdk/workspaces.py`, ~line 303):

```python
async def get_repo_permission(client: BBClient, workspace: str, repo_slug: str) -> Any | Error | None:
    """Fetch the permission configuration for a specific repository within a workspace.

    Returns:
        The repository permission object, or ``None`` if not found.
    """
    return await get_workspaces_workspace_permissions_repositories_repo_slug.asyncio(
        workspace, repo_slug, client=client.auth
    )
```

**SDK wrapper after fix:**

```python
async def get_repo_permission(
    client: BBClient, workspace: str, repo_slug: str, *, pagelen: int = 25
) -> list[Any] | Error:
    """List all user permissions for a specific repository within a workspace.

    Args:
        pagelen: Number of results per page. Defaults to 25.

    Returns:
        List of repository permission objects, or ``Error`` on failure.
    """
    result = await async_paginate(
        get_workspaces_workspace_permissions_repositories_repo_slug.asyncio,
        workspace,
        repo_slug,
        client=client.auth,
        pagelen=pagelen,
    )
    if isinstance(result, Error):
        return result
    return [x for x in result]
```

---

## Root Cause

The endpoint returns a paginated list (same structure as `repo_permissions()` and other workspace list endpoints). The original implementation incorrectly treated it as a single-object endpoint and used `asyncio()` directly, which returns the raw parsed response (the `PaginatedRepositoryPermissions` envelope). The fix uses the project's existing `async_paginate()` helper, which iterates through all pages and collects the `values[]` items.

A `pagelen` parameter is added for consistency with other SDK pagination functions (`repo_permissions`, `member_permissions`, etc.).

---

## Impact

- `workspaces.get_repo_permission()` returned a `PaginatedRepositoryPermissions` object instead of `list[RepositoryPermission]`
- Return type annotation `Any | Error | None` was misleading — the actual return was the envelope model
- Callers who iterated the result would get the model's fields, not the individual permission records
- The docstring "returns the repository permission object" was wrong — this endpoint returns all user permissions for a repo, not a single permission

---

## Fix Applied

Replaced `asyncio()` direct call with `async_paginate()` in `src/bb/cloud/sdk/workspaces.py`. Updated return type to `list[Any] | Error`, added `pagelen` parameter, updated docstring.

---

## Status

- [x] Confirmed via static analysis (endpoint returns paginated list; `asyncio()` returns envelope)
- [x] Fixed in `src/bb/cloud/sdk/workspaces.py`
