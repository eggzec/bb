from __future__ import annotations

import asyncio

from bb.cloud.models.search_code_search_result import SearchCodeSearchResult
from bb.cloud.sdk import search as _async
from bb.cloud.sdk._client import BBClient
from bb.cloud.types import UNSET, Unset

__all__ = ["code", "account", "team"]


def code(
    client: BBClient,
    workspace: str,
    *,
    query: str,
    search_query: str | Unset = UNSET,
    pagelen: int = 10,
) -> list[SearchCodeSearchResult]:
    """Sync version of :func:`~bb.cloud.sdk.search.code`."""
    return asyncio.run(_async.code(client, workspace, query=query, search_query=search_query, pagelen=pagelen))


def account(
    client: BBClient,
    selected_user: str,
    *,
    search_query: str,
    pagelen: int = 10,
) -> list[SearchCodeSearchResult]:
    """Sync version of :func:`~bb.cloud.sdk.search.account`.

    Warning:
        Deprecated. Use :func:`code` with a workspace slug instead.
    """
    return asyncio.run(_async.account(client, selected_user, search_query=search_query, pagelen=pagelen))


def team(
    client: BBClient,
    username: str,
    *,
    search_query: str,
    pagelen: int = 10,
) -> list[SearchCodeSearchResult]:
    """Sync version of :func:`~bb.cloud.sdk.search.team`.

    Warning:
        Deprecated. Use :func:`code` with a workspace slug instead.
    """
    return asyncio.run(_async.team(client, username, search_query=search_query, pagelen=pagelen))
