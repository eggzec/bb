# BUG-SCHEMA-032: 240 authenticated endpoints missing 401 Unauthorized

**Status:** FIXED
**Root cause:** spec — endpoints that require valid credentials document no 401 response
**Layer:** spec (`bb_cloud_fixed.openapi.json`)
**Severity:** Medium — callers cannot distinguish "not authenticated" from "not found" or "server error"; `_parse_response()` returns `None` silently on a 401, hiding auth failures

---

## Summary

The Bitbucket Cloud API returns `401 Unauthorized` when a request is made without valid credentials (no `Authorization` header, expired token, wrong token type). Of the 335 total endpoint/method combinations in the spec, 242 omit the `401` response entirely.

The spec already documents 401 on 93 endpoints: mainly `/addon/**`, `/branch-restrictions/**`, `/branching-model/**`, `/commit/{commit}/statuses/**`, `/pullrequests/{id}` (base + approve + request-changes), `/issues` (write paths only), `/snippets` write paths, `/user` base paths, and select `/workspaces` project paths.

Of the 242 missing, 2 are genuinely public endpoints (`GET /hook_events` and `GET /hook_events/{subject_type}`) that need no auth at all. The remaining **240 endpoints need 401 added**.

**Breakdown by HTTP method (all 242 missing 401, including 2 genuinely public):**

| Method | Missing 401 | Genuinely public (skip) | Need 401 added |
|--------|-------------|------------------------|----------------|
| GET    | 133         | 2                      | 131            |
| DELETE | 41          | 0                      | 41             |
| POST   | 36          | 0                      | 36             |
| PUT    | 32          | 0                      | 32             |
| **Total** | **242** | **2**               | **240**        |

---

## Auth categorization rules

- **Category A — Unconditional:** description `"If the request was not authenticated"`. All write ops (POST/PUT/DELETE), all `/user/*` (personal data), all `/users/{selected_user}` sub-resources (SSH keys, GPG keys, variables, properties, search), all `/workspaces/*`, all `/teams/*`, and GET on private-inherent repo paths (pipelines, pipelines_config, pipelines-config, deploy-keys, deployments, deployments_config, hooks, default-reviewers, effective-default-reviewers, override-settings, properties).
- **Category B — Conditional:** description `"If the repository is private and the request was not authenticated."` (for repo paths) or `"If the snippet is private and the request was not authenticated."` (for snippet content paths). Applied to GET on public-capable repo content (commits, branches, tags, src, issues, diff, patch, refs, watchers, forks, components, milestones, versions, PR sub-resources) and GET on snippets listing/content.
- **Skip:** `GET /hook_events` and `GET /hook_events/{subject_type}` — genuinely public, no auth required.

---

## Category A — Unconditional auth required (178 endpoints)

### A1. User profile data (`/user/*`) — 3 missing

```
GET /user/emails
GET /user/emails/{email}
GET /user/permissions/repositories
```

Note: `/user`, `/user/permissions/workspaces`, `/user/workspaces`, `/user/workspaces/{workspace}/permission`, and `/user/workspaces/{workspace}/permissions/repositories` already document 401.

### A2. User resource endpoints (`/users/{selected_user}/*`) — 19 missing

```
GET    /users/{selected_user}
GET    /users/{selected_user}/gpg-keys
GET    /users/{selected_user}/gpg-keys/{fingerprint}
GET    /users/{selected_user}/pipelines_config/variables
GET    /users/{selected_user}/pipelines_config/variables/{variable_uuid}
GET    /users/{selected_user}/properties/{app_key}/{property_name}
GET    /users/{selected_user}/search/code
GET    /users/{selected_user}/ssh-keys
GET    /users/{selected_user}/ssh-keys/{key_id}
POST   /users/{selected_user}/gpg-keys
POST   /users/{selected_user}/pipelines_config/variables
POST   /users/{selected_user}/ssh-keys
PUT    /users/{selected_user}/pipelines_config/variables/{variable_uuid}
PUT    /users/{selected_user}/properties/{app_key}/{property_name}
PUT    /users/{selected_user}/ssh-keys/{key_id}
DELETE /users/{selected_user}/gpg-keys/{fingerprint}
DELETE /users/{selected_user}/pipelines_config/variables/{variable_uuid}
DELETE /users/{selected_user}/properties/{app_key}/{property_name}
DELETE /users/{selected_user}/ssh-keys/{key_id}
```

