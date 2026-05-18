# BUG-SCHEMA-022: 3 workspace-scoped endpoints missing 404 response

**Status:** FIXED
**Root cause:** spec — 3 workspace-scoped GET endpoints omit `404 Not Found`; live API returns 404 when workspace does not exist
**Layer:** spec
**Detected by:** schemathesis — "Undocumented HTTP status code" (Received: 404)

---

## Affected endpoints

| Endpoint | Currently documented |
|---|---|
| `GET /workspaces/{workspace}/permissions/repositories/{repo_slug}` | 200, 403 |
| `GET /workspaces/{workspace}/pipelines-config/runners` | 200, 403 |
| `GET /workspaces/{workspace}/pipelines-config/variables` | 200, 403 |

---

## Description

Schemathesis uses `workspace=0` which hits a nonexistent workspace, causing the Bitbucket Cloud API to return HTTP 404. These 3 endpoints only document 200 and 403 — `404` is absent. These were missed by BUG-SCHEMA-021 (which fixed 403 on workspace endpoints) because BUG-SCHEMA-021 focused on endpoints already documented with 404 that also needed 403; these 3 endpoints need 404 added.

---

## Evidence

Schemathesis output:

```
GET /workspaces/{workspace}/permissions/repositories/{repo_slug}
- Undocumented HTTP status code
  Received: 404
  Documented: 200, 403

GET /workspaces/{workspace}/pipelines-config/runners
- Undocumented HTTP status code
  Received: 404
  Documented: 200, 403

GET /workspaces/{workspace}/pipelines-config/variables
- Undocumented HTTP status code
  Received: 404
  Documented: 200, 403
```

---

## Fix Applied

```bash
_404='{"description":"Not Found — the workspace or resource does not exist.","content":{"application/json":{"schema":{"$ref":"#/components/schemas/error"}}}}'
jq --argjson r "$_404" '
  .paths["/workspaces/{workspace}/permissions/repositories/{repo_slug}"].get.responses["404"] = $r |
  .paths["/workspaces/{workspace}/pipelines-config/runners"].get.responses["404"] = $r |
  .paths["/workspaces/{workspace}/pipelines-config/variables"].get.responses["404"] = $r
' bb_cloud_fixed.openapi.json > /tmp/fixed.json && mv /tmp/fixed.json bb_cloud_fixed.openapi.json
```

---

## Status

- [x] Confirmed via schemathesis (workspace=0 → nonexistent → 404)
- [x] Fixed in `bb_cloud_fixed.openapi.json`
- [x] Regenerated: `make generate-cloud && make diff-cloud`
