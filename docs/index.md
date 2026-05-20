# bb

`bb` is a Python SDK for the Bitbucket REST API. It provides async wrappers for both Bitbucket Cloud and Bitbucket Data Center, handles authentication, and abstracts pagination. A CLI built on top of the SDK is planned.

## SDK comparison

| Feature | Cloud SDK | Data Center SDK |
|---|---|---|
| Authentication methods | API token (Bearer) | Personal access token (Bearer), HTTP Basic |
| Async support | Yes | Yes |
| Pagination | Automatic (all pages fetched) | Manual via `async_paginate` helper |
| Resources covered | Repositories, branches, commits, pull requests, projects | Repositories, branches, commits, pull requests, projects |

## Installation

=== "uv"

    ```bash
    uv add bb
    ```

=== "pip"

    ```bash
    pip install bb
    ```

## Quick start

=== "Cloud"

    ```python
    import asyncio
    from bb.cloud import BBClient
    from bb.cloud.sdk import repos

    async def main():
        client = BBClient.from_env()  # reads BB_TOKEN from env
        all_repos = await repos.list(client, workspace="myworkspace")
        for repo in all_repos:
            print(repo.full_name)

    asyncio.run(main())
    ```

=== "Data Center"

    ```python
    import asyncio
    from bb.datacenter import BBDCClient
    from bb.datacenter.sdk import branches
    from bb.datacenter.sdk._pagination import async_paginate

    async def main():
        client = BBDCClient.from_env()  # reads BB_DC_TOKEN + BB_DC_BASE_URL from env
        async for branch in async_paginate(branches.list, client, "PRJ", "myrepo", limit=50):
            print(branch.display_id)

    asyncio.run(main())
    ```

## Next steps

- [Getting Started](getting-started/index.md) — installation, environment setup, and quickstart guides
