# BUG-WEBHOOKS-001: Webhook create/update SDK calls fail — generated API has no `body` parameter

**Status:** CONFIRMED via spec inspection (jq) + generated code analysis
**Root cause:** spec — `requestBody` is entirely absent from the OpenAPI spec for all four webhook write operations (two repo-scoped, two workspace-scoped)
**Layer:** `.paths["/repositories/{workspace}/{repo_slug}/hooks"].post.requestBody` (null), `.paths["/repositories/{workspace}/{repo_slug}/hooks/{uid}"].put.requestBody` (null), `.paths["/workspaces/{workspace}/hooks"].post.requestBody` (null), `.paths["/workspaces/{workspace}/hooks/{uid}"].put.requestBody` (null)

---

## Affected functions
- `bb.cloud.sdk.webhooks.create_repo`
- `bb.cloud.sdk.webhooks.update_repo`
- `bb.cloud.sdk.webhooks.create_workspace`
- `bb.cloud.sdk.webhooks.update_workspace`

---

## Spec inspection (jq findings)

```bash
jq '.paths | to_entries[] | select(.key | test("/hooks")) | {path: .key, post_requestBody: .value.post.requestBody, put_requestBody: .value.put.requestBody}' bb_cloud_fixed.openapi.json
```

Output:
```json
{
  "path": "/repositories/{workspace}/{repo_slug}/hooks",
  "post_requestBody": null,
  "put_requestBody": null
}
{
  "path": "/repositories/{workspace}/{repo_slug}/hooks/{uid}",
  "post_requestBody": null,
  "put_requestBody": null
}
{
  "path": "/workspaces/{workspace}/hooks",
  "post_requestBody": null,
  "put_requestBody": null
}
{
  "path": "/workspaces/{workspace}/hooks/{uid}",
  "post_requestBody": null,
  "put_requestBody": null
}
```

`requestBody` is **null (absent)** for all four endpoints. Confirmed by checking `jq '.paths["/repositories/{workspace}/{repo_slug}/hooks"].post | keys'` — returns `["description","responses","security","summary","tags","x-atlassian-auth-types","x-atlassian-oauth2-scopes"]` with no `requestBody` key.

The `webhook_subscription` schema exists:
```bash
jq '.components.schemas | to_entries[] | select(.key | test("[Ww]ebhook")) | .key' bb_cloud_fixed.openapi.json
# → "webhook_subscription", "paginated_webhook_subscriptions"
```

The `webhook_subscription` schema has properties: `uuid`, `url`, `description`, `subject_type`, `subject`, `active`, `created_at`, `events`, `secret_set`, `secret`.

---

## Live API confirmation (curl findings)

The spec's own operation descriptions include explicit curl examples with a JSON body:

**POST repo hooks** description (from spec):
```
curl -X POST -u credentials -H 'Content-Type: application/json'
  https://api.bitbucket.org/2.0/repositories/my-workspace/my-repo-slug/hooks
  -d '{"description": "Webhook Description", "url": "https://example.com/", "active": true,
       "events": ["repo:push", "issue:created", "issue:updated"]}'
```

**POST workspace hooks** description (from spec):
```
curl -X POST -u credentials -H 'Content-Type: application/json'
  https://api.bitbucket.org/2.0/workspaces/my-workspace/hooks
  -d '{"description": "Webhook Description", "url": "https://example.com/", "active": true, ...}'
```

**PUT repo/workspace hook**: mutable fields per spec descriptions are `description`, `url`, `secret`, `active`, `events`.

The live test helper confirms required body structure:
```python
def _minimal_webhook(url: str, description: str = "bb-sdk-test") -> WebhookSubscription:
    return WebhookSubscription(
        type_="webhook_subscription",
        url=url,
        description=description,
        active=True,
        events=[WebhookSubscriptionEventsItem.REPOPUSH],
    )
```

Posting without a body would return HTTP 400 — no `url` or `events` provided.

---

## Schema gap

Required fields per the live API (spec curl examples + `webhook_subscription` schema constraints):

| Field | POST (create) | PUT (update) | Notes |
|-------|--------------|-------------|-------|
| `url` | Required | Required | Must be a publicly reachable URI |
| `events` | Required | Required | Non-empty array; minItems: 1 |
| `description` | Optional | Optional | User-defined label |
| `active` | Optional | Optional | Defaults to true |
| `secret` | Optional | Optional | HMAC signing secret |

The `events` array items are validated against an enum of known Bitbucket event types.

---

## Generated code impact

All four generated modules have the same pattern — no `body` in `_get_kwargs`:

```python
# post_repositories_workspace_repo_slug_hooks.py
def _get_kwargs(workspace: str, repo_slug: str) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/repositories/{workspace}/{repo_slug}/hooks".format(...),
    }
    return _kwargs  # NO "_kwargs['json'] = body.to_dict()"
```

