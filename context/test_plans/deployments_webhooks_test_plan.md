# Test Plan — deployments / webhooks

**Workspace:** beaverish
**Probe repo:** bb-probe

**Seed data — Environments:**
- Environment "Test": UUID `{697d8906-4609-448e-85f1-6b05d5c9faa9}`
- Environment "Staging": UUID `{13053a34-e7a9-49c0-9647-f748f576208d}`
- Env variable in Test: UUID `{bbab80d0-4e11-4d66-96e9-e74cb47e981a}` (key: DEPLOY_VAR)

**Seed data — Deploy keys:**
- Deploy key id: `10958984` (label: `probe-deploy-key`)

**Seed data — Webhooks:**
- Repo webhook UUID: `{842a6a21-5169-4b95-90c2-57337ff53e18}` (url: `https://example.com/probe-webhook`)
- Workspace webhook UUID: `{b71bcb12-c9de-49e5-9d8e-e08738571d66}` (url: `https://example.com/probe-ws-webhook`)

---

## Module: `bb.cloud.sdk.deployments` (16 functions)

| # | Test ID | Function | Scenario | Expected | Status |
|---|---------|----------|----------|----------|--------|
| 1 | `test_list_returns_list` | `list` | bb-probe (pipelines may not have run) | Returns `list[Deployment]` — may be empty; no exception | PENDING |
| 2 | `test_list_items_are_deployment_type` | `list` | all items from list | Every item is a `Deployment` instance | PENDING |
| 3 | `test_get_nonexistent_deployment_is_none` | `get` | fake UUID that doesn't exist | Returns `None` or `Error`, NOT a `Deployment` | PENDING |
| 4 | `test_envs_returns_list` | `envs` | bb-probe | Returns `list[DeploymentEnvironment]`; non-empty | PENDING |
| 5 | `test_envs_contains_test_env` | `envs` | bb-probe | Environment named "Test" is present | PENDING |
| 6 | `test_envs_contains_staging_env` | `envs` | bb-probe | Environment named "Staging" is present | PENDING |
| 7 | `test_envs_items_have_uuid_and_name` | `envs` | all items | Every item has uuid and name set (not UNSET) | PENDING |
| 8 | `test_get_env_returns_test_env` | `get_env` | UUID `{697d8906-...}` | Returns `DeploymentEnvironment` with name=="Test" | PENDING |
| 9 | `test_get_env_nonexistent_is_error_or_none` | `get_env` | fake UUID | Returns `Error` or `None`, NOT a `DeploymentEnvironment` | PENDING |
| 10 | `test_create_env_roundtrip` | `create_env` | create "bb-test-env-<uuid>" | Returns `DeploymentEnvironment`; name matches | PENDING |
| 11 | `test_create_env_visible_via_get` | `create_env` + `get_env` | created env | Immediately visible via get_env | PENDING |
| 12 | `test_update_env_roundtrip` | `update_env` | update name on throwaway | Returns None (202 Accepted, async); get shows change eventually | FAIL (BUG-DEPLOY-002: TypeError — generated API has no `body` param) |
| 13 | `test_delete_env_removes_it` | `delete_env` | delete throwaway | get_env returns None or Error afterward | PENDING |
| 14 | `test_deploy_keys_returns_list` | `deploy_keys` | bb-probe | Returns `list[DeployKey]`; non-empty | PENDING |
| 15 | `test_deploy_keys_contains_seed_key` | `deploy_keys` | bb-probe | Key with id=10958984 is present | PENDING |
| 16 | `test_get_deploy_key_returns_seed_key` | `get_deploy_key` | id=10958984 | Returns `DeployKey` with label=="probe-deploy-key" | PENDING |
| 17 | `test_get_deploy_key_nonexistent_is_error_or_none` | `get_deploy_key` | id=999999999 | Returns `Error` or `None` | PENDING |
| 18 | `test_create_deploy_key_roundtrip` | `create_deploy_key` | unique RSA test key | Returns `DeployKey`; id is set; label matches | FAIL (BUG-DEPLOY-001: TypeError — generated API has no `body` param) |
| 19 | `test_create_deploy_key_visible_via_get` | `create_deploy_key` + `get_deploy_key` | created key | Immediately visible via get_deploy_key | FAIL (BUG-DEPLOY-001: TypeError — generated API has no `body` param) |
| 20 | `test_update_deploy_key_roundtrip` | `update_deploy_key` | update label | Returns `DeployKey` with new label | FAIL (BUG-DEPLOY-001: TypeError — generated API has no `body` param) |
| 21 | `test_delete_deploy_key_removes_it` | `delete_deploy_key` | delete throwaway | get_deploy_key returns None or Error afterward | FAIL (BUG-DEPLOY-001: TypeError in create step) |
| 22 | `test_env_variables_returns_list` | `env_variables` | Test env | Returns list; DEPLOY_VAR present | PENDING |
| 23 | `test_env_variables_contains_deploy_var` | `env_variables` | Test env | UUID `{bbab80d0-...}` or key "DEPLOY_VAR" found | PENDING |
| 24 | `test_create_env_variable_roundtrip` | `create_env_variable` | new var in Test env | Returns `DeploymentVariable`; uuid is set | PENDING |
| 25 | `test_update_env_variable_roundtrip` | `update_env_variable` | update value | Returns `DeploymentVariable` with updated value | PENDING |
| 26 | `test_delete_env_variable_removes_it` | `delete_env_variable` | delete throwaway | variable no longer in list | PENDING |

