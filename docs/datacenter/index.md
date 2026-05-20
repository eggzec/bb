# Data Center SDK

The Data Center SDK wraps the Bitbucket Data Center REST API v1. It provides 7 resource modules covering repositories, branches, commits, projects, pull requests, builds, and security operations. Each module exposes typed async functions that handle authentication and HTTP transport — callers work with plain Python model objects.

The SDK targets self-hosted Bitbucket Data Center instances. The base URL is always user-supplied via `BB_DC_BASE_URL`. All calls require authentication via a Personal Access Token or HTTP Basic credentials.

## Module map

| Module | Covers |
|---|---|
| `bb.datacenter.sdk.branches` | Branch listing, search, create, delete, get and set default branch |
| `bb.datacenter.sdk.builds` | Build status operations on commits |
| `bb.datacenter.sdk.commits` | Commit listing and individual commit retrieval |
| `bb.datacenter.sdk.projects` | Project list, get, create, update, delete |
| `bb.datacenter.sdk.prs` | Pull requests: list, get, create, update, merge, decline, approve, unapprove |
| `bb.datacenter.sdk.repos` | Repository list (by project or global), get, create, update, delete |
| `bb.datacenter.sdk.security` | Security-related operations |

## Authentication summary

| Class | Auth method | Wire format |
|---|---|---|
| `PersonalAccessTokenAuth` | Personal Access Token | `Authorization: Bearer <token>` |
| `BasicAuth` | HTTP Basic | `Authorization: Basic base64(username:password)` |

Both classes are in `bb.datacenter.sdk._auth`. `BBDCClient.from_env()` selects the method automatically based on which environment variables are set. For full setup details see [Authentication](authentication.md).

## Pagination

DC SDK list functions do **not** fetch all pages automatically. To iterate over all results you must use `async_paginate` (async) or `paginate` (sync) from `bb.datacenter.sdk._pagination`. This differs from the Cloud SDK, where most list functions return a complete `list[T]`.

Some module functions — such as `repos.list` and `prs.list` — call `async_paginate` internally and return a fully materialised list. Others require the caller to paginate. See [Pagination](pagination.md) for full details and examples.
