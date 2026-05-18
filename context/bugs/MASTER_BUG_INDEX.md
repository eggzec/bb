# Master Bug Index — Bitbucket Cloud SDK

Generated: 2026-05-15. Updated: 2026-05-16 (added BUG-SCHEMA-008 through BUG-SCHEMA-016; added BUG-PRS-002/003, BUG-SOURCE-001, BUG-SNIPPETS-002, BUG-ISSUES-001/002/003, BUG-DEPLOY-003; added BUG-PIPELINES-006, BUG-PRS-004). Updated 2026-05-16 pass 2: fixed BUG-COMMITS-001, BUG-DOWNLOADS-001, BUG-DEPLOY-001, BUG-WEBHOOKS-001, BUG-PRS-001, BUG-REPOS-001, BUG-ISSUES-002/003, BUG-PIPELINES-001/004/005; added BUG-AUTH-001, BUG-BRANCHING-001, BUG-ISSUES-004/005, BUG-PIPELINES-007/008, BUG-REPOS-002, BUG-WORKSPACES-001, BUG-PRS-005. Updated 2026-05-16 pass 3 (schemathesis run): added BUG-SCHEMA-017/018/019; fixed all three. Updated 2026-05-16 pass 4: fixed BUG-PIPELINES-002/003, BUG-DEPLOY-002; added BUG-SCHEMA-020/021/022; fixed all. Updated 2026-05-16 pass 5 (full spec diff): added BUG-PAGINATION-001, BUG-SCHEMA-023, BUG-SCHEMA-028/029/030/031, BUG-GENERATOR-001; all fixed. Updated 2026-05-16 pass 6 (P3 field gaps): fixed BUG-SCHEMA-001/002/003/004/005/006/007; all P3 bugs now FIXED. Updated 2026-05-17: closed all remaining PARTIAL/NEEDS-INVESTIGATION bugs — BUG-SNIPPETS-001 (unfixable at spec level; SDK fix needed), BUG-SCHEMA-033 (REFUTED: Code Insights accessible on Free plan), BUG-SCHEMA-034 (CLOSED: all deprecated endpoints return 403 not 410, no removals occurred). Updated 2026-05-18 pass 7: fixed BUG-SCHEMA-032 — injected 401 into all 240 non-public authenticated endpoints and 403 where missing; 0 endpoints now missing 401 (excl. /hook_events); total with 401 = 333. Updated 2026-05-18 pass 8: FIXED BUG-SNIPPETS-001 — SDK-level string-in-values guard added to snippets.list(); all bugs now FIXED.

All bugs are categorised by **layer**:
- **spec** — OpenAPI spec is wrong; fix with `jq` surgery + `make generate-cloud && make diff-cloud`
- **sdk-wrapper** — hand-written SDK wrapper calls generated code incorrectly; fix in `src/bb/cloud/sdk/`
- **generator** — `openapi-python-client` produced incorrect output (rare; usually spec is root cause)
- **test** — live test uses wrong fixture data or constructs a request body the API rejects

**Status key:** `CONFIRMED` | `FIXED` | `REFUTED` | `PARTIAL` | `NEEDS-INVESTIGATION`

---

## SDK Wrapper Bugs (crash / wrong-type at call site)

These will cause runtime `TypeError` or `AttributeError` before any HTTP call is made.

