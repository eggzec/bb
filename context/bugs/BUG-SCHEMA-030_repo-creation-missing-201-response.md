# BUG-SCHEMA-030: `POST /repositories/{workspace}/{repo_slug}` — missing 201 response code

**Status:** FIXED
**Layer:** spec (`bb_cloud_fixed.openapi.json`)
**Endpoint:** `POST /repositories/{workspace}/{repo_slug}`
**SDK function:** `bb.cloud.sdk.repos.create`
**Severity:** High — every successful repository creation returned `None` from the SDK wrapper instead of the created `Repository` object

---

## Description

The OpenAPI spec for repository creation (`POST /repositories/{workspace}/{repo_slug}`) only documented a `200 OK` success response. The live Bitbucket Cloud API returns **`201 Created`** on successful repository creation, not `200`. Because the generated `_parse_response()` had no branch for status code `201`, `response.parsed` was always `None` for successful calls, causing the SDK `repos.create()` wrapper to silently return `None` on every real creation.

---

## Spec Evidence

Before the fix, the documented response codes for this endpoint were:

```bash
jq '.paths["/repositories/{workspace}/{repo_slug}"].post.responses | keys' bb_cloud_fixed.openapi.json
# → ["200", "400", "401", "403"]   ← no 201
```

After the fix:

```bash
jq '.paths["/repositories/{workspace}/{repo_slug}"].post.responses | keys' bb_cloud_fixed.openapi.json
# → ["200", "201", "400", "401", "403"]
```

The added `201` response uses the same `repository` schema as the existing `200`:

```bash
jq '.paths["/repositories/{workspace}/{repo_slug}"].post.responses["201"]' bb_cloud_fixed.openapi.json
# {
#   "description": "A new repository has been created.",
#   "content": {
#     "application/json": {
#       "schema": { "$ref": "#/components/schemas/repository" }
#     }
#   }
# }
```

---

## Impact (Before Fix)

The generated `_parse_response()` for this endpoint had no `elif response.status_code == 201` branch. When the live API returned `201`, `_parse_response()` fell through to the bottom and returned `None`. The `asyncio()` shorthand therefore returned `None` on every successful creation.

The SDK wrapper `repos.create()` checks `isinstance(result, (Repository, Error))` before returning:

```python
result = await post_repositories_workspace_repo_slug.asyncio(
    workspace, repo_slug, client=client.auth, body=body
)
if isinstance(result, (Repository, Error)):
    return result
return None
```

Since `result` was always `None` (201 not parsed), the wrapper always reached `return None`. The repository was created on the server, but the caller received no confirmation and no `Repository` object.

---

## Fix Applied

### 1. Spec patch (`bb_cloud_fixed.openapi.json`)

Added a `201` response entry under `.paths["/repositories/{workspace}/{repo_slug}"].post.responses` referencing the existing `repository` schema with description "A new repository has been created."

### 2. Regeneration

After the spec was patched, `make generate-cloud` regenerated `src/bb/cloud/api/repositories/post_repositories_workspace_repo_slug.py`. The updated `_parse_response()` now includes a `201` branch (with the content-type guard from the BUG-GENERATOR-001 template fix):

```python
if response.status_code == 201:
    if "application/json" not in response.headers.get("content-type", ""):
        return None
    response_201 = Repository.from_dict(response.json())
    return response_201
```

This was confirmed via `make diff-cloud`, which showed the new `201` branch in the generated output.

### 3. SDK wrapper unchanged

No change to `src/bb/cloud/sdk/repos.py` was required. The `isinstance(result, (Repository, Error))` guard already handled any `Repository` return value correctly; once `_parse_response()` returned a `Repository` for 201 responses, the wrapper propagated it transparently.

---

## Files Changed

| File | Change |
|---|---|
| `bb_cloud_fixed.openapi.json` | Added `201` response to `POST /repositories/{workspace}/{repo_slug}` |
| `src/bb/cloud/api/repositories/post_repositories_workspace_repo_slug.py` | Regenerated — new `201` branch in `_parse_response()` |

Fix introduced in commit `e2c891a` (add 201 status support for repo creation endpoint).

---

## Notes

The `200` response remains in the spec to preserve backwards compatibility with any environments or spec parsers that rely on it, even though the live Bitbucket Cloud API exclusively returns `201`. The SDK wrapper handles both codes correctly after the fix.
