# Cloud Quickstart

This guide walks through the minimum steps to authenticate and make API calls against Bitbucket Cloud using the `bb` Cloud SDK.

## Prerequisites

Set two environment variables before running any code:

| Variable | Description |
|---|---|
| `BB_TOKEN` | An Atlassian API token from [id.atlassian.com/manage-profile/security/api-tokens](https://id.atlassian.com/manage-profile/security/api-tokens) |
| `BB_WORKSPACE` | Your Bitbucket workspace slug (visible in the URL: `bitbucket.org/<workspace>/`) |

```bash
export BB_TOKEN="your-api-token"
export BB_WORKSPACE="your-workspace-slug"
```

## Minimal working example

```python
import asyncio
from bb.cloud import BBClient
from bb.cloud.sdk import repos

async def main():
    client = BBClient.from_env()

    all_repos = await repos.list(client, workspace="myworkspace")

    for repo in all_repos:
        print(repo.full_name)

asyncio.run(main())
```

`BBClient.from_env()` reads `BB_TOKEN` and constructs an `APITokenAuth` automatically. No explicit auth setup is needed for API token authentication.

!!! note
    Most list functions in the Cloud SDK fetch all pages automatically and return a `list[T]`. You do not need to handle pagination manually for standard use. For streaming large result sets without materialising all pages in memory, see [Pagination](../cloud/pagination.md).

## Listing pull requests

Pass `state="OPEN"` to filter by pull request state. Valid values are `"OPEN"`, `"MERGED"`, and `"DECLINED"`.

```python
import asyncio
from bb.cloud import BBClient
from bb.cloud.sdk import prs

async def main():
    client = BBClient.from_env()

    open_prs = await prs.list(
        client,
        workspace="myworkspace",
        repo_slug="myrepo",
        state="OPEN",
    )

    for pr in open_prs:
        print(f"#{pr.id}  {pr.title}  ({pr.source.branch.name} -> {pr.destination.branch.name})")

asyncio.run(main())
```

## Creating a resource

Write operations require a request body model. These models are generated from the Bitbucket OpenAPI spec and live in `bb.cloud.models`. The exact class name for each operation is listed in the [API reference](../cloud/api/).

The example below creates a branch on an existing repository:

```python
import asyncio
from bb.cloud import BBClient
from bb.cloud.sdk import branches

async def main():
    client = BBClient.from_env()

    new_branch = await branches.create(
        client,
        workspace="myworkspace",
        repo_slug="myrepo",
        name="feature/my-feature",
        target_hash="abc123def456",  # commit hash to branch from
    )

    print(new_branch.name)

asyncio.run(main())
```

!!! note
    Request body models are imported from `bb.cloud.models`. See the API reference for the exact model class required by each operation. Model names follow the Bitbucket OpenAPI schema names and are generated — do not construct them by hand from the spec field names alone.

## Next steps

- [Authentication](../cloud/authentication.md) — configure OAuth, client credentials, or JWT auth
- [Pagination](../cloud/pagination.md) — stream large result sets with `async_paginate`
- [Cloud SDK overview](../cloud/index.md) — full module list and feature coverage
