"""Pagination helpers for the Bitbucket Data Center SDK.

Bitbucket Data Center REST API uses cursor-based pagination with the following
fields on list responses:

    ``start``         – current start index (integer)
    ``limit``         – page size (float/integer)
    ``is_last_page``  – ``True`` when there are no more results
    ``next_page_start`` – start index for the next page (absent on last page)
    ``values``        – the list of items for this page

Usage::

    from bb.datacenter.sdk._pagination import paginate, async_paginate
    from bb.datacenter.api.project.get_repositories import asyncio

    repos = [r async for r in async_paginate(asyncio, project_key="PRJ", client=client.auth)]
"""

from __future__ import annotations

from collections.abc import AsyncIterator, Callable, Iterator
from typing import Any, TypeVar

from bb.datacenter.types import UNSET, Unset

T = TypeVar("T")


def paginate(fn: Callable[..., Any], *args: Any, limit: int = 25, **kwargs: Any) -> Iterator[T]:
    """Yield all items from a sync page-based paginated list endpoint.

    ``fn`` must be a ``sync()`` that accepts ``start`` and ``limit`` keyword
    arguments and returns a paged response model with ``.is_last_page`` and
    ``.values``.

    Args:
        fn: A generated ``sync()`` function for a paginated endpoint.
        *args: Positional arguments forwarded to *fn*.
        limit: Number of items per page. Defaults to ``25``.
        **kwargs: Keyword arguments forwarded to *fn*.

    Yields:
        Individual items from across all pages.
    """
    start = 0
    while True:
        result = fn(*args, start=start, limit=limit, **kwargs)
        if result is None:
            break
        values = getattr(result, "values", UNSET)
        if isinstance(values, Unset) or not values:
            break
        yield from values
        is_last_page = getattr(result, "is_last_page", UNSET)
        if is_last_page is True:
            break
        next_page_start = getattr(result, "next_page_start", UNSET)
        if isinstance(next_page_start, Unset) or next_page_start is None:
            break
        start = next_page_start


async def async_paginate(fn: Callable[..., Any], *args: Any, limit: int = 25, **kwargs: Any) -> AsyncIterator[T]:
    """Yield all items from an async page-based paginated list endpoint.

    ``fn`` must be an ``asyncio()`` coroutine that accepts ``start`` and
    ``limit`` keyword arguments and returns a paged response model with
    ``.is_last_page`` and ``.values``.

    Args:
        fn: A generated ``asyncio()`` coroutine for a paginated endpoint.
        *args: Positional arguments forwarded to *fn*.
        limit: Number of items per page. Defaults to ``25``.
        **kwargs: Keyword arguments forwarded to *fn*.

    Yields:
        Individual items from across all pages.

    Usage::

        from bb.datacenter.sdk._pagination import async_paginate
        from bb.datacenter.api.project.get_repositories import asyncio

        repos = [r async for r in async_paginate(asyncio, "PRJ", client=client.auth)]
    """
    start = 0
    while True:
        result = await fn(*args, start=start, limit=limit, **kwargs)
        if result is None:
            break
        values = getattr(result, "values", UNSET)
        if isinstance(values, Unset) or not values:
            break
        for item in values:
            yield item
        is_last_page = getattr(result, "is_last_page", UNSET)
        if is_last_page is True:
            break
        next_page_start = getattr(result, "next_page_start", UNSET)
        if isinstance(next_page_start, Unset) or next_page_start is None:
            break
        start = next_page_start
