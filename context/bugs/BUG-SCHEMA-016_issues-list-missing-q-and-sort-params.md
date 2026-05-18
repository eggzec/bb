# BUG-SCHEMA-016: Issues list endpoint — `q` and `sort` query parameters missing from spec

**Status:** FIXED
**Model:** (query parameters, no model change)
**Endpoint:** `GET /repositories/{workspace}/{repo_slug}/issues`
**Layer:** spec (endpoint parameters array empty — query params undocumented)
**Severity:** Medium — SDK `issues.list(q=..., sort=...)` crashed with TypeError; filtering/sorting was impossible

## Symptom

`issues.list(q='state="open"', sort="updated_on")` raised:

```
TypeError: asyncio() got an unexpected keyword argument 'q'
```

The generated `asyncio()` (and `sync()`) functions had no `q` or `sort` parameters because
the spec's `parameters` array for this endpoint was empty (`[]`). The SDK wrapper correctly
tried to pass these common Bitbucket query parameters, but the generated code rejected them.

## Root cause

The `GET /repositories/{workspace}/{repo_slug}/issues` endpoint in the spec had its
`parameters` array set to `[]`, omitting the `q` (JQL-style query filter) and `sort`
(field to sort by) query parameters that Bitbucket's live API accepts and documents in
its user-facing docs.

```bash
jq '.paths["/repositories/{workspace}/{repo_slug}/issues"].get.parameters' \
  bb_cloud_fixed.openapi.json
# Before fix → [] (empty — only path params inherited from path level, no query params)
# After fix  → [{name: "q", in: "query", ...}, {name: "sort", in: "query", ...}]
```

Both parameters are standard across Bitbucket list endpoints (branches, commits, PRs, etc.
all support `q` and `sort`). Their absence from the issues endpoint was an oversight in
the spec.

## Impact

- `issues.list(q=...)` — `TypeError` crash; impossible to filter issues by state, assignee, etc.
- `issues.list(sort=...)` — same crash; impossible to control result ordering
- Issue search and triage workflows were non-functional at the SDK level

## Fix applied (2026-05-16)

Added `q` and `sort` as optional query parameters to the issues list endpoint:

```bash
jq '.paths["/repositories/{workspace}/{repo_slug}/issues"].get.parameters += [
  {
    "name": "q",
    "in": "query",
    "required": false,
    "description": "Query string to filter issues. Uses Bitbucket query syntax (e.g. state=\"open\" AND priority=\"major\").",
    "schema": {"type": "string"}
  },
  {
    "name": "sort",
    "in": "query",
    "required": false,
    "description": "Field to sort results by (e.g. \"updated_on\", \"created_on\", \"priority\").",
    "schema": {"type": "string"}
  }
]' bb_cloud_fixed.openapi.json > /tmp/fixed.json && mv /tmp/fixed.json bb_cloud_fixed.openapi.json
make generate-cloud && make diff-cloud
```

Fix confirmed: generated `sync()` and `asyncio()` now accept `q: Union[Unset, str]` and
`sort: Union[Unset, str]` keyword arguments, and `issues.list(q='state="open"')` works correctly.
