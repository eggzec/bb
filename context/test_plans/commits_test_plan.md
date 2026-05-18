# Test Plan: commits, commit_statuses, reports

**Modules under test:**
- `src/bb/cloud/sdk/commits.py`
- `src/bb/cloud/sdk/commit_statuses.py`
- `src/bb/cloud/sdk/reports.py`

**Seed data (never mutate):**
| Name | Value |
|---|---|
| workspace | `beaverish` |
| repo | `bb-probe` |
| commit hash | `84952fad87fb39e3c6d61811a93769378dd4fad7` |
| commit status key | `bb-probe-ci` (state: SUCCESSFUL) |
| report_id | `bb-probe-report` (type: TEST) |
| annotation_id | `bb-probe-ann-001` on `bb-probe-report` |

---

## Module: commits

### Function: `list`

**TC-COMMITS-001** — Happy path list  
- Call `commits.list(client, workspace, probe_repo_slug, pagelen=10)`  
- Assert return type is `list[BaseCommit]`, not `Error`  
- Assert every element has a non-empty `hash_`

**TC-COMMITS-002** — Pagination integrity  
- Call `list(pagelen=1)` and `list(pagelen=5)`  
- Assert `len(pagelen=1_result) == len(pagelen=5_result)`  
- Assert the sets of hashes match (no duplicates, no missing items)  
- Rationale: `async_paginate` must traverse all pages regardless of page size

### Function: `get`

**TC-COMMITS-003** — Known commit hash  
- Call `commits.get(client, workspace, "bb-probe", "84952fad87fb39e3c6d61811a93769378dd4fad7")`  
- Assert result is `Commit`  
- Assert `result.hash_ == "84952fad87fb39e3c6d61811a93769378dd4fad7"`

**TC-COMMITS-004** — Missing commit hash (negative path)  
- Call `commits.get(client, workspace, probe_repo_slug, "0000000000000000000000000000000000000000")`  
- Assert result is `Error` or `None`, NOT `Commit`  
- SDK must not raise; the function absorbs 404 and returns `Error | None`

### Function: `prs`

**TC-COMMITS-005** — PRs for seed commit  
- Call `commits.prs(client, workspace, "bb-probe", "84952fad87fb39e3c6d61811a93769378dd4fad7")`  
- Assert result is `list[Pullrequest]` (may be empty — no assert on length)  
- If non-empty, assert every element is `Pullrequest`

---

## Module: commit_statuses

### Function: `list`

**TC-CS-001** — List for seed commit  
- Call with seed commit hash  
- Assert result is `list[Commitstatus]`  
- Assert at least one status is present  
- Assert `bb-probe-ci` key is in the list

**TC-CS-002** — Every item is `Commitstatus`  
- Assert type for each item in the list

### Function: `get`

**TC-CS-003** — Get `bb-probe-ci`  
- Assert result is `Commitstatus`  
- Assert `result.key == "bb-probe-ci"`  
- Assert `result.state == CommitstatusState.SUCCESSFUL`

**TC-CS-004** — Get missing key  
- Call `commit_statuses.get(client, workspace, probe_repo_slug, commit, "key-that-does-not-exist")`  
- Assert result is `Error` or `None`, not `Commitstatus`

### Function: `create`

**TC-CS-005** — Create throwaway status  
- Key: `"bb-test-status-<uuid4>"`  
- State: `INPROGRESS`  
- In `finally` block: update the key to `STOPPED` to mark it benign (no DELETE on statuses API)  
- Assert result is `Commitstatus`  
- Assert `result.key == throwaway_key`  
- Assert `result.state == CommitstatusState.INPROGRESS`  
- **Note:** spec says POST returns 201 — if API actually returns 200, generator swallows it as `UnexpectedStatus` → `None`. Document actual HTTP status.

**TC-CS-006** — Idempotent re-create (same key, same state)  
- POST the same key twice  
- Assert second call also returns `Commitstatus` (no error)

### Function: `update`

**TC-CS-007** — Update throwaway status state  
- Create key `"bb-test-status-<uuid4>"` with `INPROGRESS`  
- Update same key with `FAILED`  
- Assert `result.state == CommitstatusState.FAILED`  
- Cleanup: update to `STOPPED`

---

## Module: reports

### Function: `list`

**TC-REP-001** — List reports for seed commit  
- Assert result is `list[Report]`  
- Assert `bb-probe-report` external_id is present in the list

### Function: `get`

**TC-REP-002** — Get `bb-probe-report`  
- Assert result is `Report`  
- Assert `result.report_type == ReportReportType.TEST`

**TC-REP-003** — Get missing report  
- Assert result is `Error` or `None`

### Function: `create_or_update` (create path)

**TC-REP-004** — Create throwaway report  
- report_id: `"bb-test-report-<uuid4>"`  
- type: `TEST`, result: `PENDING`, title: `"bb-sdk live test"`  
- Cleanup in `finally`: call `reports.delete`  
- Assert result is `Report`  
- Assert `result.external_id == report_id` or `result.report_type == ReportReportType.TEST`  
- **Note:** generated code checks only 200; API may return 201 → `UnexpectedStatus`. Document.

### Function: `create_or_update` (update path)

