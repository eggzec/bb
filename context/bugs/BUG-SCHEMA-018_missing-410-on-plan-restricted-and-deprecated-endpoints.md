# BUG-SCHEMA-018: Missing 410 response on `/snippets`, `/workspaces`, and `/user/permissions/*` endpoints

**Status:** FIXED
**Root cause:** spec — four endpoints missing `410 Gone` response; live API returns 410 for plan-restricted or deprecated operations
**Layer:** spec
**Detected by:** schemathesis — "Undocumented HTTP status code" (Received: 410, Documented: 200/401/403/404)

---

## Affected endpoints

| Endpoint | Documented responses | Also returns |
|---|---|---|
| `GET /snippets` | 200, 404 | **410** |
| `GET /workspaces` | 200, 401 | **410** |
| `GET /user/permissions/repositories` | 200, 403 | **410** |
| `GET /user/permissions/workspaces` | 200, 401, 403 | **410** |

---

## Description

All four endpoints return `HTTP 410 Gone` under certain conditions:

- **`GET /snippets`**: Snippets are not available on the Bitbucket Cloud Free plan. The API returns 410 rather than 402 (unlike downloads which return 402). Note: BUG-SNIPPETS-001 previously documented a 200-with-error-strings behavior on a different plan level; 410 is the response for a workspace where snippets are fully disabled.

- **`GET /user/permissions/repositories`** and **`GET /user/permissions/workspaces`**: These endpoints appear to have been deprecated by Bitbucket Cloud in favor of workspace-scoped permission endpoints (`/workspaces/{workspace}/permissions/repositories`). They return 410 Gone, indicating the resource is permanently unavailable.

- **`GET /workspaces`**: Returns 410 in certain plan or workspace configurations. The specific trigger is unclear but consistently reproduced across schemathesis runs with authenticated credentials.

All four endpoints have no path parameters, so these 410 responses are confirmed with real credentials (not random-path-param noise).

---

## Evidence

Schemathesis output (each with real credentials, no `0` params):

```
GET /snippets
- Undocumented HTTP status code
  Received: 410
  Documented: 200

GET /workspaces
- Undocumented HTTP status code
  Received: 410
  Documented: 200

GET /user/permissions/repositories
- Undocumented HTTP status code
  Received: 410
  Documented: 200

GET /user/permissions/workspaces
- Undocumented HTTP status code
  Received: 410
  Documented: 200
```

---

## Fix Applied

Added `410 Gone` response to all four endpoints in `bb_cloud_fixed.openapi.json`:

```bash
_410='{"description":"Gone — this endpoint is not available on the current plan or has been deprecated.","content":{"application/json":{"schema":{"$ref":"#/components/schemas/error"}}}}'

jq --argjson r410 "$_410" '
  .paths["/snippets"].get.responses["410"] = $r410 |
  .paths["/workspaces"].get.responses["410"] = $r410 |
  .paths["/user/permissions/repositories"].get.responses["410"] = $r410 |
  .paths["/user/permissions/workspaces"].get.responses["410"] = $r410
' bb_cloud_fixed.openapi.json > /tmp/fixed.json && mv /tmp/fixed.json bb_cloud_fixed.openapi.json
```

After regeneration, the generated `_parse_response()` for each endpoint now maps 410 → `Error`.

---

## SDK impact

The generated `asyncio()` for these endpoints now returns an `Error` model (rather than `None`) when the API returns 410, allowing SDK callers to detect and handle plan-restriction or deprecation responses.

---

## Status

- [x] Confirmed via schemathesis (no path params → real credential response)
- [x] Fixed in `bb_cloud_fixed.openapi.json`
- [x] Regenerated: `make generate-cloud && make diff-cloud`
