# Test Plan: projects · workspaces · users · search

Modules under test:
- `src/bb/cloud/sdk/projects.py` (15 functions)
- `src/bb/cloud/sdk/workspaces.py` (12 functions)
- `src/bb/cloud/sdk/users.py` (13 functions)
- `src/bb/cloud/sdk/search.py` (3 functions)

Workspace: **beaverish** (UUID `{8606bca9-e0ce-40b5-9b2b-a359e6ddb8b5}`)
Project key: **PROJ** (name: BB, UUID `{639f8e8a-097d-4aff-90b1-2b2d1ddfd7a8}`)
Probe repo: **bb-probe**
Owner account_id: `712020:f464b5ca-adb8-4a1e-80d4-c867bbf50805`
User UUID: `{e8e13d7c-8af1-409a-9a9e-e2bf80ade040}`
User display_name: `Laraib`
SSH key UUID: `{ed7d598c-4e45-4328-a461-554d7c0e5369}`
GPG fingerprint (partial): `7e7cd216a8df00cb`
Workspace member count: 3

---

## projects.list

- [x] **PROJ-LIST-001** Returns `list[Project]` for beaverish workspace
- [x] **PROJ-LIST-002** All items are `Project` instances (no raw dicts)
- [x] **PROJ-LIST-003** Project with key=`PROJ` and name=`BB` is present in the list
- [x] **PROJ-LIST-004** Each project has a non-empty `key` attribute
- [x] **PROJ-LIST-005** Pagination integrity: `pagelen=1` vs `pagelen=25` produce same set of keys

Expected status codes: 200 (paginated).

---

## projects.get

- [x] **PROJ-GET-001** Returns `Project` for key `PROJ`
- [x] **PROJ-GET-002** Returned project has `key="PROJ"` and `name="BB"`
- [x] **PROJ-GET-003** Non-existent key `ZZZNOPE` returns `Error | None`, never `Project`

Expected status codes: 200, 404.

---

## projects.create + update + delete (lifecycle)

- [x] **PROJ-CRE-001** Create throwaway project with `throwaway_project_key` — returns `Project`
- [x] **PROJ-CRE-002** Created project key matches `throwaway_project_key`
- [x] **PROJ-CRE-003** `projects.get` immediately returns the created project
- [x] **PROJ-UPD-001** Update throwaway project description — returns `Project` with new description
- [x] **PROJ-UPD-002** Partial update does not wipe `key` or `name`
- [x] **PROJ-DEL-001** `projects.delete` returns `None`
- [x] **PROJ-DEL-002** After delete, `projects.get` returns `Error | None`, not `Project`
- [x] **CLEANUP** Throwaway project always cleaned up in `finally` block

Note: Bitbucket's POST /workspaces/{ws}/projects rejects the `type` field in
the body ('extra keys not allowed'). Wrap the `Project` body in a shim that
strips `type` from `to_dict()`. This is a known upstream quirk, not an SDK bug.

Expected status codes: 200/201 (create), 200 (update), 204 (delete).

---

## projects.default_reviewers

- [x] **PROJ-DR-001** Returns `list` (likely empty in a single-user workspace)
- [x] **PROJ-DR-002** Empty list is valid — not an error

Expected status codes: 200.

---

## projects.get_default_reviewer / add_default_reviewer / remove_default_reviewer

- [x] **PROJ-DR-003** `add_default_reviewer` with owner's own UUID expects 400 (cannot review own PRs) or `UnexpectedStatus`; test documents but does not fail on that error
- [x] **PROJ-DR-004** `get_default_reviewer` for non-existent user returns `Error | None`, not an exception
- [x] **PROJ-DR-005** `remove_default_reviewer` for non-existent user returns `None` or raises `UnexpectedStatus` — test is tolerant

Expected status codes: 200 (get), 204 (add/remove), 400 (cannot self-review).

---

## projects.group_permissions

- [x] **PROJ-GP-001** Returns `list` for PROJ (likely empty — no groups on Free plan)
- [x] **PROJ-GP-002** Empty list is valid; `Error` triggers skip (403 on some auth methods)

Expected status codes: 200, 403 (Free plan or insufficient scope).

---

## projects.update_group_permission

- [x] **PROJ-GP-003** Calling with a non-existent group slug returns `Error | None` or raises `UnexpectedStatus` — test is tolerant

Expected status codes: 200, 404, 403.

---

## projects.delete_group_permission

- [x] **PROJ-GP-004** Calling with a non-existent group slug returns `None` or raises `UnexpectedStatus` — test is tolerant (skipped if risky)

---

## projects.user_permissions

- [x] **PROJ-UP-001** Returns `list` for PROJ
- [x] **PROJ-UP-002** Owner account_id `712020:f464b5ca-...` appears in the list (or list is empty/skip on 403)

Expected status codes: 200, 403.

---

## projects.update_user_permission

- [x] **PROJ-UP-003** Attempt to change own permission on throwaway project; document result
- [x] **PROJ-UP-004** Skip if 403 (not admin, or Free plan restriction)

