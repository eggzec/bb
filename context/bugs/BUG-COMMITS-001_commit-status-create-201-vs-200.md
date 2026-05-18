# BUG-COMMITS-001: commit_statuses.create returns None when API responds with 200

**Module:** commit_statuses
**Function:** create
**Tags:** [spec, generator]

## Symptom

`commit_statuses.create(...)` returns `None` instead of a `Commitstatus` object.
The test `test_create_throwaway_status` will assert `result is not None` and fail
with the message:

```
commit_statuses.create returned None — possible HTTP 200 vs 201 mismatch.
The generated parser only accepts 201; if the live API returned 200
the response was silently discarded.
```

## Initial theory

The Bitbucket Cloud spec documents `POST /repositories/{workspace}/{repo_slug}/commit/{commit}/statuses/build`
as returning `201 Created`. The generated `_parse_response` in
`src/bb/cloud/api/commit_statuses/post_repositories_workspace_repo_slug_commit_commit_statuses_build.py`
only handles `status_code == 201`:

```python
if response.status_code == 201:
    response_201 = Commitstatus.from_dict(response.json())
    return response_201
```

If the live Bitbucket API actually returns `200 OK` (which it does for upsert/idempotent
behaviour on keys that already exist), `_parse_response` falls through to
`raise errors.UnexpectedStatus(response.status_code, response.content)`.

The SDK wrapper absorbs `UnexpectedStatus` implicitly only if the generated `asyncio()`
returns `None` (which it does when the response is not parsed). However, `asyncio()`
calls `asyncio_detailed()` and returns `parsed` from the response — if `_parse_response`
raises, it propagates. If the HTTP response is simply not in the handled list, the
generator raises `UnexpectedStatus`.

Net effect: creating a status that already exists (same key) may return `200` and the
SDK will raise `UnexpectedStatus(200, ...)`.

## Steps to reproduce (curl)

```bash
# First call — creates, returns 201:
curl -s -X POST \
  -H "Authorization: Basic $(echo -n "$BB_EMAIL:$BB_TOKEN" | base64)" \
  -H "Content-Type: application/json" \
  "https://api.bitbucket.org/2.0/repositories/beaverish/bb-probe/commit/84952fad87fb39e3c6d61811a93769378dd4fad7/statuses/build" \
  -d '{"type":"build","key":"bb-test-probe-key","state":"INPROGRESS","url":"https://example.com"}' \
  -w "\nHTTP %{http_code}\n"

# Second call — same key, may return 200 (upsert):
curl -s -X POST \
  -H "Authorization: Basic $(echo -n "$BB_EMAIL:$BB_TOKEN" | base64)" \
  -H "Content-Type: application/json" \
  "https://api.bitbucket.org/2.0/repositories/beaverish/bb-probe/commit/84952fad87fb39e3c6d61811a93769378dd4fad7/statuses/build" \
  -d '{"type":"build","key":"bb-test-probe-key","state":"INPROGRESS","url":"https://example.com"}' \
  -w "\nHTTP %{http_code}\n"
```

## Fix recommendation

### Option A (preferred) — patch spec and regenerate

In `bb_cloud_fixed.openapi.json`, add `200` as an additional response for
`POST /repositories/{workspace}/{repo_slug}/commit/{commit}/statuses/build`:

```bash
jq '.paths["/repositories/{workspace}/{repo_slug}/commit/{commit}/statuses/build"].post.responses["200"] = {"description":"Commit status upserted","content":{"application/json":{"schema":{"$ref":"#/components/schemas/commitstatus"}}}}' \
  bb_cloud_fixed.openapi.json > /tmp/fixed.json && mv /tmp/fixed.json bb_cloud_fixed.openapi.json
make generate-cloud && make diff-cloud
```

### Option B — SDK-level workaround

Catch `UnexpectedStatus(200, ...)` in `commit_statuses.create` and parse the body
manually. Not recommended because it bypasses the generated layer.

**Status:** CONFIRMED by curl (2026-05-15).

First POST (new key) → HTTP 201 ✓  
Second POST (same key, upsert) → HTTP 200 — spec only documents 201, so `_parse_response` returns `None` and the SDK silently loses the response body on any upsert call.

**Fix:** Add `200` response to spec for this endpoint and regenerate:
```bash
jq '.paths["/repositories/{workspace}/{repo_slug}/commit/{commit}/statuses/build"].post.responses["200"] = {
  "description": "The commit status was updated (upsert).",
  "content": {"application/json": {"schema": {"$ref": "#/components/schemas/commitstatus"}}}
}' bb_cloud_fixed.openapi.json > /tmp/fixed.json && mv /tmp/fixed.json bb_cloud_fixed.openapi.json
make generate-cloud && make diff-cloud
```
