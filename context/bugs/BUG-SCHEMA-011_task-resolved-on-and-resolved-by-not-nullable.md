# BUG-SCHEMA-011: `task.resolved_on` and `task.resolved_by` — not nullable causes TypeError on unresolved tasks

**Status:** FIXED
**Model:** `task`
**Endpoint:** `GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/tasks`, and task CRUD endpoints
**Layer:** spec (response schema — date-time and `$ref` fields missing nullable handling)
**Severity:** High — any PR with unresolved tasks crashes task deserialization

## Symptom

Task list/get calls raised two distinct errors depending on which field was hit first:

For `resolved_on` (date-time field):
```
TypeError: object of type 'NoneType' has no len()
```
from `isoparse(None)` inside `Task.from_dict()`.

For `resolved_by` (`$ref` to `account`):
```
TypeError: 'NoneType' object is not iterable
```
from `Account.from_dict(None)` inside `Task.from_dict()`.

Unresolved tasks always have `"resolved_on": null` and `"resolved_by": null`. Since tasks
start out unresolved and are typically open throughout PR review, this bug triggered on nearly
every PR task query.

## Spec evidence

```bash
jq '.components.schemas.task.properties | {resolved_on, resolved_by}' bb_cloud_fixed.openapi.json
# Before fix:
# {
#   "resolved_on": {"type": "string", "format": "date-time"},
#   "resolved_by": {"$ref": "#/components/schemas/account"}
# }
# After fix:
# {
#   "resolved_on": {"type": "string", "format": "date-time", "nullable": true},
#   "resolved_by": {"anyOf": [{"$ref": "#/components/schemas/account"}], "nullable": true}
# }
```

## Impact

- `tasks.list(pull_request_id=...)` — crashed on PRs with any unresolved task
- `tasks.get(task_id=...)` — same crash for unresolved task
- Task workflows (code review, checklist tracking) were entirely non-functional

## Fix applied (2026-05-16)

Applied `nullable: true` to `resolved_on` and the `anyOf` + `nullable` pattern to `resolved_by`:

```bash
jq '
  .components.schemas.task.properties.resolved_on += {"nullable": true} |
  .components.schemas.task.properties.resolved_by = {
    "anyOf": [{"$ref": "#/components/schemas/account"}],
    "nullable": true
  }
' bb_cloud_fixed.openapi.json > /tmp/fixed.json && mv /tmp/fixed.json bb_cloud_fixed.openapi.json
make generate-cloud && make diff-cloud
```

Fix confirmed: generated `Task.from_dict()` now guards both `isoparse` (for `resolved_on`) and
`Account.from_dict` (for `resolved_by`) with `None` checks.
