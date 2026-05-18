# BUG-SCHEMA-034: Missing 410 on Additional Deprecated Endpoints

**Status:** PARTIALLY CLOSED — /addon/linkers: 403-not-410 (JWT-only); /teams/ & /users/: 403-not-410; /snippets/{workspace}: 410 needs adding
**Layer:** spec
**Triggered by:** systematic scan of deprecated endpoints lacking `410 Gone` response

---

## Background

BUG-SCHEMA-018 (FIXED) added `410` to four endpoints:
- `GET /snippets`
- `GET /workspaces`
- `GET /user/permissions/repositories`
- `GET /user/permissions/workspaces`

This report covers additional deprecated endpoints that do NOT yet have `410` in the spec.

---

## jq Evidence

All deprecated endpoints currently in the spec without a 410 response:

```bash
jq '[.paths | to_entries[] | .key as $path | .value | to_entries[] | select(.key != "parameters") | select(.value.deprecated == true) | select(.value.responses | has("410") | not) | {path: $path, method: .key}]' bb_cloud_fixed.openapi.json
```

Produces 49 operations. Key groups below.

---

## Group 1: `/addon/linkers` and sub-paths — HIGH PRIORITY

**8 operations across 5 paths. All have `deprecated: true`.**

All carry an explicit removal notice:

> "This endpoint is deprecated and will be removed by May 2026."

**Today is 2026-05-16.** The stated removal date has arrived. These endpoints may now return
`410 Gone` in practice.

| Method | Path | Current responses |
|---|---|---|
| `GET` | `/addon/linkers` | 200, 401, 403 |
| `GET` | `/addon/linkers/{linker_key}` | 200, 401, 403, 404 |
| `DELETE` | `/addon/linkers/{linker_key}/values` | 204, 401, 403, 404 |
| `GET` | `/addon/linkers/{linker_key}/values` | 200, 401, 403, 404 |
| `POST` | `/addon/linkers/{linker_key}/values` | 201, 401, 403, 404, 409 |
| `PUT` | `/addon/linkers/{linker_key}/values` | 204, 400, 401, 403, 404 |
| `DELETE` | `/addon/linkers/{linker_key}/values/{value_id}` | 204, 401, 403, 404 |
| `GET` | `/addon/linkers/{linker_key}/values/{value_id}` | 200, 401, 403, 404 |

**Live verification (2026-05-17):**

```bash
curl -u "$BB_EMAIL:$BB_TOKEN" "https://api.bitbucket.org/2.0/addon/linkers"
# → HTTP 403
# {"type":"error","error":{"message":"This API is only accessible with the following authentication types: jwt"}}
```

**Assessment: NOT 410 — Still JWT-only gated (403)**

The endpoint still returns `403` with "only accessible with jwt authentication" — it has NOT
been removed (no 410 returned). The endpoint is alive but inaccessible with Bearer tokens.
The removal date stated in the deprecation notice ("May 2026") has passed, but the endpoint
was not removed — it still enforces JWT-only auth. The existing `403` in the spec is correct.
No 410 should be added based on this evidence.

Note: BUG-SCHEMA-019 previously added `403` to these endpoints — that fix remains valid.
If Bitbucket eventually removes these endpoints (returning 410), a follow-up fix can add it.

---

## Group 2: `/teams/{username}/pipelines_config/variables` and sub-paths — MEDIUM

**5 operations across 2 paths. All have `deprecated: true`.**

> "This endpoint has been deprecated, and you should use the new workspaces endpoint."

No removal date specified. The `/workspaces/{workspace}/pipelines-config/variables` is the
replacement. These endpoints may still function (redirecting or proxying to the workspace
equivalent), or may return 410.

| Method | Path | Current responses |
|---|---|---|
| `GET` | `/teams/{username}/pipelines_config/variables` | 200, 403 |
| `POST` | `/teams/{username}/pipelines_config/variables` | 201, 403, 404, 409 |
| `GET` | `/teams/{username}/pipelines_config/variables/{variable_uuid}` | 200, 403, 404 |
| `PUT` | `/teams/{username}/pipelines_config/variables/{variable_uuid}` | 200, 403, 404 |
| `DELETE` | `/teams/{username}/pipelines_config/variables/{variable_uuid}` | 204, 403, 404 |

**Live verification (2026-05-17):**

```bash
curl -u "$BB_EMAIL:$BB_TOKEN" \
  "https://api.bitbucket.org/2.0/teams/beaverish/pipelines_config/variables"
# → HTTP 403
# {"type":"error","error":{"message":"This resource does not support authentication using the provided token"}}
```

**Assessment: NOT 410 — Returns 403 (token type restriction), not 410**

The `/teams/` endpoints are still alive but restrict access to OAuth app tokens (not API tokens).
No 410 to add. The existing 403 in the spec is correct for this access control pattern.

---

## Group 3: `/users/{selected_user}/pipelines_config/variables` and sub-paths — MEDIUM

**5 operations across 2 paths. All have `deprecated: true`.**

> "This endpoint has been deprecated, and you should use the new workspaces endpoint."

Same situation as Group 2 — deprecated in favor of workspace-level variables, no removal date.