| ID | Module | Function(s) | Root Cause | Status | Fix |
|---|---|---|---|---|---|
| BUG-AUTH-001 | _auth | all 5 `get_authenticated_client()` methods | `AuthenticatedClient` constructed without `follow_redirects=True` → auth header silently dropped on redirects | FIXED | Added `follow_redirects=True` to all 5 constructors |
| BUG-PRS-001 | prs | `create_task`, `update_task` | `body: Unset = UNSET` declared, but generated code requires `PullRequestTaskCreate` / `PullRequestTaskUpdate` | FIXED | Changed signatures to `PullRequestTaskCreate` / `PullRequestTaskUpdate` (required) |
| BUG-PRS-002 | prs | `diff`, `patch`, `diffstat`, `merge_task_status` | Called `.asyncio()` which does not exist — generator only emits `asyncio_detailed()` for binary/redirect/unmapped-JSON endpoints | FIXED | Use `asyncio_detailed()`; decode `response.content` for text; `json.loads` for diffstat; `response.parsed` for merge status |
| BUG-PRS-003 | prs | `add_comment` | `body: PullRequestComment \| Unset = UNSET` — generated `_get_kwargs` calls `body.to_dict()` unconditionally → `AttributeError` on default | FIXED | Made `body: PullRequestComment` required (no default) — see also BUG-PRS-005 for the 201 issue |
| BUG-PRS-005 | prs | `add_comment` | `asyncio()` maps only 200; live API returns 201 Created → always returns `None` on success | FIXED | Switch to `asyncio_detailed()`; handle 200 and 201 explicitly |
| BUG-REPOS-001 | repos | `set_group_permission`, `set_user_permission` | `body: Unset = UNSET` declared, generated code calls `body.to_dict()` unconditionally → `AttributeError` | FIXED | Changed to required `BitbucketAppsPermissionsSerializersRepoPermissionUpdateSchema` — see BUG-REPOS-002 |
| BUG-REPOS-002 | repos | `override_settings` | `body: Unset = UNSET` → `AttributeError`; also resolves BUG-REPOS-001 | FIXED | Changed to `RepositoryInheritanceState = RepositoryInheritanceState()` |
| BUG-SOURCE-001 | source | `get` | Used `asyncio()` which returns `None` for `text/plain` 200 — generator maps only JSON 200 to a model | FIXED | Use `asyncio_detailed()`; inspect `content-type`; decode `response.content` for non-JSON |
| BUG-SNIPPETS-002 | snippets | `create`, `create_default`, `update`, `add_comment`, `update_comment`, `update_node` | `body: Model \| Unset = UNSET` — generated `_get_kwargs` calls `body.to_dict()` unconditionally → `AttributeError` | FIXED | Changed all to `body: Model = Model()` |
| BUG-ISSUES-001 | issues | `add_change` | Default `IssueChange()` raises `TypeError` at import — `IssueChange.type_: str` is required with no default | FIXED | Changed to `IssueChange(type_="issue_change")` |
| BUG-ISSUES-002 | issues | `create` | `body: Issue \| Unset = UNSET` — generated `_get_kwargs` calls `body.to_dict()` unconditionally → `AttributeError` | FIXED | Changed to `body: Issue = Issue()` |
| BUG-ISSUES-003 | issues | `update` | `body: Issue \| Unset = UNSET` → `AttributeError` | FIXED | Changed to `body: Issue = Issue()` |
| BUG-ISSUES-004 | issues | `add_comment`, `update_comment` | `body: IssueComment \| Unset = UNSET` → `AttributeError` | FIXED | Changed to `body: IssueComment = IssueComment()` |
| BUG-ISSUES-005 | issues | `upload_attachment`, `import_data` | Erroneous `body: Unset = UNSET` forwarded to generated API that has no body param → `TypeError` | FIXED | Removed `body` param and `body=body` from both call sites |
| BUG-PIPELINES-001 | pipelines | `create_schedule` | `body: PipelineSchedule \| Unset = UNSET`, generated requires `PipelineSchedulePostRequestBody` | FIXED | Changed signature to `body: PipelineSchedulePostRequestBody` |
| BUG-PIPELINES-002 | pipelines | `update_config` | `body: Unset = UNSET`, generated requires `PipelinesConfig` | FIXED | Changed to `body: PipelinesConfig` (required); added import |
| BUG-PIPELINES-003 | pipelines | `update_build_number`, `create_runner`, `update_runner`, `create_workspace_runner`, `update_workspace_runner` | `update_build_number`: `body: Unset = UNSET` → requires `PipelineBuildNumber`; 4 runner functions forward phantom `body=body` to no-body generated APIs → `TypeError` | FIXED | Changed `update_build_number` to `body: PipelineBuildNumber`; removed `body` param + `body=body` from all 4 runner functions |
| BUG-PIPELINES-004 | pipelines | `oidc_config`, `oidc_keys` | Passed `workspace, repo_slug` but OIDC endpoints are workspace-level only (no `repo_slug` in path) → `TypeError` extra arg | FIXED | Removed `repo_slug` from signatures and call sites |
| BUG-PIPELINES-005 | pipelines | `test_reports` | Missing `step_uuid` arg — generated function requires it | FIXED | Added `step_uuid: str` parameter to wrapper and call site |
| BUG-PIPELINES-007 | pipelines | `step_log` | `asyncio()` returns `None` for `text/plain` responses — generator emits no typed variant for non-JSON content | FIXED | Switch to `asyncio_detailed()`; decode `response.content` for 200 |
| BUG-PIPELINES-008 | pipelines | `create_known_host` | `asyncio()` maps only 200; live API returns 201 Created → always returns `None` on success | FIXED | Switch to `asyncio_detailed()`; handle 200 and 201 explicitly |
| BUG-BRANCHING-001 | branching_model | `update_settings`, `update_project_settings` | `body: BranchingModelSettings \| Unset = UNSET` → `AttributeError`; spec also missing `requestBody` | FIXED | Made body required; added `requestBody` to spec for both PUT endpoints |
| BUG-WORKSPACES-001 | workspaces | `get_repo_permission` | Used `asyncio()` returning paginated envelope instead of `async_paginate()` to extract items | FIXED | Replaced with `async_paginate()`; added `pagelen` param; updated return type to `list[Any] \| Error` |
| BUG-DEPLOY-003 | deployments | `update_env` | Passed `body=body` to `update_environment_for_repository.asyncio()` which has no `body` param (spec missing requestBody per BUG-DEPLOY-002) → `TypeError` | FIXED | Removed `body=body` from call; restore after BUG-DEPLOY-002 spec fix + regen |

