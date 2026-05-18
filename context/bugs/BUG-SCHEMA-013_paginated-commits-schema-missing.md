# BUG-SCHEMA-013: `paginated_commits` schema missing — PR commits endpoint 200 response has no schema

**Status:** FIXED
**Model:** (none — schema did not exist)
**Endpoint:** `GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/commits`
**Layer:** spec (missing schema + missing 200 response body reference)
**Severity:** Critical — `prs.list_commits()` always returned `None` regardless of PR contents

## Symptom

`prs.list_commits(pull_request_id=<id>)` returned `None` for every call, even on PRs with
many commits. No exception was raised — the generated `sync()` function silently returned
`None` because `_parse_response` had no schema to deserialize into and fell through to
`return None`.

Inspection of the generated module confirmed:

```python
# generated: get_repositories_workspace_repo_slug_pullrequests_pull_request_id_commits.py
def _parse_response(*, client, response):
    if response.status_code == 200:
        return None   # ← no schema → cast(Any, None)
    ...
```

## Root cause

Two problems in the spec:

1. **No `paginated_commits` schema** — there was no component schema for a paginated list
   of commits. The equivalent `paginated_commit` or `paginated_commits` schema that other
   commit endpoints use did not exist for this resource.

2. **No 200 response body reference** — the PR commits endpoint's 200 response entry
   either had no `content` key or no `schema` reference, so the generator produced
   `cast(Any, None)` for the success path.

```bash
jq '.paths["/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/commits"].get.responses["200"]' \
  bb_cloud_fixed.openapi.json
# Before fix → {} or {"description": "..."} with no "content" key
```

## Impact

- `prs.list_commits()` — always returned `None`; commit data was completely inaccessible
- PR diff/commit analysis workflows were non-functional

## Fix applied (2026-05-16)

Two-step fix:

**Step 1** — Added `paginated_commits` schema to `components/schemas`:

```bash
jq '.components.schemas.paginated_commits = {
  "type": "object",
  "title": "Paginated Commits",
  "description": "A paginated list of commits.",
  "properties": {
    "size":     {"type": "integer", "description": "Total number of objects, if known."},
    "page":     {"type": "integer", "description": "Current page number."},
    "pagelen":  {"type": "integer", "description": "Page size."},
    "next":     {"type": "string",  "description": "URL of next page."},
    "previous": {"type": "string",  "description": "URL of previous page."},
    "values":   {
      "type": "array",
      "items": {"$ref": "#/components/schemas/commit"},
      "minItems": 0
    }
  }
}' bb_cloud_fixed.openapi.json > /tmp/fixed.json && mv /tmp/fixed.json bb_cloud_fixed.openapi.json
```

**Step 2** — Wired the schema to the endpoint 200 response:

```bash
jq '.paths["/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/commits"].get.responses["200"] = {
  "description": "The commits for the given pull request.",
  "content": {
    "application/json": {
      "schema": {"$ref": "#/components/schemas/paginated_commits"}
    }
  }
}' bb_cloud_fixed.openapi.json > /tmp/fixed.json && mv /tmp/fixed.json bb_cloud_fixed.openapi.json
make generate-cloud && make diff-cloud
```

Fix confirmed: generated `_parse_response` now deserializes 200 responses into
`PaginatedCommits`, and `prs.list_commits()` returns the correct commit list.
