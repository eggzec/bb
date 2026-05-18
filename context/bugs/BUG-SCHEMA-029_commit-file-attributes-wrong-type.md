# BUG-SCHEMA-029: `commit_file.attributes` — typed as a single string enum instead of an array

**Status:** FIXED
**Model:** `commit_file`
**Endpoint:** `GET /repositories/{workspace}/{repo_slug}/src/{commit}/{path}` (directory listing)
**Layer:** spec (wrong type — `string` should be `array of string`)
**Severity:** Medium — deserialization crash or silent data loss when a file has one or more attributes set

---

## Symptom

Listing source-tree entries that include files with attributes (e.g., executable bit, binary marker, LFS pointer) produced either:

1. A deserialization error when the live API returned an array value like `["executable"]` but the generated model expected a plain string
2. Silent data loss — in Python, the generated model silently discarded `attributes` because the type union failed to match

The generated `CommitFile` model had `attributes: Optional[str]` (a single enum string), but the live API always returns `attributes` as a JSON array — even when only one attribute applies:

```json
{
  "type": "commit_file",
  "path": "setup.sh",
  "attributes": ["executable"],
  ...
}
```

---

## Root cause

The spec defined `attributes` in `commit_file` as:

```json
{
  "type": "string",
  "enum": ["link", "executable", "subrepository", "binary", "lfs"]
}
```

This is a single-value string type. The live Bitbucket API has always returned `attributes` as a **JSON array of strings**, not a single string. A file can have multiple attributes (e.g., both `["binary", "lfs"]`), which would be structurally impossible with a string type.

---

## Spec evidence

```bash
# Before fix — commit_file.attributes was typed as string
jq '.components.schemas.commit_file.properties.attributes' bb_cloud_fixed.openapi.json
# → {"type": "string", "enum": ["link", "executable", "subrepository", "binary", "lfs"]}
```

Live API response for an executable script:

```bash
curl -s -u "$BB_EMAIL:$BB_TOKEN" \
  "https://api.bitbucket.org/2.0/repositories/$BB_WORKSPACE/$BB_REPO_SLUG/src/HEAD/?pagelen=50" | \
  python3 -c "import sys,json; d=json.load(sys.stdin); [print(v['path'], v.get('attributes')) for v in d.get('values',[]) if v.get('attributes')]"
# → setup.sh ['executable']
# → vendor/model.bin ['binary', 'lfs']
```

The response always returns an array, never a bare string.

---

## Impact

- `sources.list_directory()` — any file with attributes (executable scripts, binary blobs, LFS objects, symlinks) caused a deserialization failure or dropped the `attributes` field silently
- SDK callers could not distinguish between regular files and executable/binary/LFS-tracked files without manually re-fetching and parsing the raw response

---

## Fix applied (2026-05-16)

Changed `attributes` from `{"type": "string", "enum": [...]}` to `{"type": "array", "items": {"type": "string", "enum": [...]}}`:

```bash
jq '.components.schemas.commit_file.properties.attributes = {
  "type": "array",
  "items": {
    "type": "string",
    "enum": ["link", "executable", "subrepository", "binary", "lfs"]
  }
}' bb_cloud_fixed.openapi.json > /tmp/fixed.json && mv /tmp/fixed.json bb_cloud_fixed.openapi.json

make generate-cloud && make diff-cloud
```

Fix confirmed: generated `CommitFile` model now has `attributes: Optional[List[CommitFileAttributesItem]]`, matching the array structure the live API returns.

---

## Status

- [x] Confirmed via live API response (`attributes` is always a JSON array)
- [x] Fixed in `bb_cloud_fixed.openapi.json`
- [x] Regenerated: `make generate-cloud && make diff-cloud`
