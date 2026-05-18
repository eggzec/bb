# Test Plan — branches / branching_model / branch_restrictions

**Workspace:** beaverish  
**Probe repo:** bb-probe  
**Seed branch:** main (commit `84952fad87fb39e3c6d61811a93769378dd4fad7`)  
**Seed branch 2:** feature/add-farewell  
**Seed tag:** v0.1.0  
**Seed restriction id:** 76271307 (require_approvals_to_merge, pattern: main)

---

## Module: `bb.cloud.sdk.branches` (8 functions)

| # | Test ID | Function | Scenario | Expected | Status |
|---|---------|----------|----------|----------|--------|
| 1 | `test_list_returns_branches` | `list` | pagelen=10 on bb-probe | Returns `list[Branch]`; every item has `.name` | - |
| 2 | `test_list_pagination_consistent` | `list` | pagelen=1 vs pagelen=50 — totals equal | Counts match | - |
| 3 | `test_list_includes_main` | `list` | list bb-probe | "main" is in the names | - |
| 4 | `test_get_returns_branch` | `get` | name="main" | Returns `Branch` with name=="main" | - |
| 5 | `test_get_missing_branch_is_error_or_none` | `get` | name="no-such-branch-zzz" | Returns `Error` or `None`, NOT `Branch` | - |
| 6 | `test_create_and_delete_branch_roundtrip` | `create` / `delete` | Create throwaway from seed hash, verify get, delete, verify gone | Branch exists after create; absent after delete | - |
| 7 | `test_list_tags_returns_tags` | `tags` | bb-probe | Returns `list[Tag]`; every item has `.name` | - |
| 8 | `test_list_tags_includes_v010` | `tags` | bb-probe | "v0.1.0" in names | - |
| 9 | `test_get_tag_returns_tag` | `get_tag` | name="v0.1.0" | Returns `Tag` with name=="v0.1.0" | - |
| 10 | `test_get_tag_missing_is_error_or_none` | `get_tag` | name="no-such-tag-zzz" | Returns `Error` or `None`, NOT `Tag` | - |
| 11 | `test_create_and_delete_tag_roundtrip` | `create_tag` / `delete_tag` | Create throwaway tag on seed commit, verify get, delete, verify gone | Tag exists after create; absent after delete | - |

---

## Module: `bb.cloud.sdk.branching_model` (7 functions)

| # | Test ID | Function | Scenario | Expected | Status |
|---|---------|----------|----------|----------|--------|
| 1 | `test_get_returns_branching_model` | `get` | bb-probe | Returns `BranchingModel` or `None` (not Error) | - |
| 2 | `test_effective_returns_model` | `effective` | bb-probe | Returns `EffectiveRepoBranchingModel`; development.name is set | - |
| 3 | `test_effective_development_branch_is_main` | `effective` | bb-probe | development.name == "main" or use_mainbranch == True | - |
| 4 | `test_settings_returns_model` | `settings` | bb-probe | Returns `BranchingModelSettings`; type_ is set | - |
| 5 | `test_update_settings_roundtrip` | `update_settings` | Read → PUT same payload back → verify same type | Returns `BranchingModelSettings`; no data loss | - |
| 6 | `test_project_get_returns_model_or_none` | `project_get` | beaverish first project | Returns `BranchingModel` or None (skips if no project) | - |
| 7 | `test_project_settings_returns_model_or_none` | `project_settings` | beaverish first project | Returns `BranchingModelSettings` or None | - |

---

## Module: `bb.cloud.sdk.branch_restrictions` (5 functions)

| # | Test ID | Function | Scenario | Expected | Status |
|---|---------|----------|----------|----------|--------|
| 1 | `test_list_returns_restrictions` | `list` | bb-probe | Returns `list[Branchrestriction]`; every item is typed | - |
| 2 | `test_list_includes_seed_restriction` | `list` | bb-probe | id 76271307 is present | - |
| 3 | `test_get_seed_restriction` | `get` | id=76271307 | Returns `Branchrestriction` with kind==require_approvals_to_merge, pattern=="main" | - |
| 4 | `test_get_missing_restriction_is_error_or_none` | `get` | id=999999999 | Returns `Error` or `None`, NOT `Branchrestriction` | - |
| 5 | `test_create_update_delete_restriction_roundtrip` | `create` / `update` / `delete` | Create push+glob restriction, update value field (or pattern), delete | Full lifecycle completes cleanly | - |

---

## Cross-cutting concerns

- All SDK functions return typed objects; they never raise raw `httpx` or `UnexpectedStatus` exceptions in normal operation
- Throwaway resources are always cleaned up in `finally` blocks
- Unique names use `uuid.uuid4().hex[:8]` prefix to avoid collisions
- Pagination: pagelen=1 forces multi-page traversal; total must equal pagelen=50 result count
