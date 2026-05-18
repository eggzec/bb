# BUG-PRS-005: `add_comment` always returns `None` — API returns 201 Created, spec only documents 200

**Status:** FIXED
**Root cause:** sdk-wrapper — `asyncio()` maps only documented status codes; live API returns 201 which is unmapped → `None`
**Layer:** sdk-wrapper

---

## Affected functions
- `bb.cloud.sdk.prs.add_comment`

---

## Description

`prs.add_comment` called `post_repositories_workspace_repo_slug_pullrequests_pull_request_id_comments.asyncio()`. The OpenAPI spec for `POST /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments` documents only a 200 response. The Bitbucket Cloud API returns **201 Created** when a PR comment is successfully created. The generator's `_parse_response()` only maps documented status codes — 200 → PullRequestComment — so the live 201 response is unmapped and `asyncio()` returns `None`.

The result: every successful `prs.add_comment()` call returned `None` instead of the created `PullRequestComment` object. The `isinstance(result, (PullRequestComment, Error))` guard in the original code was unreachable on success.

This is the same root cause as BUG-PIPELINES-008 (`create_known_host` missing 201) and BUG-COMMITS-001 (commit status upsert 200 vs 201).

**Relation to BUG-PRS-003:** BUG-PRS-003 documented the body type issue (`body: PullRequestComment | Unset = UNSET` → AttributeError on default). That body-type defect was resolved in a prior commit, making `add_comment` callable with a correct body. This bug (BUG-PRS-005) is a distinct and independent issue that remained after BUG-PRS-003 was resolved: even with a correct body supplied, the function always returned `None` because the 201 response was not handled.

---

## Evidence

**SDK wrapper before fix** (`src/bb/cloud/sdk/prs.py`, ~line 645):

```python
async def add_comment(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    body: PullRequestComment,
) -> PullRequestComment | Error | None:
    result = await post_repositories_workspace_repo_slug_pullrequests_pull_request_id_comments.asyncio(
        workspace, repo_slug, pull_request_id, client=client.auth, body=body
    )
    if isinstance(result, (PullRequestComment, Error)):
        return result
    return None
```

**SDK wrapper after fix:**

```python
async def add_comment(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    body: PullRequestComment,
) -> PullRequestComment | Error | None:
    response = await post_repositories_workspace_repo_slug_pullrequests_pull_request_id_comments.asyncio_detailed(
        workspace, repo_slug, pull_request_id, client=client.auth, body=body
    )
    if response.status_code.value in (200, 201):
        import json as _json
        return PullRequestComment.from_dict(_json.loads(response.content))
    if isinstance(response.parsed, Error):
        return response.parsed
    return None
```

---

## Root Cause

The generator's `_parse_response()` maps only status codes present in the spec. The spec documents 200 → PullRequestComment; the live API responds with 201 → PullRequestComment. Since 201 is absent from `_parse_response()`, `response.parsed` is `None` and `asyncio()` returns `None`.

The fix uses `asyncio_detailed()` to access the raw `response.status_code` and `response.content` bytes. Both 200 and 201 are treated as success; `PullRequestComment.from_dict(json.loads(response.content))` deserializes the body. Error responses fall through to `response.parsed` (typed as `Error` by the generator for 4xx status codes that are documented in the spec).

---

## Impact

- `prs.add_comment()` always returned `None` on success
- The `isinstance(result, PullRequestComment)` check in test code and callers was unreachable
- Live tests for PR comment creation and subsequent operations (update, delete) would fail because the created comment UUID was not returned

---

## Fix Applied

Switched from `asyncio()` to `asyncio_detailed()` in `src/bb/cloud/sdk/prs.py`. Added explicit check for status codes 200 and 201 with manual `PullRequestComment.from_dict()` deserialization.

---

## Status

- [x] Confirmed via static analysis (spec documents 200 only; live API returns 201)
- [x] Fixed in `src/bb/cloud/sdk/prs.py`
