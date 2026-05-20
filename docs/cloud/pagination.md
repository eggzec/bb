# Pagination

The Bitbucket Cloud API uses cursor-based pagination. The Cloud SDK handles this transparently for most use cases.

## Default behaviour: automatic page fetching

Most `list` functions in the Cloud SDK return `list[T]`. When you call them, the SDK fetches all pages internally and returns the complete result set:

```python
from bb.cloud import BBClient
from bb.cloud.sdk import repos

async def main():
    client = BBClient.from_env()

    # All pages are fetched; returns list[Repository]
    all_repos = await repos.list(client, workspace="myworkspace")
    print(f"Total repos: {len(all_repos)}")
```

This is the right approach for most workloads where the result set is manageable in memory.

!!! note
    The sync `paginate` function is also available for non-async contexts. Import it from `bb.cloud.sdk._pagination`. The interface is identical to `async_paginate` but uses a regular `Iterator[T]` return type.

---

## Streaming with async_paginate

For large result sets — such as workspaces with thousands of repositories — materialising all pages at once may consume significant memory. Use `async_paginate` to iterate over items one page at a time:

```python
from bb.cloud import BBClient
from bb.cloud.sdk import repos
from bb.cloud.sdk._pagination import async_paginate

async def stream_repos(client, workspace: str):
    async for repo in async_paginate(repos.list, client, workspace, limit=100):
        # process one repo at a time; pages are fetched lazily
        print(repo.full_name)

async def main():
    client = BBClient.from_env()
    await stream_repos(client, "myworkspace")
```

`async_paginate` is an `AsyncIterator[T]`. It yields individual items (not pages) and fetches the next page only when the current page is exhausted.

---

## Parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `fn` | callable | — | The SDK list function to paginate (e.g. `repos.list`) |
| `*args` | positional | — | Positional arguments forwarded to `fn` (client, workspace, etc.) |
| `limit` | `int` | `25` | Number of items per page request |
| `**kwargs` | keyword | — | Additional keyword arguments forwarded to `fn` (e.g. `state="OPEN"`) |

Increasing `limit` reduces the number of HTTP requests at the cost of larger individual responses. The maximum value accepted by the Bitbucket Cloud API is `100`.

**Example with kwargs:**

```python
from bb.cloud.sdk._pagination import async_paginate
from bb.cloud.sdk import prs

async def stream_open_prs(client, workspace: str, repo_slug: str):
    async for pr in async_paginate(
        prs.list,
        client,
        workspace,
        repo_slug,
        limit=50,
        state="OPEN",
    ):
        print(f"#{pr.id} {pr.title}")
```

---

## Sync pagination

For code that cannot use `async`/`await`, import the synchronous variant:

```python
from bb.cloud.sdk._pagination import paginate
from bb.cloud.sdk import repos

def list_repos_sync(client, workspace: str):
    for repo in paginate(repos.list, client, workspace, limit=50):
        print(repo.full_name)
```

`paginate` has the same signature as `async_paginate` and returns a regular `Iterator[T]`.