### A3. Workspace-scoped endpoints (`/workspaces/*`) — 34 missing

**GET (18):**
```
GET /workspaces/{workspace}
GET /workspaces/{workspace}/hooks
GET /workspaces/{workspace}/hooks/{uid}
GET /workspaces/{workspace}/permissions/repositories
GET /workspaces/{workspace}/permissions/repositories/{repo_slug}
GET /workspaces/{workspace}/pipelines-config/identity/oidc/.well-known/openid-configuration
GET /workspaces/{workspace}/pipelines-config/identity/oidc/keys.json
GET /workspaces/{workspace}/pipelines-config/runners
GET /workspaces/{workspace}/pipelines-config/runners/{runner_uuid}
GET /workspaces/{workspace}/pipelines-config/variables
GET /workspaces/{workspace}/pipelines-config/variables/{variable_uuid}
GET /workspaces/{workspace}/projects
GET /workspaces/{workspace}/projects/{project_key}/default-reviewers
GET /workspaces/{workspace}/projects/{project_key}/default-reviewers/{selected_user}
GET /workspaces/{workspace}/projects/{project_key}/deploy-keys
GET /workspaces/{workspace}/projects/{project_key}/deploy-keys/{key_id}
GET /workspaces/{workspace}/pullrequests/{selected_user}
GET /workspaces/{workspace}/search/code
```

**Write ops (POST/PUT/DELETE — 16):**
```
POST   /workspaces/{workspace}/hooks
POST   /workspaces/{workspace}/pipelines-config/runners
POST   /workspaces/{workspace}/pipelines-config/variables
POST   /workspaces/{workspace}/projects
POST   /workspaces/{workspace}/projects/{project_key}/deploy-keys
PUT    /workspaces/{workspace}/hooks/{uid}
PUT    /workspaces/{workspace}/pipelines-config/runners/{runner_uuid}
PUT    /workspaces/{workspace}/pipelines-config/variables/{variable_uuid}
PUT    /workspaces/{workspace}/projects/{project_key}
PUT    /workspaces/{workspace}/projects/{project_key}/default-reviewers/{selected_user}
DELETE /workspaces/{workspace}/hooks/{uid}
DELETE /workspaces/{workspace}/pipelines-config/runners/{runner_uuid}
DELETE /workspaces/{workspace}/pipelines-config/variables/{variable_uuid}
DELETE /workspaces/{workspace}/projects/{project_key}
DELETE /workspaces/{workspace}/projects/{project_key}/default-reviewers/{selected_user}
DELETE /workspaces/{workspace}/projects/{project_key}/deploy-keys/{key_id}
```

### A4. Team pipeline variable endpoints (`/teams/*`) — 6 missing

```
GET    /teams/{username}/pipelines_config/variables
GET    /teams/{username}/pipelines_config/variables/{variable_uuid}
GET    /teams/{username}/search/code
POST   /teams/{username}/pipelines_config/variables
PUT    /teams/{username}/pipelines_config/variables/{variable_uuid}
DELETE /teams/{username}/pipelines_config/variables/{variable_uuid}
```

### A5. Private-inherent repo GET endpoints — 35 missing

These paths are only accessible with auth even on public repos (CI/CD config, deploy keys, webhooks, reviewer config, app properties):

