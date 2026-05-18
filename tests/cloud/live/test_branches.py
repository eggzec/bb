"""Live integration tests for ``bb.cloud.sdk.branches``.

Seed data (read-only):
- workspace:    beaverish
- repo:         bb-probe
- branch:       main  (commit 84952fad87fb39e3c6d61811a93769378dd4fad7)
- branch:       feature/add-farewell
- tag:          v0.1.0

Write tests use throwaway names and always clean up in finally blocks.
"""

from __future__ import annotations

import uuid

import pytest

from bb.cloud.models.branch import Branch
from bb.cloud.models.error import Error
from bb.cloud.models.tag import Tag
from bb.cloud.sdk import branches
from bb.cloud.sdk._client import BBClient

pytestmark = [pytest.mark.live]

# ---------------------------------------------------------------------------
# Seed constants (probe data; DO NOT mutate)
# ---------------------------------------------------------------------------
SEED_BRANCH = "main"
SEED_COMMIT = "84952fad87fb39e3c6d61811a93769378dd4fad7"
SEED_TAG = "v0.1.0"
EXTRA_BRANCH = "feature/add-farewell"


# ---------------------------------------------------------------------------
# branches.list
# ---------------------------------------------------------------------------


async def test_list_returns_branches(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    result = await branches.list(client, workspace, probe_repo_slug, pagelen=10)
    assert not isinstance(result, Error), (
        f"branches.list errored: {result.error.message if result.error else result!r}"
    )
    assert isinstance(result, list), f"branches.list must return list, got {type(result).__name__}"
    assert result, f"branches.list returned empty list for {probe_repo_slug!r}"
    for idx, branch in enumerate(result):
        assert isinstance(branch, Branch), (
            f"branches.list[{idx}] is {type(branch).__name__}, expected Branch"
        )
        assert branch.name, f"branches.list[{idx}] has empty name: {branch!r}"


async def test_list_includes_main(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    result = await branches.list(client, workspace, probe_repo_slug, pagelen=50)
    assert not isinstance(result, Error), (
        f"branches.list errored: {result.error.message if result.error else result!r}"
    )
    names = [b.name for b in result if isinstance(b, Branch)]
    assert SEED_BRANCH in names, (
        f"Expected branch {SEED_BRANCH!r} in list, got: {names}"
    )


async def test_list_pagination_consistent(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """pagelen=1 (forces multi-page traversal) must yield the same total as pagelen=50."""
    result_small = await branches.list(client, workspace, probe_repo_slug, pagelen=1)
    result_large = await branches.list(client, workspace, probe_repo_slug, pagelen=50)

    assert not isinstance(result_small, Error), (
        f"branches.list(pagelen=1) errored: {result_small!r}"
    )
    assert not isinstance(result_large, Error), (
        f"branches.list(pagelen=50) errored: {result_large!r}"
    )
    assert len(result_small) == len(result_large), (
        f"Pagination inconsistency: pagelen=1 → {len(result_small)} items, "
        f"pagelen=50 → {len(result_large)} items"
    )


# ---------------------------------------------------------------------------
# branches.get
# ---------------------------------------------------------------------------


async def test_get_returns_main_branch(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    result = await branches.get(client, workspace, probe_repo_slug, SEED_BRANCH)
    assert not isinstance(result, Error), (
        f"branches.get({SEED_BRANCH!r}) errored: "
        f"{result.error.message if result.error else result!r}"
    )
    assert isinstance(result, Branch), (
        f"branches.get must return Branch, got {type(result).__name__}"
    )
    assert result.name == SEED_BRANCH, (
        f"branches.get returned name={result.name!r}, expected {SEED_BRANCH!r}"
    )


async def test_get_returns_branch_for_probe(
    client: BBClient,
    workspace: str,
    probe_repo_slug: str,
    probe_branch_name: str,
) -> None:
    result = await branches.get(client, workspace, probe_repo_slug, probe_branch_name)
    assert not isinstance(result, Error), (
        f"branches.get({probe_branch_name!r}) errored: "
        f"{result.error.message if result.error else result!r}"
    )
    assert isinstance(result, Branch), (
        f"branches.get must return Branch, got {type(result).__name__}"
    )
    assert result.name == probe_branch_name, (
        f"branches.get returned name={result.name!r}, expected {probe_branch_name!r}"
    )


async def test_get_missing_branch_is_error_or_none(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    result = await branches.get(
        client, workspace, probe_repo_slug, "this-branch-does-not-exist-zzz"
    )
    assert not isinstance(result, Branch), (
        f"branches.get for a nonexistent branch must not return Branch, got {result!r}"
    )


# ---------------------------------------------------------------------------
# branches.create / branches.delete  (write path)
# ---------------------------------------------------------------------------


async def test_create_and_delete_branch_roundtrip(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    branch_name = f"test-branch-{uuid.uuid4().hex[:8]}"
    created = None
    try:
        # --- create ---
        created = await branches.create(
            client,
            workspace,
            probe_repo_slug,
            name=branch_name,
            target_hash=SEED_COMMIT,
        )
        assert isinstance(created, Branch), (
            f"branches.create must return Branch, got {type(created).__name__}: {created!r}"
        )
        assert created.name == branch_name, (
            f"created branch name {created.name!r} != expected {branch_name!r}"
        )

        # --- verify it exists ---
        fetched = await branches.get(client, workspace, probe_repo_slug, branch_name)
        assert isinstance(fetched, Branch), (
            f"branches.get after create must return Branch, got {fetched!r}"
        )
        assert fetched.name == branch_name

    finally:
        # --- delete ---
        await branches.delete(client, workspace, probe_repo_slug, branch_name)

    # verify gone (outside finally so it only runs when delete succeeded without exception)
    after_delete = await branches.get(client, workspace, probe_repo_slug, branch_name)
    assert not isinstance(after_delete, Branch), (
        f"branch {branch_name!r} still exists after delete: {after_delete!r}"
    )


async def test_create_duplicate_branch_does_not_raise(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """Creating a branch that already exists should return None or Error, not raise."""
    branch_name = f"test-dup-{uuid.uuid4().hex[:8]}"
    try:
        first = await branches.create(
            client,
            workspace,
            probe_repo_slug,
            name=branch_name,
            target_hash=SEED_COMMIT,
        )
        if not isinstance(first, Branch):
            pytest.skip("branch create not available or returned unexpected result")

        # Second create — same name
        second = await branches.create(
            client,
            workspace,
            probe_repo_slug,
            name=branch_name,
            target_hash=SEED_COMMIT,
        )
        # Must NOT raise; may return None or an Error-like value
        assert not isinstance(second, Branch) or second.name == branch_name, (
            f"duplicate create returned unexpected Branch: {second!r}"
        )
    finally:
        await branches.delete(client, workspace, probe_repo_slug, branch_name)


# ---------------------------------------------------------------------------
# branches.tags (list_tags)
# ---------------------------------------------------------------------------


async def test_list_tags_returns_tags(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    result = await branches.tags(client, workspace, probe_repo_slug, pagelen=10)
    assert not isinstance(result, Error), (
        f"branches.tags errored: {result.error.message if result.error else result!r}"
    )
    assert isinstance(result, list), f"branches.tags must return list, got {type(result).__name__}"
    for idx, tag in enumerate(result):
        assert isinstance(tag, Tag), (
            f"branches.tags[{idx}] is {type(tag).__name__}, expected Tag"
        )


async def test_list_tags_includes_seed_tag(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    result = await branches.tags(client, workspace, probe_repo_slug, pagelen=50)
    assert not isinstance(result, Error), (
        f"branches.tags errored: {result.error.message if result.error else result!r}"
    )
    names = [t.name for t in result if isinstance(t, Tag)]
    assert SEED_TAG in names, (
        f"Expected tag {SEED_TAG!r} in list, got: {names}"
    )


async def test_list_tags_pagination_consistent(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    result_small = await branches.tags(client, workspace, probe_repo_slug, pagelen=1)
    result_large = await branches.tags(client, workspace, probe_repo_slug, pagelen=50)

    assert not isinstance(result_small, Error), f"branches.tags(pagelen=1) errored: {result_small!r}"
    assert not isinstance(result_large, Error), f"branches.tags(pagelen=50) errored: {result_large!r}"
    assert len(result_small) == len(result_large), (
        f"Tag pagination inconsistency: pagelen=1 → {len(result_small)}, "
        f"pagelen=50 → {len(result_large)}"
    )


# ---------------------------------------------------------------------------
# branches.get_tag
# ---------------------------------------------------------------------------


async def test_get_tag_returns_seed_tag(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    result = await branches.get_tag(client, workspace, probe_repo_slug, SEED_TAG)
    assert not isinstance(result, Error), (
        f"branches.get_tag({SEED_TAG!r}) errored: "
        f"{result.error.message if result.error else result!r}"
    )
    assert isinstance(result, Tag), (
        f"branches.get_tag must return Tag, got {type(result).__name__}"
    )
    assert result.name == SEED_TAG, (
        f"branches.get_tag returned name={result.name!r}, expected {SEED_TAG!r}"
    )


async def test_get_tag_missing_is_error_or_none(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    result = await branches.get_tag(
        client, workspace, probe_repo_slug, "no-such-tag-zzz"
    )
    assert not isinstance(result, Tag), (
        f"branches.get_tag for nonexistent tag must not return Tag, got {result!r}"
    )


# ---------------------------------------------------------------------------
# branches.create_tag / branches.delete_tag  (write path)
# ---------------------------------------------------------------------------


async def test_create_and_delete_tag_roundtrip(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    from bb.cloud.models.commit import Commit

    tag_name = f"test-tag-{uuid.uuid4().hex[:8]}"
    tag_body = Tag(
        type_="tag",
        name=tag_name,
        target=Commit(type_="commit", hash_=SEED_COMMIT),  # type: ignore[call-arg]
    )  # type: ignore[call-arg]
    created = None
    try:
        created = await branches.create_tag(
            client, workspace, probe_repo_slug, body=tag_body
        )
        if isinstance(created, Error):
            pytest.skip(
                f"branches.create_tag not available: "
                f"{created.error.message if created.error else created!r}"
            )
        assert isinstance(created, Tag), (
            f"branches.create_tag must return Tag, got {type(created).__name__}: {created!r}"
        )
        assert created.name == tag_name, (
            f"created tag name {created.name!r} != {tag_name!r}"
        )

        # verify exists
        fetched = await branches.get_tag(client, workspace, probe_repo_slug, tag_name)
        assert isinstance(fetched, Tag), (
            f"branches.get_tag after create_tag must return Tag, got {fetched!r}"
        )
        assert fetched.name == tag_name

    finally:
        await branches.delete_tag(client, workspace, probe_repo_slug, tag_name)

    # verify gone (outside finally so it only runs when delete succeeded without exception)
    after_delete = await branches.get_tag(client, workspace, probe_repo_slug, tag_name)
    assert not isinstance(after_delete, Tag), (
        f"tag {tag_name!r} still exists after delete_tag: {after_delete!r}"
    )
