# Authentication

The Cloud SDK supports four authentication methods. Choose the one that matches how your application obtains credentials.

All auth classes are importable from `bb.cloud.sdk._auth`. `BBClient` accepts any of them via its constructor.

!!! warning
    Do not hardcode tokens or secrets in source code. Use environment variables or a secrets manager. All auth classes read credentials from environment variables when using their `from_env()` class methods.

---

## APITokenAuth

Authenticates using an Atlassian API token. This is the standard method for personal scripts and server-side tooling.

**Constructor**

```python
APITokenAuth(token: str, base_url: str | None = None)
```

- `token` — an Atlassian API token from [id.atlassian.com/manage-profile/security/api-tokens](https://id.atlassian.com/manage-profile/security/api-tokens)
- `base_url` — override the default API base URL; leave as `None` for Bitbucket Cloud

**Environment variables**

| Variable | Required | Description |
|---|---|---|
| `BB_TOKEN` | Yes | Atlassian API token |
| `BB_BASE_URL` | No | Override API base URL |

**from_env()**

```python
auth = APITokenAuth.from_env()
```

Reads `BB_TOKEN` (and optionally `BB_BASE_URL`) from the environment.

**Example**

```python
from bb.cloud.sdk._auth import APITokenAuth
from bb.cloud import BBClient
from bb.cloud.sdk import repos

async def main():
    auth = APITokenAuth.from_env()
    client = BBClient(auth=auth)

    all_repos = await repos.list(client, workspace="myworkspace")
```

Alternatively, `BBClient.from_env()` calls `APITokenAuth.from_env()` internally:

```python
client = BBClient.from_env()
```

---

## OAuthTokenAuth

Authenticates using an OAuth 2.0 bearer token that your application has already obtained. Use this when your app implements the OAuth authorization code flow and you hold a valid access token.

**Constructor**

```python
OAuthTokenAuth(token: str, base_url: str | None = None)
```

- `token` — a valid OAuth 2.0 access token
- `base_url` — override the default API base URL

**Example**

```python
from bb.cloud.sdk._auth import OAuthTokenAuth
from bb.cloud import BBClient

# token obtained from your OAuth flow
access_token = "..."

auth = OAuthTokenAuth(token=access_token)
client = BBClient(auth=auth)
```

---

## OAuthClientCredsAuth

Obtains an access token automatically using the OAuth 2.0 client credentials flow. Use this for machine-to-machine integrations where no user interaction is involved.

**Constructor**

```python
OAuthClientCredsAuth(client_id: str, client_secret: str, base_url: str | None = None)
```

- `client_id` — OAuth consumer key from your Bitbucket OAuth consumer settings
- `client_secret` — OAuth consumer secret
- `base_url` — override the default API base URL

**Example**

```python
import os
from bb.cloud.sdk._auth import OAuthClientCredsAuth
from bb.cloud import BBClient

auth = OAuthClientCredsAuth(
    client_id=os.environ["BB_CLIENT_ID"],
    client_secret=os.environ["BB_CLIENT_SECRET"],
)
client = BBClient(auth=auth)
```

---

## JWTAuth

Signs requests with a JWT using an RSA private key. This method is intended for Bitbucket Connect apps that authenticate as the add-on itself.

**Constructor**

```python
JWTAuth(private_key: str, client_key: str, base_url: str | None = None)
```

- `private_key` — PEM-encoded RSA private key
- `client_key` — the add-on's client key as registered in Bitbucket
- `base_url` — override the default API base URL

**Example**

```python
import os
from bb.cloud.sdk._auth import JWTAuth
from bb.cloud import BBClient

private_key = os.environ["BB_JWT_PRIVATE_KEY"]
client_key = os.environ["BB_JWT_CLIENT_KEY"]

auth = JWTAuth(private_key=private_key, client_key=client_key)
client = BBClient(auth=auth)
```

The `.auth` property on `BBClient` automatically refreshes the JWT when it expires. No manual refresh is needed.

---

## Auto-detection with auto_detect_auth()

`auto_detect_auth()` inspects the environment and returns the appropriate auth instance based on which variables are present.

```python
from bb.cloud.sdk._auth import auto_detect_auth
from bb.cloud import BBClient

auth = auto_detect_auth()
client = BBClient(auth=auth)
```

Detection order:

1. If `BB_TOKEN` is set — returns `APITokenAuth`
2. If `BB_CLIENT_ID` and `BB_CLIENT_SECRET` are set — returns `OAuthClientCredsAuth`
3. If `BB_JWT_PRIVATE_KEY` and `BB_JWT_CLIENT_KEY` are set — returns `JWTAuth`

If none of the required variables are present, `auto_detect_auth()` raises `AuthenticationError`.

---

## Environment variables reference

| Variable | Used by | Required |
|---|---|---|
| `BB_TOKEN` | `APITokenAuth` | Yes (for API token auth) |
| `BB_BASE_URL` | All auth classes | No — defaults to `https://api.bitbucket.org/2.0` |
| `BB_CLIENT_ID` | `OAuthClientCredsAuth` | Yes (for client credentials flow) |
| `BB_CLIENT_SECRET` | `OAuthClientCredsAuth` | Yes (for client credentials flow) |
| `BB_JWT_PRIVATE_KEY` | `JWTAuth` | Yes (for JWT auth) |
| `BB_JWT_CLIENT_KEY` | `JWTAuth` | Yes (for JWT auth) |

---

## Error handling

`bb.cloud.sdk._errors.AuthenticationError` is raised when the selected auth method is not supported for the requested endpoint, or when required environment variables are missing.

```python
from bb.cloud.sdk._errors import AuthenticationError

try:
    auth = auto_detect_auth()
except AuthenticationError as e:
    print(f"Authentication setup failed: {e}")
```
