# BUG-COMMITS-002: reports.create_or_update may raise UnexpectedStatus if API returns 201

**Module:** reports
**Function:** create_or_update
**Tags:** [spec, generator]

## Symptom

`reports.create_or_update(...)` raises `UnexpectedStatus(201, ...)` instead of returning
a `Report` object when creating a new report.

The test `test_create_throwaway_report` catches this with `pytest.xfail`:

```
reports.create_or_update raised UnexpectedStatus(201) —
likely API returned 201 but generated parser only handles 200.
```

## Initial theory

The Bitbucket Cloud spec documents `PUT /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}`
as returning `200 OK`. The generated `_parse_response` in
`src/bb/cloud/api/reports/create_or_update_report.py` only handles `status_code == 200`:

```python
if response.status_code == 200:
    response_200 = Report.from_dict(response.json())
    return response_200
```

However, for a true *create* (report_id does not yet exist), the Bitbucket REST API
may return `201 Created` instead of `200 OK`. This causes `_parse_response` to fall
through to `raise errors.UnexpectedStatus(response.status_code, response.content)`.

The SDK wrapper does not catch `UnexpectedStatus`, so it propagates to the test.

Note: *update* (report_id already exists) likely returns `200` and works fine.

## Steps to reproduce (curl)

```bash
REPORT_ID="bb-test-report-$(date +%s)"

# First PUT — creates a new report (observe HTTP status):
curl -s -X PUT \
  -H "Authorization: Basic $(echo -n "$BB_EMAIL:$BB_TOKEN" | base64)" \
  -H "Content-Type: application/json" \
  "https://api.bitbucket.org/2.0/repositories/beaverish/bb-probe/commit/84952fad87fb39e3c6d61811a93769378dd4fad7/reports/$REPORT_ID" \
  -d '{"type":"report","title":"test","report_type":"TEST","result":"PENDING","reporter":"test"}' \
  -w "\nHTTP %{http_code}\n"

# Second PUT — updates existing report (should return 200):
curl -s -X PUT \
  -H "Authorization: Basic $(echo -n "$BB_EMAIL:$BB_TOKEN" | base64)" \
  -H "Content-Type: application/json" \
  "https://api.bitbucket.org/2.0/repositories/beaverish/bb-probe/commit/84952fad87fb39e3c6d61811a93769378dd4fad7/reports/$REPORT_ID" \
  -d '{"type":"report","title":"test","report_type":"TEST","result":"PASSED","reporter":"test"}' \
  -w "\nHTTP %{http_code}\n"
```

## Fix recommendation

### Option A (preferred) — patch spec and regenerate

In `bb_cloud_fixed.openapi.json`, add `201` as a response for
`PUT /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}`:

```bash
jq '.paths["/repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}"].put.responses["201"] = {"description":"Report created","content":{"application/json":{"schema":{"$ref":"#/components/schemas/report"}}}}' \
  bb_cloud_fixed.openapi.json > /tmp/fixed.json && mv /tmp/fixed.json bb_cloud_fixed.openapi.json
make generate-cloud && make diff-cloud
```

### Option B — SDK-level workaround

Use `asyncio_detailed()` directly and check both `200` and `201` status codes.
Not recommended; it leaks the generated layer into the SDK.

**Status:** REFUTED by curl (2026-05-15).

Bitbucket Code Insights PUT always returns `200` regardless of whether the report is new or existing.
Spec documents `200` — generator handles `200` — SDK is correct. No fix needed.

Note: The original curl test with minimal body returned `400` ("required attributes not set [details]") —
the spec's `report_annotation` body constraints are incompletely documented (see BUG-SCHEMA-002 for the
related annotation `summary` issue). The report itself requires: `type`, `title`, `details`, `report_type`,
`result`, `link` — none marked as required in the spec.