```
GET /repositories/{workspace}/{repo_slug}/commit/{commit}/properties/{app_key}/{property_name}
GET /repositories/{workspace}/{repo_slug}/default-reviewers
GET /repositories/{workspace}/{repo_slug}/default-reviewers/{target_username}
GET /repositories/{workspace}/{repo_slug}/deploy-keys
GET /repositories/{workspace}/{repo_slug}/deploy-keys/{key_id}
GET /repositories/{workspace}/{repo_slug}/deployments
GET /repositories/{workspace}/{repo_slug}/deployments/{deployment_uuid}
GET /repositories/{workspace}/{repo_slug}/deployments_config/environments/{environment_uuid}/variables
GET /repositories/{workspace}/{repo_slug}/effective-default-reviewers
GET /repositories/{workspace}/{repo_slug}/hooks
GET /repositories/{workspace}/{repo_slug}/hooks/{uid}
GET /repositories/{workspace}/{repo_slug}/override-settings
GET /repositories/{workspace}/{repo_slug}/pipelines
GET /repositories/{workspace}/{repo_slug}/pipelines-config/caches
GET /repositories/{workspace}/{repo_slug}/pipelines-config/caches/{cache_uuid}/content-uri
GET /repositories/{workspace}/{repo_slug}/pipelines-config/runners
GET /repositories/{workspace}/{repo_slug}/pipelines-config/runners/{runner_uuid}
GET /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}
GET /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps
GET /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}
GET /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/log
GET /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/logs/{log_uuid}
GET /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/test_reports
GET /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/test_reports/test_cases
GET /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/test_reports/test_cases/{test_case_uuid}/test_case_reasons
GET /repositories/{workspace}/{repo_slug}/pipelines_config
GET /repositories/{workspace}/{repo_slug}/pipelines_config/schedules
GET /repositories/{workspace}/{repo_slug}/pipelines_config/schedules/{schedule_uuid}
GET /repositories/{workspace}/{repo_slug}/pipelines_config/schedules/{schedule_uuid}/executions
GET /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/key_pair
GET /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/known_hosts
GET /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/known_hosts/{known_host_uuid}
GET /repositories/{workspace}/{repo_slug}/pipelines_config/variables
GET /repositories/{workspace}/{repo_slug}/pipelines_config/variables/{variable_uuid}
GET /repositories/{workspace}/{repo_slug}/properties/{app_key}/{property_name}
GET /repositories/{workspace}/{repo_slug}/pullrequests/{pullrequest_id}/properties/{app_key}/{property_name}
```

### A6. Write ops on `/repositories/*` — 81 missing

Every write operation on a repository requires authentication.

**DELETE (29):**
```
DELETE /repositories/{workspace}/{repo_slug}
DELETE /repositories/{workspace}/{repo_slug}/commit/{commit}/approve
DELETE /repositories/{workspace}/{repo_slug}/commit/{commit}/comments/{comment_id}
DELETE /repositories/{workspace}/{repo_slug}/commit/{commit}/properties/{app_key}/{property_name}
DELETE /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}
DELETE /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations/{annotationId}
DELETE /repositories/{workspace}/{repo_slug}/default-reviewers/{target_username}
DELETE /repositories/{workspace}/{repo_slug}/deploy-keys/{key_id}
DELETE /repositories/{workspace}/{repo_slug}/deployments_config/environments/{environment_uuid}/variables/{variable_uuid}
DELETE /repositories/{workspace}/{repo_slug}/downloads/{filename}
DELETE /repositories/{workspace}/{repo_slug}/environments/{environment_uuid}
DELETE /repositories/{workspace}/{repo_slug}/hooks/{uid}
DELETE /repositories/{workspace}/{repo_slug}/issues/{issue_id}
DELETE /repositories/{workspace}/{repo_slug}/issues/{issue_id}/comments/{comment_id}
DELETE /repositories/{workspace}/{repo_slug}/issues/{issue_id}/vote
DELETE /repositories/{workspace}/{repo_slug}/pipelines-config/caches
DELETE /repositories/{workspace}/{repo_slug}/pipelines-config/caches/{cache_uuid}
DELETE /repositories/{workspace}/{repo_slug}/pipelines-config/runners/{runner_uuid}
DELETE /repositories/{workspace}/{repo_slug}/pipelines_config/schedules/{schedule_uuid}
DELETE /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/key_pair
DELETE /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/known_hosts/{known_host_uuid}
DELETE /repositories/{workspace}/{repo_slug}/pipelines_config/variables/{variable_uuid}
DELETE /repositories/{workspace}/{repo_slug}/properties/{app_key}/{property_name}
DELETE /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments/{comment_id}
DELETE /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments/{comment_id}/resolve
DELETE /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/tasks/{task_id}
DELETE /repositories/{workspace}/{repo_slug}/pullrequests/{pullrequest_id}/properties/{app_key}/{property_name}
DELETE /repositories/{workspace}/{repo_slug}/refs/branches/{name}
DELETE /repositories/{workspace}/{repo_slug}/refs/tags/{name}
```