**TC-REP-005** — Update throwaway report  
- Create first, then PUT again with `result=PASSED`  
- Assert updated result has `result == ReportResult.PASSED`  
- Cleanup in `finally`: call `reports.delete`

### Function: `delete`

**TC-REP-006** — Delete throwaway report  
- Create throwaway, delete it, then `get` it  
- Assert get returns `Error` or `None`  
- (delete itself should not raise)

### Function: `annotations`

**TC-REP-007** — List annotations on `bb-probe-report`  
- Assert result is `list[ReportAnnotation]`  
- Assert `bb-probe-ann-001` external_id is present

### Function: `get_annotation`

**TC-REP-008** — Get `bb-probe-ann-001`  
- Assert result is `ReportAnnotation`  
- Assert `result.external_id == "bb-probe-ann-001"`

**TC-REP-009** — Get missing annotation  
- Assert result is `Error` or `None`

### Function: `create_annotation`

**TC-REP-010** — Create throwaway annotation  
- On `bb-probe-report`  
- annotation_id: `"bb-test-ann-<uuid4>"`  
- Cleanup in `finally`: call `reports.delete_annotation`  
- Assert result is `ReportAnnotation`

### Function: `delete_annotation`

**TC-REP-011** — Delete throwaway annotation  
- Create, delete, then get  
- Assert get returns `Error` or `None`

---

## Known Spec / Generator Risk Areas

| Risk | Description |
|---|---|
| commit_statuses.create 201 vs 200 | Spec documents POST → 201; if API returns 200, generator raises `UnexpectedStatus` |
| reports.create_or_update 201 vs 200 | Spec documents PUT → 200; if API returns 201, generator raises `UnexpectedStatus` |
| reports.create_annotation 201 vs 200 | Same risk as above for annotation PUT |
| Missing hash → Error or None | API returns 404; SDK must absorb it not raise |

---

## Checklist

| Test Case | Function | Test name | Status | Notes |
|---|---|---|---|---|
| TC-COMMITS-001 | commits.list | test_list_returns_commits | PENDING | |
| TC-COMMITS-002 | commits.list | test_list_pagelen_integrity | PENDING | |
| TC-COMMITS-003 | commits.get | test_get_known_commit | PENDING | Uses seed hash |
| TC-COMMITS-003b | commits.get | test_get_probe_commit_via_fixture | PENDING | Uses fixture hash |
| TC-COMMITS-004 | commits.get | test_get_missing_commit_is_error_or_none | PENDING | |
| TC-COMMITS-005 | commits.prs | test_prs_for_seed_commit | PENDING | May be empty list |
| TC-CS-001 | commit_statuses.list | test_list_returns_statuses | PENDING | |
| TC-CS-002 | commit_statuses.list | (within TC-CS-001) | PENDING | Per-item type check |
| TC-CS-003 | commit_statuses.get | test_get_seed_status | PENDING | Verify SUCCESSFUL |
| TC-CS-004 | commit_statuses.get | test_get_missing_status_is_error_or_none | PENDING | |
| TC-CS-005 | commit_statuses.create | test_create_throwaway_status | PENDING | Risk: BUG-COMMITS-001 |
| TC-CS-006 | commit_statuses.create | test_create_idempotent_same_key | PENDING | Risk: BUG-COMMITS-001 |
| TC-CS-007 | commit_statuses.update | test_update_throwaway_status | PENDING | Risk: BUG-COMMITS-001 for create step |
| TC-REP-001 | reports.list | test_list_reports_for_seed_commit | PENDING | |
| TC-REP-002 | reports.get | test_get_seed_report | PENDING | Verify type=TEST |
| TC-REP-003 | reports.get | test_get_missing_report_is_error_or_none | PENDING | |
| TC-REP-004 | reports.create_or_update | test_create_throwaway_report | PENDING | Risk: BUG-COMMITS-002 |
| TC-REP-005 | reports.create_or_update | test_update_throwaway_report | PENDING | Risk: BUG-COMMITS-002 |
| TC-REP-006 | reports.delete | test_delete_throwaway_report | PENDING | Risk: BUG-COMMITS-002 |
| TC-REP-007 | reports.annotations | test_list_annotations_for_seed_report | PENDING | |
| TC-REP-008 | reports.get_annotation | test_get_seed_annotation | PENDING | |
| TC-REP-009 | reports.get_annotation | test_get_missing_annotation_is_error_or_none | PENDING | |
| TC-REP-010 | reports.create_annotation | test_create_throwaway_annotation | PENDING | Risk: BUG-COMMITS-003 |
| TC-REP-011 | reports.delete_annotation | test_delete_throwaway_annotation | PENDING | Risk: BUG-COMMITS-003 |

## Bug Reports Filed (pre-run static analysis)

| Bug | Module/Function | Summary |
|---|---|---|
| BUG-COMMITS-001 | commit_statuses.create | POST may return 200; generator only handles 201 → None or UnexpectedStatus |
| BUG-COMMITS-002 | reports.create_or_update | PUT (create) may return 201; generator only handles 200 → UnexpectedStatus |
| BUG-COMMITS-003 | reports.create_annotation | PUT (create) may return 201; generator only handles 200 → UnexpectedStatus |