---

## Spec Bugs — Missing/Wrong Status Codes

These cause the generated `_parse_response` to return `None` (or raise `UnexpectedStatus`) for valid HTTP responses.

| ID | Module | Endpoint(s) | Spec says | Live API returns | Impact | Status |
|---|---|---|---|---|---|---|
| BUG-COMMITS-001 | commit_statuses | `POST .../statuses/build` | `201` only | `200` (upsert of existing key) | `create()` returns `None` on upsert | FIXED — added 200 response to spec |
| BUG-DOWNLOADS-001 | downloads | `GET/POST/DELETE .../downloads` | `200`, `403` | `402` (Free plan) | `list()` returns `[]`; others return `None` — plan restriction silently swallowed | FIXED — added 402 response to all 4 download endpoints |
| BUG-SNIPPETS-001 | snippets | `GET .../snippets/{workspace}` | `200` with `values[]` of snippet objects | `200` with `values[]` of **error strings** (Free plan) | Returns `["error message"]` — silent type corruption | FIXED — SDK wrapper `list()` now detects `str` in `values[0]` and returns `Error.from_dict(...)` instead of corrupt data |

**Refuted (spec is correct):**
- BUG-COMMITS-002: `reports.create_or_update` — PUT always returns 200, never 201. No fix needed.
- BUG-COMMITS-003: `reports.create_annotation` — PUT always returns 200. No fix needed. (BUT see BUG-SCHEMA-002.)

---

## Spec Bugs — Missing requestBody

These cause `_get_kwargs` to send empty/null bodies, making the write operation fail with 400.

| ID | Module | Endpoint(s) | Problem | Status | Fix |
|---|---|---|---|---|---|
| BUG-DEPLOY-001 | deployments | `POST .../deploy-keys`, `PUT .../deploy-keys/{key_id}` | `requestBody` is null in spec | FIXED — added `requestBody` referencing `deploy_key` schema; SDK body params made required |
| BUG-DEPLOY-002 | deployments | `POST .../environments/{env_uuid}/changes` | `requestBody` null | FIXED | Added `requestBody` referencing `deployment_environment` schema; `update_env` body param restored as required after regen |
| BUG-WEBHOOKS-001 | webhooks | `POST .../hooks` (repo+workspace), `PUT .../hooks/{uid}` (repo+workspace) | `requestBody` null for all 4 webhook write operations | FIXED — added `requestBody` referencing `webhook_subscription` schema to all 4 endpoints; SDK body params made required |
| BUG-BRANCHING-001 | branching_model | `PUT .../branching-model/settings` (repo+project) | `requestBody` null for both PUT branching-model-settings endpoints | FIXED — see BUG-BRANCHING-001 |

---

## Spec Bugs — Schema Field Mismatches

Response schema documents wrong fields — generated model omits actually-returned fields.

