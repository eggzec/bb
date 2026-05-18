# BUG-SCHEMA-007: deployment_environment schema documents only 2 of 12 fields

**Module:** deployments
**Function:** get_environment, list_environments, create_environment, update_environment
**HTTP Status:** 200
**Tags:** [spec, schema]

## Symptom

The `deployment_environment` schema in `bb_cloud_fixed.openapi.json` only documents
`name` and `uuid`. The live API returns 12 fields. 10 fields are completely undocumented,
making the generated `DeploymentEnvironment` model nearly useless — callers can only
read `name` and `uuid` from the SDK, even though the API always provides the full object.

## Steps to reproduce (curl)

```bash
# URL-encode the curly-brace UUID — raw {uuid} in path → HTTP 400
curl -s -H "Authorization: Basic $AUTH" \
  "https://api.bitbucket.org/2.0/repositories/beaverish/bb-probe/environments/%7B697d8906-4609-448e-85f1-6b05d5c9faa9%7D" \
  | jq '[keys[]] | sort'
# → ["category","deployment_gate_enabled","environment_lock_enabled","environment_type",
#    "hidden","lock","name","rank","restrictions","slug","type","uuid"]
```

Note: the generated SDK correctly URL-encodes the UUID via `urllib.parse.quote`, so SDK
callers do NOT need to pre-encode. The 400 only occurs with raw curl using literal `{uuid}`.

## Spec vs actual

```bash
jq '[.components.schemas.deployment_environment.allOf[] | .properties // {} | keys[]] | flatten | unique | sort' \
  bb_cloud_fixed.openapi.json
# → ["name","uuid"]
```

### Documented (2 fields)

| Field | Spec type |
|---|---|
| `name` | string |
| `uuid` | string |

### Undocumented (10 additional fields in live response)

| Field | Observed type | Description |
|---|---|---|
| `type` | string | `"deployment_environment"` |
| `slug` | string | URL-safe name (e.g. `"test"`, `"staging"`, `"production"`) |
| `rank` | integer | Sort order (0=Test, 1=Staging, 2=Production) |
| `category` | object | `{"name": "Test"}` |
| `environment_type` | object | `{"name": "Test", "rank": 0, "type": "deployment_environment_type"}` |
| `deployment_gate_enabled` | boolean | Whether deployment gates are enabled |
| `environment_lock_enabled` | boolean | Whether the environment has a deployment lock |
| `lock` | object | Current lock state (complex — includes `lock_opener`, `triggerer`, `name`, `type`) |
| `restrictions` | object | `{"type": "deployment_restrictions_configuration", "admin_only": false}` |
| `hidden` | boolean | Whether the environment is hidden in the UI |

## Impact

- `DeploymentEnvironment.slug` — no attribute on generated model
- `DeploymentEnvironment.rank` — no attribute
- `DeploymentEnvironment.category` — no attribute
- `DeploymentEnvironment.environment_type` — no attribute
- `DeploymentEnvironment.deployment_gate_enabled` — no attribute
- `DeploymentEnvironment.environment_lock_enabled` — no attribute
- `DeploymentEnvironment.lock` — no attribute (critical — needed to check if env is locked)
- `DeploymentEnvironment.restrictions` — no attribute
- `DeploymentEnvironment.hidden` — no attribute

The `lock` field is particularly important — it tells callers whether a pipeline is
currently deploying to this environment and the deployment gate state.

## Fix recommendation

The `lock` and `restrictions` subobjects also need schema definitions. A full fix:

1. Define `deployment_environment_lock` and `deployment_restrictions_configuration` schemas
2. Extend `deployment_environment` properties

Minimal patch to expose the simple scalar fields:

```bash
jq '(.components.schemas.deployment_environment.allOf[] | select(.properties != null) | .properties) += {
  "type": {"type": "string"},
  "slug": {"type": "string", "description": "URL-safe environment name."},
  "rank": {"type": "integer", "description": "Sort order for the environment."},
  "hidden": {"type": "boolean"},
  "deployment_gate_enabled": {"type": "boolean"},
  "environment_lock_enabled": {"type": "boolean"},
  "category": {"type": "object", "additionalProperties": true},
  "environment_type": {"type": "object", "additionalProperties": true},
  "lock": {"type": "object", "additionalProperties": true},
  "restrictions": {"type": "object", "additionalProperties": true}
}' bb_cloud_fixed.openapi.json > /tmp/fixed.json && mv /tmp/fixed.json bb_cloud_fixed.openapi.json
make generate-cloud && make diff-cloud
```

## Related note — UUID URL-encoding

Raw `GET /environments/{697d8906-...}` (curly braces in URL) → HTTP 400.
URL-encoded `GET /environments/%7B697d8906-...%7D` → HTTP 200.

The generated SDK correctly calls `urllib.parse.quote(environment_uuid, safe="")` in
`_get_kwargs`, so this is transparent to SDK callers. No fix needed for the SDK.

## Confirmation (2026-05-15)

**Status: FIXED** — added `type`, `slug`, `rank`, `hidden`, `deployment_gate_enabled`, `environment_lock_enabled`, `category`, `lock`, `restrictions` to `deployment_environment` allOf properties. Note: `environment_type` and `name`/`uuid` were already present. Regenerated 2026-05-16.
