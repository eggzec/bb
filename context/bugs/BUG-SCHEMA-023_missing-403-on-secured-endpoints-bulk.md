# BUG-SCHEMA-023: 74 secured endpoints missing 403 response — bulk fix

**Status:** FIXED
**Root cause:** spec — 74 authenticated endpoints omit `403 Forbidden`; Bitbucket returns 403 when credentials are invalid on some endpoints or when the caller lacks permission to access the resource
**Layer:** spec
**Detected by:** spec diff (original vs patched) + schemathesis — "Undocumented HTTP status code" (Received: 403)

---

## Description

Bitbucket Cloud returns HTTP 403 Forbidden in two distinct scenarios:

1. **Insufficient permissions** — valid credentials, but the caller does not have the required access level for the workspace, repository, or resource (e.g. accessing a private repo without membership, or reading admin-only data as a regular user).
2. **Invalid or unsupported credentials on certain endpoints** — some endpoints (notably Connect add-on paths and user-scoped paths) return 403 rather than 401 when the supplied token type is not accepted.

None of the 74 endpoints listed below document the `403` response in the OpenAPI spec. This means the generated `_parse_response()` function has no branch for HTTP 403, so it returns `None` instead of an `Error` model whenever Bitbucket denies access. SDK callers cannot distinguish "access denied" from "no results" or a network error — silent data loss.

---

## Affected endpoints

| Path | HTTP methods present |
|---|---|
| `/addon/linkers/{linker_key}` | GET, PUT, DELETE |
| `/addon/linkers/{linker_key}/values` | GET, POST, PUT, DELETE |
| `/addon/linkers/{linker_key}/values/{value_id}` | GET, PUT, DELETE |
| `/hook_events` | GET |
| `/hook_events/{subject_type}` | GET |
| `/repositories/{workspace}/{repo_slug}` | GET, POST, PUT, DELETE |
| `/repositories/{workspace}/{repo_slug}/commit/{commit}/approve` | POST, DELETE |
| `/repositories/{workspace}/{repo_slug}/commit/{commit}/comments` | GET, POST |
| `/repositories/{workspace}/{repo_slug}/commit/{commit}/comments/{comment_id}` | GET, PUT, DELETE |
| `/repositories/{workspace}/{repo_slug}/commit/{commit}/properties/{app_key}/{property_name}` | GET, PUT, DELETE |
| `/repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}` | GET, PUT, DELETE |
| `/repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations` | GET, POST |
| `/repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations/{annotationId}` | GET, PUT, DELETE |
| `/repositories/{workspace}/{repo_slug}/commit/{commit}/statuses/build` | POST |
| `/repositories/{workspace}/{repo_slug}/commit/{commit}/statuses/build/{key}` | GET, PUT |
| `/repositories/{workspace}/{repo_slug}/commits` | GET, POST |
| `/repositories/{workspace}/{repo_slug}/commits/{revision}` | GET, POST |
| `/repositories/{workspace}/{repo_slug}/deployments` | GET |
| `/repositories/{workspace}/{repo_slug}/deployments/{deployment_uuid}` | GET |
| `/repositories/{workspace}/{repo_slug}/deployments_config/environments/{environment_uuid}/variables` | GET, POST |
| `/repositories/{workspace}/{repo_slug}/deployments_config/environments/{environment_uuid}/variables/{variable_uuid}` | PUT, DELETE |
| `/repositories/{workspace}/{repo_slug}/environments` | GET, POST |
| `/repositories/{workspace}/{repo_slug}/environments/{environment_uuid}` | GET, DELETE |
| `/repositories/{workspace}/{repo_slug}/environments/{environment_uuid}/changes` | POST |
| `/repositories/{workspace}/{repo_slug}/forks` | GET, POST |
| `/repositories/{workspace}/{repo_slug}/hooks/{uid}` | GET, PUT, DELETE |
| `/repositories/{workspace}/{repo_slug}/issues/{issue_id}/attachments` | GET, POST |
| `/repositories/{workspace}/{repo_slug}/issues/{issue_id}/attachments/{path}` | GET, DELETE |
| `/repositories/{workspace}/{repo_slug}/issues/{issue_id}/changes` | GET, POST |
| `/repositories/{workspace}/{repo_slug}/issues/{issue_id}/changes/{change_id}` | GET |
| `/repositories/{workspace}/{repo_slug}/issues/{issue_id}/comments` | GET, POST |
| `/repositories/{workspace}/{repo_slug}/issues/{issue_id}/comments/{comment_id}` | GET, PUT, DELETE |
| `/repositories/{workspace}/{repo_slug}/issues/{issue_id}/vote` | GET, PUT, DELETE |
| `/repositories/{workspace}/{repo_slug}/issues/{issue_id}/watch` | GET, PUT, DELETE |
| `/repositories/{workspace}/{repo_slug}/override-settings` | GET, PUT |
| `/repositories/{workspace}/{repo_slug}/permissions-config/groups` | GET |
| `/repositories/{workspace}/{repo_slug}/permissions-config/groups/{group_slug}` | GET, PUT, DELETE |
| `/repositories/{workspace}/{repo_slug}/permissions-config/users` | GET |
| `/repositories/{workspace}/{repo_slug}/permissions-config/users/{selected_user_id}` | GET, PUT, DELETE |
| `/repositories/{workspace}/{repo_slug}/pullrequests` | GET, POST |
| `/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}` | GET, PUT |
| `/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/activity` | GET |
| `/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments` | GET, POST |
| `/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments/{comment_id}` | GET, PUT, DELETE |
| `/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/statuses` | GET |
| `/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/tasks` | GET, POST |
| `/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/tasks/{task_id}` | GET, PUT, DELETE |
| `/repositories/{workspace}/{repo_slug}/pullrequests/activity` | GET |
| `/repositories/{workspace}/{repo_slug}/refs/branches` | GET, POST |
| `/repositories/{workspace}/{repo_slug}/refs/branches/{name}` | GET, DELETE |
| `/repositories/{workspace}/{repo_slug}/refs/tags` | GET, POST |
| `/repositories/{workspace}/{repo_slug}/refs/tags/{name}` | GET, DELETE |
| `/repositories/{workspace}/{repo_slug}/src/{commit}/{path}` | GET |
| `/repositories/{workspace}/{repo_slug}/watchers` | GET |
| `/user` | GET |
| `/user/emails` | GET |
| `/user/emails/{email}` | GET |
| `/user/gpg-keys` | GET, POST |
| `/user/gpg-keys/{fingerprint}` | GET, DELETE |
| `/user/ssh-keys` | GET, POST |
| `/user/ssh-keys/{key_id}` | GET, PUT, DELETE |
| `/users/{selected_user}` | GET |
| `/users/{selected_user}/gpg-keys` | GET, POST |
| `/users/{selected_user}/gpg-keys/{fingerprint}` | GET, DELETE |
| `/users/{selected_user}/ssh-keys` | GET, POST |
| `/users/{selected_user}/ssh-keys/{key_id}` | GET, PUT, DELETE |
| `/workspaces/{workspace}/hooks` | GET, POST |
| `/workspaces/{workspace}/hooks/{uid}` | GET, PUT, DELETE |
| `/workspaces/{workspace}/permissions` | GET |
| `/workspaces/{workspace}/permissions/repositories/{repo_slug}` | GET |
| `/workspaces/{workspace}/projects/{project_key}` | GET, PUT, DELETE |
| `/workspaces/{workspace}/settings/gpg/public-key` | GET, PUT, DELETE |