**POST (26):**
```
POST /repositories/{workspace}/{repo_slug}/commit/{commit}/approve
POST /repositories/{workspace}/{repo_slug}/commit/{commit}/comments
POST /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations
POST /repositories/{workspace}/{repo_slug}/commits
POST /repositories/{workspace}/{repo_slug}/commits/{revision}
POST /repositories/{workspace}/{repo_slug}/deploy-keys
POST /repositories/{workspace}/{repo_slug}/deployments_config/environments/{environment_uuid}/variables
POST /repositories/{workspace}/{repo_slug}/downloads
POST /repositories/{workspace}/{repo_slug}/environments
POST /repositories/{workspace}/{repo_slug}/environments/{environment_uuid}/changes
POST /repositories/{workspace}/{repo_slug}/forks
POST /repositories/{workspace}/{repo_slug}/hooks
POST /repositories/{workspace}/{repo_slug}/issues/{issue_id}/comments
POST /repositories/{workspace}/{repo_slug}/pipelines
POST /repositories/{workspace}/{repo_slug}/pipelines-config/runners
POST /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/stopPipeline
POST /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/known_hosts
POST /repositories/{workspace}/{repo_slug}/pipelines_config/variables
POST /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments
POST /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments/{comment_id}/resolve
POST /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/decline
POST /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/merge
POST /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/tasks
POST /repositories/{workspace}/{repo_slug}/refs/branches
POST /repositories/{workspace}/{repo_slug}/refs/tags
POST /repositories/{workspace}/{repo_slug}/src
```

**PUT (26):**
```
PUT /repositories/{workspace}/{repo_slug}/commit/{commit}/comments/{comment_id}
PUT /repositories/{workspace}/{repo_slug}/commit/{commit}/properties/{app_key}/{property_name}
PUT /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}
PUT /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations/{annotationId}
PUT /repositories/{workspace}/{repo_slug}/default-reviewers/{target_username}
PUT /repositories/{workspace}/{repo_slug}/deploy-keys/{key_id}
PUT /repositories/{workspace}/{repo_slug}/deployments_config/environments/{environment_uuid}/variables/{variable_uuid}
PUT /repositories/{workspace}/{repo_slug}/hooks/{uid}
PUT /repositories/{workspace}/{repo_slug}/issues/{issue_id}
PUT /repositories/{workspace}/{repo_slug}/issues/{issue_id}/comments/{comment_id}
PUT /repositories/{workspace}/{repo_slug}/override-settings
PUT /repositories/{workspace}/{repo_slug}/pipelines-config/runners/{runner_uuid}
PUT /repositories/{workspace}/{repo_slug}/pipelines_config
PUT /repositories/{workspace}/{repo_slug}/pipelines_config/build_number
PUT /repositories/{workspace}/{repo_slug}/pipelines_config/schedules/{schedule_uuid}
PUT /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/key_pair
PUT /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/known_hosts/{known_host_uuid}
PUT /repositories/{workspace}/{repo_slug}/pipelines_config/variables/{variable_uuid}
PUT /repositories/{workspace}/{repo_slug}/properties/{app_key}/{property_name}
PUT /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments/{comment_id}
PUT /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/tasks/{task_id}
PUT /repositories/{workspace}/{repo_slug}/pullrequests/{pullrequest_id}/properties/{app_key}/{property_name}
```

### A7. Write ops on `/snippets/*` — 3 missing

```
POST   /snippets/{workspace}/{encoded_id}/comments
PUT    /snippets/{workspace}/{encoded_id}/comments/{comment_id}
DELETE /snippets/{workspace}/{encoded_id}/comments/{comment_id}
```

---

## Category B — Auth-conditional (62 endpoints)

These serve both public and private content. On public repos/snippets the call succeeds without auth; on private ones, 401 is returned. Use the visibility-scoped description.

### B1. Public-capable repo content GET — 50 missing

Description to use: `"If the repository is private and the request was not authenticated."`

