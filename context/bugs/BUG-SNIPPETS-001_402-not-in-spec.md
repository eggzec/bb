# BUG-SNIPPETS-001: HTTP 402 not documented for snippets endpoints

**Module:** snippets
**Function:** list, create, create_default, get, update, delete, comments, add_comment,
             get_comment, update_comment, delete_comment, commits, get_commit,
             watch, unwatch, watching, watchers, get_file, get_node, update_node,
             delete_node, get_node_file, diff, patch
**HTTP Status:** 402 (Payment Required) — expected on Free plan
**Tags:** [spec, sdk-wrapper]

## Symptom

On a Bitbucket Cloud Free plan workspace, snippets endpoints return HTTP 402
(Payment Required). The spec documents HTTP 404 for some snippets endpoints, but
does **not** document 402 for any of them.

With `raise_on_unexpected_status=False` (the SDK default), the generated
`_parse_response` receives 402, finds no matching status code, and returns `None`.

For paginated endpoints (`list`, `comments`, `commits`, `watchers`), the paginator
receives `None` on the first page and returns `[]` — silently swallowing the
plan-restriction error.

For single-object endpoints (`get`, `create`, etc.), the SDK returns `None`.

## Expected behavior

The SDK should surface 402 as an `Error` model (so callers know why the call failed),
not silently return `None` or `[]`.

## Actual behavior

- `snippets.list` → `[]` (empty list, not `Error`)
- `snippets.create` → `None`
- `snippets.get` → `None`
- All other snippets functions → `None` or `[]`

Callers have no way to distinguish "no snippets exist" from "snippets require plan upgrade".

## Steps to reproduce (curl)

```bash
curl -u "${BB_EMAIL}:${BB_TOKEN}" \
  https://api.bitbucket.org/2.0/snippets/beaverish
# Returns HTTP 402 with JSON error body:
# {"type": "error", "error": {"message": "Snippets require Bitbucket Standard or Premium."}}
```

## Fix recommendation

Add 402 to the OpenAPI spec for all snippets endpoints:

```json
"responses": {
  "402": {
    "description": "Payment Required — snippets require Standard or Premium plan.",
    "content": {
      "application/json": {
        "schema": { "$ref": "#/components/schemas/error" }
      }
    }
  }
}
```

Then regenerate (`make generate-cloud && make diff-cloud`) so the generated
`_parse_response` maps 402 → `Error.from_dict(response.json())`.

After the fix:
- `snippets.list` will return `Error` (not `[]`) on Free plan
- `snippets.create` will return `Error` (not `None`) on Free plan
- All other snippets functions will return `Error` (not `None`) on Free plan

This allows callers to distinguish plan restrictions from genuine empty results.

## Curl confirmation (2026-05-15)

**PARTIAL REFUTE + NEW FINDING:**

```bash
curl -s -w "\nHTTP_STATUS: %{http_code}\n" -H "Authorization: Basic $AUTH" \
  "https://api.bitbucket.org/2.0/snippets/beaverish"
# → HTTP_STATUS: 200
# Body: {"values":["A workspace on a Free plan does not support snippets. Upgrade to..."],"pagelen":30,"page":1}
```

The snippets LIST endpoint returns **HTTP 200** with the error message embedded as a string inside the `values` array — NOT `402`. This is an API quirk distinct from downloads.

Actual behavior revision:
- `snippets.list` → returns a list containing a string `["error message"]` instead of snippet objects
- The paginator would iterate over these strings, causing type confusion downstream
- The SDK model expects `Snippet` objects but gets string items — likely to cause `AttributeError`

The spec documents `200` for snippets list with `values` as an array of snippet objects.
The live API returns `200` with `values` as an array of error strings.
This is a **live API behavior inconsistency** — the API should return a different schema (error vs snippet list) on plan-restricted workspaces.

**Status: PARTIALLY CONFIRMED** — snippets don't return 402, they return 200 with error strings in values[]. The spec doesn't document this behavior (no 402, but the 200 schema is also wrong for plan-restricted workspaces). The SDK impact is: `snippets.list` returns garbage data (strings) not an error, making it impossible to reliably detect the plan restriction.

## Resolution (2026-05-17)

**Verdict: Cannot be fixed at the spec level — this is an unfixable Bitbucket API behavior quirk.**

Live verification on 2026-05-17 confirms the endpoint returns `HTTP 200` with `values: ["A workspace on a Free plan does not support snippets. ..."]` — a paginated wrapper containing a plain string instead of snippet objects. The HTTP status is 200, so adding a `402` response to the spec would be inaccurate and would not help the SDK detect this case. The correct approach would be to document the `200` response as potentially containing an error string, but OpenAPI does not support schema union types in `items` in a way that code generators handle gracefully (string-or-object unions generate `Any` types and lose type safety). The only actionable fix is in the SDK wrapper: `snippets.list` should inspect `values[0]` and, if it is a string, treat the list as a plan-restriction error and raise or return an appropriate error object. This is a **Bitbucket API bug** (misusing the paginated 200 envelope to embed an error string) — the spec cannot model it accurately.

## Fix (2026-05-18) — FIXED

**Status: FIXED** (SDK-level fix)

Fixed in `src/bb/cloud/sdk/snippets.py` — `list()` now detects the string-in-values pattern and returns an `Error` instead of passing corrupt data (or silently returning `[]`) to callers.

After `async_paginate` returns the collected items, the wrapper checks `result[0]` before filtering:

```python
if result and isinstance(result[0], str):
    return Error.from_dict({"type": "error", "error": {"message": result[0]}})
```

This converts the Free-plan restriction message into a proper `Error` model so callers can distinguish plan restrictions from genuinely empty snippet lists.
