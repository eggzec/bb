# BUG-SOURCE-001: `source.get` returned `None` for plain-text file content

**Status:** FIXED
**Layer:** sdk-wrapper
**Module:** `bb.cloud.sdk.source`
**Function:** `get`
**Severity:** High (function always returned `None` for text files — the primary use case)

---

## Symptom

```
AssertionError: source.get returned None
```

Observed in the live test suite when fetching a text file (e.g., `README.md`, `pyproject.toml`). The function returned `None` even though the API returned `200 OK` with `Content-Type: text/plain`.

---

## Root Cause

The `GET /repositories/{workspace}/{repo_slug}/src/{commit}/{path}` endpoint returns:

- **Text files:** `200 OK` with `Content-Type: text/plain` and raw file bytes in the body
- **Directories:** `200 OK` with `Content-Type: application/json` and a paginated listing
- **Binaries:** `200 OK` with `Content-Type: application/octet-stream`

The generated `_parse_response` for this endpoint maps `200 → None` (or a directory listing model), because the spec does not adequately model the plain-text response variant. Calling `asyncio()` (the shorthand) returns the parsed result — which is `None` for a plain-text 200 because `_parse_response` returned `None`.

The original wrapper used `.asyncio()` and returned whatever `.parsed` contained — `None` for all text file responses.

---

## Generated Code Behaviour

```python
# get_repositories_workspace_repo_slug_src_commit_path.py
def _parse_response(*, client, response):
    if response.status_code == 200:
        # Only maps to a model if Content-Type is application/json (directory listing)
        # For text/plain, returns None
        return None
    ...
```

Since `asyncio()` returns `response.parsed`, all text-file fetches silently returned `None`.

---

## Fix Applied

Changed to `asyncio_detailed()`, inspected the `content-type` header, and decoded `response.content` for non-JSON 200 responses:

```python
# BEFORE (broken):
result = await get_repositories_workspace_repo_slug_src_commit_path.asyncio(
    commit, path, workspace, repo_slug, client=client.auth
)
return result

# AFTER (fixed):
response = await get_repositories_workspace_repo_slug_src_commit_path.asyncio_detailed(
    commit, path, workspace, repo_slug, client=client.auth
)
if response.status_code.value == 200:
    content_type = response.headers.get("content-type", "")
    if "application/json" not in content_type:
        return response.content.decode()
    # directory listing — fall through to response.parsed
return response.parsed
```

---

## Current State

Fixed. `src/bb/cloud/sdk/source.py` line ~55 now uses `asyncio_detailed()` and branches on `content-type` (confirmed by code inspection).

---

## General Rule

> Any SDK endpoint that serves non-JSON 200 responses (plain text, binary, mixed content types) will have `_parse_response` return `None` for those content types. SDK wrappers must use `asyncio_detailed()` and inspect `response.headers["content-type"]` and `response.content` directly.
