# BUG-SCHEMA-006: branch response includes undocumented fields

**Module:** branches
**Function:** list, get, create, delete
**HTTP Status:** 200
**Tags:** [spec, schema]

## Symptom

The live Bitbucket API returns `branch` objects with fields not documented in the spec.
The generated `Branch` model silently drops them on deserialization.

## Steps to reproduce (curl)

```bash
curl -s -H "Authorization: Basic $AUTH" \
  "https://api.bitbucket.org/2.0/repositories/beaverish/bb-probe/refs/branches/main" \
  | jq '[keys[]] | sort'
# → ["default_merge_strategy","links","merge_strategies","name","sync_strategies","target","type"]
```

## Spec vs actual

```bash
jq '[.components.schemas.branch.allOf[] | .properties // {} | keys[]] | flatten | unique | sort' \
  bb_cloud_fixed.openapi.json
# → ["links","merge_strategies","name","target","type"]
```

### Undocumented fields (present in live response, absent from spec)

| Field | Type | Sample value | Description |
|---|---|---|---|
| `default_merge_strategy` | string | `"merge_commit"` | The default merge strategy for PRs into this branch |
| `sync_strategies` | array | `["sync","fast_forward"]` | Available strategies when syncing a fork branch |

### Spec-documented fields (confirmed present in live response)

`links`, `merge_strategies`, `name`, `target`, `type`

## Impact

- `Branch.default_merge_strategy` — attribute does not exist on generated model
- `Branch.sync_strategies` — attribute does not exist on generated model

Callers cannot read the default merge strategy or available sync strategies even though
the API always includes them in branch responses.

`default_merge_strategy` is especially useful — it tells callers which strategy a PR
merge will use by default before a merge is attempted.

## Fix recommendation

Add the two undocumented properties to the `branch` schema in `bb_cloud_fixed.openapi.json`.
The `branch` model uses `allOf`, so the properties must be added to the branch-specific
`allOf` entry (the one with the branch-specific properties, not the `ref` base):

```bash
# First, identify which allOf entry has branch-specific props
jq '.components.schemas.branch.allOf[] | select(.properties != null) | .properties | keys' \
  bb_cloud_fixed.openapi.json

# Add to the branch-specific allOf entry
jq '(.components.schemas.branch.allOf[] | select(.properties != null) | .properties) += {
  "default_merge_strategy": {
    "type": "string",
    "description": "The default merge strategy for pull requests targeting this branch."
  },
  "sync_strategies": {
    "type": "array",
    "items": {"type": "string"},
    "description": "Available strategies for syncing a fork branch with this branch."
  }
}' bb_cloud_fixed.openapi.json > /tmp/fixed.json && mv /tmp/fixed.json bb_cloud_fixed.openapi.json
make generate-cloud && make diff-cloud
```

## Confirmation (2026-05-15)

```bash
curl -s -H "Authorization: Basic $AUTH" \
  "https://api.bitbucket.org/2.0/repositories/beaverish/bb-probe/refs/branches/main" \
  | jq '{default_merge_strategy, sync_strategies}'
# → {"default_merge_strategy": "merge_commit", "sync_strategies": ["sync", "fast_forward"]}
```

**Status: FIXED** — added `sync_strategies` (array of strings) to `branch` allOf properties. Note: `default_merge_strategy` was already present in the spec when this fix was applied. Regenerated 2026-05-16.
