# BUG-SCHEMA-005: webhook_subscription response includes undocumented fields

**Module:** webhooks
**Function:** get_repo, list_repo, create_repo, update_repo, get_workspace, list_workspace, create_workspace, update_workspace
**HTTP Status:** 200
**Tags:** [spec, schema]

## Symptom

The live Bitbucket API returns `webhook_subscription` objects with fields that are not
documented in the `webhook_subscription` schema in `bb_cloud_fixed.openapi.json`.

The generated `WebhookSubscription` model is built from the spec — it only knows about
the documented properties. The extra fields are silently dropped when attrs deserializes
the JSON, so callers never see them.

## Steps to reproduce (curl)

```bash
curl -s -H "Authorization: Basic $AUTH" \
  "https://api.bitbucket.org/2.0/repositories/beaverish/bb-probe/hooks" \
  | jq '.values[0] | [keys[]] | sort'
# → ["active","created_at","description","events","history_enabled","links",
#    "read_only","secret_set","skip_cert_verification","source","type","url","uuid"]
```

## Spec vs actual

```bash
jq '.components.schemas.webhook_subscription | {required: .required, properties: (.properties // {} | keys)}' \
  bb_cloud_fixed.openapi.json
# → {"required": null, "properties": ["active","created_at","description","events","links","secret_set","url","uuid"]}
```

### Undocumented fields (present in live response, absent from spec)

| Field | Type | Description |
|---|---|---|
| `history_enabled` | boolean | Whether event history is enabled for this webhook |
| `read_only` | boolean | Whether the webhook is read-only (system-managed) |
| `skip_cert_verification` | boolean | Whether SSL certificate verification is skipped |
| `source` | string | Webhook source (e.g. `"USER"`) |

### Spec-documented fields (confirmed present in live response)

`active`, `created_at`, `description`, `events`, `links`, `secret_set`, `url`, `uuid`

## Impact

- `WebhookSubscription.history_enabled` — attribute does not exist on generated model
- `WebhookSubscription.read_only` — attribute does not exist
- `WebhookSubscription.skip_cert_verification` — attribute does not exist
- `WebhookSubscription.source` — attribute does not exist

Callers cannot read these fields from SDK objects even though the API always returns them.

## Fix recommendation

Add the four undocumented properties to `webhook_subscription` schema in `bb_cloud_fixed.openapi.json`:

```bash
jq '.components.schemas.webhook_subscription.properties += {
  "history_enabled": {"type": "boolean", "description": "Whether event delivery history is enabled."},
  "read_only": {"type": "boolean", "description": "Whether this webhook is read-only."},
  "skip_cert_verification": {"type": "boolean", "description": "Whether SSL certificate verification is skipped."},
  "source": {"type": "string", "description": "Source of the webhook (e.g. USER)."}
}' bb_cloud_fixed.openapi.json > /tmp/fixed.json && mv /tmp/fixed.json bb_cloud_fixed.openapi.json
make generate-cloud && make diff-cloud
```

## Confirmation (2026-05-15)

```bash
curl -s -H "Authorization: Basic $AUTH" \
  "https://api.bitbucket.org/2.0/repositories/beaverish/bb-probe/hooks/842a6a21-..." \
  | jq '[keys[]] | sort'
# → ["active","created_at","description","events","history_enabled","links",
#    "read_only","secret_set","skip_cert_verification","source","type","url","uuid"]
```

**Status: FIXED** — added `history_enabled`, `read_only`, `skip_cert_verification`, `source` to `webhook_subscription` allOf properties. Regenerated 2026-05-16.
