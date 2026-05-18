# Test Plan: `bb.cloud.sdk.repos`

Module: `src/bb/cloud/sdk/repos.py`
Probe repo: `beaverish/bb-probe`
Group slug: `0804948d-0ec2-4630-bc87-d3ef37cdb221`
Owner account_id: `712020:f464b5ca-adb8-4a1e-80d4-c867bbf50805`
User UUID: `{e8e13d7c-8af1-409a-9a9e-e2bf80ade040}`

---

## `repos.list`

- [ ] **HAPPY-001** Happy path: returns `list[Repository]` for a valid workspace
- [ ] **HAPPY-002** All items are `Repository` instances (no raw dicts)
- [ ] **HAPPY-003** Each `Repository.full_name` starts with `{workspace}/`
- [ ] **PAGINATION-001** `pagelen=1` vs `pagelen=50` gives the same total count
- [ ] **PAGINATION-002** `pagelen=1` vs `pagelen=50` gives the same set of full_names (no dups/drops)
- [ ] **FILTER-001** `q="scm=\"git\""` filters to only git repos
- [ ] **ERROR-001** Invalid workspace slug returns `Error` (not an exception)

Expected status codes: 200 (paginated). Possibly 404 for unknown workspace.

---

## `repos.get`

- [ ] **HAPPY-004** Returns `Repository` with correct `full_name` for `bb-probe`
- [ ] **HAPPY-005** `repo.full_name` contains the slug
- [ ] **HAPPY-006** `repo.scm` is set (not None)
- [ ] **HAPPY-007** `repo.is_private` is a bool
- [ ] **ERROR-002** Non-existent slug returns `Error | None`, never a `Repository`
- [ ] **ERROR-003** Wrong workspace returns `Error | None`

Expected status codes: 200, 404.

---

## `repos.create`

- [ ] **WRITES-001** Creates a private git repo in project `PROJ`, receives `Repository` back
- [ ] **WRITES-002** Created repo is immediately (or within ~10 s) visible via `repos.get`
- [ ] **WRITES-003** Created repo's `full_name` contains the throwaway slug
- [ ] **WRITES-004** Created repo is `is_private=True`
- [ ] **STATUS-001** Check whether API returns 200 or 201 — the spec may only document 200 but the API returns 201 (potential bug)
- [ ] **ERROR-004** Creating a repo with a duplicate slug returns `Error` (not an exception)
- [ ] **CLEANUP** Always deletes the throwaway repo in a `finally` block

Expected status codes: 200 or 201 (spec may only document 200). Possibly 400 (validation error).

---

## `repos.update`

- [ ] **WRITES-005** Updates the throwaway repo description, `repos.get` reflects the new description
- [ ] **WRITES-006** Partial update (description only) does not wipe other fields
- [ ] **ERROR-005** Update on non-existent repo returns `Error` or raises `UnexpectedStatus`
- [ ] **CLEANUP** Always deletes throwaway repo in a `finally` block (create first, update, delete)

Expected status codes: 200.

---

## `repos.delete`

- [ ] **WRITES-007** Deletes the throwaway repo; subsequent `repos.get` returns `Error|None`
- [ ] **WRITES-008** `delete` returns `None` (no return value)
- [ ] **ERROR-006** Deleting a non-existent repo does not crash (or returns `UnexpectedStatus` 404)
- [ ] **CLEANUP** Throwaway repo always cleaned up (create, delete, verify gone)

Expected status codes: 204. Possibly 404 for missing repos.

---

## `repos.fork`

- [ ] **WRITES-009** Fork `bb-probe` to a throwaway name in the same workspace — verify `Repository` returned or document plan restriction
- [ ] **WRITES-010** Forked repo `parent` field points to original
- [ ] **PLAN-001** If plan restriction applies, verify `Error` is returned (not an exception), or document 403
- [ ] **CLEANUP** Delete forked repo in a `finally` block if fork succeeds

Expected status codes: 200 or 201. Possibly 403 (Free plan restriction).

---

## `repos.forks`

- [ ] **HAPPY-008** Returns `list[Repository]` (possibly empty) for `bb-probe`
- [ ] **HAPPY-009** If forks exist, each item is a `Repository` instance
- [ ] **HAPPY-010** Empty list is valid (no forks yet)
- [ ] **PAGINATION-003** Pagination integrity: `pagelen=1` vs `pagelen=50` gives same fork count

Expected status codes: 200.

---

## `repos.watchers`

- [ ] **HAPPY-011** Returns `list` (possibly empty) for `bb-probe`
- [ ] **HAPPY-012** List contains at least the owner (account_id `712020:f464b5ca-...`)
- [ ] **HAPPY-013** Each watcher has an `account_id` or `uuid` attribute

Expected status codes: 200.

---

## `repos.override_settings`

- [ ] **HAPPY-014** Returns `RepositoryInheritanceState` (or `None`) for `bb-probe`
- [ ] **HAPPY-015** Returned object has `type_` attribute
- [ ] **ERROR-007** Non-existent repo returns `Error` or `None`, not an exception

