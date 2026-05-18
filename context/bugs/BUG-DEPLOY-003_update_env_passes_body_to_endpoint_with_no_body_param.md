# BUG-DEPLOY-003: `deployments.update_env` passed `body=body` to `update_environment_for_repository.asyncio()` which has no `body` parameter

**Status:** FIXED
**Layer:** sdk-wrapper
**Module:** `bb.cloud.sdk.deployments`
**Function:** `update_env`
**Severity:** High (runtime `TypeError` — function completely unusable)

---

## Symptom

```
TypeError: asyncio() got an unexpected keyword argument 'body'
```

Triggered on every call to `deployments.update_env()`.

---

## Root Cause

The `POST /repositories/{workspace}/{repo_slug}/environments/{environment_uuid}/changes` endpoint has **no `requestBody`** in the OpenAPI spec (confirmed by `jq` inspection — see BUG-DEPLOY-002 for spec-layer details). Because there is no `requestBody`, the generator does not add a `body` parameter to `_get_kwargs` or the `asyncio()` function.

The SDK wrapper, however, was written to accept and forward a `body` argument:

```python
# BEFORE (broken):
async def update_env(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    environment_uuid: str,
    *,
    body: DeploymentEnvironment | Unset = UNSET,
) -> DeploymentEnvironment | Error | None:
    result = await update_environment_for_repository.asyncio(
        workspace, repo_slug, environment_uuid, client=client.auth, body=body  # ← TypeError
    )
```

The generated `update_environment_for_repository.asyncio()` signature is:
```python
async def asyncio(workspace: str, repo_slug: str, environment_uuid: str, *, client: AuthenticatedClient) -> ...:
```
No `body` parameter exists. Passing `body=body` raises `TypeError`.

---

## Relationship to BUG-DEPLOY-002

BUG-DEPLOY-002 documents the **spec-layer root cause**: the `/changes` endpoint is missing its `requestBody` in `bb_cloud_fixed.openapi.json`. Once BUG-DEPLOY-002's spec fix is applied and the code is regenerated, the generated `asyncio()` will gain a `body` parameter — and this SDK wrapper bug will also be resolved.

This bug (BUG-DEPLOY-003) documents the **sdk-wrapper manifestation**: the immediate runtime crash from passing `body=body` to a generated function that has no `body` parameter. It was fixed independently by removing the erroneous `body=body` argument while the spec fix is pending.

---

## Fix Applied

Removed `body=body` from the generated API call:

```python
# AFTER (fixed):
async def update_env(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    environment_uuid: str,
    *,
    body: DeploymentEnvironment | Unset = UNSET,
) -> DeploymentEnvironment | Error | None:
    result = await update_environment_for_repository.asyncio(
        workspace, repo_slug, environment_uuid, client=client.auth
        # body= removed — generated function has no body param (spec missing requestBody)
    )
    if isinstance(result, (DeploymentEnvironment, Error)):
        return result
    return None
```

Note: the `body` parameter is intentionally retained in the wrapper signature so that once BUG-DEPLOY-002's spec fix is applied and code is regenerated, the `body=body` argument can be restored without a breaking API change for callers.

---

## Current State

Fixed. `src/bb/cloud/sdk/deployments.py` line ~332 no longer passes `body=body` to the generated call (confirmed at lines 332–334).

---

## Follow-up Required

Once BUG-DEPLOY-002's spec fix is applied (`requestBody` added to the `/changes` POST endpoint) and `make generate-cloud` is run:

1. Verify that `update_environment_for_repository.py`'s `_get_kwargs` gains a `body: DeploymentEnvironment` parameter
2. Restore `body=body` in the `update_env` SDK wrapper call
3. Remove `| Unset = UNSET` from the wrapper's `body` parameter (since spec marks requestBody required)
