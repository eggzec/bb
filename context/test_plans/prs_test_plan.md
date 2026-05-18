# Test Plan: `bb.cloud.sdk.prs`

Module: `src/bb/cloud/sdk/prs.py`
Probe repo: `beaverish/bb-probe`
Seed PR #1 (open): `feature/add-farewell` → `main`
Seed PR #2 (merged)
Seed comment_id: `797172056`
Seed task_id: `64759588`
Owner account_id: `712020:f464b5ca-adb8-4a1e-80d4-c867bbf50805`
Seed commit: `84952fad87fb39e3c6d61811a93769378dd4fad7`

---

## `prs.list`

- [ ] **LIST-001** Happy path: returns `list[Pullrequest]` with no state filter
- [ ] **LIST-002** All items are `Pullrequest` instances (no raw dicts)
- [ ] **LIST-003** Each `Pullrequest.id` is not None
- [ ] **LIST-004** Filter by state=OPEN returns only open PRs
- [ ] **LIST-005** Filter by state=MERGED returns only merged PRs
- [ ] **LIST-006** Filter by state=DECLINED returns list (may be empty)
- [ ] **LIST-007** Filter by state=SUPERSEDED returns list (may be empty)
- [ ] **LIST-008** `pagelen=1` vs `pagelen=50` gives identical total count (pagination integrity)

---

## `prs.get`

- [ ] **GET-001** Returns `Pullrequest` for PR #1
- [ ] **GET-002** Returned PR has `id == 1`
- [ ] **GET-003** Returned PR has non-empty `title`
- [ ] **GET-004** Nonexistent PR ID `999_999_999` returns `Error` or `None`, not `Pullrequest`

---

## `prs.create`

- [ ] **CREATE-001** Creates a PR from throwaway branch to `main` — returns `Pullrequest`
- [ ] **CREATE-002** Created PR has non-None `id`
- [ ] **CREATE-003** Created PR has `title` matching what was supplied
- [ ] **CREATE-004** Cleanup: throwaway PR is declined and throwaway branch deleted in `finally`

---

## `prs.update`

- [ ] **UPDATE-001** Update throwaway PR title — returns `Pullrequest`
- [ ] **UPDATE-002** Updated PR has the new title

---

## `prs.merge`

- [ ] **MERGE-001** SKIPPED — permanently merges the branch; not tested in live suite

---

## `prs.approve` / `prs.unapprove`

- [ ] **APPROVE-001** Approve PR #1 — returns `Participant`
- [ ] **APPROVE-002** Participant has non-None user
- [ ] **UNAPPROVE-001** Unapprove PR #1 — returns None (204)

---

## `prs.decline`

- [ ] **DECLINE-001** Decline throwaway PR — returns `Pullrequest` in DECLINED state

---

## `prs.request_changes` / `prs.unrequest_changes`

- [ ] **RC-001** `request_changes` on own PR — expected to return `Error` (self-review not allowed by BB) or raise; document result
- [ ] **RC-002** `unrequest_changes` on own PR — expected to succeed silently or error; document result

---

## `prs.comments`

- [ ] **COMMENTS-001** Returns `list[PullRequestComment]` for PR #1
- [ ] **COMMENTS-002** All items are `PullrequestComment` instances
- [ ] **COMMENTS-003** Seed comment_id `797172056` is present in the list

---

## `prs.add_comment` / `prs.get_comment` / `prs.update_comment` / `prs.delete_comment`

- [ ] **ADD-COMMENT-001** Add throwaway comment to PR #1 — returns `PullrequestComment`
- [ ] **ADD-COMMENT-002** Throwaway comment has a non-None `id`
- [ ] **GET-COMMENT-001** `get_comment` for seed comment `797172056` returns `PullrequestComment`
- [ ] **GET-COMMENT-002** Retrieved comment `id == 797172056`
- [ ] **UPDATE-COMMENT-001** Update throwaway comment — returns updated `PullrequestComment`
- [ ] **UPDATE-COMMENT-002** Updated comment has new content
- [ ] **DELETE-COMMENT-001** Delete throwaway comment — returns None (204)
- [ ] **DELETE-COMMENT-002** Cleanup: throwaway comment deleted in `finally`

---

## `prs.resolve_comment` / `prs.unresolve_comment`

- [ ] **RESOLVE-001** Resolve seed comment `797172056` — returns any non-Error result
- [ ] **UNRESOLVE-001** Unresolve seed comment `797172056` — returns None

---

## `prs.diff`

- [ ] **DIFF-001** Returns a non-empty string for PR #1
- [ ] **DIFF-002** Result is of type `str`

---

## `prs.commits`

- [ ] **COMMITS-001** Returns a non-empty list for PR #1
- [ ] **COMMITS-002** Items have a `hash_` attribute (or similar)

---

## `prs.tasks`

- [ ] **TASKS-001** Returns a list for PR #1
- [ ] **TASKS-002** Seed task_id `64759588` is present in the list

---

## `prs.create_task` / `prs.get_task` / `prs.update_task` / `prs.delete_task`

