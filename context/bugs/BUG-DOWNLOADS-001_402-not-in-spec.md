# BUG-DOWNLOADS-001: HTTP 402 not documented for downloads endpoints

**Module:** downloads
**Function:** list, get, upload, delete
**HTTP Status:** 402 (Payment Required) — expected on Free plan
**Tags:** [spec, sdk-wrapper]

## Symptom

On a Bitbucket Cloud Free plan workspace, all downloads endpoints return
HTTP 402 (Payment Required) with body:

```json
{
  "type": "error",
  "error": {
    "message": "Repository downloads require Bitbucket Standard or Premium."
  }
}
```

The generated `_parse_response` for `get_repositories_workspace_repo_slug_downloads`
handles 200 and 403, but does **not** handle 402. With `raise_on_unexpected_status=False`
(the SDK default), the 402 falls through to `return None`.

## Expected behavior

The SDK should either:
1. Return an `Error` model with the 402 message (preferred — caller can inspect it), OR
2. Raise `UnexpectedStatus(402)` (acceptable if documented as such)

Instead, `downloads.list` returns `[]` (empty list) because the paginator treats
the `None` first-page response as an empty result set. The caller cannot
distinguish "no downloads exist" from "downloads are plan-restricted".

## Actual behavior

- `downloads.list` returns `[]` (silently, no Error)
- `downloads.get` returns `None` (silently)
- `downloads.delete` returns `None` (silently)

## Steps to reproduce (curl)

```bash
curl -u "${BB_EMAIL}:${BB_TOKEN}" \
  https://api.bitbucket.org/2.0/repositories/beaverish/bb-probe/downloads
# Returns HTTP 402 with JSON error body
```

## Fix recommendation

Add 402 to the OpenAPI spec for all four downloads endpoints:

```json
"responses": {
  "402": {
    "description": "Payment Required — repository downloads require Standard or Premium plan.",
    "content": {
      "application/json": {
        "schema": { "$ref": "#/components/schemas/error" }
      }
    }
  }
}
```

Then regenerate (`make generate-cloud && make diff-cloud`) so that the generated
`_parse_response` maps 402 → `Error.from_dict(response.json())`.

After the fix, `downloads.list` will return `Error` instead of `[]` on Free plan,
allowing callers to detect the plan restriction.

## Curl confirmation (2026-05-15)

```bash
curl -s -w "\nHTTP_STATUS: %{http_code}\n" -H "Authorization: Basic $AUTH" \
  "https://api.bitbucket.org/2.0/repositories/beaverish/bb-probe/downloads"
# → "A workspace on a Free plan does not support uploading or downloading files..."
# → HTTP_STATUS: 402

jq '[.paths | to_entries[] | .value | to_entries[] | select(.key | test("^(get|post|put|delete)$")) | .value.responses | to_entries[] | select(.key == "402") | {path: "found"}] | length' bb_cloud_fixed.openapi.json
# → 4 (but those 4 are permission endpoints, NOT downloads)
```

**Status: CONFIRMED** — downloads endpoints return 402 but spec only documents 200/403 for GET and 201/400/403/406 for POST. 402 appears nowhere near downloads in the spec. Fix is to add 402 response to all downloads path operations.
