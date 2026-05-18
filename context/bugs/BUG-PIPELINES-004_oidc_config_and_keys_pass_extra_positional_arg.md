# BUG-PIPELINES-004: `oidc_config` and `oidc_keys` pass extra positional arg — will crash at runtime

**Module:** `bb.cloud.sdk.pipelines`
**Functions:** `oidc_config`, `oidc_keys`
**Severity:** Critical (runtime `TypeError` on every call)

## Description

The SDK wrappers `oidc_config` and `oidc_keys` both accept a `repo_slug` parameter in their
signature (matching the other SDK functions for consistency) and pass it as a second positional
argument to the generated API. However, the generated API functions for OIDC are workspace-scoped
and only accept `workspace` as a positional argument — there is no `repo_slug` parameter.

This causes a **`TypeError: asyncio() takes 1 positional argument but 2 were given`** on every call.

## Evidence

**SDK wrapper** (`src/bb/cloud/sdk/pipelines.py`, line ~1544):
```python
async def oidc_config(client: BBClient, workspace: str, repo_slug: str) -> Any:
    return await get_oidc_configuration.asyncio(workspace, repo_slug, client=client.auth)
    #                                                       ^^^^^^^^^ BUG: extra arg
```

**Generated API** (`src/bb/cloud/api/pipelines/get_oidc_configuration.py`, line ~161):
```python
async def asyncio(
    workspace: str,          # <-- only one positional parameter
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
```

Passing `repo_slug` as the second positional argument will raise:
```
TypeError: asyncio() takes 1 positional argument but 2 were given
```

The same bug exists in `oidc_keys`:
```python
async def oidc_keys(client: BBClient, workspace: str, repo_slug: str) -> Any:
    return await get_oidc_keys.asyncio(workspace, repo_slug, client=client.auth)
    #                                             ^^^^^^^^^ BUG: extra arg
```

## API Endpoint

The OIDC endpoints are workspace-scoped:
- `GET /2.0/workspaces/{workspace}/pipelines-config/identity/oidc/.well-known/openid-configuration`
- `GET /2.0/workspaces/{workspace}/pipelines-config/identity/oidc/keys.json`

Neither has a `repo_slug` path parameter.

## Recommended Fix

Remove `repo_slug` from the generated API calls (keep the SDK signature for API consistency if desired, or remove it too):

```python
async def oidc_config(client: BBClient, workspace: str, repo_slug: str) -> Any:
    # repo_slug is not used by this endpoint — it is workspace-scoped
    return await get_oidc_configuration.asyncio(workspace, client=client.auth)

async def oidc_keys(client: BBClient, workspace: str, repo_slug: str) -> Any:
    # repo_slug is not used by this endpoint — it is workspace-scoped
    return await get_oidc_keys.asyncio(workspace, client=client.auth)
```

Or ideally remove `repo_slug` from the SDK signatures since these are workspace endpoints:

```python
async def oidc_config(client: BBClient, workspace: str) -> Any:
    return await get_oidc_configuration.asyncio(workspace, client=client.auth)

async def oidc_keys(client: BBClient, workspace: str) -> Any:
    return await get_oidc_keys.asyncio(workspace, client=client.auth)
```

## Status

- [x] Confirmed via static analysis (signature mismatch is unambiguous)
- [ ] Confirmed via live test run (expected: TypeError)
