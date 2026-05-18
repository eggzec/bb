# BUG-PIPELINES-008: `create_known_host` always returns `None` — API returns 201, spec only documents 200

**Status:** FIXED
**Root cause:** sdk-wrapper — `asyncio()` maps only documented status codes; live API returns 201 Created which is unmapped → `None`
**Layer:** sdk-wrapper

---

## Affected functions
- `bb.cloud.sdk.pipelines.create_known_host`

---

## Description

`pipelines.create_known_host` called `create_repository_pipeline_known_host.asyncio()`. The OpenAPI spec for `POST /repositories/{workspace}/{repo_slug}/pipelines/config/ssh/known_hosts` documents a 200 response. The Bitbucket Cloud API returns **201 Created** on successful host creation. The generator's `_parse_response()` only maps documented status codes — so the live 201 response falls through to `None`.

The result: every successful `create_known_host()` call returned `None` instead of the created `PipelineKnownHost` object. The `isinstance(result, (PipelineKnownHost, Error))` guard in the original code was unreachable on success.

This is the same root cause as BUG-PRS-005 (`prs.add_comment` missing 201 handling) and the commit status upsert bug BUG-COMMITS-001.

---

## Evidence

**SDK wrapper before fix** (`src/bb/cloud/sdk/pipelines.py`, ~line 1183):

```python
async def create_known_host(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    body: PipelineKnownHost,
) -> PipelineKnownHost | Error | None:
    result = await create_repository_pipeline_known_host.asyncio(
        workspace, repo_slug, client=client.auth, body=body
    )
    if isinstance(result, (PipelineKnownHost, Error)):
        return result
    return None
```

**SDK wrapper after fix:**

```python
async def create_known_host(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    body: PipelineKnownHost,
) -> PipelineKnownHost | Error | None:
    response = await create_repository_pipeline_known_host.asyncio_detailed(
        workspace, repo_slug, client=client.auth, body=body
    )
    if response.status_code.value in (200, 201):
        import json as _json
        return PipelineKnownHost.from_dict(_json.loads(response.content))
    if isinstance(response.parsed, Error):
        return response.parsed
    return None
```

---

## Root Cause

The generator's `_parse_response()` maps only status codes present in the spec. The spec documents 200 → PipelineKnownHost; the live API responds with 201 → PipelineKnownHost. Since 201 is absent from `_parse_response()`, `response.parsed` is `None` and `asyncio()` returns `None`.

The fix uses `asyncio_detailed()` which returns the raw `Response[T]` with `status_code` and `content` bytes. Both 200 and 201 are accepted as success, and `PipelineKnownHost.from_dict()` deserializes the response body directly from `response.content` (raw bytes decoded via `json.loads`).

---

## Relation to BUG-PIPELINES-006

BUG-PIPELINES-006 fixed the test using a reserved hostname (`github.com`) and missing `public_key`. Even after that fix, successful creation would still return `None` due to this bug — the two bugs are independent and both need to be resolved for the `test_create_delete_known_host_roundtrip` test to pass end-to-end.

---

## Impact

- `pipelines.create_known_host()` always returned `None` on success
- The `isinstance(result, PipelineKnownHost)` check in callers was unreachable
- Known-host creation appeared to succeed (no exception) but the caller could not inspect the created object

---

## Fix Applied

Switched from `asyncio()` to `asyncio_detailed()` in `src/bb/cloud/sdk/pipelines.py`. Added explicit check for status codes 200 and 201 with manual `PipelineKnownHost.from_dict()` deserialization. Error responses fall through to `response.parsed` (which is an `Error` for 4xx responses mapped by the generator).

---

## Status

- [x] Confirmed via static analysis (spec documents 200 only; live API returns 201)
- [x] Fixed in `src/bb/cloud/sdk/pipelines.py`