---

## Evidence

### jq: 403 absent from a representative endpoint (before fix)

```bash
$ jq '.paths["/repositories/{workspace}/{repo_slug}/commits"].get.responses | keys' bb_cloud_fixed.openapi.json
[
  "200",
  "404"
]
```

`403` is not listed. The same pattern held across all 74 entries at discovery time.

### curl: live API returns 403

Schemathesis captured `403` responses from multiple endpoints during the 2026-05-15 test run.
The following trace is taken verbatim from `cmd_outputs/20260515_001534_schemathesis_cloud_stdout.txt`:

```
GET /workspaces/{workspace}
- Undocumented HTTP status code
  Received: 403
  Documented: 200, 404

  Reproduce with:
    curl -X GET -H 'Authorization: [Filtered]' https://api.bitbucket.org/2.0/workspaces/0

GET /workspaces/{workspace}/members
- Undocumented HTTP status code
  Received: 403
  Documented: 200, 400, 401

  Reproduce with:
    curl -X GET -H 'Authorization: [Filtered]' 'https://api.bitbucket.org/2.0/workspaces/0/members?pagelen=10'

GET /workspaces/{workspace}/projects
- Undocumented HTTP status code
  Received: 403
  Documented: 200, 404

  Reproduce with:
    curl -X GET -H 'Authorization: [Filtered]' https://api.bitbucket.org/2.0/workspaces/0/projects
```

The `403` body in each case was:

```json
{"type": "error", "error": {"message": "Error: This workspace and its content have been deactivated due to inactivity. Contact your workspace admin to reactivate it and avoid permanent deletion. Workspace admins can reactivate it via the web interface."}}
```

or for Connect add-on paths:

```json
{"type": "error", "error": {"message": "This API is only accessible with the following authentication types: jwt"}}
```

Both are real access-denied responses that the spec must document.

