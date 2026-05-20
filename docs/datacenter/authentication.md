# Authentication

The DC SDK supports two authentication methods: Personal Access Token (PAT) and HTTP Basic. Both are accepted by all Bitbucket Data Center REST endpoints.

!!! tip
    Use PAT authentication in production and CI environments. Basic auth sends your password on every request and is harder to rotate. PATs can be scoped and revoked independently of your account password.

!!! warning
    Do not hardcode credentials in source code. Use environment variables or a secrets manager and load them at runtime.

## PersonalAccessTokenAuth

Sends `Authorization: Bearer <token>` on every request.

**Constructor:**

```python
PersonalAccessTokenAuth(token: str, base_url: str | None = None)
```

- `token`: The Personal Access Token string.
- `base_url`: REST root of your Bitbucket instance. If omitted, falls back to `BB_DC_BASE_URL`, then defaults to `http://localhost:7990/rest`.

**From environment:**

```python
PersonalAccessTokenAuth.from_env() -> PersonalAccessTokenAuth
```

Reads `BB_DC_TOKEN`. Raises `RuntimeError` if the variable is not set.

**Environment variables:**

| Variable | Required | Description |
|---|---|---|
| `BB_DC_TOKEN` | Yes | Personal Access Token |
| `BB_DC_BASE_URL` | Recommended | REST root URL of your instance |

**Example:**

```python
from bb.datacenter.sdk._auth import PersonalAccessTokenAuth
from bb.datacenter import BBDCClient

auth = PersonalAccessTokenAuth(
    token="mytoken",
    base_url="https://bitbucket.example.com/rest",
)
client = BBDCClient(auth=auth)
```

Or, loading from environment variables:

```python
import os
from bb.datacenter.sdk._auth import PersonalAccessTokenAuth
from bb.datacenter import BBDCClient

os.environ["BB_DC_TOKEN"] = "mytoken"
os.environ["BB_DC_BASE_URL"] = "https://bitbucket.example.com/rest"

client = BBDCClient(auth=PersonalAccessTokenAuth.from_env())
```

## BasicAuth

Sends `Authorization: Basic base64(username:password)` on every request.

**Constructor:**

```python
BasicAuth(username: str, password: str, base_url: str | None = None)
```

- `username`: Bitbucket Data Center username.
- `password`: Account password.
- `base_url`: REST root of your Bitbucket instance. If omitted, falls back to `BB_DC_BASE_URL`, then defaults to `http://localhost:7990/rest`.

**From environment:**

```python
BasicAuth.from_env() -> BasicAuth
```

Reads `BB_DC_USERNAME` and `BB_DC_PASSWORD`. Raises `RuntimeError` if either variable is missing.

**Environment variables:**

| Variable | Required | Description |
|---|---|---|
| `BB_DC_USERNAME` | Yes | Bitbucket Data Center username |
| `BB_DC_PASSWORD` | Yes | Account password |
| `BB_DC_BASE_URL` | Recommended | REST root URL of your instance |

**Example:**

```python
from bb.datacenter.sdk._auth import BasicAuth
from bb.datacenter import BBDCClient

auth = BasicAuth(
    username="admin",
    password="secret",
    base_url="https://bitbucket.example.com/rest",
)
client = BBDCClient(auth=auth)
```

## auto_detect_auth()

```python
from bb.datacenter.sdk._auth import auto_detect_auth

auth = auto_detect_auth()
```

Inspects environment variables and returns the appropriate auth object. Priority order:

1. If `BB_DC_TOKEN` is set — returns `PersonalAccessTokenAuth.from_env()`
2. If `BB_DC_USERNAME` **and** `BB_DC_PASSWORD` are set — returns `BasicAuth.from_env()`
3. Otherwise — raises `RuntimeError` with a message listing the missing variables

`BBDCClient.from_env()` calls `auto_detect_auth()` internally. Use it directly if you need to inspect or store the auth object before constructing a client.

## require_auth decorator

All SDK resource functions are decorated with `@require_auth(AuthMethod.BEARER, AuthMethod.BASIC)`. The decorator validates the client's auth method before the function body runs.

If the client carries an unrecognised auth method or a method not in the allowed set, `AuthenticationError` is raised immediately — before any network call is made.

```python
from bb.datacenter.sdk._errors import AuthenticationError
from bb.datacenter import BBDCClient
from bb.datacenter.sdk import repos

client = BBDCClient(auth=some_unsupported_auth)

try:
    result = await repos.list(client, project_key="PRJ")
except AuthenticationError as e:
    print(f"Auth validation failed: {e}")
```

In practice, constructing a client with `PersonalAccessTokenAuth` or `BasicAuth` — the only two provided auth classes — always satisfies the decorator. `AuthenticationError` is only raised if you construct `BBDCClient` with a custom `BaseAuth` subclass that sets an unrecognised `prefix` on the underlying `AuthenticatedClient`.
