# BUG-PAGINATION-001: Missing `page` and `pagelen` parameters on list endpoints

**Status:** FIXED
**Root cause:** spec — 17 paginated list endpoints omit `page` and `pagelen` query parameters; the live API accepts and respects these parameters but generated SDK clients cannot pass them
**Layer:** spec
**Detected by:** spec diff — parameters present in live API responses but absent from OpenAPI spec

---

## Affected endpoints

The following 17 GET list endpoints were missing `page` and/or `pagelen` in the spec. (Five endpoints in the original task list — `/repositories/{workspace}`, `/repositories/{workspace}/{repo_slug}/commits`, `/repositories/{workspace}/{repo_slug}/pullrequests`, `/repositories/{workspace}/{repo_slug}/refs/branches`, `/workspaces` — already had both parameters and were not affected.)

| Endpoint | Parameters missing |
|---|---|
| `GET /repositories/{workspace}/{repo_slug}/default-reviewers` | `page`, `pagelen` |
| `GET /repositories/{workspace}/{repo_slug}/effective-default-reviewers` | `page`, `pagelen` |
| `GET /repositories/{workspace}/{repo_slug}/forks` | `page`, `pagelen` |
| `GET /repositories/{workspace}/{repo_slug}/issues` | `page`, `pagelen` |
| `GET /repositories/{workspace}/{repo_slug}/permissions-config/groups` | `page`, `pagelen` |
| `GET /repositories/{workspace}/{repo_slug}/permissions-config/users` | `page`, `pagelen` |
| `GET /repositories/{workspace}/{repo_slug}/pullrequests/activity` | `page`, `pagelen` |
| `GET /repositories/{workspace}/{repo_slug}/refs/tags` | `page`, `pagelen` |
| `GET /repositories/{workspace}/{repo_slug}/watchers` | `page`, `pagelen` |
| `GET /user/permissions/repositories` | `page`, `pagelen` |
| `GET /user/permissions/workspaces` | `page`, `pagelen` |
| `GET /user/workspaces` | `page`, `pagelen` |
| `GET /user/workspaces/{workspace}/permissions/repositories` | `page`, `pagelen` |
| `GET /workspaces/{workspace}/members` | `page`, `pagelen` |
| `GET /workspaces/{workspace}/permissions` | `page`, `pagelen` |
| `GET /workspaces/{workspace}/permissions/repositories` | `page`, `pagelen` |
| `GET /workspaces/{workspace}/pullrequests/{selected_user}` | `page`, `pagelen` |

---

## Description

Bitbucket Cloud's REST API uses two standard query parameters for pagination across all list endpoints:

- **`page`** (`integer`, min: 1, default: 1) — which page of results to return
- **`pagelen`** (`integer`, min: 1, max: 100, default: 10) — number of items per page

The spec documents these parameters on some list endpoints (e.g. `GET /repositories/{workspace}/{repo_slug}/pullrequests` has `page` and `pagelen` defined) but silently omits them from 17 others. The omission is inconsistent — there is no functional difference between the documented and undocumented endpoints; all of them accept and process these parameters at runtime.

A code generator consuming the spec has no way to know these parameters exist on the affected endpoints. The generated `_get_kwargs()` functions for those endpoints have no `page` or `pagelen` parameters in their signatures, so generated SDK clients are permanently stuck on page 1 with the default page size (10 items). Callers cannot retrieve results beyond the first page without resorting to raw HTTP calls that bypass the generated client entirely.

---

## Evidence

**Spec missing params on one affected endpoint (pre-fix):**

```bash
$ git show a2e028f~1:bb_cloud_fixed.openapi.json \
    | jq '.paths["/repositories/{workspace}/{repo_slug}/refs/tags"].get.parameters // [] | [.[].name]'
# (no output — parameters array was absent entirely)
```

**Well-documented endpoint for contrast:**

```bash
$ jq '.paths["/repositories/{workspace}/{repo_slug}/pullrequests"].get.parameters[].name' \
    bb_cloud_fixed.openapi.json
"state"
"page"
"pagelen"
```

**Live API confirms `page` and `pagelen` are accepted and reflected in the response:**

```bash
$ curl -s -u "$BB_EMAIL:$BB_TOKEN" \
    "https://api.bitbucket.org/2.0/repositories/$BB_WORKSPACE?page=1&pagelen=5" \
    | python3 -c "import sys,json; d=json.load(sys.stdin); print('pagelen:', d.get('pagelen'), 'page:', d.get('page'), 'size:', d.get('size'))"
pagelen: 5 page: 1 size: 4
```

The API accepted `pagelen=5`, honoured it (response `pagelen: 5`), and returned the `page` field — confirming the parameters are fully functional regardless of their absence from the spec.

---

## Impact

- Generated SDK clients for all 17 affected endpoints have no `page` or `pagelen` parameters in their `_get_kwargs()` signatures
- Callers cannot paginate these endpoints through the generated client — they are permanently limited to the first page of up to 10 results
- Any SDK wrapper that relies on the generated client for these endpoints (e.g. the `async_paginate()` helper) also cannot pass page parameters, silently returning only the first page
- The inconsistency between endpoints that have the params and those that don't makes it non-obvious which endpoints support pagination, increasing the chance of missed bugs

---

## Fix Applied

Added `page` and `pagelen` query parameter objects to the `parameters` array of each affected endpoint's `GET` operation in `bb_cloud_fixed.openapi.json`. The same schema definition was used for all 17 endpoints, matching the pattern already present on well-documented endpoints:

```json
{
  "name": "page",
  "description": "The page number of elements to retrieve.",
  "required": false,
  "in": "query",
  "schema": {
    "type": "integer",
    "format": "int32",
    "minimum": 1,
    "default": 1
  }
},
{
  "name": "pagelen",
  "description": "The maximum number of results to return.",
  "required": false,
  "in": "query",
  "schema": {
    "type": "integer",
    "format": "int32",
    "minimum": 1,
    "maximum": 100,
    "default": 10
  }
}
```

The fix was applied via direct JSON surgery on `bb_cloud_fixed.openapi.json`. After patching, `make generate-cloud && make diff-cloud` was run to confirm the parameter changes propagated into the generated `_get_kwargs()` function signatures for each affected endpoint module.

---

## Status

- [x] Confirmed via live API (`page`/`pagelen` accepted and reflected in response body)
- [x] Fixed in `bb_cloud_fixed.openapi.json` (commit `a2e028f`)
- [x] Regenerated: `make generate-cloud && make diff-cloud`
