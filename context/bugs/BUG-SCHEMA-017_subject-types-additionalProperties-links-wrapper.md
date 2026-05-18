# BUG-SCHEMA-017: `subject_types` schema uses `additionalProperties: false` but live API returns a `links` wrapper

**Status:** FIXED
**Root cause:** spec — `subject_types.properties.repository` and `.workspace` had `additionalProperties: false` with `events` as a direct property; live API wraps it inside a `links` object
**Layer:** spec
**Detected by:** schemathesis `GET /hook_events` → "Additional properties are not allowed ('links' was unexpected)"

---

## Affected schema
- `components/schemas/subject_types/properties/repository`
- `components/schemas/subject_types/properties/workspace`

---

## Description

The `GET /hook_events` endpoint returns a `subject_types` object describing the available webhook event types. Each subject type (e.g., `repository`, `workspace`) has a `links` field with an `events` link inside it. The spec modelled these sub-schemas with `events` directly on the object and `additionalProperties: false`, which rejects the `links` wrapper the live API actually returns.

---

## Evidence

**Spec before fix** (`components/schemas/subject_types/properties/repository`):

```json
{
  "type": "object",
  "properties": {
    "events": { "$ref": "#/components/schemas/link" }
  },
  "additionalProperties": false
}
```

**Live API response** (from schemathesis capture):

```json
{
  "repository": {
    "links": {
      "events": { "href": "https://api.bitbucket.org/2.0/hook_events/repository" }
    }
  },
  "workspace": {
    "links": {
      "events": { "href": "https://api.bitbucket.org/2.0/hook_events/workspace" }
    }
  }
}
```

The `events` link is nested inside `links`, not at the top level. The `additionalProperties: false` constraint caused schemathesis to report 2 violations (one for `repository`, one for `workspace`):

```
Additional properties are not allowed ('links' was unexpected)
```

**Spec after fix:**

```json
{
  "type": "object",
  "properties": {
    "links": {
      "type": "object",
      "properties": {
        "events": { "$ref": "#/components/schemas/link" }
      }
    }
  }
}
```

Both `additionalProperties: false` constraints removed; `events` moved under `links`.

---

## jq fix command

```bash
jq '
  .components.schemas.subject_types.properties.repository = {
    "type": "object",
    "properties": {
      "links": {
        "type": "object",
        "properties": {
          "events": {"$ref": "#/components/schemas/link"}
        }
      }
    }
  } |
  .components.schemas.subject_types.properties.workspace = {
    "type": "object",
    "properties": {
      "links": {
        "type": "object",
        "properties": {
          "events": {"$ref": "#/components/schemas/link"}
        }
      }
    }
  }
' bb_cloud_fixed.openapi.json > /tmp/fixed.json && mv /tmp/fixed.json bb_cloud_fixed.openapi.json
```

---

## Impact

Any code that accessed `subject_types.repository.events` (direct property) would fail because the actual structure is `subject_types.repository.links.events`. The `additionalProperties: false` constraint also caused strict JSON schema validators (including schemathesis) to reject valid 200 responses from `GET /hook_events`.

---

## Status

- [x] Confirmed via schemathesis (`GET /hook_events` — no random path params, always reproducible)
- [x] Fixed in `bb_cloud_fixed.openapi.json`
- [x] Regenerated: `make generate-cloud && make diff-cloud`
