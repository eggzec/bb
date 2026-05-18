# BUG-PIPELINES-005: `test_reports` SDK function is missing the required `step_uuid` argument

**Module:** `bb.cloud.sdk.pipelines`
**Function:** `test_reports`
**Severity:** Critical (runtime `TypeError` on every call — missing required positional arg)

## Description

The `test_reports` SDK function only accepts `pipeline_uuid` but the underlying generated API
requires both `pipeline_uuid` and `step_uuid`. The API endpoint is:

```
GET /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/test_reports
```

The SDK calls the generated function without providing `step_uuid`, which will raise:
```
TypeError: asyncio() missing 1 required positional argument: 'step_uuid'
```

## Evidence

**SDK wrapper** (`src/bb/cloud/sdk/pipelines.py`, line ~2215):
```python
async def test_reports(client: BBClient, workspace: str, repo_slug: str, pipeline_uuid: str) -> Any:
    return await get_pipeline_test_reports.asyncio(workspace, repo_slug, pipeline_uuid, client=client.auth)
    #            missing step_uuid ────────────────────────────────────────────────────────────────────────
```

**Generated API** (`src/bb/cloud/api/pipelines/get_pipeline_test_reports.py`, line ~20):
```python
def _get_kwargs(
    workspace: str,
    repo_slug: str,
    pipeline_uuid: str,
    step_uuid: str,     # <-- required, but SDK doesn't pass it
) -> dict[str, Any]:
```

The `asyncio` function signature:
```python
async def asyncio(
    workspace: str,
    repo_slug: str,
    pipeline_uuid: str,
    step_uuid: str,   # <-- required positional
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
```

## Same Bug in `test_cases` and `test_case_reasons`

`test_cases` calls `get_pipeline_test_report_test_cases` with `report_uuid` as 4th arg but the
generated API parameter name is `step_uuid`. This is semantically equivalent but the naming
discrepancy in the SDK is confusing.

`test_case_reasons` has the correct 5-arg call but should be verified.

## Recommended Fix

Add `step_uuid` to the SDK function signature:

```python
async def test_reports(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    pipeline_uuid: str,
    step_uuid: str,           # <-- ADD THIS
) -> Any:
    return await get_pipeline_test_reports.asyncio(
        workspace, repo_slug, pipeline_uuid, step_uuid, client=client.auth
    )
```

Also update `__all__` documentation and docstrings accordingly.

## Status

- [x] Confirmed via static analysis (signature mismatch is unambiguous)
- [ ] Confirmed via live test run (expected: TypeError)
