# Cloud SDK

The Cloud SDK wraps the Bitbucket Cloud REST API. It provides 21 resource modules covering repositories, pull requests, branches, commits, pipelines, issues, snippets, webhooks, and more. Each module exposes typed functions that handle authentication, HTTP transport, and pagination — callers work with plain Python objects.

The SDK targets the authenticated Bitbucket Cloud API at `https://api.bitbucket.org/2.0`. All calls require a valid authentication credential. See [Authentication](authentication.md) for the supported methods.

## Module map

| Module | Covers |
|---|---|
| `addon` | Bitbucket Connect add-on lifecycle endpoints |
| `branch_restrictions` | Branch restriction rules (push, merge, delete) |
| `branches` | Branch listing, creation, and deletion |
| `branching_model` | Repository branching model configuration |
| `commit_statuses` | Build and CI status on commits |
| `commits` | Commit listing and individual commit retrieval |
| `deployments` | Deployment tracking and environment management |
| `downloads` | Repository downloads (file attachments) |
| `issues` | Issue tracker: issues, comments, and changes |
| `pipelines` | Pipeline runs, steps, and configuration |
| `projects` | Workspace project management |
| `properties` | Repository and commit custom properties |
| `prs` | Pull requests: create, list, review, merge, decline |
| `repos` | Repository CRUD and repository-level settings |
| `search` | Code search within a workspace |
| `snippets` | Snippet creation and retrieval |
| `source` | Source tree browsing and raw file access |
| `users` | User profile and account information |
| `webhooks` | Repository and workspace webhook management |
| `workspaces` | Workspace listing and membership |

## Authentication summary

| Class | Description |
|---|---|
| `APITokenAuth` | Authenticates with an Atlassian API token via `BB_TOKEN` |
| `OAuthTokenAuth` | Authenticates with an OAuth 2.0 bearer token |
| `OAuthClientCredsAuth` | Obtains a token via the OAuth 2.0 client credentials flow |
| `JWTAuth` | Signs requests with a JWT private key for Bitbucket Connect apps |

All auth classes are in `bb.cloud.sdk._auth`. For setup details and environment variable reference, see [Authentication](authentication.md).

## Pagination

Most list functions return `list[T]`, fetching all pages automatically. For large result sets where you want to avoid materialising all records at once, use `async_paginate` directly. See [Pagination](pagination.md).
