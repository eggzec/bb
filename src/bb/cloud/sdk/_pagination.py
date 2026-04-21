"""Pagination helpers for Bitbucket Cloud page-based list endpoints.

Bitbucket Cloud uses page-based pagination with ``page`` / ``pagelen`` query
parameters and responses of the form::

    { "values": [...], "next": "...", "page": 1, "size": ... }

The generated models expose these as ``result.values`` and ``result.next_``.

This module provides two complementary APIs:

* :func:`paginate` / :func:`async_paginate` — **collect** helpers that return a
  flat ``list`` on success or the :class:`~bb.cloud.models.error.Error`
  object on failure. These are what the SDK resource modules use internally.

* :func:`iter_pages` / :func:`aiter_pages` — **generator** helpers for callers
  that want lazy streaming. They yield items one at a time and stop on the
  first error/empty page. Use when you don't need the whole list up front.
"""

from __future__ import annotations

import inspect
from collections.abc import AsyncIterator, Awaitable, Callable, Iterator
from functools import cache
from typing import Any

from bb.cloud.models.error import Error
from bb.cloud.types import UNSET, Unset

__all__ = [
    "paginate",
    "async_paginate",
    "iter_pages",
    "aiter_pages",
]


@cache
def _accepts(fn: Callable[..., Any], name: str) -> bool:
    """Return True iff *fn* declares a keyword argument called *name*.

    A handful of Bitbucket Cloud paginated endpoints omit ``page``/``pagelen``
    from their OpenAPI spec even though the live API accepts them. We inspect
    the generated signature to avoid ``TypeError`` from unexpected kwargs.
    """
    try:
        params = inspect.signature(fn).parameters
    except (TypeError, ValueError):
        return True  # be permissive when introspection fails
    if name in params:
        return True
    # Functions declaring **kwargs are treated as accepting *name*.
    return any(p.kind is inspect.Parameter.VAR_KEYWORD for p in params.values())


def _page_kwargs(fn: Callable[..., Any], page: int, pagelen: int) -> dict[str, Any]:
    kw: dict[str, Any] = {}
    if _accepts(fn, "page"):
        kw["page"] = page
    if _accepts(fn, "pagelen"):
        kw["pagelen"] = pagelen
    return kw


def _should_stop(result: Any) -> bool:
    """Return True when the paginator loop should terminate on *result*."""
    if result is None:
        return True
    values = getattr(result, "values", UNSET)
    return isinstance(values, Unset) or not values


def _values(result: Any) -> list[Any]:
    values = getattr(result, "values", UNSET)
    return [] if isinstance(values, Unset) else list(values)


def _has_next(result: Any) -> bool:
    next_ = getattr(result, "next_", UNSET)
    return not (isinstance(next_, Unset) or not next_)


def paginate(
    fn: Callable[..., Any],
    *args: Any,
    pagelen: int = 25,
    **kwargs: Any,
) -> list[Any] | Error:
    """Collect every item from a **sync** page-based list endpoint.

    ``fn`` must accept ``page`` and ``pagelen`` keyword arguments and return
    a ``Paginated*`` model (with ``.values`` / ``.next_``) or an
    :class:`~bb.cloud.models.error.Error`.

    Returns a flat ``list`` of items on success, or the first ``Error``
    encountered.
    """
    items: list[Any] = []
    page = 1
    paged = _accepts(fn, "page")
    while True:
        result = fn(*args, **_page_kwargs(fn, page, pagelen), **kwargs)
        if isinstance(result, Error):
            return result
        if _should_stop(result):
            break
        items.extend(_values(result))
        if not paged or not _has_next(result):
            break
        page += 1
    return items


async def async_paginate(
    fn: Callable[..., Awaitable[Any]],
    *args: Any,
    pagelen: int = 25,
    **kwargs: Any,
) -> list[Any] | Error:
    """Async counterpart of :func:`paginate`.

    ``fn`` must be an ``asyncio()`` coroutine that accepts ``page`` /
    ``pagelen``. Returns a flat list on success or ``Error`` on failure.
    """
    items: list[Any] = []
    page = 1
    paged = _accepts(fn, "page")
    while True:
        result = await fn(*args, **_page_kwargs(fn, page, pagelen), **kwargs)
        if isinstance(result, Error):
            return result
        if _should_stop(result):
            break
        items.extend(_values(result))
        if not paged or not _has_next(result):
            break
        page += 1
    return items


def iter_pages(
    fn: Callable[..., Any],
    *args: Any,
    pagelen: int = 25,
    **kwargs: Any,
) -> Iterator[Any]:
    """Yield items lazily from a sync page-based endpoint.

    Stops silently on empty pages, ``None`` results, or
    :class:`~bb.cloud.models.error.Error` responses — use :func:`paginate`
    if you need explicit error signalling.
    """
    page = 1
    paged = _accepts(fn, "page")
    while True:
        result = fn(*args, **_page_kwargs(fn, page, pagelen), **kwargs)
        if isinstance(result, Error) or _should_stop(result):
            return
        yield from _values(result)
        if not paged or not _has_next(result):
            return
        page += 1


async def aiter_pages(
    fn: Callable[..., Awaitable[Any]],
    *args: Any,
    pagelen: int = 25,
    **kwargs: Any,
) -> AsyncIterator[Any]:
    """Async counterpart of :func:`iter_pages`."""
    page = 1
    paged = _accepts(fn, "page")
    while True:
        result = await fn(*args, **_page_kwargs(fn, page, pagelen), **kwargs)
        if isinstance(result, Error) or _should_stop(result):
            return
        for item in _values(result):
            yield item
        if not paged or not _has_next(result):
            return
        page += 1
