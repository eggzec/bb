# BUG-SCHEMA-008: `pullrequest.closed_by` — nullable `$ref` without `anyOf` pattern causes TypeError on open PRs

**Status:** FIXED
**Model:** `pullrequest`
**Endpoint:** `GET /repositories/{workspace}/{repo_slug}/pullrequests`, `GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}`
**Layer:** spec (response schema — nullable `$ref` missing `anyOf` wrapper)
**Severity:** Critical — ALL PR get/list calls crashed for open PRs

## Symptom

`prs.list()` and `prs.get()` raised:

```
TypeError: 'NoneType' object is not iterable
```

The crash occurred inside the generated `PullRequest.from_dict()` when deserializing an open PR
whose `closed_by` field is `null`. Open PRs always have `closed_by: null` because no one has
closed them yet, making this bug 100% reproducible on any workspace with open PRs.

## Root cause

The spec defined `pullrequest.properties.closed_by` as:

```json
{
  "$ref": "#/components/schemas/account",
  "nullable": true
}
```

`openapi-python-client` does not honour `nullable: true` on a bare `$ref` field. It generates
`Account.from_dict(data)` unconditionally, without a `None` guard. When the API returns
`"closed_by": null`, `from_dict(None)` iterates over `None` and throws `TypeError`.

The correct pattern for a nullable `$ref` is to wrap the reference in `anyOf`:

```json
{
  "anyOf": [{"$ref": "#/components/schemas/account"}],
  "nullable": true
}
```

This signals to the generator that the field may be `None` and causes it to emit
`Account.from_dict(data) if data is not None else None`.

## Spec evidence

```bash
jq '.components.schemas.pullrequest.allOf[] | select(.properties.closed_by != null) | .properties.closed_by' \
  bb_cloud_fixed.openapi.json
# Before fix → {"$ref": "#/components/schemas/account", "nullable": true}
# After fix  → {"anyOf": [{"$ref": "#/components/schemas/account"}], "nullable": true}
```

## Impact

- `prs.list()` — crashed on every workspace that has at least one open PR
- `prs.get(pull_request_id=<open PR>)` — same crash
- Entire PR read path was non-functional for the common case (open PRs)

## Fix applied (2026-05-16)

Changed `closed_by` in `pullrequest.allOf[*].properties` from a bare `$ref` to the `anyOf` + `nullable` pattern:

```bash
jq '(
  .components.schemas.pullrequest.allOf[]
  | select(.properties.closed_by != null)
  | .properties.closed_by
) = {"anyOf": [{"$ref": "#/components/schemas/account"}], "nullable": true}' \
  bb_cloud_fixed.openapi.json > /tmp/fixed.json && mv /tmp/fixed.json bb_cloud_fixed.openapi.json
make generate-cloud && make diff-cloud
```

Fix confirmed: generated `from_dict` now guards `closed_by` deserialization with a `None` check.
