# Pagination

## How DC pagination works

The Bitbucket Data Center REST API uses cursor-based pagination. Each list response includes:

| Field | Type | Description |
|---|---|---|
| `values` | list | Items on the current page |
| `start` | int | Start index of the current page |
| `limit` | int | Maximum items per page |
| `is_last_page` | bool | `True` when no further pages exist |
| `next_page_start` | int | Start index to use for the next request (absent on last page) |

To retrieve subsequent pages, pass `next_page_start` as the `start` parameter of the next request. The `paginate` and `async_paginate` helpers handle this loop automatically.

## Difference from the Cloud SDK

The Cloud SDK materialises all pages internally for most list functions, returning `list[T]` directly. The DC SDK does not do this at the generated-API level — callers are responsible for pagination.

Some higher-level SDK wrapper functions (`repos.list`, `prs.list`, `branches.list`, etc.) call `async_paginate` internally and return a fully materialised list. For direct use of generated API functions, or for streaming results without building the full list in memory, use `async_paginate` or `paginate` directly.

## async_paginate

`async_paginate` is the primary pagination pattern for the DC SDK. It is an async generator that yields individual items across all pages.

```python
async_paginate(fn, *args, limit=25, **kwargs) -> AsyncIterator[T]
```

- `fn`: An async generated API function (`asyncio()`) or an SDK wrapper function that accepts `start` and `limit` keyword arguments.
- `*args`: Positional arguments forwarded to `fn`.
- `limit`: Items per page request. Defaults to `25`.
- `**kwargs`: Keyword arguments forwarded to `fn`.

**Example — iterate all repos in a project:**

```python
import asyncio
from bb.datacenter import BBDCClient
from bb.datacenter.sdk import repos
from bb.datacenter.sdk._pagination import async_paginate

async def main():
    client = BBDCClient.from_env()

    async for repo in async_paginate(repos.list, client, "PRJ", limit=50):
        print(repo.slug)

asyncio.run(main())
```

**Example — collect all results into a list:**

```python
import asyncio
from bb.datacenter import BBDCClient
from bb.datacenter.sdk import repos
from bb.datacenter.sdk._pagination import async_paginate

async def main():
    client = BBDCClient.from_env()

    all_repos = [
        repo
        async for repo in async_paginate(repos.list, client, "PRJ", limit=50)
    ]
    print(len(all_repos))

asyncio.run(main())
```

## paginate

`paginate` is the synchronous equivalent of `async_paginate`. Use it when you cannot run an event loop.

```python
paginate(fn, *args, limit=25, **kwargs) -> Iterator[T]
```

- `fn`: A sync generated API function (`sync()`) that accepts `start` and `limit` keyword arguments.
- `*args`: Positional arguments forwarded to `fn`.
- `limit`: Items per page request. Defaults to `25`.
- `**kwargs`: Keyword arguments forwarded to `fn`.

**Example — sync iteration over repos:**

```python
from bb.datacenter.sdk._pagination import paginate
from bb.datacenter.api.project.get_repositories import sync as get_repos_sync
from bb.datacenter import BBDCClient

client = BBDCClient.from_env()

for repo in paginate(get_repos_sync, "PRJ", client=client.auth, limit=25):
    print(repo.slug)
```

!!! note
    `paginate` is intended for use with generated `sync()` functions from `bb.datacenter.api`. The higher-level SDK wrapper functions (`repos.list`, `branches.list`, etc.) are async-only and must be used with `async_paginate` or called directly inside an async context.

## limit parameter

The `limit` parameter controls how many items are requested per page. The default is `25`.

Bitbucket Data Center enforces a server-side maximum page size. Requesting a `limit` larger than the server allows results in the server silently capping the response to its maximum. The SDK does not enforce or document a specific upper bound — check your instance configuration if you see responses consistently returning fewer items than requested.

Setting a higher `limit` reduces the number of round trips for large result sets at the cost of larger individual responses. For most workloads, values between `25` and `100` are reasonable.

!!! note
    SDK wrapper functions such as `branches.list`, `repos.list`, and `prs.list` accept a `limit` keyword argument and pass it through to `async_paginate` internally. These functions return a fully materialised `list[T]`, so the `limit` only affects page size during fetching, not the size of the returned list. If you need to stream results without building a full list in memory, call `async_paginate` directly with the underlying generated API function.
