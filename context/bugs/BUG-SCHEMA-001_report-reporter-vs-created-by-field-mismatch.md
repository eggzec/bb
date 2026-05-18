# BUG-SCHEMA-001: `report` schema — `reporter` field documented but API returns `created_by`

**Status:** FIXED — renamed `reporter` → `created_by` ($ref account); added `type` field to report allOf properties. Regenerated 2026-05-16.
**Model:** `report` (allOf)
**Endpoint:** `PUT /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}`
**Layer:** spec (response schema uses wrong field name)
**Severity:** High — SDK exposes `.reporter` attribute (None/UNSET) but actual data is in `.created_by`

## Symptom

`reports.create_or_update()` returns a `Report` object. User code accessing `.reporter` gets `None`/`UNSET`
because the live API returns the field as `created_by`, not `reporter`.

## Spec evidence

```bash
jq '[.components.schemas.report.allOf[] | .properties // {} | keys[]] | flatten | unique | sort' bb_cloud_fixed.openapi.json
# → [..., "reporter", ...]  ← spec uses "reporter"
```

Spec `report.allOf[1].properties.reporter` exists; `created_by` does NOT appear in the spec.

## Live API evidence (curl)

```bash
curl -s -X PUT -H "Authorization: Basic $AUTH" -H "Content-Type: application/json" \
  "https://api.bitbucket.org/2.0/repositories/beaverish/bb-probe/commit/84952fad.../reports/test" \
  -d '{"type":"report","title":"t","details":"d","report_type":"TEST","result":"PASSED","link":"https://example.com"}' \
  | jq '[keys[]]'
# → ["created_by", "created_on", "data", "details", "external_id", "link",
#     "remote_link_enabled", "report_type", "reporter", "result", "title",
#     "type", "updated_on", "uuid"]
```

Wait — actual response has BOTH `created_by` (populated Account object) AND `reporter` (missing from actual).
Let me clarify: the actual API response contains:
- `created_by`: Account object (populated)
- `reporter`: NOT returned by the API at all

But the generated `Report` model has a `.reporter` attribute (from spec) and NO `.created_by` attribute.
The actual data is inaccessible through the SDK.

## Fields missing from spec (returned by API but not documented)
| Field | Observed type | Notes |
|-------|---------------|-------|
| `created_by` | Account object | Who created the report — the actual author field |
| `type` | string `"report"` | Standard Bitbucket type discriminator |

## Fields in spec but NOT returned by API
| Field | Notes |
|-------|-------|
| `reporter` | Spec property exists but API does not return this key |
| `logo_url` | Spec property exists but API did not return it in our test |

## Fix recommendation

1. **Rename `reporter` to `created_by`** in `report.allOf[1].properties` in `bb_cloud_fixed.openapi.json`
2. **Add `type` to `report.allOf[1].properties`** as a string
3. Regenerate: `make generate-cloud && make diff-cloud`

Exact jq surgery:
```bash
# Rename reporter → created_by (referencing the account schema)
jq '(.components.schemas.report.allOf[] | select(.properties.reporter != null)).properties.created_by =
    (.components.schemas.report.allOf[] | select(.properties.reporter != null)).properties.reporter |
    del((.components.schemas.report.allOf[] | select(.properties.created_by != null)).properties.reporter)' \
  bb_cloud_fixed.openapi.json > /tmp/fixed.json && mv /tmp/fixed.json bb_cloud_fixed.openapi.json
```
