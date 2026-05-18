# BUG-SCHEMA-019: `GET /addon/linkers` missing 403 response — returns 403 for non-Connect-app callers

**Status:** FIXED
**Root cause:** spec — `GET /addon/linkers` only documents 200 and 401; live API returns 403 for standard API callers who are not Bitbucket Connect apps
**Layer:** spec
**Detected by:** schemathesis — "Undocumented HTTP status code" (Received: 403, Documented: 200, 401)

---

## Affected endpoint
- `GET /addon/linkers`

---

## Description

The `GET /addon/linkers` endpoint is part of the Bitbucket Connect add-on API. It lists the Bitbucket Connect linker objects for the currently authenticated add-on. Standard Bitbucket API callers (API token, OAuth, app password) that are not acting as a Bitbucket Connect add-on receive HTTP 403 Forbidden instead of the documented 200 OK response.

The endpoint has no path parameters, so the 403 is confirmed with real credentials (not random-path-param noise from schemathesis).

---

## Evidence

Schemathesis output:

```
GET /addon/linkers
- Undocumented HTTP status code
  Received: 403
  Documented: 200

Reproduce with:
  curl -X GET -H 'Authorization: [Filtered]' https://api.bitbucket.org/2.0/addon/linkers
```

Current spec for this endpoint:

```bash
jq '.paths["/addon/linkers"].get.responses | keys' bb_cloud_fixed.openapi.json
# → ["200", "401"]
```

---

## Fix Applied

Added `403 Forbidden` response to `GET /addon/linkers` in `bb_cloud_fixed.openapi.json`:

```bash
_403='{"description":"Forbidden — the caller does not have permission to access this resource.","content":{"application/json":{"schema":{"$ref":"#/components/schemas/error"}}}}'

jq --argjson r403 "$_403" '
  .paths["/addon/linkers"].get.responses["403"] = $r403
' bb_cloud_fixed.openapi.json > /tmp/fixed.json && mv /tmp/fixed.json bb_cloud_fixed.openapi.json
```

---

## Status

- [x] Confirmed via schemathesis (no path params → real credential response)
- [x] Fixed in `bb_cloud_fixed.openapi.json`
- [x] Regenerated: `make generate-cloud && make diff-cloud`