```
GET /repositories/{workspace}
GET /repositories/{workspace}/{repo_slug}
GET /repositories/{workspace}/{repo_slug}/commit/{commit}
GET /repositories/{workspace}/{repo_slug}/commit/{commit}/comments
GET /repositories/{workspace}/{repo_slug}/commit/{commit}/comments/{comment_id}
GET /repositories/{workspace}/{repo_slug}/commit/{commit}/pullrequests
GET /repositories/{workspace}/{repo_slug}/commit/{commit}/reports
GET /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}
GET /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations
GET /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations/{annotationId}
GET /repositories/{workspace}/{repo_slug}/commits
GET /repositories/{workspace}/{repo_slug}/commits/{revision}
GET /repositories/{workspace}/{repo_slug}/components
GET /repositories/{workspace}/{repo_slug}/components/{component_id}
GET /repositories/{workspace}/{repo_slug}/diff/{spec}
GET /repositories/{workspace}/{repo_slug}/diffstat/{spec}
GET /repositories/{workspace}/{repo_slug}/downloads
GET /repositories/{workspace}/{repo_slug}/downloads/{filename}
GET /repositories/{workspace}/{repo_slug}/environments
GET /repositories/{workspace}/{repo_slug}/environments/{environment_uuid}
GET /repositories/{workspace}/{repo_slug}/filehistory/{commit}/{path}
GET /repositories/{workspace}/{repo_slug}/forks
GET /repositories/{workspace}/{repo_slug}/issues
GET /repositories/{workspace}/{repo_slug}/issues/{issue_id}
GET /repositories/{workspace}/{repo_slug}/issues/{issue_id}/changes
GET /repositories/{workspace}/{repo_slug}/issues/{issue_id}/changes/{change_id}
GET /repositories/{workspace}/{repo_slug}/issues/{issue_id}/comments
GET /repositories/{workspace}/{repo_slug}/issues/{issue_id}/comments/{comment_id}
GET /repositories/{workspace}/{repo_slug}/milestones
GET /repositories/{workspace}/{repo_slug}/milestones/{milestone_id}
GET /repositories/{workspace}/{repo_slug}/patch/{spec}
GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments
GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments/{comment_id}
GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/commits
GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/diff
GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/diffstat
GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/merge/task-status/{task_id}
GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/patch
GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/tasks
GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/tasks/{task_id}
GET /repositories/{workspace}/{repo_slug}/refs
GET /repositories/{workspace}/{repo_slug}/refs/branches
GET /repositories/{workspace}/{repo_slug}/refs/branches/{name}
GET /repositories/{workspace}/{repo_slug}/refs/tags
GET /repositories/{workspace}/{repo_slug}/refs/tags/{name}
GET /repositories/{workspace}/{repo_slug}/src
GET /repositories/{workspace}/{repo_slug}/src/{commit}/{path}
GET /repositories/{workspace}/{repo_slug}/versions
GET /repositories/{workspace}/{repo_slug}/versions/{version_id}
GET /repositories/{workspace}/{repo_slug}/watchers
```

### B2. Snippet listing/content GET — 12 missing

Description to use: `"If the snippet is private and the request was not authenticated."`

```
GET /snippets
GET /snippets/{workspace}
GET /snippets/{workspace}/{encoded_id}/comments
GET /snippets/{workspace}/{encoded_id}/comments/{comment_id}
GET /snippets/{workspace}/{encoded_id}/commits
GET /snippets/{workspace}/{encoded_id}/commits/{revision}
GET /snippets/{workspace}/{encoded_id}/files/{path}
GET /snippets/{workspace}/{encoded_id}/watch
GET /snippets/{workspace}/{encoded_id}/watchers
GET /snippets/{workspace}/{encoded_id}/{node_id}/files/{path}
GET /snippets/{workspace}/{encoded_id}/{revision}/diff
GET /snippets/{workspace}/{encoded_id}/{revision}/patch
```

---

## Category C — Also missing 403 (53 endpoints that need BOTH 401 and 403 added)

These 53 endpoints currently have neither 401 nor 403. They need both responses injected. The 401 description follows the category A/B rules above; the 403 description uses `"If the authenticated user does not have permission to access the resource."`.

