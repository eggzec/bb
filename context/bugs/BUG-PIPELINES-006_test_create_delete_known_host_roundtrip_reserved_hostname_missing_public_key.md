# BUG-PIPELINES-006: `test_create_delete_known_host_roundtrip` uses reserved hostname + missing `publicKey`

**Status:** FIXED
**Layer:** test (wrong test data)
**File:** `tests/cloud/live/test_pipelines.py`
**Test:** `test_create_delete_known_host_roundtrip`
**Severity:** High (test always fails with HTTP 400 before any assertion is reached)

---

## Symptom

The test called `pipelines.create_known_host` with `github.com` as the hostname. Bitbucket manages
SSH host keys for well-known providers (GitHub, Bitbucket, GitLab) internally and rejects any
attempt to re-add them:

```
HTTP 400 Bad Request
{
  "type": "error",
  "error": {
    "message": "hostname-not-allowed: SSH for this hostname is already configured by Bitbucket"
  }
}
```

Additionally, the `PipelineKnownHost` body had no `public_key` field, which the API also requires
as part of the request body — causing a separate 400 even if a non-reserved hostname had been used.

---

## Evidence

**Raw API call with reserved hostname (before fix):**
```
POST /repositories/{workspace}/{repo}/pipelines_config/ssh/known_hosts
Body: {"hostname": "github.com"}
→ 400  hostname-not-allowed: SSH for this hostname is already configured by Bitbucket
```

**Raw API call with custom hostname + `public_key` (after fix):**
```
POST /repositories/{workspace}/{repo}/pipelines_config/ssh/known_hosts
Body: {
  "hostname": "test-host-3f7a1c2b.example.com",
  "public_key": {
    "key_type": "rsa",
    "key": "AAAA..."
  }
}
→ 201 Created
```

---

## Root Cause

Two independent mistakes in the test fixture:

1. **Reserved hostname** — `github.com` is pre-configured by Bitbucket for all repositories.
   The API enforces a blocklist and returns 400 for any hostname on that list.

2. **Missing `public_key`** — The `PipelineKnownHost` body was constructed without a `public_key`
   field. The Bitbucket API requires a `public_key` object (`key_type` + `key`) to register a
   known host; the endpoint rejects the request with 400 if it is absent.

---

## Fix Applied

Changed the test to use a random hostname guaranteed not to be on Bitbucket's reserved list, and
added a valid RSA `public_key` to the `PipelineKnownHost` body.

**Before:**
```python
known_host_body = PipelineKnownHost(hostname="github.com")
result = await pipelines.create_known_host(client, workspace, repo_slug, body=known_host_body)
assert result.hostname == "github.com"
```

**After:**
```python
import uuid
hostname = f"test-host-{uuid.uuid4().hex[:8]}.example.com"
known_host_body = PipelineKnownHost(
    hostname=hostname,
    public_key=PipelineSshPublicKey(
        key_type="rsa",
        key="AAAA...",   # minimal valid RSA public key material
    ),
)
result = await pipelines.create_known_host(client, workspace, repo_slug, body=known_host_body)
assert result.hostname == hostname
```

---

## Status

- [x] Root cause confirmed via live API call (400 with `github.com`)
- [x] Fix confirmed via live API call (201 with custom hostname + `public_key`)
- [x] Fix applied to `tests/cloud/live/test_pipelines.py`