Expected status codes: 200, 404.

---

## `repos.update_override_settings`

- [ ] **WRITES-011** PUT to `bb-probe` returns `None` (204 no-content) or an object (200)
- [ ] **WRITES-012** Does not corrupt the existing settings (re-read and verify)
- [ ] **ERROR-008** 403 if not authorized — verify `Error` or `None` returned (not `UnexpectedStatus`)

Expected status codes: 204 (no-content, cast as `None`). Possibly 403, 404.

---

## `repos.group_permissions`

- [ ] **HAPPY-016** Returns `list` for `bb-probe`
- [ ] **HAPPY-017** The known group slug `0804948d-...` appears in the results
- [ ] **PLAN-002** If plan restriction, returns `Error` (not exception) — verify 403 is handled
- [ ] **PAGINATION-004** Pagination integrity across page sizes

Expected status codes: 200. Possibly 403 (Free plan).

---

## `repos.get_group_permission`

- [ ] **HAPPY-018** Returns group permission object for `0804948d-...` on `bb-probe`
- [ ] **HAPPY-019** Returned object has a `permission` attribute (e.g., "read")
- [ ] **HAPPY-020** Returned object has a `group` attribute
- [ ] **ERROR-009** Unknown group slug returns `None` (not an exception)
- [ ] **PLAN-003** 403 on Free plan — verify handled gracefully

Expected status codes: 200. Possibly 403, 404.

---

## `repos.set_group_permission`

- [ ] **WRITES-013** Set group permission to `write` on `bb-probe`, verify change, revert to `read`
- [ ] **PLAN-004** If 403 returned, verify it is `Error | None`, not `UnexpectedStatus`
- [ ] **WRITES-014** After revert, permission is back to `read`

Expected status codes: 200. Possibly 403 (Free plan).

---

## `repos.delete_group_permission`

- [ ] **WRITES-015** Only run if `set_group_permission` succeeds — delete and restore via `set_group_permission`
- [ ] **PLAN-005** Skip or document if 403 on Free plan
- [ ] **CLEANUP** Always restore original permission in `finally` block

Expected status codes: 204. Possibly 403, 404.

---

## `repos.user_permissions`

- [ ] **HAPPY-021** Returns `list` for `bb-probe`
- [ ] **HAPPY-022** Owner account_id `712020:f464b5ca-...` appears in the list
- [ ] **PLAN-006** If 403 on Free plan, verify `Error` returned (not exception)
- [ ] **PAGINATION-005** Pagination integrity across page sizes

Expected status codes: 200. Possibly 403 (Free plan).

---

## `repos.get_user_permission`

- [ ] **HAPPY-023** Returns user permission object for owner `712020:f464b5ca-...` on `bb-probe`
- [ ] **HAPPY-024** Returned object has `permission` attribute (e.g., "admin")
- [ ] **HAPPY-025** Returned object has `user` attribute
- [ ] **ERROR-010** Unknown user UUID returns `None` (not exception)
- [ ] **PLAN-007** 403 on Free plan — verify handled

Expected status codes: 200. Possibly 403, 404.

---

## `repos.set_user_permission`

- [ ] **WRITES-016** Attempt to set admin's own permission — likely 400/403 (would lock ourselves out)
- [ ] **PLAN-008** Document result — skip if risky

Expected status codes: 200. Possibly 400, 403, 404.

---

## `repos.delete_user_permission`

- [ ] **SKIP-001** Skip — deleting admin's own permission would lock us out
- [ ] **NOTE** Document that this was intentionally skipped for safety

---

## `repos.my_permissions`

- [ ] **HAPPY-026** Returns `list` (non-empty for authenticated user)
- [ ] **HAPPY-027** `bb-probe` entry appears in the list
- [ ] **HAPPY-028** Each entry has `permission` and `repository` attributes
- [ ] **PAGINATION-006** `pagelen=1` vs `pagelen=50` gives same total count

Expected status codes: 200.

---

## `repos.workspace_user_permissions`

- [ ] **HAPPY-029** Returns `list` for the workspace
- [ ] **HAPPY-030** `bb-probe` permission entry is included
- [ ] **HAPPY-031** Each entry has `permission` attribute
- [ ] **PAGINATION-007** Pagination integrity across page sizes

Expected status codes: 200.

---

## Cross-Cutting / Undocumented Status Codes to Probe

| Endpoint | Likely Undocumented | Reason |
|---|---|---|
| `POST /repositories/{ws}/{slug}` | 201 Created | API returns 201, spec may only document 200 |
| `POST .../forks` | 201 Created | Same pattern |
| `GET .../permissions-config/groups` | 403 Forbidden | Free plan restriction |
| `GET .../permissions-config/users` | 403 Forbidden | Free plan restriction |
| `PUT .../permissions-config/groups/{slug}` | 403 Forbidden | Free plan |
| `DELETE .../permissions-config/groups/{slug}` | 403 Forbidden | Free plan |
| `GET /repositories/{ws}/{slug}` | 410 Gone | Deleted repos may return 410 |
