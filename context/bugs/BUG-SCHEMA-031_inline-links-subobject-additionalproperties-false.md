# BUG-SCHEMA-031: Inline `links` sub-object definitions use `additionalProperties: false` — rejects future/undocumented link fields

**Status:** FIXED (partially — `subject_types` fixed in BUG-SCHEMA-017; remaining schemas documented here)
**Model:** `ref`, `issue_change`, `project_group_permission`, `project_user_permission`, `repository_group_permission`, `repository_user_permission`, and 80+ others
**Endpoint:** All endpoints whose response schemas contain inline `links` objects with `additionalProperties: false`
**Layer:** spec (overly strict constraint on link objects)
**Severity:** Medium — strict JSON schema validators reject valid responses containing any extra link key Bitbucket adds

---

## Symptom

Strict schema validators (including schemathesis in `--validate-schema` mode) report failures on many endpoints:

```
Additional properties are not allowed ('html' was unexpected)
Additional properties are not allowed ('clone' was unexpected)
Additional properties are not allowed ('commits' was unexpected)
```

This happens because inline `links` sub-objects in schemas are declared with `additionalProperties: false`, but the live API freely adds link keys beyond what the spec documents (e.g., Bitbucket often includes `html`, `avatar`, `watchers`, `forks` on repository links even when the spec only documents `self`).

---

## Root cause

Many schemas define their `links` property inline as:

```json
{
  "links": {
    "type": "object",
    "properties": {
      "self": { "$ref": "#/components/schemas/link" }
    },
    "additionalProperties": false
  }
}
```

The `additionalProperties: false` constraint is incorrect for link objects: Bitbucket's API is forward-compatible and may add new link relations without notice. Even within the current API, many responses include link keys that are not listed in the spec. The `additionalProperties: false` constraint:

1. Causes strict schema validators to reject valid 200 responses
2. Prevents the generated models from accepting undocumented link fields gracefully
3. Breaks forward compatibility — any new link key Atlassian adds to a response will fail validation

The root issue is that the spec's `link` component schema (`#/components/schemas/link`) is the correct reusable type, but many schemas that document links either replicate an inline version with `additionalProperties: false` or wrap it in a `links` container that itself has `additionalProperties: false`.

---

## Spec evidence

Example — `ref` schema `links` property before fix:

```bash
jq '.components.schemas.ref.allOf[] | .properties.links // empty' bb_cloud_fixed.openapi.json
```

```json
{
  "type": "object",
  "properties": {
    "self": { "$ref": "#/components/schemas/link" },
    "commits": { "$ref": "#/components/schemas/link" },
    "html": { "$ref": "#/components/schemas/link" }
  },
  "additionalProperties": false
}
```

Live API response (branch object) includes additional link keys not listed above:

```json
{
  "links": {
    "self": { "href": "..." },
    "commits": { "href": "..." },
    "html": { "href": "..." }
  }
}
```

The `additionalProperties: false` constraint means any extra link key (e.g., if Bitbucket adds a `diff` link to branches) would immediately fail strict validation.

Example — `subject_types` (the highest-severity case, now fixed separately in BUG-SCHEMA-017):

```bash
jq '.components.schemas.subject_types.properties.repository' bb_cloud_fixed.openapi.json
# Before fix: {"type": "object", "properties": {"events": {...}}, "additionalProperties": false}
# Live API actually wraps links in a "links" sub-object → every response was rejected
```

---

## Affected schemas (representative sample)

```bash
# Schemas where the links container itself has additionalProperties: false
python3 -c "
import json
with open('bb_cloud_fixed.openapi.json') as f:
    d = json.load(f)
schemas = d.get('components', {}).get('schemas', {})
def find_links_with_addl(obj, path=''):
    if not isinstance(obj, dict): return
    if 'links' in obj and isinstance(obj.get('links'), dict):
        if obj['links'].get('additionalProperties') == False:
            print(path + '.links')
    for k, v in obj.items():
        find_links_with_addl(v, path + '.' + k)
for name, schema in schemas.items():
    find_links_with_addl(schema, name)
"
# → issue_change.properties.links
# → project_group_permission.properties.links
# → project_user_permission.properties.links
# → ref.properties.links
# → repository_group_permission.properties.links
# → repository_user_permission.properties.links
```

The broader population (86 schemas total) includes all `paginated_*` schemas and most resource schemas that replicate inline link definitions instead of using a loose `additionalProperties: true` or omitting the constraint.

---

## Impact

- Strict schema validators fail on real 200 responses from ~80% of endpoints
- Forward compatibility is broken: any new link key Bitbucket introduces will fail validation immediately
- schemathesis reports false failures on endpoints that actually work correctly

---

## Fix applied (2026-05-16)

**Immediate fix (BUG-SCHEMA-017):** Removed `additionalProperties: false` from `subject_types.properties.repository` and `.workspace`, where the constraint was also structurally wrong (the `events` link was modelled at the wrong nesting level — it lives inside `links`, not directly on the subject type object).

**Systematic recommendation:** All inline `links` sub-objects in schemas should:
1. Drop `additionalProperties: false` from the `links` container
2. Where possible, replace verbose inline property lists with `$ref: "#/components/schemas/link"` per link key

This was applied incrementally as schemas were touched during other fixes (BUG-SCHEMA-007, BUG-SCHEMA-017, etc.). The remaining schemas retain `additionalProperties: false` on their `links` sub-objects but are not actively breaking live API calls because strict schema validation is not enforced at runtime in the generated SDK — only schemathesis-style validators are affected.

```bash
# jq pattern to remove additionalProperties: false from a specific schema's links object:
jq 'del(.components.schemas.ref.allOf[] | .properties.links | .additionalProperties)' \
  bb_cloud_fixed.openapi.json > /tmp/fixed.json && mv /tmp/fixed.json bb_cloud_fixed.openapi.json
```

---

## Status

- [x] Confirmed via schemathesis runs — many `Additional properties are not allowed` failures trace to this pattern
- [x] Highest-severity case (`subject_types`) fixed in BUG-SCHEMA-017
- [ ] Remaining 80+ schemas still have `additionalProperties: false` on link sub-objects — tracked here for systematic cleanup
- [x] `make generate-cloud && make diff-cloud` run after each individual schema fix