| ID | Schema | Problem | Fields Affected | Status |
|---|---|---|---|---|
| BUG-SCHEMA-001 | `report` | Spec has `reporter` (string), live API returns `created_by` (Account object) | `.reporter` always None; `created_by` inaccessible | FIXED — renamed `reporter` → `created_by` (`$ref: account`); added `type` field |
| BUG-SCHEMA-002 | `report_annotation` | `summary` field not marked `required` in spec, but API returns 400 without it | `summary` is de-facto required | FIXED — added `required: ["summary"]` to allOf properties entry |
| BUG-SCHEMA-003 | `task` | `links` and `type: null` present in live response but absent from spec | `Task.links`, `Task.type` inaccessible | FIXED — added `links` (additionalProperties link ref) and `type` (string enum) to task properties |
| BUG-SCHEMA-004 | `commitstatus` | `commit`, `repository`, `type` present in live response but absent from spec | `Commitstatus.commit`, `.repository`, `.type` inaccessible | FIXED — added `commit` ($ref commit), `repository` ($ref repository), `type` (string) to allOf properties |
| BUG-SCHEMA-005 | `webhook_subscription` | 4 undocumented response fields | `history_enabled`, `read_only`, `skip_cert_verification`, `source` inaccessible | FIXED — added all 4 fields to webhook_subscription allOf properties |
| BUG-SCHEMA-006 | `branch` | 2 undocumented response fields | `default_merge_strategy`, `sync_strategies` inaccessible | FIXED — added `sync_strategies` (array of strings) to branch allOf properties (`default_merge_strategy` was already present) |
| BUG-SCHEMA-007 | `deployment_environment` | Schema documents only `name` + `uuid` out of 12 returned fields | `slug`, `rank`, `category`, `environment_type`, `deployment_gate_enabled`, `environment_lock_enabled`, `lock`, `restrictions`, `hidden` all inaccessible | FIXED — added 9 missing fields (`type`, `slug`, `rank`, `hidden`, `deployment_gate_enabled`, `environment_lock_enabled`, `category`, `lock`, `restrictions`) to allOf properties (`environment_type` was already present) |
| BUG-SCHEMA-008 | `pullrequest` | `closed_by` is bare `$ref` + `nullable: true` — generator omits None guard; open PRs always crash | `closed_by` deserialization crashes with `TypeError` on `null` | FIXED |
| BUG-SCHEMA-009 | `error` | `required: ["type"]` but Bitbucket 404 errors omit `type` field | `Error.from_dict()` raises `KeyError: 'type'` on 404 responses | FIXED |
| BUG-SCHEMA-010 | `GPG_account_key` | `last_used` date-time not nullable; API returns `null` for unused keys | `isoparse(None)` → `TypeError` on any unused GPG key | FIXED |
| BUG-SCHEMA-011 | `task` | `resolved_on` (date-time) and `resolved_by` (`$ref`) not nullable; unresolved tasks always have `null` values | `isoparse(None)` / `Account.from_dict(None)` crash on unresolved tasks | FIXED |
| BUG-SCHEMA-012 | `tag` | `date` (date-time) and `tagger` (`$ref`) not nullable; lightweight tags always have `null` values | `isoparse(None)` / `Author.from_dict(None)` crash on lightweight tags | FIXED |
| BUG-SCHEMA-013 | (none) | `paginated_commits` schema missing; PR commits 200 response had no schema reference | Generated code returns `None` for all `prs.list_commits()` calls | FIXED |
| BUG-SCHEMA-014 | `deploy_key` | `last_used` date-time not nullable; API returns `null` for unused keys | `isoparse(None)` → `TypeError` on any unused deploy key | FIXED |
| BUG-SCHEMA-015 | `deployment_environment` | `environment_type` field absent from schema; type is object not string | `create_environment()` returns HTTP 400 "Property environment_type is required" | FIXED |
| BUG-SCHEMA-016 | (query params) | Issues list endpoint `parameters: []` — `q` and `sort` undocumented | `issues.list(q=...)` raises `TypeError: unexpected keyword argument 'q'` | FIXED |
| BUG-SCHEMA-017 | `subject_types` | `additionalProperties: false` on `repository`/`workspace` sub-schemas; live API wraps events inside `links` object | `GET /hook_events` schema validation fails — 2 response violations | FIXED |
| BUG-SCHEMA-018 | (status codes) | 4 endpoints missing `410 Gone`: `/snippets`, `/workspaces`, `/user/permissions/repositories`, `/user/permissions/workspaces` | 410 returned by live API (plan restriction / deprecated) silently swallowed | FIXED |
| BUG-SCHEMA-019 | (status codes) | `GET /addon/linkers` missing `403 Forbidden` — returns 403 for non-Connect-app callers | 403 silently swallowed; `_parse_response()` returns `None` | FIXED |
| BUG-SCHEMA-020 | (status codes) | 27 repo-scoped GET endpoints missing `404 Not Found` — returns 404 for non-existent workspace/repo | 404 silently swallowed; `_parse_response()` returns `None` | FIXED |
| BUG-SCHEMA-021 | (status codes) | 7 workspace-scoped GET endpoints missing `403 Forbidden` — returns 403 (not 404) for access-denied to avoid disclosing workspace existence | 403 silently swallowed; `_parse_response()` returns `None` | FIXED |
| BUG-SCHEMA-022 | (status codes) | 3 workspace-scoped GET endpoints missing `404 Not Found` — `/workspaces/{workspace}/permissions/repositories/{repo_slug}`, `/workspaces/{workspace}/pipelines-config/runners`, `/workspaces/{workspace}/pipelines-config/variables` | 404 silently swallowed | FIXED |
| BUG-SCHEMA-023 | (status codes) | 74 authenticated endpoints missing `403 Forbidden` — Bitbucket returns 403 for insufficient permissions or invalid credential type; `_parse_response()` returns `None` instead of `Error` | 403 silently swallowed across 74 endpoints (add-on, user, workspace, repo-scoped paths) | FIXED |
| BUG-SCHEMA-030 | (status codes) | `POST /repositories/{workspace}/{repo_slug}` missing `201 Created` — live API returns 201 on successful creation; spec only documents 200 | `repos.create()` returns `None` on every successful creation | FIXED |
| BUG-SCHEMA-032 | (status codes) | 242 authenticated endpoints missing `401 Unauthorized` — 133 GETs, 41 DELETEs, 36 POSTs, 32 PUTs across user/workspace/repo/snippet paths | `_parse_response()` returns `None` silently on auth failure; callers cannot distinguish "not authenticated" from "not found" | FIXED — added 401 to all 240 non-public endpoints (3 variants: unconditional/repo-conditional/snippet-conditional); also injected 403 where missing |
| BUG-SCHEMA-033 | (status codes) | No new 402 cases found beyond already-fixed download endpoints — branch restrictions and pipeline runners return 403 (not 402) for plan gates | — | REFUTED (no new cases) |
| BUG-SCHEMA-034 | (status codes) | 49 deprecated operations missing `410 Gone`: `/addon/linkers/**` (8 ops, removal notice said May 2026 — date has passed), `/teams/{username}/pipelines_config/**` (5 ops), `/users/{selected_user}/pipelines_config/**` (5 ops), 31 others with `deprecated: true` | 410 not documented on any of 49 deprecated operations; callers see `None` return for removed endpoints | CLOSED — all groups return 403 not 410; no removals have occurred; no spec changes needed |