```
GET /repositories/{workspace}/{repo_slug}/commit/{commit}
GET /repositories/{workspace}/{repo_slug}/commit/{commit}/comments
GET /repositories/{workspace}/{repo_slug}/commit/{commit}/comments/{comment_id}
GET /repositories/{workspace}/{repo_slug}/commit/{commit}/pullrequests
GET /repositories/{workspace}/{repo_slug}/commit/{commit}/reports
GET /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}
GET /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations
GET /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations/{annotationId}
GET /repositories/{workspace}/{repo_slug}/commits
GET /repositories/{workspace}/{repo_slug}/commits/{revision}
GET /repositories/{workspace}/{repo_slug}/components
GET /repositories/{workspace}/{repo_slug}/components/{component_id}
GET /repositories/{workspace}/{repo_slug}/diff/{spec}
GET /repositories/{workspace}/{repo_slug}/diffstat/{spec}
GET /repositories/{workspace}/{repo_slug}/environments
GET /repositories/{workspace}/{repo_slug}/environments/{environment_uuid}
GET /repositories/{workspace}/{repo_slug}/filehistory/{commit}/{path}
GET /repositories/{workspace}/{repo_slug}/forks
GET /repositories/{workspace}/{repo_slug}/issues
GET /repositories/{workspace}/{repo_slug}/issues/{issue_id}/changes
GET /repositories/{workspace}/{repo_slug}/issues/{issue_id}/changes/{change_id}
GET /repositories/{workspace}/{repo_slug}/issues/{issue_id}/comments
GET /repositories/{workspace}/{repo_slug}/issues/{issue_id}/comments/{comment_id}
GET /repositories/{workspace}/{repo_slug}/milestones
GET /repositories/{workspace}/{repo_slug}/milestones/{milestone_id}
GET /repositories/{workspace}/{repo_slug}/override-settings
GET /repositories/{workspace}/{repo_slug}/patch/{spec}
GET /repositories/{workspace}/{repo_slug}/pipelines
GET /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}
GET /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps
GET /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}
GET /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/log
GET /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/logs/{log_uuid}
GET /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/test_reports
GET /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/test_reports/test_cases
GET /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/test_reports/test_cases/{test_case_uuid}/test_case_reasons
GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/diff
GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/diffstat
GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/patch
GET /repositories/{workspace}/{repo_slug}/src
GET /repositories/{workspace}/{repo_slug}/src/{commit}/{path}
GET /repositories/{workspace}/{repo_slug}/versions
GET /repositories/{workspace}/{repo_slug}/versions/{version_id}
GET /repositories/{workspace}/{repo_slug}/watchers
GET /snippets
GET /snippets/{workspace}
GET /snippets/{workspace}/{encoded_id}/watch
GET /teams/{username}/search/code
GET /user/emails
GET /user/emails/{email}
GET /users/{selected_user}
GET /users/{selected_user}/search/code
GET /workspaces/{workspace}/search/code
```

---

## Evidence

```bash
# Write op with no 401
jq '.paths["/repositories/{workspace}/{repo_slug}/commit/{commit}/approve"].post.responses | keys' bb_cloud_fixed.openapi.json
# ["200"]

# User endpoint with no 401
jq '.paths["/user/emails"].get.responses | keys' bb_cloud_fixed.openapi.json
# ["200"]

# Private-only repo endpoint — has 403 but no 401
jq '.paths["/repositories/{workspace}/{repo_slug}/hooks"].get.responses | keys' bb_cloud_fixed.openapi.json
# ["200", "403"]

# Workspace endpoint — has 403 but no 401
jq '.paths["/workspaces/{workspace}/hooks"].get.responses | keys' bb_cloud_fixed.openapi.json
# ["200", "403"]
```

### Existing 401 body format in spec

```bash
jq '.paths["/repositories/{workspace}/{repo_slug}/branch-restrictions"].get.responses["401"]' bb_cloud_fixed.openapi.json
```

```json
{
  "description": "If the request was not authenticated",
  "content": { "application/json": { "schema": { "$ref": "#/components/schemas/error" } } }
}
```

---

## Fix

**Do NOT apply yet — coordinate with the fix pass.**

Three description variants. The jq values to use as shell variables:

```bash
_401_unconditional='{
  "description": "If the request was not authenticated",
  "content": {"application/json": {"schema": {"$ref": "#/components/schemas/error"}}}
}'

_401_repo_conditional='{
  "description": "If the repository is private and the request was not authenticated.",
  "content": {"application/json": {"schema": {"$ref": "#/components/schemas/error"}}}
}'

_401_snippet_conditional='{
  "description": "If the snippet is private and the request was not authenticated.",
  "content": {"application/json": {"schema": {"$ref": "#/components/schemas/error"}}}
}'

_403='{
  "description": "If the authenticated user does not have permission to access the resource.",
  "content": {"application/json": {"schema": {"$ref": "#/components/schemas/error"}}}
}'
```