---

## Module: `bb.cloud.sdk.webhooks` (11 functions)

| # | Test ID | Function | Scenario | Expected | Status |
|---|---------|----------|----------|----------|--------|
| 1 | `test_list_repo_returns_list` | `list_repo` | bb-probe | Returns `list[WebhookSubscription]`; non-empty | PENDING |
| 2 | `test_list_repo_contains_seed_webhook` | `list_repo` | bb-probe | UUID `{842a6a21-...}` present | PENDING |
| 3 | `test_get_repo_webhook_returns_seed` | `get_repo` | uid=`{842a6a21-...}` | Returns `WebhookSubscription` with url=="https://example.com/probe-webhook" | PENDING |
| 4 | `test_get_repo_webhook_nonexistent_is_error_or_none` | `get_repo` | fake uid | Returns `Error` or `None` | PENDING |
| 5 | `test_create_repo_webhook_roundtrip` | `create_repo` | unique URL | Returns `WebhookSubscription`; uuid is set | FAIL (BUG-WEBHOOKS-001: TypeError — generated API has no `body` param) |
| 6 | `test_create_repo_webhook_visible_via_get` | `create_repo` + `get_repo` | created hook | Immediately visible via get_repo | FAIL (BUG-WEBHOOKS-001: TypeError — generated API has no `body` param) |
| 7 | `test_update_repo_webhook_roundtrip` | `update_repo` | update description | Returns `WebhookSubscription` with new description | FAIL (BUG-WEBHOOKS-001: TypeError — generated API has no `body` param) |
| 8 | `test_delete_repo_webhook_removes_it` | `delete_repo` | delete throwaway | get_repo returns None or Error afterward | FAIL (BUG-WEBHOOKS-001: TypeError in create step) |
| 9 | `test_list_workspace_returns_list` | `list_workspace` | beaverish | Returns `list[WebhookSubscription]`; non-empty | PENDING |
| 10 | `test_list_workspace_contains_seed_webhook` | `list_workspace` | beaverish | UUID `{b71bcb12-...}` present | PENDING |
| 11 | `test_get_workspace_webhook_returns_seed` | `get_workspace` | uid=`{b71bcb12-...}` | Returns `WebhookSubscription` with url=="https://example.com/probe-ws-webhook" | PENDING |
| 12 | `test_get_workspace_webhook_nonexistent_is_error_or_none` | `get_workspace` | fake uid | Returns `Error` or `None` | PENDING |
| 13 | `test_create_workspace_webhook_roundtrip` | `create_workspace` | unique URL | Returns `WebhookSubscription`; uuid is set | FAIL (BUG-WEBHOOKS-001: TypeError — generated API has no `body` param) |
| 14 | `test_create_workspace_webhook_visible_via_get` | `create_workspace` + `get_workspace` | created hook | Immediately visible via get_workspace | FAIL (BUG-WEBHOOKS-001: TypeError — generated API has no `body` param) |
| 15 | `test_update_workspace_webhook_roundtrip` | `update_workspace` | update description | Returns `WebhookSubscription` with new description | FAIL (BUG-WEBHOOKS-001: TypeError — generated API has no `body` param) |
| 16 | `test_delete_workspace_webhook_removes_it` | `delete_workspace` | delete throwaway | get_workspace returns None or Error afterward | FAIL (BUG-WEBHOOKS-001: TypeError in create step) |
| 17 | `test_events_repository_returns_list` | `events` | subject_type=REPOSITORY | Returns non-empty `list[HookEvent]`; every item has .event set | PENDING |
| 18 | `test_events_workspace_returns_list` | `events` | subject_type=WORKSPACE | Returns non-empty `list[HookEvent]`; every item has .event set | PENDING |

---

## Notes on edge cases

### Deployments
- `list` may return an empty list if pipelines have never run on bb-probe — test must not fail for empty list
- `get` on a nonexistent UUID should return `None` or `Error`, never raise an exception
- `update_env` calls the `/environments/{uuid}/changes` endpoint which returns 202 Accepted (async update); the SDK returns `None` (not a `DeploymentEnvironment`)
- Deploy key `key` field must be a valid SSH public key (RSA/Ed25519); use a known-good test public key that has never been registered
- Duplicate deploy key (same public key content) returns 400 — test should detect `Error` not crash
- Duplicate environment name may return 409 — test should detect `Error`

### Webhooks
- `create_repo` and `create_workspace` use unique URLs (`https://example.com/test-<uuid>`) to prevent duplicates
- After `delete_repo` / `delete_workspace`, `get_repo` / `get_workspace` should return `None` or `Error`; the SDK returns `None` for 404
- `events` is a static list endpoint — no write operations needed; test both REPOSITORY and WORKSPACE subject types
- `update_repo` / `update_workspace` require the full webhook body (url + events) — must supply them in the PUT body

---

## Cross-cutting concerns
- Throwaway resources always cleaned up in `finally` blocks
- Unique names use `uuid.uuid4().hex[:8]` to avoid collisions
- Webhook URLs use `https://example.com/test-<uuid>` format
- Deploy key uniqueness enforced by using a distinct RSA public key per test run (embed key bits that include a uuid-based comment suffix)
- Never assert on `id` fields of newly created resources without first receiving them from the API response