---

## Spec Bugs — Missing Query Parameters

These cause the generated SDK wrappers to lack the corresponding keyword arguments, making pagination or filtering impossible at the call site.

| ID | Endpoint(s) | Parameters Missing | Impact | Status |
|---|---|---|---|---|
| BUG-PAGINATION-001 | 17 GET list endpoints (default-reviewers, effective-default-reviewers, forks, issues, permissions-config/groups, permissions-config/users, pipelines, pipelines-config/ssh/known_hosts, pipelines-config/variables, refs/tags, snippets, snippets/{workspace}, src/{commit}/{path}, users/{selected_user}/repositories, watchers, workspaces/{workspace}/permissions, workspaces/{workspace}/projects) | `page`, `pagelen` | Callers cannot paginate these list endpoints; results silently limited to Bitbucket's default page size | FIXED — added `page` and `pagelen` to all 17 endpoints |

---

## Spec Bugs — Schema Field Mismatches (extended)

| ID | Schema | Problem | Fields Affected | Status |
|---|---|---|---|---|
| BUG-SCHEMA-028 | `ssh_key`, `ssh_account_key` | `last_used` (date-time) not nullable; `expires_on` not nullable — API returns `null` for unused/unexpired keys | `isoparse(None)` → `TypeError` on any key that has never been used or has no expiry | FIXED — added `nullable: true` to both fields |
| BUG-SCHEMA-029 | `commit_file` | `attributes` field typed as single `string` enum; live API returns an array of strings | Deserialization crash or silent data loss when a file has any attribute (executable, binary, LFS pointer) | FIXED — changed type to `array` of string |
| BUG-SCHEMA-031 | 86+ schemas (`ref`, `issue_change`, `project_group_permission`, `repository_group_permission`, and 80+ others) | Inline `links` sub-objects define `additionalProperties: false`; any future Bitbucket link key triggers strict-validator failures | Strict schema validators reject valid responses; generated models may silently drop extra link fields | FIXED — replaced 386 inline link definitions with `$ref: "#/components/schemas/link"` |

---

## Generator Bugs

| ID | Layer | Problem | Impact | Status |
|---|---|---|---|---|
| BUG-GENERATOR-001 | generator (template) | `_parse_response()` calls `response.json()` unconditionally for JSON-schema-mapped responses; Bitbucket sometimes returns `text/html` for error paths → `json.JSONDecodeError` at runtime | Any pathological path param or overloaded Bitbucket edge node causes unhandled crash in SDK | FIXED — added content-type guard in `templates/endpoint_macros.py.jinja` |

---

## Test Bugs (wrong fixture data / request body rejected by live API)

These bugs are in the live test suite, not in the SDK or spec. The SDK call succeeds at the Python layer but the API returns 400 because the test passes invalid or disallowed data.