- [ ] **CREATE-TASK-001** Create a throwaway task on PR #1 — returns `PullrequestCommentTask`
- [ ] **CREATE-TASK-002** Created task has a non-None `id`
- [ ] **GET-TASK-001** `get_task` for seed task `64759588` returns a task object
- [ ] **UPDATE-TASK-001** Update throwaway task state to RESOLVED — returns task object
- [ ] **DELETE-TASK-001** Delete throwaway task — returns None
- [ ] **DELETE-TASK-002** Cleanup: throwaway task deleted in `finally`

**Known issue**: `prs.create_task` SDK wrapper signature uses `body: Unset = UNSET` but the
generated API requires `body: PullRequestTaskCreate`. This is a type-safety bug in the SDK wrapper.

---

## `prs.default_reviewers`

- [ ] **DR-001** Returns a list (likely empty for single-user workspace)
- [ ] **DR-002** Does not raise; returns `list` or `Error`

---

## `prs.add_default_reviewer` / `prs.remove_default_reviewer` / `prs.get_default_reviewer`

- [ ] **DR-ADD-001** SKIPPED — single-user workspace; adding self as reviewer expected to return 400
- [ ] **DR-REMOVE-001** SKIPPED — nothing to remove
- [ ] **DR-GET-001** `get_default_reviewer` for owner account_id — likely returns Error/None; document result

---

## `prs.effective_default_reviewers`

- [ ] **EDR-001** Returns a list for `bb-probe`
- [ ] **EDR-002** Does not raise; returns `list` or skips on Error

---

## `prs.activity`

- [ ] **ACTIVITY-001** Returns a list for `bb-probe` repository
- [ ] **ACTIVITY-002** Does not raise; returns `list` or `Error`

---

## `prs.pr_activity`

- [ ] **PR-ACTIVITY-001** Returns a list for PR #1
- [ ] **PR-ACTIVITY-002** Does not raise; returns `list` or `Error`

---

## `prs.diffstat`

- [ ] **DIFFSTAT-001** Returns a result for PR #1
- [ ] **DIFFSTAT-002** Result is not None

---

## `prs.patch`

- [ ] **PATCH-001** Returns a non-empty string for PR #1
- [ ] **PATCH-002** Result is of type `str`

---

## `prs.statuses`

- [ ] **STATUSES-001** Returns a list for PR #1 (may be empty — no CI configured)
- [ ] **STATUSES-002** Does not raise

---

## `prs.user_prs`

- [ ] **USER-PRS-001** Returns a list for owner account_id
- [ ] **USER-PRS-002** All items are `Pullrequest` instances
- [ ] **USER-PRS-003** Does not raise; list may be empty

---

## `prs.merge_task_status`

- [ ] **MTS-001** Called with a bogus task_id — returns Error or None (not exception)
- [ ] **MTS-002** Does not raise for invalid task_id

---

## Status Summary (updated after test run)

| ID | Function | Status |
|----|----------|--------|
| LIST-001..008 | `prs.list` | PENDING |
| GET-001..004 | `prs.get` | PENDING |
| CREATE-001..004 | `prs.create` | PENDING |
| UPDATE-001..002 | `prs.update` | PENDING |
| APPROVE-001..002 | `prs.approve` | PENDING |
| UNAPPROVE-001 | `prs.unapprove` | PENDING |
| DECLINE-001 | `prs.decline` | PENDING |
| RC-001..002 | `prs.request_changes` / `unrequest_changes` | PENDING |
| COMMENTS-001..003 | `prs.comments` | PENDING |
| ADD-COMMENT-001..002 | `prs.add_comment` | PENDING |
| GET-COMMENT-001..002 | `prs.get_comment` | PENDING |
| UPDATE-COMMENT-001..002 | `prs.update_comment` | PENDING |
| DELETE-COMMENT-001..002 | `prs.delete_comment` | PENDING |
| RESOLVE-001 | `prs.resolve_comment` | PENDING |
| UNRESOLVE-001 | `prs.unresolve_comment` | PENDING |
| DIFF-001..002 | `prs.diff` | PENDING |
| COMMITS-001..002 | `prs.commits` | PENDING |
| TASKS-001..002 | `prs.tasks` | PENDING |
| CREATE-TASK-001..002 | `prs.create_task` | PENDING |
| GET-TASK-001 | `prs.get_task` | PENDING |
| UPDATE-TASK-001 | `prs.update_task` | PENDING |
| DELETE-TASK-001..002 | `prs.delete_task` | PENDING |
| DR-001..002 | `prs.default_reviewers` | PENDING |
| EDR-001..002 | `prs.effective_default_reviewers` | PENDING |
| ACTIVITY-001..002 | `prs.activity` | PENDING |
| PR-ACTIVITY-001..002 | `prs.pr_activity` | PENDING |
| DIFFSTAT-001..002 | `prs.diffstat` | PENDING |
| PATCH-001..002 | `prs.patch` | PENDING |
| STATUSES-001..002 | `prs.statuses` | PENDING |
| USER-PRS-001..003 | `prs.user_prs` | PENDING |
| MTS-001..002 | `prs.merge_task_status` | PENDING |