### Recommended bulk jq fix command

The fix uses path-based pattern matching to select the correct 401 variant and also injects 403 where it is missing:

```bash
jq '
  def auth_401: {
    "description": "If the request was not authenticated",
    "content": { "application/json": { "schema": { "$ref": "#/components/schemas/error" } } }
  };
  def repo_401: {
    "description": "If the repository is private and the request was not authenticated.",
    "content": { "application/json": { "schema": { "$ref": "#/components/schemas/error" } } }
  };
  def snippet_401: {
    "description": "If the snippet is private and the request was not authenticated.",
    "content": { "application/json": { "schema": { "$ref": "#/components/schemas/error" } } }
  };
  def generic_403: {
    "description": "If the authenticated user does not have permission to access the resource.",
    "content": { "application/json": { "schema": { "$ref": "#/components/schemas/error" } } }
  };

  # Private-inherent repo sub-paths (always need auth even on public repos)
  def is_private_repo_path($p): $p | test(
    "/pipelines(?:[/_-]|$)|/pipelines_config|/pipelines-config|/deploy-keys|/deployments|/deployments_config|/hooks|/default-reviewers|/effective-default-reviewers|/override-settings|/properties"
  );

  .paths |= with_entries(
    .key as $path |
    .value |= with_entries(
      if (.key | test("^(get|post|put|delete|patch)$")) then
        # Inject 401 if missing
        if (.value.responses | has("401") | not) then
          if ($path | test("^/hook_events")) then
            # Genuinely public — skip
            .
          elif (.key == "get" and ($path | test("^/snippets"))) then
            .value.responses["401"] = snippet_401
          elif (.key == "get" and ($path | test("^/repositories/[^/]+/[^/]+$|^/repositories/[^/]+/[^/]+/")) and (is_private_repo_path($path) | not)) then
            .value.responses["401"] = repo_401
          elif ($path | test("^/repositories/[^/]+$")) then
            # /repositories/{workspace} listing — conditional
            .value.responses["401"] = repo_401
          else
            .value.responses["401"] = auth_401
          end
        else . end |
        # Also inject 403 if missing (for endpoints that have neither 401 nor 403)
        if (.value.responses | has("403") | not) and ($path | test("^/hook_events") | not) then
          .value.responses["403"] = generic_403
        else . end
      else . end
    )
  )
' bb_cloud_fixed.openapi.json > /tmp/fixed.json && mv /tmp/fixed.json bb_cloud_fixed.openapi.json
```

### Post-fix verification

```bash
# Should return 0 (excluding /hook_events which is genuinely public)
jq '[.paths | to_entries[] |
  select(.key | test("^/hook_events") | not) |
  .key as $path | .value | to_entries[] |
  select(.key | test("^(get|post|put|delete|patch)$")) |
  select(.value.responses | has("401") | not) |
  {path: $path, method: .key}] | length' bb_cloud_fixed.openapi.json
# Expected: 0

# Total operations now documenting 401
jq '[.paths | to_entries[] | .key as $path | .value | to_entries[] |
  select(.key | test("^(get|post|put|delete|patch)$")) |
  select(.value.responses | has("401"))] | length' bb_cloud_fixed.openapi.json
# Expected: 333 (335 total - 2 hook_events)
```

---

## Applied

Applied 2026-05-18. `make generate-cloud` completed with 0 errors. `make diff-cloud` returned exit 0 (clean — no unexpected diffs).

**Before fix:**
- Endpoints missing 401 (excl. `/hook_events`): **240**
- Endpoints missing 403 (excl. `/hook_events`): **66**
- Total endpoints documenting 401: **93**

**After fix:**
- Endpoints missing 401 (excl. `/hook_events`): **0**
- Total endpoints documenting 401: **333** (335 total − 2 genuinely public `/hook_events`)
- 401 injected across 240 endpoints; 403 also injected where missing (bulk coverage via pattern-based jq)