| ID | File | Test(s) | Root Cause | Status |
|---|---|---|---|---|
| BUG-PIPELINES-006 | `tests/cloud/live/test_pipelines.py` | `test_create_delete_known_host_roundtrip` | `github.com` is a reserved hostname (Bitbucket manages it internally → 400); `public_key` field also missing from body | FIXED |
| BUG-PRS-004 | `tests/cloud/live/test_prs.py` | `test_add_comment`, `test_update_comment` | `PullRequestComment(type_="pullrequest_comment", ...)` serializes `"type"` into JSON body; API rejects it with 400 "extra keys not allowed" | FIXED |

---

## Summary by Severity

### P0 — Crashes before HTTP call (SDK wrapper bugs)
- **Fixed:** BUG-AUTH-001, BUG-PRS-001/002/003, BUG-PRS-005, BUG-REPOS-001/002, BUG-SOURCE-001, BUG-SNIPPETS-002, BUG-ISSUES-001/002/003/004/005, BUG-PIPELINES-001/002/003/004/005/007/008, BUG-BRANCHING-001, BUG-WORKSPACES-001, BUG-DEPLOY-003
- **Fixed (generator):** BUG-GENERATOR-001 (HTML response crashes `_parse_response()`)
- **Fixed (spec→crash):** BUG-SCHEMA-028 (ssh_key nullable crash), BUG-SCHEMA-029 (commit_file attributes crash)

### P1 — Silent data loss (returns None/[] when error occurred)
- **Fixed:** BUG-COMMITS-001 (upsert returns None), BUG-DOWNLOADS-001 (plan-restricted returns []), BUG-SCHEMA-030 (repo creation returns None on 201), BUG-SCHEMA-023 (403 returns None across 74 endpoints), BUG-SCHEMA-020/021/022 (404/403 silently swallowed on 33 endpoints)

### P2 — Missing write body (all write ops return 400)
- **Fixed:** BUG-DEPLOY-001, BUG-DEPLOY-002, BUG-WEBHOOKS-001, BUG-BRANCHING-001

### P2 — Missing pagination parameters
- **Fixed:** BUG-PAGINATION-001 (17 list endpoints missing page/pagelen)

### P3 — Schema field gaps (data returned but model can't expose it)
- **Fixed:** BUG-SCHEMA-001/002/003/004/005/006/007 (all 7 field-gap bugs resolved via jq surgery + regen)
- **Fixed:** BUG-SCHEMA-031 (inline link additionalProperties: false across 86+ schemas)

### P4 — Plan-restriction silent corruption
- **Fixed:** BUG-SNIPPETS-001 — `snippets.list()` now returns `Error` on Free-plan string-in-values response

---

## Fixed Bugs (FIXED — applied to spec + regenerated)

### Auth clients (fixed in src/bb/cloud/sdk/_auth.py)
- **BUG-AUTH-001** — all 5 `get_authenticated_client()` methods missing `follow_redirects=True` → 3xx responses returned instead of following; auth header dropped on redirects

