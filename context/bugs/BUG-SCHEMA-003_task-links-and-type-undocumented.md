# BUG-SCHEMA-003: `task` schema — `links` and `type` returned by API but missing from spec properties

**Status:** FIXED — added `links` (additionalProperties $ref link) and `type` (string enum "task") to `task.properties`. Regenerated 2026-05-16.
**Model:** `task`
**Endpoint:** `GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/tasks/{task_id}`
**Layer:** spec (response schema incomplete)
**Severity:** Medium — `links` navigation field inaccessible through SDK; `type` discriminator missing

## Spec evidence

```bash
jq '.components.schemas.task | {required: .required, properties: (.properties | keys)}' bb_cloud_fixed.openapi.json
# {
#   "required": ["created_on", "updated_on", "state", "content", "creator"],
#   "properties": ["content", "created_on", "creator", "id", "pending",
#                  "resolved_by", "resolved_on", "state", "updated_on"]
# }
```

`links` and `type` are **not in spec properties**.

## Live API evidence

```bash
curl -s -H "Authorization: Basic $AUTH" \
  ".../pullrequests/1/tasks/64759588" | jq '[keys[]]'
# → ["content", "created_on", "creator", "id", "links", "pending",
#    "resolved_by", "resolved_on", "state", "updated_on"]
# NOTE: type is null (returned but null)
```

Fields returned by API but missing from spec:
| Field | Observed value | Notes |
|-------|---------------|-------|
| `links` | Object with `self`, `html` | Standard navigation links — SDK users can't access them |
| `type` | `null` | Returned as null; should be `"task"` per Bitbucket convention |

Also: `required` says `creator` is required, but `creator` is likely always present. No gap there.

## Impact

The generated `Task` model has no `.links` attribute. SDK users can't get the task URL without constructing it manually.

## Fix recommendation

```bash
jq '.components.schemas.task.properties.links = {
  "type": "object",
  "description": "Navigation links for this task",
  "additionalProperties": {"$ref": "#/components/schemas/link"}
} | .components.schemas.task.properties.type = {"type": "string", "enum": ["task"]}' \
  bb_cloud_fixed.openapi.json > /tmp/fixed.json && mv /tmp/fixed.json bb_cloud_fixed.openapi.json
make generate-cloud && make diff-cloud
```
