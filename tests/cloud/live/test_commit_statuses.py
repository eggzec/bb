"""Live tests for ``bb.cloud.sdk.commit_statuses``.

Seed data (never mutate):
- workspace:   beaverish
- repo:        bb-probe
- commit hash: 84952fad87fb39e3c6d61811a93769378dd4fad7
- status key:  bb-probe-ci (state: SUCCESSFUL)

Cleanup note: the Bitbucket API does NOT expose DELETE for commit statuses.
Throwaway statuses are left in state STOPPED after the test runs.

Spec / generator risk:
- POST /commit/statuses/build → spec says 201; if the live API returns 200 the
  generated _parse_response ignores it and asyncio() returns None → SDK returns None.
  Tests explicitly document which HTTP response was observed.
"""

from __future__ import annotations

import uuid

import pytest

from bb.cloud.models.commitstatus import Commitstatus
from bb.cloud.models.commitstatus_state import CommitstatusState
from bb.cloud.models.error import Error
from bb.cloud.sdk import commit_statuses
from bb.cloud.sdk._client import BBClient

pytestmark = pytest.mark.live

# ---------------------------------------------------------------------------
# Seed constants
# ---------------------------------------------------------------------------
SEED_COMMIT = "84952fad87fb39e3c6d61811a93769378dd4fad7"
SEED_REPO = "bb-probe"
SEED_STATUS_KEY = "bb-probe-ci"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _err(result: object) -> str:
    if isinstance(result, Error):
        return result.error.message if getattr(result, "error", None) else repr(result)
    return repr(result)


def _make_status(key: str, state: CommitstatusState) -> Commitstatus:
    return Commitstatus(
        type_="build",
        key=key,
        state=state,
        url="https://example.com/build",
        name=f"bb-sdk-live-test ({key})",
        description="Throwaway status created by bb SDK live tests",
    )


# ---------------------------------------------------------------------------
# TC-CS-001 / TC-CS-002: list
# ---------------------------------------------------------------------------


async def test_list_returns_statuses(
    client: BBClient,
    workspace: str,
) -> None:
    """TC-CS-001/TC-CS-002: list returns a list of Commitstatus for the seed commit."""
    result = await commit_statuses.list(
        client, workspace, SEED_REPO, SEED_COMMIT, pagelen=25
    )
    assert not isinstance(result, Error), (
        f"commit_statuses.list errored: {_err(result)}"
    )
    assert isinstance(result, list), (
        f"commit_statuses.list must return list, got {type(result).__name__}"
    )
    assert result, (
        f"commit_statuses.list returned empty list for commit {SEED_COMMIT!r} "
        f"— expected at least {SEED_STATUS_KEY!r}"
    )
    for idx, status in enumerate(result):
        assert isinstance(status, Commitstatus), (
            f"commit_statuses.list[{idx}] is {type(status).__name__}, expected Commitstatus"
        )

    keys = {s.key for s in result}
    assert SEED_STATUS_KEY in keys, (
        f"Expected seed key {SEED_STATUS_KEY!r} in commit statuses, got: {keys!r}"
    )


# ---------------------------------------------------------------------------
# TC-CS-003 / TC-CS-004: get
# ---------------------------------------------------------------------------


async def test_get_seed_status(
    client: BBClient,
    workspace: str,
) -> None:
    """TC-CS-003: get the seeded status by key and verify state=SUCCESSFUL."""
    result = await commit_statuses.get(
        client, workspace, SEED_REPO, SEED_COMMIT, SEED_STATUS_KEY
    )
    assert not isinstance(result, Error), (
        f"commit_statuses.get({SEED_STATUS_KEY!r}) errored: {_err(result)}"
    )
    assert isinstance(result, Commitstatus), (
        f"commit_statuses.get must return Commitstatus, got {type(result).__name__}"
    )
    assert result.key == SEED_STATUS_KEY, (
        f"key mismatch: got {result.key!r}, expected {SEED_STATUS_KEY!r}"
    )
    assert result.state == CommitstatusState.SUCCESSFUL, (
        f"state mismatch: got {result.state!r}, expected SUCCESSFUL"
    )


async def test_get_missing_status_is_error_or_none(
    client: BBClient,
    workspace: str,
    probe_repo_slug: str,
    probe_commit_hash: str,
) -> None:
    """TC-CS-004: get with a nonexistent key returns Error or None, does not raise."""
    result = await commit_statuses.get(
        client, workspace, probe_repo_slug, probe_commit_hash, "key-that-does-not-exist-xyz"
    )
    assert not isinstance(result, Commitstatus), (
        f"commit_statuses.get for missing key must not return Commitstatus, got {result!r}"
    )


# ---------------------------------------------------------------------------
# TC-CS-005 / TC-CS-006: create
# ---------------------------------------------------------------------------