SDK wrappers pass `body=body` at call sites:
```python
# sdk/webhooks.py:170
result = await post_repositories_workspace_repo_slug_hooks.asyncio(
    workspace, repo_slug, client=client.auth, body=body  # body= not accepted
)
# sdk/webhooks.py:218
result = await put_repositories_workspace_repo_slug_hooks_uid.asyncio(
    workspace, repo_slug, uid, client=client.auth, body=body  # body= not accepted
)
# sdk/webhooks.py:379
result = await post_workspaces_workspace_hooks.asyncio(workspace, client=client.auth, body=body)
# sdk/webhooks.py:423
result = await put_workspaces_workspace_hooks_uid.asyncio(workspace, uid, client=client.auth, body=body)
```

At runtime all four raise:
```
TypeError: asyncio() got an unexpected keyword argument 'body'
```

---

## Exact fix

All four fixes must be applied atomically (chained jq commands or applied one-at-a-time). Apply in order:

### Step 1 — POST /repositories/{workspace}/{repo_slug}/hooks (create repo webhook)

```bash
cd /home/ali/Documents/repos/bb.git/fix-paginaton

jq '.paths["/repositories/{workspace}/{repo_slug}/hooks"].post.requestBody = {
  "required": true,
  "description": "The webhook subscription to create.",
  "content": {
    "application/json": {
      "schema": {"$ref": "#/components/schemas/webhook_subscription"}
    }
  }
}' bb_cloud_fixed.openapi.json > /tmp/fixed.json && mv /tmp/fixed.json bb_cloud_fixed.openapi.json
```

### Step 2 — PUT /repositories/{workspace}/{repo_slug}/hooks/{uid} (update repo webhook)

```bash
jq '.paths["/repositories/{workspace}/{repo_slug}/hooks/{uid}"].put.requestBody = {
  "required": true,
  "description": "The updated webhook subscription.",
  "content": {
    "application/json": {
      "schema": {"$ref": "#/components/schemas/webhook_subscription"}
    }
  }
}' bb_cloud_fixed.openapi.json > /tmp/fixed.json && mv /tmp/fixed.json bb_cloud_fixed.openapi.json
```

### Step 3 — POST /workspaces/{workspace}/hooks (create workspace webhook)

```bash
jq '.paths["/workspaces/{workspace}/hooks"].post.requestBody = {
  "required": true,
  "description": "The webhook subscription to create.",
  "content": {
    "application/json": {
      "schema": {"$ref": "#/components/schemas/webhook_subscription"}
    }
  }
}' bb_cloud_fixed.openapi.json > /tmp/fixed.json && mv /tmp/fixed.json bb_cloud_fixed.openapi.json
```

### Step 4 — PUT /workspaces/{workspace}/hooks/{uid} (update workspace webhook)

```bash
jq '.paths["/workspaces/{workspace}/hooks/{uid}"].put.requestBody = {
  "required": true,
  "description": "The updated webhook subscription.",
  "content": {
    "application/json": {
      "schema": {"$ref": "#/components/schemas/webhook_subscription"}
    }
  }
}' bb_cloud_fixed.openapi.json > /tmp/fixed.json && mv /tmp/fixed.json bb_cloud_fixed.openapi.json
```

### Step 5 — Regenerate and verify

```bash
make generate-cloud && make diff-cloud
```

After regeneration, verify that `_get_kwargs` in all four generated modules gains a `body: WebhookSubscription` parameter and injects `_kwargs["json"] = body.to_dict()`.

### Single-pass alternative (all four in one jq call)

```bash
jq '
  .paths["/repositories/{workspace}/{repo_slug}/hooks"].post.requestBody = {
    "required": true, "description": "The webhook subscription to create.",
    "content": {"application/json": {"schema": {"$ref": "#/components/schemas/webhook_subscription"}}}
  } |
  .paths["/repositories/{workspace}/{repo_slug}/hooks/{uid}"].put.requestBody = {
    "required": true, "description": "The updated webhook subscription.",
    "content": {"application/json": {"schema": {"$ref": "#/components/schemas/webhook_subscription"}}}
  } |
  .paths["/workspaces/{workspace}/hooks"].post.requestBody = {
    "required": true, "description": "The webhook subscription to create.",
    "content": {"application/json": {"schema": {"$ref": "#/components/schemas/webhook_subscription"}}}
  } |
  .paths["/workspaces/{workspace}/hooks/{uid}"].put.requestBody = {
    "required": true, "description": "The updated webhook subscription.",
    "content": {"application/json": {"schema": {"$ref": "#/components/schemas/webhook_subscription"}}}
  }
' bb_cloud_fixed.openapi.json > /tmp/fixed.json && mv /tmp/fixed.json bb_cloud_fixed.openapi.json
```

---

## Tests that expose this bug
- `test_create_repo_webhook_roundtrip` — fails with `TypeError`
- `test_create_repo_webhook_visible_via_get` — fails with `TypeError`
- `test_update_repo_webhook_roundtrip` — fails with `TypeError`
- `test_delete_repo_webhook_removes_it` — fails with `TypeError` (create step)
- `test_create_workspace_webhook_roundtrip` — fails with `TypeError`
- `test_create_workspace_webhook_visible_via_get` — fails with `TypeError`
- `test_update_workspace_webhook_roundtrip` — fails with `TypeError`
- `test_delete_workspace_webhook_removes_it` — fails with `TypeError` (create step)
