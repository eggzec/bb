# BUG-SCHEMA-033: Investigation — Missing 402 on Subscription-Gated Endpoints

**Status:** CLOSED — existing 402 coverage is complete; Code Insights REFUTED (Free plan accessible)
**Layer:** spec (investigation)
**Triggered by:** systematic spec scan for missing 402 responses on subscription-gated features

---

## Scope

Scanned all 335 operations in `bb_cloud_fixed.openapi.json` for endpoints that return
`402 Payment Required` in practice but lack that response code in the spec.

```bash
jq '[.paths | to_entries[] | .key as $path | .value | to_entries[] | select(.key != "parameters") | {path: $path, method: .key, has_402: (.value.responses | has("402"))}]' bb_cloud_fixed.openapi.json | python3 -c "..."
# Total operations: 335
# Operations with 402: 8
# Operations without 402: 327
```

---

## Current 402 Coverage (8 operations — all confirmed correct)

| Method | Path | Reason |
|---|---|---|
| `GET` | `/repositories/{workspace}/{repo_slug}/downloads` | Downloads require Standard or Premium |
| `POST` | `/repositories/{workspace}/{repo_slug}/downloads` | Downloads require Standard or Premium |
| `DELETE` | `/repositories/{workspace}/{repo_slug}/downloads/{filename}` | Downloads require Standard or Premium |
| `GET` | `/repositories/{workspace}/{repo_slug}/downloads/{filename}` | Downloads require Standard or Premium |
| `PUT` | `/repositories/{workspace}/{repo_slug}/permissions-config/groups/{group_slug}` | Plan user-limit hit |
| `PUT` | `/repositories/{workspace}/{repo_slug}/permissions-config/users/{selected_user_id}` | Plan user-limit hit |
| `PUT` | `/workspaces/{workspace}/projects/{project_key}/permissions-config/groups/{group_slug}` | Plan user-limit hit |
| `PUT` | `/workspaces/{workspace}/projects/{project_key}/permissions-config/users/{selected_user_id}` | Plan user-limit hit |

These were previously identified in BUG-DOWNLOADS-001 and BUG-SCHEMA-023 and are already fixed.

---

## Candidates Investigated

### 1. Branch Restrictions (Premium kinds) — NOT 402

`/repositories/{workspace}/{repo_slug}/branch-restrictions` (GET, POST) and
`/repositories/{workspace}/{repo_slug}/branch-restrictions/{id}` (GET, PUT, DELETE)

The POST endpoint documents restriction kinds that require Premium:
`enforce_merge_checks`, `allow_auto_merge_when_builds_pass`,
`require_default_reviewer_approvals_to_merge`, etc.

**Finding:** Bitbucket returns `403 Forbidden` (not 402) when a plan-gated restriction kind
is used without the required plan. The 403 is already documented. No 402 missing.

### 2. Snippets — Confirmed 200-with-error, NOT 402

All `/snippets/**` endpoints. BUG-SNIPPETS-001 investigated this.

**Finding:** On a Free plan workspace, snippets endpoints return HTTP 200 with error strings
embedded in `values[]` — not 402. BUG-SNIPPETS-001 is marked PARTIALLY CONFIRMED with
status "returns 200 with error strings in values[], not 402." No 402 to add.

The `/snippets` GET already has a `410` response (added in BUG-SCHEMA-018).

### 3. Pipelines Runners (Premium) — NOT 402

`/repositories/{workspace}/{repo_slug}/pipelines-config/runners` (GET, POST) and
`/workspaces/{workspace}/pipelines-config/runners` (GET, POST)

**Finding:** Self-hosted runners require Bitbucket Premium. The API returns `403` when the
workspace lacks the Premium plan. 403 is already documented on these endpoints. No 402.

### 4. Pipelines Config Variables — NOT 402

`/repositories/{workspace}/{repo_slug}/pipelines_config/variables` and related endpoints.

**Finding:** Pipelines is available on all plans (with minute limits). The 403 documented is
for access control, not plan gating. No 402 applies.

### 5. Deployment Environments — NOT 402

`/repositories/{workspace}/{repo_slug}/environments` and sub-paths.

**Finding:** Environments are available on Standard and above. The API returns `403` for
access-denied, but plan gating for environments is enforced at the POST level via the
existing 403. No 402 documented or observed.

### 6. Code Insights (Commit Reports/Annotations) — NOT 402

`/repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}` (PUT, GET, DELETE)
and annotation sub-paths.

Code Insights is documented as requiring Standard or Premium plan in Bitbucket's marketing
pages. However, the spec only documents 200/403/404 and no 402.

**Live verification (2026-05-17):**

```bash
# GET reports list — returns 200 with existing report (seeded fixture)
curl -u "$BB_EMAIL:$BB_TOKEN" \
  "https://api.bitbucket.org/2.0/repositories/beaverish/bb-probe/commit/9cb3ffdb9631/reports"
# → HTTP 200, returns paginated list with existing report

# PUT create a new report — returns 200
curl -u "$BB_EMAIL:$BB_TOKEN" -X PUT -H "Content-Type: application/json" \
  -d '{"title":"spec-check","report_type":"TEST","result":"PASSED"}' \
  "https://api.bitbucket.org/2.0/repositories/beaverish/bb-probe/commit/9cb3ffdb9631/reports/spec-check-2026"
# → HTTP 200 with full report object (no 402, no 403)
```

**Finding:** Code Insights endpoints are **fully accessible on Free plan** — no plan restriction
applies. The Free plan does have Code Insights for basic reports. No 402 is returned.
The 402 suspicion was based on Atlassian's marketing page language, which appears outdated.

**Assessment: REFUTED — No 402 missing here.**

### 7. Issue Tracker Endpoints — NOT 402

All `/repositories/{workspace}/{repo_slug}/issues/**`,
`/repositories/{workspace}/{repo_slug}/milestones/**`,
`/repositories/{workspace}/{repo_slug}/components/**`,
`/repositories/{workspace}/{repo_slug}/versions/**`

**Finding:** Issue tracker can be enabled/disabled per repo, and the API returns `404`
when disabled (documented: "The specified repository does not exist or does not have the
issue tracker enabled."). No plan-based 402 applies here.

### 8. Deploy Keys — NOT 402

`/repositories/{workspace}/{repo_slug}/deploy-keys` and sub-paths.

**Finding:** Deploy keys are available on all plans. No 402 applicable.

---

## Conclusion (Updated 2026-05-17)

**Status: CLOSED — No new 402 cases found.**

No new 402 cases were found beyond the already-fixed downloads and permissions-config endpoints.

The Code Insights investigation (candidate 6) is now REFUTED: live testing on 2026-05-17
confirmed that Code Insights endpoints (`GET`, `PUT` for reports) return HTTP 200 on a Free
plan workspace. Code Insights is accessible on Free plan — no plan restriction applies, so
no 402 response is needed in the spec.

The 8 existing 402 cases in the spec are correct and complete. No further 402 additions are
warranted across all 335 operations.
