# BUG-SCHEMA-028: `ssh_key` and `ssh_account_key` date-time fields not nullable — crashes on unused/unconfigured SSH keys

**Status:** FIXED
**Model:** `ssh_key`, `ssh_account_key`
**Endpoint:** `GET /users/{selected_user}/ssh-keys`, `GET /users/{selected_user}/ssh-keys/{key_id}`
**Layer:** spec (missing `nullable: true` on date-time fields)
**Severity:** High — any SSH key that has never been used or lacks an expiry produces `TypeError` during deserialization

---

## Symptom

Fetching SSH keys for a user raised a `TypeError` when the key had never been used or had no expiry date set:

```
TypeError: fromisoformat: argument must be str
```

The generated model tried to call `isoparse(None)` when `last_used` or `expires_on` was `null` in the JSON response. No exception was documented or expected — the model simply crashed on any key that had never authenticated.

---

## Root cause

Three date-time fields in `ssh_key` and `ssh_account_key` were missing `nullable: true`:

| Schema | Field | Live API value |
|---|---|---|
| `ssh_key` | `last_used` | `null` for keys never used |
| `ssh_key` | `created_on` | `null` in some edge cases |
| `ssh_account_key` | `expires_on` | `null` for non-expiring keys |

`ssh_account_key` inherits `last_used` and `created_on` from `ssh_key` via `allOf $ref`, so those two fields were also broken for `ssh_account_key` responses.

---

## Spec evidence

```bash
# Before fix — last_used in ssh_key had no nullable marker
jq '.components.schemas.ssh_key.allOf[] | .properties // {} | .last_used' bb_cloud_fixed.openapi.json
# → {"type": "string", "format": "date-time"}   ← nullable: true missing

# Before fix — expires_on in ssh_account_key had no nullable marker
jq '.components.schemas.ssh_account_key.allOf[] | .properties // {} | .expires_on' bb_cloud_fixed.openapi.json
# → {"type": "string", "format": "date-time"}   ← nullable: true missing
```

Live API example (a key that has never been used):

```json
{
  "type": "ssh_key",
  "uuid": "{abc123}",
  "key": "ssh-ed25519 AAAA...",
  "label": "laptop",
  "created_on": "2025-01-10T12:00:00.000000+00:00",
  "last_used": null,
  "links": { "self": { "href": "https://api.bitbucket.org/2.0/users/.../ssh-keys/..." } }
}
```

The generated `SshKey` attrs model used `isoparse` for `last_used`, which raised `TypeError` on `null`.

---

## Related bugs

This is the same class of bug as:
- **BUG-SCHEMA-010** — `GPG_account_key.last_used` not nullable
- **BUG-SCHEMA-014** — `deploy_key.last_used` not nullable
- **BUG-SCHEMA-012** — `tag.date` and `tag.tagger` not nullable

---

## Fix applied (2026-05-16)

Added `nullable: true` to the affected fields in both schemas:

**`ssh_key.last_used` and `ssh_key.created_on`:**

```bash
jq '(
  .components.schemas.ssh_key.allOf[]
  | select(.properties != null)
  | .properties.last_used
) += {"nullable": true} |
(
  .components.schemas.ssh_key.allOf[]
  | select(.properties != null)
  | .properties.created_on
) += {"nullable": true}
' bb_cloud_fixed.openapi.json > /tmp/fixed.json && mv /tmp/fixed.json bb_cloud_fixed.openapi.json
```

**`ssh_account_key.expires_on`:**

```bash
jq '(
  .components.schemas.ssh_account_key.allOf[]
  | select(.properties != null)
  | .properties.expires_on
) += {"nullable": true}
' bb_cloud_fixed.openapi.json > /tmp/fixed.json && mv /tmp/fixed.json bb_cloud_fixed.openapi.json

make generate-cloud && make diff-cloud
```

Fix confirmed: generated models now use `Optional[datetime]` for all three fields, and `None` is returned (not a crash) for keys that have never been used or have no expiry.

---

## Status

- [x] Confirmed via live API response inspection (`last_used: null` on brand-new SSH keys)
- [x] Fixed in `bb_cloud_fixed.openapi.json`
- [x] Regenerated: `make generate-cloud && make diff-cloud`