Expected status codes: 200, 400, 403.

---

## projects.delete_user_permission

- [x] **PROJ-UP-005** Skip — would lock the only admin out of the project

---

---

## workspaces.list / workspaces.mine

- [x] **WS-LIST-001** `workspaces.list` returns `list[Workspace]`
- [x] **WS-LIST-002** All items are `Workspace` instances
- [x] **WS-LIST-003** `beaverish` slug or UUID appears in the list (skip if empty — API token limitation)
- [x] **WS-MINE-001** `workspaces.mine` returns `list[Workspace]`
- [x] **WS-MINE-002** `beaverish` appears in mine (skip if empty)

Expected status codes: 200 (paginated).

---

## workspaces.get

- [x] **WS-GET-001** Returns `Workspace` for `beaverish`
- [x] **WS-GET-002** `workspace.slug == "beaverish"` or UUID matches
- [x] **WS-GET-003** Non-existent slug returns `Error | None`, not `Workspace`
- [x] **WS-GET-004** UUID lookup `{8606bca9-e0ce-40b5-9b2b-a359e6ddb8b5}` returns same workspace

Expected status codes: 200, 404.

---

## workspaces.members

- [x] **WS-MEM-001** Returns `list` with at least 1 member
- [x] **WS-MEM-002** Member count equals 3 (the seeded count)
- [x] **WS-MEM-003** Each member has an `account_id` or `uuid` attribute

Expected status codes: 200. Possibly 403 (scope).

---

## workspaces.get_member

- [x] **WS-MEM-004** Fetching owner by UUID returns member object
- [x] **WS-MEM-005** Returned object has non-empty identifier
- [x] **WS-MEM-006** Fetching non-existent member returns `None` or `Error`

Expected status codes: 200, 404.

---

## workspaces.permissions

- [x] **WS-PERM-001** Returns `list` with at least 1 entry
- [x] **WS-PERM-002** Owner entry has permission `owner` or `admin`
- [x] **WS-PERM-003** Error triggers skip, not fail (403 on some scopes)

Expected status codes: 200, 403.

---

## workspaces.repo_permissions

- [x] **WS-RPERM-001** Returns `list` (at least 1 entry for `bb-probe`)
- [x] **WS-RPERM-002** Each entry has a `permission` attribute
- [x] **WS-RPERM-003** 403 triggers skip

Expected status codes: 200, 403.

---

## workspaces.get_repo_permission

- [x] **WS-RPERM-004** Returns permission object for `bb-probe`
- [x] **WS-RPERM-005** Returned object has `permission` attribute
- [x] **WS-RPERM-006** Non-existent repo slug returns `None` or `Error`

Expected status codes: 200, 404.

---

## workspaces.user_prs

- [x] **WS-PR-001** Returns `list` (may be empty — no open PRs seeded in probe repo)
- [x] **WS-PR-002** Each PR has an `id` attribute
- [x] **WS-PR-003** 403/404 triggers skip

Expected status codes: 200, 403, 404.

---

## workspaces.gpg_key

- [x] **WS-GPG-001** Returns `None`, `Error`, or a GPG key object — all are valid (endpoint may not have a configured key)
- [x] **WS-GPG-002** `UnexpectedStatus` is tolerated (endpoint may return undocumented 404)

Expected status codes: 200, 404.

---

## workspaces.my_permissions

- [x] **WS-MPERM-001** Returns `list` with at least 1 entry
- [x] **WS-MPERM-002** Each entry has a `permission` and a `workspace` attribute

Expected status codes: 200 (paginated).

---

## workspaces.my_permission

- [x] **WS-MPERM-003** Returns permission object for `beaverish`
- [x] **WS-MPERM-004** Returned object has `permission` attribute

Expected status codes: 200, 404.

---

---

## users.me

- [x] **USR-ME-001** Returns `Account` (not `Error`, not `None`)
- [x] **USR-ME-002** `display_name` contains `"Laraib"`
- [x] **USR-ME-003** `uuid` equals `{e8e13d7c-8af1-409a-9a9e-e2bf80ade040}` (or similar check)
- [x] **USR-ME-004** `account_id` attribute is set OR `uuid` is set

Expected status codes: 200.

---

## users.get

- [x] **USR-GET-001** `users.get(client, "{e8e13d7c-...}")` returns same account as `users.me`
- [x] **USR-GET-002** UUIDs match between me() and get()
- [x] **USR-GET-003** Invalid UUID `{00000000-...-000}` returns `Error | None`, not `Account`

Expected status codes: 200, 404.

---

## users.emails

- [x] **USR-EMAIL-001** Returns `list` with at least 1 email object
- [x] **USR-EMAIL-002** Email `laraib.ali@soco-engineers.com` is present
- [x] **USR-EMAIL-003** 403/scope error triggers skip

Expected status codes: 200, 403. Note: this endpoint sometimes returns non-standard error payloads — catch `KeyError` and skip.

---

## users.get_email

