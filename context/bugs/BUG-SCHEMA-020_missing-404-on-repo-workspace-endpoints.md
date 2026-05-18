# BUG-SCHEMA-020: 27 repo-scoped endpoints missing 404 response

**Status:** FIXED
**Root cause:** spec — 27 repo-scoped GET endpoints omit `404 Not Found`; live API returns 404 when workspace or repo_slug does not exist
**Layer:** spec
**Detected by:** schemathesis — "Undocumented HTTP status code" (Received: 404)

---

## Affected endpoints

| Endpoint | Currently documented |
|---|---|
| `GET /repositories/{workspace}/{repo_slug}/commit/{commit}/comments` | 200 |
| `GET /repositories/{workspace}/{repo_slug}/commit/{commit}/comments/{comment_id}` | 200 |
| `GET /repositories/{workspace}/{repo_slug}/commit/{commit}/reports` | 200 |
| `GET /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations` | 200 |
| `GET /repositories/{workspace}/{repo_slug}/default-reviewers` | 200, 403 |
| `GET /repositories/{workspace}/{repo_slug}/deployments` | 200, 403 |
| `GET /repositories/{workspace}/{repo_slug}/deployments_config/environments/{environment_uuid}/variables` | 200, 403 |
| `GET /repositories/{workspace}/{repo_slug}/diff/{spec}` | 200, 555 |
| `GET /repositories/{workspace}/{repo_slug}/diffstat/{spec}` | 200, 555 |
| `GET /repositories/{workspace}/{repo_slug}/downloads` | 200, 402, 403 |
| `GET /repositories/{workspace}/{repo_slug}/effective-default-reviewers` | 200, 403 |
| `GET /repositories/{workspace}/{repo_slug}/environments` | 200 |
| `GET /repositories/{workspace}/{repo_slug}/forks` | 200 |
| `GET /repositories/{workspace}/{repo_slug}/issues/{issue_id}/comments` | 200 |
| `GET /repositories/{workspace}/{repo_slug}/issues/{issue_id}/comments/{comment_id}` | 200 |
| `GET /repositories/{workspace}/{repo_slug}/patch/{spec}` | 200, 555 |
| `GET /repositories/{workspace}/{repo_slug}/pipelines` | 200 |
| `GET /repositories/{workspace}/{repo_slug}/pipelines-config/runners` | 200, 403 |
| `GET /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps` | 200 |
| `GET /repositories/{workspace}/{repo_slug}/pipelines_config` | 200, 403 |
| `GET /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/known_hosts` | 200, 403 |
| `GET /repositories/{workspace}/{repo_slug}/pipelines_config/variables` | 200, 403 |
| `GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/diff` | 302 |
| `GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/diffstat` | 302 |
| `GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/merge/task-status/{task_id}` | 200, 400, 403, 409 |
| `GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/patch` | 302 |
| `GET /repositories/{workspace}/{repo_slug}/watchers` | 200 |

---

## Description

Schemathesis tests live endpoints using randomly generated path parameter values (`workspace=0`, `repo_slug=0`). These values reference non-existent workspaces and repositories, so the Bitbucket Cloud API returns HTTP 404 Not Found. None of these 27 endpoints document the `404` response code in the spec.

**Impact:** The generated `_parse_response()` for each endpoint has no branch for `404`, so it returns `None` instead of an `Error` model. SDK callers receiving `None` cannot distinguish "resource not found" from other error conditions.

---

## Evidence

Schemathesis captured (workspace=0, repo_slug=0 → non-existent → 404):

```
GET /repositories/{workspace}/{repo_slug}/environments
- Undocumented HTTP status code
  Received: 404
  Documented: 200

Reproduce with:
  curl -X GET -H 'Authorization: Basic <token>' \
    https://api.bitbucket.org/2.0/repositories/0/0/environments
  # → 404 {"type": "error", "error": {"message": "No workspace with identifier '0'."}}
```

This pattern is consistent across all 27 endpoints — the 404 is not specific to any single endpoint but is a systematic omission affecting all repo-scoped resources.

---

## Fix Applied

Added `404 Not Found` response to all 27 endpoints in `bb_cloud_fixed.openapi.json`:

```bash
_404='{"description":"Not Found — the repository or resource does not exist.","content":{"application/json":{"schema":{"$ref":"#/components/schemas/error"}}}}'
jq --argjson r "$_404" '
  .paths["/repositories/{workspace}/{repo_slug}/commit/{commit}/comments"].get.responses["404"] = $r |
  .paths["/repositories/{workspace}/{repo_slug}/commit/{commit}/comments/{comment_id}"].get.responses["404"] = $r |
  .paths["/repositories/{workspace}/{repo_slug}/commit/{commit}/reports"].get.responses["404"] = $r |
  .paths["/repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations"].get.responses["404"] = $r |
  .paths["/repositories/{workspace}/{repo_slug}/default-reviewers"].get.responses["404"] = $r |
  .paths["/repositories/{workspace}/{repo_slug}/deployments"].get.responses["404"] = $r |
  .paths["/repositories/{workspace}/{repo_slug}/deployments_config/environments/{environment_uuid}/variables"].get.responses["404"] = $r |
  .paths["/repositories/{workspace}/{repo_slug}/diff/{spec}"].get.responses["404"] = $r |
  .paths["/repositories/{workspace}/{repo_slug}/diffstat/{spec}"].get.responses["404"] = $r |
  .paths["/repositories/{workspace}/{repo_slug}/downloads"].get.responses["404"] = $r |
  .paths["/repositories/{workspace}/{repo_slug}/effective-default-reviewers"].get.responses["404"] = $r |
  .paths["/repositories/{workspace}/{repo_slug}/environments"].get.responses["404"] = $r |
  .paths["/repositories/{workspace}/{repo_slug}/forks"].get.responses["404"] = $r |
  .paths["/repositories/{workspace}/{repo_slug}/issues/{issue_id}/comments"].get.responses["404"] = $r |
  .paths["/repositories/{workspace}/{repo_slug}/issues/{issue_id}/comments/{comment_id}"].get.responses["404"] = $r |
  .paths["/repositories/{workspace}/{repo_slug}/patch/{spec}"].get.responses["404"] = $r |
  .paths["/repositories/{workspace}/{repo_slug}/pipelines"].get.responses["404"] = $r |
  .paths["/repositories/{workspace}/{repo_slug}/pipelines-config/runners"].get.responses["404"] = $r |
  .paths["/repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps"].get.responses["404"] = $r |
  .paths["/repositories/{workspace}/{repo_slug}/pipelines_config"].get.responses["404"] = $r |
  .paths["/repositories/{workspace}/{repo_slug}/pipelines_config/ssh/known_hosts"].get.responses["404"] = $r |
  .paths["/repositories/{workspace}/{repo_slug}/pipelines_config/variables"].get.responses["404"] = $r |
  .paths["/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/diff"].get.responses["404"] = $r |
  .paths["/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/diffstat"].get.responses["404"] = $r |
  .paths["/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/merge/task-status/{task_id}"].get.responses["404"] = $r |
  .paths["/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/patch"].get.responses["404"] = $r |
  .paths["/repositories/{workspace}/{repo_slug}/watchers"].get.responses["404"] = $r
' bb_cloud_fixed.openapi.json > /tmp/fixed.json && mv /tmp/fixed.json bb_cloud_fixed.openapi.json
```

---

## Status

- [x] Confirmed via schemathesis (random path params → 404 for non-existent resources)
- [x] Fixed in `bb_cloud_fixed.openapi.json`
- [x] Regenerated: `make generate-cloud && make diff-cloud`
