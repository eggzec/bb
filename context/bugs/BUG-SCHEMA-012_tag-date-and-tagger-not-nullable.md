# BUG-SCHEMA-012: `tag.date` and `tag.tagger` — not nullable causes TypeError on lightweight (unannotated) tags

**Status:** FIXED
**Model:** `tag` (allOf)
**Endpoint:** `GET /repositories/{workspace}/{repo_slug}/refs/tags`, `GET /repositories/{workspace}/{repo_slug}/refs/tags/{name}`
**Layer:** spec (response schema — date-time and `$ref` fields missing nullable handling)
**Severity:** High — any repository with lightweight (non-annotated) tags crashes tag listing

## Symptom

`refs.list_tags()` and `refs.get_tag()` raised two distinct errors:

For `date` (date-time field, only present on annotated tags):
```
TypeError: object of type 'NoneType' has no len()
```
from `isoparse(None)` inside `Tag.from_dict()`.

For `tagger` (`$ref` to `author`, only present on annotated tags):
```
TypeError: 'NoneType' object is not iterable
```
from `Author.from_dict(None)` inside `Tag.from_dict()`.

Lightweight tags (created with `git tag <name>` without `-a` or `-m`) have no annotation
and always return `"date": null` and `"tagger": null`. Lightweight tags are extremely common —
they are the default tag type in most workflows.

## Spec evidence

```bash
jq '.components.schemas.tag.allOf[] | select(.properties.date != null) | .properties | {date, tagger}' \
  bb_cloud_fixed.openapi.json
# Before fix:
# {
#   "date": {"type": "string", "format": "date-time"},
#   "tagger": {"$ref": "#/components/schemas/author"}
# }
# After fix:
# {
#   "date": {"type": "string", "format": "date-time", "nullable": true},
#   "tagger": {"anyOf": [{"$ref": "#/components/schemas/author"}], "nullable": true}
# }
```

## Impact

- `refs.list_tags()` — crashed on any repository containing at least one lightweight tag
- `refs.get_tag(name=<lightweight tag>)` — same crash
- Tag listing was completely broken for the majority of real-world repositories

## Fix applied (2026-05-16)

Applied `nullable: true` to `date` and the `anyOf` + `nullable` pattern to `tagger` within
`tag.allOf[*].properties`:

```bash
jq '(
  .components.schemas.tag.allOf[]
  | select(.properties.date != null)
  | .properties.date
) += {"nullable": true} |
(
  .components.schemas.tag.allOf[]
  | select(.properties.tagger != null)
  | .properties.tagger
) = {"anyOf": [{"$ref": "#/components/schemas/author"}], "nullable": true}' \
  bb_cloud_fixed.openapi.json > /tmp/fixed.json && mv /tmp/fixed.json bb_cloud_fixed.openapi.json
make generate-cloud && make diff-cloud
```

Fix confirmed: generated `Tag.from_dict()` now guards `isoparse` (for `date`) and
`Author.from_dict` (for `tagger`) with `None` checks.
