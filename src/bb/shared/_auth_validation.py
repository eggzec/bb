"""Shared ``require_auth`` decorator factory for Bitbucket SDK targets.

Both Cloud and Data Center SDKs need a ``require_auth`` decorator that:

1. Declares which :class:`AuthMethod` values an endpoint accepts.
2. Validates ``client.auth`` against those methods at call time.
3. Raises :exc:`~bb.shared._errors.AuthenticationError` on mismatch.

The validation logic (which methods are valid, how to infer the method from
``client.auth.prefix``) is target-specific.  This module provides
:func:`make_require_auth`, a factory that binds the target's ``_validate``
function to the generic decorator machinery.

Usage in each target's ``_auth_validation.py``::

    from bb.shared._auth_validation import make_require_auth

    # After defining the local _validate() function:
    require_auth = make_require_auth(_validate)
"""

from __future__ import annotations

import functools
from collections.abc import Awaitable, Callable
from typing import Any, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def make_require_auth(
    validate_fn: Callable[..., None],
) -> Callable[..., Callable[[Callable[P, Awaitable[R]]], Callable[P, Awaitable[R]]]]:
    """Return a ``require_auth`` decorator factory bound to *validate_fn*.

    Args:
        validate_fn: A callable with signature
            ``(client, allowed: frozenset[AuthMethod]) -> None`` that raises
            :exc:`~bb.shared._errors.AuthenticationError` when validation
            fails.  Typically the ``_validate`` function defined in the
            target's ``_auth_validation`` module.

    Returns:
        A ``require_auth(*methods)`` decorator factory with the same interface
        as if it had been defined locally — only the validation logic differs.

    Example::

        from bb.shared._auth_validation import make_require_auth

        # Bind the factory to this target's _validate function
        require_auth = make_require_auth(_validate)

        @require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
        async def get(client, workspace, repo_slug):
            ...
    """

    def require_auth(
        *methods: Any,
    ) -> Callable[[Callable[P, Awaitable[R]]], Callable[P, Awaitable[R]]]:
        allowed: frozenset[Any] = frozenset(methods)

        def decorator(
            func: Callable[P, Awaitable[R]],
        ) -> Callable[P, Awaitable[R]]:
            @functools.wraps(func)
            async def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
                # ``client`` is always the first positional argument.
                validate_fn(args[0], allowed)  # type: ignore[arg-type]
                return await func(*args, **kwargs)

            return wrapper

        return decorator

    return require_auth
