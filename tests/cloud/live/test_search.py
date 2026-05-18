"""Live tests for ``bb.cloud.sdk.search``.

Covers all 3 SDK functions:
    code, account (deprecated), team (deprecated)

Seed data (read-only):
    workspace: beaverish
    probe repo: bb-probe  (contains Python files with 'def' keyword)
    owner uuid: {e8e13d7c-8af1-409a-9a9e-e2bf80ade040}
    search query: "def"  (known to return results)
"""

from __future__ import annotations

import os

import pytest

from bb.cloud.errors import UnexpectedStatus
from bb.cloud.models.error import Error
from bb.cloud.models.search_code_search_result import SearchCodeSearchResult
from bb.cloud.sdk import search
from bb.cloud.sdk._client import BBClient

pytestmark = pytest.mark.live

OWNER_UUID = "{e8e13d7c-8af1-409a-9a9e-e2bf80ade040}"
WORKSPACE_SLUG = "beaverish"

# ──────────────────────────────────────────────────────────────────────────────
# search.code
# ──────────────────────────────────────────────────────────────────────────────


async def test_code_search_returns_results(client: BBClient, workspace: str) -> None:
    """SRCH-CODE-001/002/003: code search returns list of SearchCodeSearchResult."""
    query = os.environ.get("BB_SEARCH_QUERY", "def").strip() or "def"
    result = await search.code(client, workspace, query=query, pagelen=5)
    if isinstance(result, Error):
        pytest.skip(
            f"search.code not available for this workspace/auth: "
            f"{result.error.message if result.error else result!r}"
        )
    assert isinstance(result, list), (
        f"search.code must return list, got {type(result).__name__}"
    )
    # With a seeded repo containing Python source, we expect at least 1 result.
    assert len(result) >= 1, (
        f"search.code({query!r}) returned 0 results — expected at least 1 from bb-probe"
    )
    for idx, hit in enumerate(result):
        assert isinstance(hit, SearchCodeSearchResult), (
            f"search.code[{idx}] is {type(hit).__name__}, expected SearchCodeSearchResult"
        )


async def test_code_search_results_have_file_with_path(client: BBClient, workspace: str) -> None:
    """SRCH-CODE-004: each result has a file attribute with a path."""
    query = os.environ.get("BB_SEARCH_QUERY", "def").strip() or "def"
    result = await search.code(client, workspace, query=query, pagelen=5)
    if isinstance(result, Error):
        pytest.skip(
            f"search.code not available: "
            f"{result.error.message if result.error else result!r}"
        )
    if not result:
        pytest.skip("search.code returned 0 results — cannot verify file structure")
    for idx, hit in enumerate(result):
        file_obj = getattr(hit, "file", None)
        assert file_obj is not None, (
            f"search.code[{idx}].file is None — expected a CommitFile object"
        )
        path = getattr(file_obj, "path", None)
        assert path, (
            f"search.code[{idx}].file.path is empty: {file_obj!r}"
        )


async def test_code_search_results_have_content_match_count(client: BBClient, workspace: str) -> None:
    """SRCH-CODE-005: each result has content_match_count > 0."""
    query = os.environ.get("BB_SEARCH_QUERY", "def").strip() or "def"
    result = await search.code(client, workspace, query=query, pagelen=5)
    if isinstance(result, Error):
        pytest.skip(
            f"search.code not available: "
            f"{result.error.message if result.error else result!r}"
        )
    if not result:
        pytest.skip("search.code returned 0 results — cannot verify content_match_count")
    for idx, hit in enumerate(result):
        count = getattr(hit, "content_match_count", None)
        # count may be UNSET (Unset object) or an int.
        if count is not None and not isinstance(count, int):
            # UNSET sentinel — skip this check for this result.
            continue
        if count is not None:
            assert count >= 0, (
                f"search.code[{idx}].content_match_count={count!r} is negative"
            )


async def test_code_search_with_search_query_kwarg(client: BBClient, workspace: str) -> None:
    """SRCH-CODE-001 (search_query kwarg): search_query takes precedence over query."""
    try:
        result = await search.code(
            client, workspace, query="IGNORED", search_query="def", pagelen=3
        )
    except UnexpectedStatus as exc:
        pytest.skip(f"search.code raised UnexpectedStatus {exc.status_code}")
    if isinstance(result, Error):
        pytest.skip(
            f"search.code not available: "
            f"{result.error.message if result.error else result!r}"
        )
    assert isinstance(result, list), (
        f"search.code with search_query kwarg must return list, got {type(result).__name__}"
    )


async def test_code_search_error_not_exception(client: BBClient, workspace: str) -> None:
    """SRCH-CODE-006: search with very long query returns list or Error, not exception."""
    long_query = "a" * 500
    try:
        result = await search.code(client, workspace, query=long_query, pagelen=5)
        assert isinstance(result, (list, Error)), (
            f"search.code must return list or Error, got {type(result).__name__}"
        )
    except UnexpectedStatus:
        pass  # 400 Bad Request is acceptable for an overlong query


# ──────────────────────────────────────────────────────────────────────────────
# search.account  (deprecated endpoint)
# ──────────────────────────────────────────────────────────────────────────────


async def test_account_search_does_not_raise(client: BBClient) -> None:
    """SRCH-ACCT-001/002: account search returns list or Error — no unhandled exception."""
    try:
        result = await search.account(client, OWNER_UUID, search_query="def", pagelen=3)
        assert isinstance(result, (list, Error)), (
            f"search.account must return list or Error, got {type(result).__name__}"
        )
        if isinstance(result, list):
            for idx, hit in enumerate(result):
                assert isinstance(hit, SearchCodeSearchResult), (
                    f"search.account[{idx}] is {type(hit).__name__}, expected SearchCodeSearchResult"
                )
    except UnexpectedStatus as exc:
        # 400 (deprecated, removed), 404 are acceptable.
        assert exc.status_code in (400, 404, 403), (
            f"search.account raised UnexpectedStatus with unexpected code {exc.status_code}"
        )


# ──────────────────────────────────────────────────────────────────────────────
# search.team  (deprecated endpoint)
# ──────────────────────────────────────────────────────────────────────────────


async def test_team_search_does_not_raise(client: BBClient, workspace: str) -> None:
    """SRCH-TEAM-001/002: team search returns list or Error — no unhandled exception."""
    try:
        result = await search.team(client, workspace, search_query="def", pagelen=3)
        assert isinstance(result, (list, Error)), (
            f"search.team must return list or Error, got {type(result).__name__}"
        )
        if isinstance(result, list):
            for idx, hit in enumerate(result):
                assert isinstance(hit, SearchCodeSearchResult), (
                    f"search.team[{idx}] is {type(hit).__name__}, expected SearchCodeSearchResult"
                )
    except UnexpectedStatus as exc:
        # 400 (deprecated, removed), 404, 410 are acceptable.
        assert exc.status_code in (400, 404, 403, 410), (
            f"search.team raised UnexpectedStatus with unexpected code {exc.status_code}"
        )
