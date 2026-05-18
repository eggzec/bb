# BUG-SCHEMA-014: `deploy_key.last_used` — date-time field not nullable causes TypeError on unused keys

**Status:** FIXED
**Model:** `deploy_key` (allOf)
**Endpoint:** `GET /repositories/{workspace}/{repo_slug}/deploy-keys`, `GET /repositories/{workspace}/{repo_slug}/deploy-keys/{key_id}`
**Layer:** spec (response schema — date-time field missing `nullable: true`)
**Severity:** High — any deploy key that has never been used crashes deserialization

## Symptom

`deploy_keys.list()` and `deploy_keys.get()` raised:

```
TypeError: object of type 'NoneType' has no len()
```

The crash occurred inside `isoparse(None)` within the generated `DeployKey.from_dict()`.
A deploy key that has never been used for a clone or fetch has `"last_used": null` in the
API response. Without `nullable: true` in the spec, the generator emits
`isoparse(data["last_used"])` unconditionally, failing when the value is `None`.

This is the same class of bug as BUG-SCHEMA-010 (`GPG_account_key.last_used`), applied to
the deploy key schema.

## Spec evidence

```bash
jq '.components.schemas.deploy_key.allOf[] | select(.properties.last_used != null) | .properties.last_used' \
  bb_cloud_fixed.openapi.json
# Before fix → {"type": "string", "format": "date-time"}
# After fix  → {"type": "string", "format": "date-time", "nullable": true}
```

## Impact

- `deploy_keys.list()` — crashed on any repository that has a deploy key never used
  for authentication (e.g., a key added but the CI system not yet configured)
- `deploy_keys.get(key_id=<unused key>)` — same crash
- Newly-added deploy keys always trigger this bug before first use

## Fix applied (2026-05-16)

Added `nullable: true` to `last_used` in `deploy_key.allOf[*].properties`:

```bash
jq '(
  .components.schemas.deploy_key.allOf[]
  | select(.properties.last_used != null)
  | .properties.last_used
) += {"nullable": true}' \
  bb_cloud_fixed.openapi.json > /tmp/fixed.json && mv /tmp/fixed.json bb_cloud_fixed.openapi.json
make generate-cloud && make diff-cloud
```

Fix confirmed: generated `from_dict` now guards `isoparse` with a `None` check for `last_used`.
