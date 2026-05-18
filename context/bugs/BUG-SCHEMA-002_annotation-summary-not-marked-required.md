# BUG-SCHEMA-002: `report_annotation` — `summary` required by API but not marked required in spec

**Status:** FIXED — added `required: ["summary"]` to the allOf properties entry of `report_annotation`. Regenerated 2026-05-16.
**Model:** `report_annotation` (allOf)
**Endpoint:** `PUT /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations/{annotationId}`
**Layer:** spec (request body schema missing required constraint)
**Severity:** High — SDK users following spec won't know summary is mandatory; calls fail with 400

## Symptom

Creating an annotation without `summary` returns HTTP 400:
```json
{"key": "report-service.general.bad-request", "message": "Cannot build Annotation, some of required attributes are not set [summary]", "arguments": {}}
```

## Spec evidence

```bash
jq '.components.schemas.report_annotation.allOf[] | .required // "NO REQUIRED"' bb_cloud_fixed.openapi.json
# → "NO REQUIRED"
# → "NO REQUIRED"
```

`summary` appears in `allOf[1].properties` but **no `required` array exists** in either allOf part.

```bash
jq '[.components.schemas.report_annotation.allOf[] | .properties // {} | keys[]] | flatten | unique | sort' bb_cloud_fixed.openapi.json
# → ["annotation_type","created_on","details","external_id","line","link","path","result","severity","summary","updated_on","uuid"]
```

`summary` IS listed as a property, just not as required.

## Live API confirmation (curl)

```bash
# Without summary → 400
curl -s -w "\nHTTP_STATUS: %{http_code}\n" -X PUT \
  -H "Authorization: Basic $AUTH" -H "Content-Type: application/json" \
  ".../annotations/ann-001" \
  -d '{"type":"report_annotation","title":"test","annotation_type":"VULNERABILITY","severity":"LOW","path":"greet.py","line":1}'
# HTTP_STATUS: 400 — "Cannot build Annotation, some of required attributes are not set [summary]"

# With summary → 200
curl -s -w "\nHTTP_STATUS: %{http_code}\n" -X PUT \
  -H "Authorization: Basic $AUTH" -H "Content-Type: application/json" \
  ".../annotations/ann-001" \
  -d '{"type":"report_annotation","title":"test","summary":"description","annotation_type":"VULNERABILITY","severity":"LOW","path":"greet.py","line":1}'
# HTTP_STATUS: 200 ✓
```

## Fix recommendation

Add `required` to the second allOf entry (the one with `properties`) in `report_annotation`:

```bash
jq '(.components.schemas.report_annotation.allOf[] | select(.properties != null)).required = ["summary"]' \
  bb_cloud_fixed.openapi.json > /tmp/fixed.json && mv /tmp/fixed.json bb_cloud_fixed.openapi.json
make generate-cloud && make diff-cloud
```

The SDK test file should be updated to always pass `summary` when creating annotations.
