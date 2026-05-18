# BUG-COMMITS-003: reports.create_annotation may raise UnexpectedStatus if API returns 201

**Module:** reports
**Function:** create_annotation
**Tags:** [spec, generator]

## Symptom

`reports.create_annotation(...)` raises `UnexpectedStatus(201, ...)` instead of returning
a `ReportAnnotation` when creating a new annotation.

The test `test_create_throwaway_annotation` catches this with `pytest.xfail`:

```
reports.create_annotation raised UnexpectedStatus(201) —
likely API returned 201 but generated parser only handles 200.
```

## Initial theory

The Bitbucket Cloud spec documents
`PUT /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations/{annotationId}`
as returning `200 OK`. The generated `_parse_response` in
`src/bb/cloud/api/reports/create_or_update_annotation.py` only handles `status_code == 200`:

```python
if response.status_code == 200:
    response_200 = ReportAnnotation.from_dict(response.json())
    return response_200
```

Same pattern as BUG-COMMITS-002: a *create* (new annotationId) may return `201 Created`
while an *update* (existing annotationId) returns `200 OK`.

## Steps to reproduce (curl)

```bash
ANN_ID="bb-test-ann-$(date +%s)"

# First PUT — creates a new annotation (observe HTTP status):
curl -s -X PUT \
  -H "Authorization: Basic $(echo -n "$BB_EMAIL:$BB_TOKEN" | base64)" \
  -H "Content-Type: application/json" \
  "https://api.bitbucket.org/2.0/repositories/beaverish/bb-probe/commit/84952fad87fb39e3c6d61811a93769378dd4fad7/reports/bb-probe-report/annotations/$ANN_ID" \
  -d '{"type":"report_annotation","annotation_type":"BUG","summary":"test","result":"FAILED","severity":"LOW"}' \
  -w "\nHTTP %{http_code}\n"
```

## Fix recommendation

### Option A (preferred) — patch spec and regenerate

In `bb_cloud_fixed.openapi.json`, add `201` as a response for
`PUT /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations/{annotationId}`:

```bash
jq '.paths["/repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations/{annotationId}"].put.responses["201"] = {"description":"Annotation created","content":{"application/json":{"schema":{"$ref":"#/components/schemas/report_annotation"}}}}' \
  bb_cloud_fixed.openapi.json > /tmp/fixed.json && mv /tmp/fixed.json bb_cloud_fixed.openapi.json
make generate-cloud && make diff-cloud
```

**Status:** REFUTED by curl (2026-05-15).

Annotation PUT always returns `200` for both new and existing annotation IDs.
Spec documents `200` — generator handles `200` — SDK is correct. No status-code fix needed.

HOWEVER: a related real bug was discovered — `summary` is required by the live API but not
marked as required in the spec (see BUG-SCHEMA-002). Without `summary`, annotation creation
returns `400`, not `200` or `201`. Fix BUG-SCHEMA-002 instead.