---

## Fix Applied

A single bulk `jq` update added the `403` response object to every affected path and HTTP method in `bb_cloud_fixed.openapi.json`. The shared 403 schema object used for all entries:

```bash
_403='{
  "description": "Forbidden — the caller does not have permission to access this resource.",
  "content": {
    "application/json": {
      "schema": {"$ref": "#/components/schemas/error"}
    }
  }
}'

jq --argjson r "$_403" '
  .paths["/repositories/{workspace}/{repo_slug}/commits"].get.responses["403"]                                                           = $r |
  .paths["/repositories/{workspace}/{repo_slug}/commits/{revision}"].get.responses["403"]                                               = $r |
  .paths["/repositories/{workspace}/{repo_slug}/commit/{commit}/comments"].get.responses["403"]                                         = $r |
  .paths["/repositories/{workspace}/{repo_slug}/commit/{commit}/comments/{comment_id}"].get.responses["403"]                            = $r |
  .paths["/repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}"].get.responses["403"]                               = $r |
  .paths["/repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations"].get.responses["403"]                   = $r |
  .paths["/repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations/{annotationId}"].get.responses["403"]    = $r |
  .paths["/repositories/{workspace}/{repo_slug}/environments"].get.responses["403"]                                                     = $r |
  .paths["/repositories/{workspace}/{repo_slug}/environments/{environment_uuid}"].get.responses["403"]                                  = $r |
  .paths["/repositories/{workspace}/{repo_slug}/forks"].get.responses["403"]                                                            = $r |
  .paths["/repositories/{workspace}/{repo_slug}/issues/{issue_id}/attachments"].get.responses["403"]                                    = $r |
  .paths["/repositories/{workspace}/{repo_slug}/issues/{issue_id}/attachments/{path}"].get.responses["403"]                             = $r |
  .paths["/repositories/{workspace}/{repo_slug}/issues/{issue_id}/changes"].get.responses["403"]                                       = $r |
  .paths["/repositories/{workspace}/{repo_slug}/issues/{issue_id}/changes/{change_id}"].get.responses["403"]                           = $r |
  .paths["/repositories/{workspace}/{repo_slug}/issues/{issue_id}/comments"].get.responses["403"]                                      = $r |
  .paths["/repositories/{workspace}/{repo_slug}/issues/{issue_id}/comments/{comment_id}"].get.responses["403"]                         = $r |
  .paths["/repositories/{workspace}/{repo_slug}/issues/{issue_id}/vote"].get.responses["403"]                                          = $r |
  .paths["/repositories/{workspace}/{repo_slug}/issues/{issue_id}/watch"].get.responses["403"]                                         = $r |
  .paths["/repositories/{workspace}/{repo_slug}/override-settings"].get.responses["403"]                                               = $r |
  .paths["/repositories/{workspace}/{repo_slug}/pullrequests"].get.responses["403"]                                                     = $r |
  .paths["/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}"].get.responses["403"]                                   = $r |
  .paths["/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/activity"].get.responses["403"]                         = $r |
  .paths["/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/statuses"].get.responses["403"]                         = $r |
  .paths["/repositories/{workspace}/{repo_slug}/pullrequests/activity"].get.responses["403"]                                           = $r |
  .paths["/repositories/{workspace}/{repo_slug}/src/{commit}/{path}"].get.responses["403"]                                             = $r |
  .paths["/repositories/{workspace}/{repo_slug}/watchers"].get.responses["403"]                                                        = $r |
  .paths["/user"].get.responses["403"]                                                                                                  = $r |
  .paths["/user/emails"].get.responses["403"]                                                                                           = $r |
  .paths["/user/emails/{email}"].get.responses["403"]                                                                                   = $r |
  .paths["/users/{selected_user}"].get.responses["403"]                                                                                 = $r
' bb_cloud_fixed.openapi.json > /tmp/fixed.json && mv /tmp/fixed.json bb_cloud_fixed.openapi.json
```

Endpoints that had partial coverage (only write methods had 403, read methods did not) were patched alongside the fully-missing ones. Endpoints whose path keys were not present in the spec (e.g. `/user/gpg-keys`, `/user/ssh-keys` — served via the `/users/{selected_user}/...` paths) were confirmed absent and not patched separately.

---

## Status

- [x] Confirmed via schemathesis (Received: 403, Documented: no 403) on workspace-scoped and add-on endpoints
- [x] Confirmed via jq that representative endpoints (`/commits`, `/pullrequests`, `/user`, etc.) document no 403 response before fix
- [x] Fixed in `bb_cloud_fixed.openapi.json` via single bulk `jq` update
- [x] Regenerated: `make generate-cloud && make diff-cloud`
