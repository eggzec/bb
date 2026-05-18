# BUG-SCHEMA-010: `GPG_account_key.last_used` — date-time field not nullable causes TypeError on unused keys

**Status:** FIXED
**Model:** `GPG_account_key`
**Endpoint:** `GET /users/{selected_user}/gpg-keys`, `GET /users/{selected_user}/gpg-keys/{id}`
**Layer:** spec (response schema — date-time field missing `nullable: true`)
**Severity:** High — any GPG key that has never been used crashes deserialization

## Symptom

`gpg_keys.list()` and `gpg_keys.get()` raised:

```
TypeError: object of type 'NoneType' has no len()
```

The crash occurred inside `isoparse(None)` within the generated `GPGAccountKey.from_dict()`.
A GPG key that has never been used has `"last_used": null` in the API response. Without
`nullable: true` in the spec, the generator emits `isoparse(data["last_used"])` unconditionally,
which fails when the value is `None`.

## Spec evidence

```bash
jq '.components.schemas.GPG_account_key.allOf[] | select(.properties.last_used != null) | .properties.last_used' \
  bb_cloud_fixed.openapi.json
# Before fix → {"type": "string", "format": "date-time"}
# After fix  → {"type": "string", "format": "date-time", "nullable": true}
```

## Impact

- `gpg_keys.list()` — crashed on any account that has an unused GPG key
- `gpg_keys.get(id=<unused key>)` — same crash
- Newly-added keys (never used for authentication) always trigger this bug

## Fix applied (2026-05-16)

Added `nullable: true` to `last_used` in `GPG_account_key.allOf[*].properties`:

```bash
jq '(
  .components.schemas.GPG_account_key.allOf[]
  | select(.properties.last_used != null)
  | .properties.last_used
) += {"nullable": true}' \
  bb_cloud_fixed.openapi.json > /tmp/fixed.json && mv /tmp/fixed.json bb_cloud_fixed.openapi.json
make generate-cloud && make diff-cloud
```

Fix confirmed: generated `from_dict` now guards `isoparse` with a `None` check for `last_used`.
