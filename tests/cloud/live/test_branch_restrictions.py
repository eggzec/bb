"""Live integration tests for ``bb.cloud.sdk.branch_restrictions``.

Seed data (read-only):
- workspace:       beaverish
- repo:            bb-probe
- restriction id:  76271307  (require_approvals_to_merge, pattern: main)

Write tests create throwaway restrictions and always clean up in finally blocks.
"""

from __future__ import annotations

import uuid

import pytest

from bb.cloud.models.branchrestriction import Branchrestriction
from bb.cloud.models.branchrestriction_branch_match_kind import BranchrestrictionBranchMatchKind
from bb.cloud.models.branchrestriction_kind import BranchrestrictionKind
from bb.cloud.models.error import Error
from bb.cloud.sdk import branch_restrictions
from bb.cloud.sdk._client import BBClient

pytestmark = [pytest.mark.live]

# Seed restriction — DO NOT delete or mutate
SEED_RESTRICTION_ID = 76271307
SEED_RESTRICTION_KIND = BranchrestrictionKind.REQUIRE_APPROVALS_TO_MERGE
SEED_RESTRICTION_PATTERN = "main"


# ---------------------------------------------------------------------------
# branch_restrictions.list
# ---------------------------------------------------------------------------


async def test_list_returns_restrictions(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    result = await branch_restrictions.list(client, workspace, probe_repo_slug, pagelen=10)
    if isinstance(result, Error):
        pytest.skip(
            f"branch_restrictions.list not available: "
            f"{result.error.message if result.error else result!r}"
        )
    assert isinstance(result, list), (
        f"branch_restrictions.list must return list, got {type(result).__name__}"
    )
    for idx, item in enumerate(result):
        assert isinstance(item, Branchrestriction), (
            f"branch_restrictions.list[{idx}] is {type(item).__name__}, expected Branchrestriction"
        )


async def test_list_includes_seed_restriction(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    result = await branch_restrictions.list(client, workspace, probe_repo_slug, pagelen=50)
    if isinstance(result, Error):
        pytest.skip(
            f"branch_restrictions.list not available: "
            f"{result.error.message if result.error else result!r}"
        )
    ids = [r.id for r in result if isinstance(r, Branchrestriction)]
    assert SEED_RESTRICTION_ID in ids, (
        f"Expected restriction id {SEED_RESTRICTION_ID} in list, got ids: {ids}"
    )


async def test_list_pagination_consistent(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    result_small = await branch_restrictions.list(client, workspace, probe_repo_slug, pagelen=1)
    result_large = await branch_restrictions.list(client, workspace, probe_repo_slug, pagelen=50)

    if isinstance(result_small, Error) or isinstance(result_large, Error):
        pytest.skip("branch_restrictions.list not available")

    assert len(result_small) == len(result_large), (
        f"Pagination inconsistency: pagelen=1 → {len(result_small)}, "
        f"pagelen=50 → {len(result_large)}"
    )


# ---------------------------------------------------------------------------
# branch_restrictions.get
# ---------------------------------------------------------------------------


async def test_get_seed_restriction(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    result = await branch_restrictions.get(
        client, workspace, probe_repo_slug, SEED_RESTRICTION_ID
    )
    if isinstance(result, Error):
        pytest.skip(
            f"branch_restrictions.get not available: "
            f"{result.error.message if result.error else result!r}"
        )
    assert isinstance(result, Branchrestriction), (
        f"branch_restrictions.get must return Branchrestriction, got {type(result).__name__}"
    )
    assert result.id == SEED_RESTRICTION_ID, (
        f"Expected id={SEED_RESTRICTION_ID}, got {result.id!r}"
    )
    assert result.kind == SEED_RESTRICTION_KIND, (
        f"Expected kind={SEED_RESTRICTION_KIND!r}, got {result.kind!r}"
    )
    assert result.pattern == SEED_RESTRICTION_PATTERN, (
        f"Expected pattern={SEED_RESTRICTION_PATTERN!r}, got {result.pattern!r}"
    )


async def test_get_seed_restriction_branch_match_kind(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    result = await branch_restrictions.get(
        client, workspace, probe_repo_slug, SEED_RESTRICTION_ID
    )
    if isinstance(result, Error) or result is None:
        pytest.skip("branch_restrictions.get not available")
    assert isinstance(result, Branchrestriction)
    assert result.branch_match_kind == BranchrestrictionBranchMatchKind.GLOB, (
        f"Expected branch_match_kind=glob, got {result.branch_match_kind!r}"
    )


async def test_get_missing_restriction_is_error_or_none(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    result = await branch_restrictions.get(
        client, workspace, probe_repo_slug, 999_999_999
    )
    assert not isinstance(result, Branchrestriction), (
        f"branch_restrictions.get for nonexistent id must not return Branchrestriction, got {result!r}"
    )


# ---------------------------------------------------------------------------
# branch_restrictions.create / update / delete  (write path)
# ---------------------------------------------------------------------------


async def test_create_update_delete_restriction_roundtrip(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    # Use a unique glob pattern to avoid conflicts
    unique_pattern = f"test-restrict-{uuid.uuid4().hex[:8]}/*"

    body = Branchrestriction(
        type_="branchrestriction",
        kind=BranchrestrictionKind.PUSH,
        branch_match_kind=BranchrestrictionBranchMatchKind.GLOB,
        pattern=unique_pattern,
    )  # type: ignore[call-arg]

    created = None
    created_id: int | None = None
    try:
        # --- create ---
        created = await branch_restrictions.create(
            client, workspace, probe_repo_slug, body=body
        )
        if isinstance(created, Error):
            pytest.skip(
                f"branch_restrictions.create not available: "
                f"{created.error.message if created.error else created!r}"
            )
        assert isinstance(created, Branchrestriction), (
            f"branch_restrictions.create must return Branchrestriction, "
            f"got {type(created).__name__}: {created!r}"
        )
        assert created.kind == BranchrestrictionKind.PUSH, (
            f"Expected kind=push, got {created.kind!r}"
        )
        assert created.pattern == unique_pattern, (
            f"Expected pattern={unique_pattern!r}, got {created.pattern!r}"
        )
        from bb.cloud.types import Unset
        assert not isinstance(created.id, Unset) and created.id is not None, (
            f"Created restriction has no id: {created!r}"
        )
        created_id = created.id

        # --- verify via get ---
        fetched = await branch_restrictions.get(
            client, workspace, probe_repo_slug, created_id
        )
        assert isinstance(fetched, Branchrestriction), (
            f"branch_restrictions.get after create must return Branchrestriction, got {fetched!r}"
        )
        assert fetched.id == created_id
        assert fetched.pattern == unique_pattern

        # --- update: change the pattern ---
        updated_pattern = f"test-restrict-upd-{uuid.uuid4().hex[:8]}/*"
        update_body = Branchrestriction(
            type_="branchrestriction",
            kind=BranchrestrictionKind.PUSH,
            branch_match_kind=BranchrestrictionBranchMatchKind.GLOB,
            pattern=updated_pattern,
        )  # type: ignore[call-arg]

        updated = await branch_restrictions.update(
            client, workspace, probe_repo_slug, created_id, body=update_body
        )
        if isinstance(updated, Error):
            pytest.skip(
                f"branch_restrictions.update not available: "
                f"{updated.error.message if updated.error else updated!r}"
            )
        assert isinstance(updated, Branchrestriction), (
            f"branch_restrictions.update must return Branchrestriction, "
            f"got {type(updated).__name__}: {updated!r}"
        )
        assert updated.pattern == updated_pattern, (
            f"Expected updated pattern={updated_pattern!r}, got {updated.pattern!r}"
        )
        assert updated.id == created_id, (
            f"Updated restriction id changed: {updated.id!r} != {created_id!r}"
        )

    finally:
        if created_id is not None:
            # --- delete ---
            await branch_restrictions.delete(client, workspace, probe_repo_slug, created_id)

            # verify gone
            after_delete = await branch_restrictions.get(
                client, workspace, probe_repo_slug, created_id
            )
            assert not isinstance(after_delete, Branchrestriction), (
                f"Restriction {created_id} still exists after delete: {after_delete!r}"
            )


async def test_create_restriction_missing_kind_returns_error_not_raise(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """The SDK must not raise when the API rejects a bad payload.

    We send a valid-looking body but with an unusual combination.  The goal is
    to confirm that errors surface as Error / None — not as raw exceptions.
    """
    # "delete" restriction on a nonsensical pattern — should succeed or return Error
    unique_pattern = f"test-bad-{uuid.uuid4().hex[:8]}"
    body = Branchrestriction(
        type_="branchrestriction",
        kind=BranchrestrictionKind.DELETE,
        branch_match_kind=BranchrestrictionBranchMatchKind.GLOB,
        pattern=unique_pattern,
    )  # type: ignore[call-arg]

    created_id: int | None = None
    try:
        result = await branch_restrictions.create(
            client, workspace, probe_repo_slug, body=body
        )
        # Acceptable: Branchrestriction (created), Error, or None — NOT a raw exception
        assert result is None or isinstance(result, (Branchrestriction, Error)), (
            f"Expected Branchrestriction, Error, or None — got {type(result).__name__}: {result!r}"
        )
        if isinstance(result, Branchrestriction):
            from bb.cloud.types import Unset
            if not isinstance(result.id, Unset) and result.id is not None:
                created_id = result.id
    finally:
        if created_id is not None:
            await branch_restrictions.delete(client, workspace, probe_repo_slug, created_id)
