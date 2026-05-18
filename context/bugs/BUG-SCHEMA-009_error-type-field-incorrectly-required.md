# BUG-SCHEMA-009: `error` schema — `type` in `required` array but Bitbucket 404 responses omit it

**Status:** FIXED
**Model:** `error` (components/schemas)
**Endpoint:** Any endpoint that returns an `error` schema on 4xx (most endpoints)
**Layer:** spec (schema — field marked required that API does not always send)
**Severity:** High — any endpoint returning a 404 Error crashed during deserialization

## Symptom

SDK calls to endpoints with non-existent resources (404 responses) raised:

```
KeyError: 'type'
```

The crash occurred inside the generated `Error.from_dict()`. The generator emits
`data["type"]` (not `data.get("type")`) for fields listed in `required`, so when the
live API omits `type` from a 404 error body, `from_dict` throws `KeyError`.

Example 404 error body returned by Bitbucket:

```json
{
  "error": {
    "message": "Repository beaverish/nonexistent not found."
  }
}
```

No `"type"` key is present. The spec's `required: ["type"]` forced the generator to assume
it would always be there.

## Spec evidence

```bash
jq '.components.schemas.error.required' bb_cloud_fixed.openapi.json
# Before fix → ["type"]
# After fix  → []
```

## Impact

- Every endpoint whose 404 response body is an `Error` object crashed rather than
  returning a usable error — this covers the vast majority of resource-scoped endpoints
  (repos, PRs, commits, branches, tags, etc.)
- Error handling path was completely broken

## Fix applied (2026-05-16)

Cleared the `required` array on the `error` schema so `type` is treated as optional:

```bash
jq '.components.schemas.error.required = []' \
  bb_cloud_fixed.openapi.json > /tmp/fixed.json && mv /tmp/fixed.json bb_cloud_fixed.openapi.json
make generate-cloud && make diff-cloud
```

Fix confirmed: generated `Error.from_dict()` now uses `data.get("type")` (optional access)
instead of `data["type"]` (required access).
