"""Custom deprecation handling for Bitbucket Data Center API endpoints.

Unlike the Cloud SDK, Bitbucket Data Center does not publish scheduled
endpoint removal dates, so ``deprecated_endpoint`` unconditionally emits
a :class:`DeprecationWarning` on every call with no date-based blocking.

This module is injected into generated ``bb.datacenter.api.*`` modules by
the post-generation hook ``scripts/apply_deprecations_dc.py``.  The
decorator is applied to ``sync_detailed``, ``sync``, ``asyncio_detailed``,
and ``asyncio`` in each deprecated endpoint module.
"""

from __future__ import annotations

import warnings
from collections.abc import Callable
from functools import wraps
from typing import Any, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


def _endpoint_name(func: Callable[..., Any]) -> str:
    return f"{func.__module__}.{func.__name__}"


def deprecated_endpoint(removal_date: str | None = None) -> Callable[[F], F]:
    """Mark a generated API endpoint function as deprecated.

    Emits :class:`DeprecationWarning` on every call.  The *removal_date*
    parameter is accepted for API compatibility with the Cloud SDK decorator
    but is **ignored** — DC does not publish removal dates.

    Args:
        removal_date: Ignored. Present for parity with the Cloud version.
            Pass ``None`` or omit entirely.

    Returns:
        A decorator that wraps the target function (sync or async) and
        emits :class:`DeprecationWarning` before delegating to it.

    Example (injected by ``apply_deprecations_dc.py``)::

        from ...deprecation import deprecated_endpoint

        @deprecated_endpoint(None)
        def sync_detailed(...):
            ...

        @deprecated_endpoint(None)
        async def asyncio(...):
            ...
    """

    def decorator(func: F) -> F:
        endpoint = _endpoint_name(func)
        msg = f"'{endpoint}' is deprecated in the Bitbucket Data Center REST API."

        if _is_async(func):

            @wraps(func)
            async def async_wrapper(*args: Any, **kwargs: Any) -> Any:
                warnings.warn(msg, DeprecationWarning, stacklevel=2)
                return await func(*args, **kwargs)  # type: ignore[misc]

            return async_wrapper  # type: ignore[return-value]

        else:

            @wraps(func)
            def sync_wrapper(*args: Any, **kwargs: Any) -> Any:
                warnings.warn(msg, DeprecationWarning, stacklevel=2)
                return func(*args, **kwargs)

            return sync_wrapper  # type: ignore[return-value]

    return decorator  # type: ignore[return-value]


def _is_async(func: Callable[..., Any]) -> bool:
    """Return True if *func* is a coroutine function."""
    import asyncio

    return asyncio.iscoroutinefunction(func)