| Method | Path | Current responses |
|---|---|---|
| `GET` | `/users/{selected_user}/pipelines_config/variables` | 200, 403 |
| `POST` | `/users/{selected_user}/pipelines_config/variables` | 201, 403, 404, 409 |
| `GET` | `/users/{selected_user}/pipelines_config/variables/{variable_uuid}` | 200, 403, 404 |
| `PUT` | `/users/{selected_user}/pipelines_config/variables/{variable_uuid}` | 200, 403, 404 |
| `DELETE` | `/users/{selected_user}/pipelines_config/variables/{variable_uuid}` | 204, 403, 404 |

**Live verification (2026-05-17):**

```bash
curl -u "$BB_EMAIL:$BB_TOKEN" \
  "https://api.bitbucket.org/2.0/users/beaverish/pipelines_config/variables"
# → HTTP 403
# {"type":"error","error":{"message":"This resource does not support authentication using the provided token"}}
```

**Assessment: NOT 410 — Returns 403 (same token-type restriction as /teams/)**

Same behavior as Group 2. The `/users/` endpoints are alive but require OAuth app tokens.
No 410 to add.

---

## Group 4: Issue Tracker, Milestones, Components, Versions — LOW PRIORITY

**All marked `deprecated: true` in the spec. 33 operations across 19 paths.**

These include all `/repositories/{workspace}/{repo_slug}/issues/**`,
`/milestones/**`, `/components/**`, `/versions/**`.

However, these endpoints return `404` (not `410`) when the issue tracker is disabled — the
404 description explicitly says: "The specified repository does not exist or does not have
the issue tracker enabled."

The issue tracker still exists as a feature for repositories that have it enabled. The
`deprecated: true` flag in the spec appears to reflect Atlassian's long-term plan to migrate
away from the built-in issue tracker (in favour of Jira), not an imminent removal.

**Assessment: NOT A 410 CANDIDATE**

No 410 should be added here. The `deprecated: true` in the spec is a forward-looking signal,
not evidence of a 410-returning endpoint. The API still returns 200 for repos with the issue
tracker enabled and 404 for repos without it.

---

## Group 5: `/snippets/{workspace}` GET — LOW PRIORITY

`GET /snippets/{workspace}` currently documents `200, 404` but not `410`.

`GET /snippets` (the root) already has `410` (added in BUG-SCHEMA-018).
`GET /snippets/{workspace}/{encoded_id}` already has `410`.

But `GET /snippets/{workspace}` (list snippets for a workspace) is missing `410`.
If snippets are plan-restricted for the workspace, this endpoint may also return 410.

**Live verification (2026-05-17):**

```bash
# GET /snippets (root, no workspace) — returns 410
curl -u "$BB_EMAIL:$BB_TOKEN" "https://api.bitbucket.org/2.0/snippets"
# → HTTP 410
# {"type":"error","error":{"message":"CHANGE-2770 - Functionality has been deprecated","detail":"Please read the changelog entry for more details.",...}}

# GET /snippets/{workspace} — returns 200 with error string in values[] (Free plan)
curl -u "$BB_EMAIL:$BB_TOKEN" "https://api.bitbucket.org/2.0/snippets/beaverish"
# → HTTP 200
# {"values":["A workspace on a Free plan does not support snippets..."],"pagelen":30,"page":1}
```

**Assessment: CONFIRMED — `GET /snippets/{workspace}` does NOT return 410; no 410 to add here**

The workspace-scoped endpoint returns `200` (with an error string embedded in values[] on Free
plan — documented in BUG-SNIPPETS-001). It does NOT return `410`. The `410` on the root
`GET /snippets` is the deprecated global listing endpoint; the workspace-scoped listing is
a different behavior. No `410` should be added to `GET /snippets/{workspace}`.

The spec's current `200, 404` coverage for `GET /snippets/{workspace}` is correct.

---

## Resolution (2026-05-17)

**No 410 responses need to be added to any group in this bug report.**

All investigated groups returned `403` (not `410`) from live API calls:
- `/addon/linkers/**`: JWT-only gate → 403 (not removed)
- `/teams/*/pipelines_config/variables`: OAuth-token-only gate → 403 (not removed)
- `/users/*/pipelines_config/variables`: OAuth-token-only gate → 403 (not removed)
- `GET /snippets/{workspace}`: Returns 200 (with error string in values[] for Free plan)

Despite the stated removal dates passing, none of these endpoints actually return `410 Gone`.
The existing spec responses for each group are correct. No spec changes are needed from this
investigation.

---

## Summary Table (Updated 2026-05-17)

| Group | Paths | Operations | Priority | Assessment |
|---|---|---|---|---|
| `/addon/linkers/**` | 5 | 8 | HIGH | CLOSED — Returns 403 (JWT-only), not 410. Not removed. |
| `/teams/*/pipelines_config/variables` | 2 | 5 | MEDIUM | CLOSED — Returns 403 (OAuth-only), not 410. Not removed. |
| `/users/*/pipelines_config/variables` | 2 | 5 | MEDIUM | CLOSED — Returns 403 (OAuth-only), not 410. Not removed. |
| Issue tracker, milestones, components, versions | 19 | 33 | LOW | NOT A 410 CANDIDATE (404 is correct behavior) |
| `GET /snippets/{workspace}` | 1 | 1 | LOW | CLOSED — Returns 200 (Free plan error in values[]), not 410. |
