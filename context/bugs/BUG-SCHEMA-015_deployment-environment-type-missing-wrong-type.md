# BUG-SCHEMA-015: `deployment_environment.environment_type` — field missing from schema; must be object not string

**Status:** FIXED
**Model:** `deployment_environment`
**Endpoint:** `POST /repositories/{workspace}/{repo_slug}/environments`
**Layer:** spec (request/response schema — required field absent; type wrong in initial fix attempt)
**Severity:** High — `create_environment()` always returned 400 "Property environment_type is required"

## Symptom

`deployments.create_environment(name=..., environment_type=...)` returned HTTP 400:

```json
{"error": {"message": "Property environment_type is required."}}
```

Even when the SDK caller passed `environment_type`, the generated request body did not include
the field because `deployment_environment` schema had no `environment_type` property. The field
was silently dropped during serialization.

A secondary bug was exposed during the fix attempt: passing `environment_type` as a plain
string (e.g., `"Test"`) also returned 400. The live API requires an object:
`{"name": "Test"}`, not the string `"Test"`.

## Root cause

Two problems:

1. **Field absent from schema** — `deployment_environment.properties` did not contain
   `environment_type`. The generator therefore produced no parameter for it, and SDK
   callers had no way to set it. (Partially covered by BUG-SCHEMA-007, but that report
   focused on the read/GET side; this bug covers the write/POST side.)

2. **Wrong type assumption** — initial fix attempt added `environment_type` as `{"type": "string"}`.
   The live API rejected this with 400 because `environment_type` must be an object with
   a `name` field (e.g., `{"name": "Test"}`), matching the same structure documented for
   `deployment_environment_type` in the schema.

## Spec evidence

```bash
# Before fix — field entirely missing
jq '.components.schemas.deployment_environment.allOf[] | .properties // {} | keys[]' \
  bb_cloud_fixed.openapi.json
# → ["name", "uuid"] only

# After fix — deployment_environment_type schema added
jq '.components.schemas.deployment_environment_type' bb_cloud_fixed.openapi.json
# → {"type": "object", "properties": {"name": {...}, "rank": {...}}, ...}
```

## Impact

- `deployments.create_environment()` — always returned 400; environment creation was
  completely broken regardless of the parameters supplied
- Even workarounds using the raw generated API layer failed because the schema omission
  meant the field was never serialized into the request body

## Fix applied (2026-05-16)

Three-step fix:

**Step 1** — Added `deployment_environment_type` schema to `components/schemas`:

```bash
jq '.components.schemas.deployment_environment_type = {
  "type": "object",
  "title": "DeploymentEnvironmentType",
  "description": "The type classification for a deployment environment.",
  "properties": {
    "name": {"type": "string", "description": "Human-readable name (e.g. Test, Staging, Production)."},
    "rank": {"type": "integer", "description": "Numeric rank for ordering environment types."}
  }
}' bb_cloud_fixed.openapi.json > /tmp/fixed.json && mv /tmp/fixed.json bb_cloud_fixed.openapi.json
```

**Step 2** — Added `environment_type` property referencing the new schema in `deployment_environment`:

```bash
jq '(
  .components.schemas.deployment_environment.allOf[]
  | select(.properties != null)
  | .properties
) += {
  "environment_type": {"$ref": "#/components/schemas/deployment_environment_type"}
}' bb_cloud_fixed.openapi.json > /tmp/fixed.json && mv /tmp/fixed.json bb_cloud_fixed.openapi.json
```

**Step 3** — Added missing 400 Error response to the create_environment endpoint:

```bash
jq '.paths["/repositories/{workspace}/{repo_slug}/environments"].post.responses["400"] = {
  "description": "Bad Request — required field missing or invalid environment_type.",
  "content": {"application/json": {"schema": {"$ref": "#/components/schemas/error"}}}
}' bb_cloud_fixed.openapi.json > /tmp/fixed.json && mv /tmp/fixed.json bb_cloud_fixed.openapi.json
make generate-cloud && make diff-cloud
```

Fix confirmed: `create_environment(name="staging", environment_type=DeploymentEnvironmentType(name="Staging"))`
now serializes the correct request body and returns HTTP 201.
