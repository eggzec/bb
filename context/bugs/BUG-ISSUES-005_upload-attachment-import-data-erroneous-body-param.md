# BUG-ISSUES-005: `upload_attachment` / `import_data` crash — erroneous `body` kwarg passed to generated API with no body parameter

**Status:** FIXED
**Root cause:** sdk-wrapper — `body: Unset = UNSET` declared and forwarded to generated endpoints that have no `body` parameter → `TypeError: asyncio() got an unexpected keyword argument 'body'`
**Layer:** sdk-wrapper

---

## Affected functions
- `bb.cloud.sdk.issues.upload_attachment`
- `bb.cloud.sdk.issues.import_data`

---

## Description

Both `upload_attachment` and `import_data` declared `body: Unset = UNSET` as a keyword-only argument and forwarded it to the underlying generated `asyncio()` call via `body=body`. The generated API endpoints for these operations (`POST .../issues/{issue_id}/attachments` and `POST .../issues/import`) have no `requestBody` in the spec, so the generator produces `asyncio()` functions with no `body` parameter. Passing an unexpected `body=UNSET` keyword argument raises:

```
TypeError: asyncio() got an unexpected keyword argument 'body'
```

This is the inverse of bugs like BUG-WEBHOOKS-001 (spec missing body → generated code has no `body` param, but SDK tries to pass one). The spec is correct for these endpoints (they use multipart/form-data file upload or no body); the SDK erroneously added a body parameter that was never required by the generated code.

---

## Evidence

**SDK wrapper before fix** (`src/bb/cloud/sdk/issues.py`):

```python
# upload_attachment (~line 1285)
async def upload_attachment(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    issue_id: int,
    *,
    body: Unset = UNSET,    # erroneous — generated API has no body param
) -> None | Error:
    ...
    return await post_repositories_workspace_repo_slug_issues_issue_id_attachments.asyncio(
        workspace, repo_slug, issue_id, client=client.auth, body=body  # TypeError
    )

# import_data (~line 1488)
async def import_data(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: Unset = UNSET,    # erroneous — generated API has no body param
) -> None | Error:
    ...
    return await post_repositories_workspace_repo_slug_issues_import.asyncio(
        workspace, repo_slug, client=client.auth, body=body  # TypeError
    )
```

**SDK wrapper after fix:**

```python
# upload_attachment
async def upload_attachment(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    issue_id: int,
) -> None | Error:
    ...
    return await post_repositories_workspace_repo_slug_issues_issue_id_attachments.asyncio(
        workspace, repo_slug, issue_id, client=client.auth
    )

# import_data
async def import_data(
    client: BBClient,
    workspace: str,
    repo_slug: str,
) -> None | Error:
    ...
    return await post_repositories_workspace_repo_slug_issues_import.asyncio(
        workspace, repo_slug, client=client.auth
    )
```

The `body` parameter and the `*` keyword-only separator were removed entirely. The `body=body` keyword argument was removed from the `asyncio()` call.

---

## Impact

- `issues.upload_attachment()` raises `TypeError` on every call — impossible to attach files to issues
- `issues.import_data()` raises `TypeError` on every call — impossible to import issue data
- The failure happens before any HTTP call is made, so no network request is ever sent

---

## Fix Applied

Removed `*, body: Unset = UNSET` from both function signatures and removed `body=body` from both `asyncio()` call sites in `src/bb/cloud/sdk/issues.py`.

---

## Status

- [x] Confirmed via static analysis (generated API signatures confirm no `body` parameter)
- [x] Fixed in `src/bb/cloud/sdk/issues.py`
