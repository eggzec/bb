# Bug Investigation Summary — 2026-05-17

## Scope

Investigated all bugs marked `PARTIAL` or `NEEDS-INVESTIGATION` in `MASTER_BUG_INDEX.md`:
- **BUG-SNIPPETS-001** (PARTIAL): Can we fix the snippets Free-plan issue at spec level?
- **BUG-SCHEMA-033** (NEEDS-INVESTIGATION): Code Insights endpoints — do they return 402?
- **BUG-SCHEMA-034** (NEEDS-INVESTIGATION): Deprecated endpoints missing 410?

---

## BUG-SNIPPETS-001: Snippets Free-Plan Behavior

**Verdict: CANNOT BE FIXED AT SPEC LEVEL — Bitbucket API bug, no spec fix applies.**

**Live confirmation (2026-05-17):**
```
GET /2.0/snippets/beaverish → HTTP 200
Body: {"values":["A workspace on a Free plan does not support snippets. Upgrade to..."],"pagelen":30,"page":1}
```

The endpoint returns HTTP 200 (not 402, not 410) with the error message embedded as a **string
element** inside the `values` array that the spec declares as an array of snippet objects.

**Why it cannot be fixed at the spec level:**
1. **Adding 402** — wrong, the HTTP status is 200, not 402.
2. **Making `values` a union type** — OpenAPI `oneOf`/`anyOf` in array items is poorly
   supported by code generators (produces `Any` types, loses type safety). Not a good fit.
3. **Adding an `x-plan-restriction` extension** — non-standard, ignored by generators.
4. **Changing nothing** — closest to correct, but leaves callers unable to detect the error.

**Actionable fix: SDK wrapper only.** `snippets.list()` should inspect `values[0]`: if it is
a string, treat the response as a plan-restriction error and raise `PlanRestrictionError` or
return an appropriate `Error` object. This is a **Bitbucket API bug** — the paginated 200
envelope is misused to embed error strings instead of returning a proper error response.

**Bug report updated** — Resolution section added to `BUG-SNIPPETS-001_402-not-in-spec.md`.

---

## BUG-SCHEMA-033: Code Insights Missing 402

**Verdict: REFUTED — Code Insights is accessible on Free plan; no 402 needed.**

**Live confirmation (2026-05-17):**
```
GET  /repositories/beaverish/bb-probe/commit/9cb3ffdb9631/reports → HTTP 200 (list with seeded fixture)
PUT  /repositories/beaverish/bb-probe/commit/9cb3ffdb9631/reports/spec-check-2026 → HTTP 200 (created)
```

Both read and write Code Insights endpoints returned 200 on a Free-plan workspace. No 402
(Payment Required) was observed. The Bitbucket plan comparison page language about Code
Insights being a paid feature appears to be outdated or refers to advanced enterprise features.

The existing 8 `402` responses in the spec (downloads + permissions-config) remain correct and
complete. **No new 402 cases exist.**

**Bug report updated** — Code Insights section updated from NEEDS-INVESTIGATION to REFUTED;
Conclusion updated to CLOSED in `BUG-SCHEMA-033_missing-402-subscription-gated-endpoints.md`.

---

## BUG-SCHEMA-034: Missing 410 on Deprecated Endpoints

**Verdict: NO 410 CHANGES NEEDED — All investigated deprecated endpoints still live.**

### Group 1: `/addon/linkers/**` (8 operations)

```
GET /2.0/addon/linkers → HTTP 403
{"error":{"message":"This API is only accessible with the following authentication types: jwt"}}
```

The stated removal date of "May 2026" has passed, but the endpoint returns **403** (not 410).
The endpoint is alive but requires Connect app JWT auth. The existing 403 in the spec (added
by BUG-SCHEMA-019) is correct. No 410 needed.

### Group 2: `/teams/{username}/pipelines_config/variables` (5 operations)

```
GET /2.0/teams/beaverish/pipelines_config/variables → HTTP 403
{"error":{"message":"This resource does not support authentication using the provided token"}}
```

Still alive, returns 403 (OAuth app token required, not API token). No 410 needed.

### Group 3: `/users/{selected_user}/pipelines_config/variables` (5 operations)

```
GET /2.0/users/beaverish/pipelines_config/variables → HTTP 403
{"error":{"message":"This resource does not support authentication using the provided token"}}
```

Same as Group 2 — alive, 403, not 410. No 410 needed.

### Group 4: Issue tracker, milestones, components, versions (33 operations)

Not a 410 candidate (confirmed in prior investigation). API returns 200 for repos with
issue tracker enabled, 404 for repos without it. No change needed.

### Group 5: `GET /snippets/{workspace}` (1 operation)

```
GET /2.0/snippets/beaverish → HTTP 200 (with error string in values[], Free plan)
GET /2.0/snippets          → HTTP 410 (root endpoint, already documented)
```

The workspace-scoped snippet list returns 200, not 410. Only the global root
`GET /snippets` returns 410 (already in spec). No 410 to add to `GET /snippets/{workspace}`.

**Bug report updated** — all groups updated with live verification findings; status changed
to PARTIALLY CLOSED with all groups resolved as NOT 410 in
`BUG-SCHEMA-034_additional-410-deprecated-endpoints.md`.

---

## Overall Conclusion

| Bug | Old Status | New Status | Spec Change? |
|---|---|---|---|
| BUG-SNIPPETS-001 | PARTIAL | RESOLVED (no spec fix possible) | No — SDK wrapper fix needed |
| BUG-SCHEMA-033 Code Insights | NEEDS-INVESTIGATION | CLOSED (REFUTED) | No |
| BUG-SCHEMA-034 addon/linkers | NEEDS-INVESTIGATION | CLOSED (403, not 410) | No |
| BUG-SCHEMA-034 /teams/ | NEEDS-INVESTIGATION | CLOSED (403, not 410) | No |
| BUG-SCHEMA-034 /users/ | NEEDS-INVESTIGATION | CLOSED (403, not 410) | No |
| BUG-SCHEMA-034 snippets/{ws} | NEEDS-INVESTIGATION | CLOSED (200, not 410) | No |

**Zero spec changes are warranted from this investigation.** All PARTIAL/NEEDS-INVESTIGATION
bugs are now resolved. The only actionable item remaining is a **SDK-layer fix** for
`snippets.list()` to detect the Free-plan error string in `values[]` and raise an appropriate
error instead of silently returning a list of strings.