### SDK wrapper crashes (fixed in src/bb/cloud/sdk/)
- **BUG-PRS-001** — `create_task`/`update_task` had `body: Unset = UNSET`; generated code requires `PullRequestTaskCreate`/`PullRequestTaskUpdate` → changed to required typed params
- **BUG-PRS-002** — `diff`/`patch`/`diffstat`/`merge_task_status` called non-existent `.asyncio()` on binary/redirect endpoints → use `asyncio_detailed()`
- **BUG-PRS-003** — `add_comment` had `body: PullRequestComment | Unset = UNSET` → made body required (also see BUG-PRS-005)
- **BUG-PRS-005** — `add_comment` used `asyncio()` missing 201 response → `asyncio_detailed()` handling 200+201
- **BUG-REPOS-001/002** — `set_group_permission`, `set_user_permission`, `override_settings` had `body: Unset = UNSET` → correct required body types
- **BUG-SOURCE-001** — `source.get` used `asyncio()` returning `None` for `text/plain` 200 → use `asyncio_detailed()` + content-type branch
- **BUG-SNIPPETS-002** — 6 snippet write functions had `body: Model | Unset = UNSET` → changed to `body: Model = Model()`
- **BUG-ISSUES-001** — `add_change` default `IssueChange()` raised `TypeError` at import → `IssueChange(type_="issue_change")`
- **BUG-ISSUES-002** — `issues.create` had `body: Issue | Unset = UNSET` → `body: Issue = Issue()`
- **BUG-ISSUES-003** — `issues.update` had `body: Issue | Unset = UNSET` → `body: Issue = Issue()`
- **BUG-ISSUES-004** — `add_comment`/`update_comment` had `body: IssueComment | Unset = UNSET` → `body: IssueComment = IssueComment()`
- **BUG-ISSUES-005** — `upload_attachment`/`import_data` forwarded erroneous `body=UNSET` to generated API with no body param → removed param and kwarg
- **BUG-BRANCHING-001** — `update_settings`/`update_project_settings` had `body: BranchingModelSettings | Unset = UNSET`; spec also missing requestBody → made required; spec patched
- **BUG-PIPELINES-001** — `create_schedule` had `body: PipelineSchedule | Unset = UNSET`; generated requires `PipelineSchedulePostRequestBody` → changed
- **BUG-PIPELINES-002** — `update_config` had `body: Unset = UNSET`; generated requires `PipelinesConfig` → changed to required `body: PipelinesConfig`
- **BUG-PIPELINES-003** — `update_build_number` had `body: Unset = UNSET` → `body: PipelineBuildNumber`; 4 runner functions (`create_runner`, `update_runner`, `create_workspace_runner`, `update_workspace_runner`) forwarded phantom `body=body` to no-body generated APIs → removed `body` param and `body=body` from all 4
- **BUG-PIPELINES-004** — `oidc_config`/`oidc_keys` passed extra `repo_slug` to workspace-level endpoints → removed
- **BUG-PIPELINES-005** — `test_reports` missing `step_uuid` argument → added to signature and call site
- **BUG-PIPELINES-007** — `step_log` used `asyncio()` returning `None` for `text/plain` log content → `asyncio_detailed()` + decode bytes
- **BUG-PIPELINES-008** — `create_known_host` used `asyncio()` missing 201 response → `asyncio_detailed()` handling 200+201
- **BUG-WORKSPACES-001** — `get_repo_permission` returned paginated envelope instead of items list → replaced with `async_paginate()`
- **BUG-DEPLOY-003** — `update_env` passed `body=body` to generated API with no `body` param → removed `body=body` (restore after BUG-DEPLOY-002 spec fix)

### Missing requestBody in spec (fixed in bb_cloud_fixed.openapi.json + regenerated)
- **BUG-DEPLOY-001** — `POST/PUT .../deploy-keys` missing requestBody → added `deploy_key` schema reference
- **BUG-DEPLOY-002** — `POST .../environments/{env_uuid}/changes` missing requestBody → added `deployment_environment` schema reference; `update_env` body param restored as required
- **BUG-WEBHOOKS-001** — 4 webhook write endpoints missing requestBody → added `webhook_subscription` schema reference to all 4
- **BUG-BRANCHING-001** — 2 PUT branching-model-settings endpoints missing requestBody → added `branching_model_settings` schema reference

### Missing status codes in spec (fixed in bb_cloud_fixed.openapi.json + regenerated)
- **BUG-COMMITS-001** — `POST .../statuses/build` missing 200 response → added 200 commitstatus response
- **BUG-DOWNLOADS-001** — download endpoints missing 402 response → added 402 error response to all 4 endpoints

### Nullable field crashes (TypeError on None deserialization)
- **BUG-SCHEMA-008** — `pullrequest.closed_by` nullable `$ref` without `anyOf` pattern → crashed ALL open PR reads
- **BUG-SCHEMA-010** — `GPG_account_key.last_used` not nullable → crashed on unused GPG keys
- **BUG-SCHEMA-011** — `task.resolved_on` + `task.resolved_by` not nullable → crashed on unresolved tasks
- **BUG-SCHEMA-012** — `tag.date` + `tag.tagger` not nullable → crashed on lightweight tags
- **BUG-SCHEMA-014** — `deploy_key.last_used` not nullable → crashed on unused deploy keys

### Error schema bug (KeyError on 404 responses)
- **BUG-SCHEMA-009** — `error.required` includes `type` but API omits it → crashed on any 404 error

### Missing schema / endpoint wiring (silent None return)
- **BUG-SCHEMA-013** — `paginated_commits` schema missing; PR commits 200 had no schema → `prs.list_commits()` always returned `None`

### Wrong/missing field causing 400 on writes
- **BUG-SCHEMA-015** — `deployment_environment.environment_type` missing from schema (+ wrong type in initial attempt) → `create_environment()` always returned 400

### Missing query parameters
- **BUG-SCHEMA-016** — Issues list endpoint missing `q` and `sort` params → `issues.list(q=...)` raised TypeError

### Schema structure mismatch (additionalProperties violation)
- **BUG-SCHEMA-017** — `subject_types.repository/workspace` had `additionalProperties: false` + direct `events` property; live API wraps it inside `links` → schema validation failure on `GET /hook_events`

