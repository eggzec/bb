# Data Center Quickstart

This guide covers the minimum steps to authenticate and make API calls against a Bitbucket Data Center instance using the `bb` Data Center SDK.

## Prerequisites

You need:

- A running Bitbucket Data Center instance with a known REST base URL (e.g. `https://bitbucket.example.com/rest`)
- A Personal Access Token (PAT) **or** a username and password with API access
- Python 3.11+ and `bb` installed

## Environment variable setup

Set the variables below before running any code. The `BB_DC_BASE_URL` variable is always required and must point to the REST root of your instance.

=== "PAT"

    ```bash
    export BB_DC_TOKEN="your-personal-access-token"
    export BB_DC_BASE_URL="https://bitbucket.example.com/rest"
    ```

    Generate a PAT from your Bitbucket Data Center profile:
    **Profile > Manage account > Personal access tokens > Create token**.
    Grant it at least **Project read** and **Repository read** permissions.

=== "Basic"

    ```bash
    export BB_DC_USERNAME="your-username"
    export BB_DC_PASSWORD="your-password"
    export BB_DC_BASE_URL="https://bitbucket.example.com/rest"
    ```

    HTTP Basic auth uses your Bitbucket Data Center login credentials directly.
    PAT authentication is preferred in automated environments.

## Minimal working example

```python
import asyncio
from bb.datacenter import BBDCClient
from bb.datacenter.sdk import repos
from bb.datacenter.sdk._pagination import async_paginate

async def main():
    client = BBDCClient.from_env()

    # Collect all repos in a project across all pages
    all_repos = []
    async for repo in async_paginate(repos.list, client, "PRJ", limit=50):
        all_repos.append(repo)

    for repo in all_repos:
        print(repo.slug)

asyncio.run(main())
```

`BBDCClient.from_env()` reads the environment variables and builds the client automatically. It prefers PAT authentication if `BB_DC_TOKEN` is set; otherwise it falls back to Basic auth using `BB_DC_USERNAME` and `BB_DC_PASSWORD`. A `RuntimeError` is raised if neither is available.

!!! note
    DC SDK list functions such as `repos.list` and `prs.list` do **not** fetch all pages automatically. You must iterate with `async_paginate` (async) or `paginate` (sync) to traverse multiple pages. This differs from the Cloud SDK, where most list functions fetch all pages and return a `list[T]` directly. See [Pagination](../datacenter/pagination.md) for details.

## Working with pull requests

### List open pull requests

```python
import asyncio
from bb.datacenter import BBDCClient
from bb.datacenter.sdk import prs

async def main():
    client = BBDCClient.from_env()

    open_prs = await prs.list(
        client,
        project_key="PRJ",
        repo_slug="myrepo",
        state="OPEN",
    )

    for pr in open_prs:
        print(f"#{pr.id}  {pr.title}")

asyncio.run(main())
```

`prs.list` fetches all pages internally and returns a `list[RestPullRequest]`. Valid `state` values are `"OPEN"`, `"MERGED"`, `"DECLINED"`, and `"ALL"`.

### Fetch a single pull request

```python
import asyncio
from bb.datacenter import BBDCClient
from bb.datacenter.sdk import prs

async def main():
    client = BBDCClient.from_env()

    pr = await prs.get(
        client,
        project_key="PRJ",
        repo_slug="myrepo",
        pull_request_id="42",
    )

    if pr is not None:
        print(pr.title, pr.state)

asyncio.run(main())
```

### Merge a pull request

```python
import asyncio
from bb.datacenter import BBDCClient
from bb.datacenter.sdk import prs

async def main():
    client = BBDCClient.from_env()

    merged = await prs.merge(
        client,
        project_key="PRJ",
        repo_slug="myrepo",
        pull_request_id="42",
    )

    if merged is not None:
        print(f"Merged: {merged.title}")

asyncio.run(main())
```

The `merge` function accepts an optional `body` (`RestPullRequestMergeRequest`) for merge strategy configuration and a `version` string for optimistic concurrency control.

## Next steps

- [Authentication](../datacenter/authentication.md) — configure PAT or Basic auth explicitly
- [Pagination](../datacenter/pagination.md) — iterate over large result sets
- [Data Center SDK overview](../datacenter/index.md) — full module list and coverage
