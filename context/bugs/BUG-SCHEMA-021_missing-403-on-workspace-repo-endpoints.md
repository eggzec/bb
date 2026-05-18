# BUG-SCHEMA-021: 7 workspace-scoped endpoints missing 403 response

**Status:** FIXED
**Root cause:** spec — 7 workspace/snippet-scoped GET endpoints omit `403 Forbidden`; live API returns 403 when the caller lacks access to the workspace (instead of 404, to avoid disclosing workspace existence)
**Layer:** spec
**Detected by:** schemathesis — "Undocumented HTTP status code" (Received: 403)

---

## Affected endpoints

| Endpoint | Currently documented |
|---|---|
| `GET /repositories/{workspace}` | 200, 404, 410 |
| `GET /snippets/{workspace}/{encoded_id}/watchers` | 200, 404 |
| `GET /workspaces/{workspace}` | 200, 404 |
| `GET /workspaces/{workspace}/members` | 200, 400, 401 |
| `GET /workspaces/{workspace}/members/{member}` | 200, 401, 404 |
| `GET /workspaces/{workspace}/projects` | 200, 404 |
| `GET /workspaces/{workspace}/pullrequests/{selected_user}` | 200, 404 |

---

## Description

Bitbucket Cloud returns HTTP 403 Forbidden (not 404) when access to a workspace-scoped resource is denied for the authenticated caller. This is a deliberate security pattern: returning 403 instead of 404 prevents information disclosure (a 404 would reveal that the workspace or resource does not exist). None of these 7 endpoints document the `403` response code in the spec.

**Impact:** The generated `_parse_response()` for each endpoint has no branch for `403`, so it returns `None` instead of an `Error` model. SDK callers receiving `None` cannot distinguish "access denied" from other error conditions.

---

## Evidence

Schemathesis captured (workspace path param → access denied → 403):

```
GET /workspaces/{workspace}
- Undocumented HTTP status code
  Received: 403
  Documented: 200, 404

GET /repositories/{workspace}
- Undocumented HTTP status code
  Received: 403
  Documented: 200, 404, 410

Reproduce with:
  curl -X GET -H 'Authorization: Basic <token>' \
    https://api.bitbucket.org/2.0/workspaces/some-private-workspace
  # → 403 {"type": "error", "error": {"message": "You do not have access to this workspace."}}
```

This pattern is consistent across all 7 endpoints — Bitbucket uses 403 (not 404) to gate access to workspace-scoped resources, hiding workspace existence from unauthorized callers.

---

## Fix Applied

Added `403 Forbidden` response to all 7 endpoints in `bb_cloud_fixed.openapi.json`:

```bash
_403='{"description":"Forbidden — the caller does not have permission to access this resource.","content":{"application/json":{"schema":{"$ref":"#/components/schemas/error"}}}}'
jq --argjson r "$_403" '
  .paths["/repositories/{workspace}"].get.responses["403"] = $r |
  .paths["/snippets/{workspace}/{encoded_id}/watchers"].get.responses["403"] = $r |
  .paths["/workspaces/{workspace}"].get.responses["403"] = $r |
  .paths["/workspaces/{workspace}/members"].get.responses["403"] = $r |
  .paths["/workspaces/{workspace}/members/{member}"].get.responses["403"] = $r |
  .paths["/workspaces/{workspace}/projects"].get.responses["403"] = $r |
  .paths["/workspaces/{workspace}/pullrequests/{selected_user}"].get.responses["403"] = $r
' bb_cloud_fixed.openapi.json > /tmp/fixed.json && mv /tmp/fixed.json bb_cloud_fixed.openapi.json
```

---

## Status

- [x] Confirmed via schemathesis (workspace path params → 403 access-denied response)
- [x] Fixed in `bb_cloud_fixed.openapi.json`
- [x] Regenerated: `make generate-cloud && make diff-cloud`
