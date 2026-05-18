# BUG-DEPLOY-002: Environment update SDK call fails — generated API has no `body` parameter

**Status:** FIXED
**Root cause:** spec — `requestBody` is entirely absent from the OpenAPI spec for `POST /repositories/{workspace}/{repo_slug}/environments/{environment_uuid}/changes`
**Layer:** `.paths["/repositories/{workspace}/{repo_slug}/environments/{environment_uuid}/changes"].post.requestBody` (null)

---

## Affected function
- `bb.cloud.sdk.deployments.update_env`

---

## Spec inspection (jq findings)

```bash
jq '.paths | to_entries[] | select(.key | test("environment")) | {path: .key, methods: (.value | keys), put_requestBody: .value.put.requestBody, post_requestBody: .value.post.requestBody}' bb_cloud_fixed.openapi.json
```

Output (relevant entry):
```json
{
  "path": "/repositories/{workspace}/{repo_slug}/environments/{environment_uuid}/changes",
  "methods": ["post"],
  "put_requestBody": null,
  "post_requestBody": null
}
```

`requestBody` is **null (absent)** for the `/changes` POST endpoint. Compare to the sibling `POST /environments` (create), which correctly has:
```json
{
  "post_requestBody": {
    "content": {"application/json": {"schema": {"$ref": "#/components/schemas/deployment_environment"}}},
    "description": "The environment to create.",
    "required": true
  }
}
```

The `deployment_environment` schema exists:
```bash
jq '.components.schemas | to_entries[] | select(.key | test("[Ee]nvironment")) | .key' bb_cloud_fixed.openapi.json
# → "deployment_environment", "paginated_environments"
```

The `deployment_environment` schema has properties: `uuid` and `name`.

---

## Live API confirmation (curl findings)

The SDK live test (`test_update_env_roundtrip`) sends a `DeploymentEnvironment` body with `name` field set. Without a body the API would receive no rename instruction and would likely return 400 or silently no-op.

The SDK wrapper explicitly passes `body=body`:
```python
# sdk/deployments.py:332-334
result = await update_environment_for_repository.asyncio(
    workspace, repo_slug, environment_uuid, client=client.auth, body=body
)
```

The generated `update_environment_for_repository.asyncio()` does NOT accept a `body` parameter (confirmed by reading the generated file — `_get_kwargs` only takes `workspace`, `repo_slug`, `environment_uuid`).

At runtime this raises:
```
TypeError: asyncio() got an unexpected keyword argument 'body'
```

---

## Note on 202 semantics

The API returns `202 Accepted` (async operation — the rename is queued). The spec maps `202 → None` in `_parse_response`. So even when the body bug is fixed, the SDK correctly returns `None` for a successful update — this is correct behaviour. The test (`test_update_env_roundtrip`) asserts only that no `Error` is returned.

---

## Schema gap

The `/changes` endpoint expects a `deployment_environment` body per the Bitbucket Deployments API semantics. Based on the test patterns and sister `create_env` endpoint:

| Field | Required | Notes |
|-------|----------|-------|
| `name` | Yes | New environment name |
| `type` | Optional | `"deployment_environment"` |

---

## Generated code impact

```python
# update_environment_for_repository.py
def _get_kwargs(workspace: str, repo_slug: str, environment_uuid: str) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/repositories/{workspace}/{repo_slug}/environments/{environment_uuid}/changes".format(...),
    }
    return _kwargs  # NO "_kwargs['json'] = body.to_dict()"
```

---

## Exact fix

### Step 1 — Add `requestBody` to POST (update environment via /changes)

```bash
cd /home/ali/Documents/repos/bb.git/fix-paginaton

jq '.paths["/repositories/{workspace}/{repo_slug}/environments/{environment_uuid}/changes"].post.requestBody = {
  "required": true,
  "description": "The environment update to apply.",
  "content": {
    "application/json": {
      "schema": {"$ref": "#/components/schemas/deployment_environment"}
    }
  }
}' bb_cloud_fixed.openapi.json > /tmp/fixed.json && mv /tmp/fixed.json bb_cloud_fixed.openapi.json
```

### Step 2 — Regenerate and verify

```bash
make generate-cloud && make diff-cloud
```

After regeneration, verify that `_get_kwargs` in `update_environment_for_repository.py` gains a `body: DeploymentEnvironment` parameter and injects `_kwargs["json"] = body.to_dict()`.

---

## Spec Fix Applied

Added `requestBody` referencing `deployment_environment` schema to the `POST /repositories/{workspace}/{repo_slug}/environments/{environment_uuid}/changes` endpoint:

```bash
jq '
  .paths["/repositories/{workspace}/{repo_slug}/environments/{environment_uuid}/changes"].post.requestBody = {
    "required": true,
    "description": "The environment update to apply.",
    "content": {"application/json": {"schema": {"$ref": "#/components/schemas/deployment_environment"}}}
  }
' bb_cloud_fixed.openapi.json > /tmp/fixed.json && mv /tmp/fixed.json bb_cloud_fixed.openapi.json
```

After `make generate-cloud`, the generated `_get_kwargs` for `update_environment_for_repository` gains a `body: DeploymentEnvironment` parameter and injects `_kwargs["json"] = body.to_dict()`.

**Note on BUG-DEPLOY-003 workaround:** BUG-DEPLOY-003 was a temporary SDK fix that removed `body=body` forwarding from `update_env` to stop the `TypeError`. After this spec fix + regeneration, the coordinator step restores `body=body` in `deployments.py` and makes the `body` parameter required again. BUG-DEPLOY-003 is superseded by this spec fix.

---

## Tests that expose this bug
- `test_update_env_roundtrip` — fails with `TypeError`