async def test_create_throwaway_status(
    client: BBClient,
    workspace: str,
) -> None:
    """TC-CS-005: create a new commit status; cleanup via update to STOPPED.

    SPEC NOTE: POST /commit/statuses/build is documented as returning 201.
    The generated _parse_response only handles 201. If the live API returns 200
    instead, asyncio() returns None and the SDK returns None here (not a
    Commitstatus). This test will catch that discrepancy.
    """
    throwaway_key = f"bb-test-status-{uuid.uuid4().hex[:8]}"
    result = None
    try:
        result = await commit_statuses.create(
            client,
            workspace,
            SEED_REPO,
            SEED_COMMIT,
            body=_make_status(throwaway_key, CommitstatusState.INPROGRESS),
        )
        assert result is not None, (
            f"commit_statuses.create returned None — possible HTTP 200 vs 201 mismatch. "
            f"The generated parser only accepts 201; if the live API returned 200 "
            f"the response was silently discarded. See BUG-COMMITS-001."
        )
        assert not isinstance(result, Error), (
            f"commit_statuses.create errored: {_err(result)}"
        )
        assert isinstance(result, Commitstatus), (
            f"commit_statuses.create must return Commitstatus, got {type(result).__name__}"
        )
        assert result.key == throwaway_key, (
            f"key mismatch: got {result.key!r}, expected {throwaway_key!r}"
        )
        assert result.state == CommitstatusState.INPROGRESS, (
            f"state mismatch: got {result.state!r}, expected INPROGRESS"
        )
    finally:
        # No DELETE on commit statuses — update to STOPPED to mark it benign.
        if throwaway_key:
            await commit_statuses.update(
                client,
                workspace,
                SEED_REPO,
                SEED_COMMIT,
                throwaway_key,
                body=_make_status(throwaway_key, CommitstatusState.STOPPED),
            )


async def test_create_idempotent_same_key(
    client: BBClient,
    workspace: str,
) -> None:
    """TC-CS-006: POSTing the same key twice is idempotent (BB upserts on key)."""
    throwaway_key = f"bb-test-status-{uuid.uuid4().hex[:8]}"
    try:
        first = await commit_statuses.create(
            client,
            workspace,
            SEED_REPO,
            SEED_COMMIT,
            body=_make_status(throwaway_key, CommitstatusState.INPROGRESS),
        )
        second = await commit_statuses.create(
            client,
            workspace,
            SEED_REPO,
            SEED_COMMIT,
            body=_make_status(throwaway_key, CommitstatusState.INPROGRESS),
        )
        # Both should succeed (not raise, not return Error).
        # If the API returns 200 instead of 201, result will be None (see TC-CS-005 note).
        for attempt, res in enumerate([first, second], start=1):
            if res is None:
                pytest.xfail(
                    f"Attempt {attempt}: commit_statuses.create returned None — "
                    f"likely HTTP 200 vs expected 201. See BUG-COMMITS-001."
                )
            assert not isinstance(res, Error), (
                f"Attempt {attempt}: commit_statuses.create errored: {_err(res)}"
            )
            assert isinstance(res, Commitstatus), (
                f"Attempt {attempt}: expected Commitstatus, got {type(res).__name__}"
            )
    finally:
        await commit_statuses.update(
            client,
            workspace,
            SEED_REPO,
            SEED_COMMIT,
            throwaway_key,
            body=_make_status(throwaway_key, CommitstatusState.STOPPED),
        )


# ---------------------------------------------------------------------------
# TC-CS-007: update
# ---------------------------------------------------------------------------


async def test_update_throwaway_status(
    client: BBClient,
    workspace: str,
) -> None:
    """TC-CS-007: create a status then update its state from INPROGRESS to FAILED."""
    throwaway_key = f"bb-test-status-{uuid.uuid4().hex[:8]}"
    try:
        # Create first.
        create_result = await commit_statuses.create(
            client,
            workspace,
            SEED_REPO,
            SEED_COMMIT,
            body=_make_status(throwaway_key, CommitstatusState.INPROGRESS),
        )
        if create_result is None:
            pytest.xfail(
                "commit_statuses.create returned None — likely HTTP 200 vs expected 201. "
                "Cannot test update without a successfully created status. See BUG-COMMITS-001."
            )

        # Update to FAILED.
        updated = await commit_statuses.update(
            client,
            workspace,
            SEED_REPO,
            SEED_COMMIT,
            throwaway_key,
            body=_make_status(throwaway_key, CommitstatusState.FAILED),
        )
        assert not isinstance(updated, Error), (
            f"commit_statuses.update errored: {_err(updated)}"
        )
        assert isinstance(updated, Commitstatus), (
            f"commit_statuses.update must return Commitstatus, got {type(updated).__name__}"
        )
        assert updated.state == CommitstatusState.FAILED, (
            f"state mismatch after update: got {updated.state!r}, expected FAILED"
        )
    finally:
        # Mark as STOPPED regardless.
        await commit_statuses.update(
            client,
            workspace,
            SEED_REPO,
            SEED_COMMIT,
            throwaway_key,
            body=_make_status(throwaway_key, CommitstatusState.STOPPED),
        )