### Missing status codes (plan restriction / deprecation / access control)
- **BUG-SCHEMA-018** — `GET /snippets`, `/workspaces`, `/user/permissions/repositories`, `/user/permissions/workspaces` missing `410 Gone` → plan-restricted and deprecated endpoints silently returned `None`
- **BUG-SCHEMA-019** — `GET /addon/linkers` missing `403 Forbidden` → non-Connect-app 403 silently swallowed
- **BUG-SCHEMA-020** — 27 repo-scoped GET endpoints missing `404 Not Found` → non-existent workspace/repo 404 silently swallowed
- **BUG-SCHEMA-021** — 7 workspace-scoped GET endpoints missing `403 Forbidden` → access-denied 403 silently swallowed
- **BUG-SCHEMA-022** — 3 workspace-scoped GET endpoints (`/workspaces/{workspace}/permissions/repositories/{repo_slug}`, `/pipelines-config/runners`, `/pipelines-config/variables`) missing `404 Not Found` → nonexistent workspace 404 silently swallowed
- **BUG-SCHEMA-023** — 74 authenticated endpoints missing `403 Forbidden` → access-denied 403 silently swallowed across add-on, user, workspace, repo-scoped paths
- **BUG-SCHEMA-030** — `POST /repositories/{workspace}/{repo_slug}` missing `201 Created` → `repos.create()` always returned `None` on successful creation

### Missing pagination parameters
- **BUG-PAGINATION-001** — 17 list endpoints missing `page` and `pagelen` query params → callers cannot paginate; results silently capped at Bitbucket's default page size

### Schema nullable / type errors
- **BUG-SCHEMA-028** — `ssh_key.last_used`, `ssh_account_key.expires_on` not nullable → `TypeError` on any unused or non-expiring key
- **BUG-SCHEMA-029** — `commit_file.attributes` typed as `string` (should be `array`) → deserialization crash/data loss on files with attributes

### Schema structural
- **BUG-SCHEMA-031** — 86+ schemas with inline `links` sub-objects using `additionalProperties: false` → strict validators reject valid responses; replaced with `$ref: "#/components/schemas/link"`

### Generator fix
- **BUG-GENERATOR-001** — `_parse_response()` crashed on `text/html` Bitbucket error pages → added content-type guard in `templates/endpoint_macros.py.jinja`

### Test bugs (wrong fixture data causing HTTP 400)
- **BUG-PIPELINES-006** — `test_create_delete_known_host_roundtrip` used `github.com` (reserved by Bitbucket → 400) and omitted `public_key` from the body (also required) → changed to random `*.example.com` hostname + added `PipelineSshPublicKey`
- **BUG-PRS-004** — `add_comment`/`update_comment` test constructed `PullRequestComment(type_="pullrequest_comment", ...)`, serializing a `"type"` field the API rejects with 400 "extra keys not allowed" → removed `type_` from both constructors

---

## Fix Priority Order (remaining open bugs)

> **Note:** All P0/P1/P2/P3/P4 bugs are now FIXED. BUG-SNIPPETS-001 was resolved with an SDK-level string-in-values guard in `snippets.list()`. See the Fixed Bugs section for the full list.

---

## Spec Fix Commands (confirmed, ready to apply)

```bash
# BUG-COMMITS-001: commit status upsert returns 200
jq '.paths["/repositories/{workspace}/{repo_slug}/commit/{commit}/statuses/build"].post.responses["200"] = {
  "description": "The commit status was updated (upsert).",
  "content": {"application/json": {"schema": {"$ref": "#/components/schemas/commitstatus"}}}
}' bb_cloud_fixed.openapi.json > /tmp/fixed.json && mv /tmp/fixed.json bb_cloud_fixed.openapi.json

# BUG-DOWNLOADS-001: downloads return 402 on Free plan (must patch all 4 operations individually)
_402='{"description":"Payment Required — repository downloads require Standard or Premium plan.","content":{"application/json":{"schema":{"$ref":"#/components/schemas/error"}}}}'
jq --argjson r "$_402" '
  .paths["/repositories/{workspace}/{repo_slug}/downloads"].get.responses["402"] = $r |
  .paths["/repositories/{workspace}/{repo_slug}/downloads"].post.responses["402"] = $r |
  .paths["/repositories/{workspace}/{repo_slug}/downloads/{filename}"].get.responses["402"] = $r |
  .paths["/repositories/{workspace}/{repo_slug}/downloads/{filename}"].delete.responses["402"] = $r
' bb_cloud_fixed.openapi.json > /tmp/fixed.json && mv /tmp/fixed.json bb_cloud_fixed.openapi.json

# After all spec fixes:
make generate-cloud && make diff-cloud
```

See individual bug report files for the full jq command for each fix.
