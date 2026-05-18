# BUG-SCHEMA-004: `commitstatus` schema — `commit`, `repository`, `refname` fields missing from spec allOf

**Status:** FIXED — added `commit` ($ref commit), `repository` ($ref repository), `type` (string) to `commitstatus` allOf properties entry. Regenerated 2026-05-16.
**Model:** `commitstatus` (allOf)
**Endpoint:** `GET /repositories/{workspace}/{repo_slug}/commit/{commit}/statuses/build/{key}`
**Layer:** spec (response schema incomplete)
**Severity:** Medium — commit and repository navigation data returned by API is inaccessible through SDK model

## Spec evidence

```bash
jq '[.components.schemas.commitstatus.allOf[] | .properties // {} | keys[]] | flatten | unique | sort' bb_cloud_fixed.openapi.json
# → ["created_on", "description", "key", "links", "name", "refname", "state", "updated_on", "url"]
```

`commit`, `repository` are **not in spec allOf properties**.  
`refname` IS in spec — that's fine.

## Live API evidence

```bash
curl -s -H "Authorization: Basic $AUTH" \
  ".../commit/84952fad.../statuses/build/bb-probe-ci" | jq '[keys[]] | sort'
# → ["commit", "created_on", "description", "key", "links", "name",
#    "refname", "repository", "state", "type", "updated_on", "url"]
```

Fields returned by API but missing from spec:
| Field | Type | Notes |
|-------|------|-------|
| `commit` | Object (commit reference) | Commit this status belongs to |
| `repository` | Object (repository reference) | Repo this status belongs to |
| `type` | `"build"` | Type discriminator |

## Impact

`Commitstatus` model has no `.commit` or `.repository` attributes. Users can't navigate from a status back to the commit/repo without additional API calls.

## Fix recommendation

Add `commit`, `repository`, `type` to the second allOf entry in `commitstatus`:

```bash
jq '(.components.schemas.commitstatus.allOf[] | select(.properties != null)).properties.commit = {
  "$ref": "#/components/schemas/commit"
} | (.components.schemas.commitstatus.allOf[] | select(.properties != null)).properties.repository = {
  "$ref": "#/components/schemas/repository"
} | (.components.schemas.commitstatus.allOf[] | select(.properties != null)).properties.type = {
  "type": "string"
}' bb_cloud_fixed.openapi.json > /tmp/fixed.json && mv /tmp/fixed.json bb_cloud_fixed.openapi.json
make generate-cloud && make diff-cloud
```
