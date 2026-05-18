# BUG-AUTH-001: All auth clients drop Authorization header on HTTP redirects

**Module:** `bb.cloud.sdk._auth`
**Function:** `APITokenAuth.get_authenticated_client`, `OAuthTokenAuth.get_authenticated_client`, `OAuthClientCredsAuth.get_authenticated_client`, `JWTAuth.get_authenticated_client`, `AppPasswordAuth.get_authenticated_client`
**Severity:** High — silent failure on every authenticated API call that encounters an HTTP redirect

## Description

All five `get_authenticated_client()` implementations in `src/bb/cloud/sdk/_auth.py` construct an `AuthenticatedClient` without passing `follow_redirects=True`. The Bitbucket Cloud API at `api.bitbucket.org` issues HTTP redirects for trailing-slash normalization and regional routing. When `httpx` encounters a redirect without `follow_redirects=True`, it returns the 3xx response directly to the caller instead of following it. The caller receives no data and no Python exception — just an unexpected status code.

Even in cases where httpx might follow a redirect automatically, the `Authorization` header is dropped on cross-origin redirects by default. The project's own `CLAUDE.md` explicitly documents this risk: "Critical: always use httpx (not urllib.request.urlopen) in any script that calls the BB API. urllib follows Bitbucket's redirect and silently drops the Authorization header → 401. httpx.get(..., follow_redirects=True) preserves auth on same-host redirects." The same rule applies to `AuthenticatedClient` construction — the flag must be set explicitly.

Because the failure mode is a 3xx or 401 HTTP response (not a raised exception), the bug is very difficult to diagnose. All SDK methods built on top of any of the five auth classes are affected: any call that hits a redirect returns `None` or raises `UnexpectedStatus` depending on how the wrapper handles unknown status codes, with no indication that a redirect was the cause.

## Evidence

**Code before fix** (`src/bb/cloud/sdk/_auth.py`, lines ~70, ~119, ~204, ~268, ~307):

```python
# APITokenAuth (~line 70)
return AuthenticatedClient(base_url=BASE_URL, token=encoded, prefix="Basic")

# OAuthTokenAuth (~line 119)
return AuthenticatedClient(
    base_url=BASE_URL,
    token=self.access_token,
    prefix=self.token_type.capitalize(),
)

# OAuthClientCredsAuth (~line 204)
return AuthenticatedClient(base_url=BASE_URL, token=self.get_access_token(), prefix="Bearer")

# JWTAuth (~line 268)
return AuthenticatedClient(base_url=BASE_URL, token=self._create_jwt_token(), prefix="JWT")

# AppPasswordAuth (~line 307)
return AuthenticatedClient(base_url=BASE_URL, token=encoded, prefix="Basic")
```

**Code after fix:**

```python
# APITokenAuth
return AuthenticatedClient(base_url=BASE_URL, token=encoded, prefix="Basic", follow_redirects=True)

# OAuthTokenAuth
return AuthenticatedClient(
    base_url=BASE_URL,
    token=self.access_token,
    prefix=self.token_type.capitalize(),
    follow_redirects=True,
)

# OAuthClientCredsAuth
return AuthenticatedClient(base_url=BASE_URL, token=self.get_access_token(), prefix="Bearer", follow_redirects=True)

# JWTAuth
return AuthenticatedClient(base_url=BASE_URL, token=self._create_jwt_token(), prefix="JWT", follow_redirects=True)

# AppPasswordAuth
return AuthenticatedClient(base_url=BASE_URL, token=encoded, prefix="Basic", follow_redirects=True)
```

## Impact

Every SDK call that uses any of the five auth mechanisms is affected whenever the API issues a redirect. The failure is silent: the caller receives a 3xx response (or a 401 after the Authorization header is dropped on the redirected request) rather than a Python exception. Wrappers that check for `None` will return `None` to the user with no error; wrappers that raise `UnexpectedStatus` will surface a confusing HTTP status code with no redirect context. All SDK resource modules — repos, branches, commits, PRs, pipelines, webhooks, etc. — are downstream of `get_authenticated_client()` and are therefore all affected.

## Root Cause

`httpx` does not follow redirects by default. `AuthenticatedClient` in the generated `client.py` wraps `httpx.Client`; it exposes a `follow_redirects` constructor parameter but the default is `False`. None of the five auth class implementations passed this parameter, so the client was constructed in the non-following state. On any redirect from `api.bitbucket.org`, the client returned the 3xx response without following it and without raising an exception.

## Fix Applied

Added `follow_redirects=True` to every `AuthenticatedClient(...)` call in `src/bb/cloud/sdk/_auth.py` — one addition per auth class, five total. No other changes were required. The `follow_redirects` parameter is accepted by `AuthenticatedClient` as a pass-through to the underlying `httpx.Client`.

## Status

- [x] Confirmed via static analysis
- [x] Fixed in `src/bb/cloud/sdk/_auth.py`
