from collections.abc import AsyncIterator, Callable, Iterator
from typing import Any, TypeVar

from bb.cloud.types import UNSET, Unset

T = TypeVar("T")


def paginate(fn: Callable[..., Any], *args: Any, pagelen: int = 25, **kwargs: Any) -> Iterator[T]:
    """Yield all items from a sync page-based paginated list endpoint.

    ``fn`` must be a ``sync()`` that accepts ``page`` and ``pagelen`` keyword
    arguments and returns a Paginated* model with ``.values`` and ``.next_``.
    """
    page = 1
    while True:
        result = fn(*args, page=page, pagelen=pagelen, **kwargs)
        if result is None:
            break
        values = getattr(result, "values", UNSET)
        if isinstance(values, Unset) or not values:
            break
        yield from values
        next_ = getattr(result, "next_", UNSET)
        if isinstance(next_, Unset) or not next_:
            break
        page += 1


async def async_paginate(fn: Callable[..., Any], *args: Any, pagelen: int = 25, **kwargs: Any) -> AsyncIterator[T]:
    """Yield all items from an async page-based paginated list endpoint.

    ``fn`` must be an ``asyncio()`` coroutine that accepts ``page`` and
    ``pagelen`` keyword arguments and returns a Paginated* model with
    ``.values`` and ``.next_``.

    Usage::

        from bb.cloud.sdk._pagination import async_paginate
        from bb.cloud.api.repositories.get_repositories_workspace import asyncio

        repos = [r async for r in async_paginate(asyncio, workspace, client=client.auth)]
    """
    page = 1
    while True:
        result = await fn(*args, page=page, pagelen=pagelen, **kwargs)
        if result is None:
            break
        values = getattr(result, "values", UNSET)
        if isinstance(values, Unset) or not values:
            break
        for item in values:
            yield item
        next_ = getattr(result, "next_", UNSET)
        if isinstance(next_, Unset) or not next_:
            break
        page += 1