- [x] **USR-EMAIL-004** `users.get_email(client, "laraib.ali@soco-engineers.com")` returns an object
- [x] **USR-EMAIL-005** Returned object is not `None` and not `Error`
- [x] **USR-EMAIL-006** Non-existent email returns `None` or `Error`

Expected status codes: 200, 404, 403.

---

## users.ssh_keys / get_ssh_key (read-only)

- [x] **USR-SSH-001** `users.ssh_keys` returns `list[SshAccountKey]`
- [x] **USR-SSH-002** SSH key with UUID `{ed7d598c-...}` is in the list
- [x] **USR-SSH-003** Each key has a non-empty `key` or `uuid` attribute
- [x] **USR-SSH-004** `users.get_ssh_key` by numeric `id` returns `SshAccountKey`
- [x] **USR-SSH-005** Returned key UUID matches the known key

Expected status codes: 200.

---

## users.add_ssh_key / update_ssh_key / delete_ssh_key (lifecycle)

- [x] **USR-SSH-006** `add_ssh_key` with a test RSA public key returns `SshAccountKey`
- [x] **USR-SSH-007** Created key has expected `label`
- [x] **USR-SSH-008** `update_ssh_key` changes the label, returns updated `SshAccountKey`
- [x] **USR-SSH-009** `delete_ssh_key` returns `None`
- [x] **USR-SSH-010** After delete, `get_ssh_key` returns `None` or `Error`
- [x] **CLEANUP** Always delete throwaway SSH key in `finally` block

Note: Test RSA public key:
`ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAQQDFGt5XQxBa6kRiSjbQBlkxmMWLrFkKDt7PZMH2BnKLuJ8BHfVw2pHH3NRDvFh2K5K0V9mFqYk7c8iDLbTtHN3 test-user@bb-sdk-test`

Expected status codes: 201 (create), 200 (update/read), 204 (delete).

---

## users.gpg_keys / get_gpg_key

- [x] **USR-GPG-001** `users.gpg_keys` returns `list[GPGAccountKey]`
- [x] **USR-GPG-002** GPG key with partial fingerprint `7e7cd216a8df00cb` is present
- [x] **USR-GPG-003** `users.get_gpg_key` by full fingerprint returns `GPGAccountKey`
- [x] **USR-GPG-004** Returned GPG key has non-empty `fingerprint` attribute

Expected status codes: 200.

---

## users.add_gpg_key

- [x] **USR-GPG-005** Skip — GPG key format is complex (armored PGP block required) and the existing key covers the happy path; see future test TODOs

---

## users.delete_gpg_key

- [x] **USR-GPG-006** Skip — would delete the only GPG key and break workspace signing

---

---

## search.code

- [x] **SRCH-CODE-001** Returns `list[SearchCodeSearchResult]` for query `"def"`
- [x] **SRCH-CODE-002** At least 1 result returned (workspace has Python files in bb-probe)
- [x] **SRCH-CODE-003** Each result is `SearchCodeSearchResult` instance
- [x] **SRCH-CODE-004** Each result has a `file` attribute (not `None`) with a `path`
- [x] **SRCH-CODE-005** `content_match_count` is a positive int on each result
- [x] **SRCH-CODE-006** 403/empty result triggers skip (not fail)

Expected status codes: 200 (paginated).

---

## search.account (deprecated)

- [x] **SRCH-ACCT-001** Returns `list` or `Error` — 400/404 acceptable (deprecated endpoint)
- [x] **SRCH-ACCT-002** Does not raise an exception

---

## search.team (deprecated)

- [x] **SRCH-TEAM-001** Returns `list` or `Error` — 400/404 acceptable (deprecated endpoint)
- [x] **SRCH-TEAM-002** Does not raise an exception

---

## Edge Cases

| Scenario | Expected |
|---|---|
| `projects.get` with invalid key `ZZZNOPE` | `Error` or `None`, not `Project` |
| `workspaces.get` with bogus slug | `Error` or `None`, not `Workspace` |
| `users.get` with all-zero UUID | `Error` or `None`, not `Account` |
| `search.code` with very long query | No exception; returns `list` or `Error` |
| `projects.user_permissions` with PROJ when single-user | `list` (owner only) or `Error` (403) |
| `workspaces.gpg_key` when no key configured | `None` or `Error` — not exception |

---

## Undocumented Status Codes to Watch

| Endpoint | Likely Undocumented | Reason |
|---|---|---|
| POST /workspaces/{ws}/projects | 201 Created | API may return 201, spec documents 200 |
| GET /workspaces/{ws}/projects/{key}/permissions-config/groups | 403 | Free plan restriction |
| GET /workspaces/{ws}/projects/{key}/permissions-config/users | 403 | Free plan restriction |
| PUT /workspaces/{ws}/projects/{key}/default-reviewers/{user} | 400 | Cannot add self as reviewer |
| GET /workspaces/{ws}/settings/gpg-public-key | 404 | Not configured |
| GET /user/emails/{email} | 403 | Scope restriction |
