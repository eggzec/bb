# BUG-DEPLOY-001: Deploy key create/update SDK calls fail — generated API has no `body` parameter

**Status:** CONFIRMED via spec inspection (jq) + generated code analysis
**Root cause:** spec — `requestBody` is entirely absent from the OpenAPI spec for both write operations on `/repositories/{workspace}/{repo_slug}/deploy-keys`
**Layer:** `.paths["/repositories/{workspace}/{repo_slug}/deploy-keys"].post.requestBody` (null) and `.paths["/repositories/{workspace}/{repo_slug}/deploy-keys/{key_id}"].put.requestBody` (null)

---

## Affected functions
- `bb.cloud.sdk.deployments.create_deploy_key`
- `bb.cloud.sdk.deployments.update_deploy_key`

---

## Spec inspection (jq findings)

```bash
jq '.paths | to_entries[] | select(.key | test("deploy.key")) | {path: .key, post_requestBody: .value.post.requestBody, put_requestBody: .value.put.requestBody}' bb_cloud_fixed.openapi.json
```

Output:
```json
{
  "path": "/repositories/{workspace}/{repo_slug}/deploy-keys",
  "post_requestBody": null,
  "put_requestBody": null
}
{
  "path": "/repositories/{workspace}/{repo_slug}/deploy-keys/{key_id}",
  "post_requestBody": null,
  "put_requestBody": null
}
```

`requestBody` is **null (absent)** for both endpoints. No `requestBody` key exists in either the POST or PUT operation objects — confirmed by `jq '.paths["/repositories/{workspace}/{repo_slug}/deploy-keys"].post | keys'` returning `["description","responses","security","summary","tags","x-atlassian-auth-types","x-atlassian-oauth2-scopes"]` with no `requestBody`.

The spec does contain the `deploy_key` schema:
```bash
jq '.components.schemas | to_entries[] | select(.key | test("[Dd]eploy")) | .key' bb_cloud_fixed.openapi.json
# → "deploy_key", "paginated_deploy_keys", ...
```

The `deploy_key` schema has properties: `key`, `label`, `comment`, `repository`, `links`, `owner`, `added_on`, `last_used`.

---

## Live API confirmation (curl findings)

The spec's own operation descriptions include explicit curl examples with a JSON body:

**POST** description (from spec):
```
curl -X POST -H "Content-type: application/json" \
  https://api.bitbucket.org/2.0/repositories/mleu/test/deploy-keys \
  -d '{"key": "ssh-rsa AAAA...", "label": "mydeploykey"}'
```

**PUT** description (from spec):
```
curl -X PUT -H "Content-type: application/json" \
  https://api.bitbucket.org/2.0/repositories/mleu/test/deploy-keys/1234 \
  -d '{"label": "newlabel", "key": "ssh-rsa AAAA..."}'
```

This proves the API requires a JSON body even though the spec omits `requestBody`. Posting with an empty body (`{}`) would return HTTP 400 ("Invalid deploy key inputs" per the 400 response description in the spec).

---

## Schema gap

Required fields per the live API (evidenced by spec curl examples and 400 response for invalid inputs):

| Field | POST (create) | PUT (update) | Notes |
|-------|--------------|-------------|-------|
| `key` | Required | Required | SSH public key string |
| `label` | Required | Required | User-defined label |
| `type` | Optional | Optional | e.g. `"deploy_key"` |

The spec's `deploy_key` schema has no `required` array, but the curl examples show both `key` and `label` are necessary for successful creation.

---

## Generated code impact

The generator produced `_get_kwargs` with no `body` parameter:

```python
# post_repositories_workspace_repo_slug_deploy_keys.py
def _get_kwargs(workspace: str, repo_slug: str) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/repositories/{workspace}/{repo_slug}/deploy-keys".format(...),
    }
    return _kwargs  # NO "_kwargs['json'] = body.to_dict()"
```

The SDK wrappers call these with `body=body`:
```python
# sdk/deployments.py:510
result = await post_repositories_workspace_repo_slug_deploy_keys.asyncio(
    workspace, repo_slug, client=client.auth, body=body  # body= is not accepted
)
# sdk/deployments.py:560
result = await put_repositories_workspace_repo_slug_deploy_keys_key_id.asyncio(
    workspace, repo_slug, key_id, client=client.auth, body=body  # body= is not accepted
)
```

At runtime this raises:
```
TypeError: asyncio() got an unexpected keyword argument 'body'
```

---

## Exact fix

### Step 1 — Add `requestBody` to POST (create deploy key)

```bash
cd /home/ali/Documents/repos/bb.git/fix-paginaton

jq '.paths["/repositories/{workspace}/{repo_slug}/deploy-keys"].post.requestBody = {
  "required": true,
  "description": "The deploy key to create.",
  "content": {
    "application/json": {
      "schema": {"$ref": "#/components/schemas/deploy_key"}
    }
  }
}' bb_cloud_fixed.openapi.json > /tmp/fixed.json && mv /tmp/fixed.json bb_cloud_fixed.openapi.json
```

### Step 2 — Add `requestBody` to PUT (update deploy key)

```bash
jq '.paths["/repositories/{workspace}/{repo_slug}/deploy-keys/{key_id}"].put.requestBody = {
  "required": true,
  "description": "The updated deploy key.",
  "content": {
    "application/json": {
      "schema": {"$ref": "#/components/schemas/deploy_key"}
    }
  }
}' bb_cloud_fixed.openapi.json > /tmp/fixed.json && mv /tmp/fixed.json bb_cloud_fixed.openapi.json
```

### Step 3 — Regenerate and verify

```bash
make generate-cloud && make diff-cloud
```

After regeneration, verify that `_get_kwargs` in both generated modules gains a `body: DeployKey` parameter and injects `_kwargs["json"] = body.to_dict()`.

---

## Tests that expose this bug
- `test_create_deploy_key_roundtrip` — fails with `TypeError`
- `test_create_deploy_key_visible_via_get` — fails with `TypeError`
- `test_update_deploy_key_roundtrip` — fails with `TypeError`
- `test_delete_deploy_key_removes_it` — fails with `TypeError` (create step)
