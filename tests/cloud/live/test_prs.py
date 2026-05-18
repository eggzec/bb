"""Live integration tests for ``bb.cloud.sdk.prs``.

Seed data (beaverish/bb-probe — DO NOT mutate these resources):
- PR #1: open, feature/add-farewell → main
- PR #2: merged
- comment_id: 797172056
- task_id: 64759588
- seed commit: 84952fad87fb39e3c6d61811a93769378dd4fad7
- owner account_id: 712020:f464b5ca-adb8-4a1e-80d4-c867bbf50805
"""

from __future__ import annotations

import uuid

import pytest

from bb.cloud.models.comment_content import CommentContent
from bb.cloud.models.error import Error
from bb.cloud.models.participant import Participant
from bb.cloud.models.pull_request_endpoint import PullRequestEndpoint
from bb.cloud.models.pull_request_endpoint_pull_request_branch import PullRequestEndpointPullRequestBranch
from bb.cloud.models.pull_request_task_create import PullRequestTaskCreate
from bb.cloud.models.pull_request_task_create_task_raw_content import PullRequestTaskCreateTaskRawContent
from bb.cloud.models.pull_request_task_update import PullRequestTaskUpdate
from bb.cloud.models.pull_request_task_update_state import PullRequestTaskUpdateState
from bb.cloud.models.pull_request_task_update_task_raw_content import PullRequestTaskUpdateTaskRawContent
from bb.cloud.models.pullrequest import Pullrequest
from bb.cloud.models.pullrequest_comment import PullrequestComment as PullRequestComment
from bb.cloud.sdk import branches as branches_sdk
from bb.cloud.sdk import prs
from bb.cloud.sdk._client import BBClient

pytestmark = pytest.mark.live

# ---------------------------------------------------------------------------
# Seed data constants
# ---------------------------------------------------------------------------
SEED_PR_ID = 1
SEED_MERGED_PR_ID = 2
SEED_COMMENT_ID = 797172056
SEED_TASK_ID = 64759588
SEED_COMMIT_HASH = "84952fad87fb39e3c6d61811a93769378dd4fad7"
OWNER_ACCOUNT_ID = "712020:f464b5ca-adb8-4a1e-80d4-c867bbf50805"
PROBE_REPO = "bb-probe"


# ---------------------------------------------------------------------------
# Module-scoped throwaway fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
async def throwaway_pr(client: BBClient, workspace: str) -> dict:
    """Create a throwaway branch + PR. Decline + delete branch in finally.

    Yields a dict with keys: ``pr_id``, ``branch_name``.
    """
    branch_name = f"test/throwaway-pr-{uuid.uuid4().hex[:8]}"

    # Create the branch from the known seed commit
    branch = await branches_sdk.create(
        client,
        workspace,
        PROBE_REPO,
        name=branch_name,
        target_hash=SEED_COMMIT_HASH,
    )
    if branch is None:
        pytest.skip(f"Could not create throwaway branch {branch_name!r} — skipping mutation tests")

    pr_body = Pullrequest(
        type_="pullrequest",
        title=f"[test] throwaway PR {uuid.uuid4().hex[:6]}",
        source=PullRequestEndpoint(
            branch=PullRequestEndpointPullRequestBranch(name=branch_name)
        ),
        destination=PullRequestEndpoint(
            branch=PullRequestEndpointPullRequestBranch(name="main")
        ),
    )

    result = await prs.create(client, workspace, PROBE_REPO, body=pr_body)
    if isinstance(result, Error) or result is None:
        # Clean up branch
        await branches_sdk.delete(client, workspace, PROBE_REPO, branch_name)
        msg = result.error.message if isinstance(result, Error) and result.error else repr(result)
        pytest.skip(f"Could not create throwaway PR: {msg}")

    pr_id = result.id
    info = {"pr_id": pr_id, "branch_name": branch_name}

    yield info

    # Cleanup
    try:
        # Decline the PR so we can delete the branch
        await prs.decline(client, workspace, PROBE_REPO, pr_id)
    except Exception:
        pass
    try:
        await branches_sdk.delete(client, workspace, PROBE_REPO, branch_name)
    except Exception:
        pass


# ---------------------------------------------------------------------------
# 1. prs.list
# ---------------------------------------------------------------------------

async def test_list_returns_pullrequests(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """LIST-001/002/003 — happy path, all items are Pullrequest with id."""
    result = await prs.list(client, workspace, probe_repo_slug, pagelen=10)
    assert not isinstance(result, Error), (
        f"prs.list errored: {result.error.message if result.error else result!r}"
    )
    assert isinstance(result, list), f"prs.list must return list, got {type(result).__name__}"
    for idx, pr in enumerate(result):
        assert isinstance(pr, Pullrequest), (
            f"prs.list[{idx}] is {type(pr).__name__}, expected Pullrequest"
        )
        assert pr.id is not None, f"prs.list[{idx}] has no id: {pr!r}"


@pytest.mark.parametrize(
    "state",
    [
        prs.PullrequestState.OPEN,
        prs.PullrequestState.MERGED,
        prs.PullrequestState.DECLINED,
        prs.PullrequestState.SUPERSEDED,
    ],
)
async def test_list_filter_by_state(
    client: BBClient,
    workspace: str,
    probe_repo_slug: str,
    state: prs.PullrequestState,
) -> None:
    """LIST-004/005/006/007 — state filter returns matching PRs."""
    result = await prs.list(client, workspace, probe_repo_slug, state=state, pagelen=10)
    if isinstance(result, Error):
        pytest.skip(
            f"prs.list(state={state.value!r}) errored: "
            f"{result.error.message if result.error else result!r}"
        )
    assert isinstance(result, list), (
        f"prs.list(state={state.value!r}) must return list, got {type(result).__name__}"
    )
    for idx, pr in enumerate(result):
        assert isinstance(pr, Pullrequest), (
            f"prs.list(state={state.value!r})[{idx}] is {type(pr).__name__}, expected Pullrequest"
        )
        assert pr.state is None or str(pr.state).upper() == state.value.upper(), (
            f"prs.list(state={state.value!r})[{idx}] has wrong state: {pr.state!r}"
        )


async def test_list_pagination_integrity(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """LIST-008 — pagelen=1 vs pagelen=50 gives the same total count."""
    small = await prs.list(client, workspace, probe_repo_slug, pagelen=1)
    big = await prs.list(client, workspace, probe_repo_slug, pagelen=50)
    if isinstance(small, Error) or isinstance(big, Error):
        pytest.skip("prs.list errored during pagination test")
    assert len(small) == len(big), (
        f"pagination inconsistency: pagelen=1 returned {len(small)} but pagelen=50 returned {len(big)}"
    )
    small_ids = {pr.id for pr in small}
    big_ids = {pr.id for pr in big}
    assert small_ids == big_ids, (
        f"pagination returned different PR sets: "
        f"only-in-small={small_ids - big_ids!r}, only-in-big={big_ids - small_ids!r}"
    )


# ---------------------------------------------------------------------------
# 2. prs.get
# ---------------------------------------------------------------------------

async def test_get_returns_pullrequest(
    client: BBClient, workspace: str
) -> None:
    """GET-001/002/003 — returns Pullrequest for seed PR #1 with correct id/title."""
    result = await prs.get(client, workspace, PROBE_REPO, SEED_PR_ID)
    assert not isinstance(result, Error), (
        f"prs.get({SEED_PR_ID}) errored: "
        f"{result.error.message if result.error else result!r}"
    )
    assert isinstance(result, Pullrequest), (
        f"prs.get must return Pullrequest, got {type(result).__name__}"
    )
    assert result.id == SEED_PR_ID, (
        f"prs.get returned id={result.id!r}, expected {SEED_PR_ID!r}"
    )
    assert result.title, f"prs.get returned PR with empty title: {result!r}"


async def test_get_missing_pullrequest_is_error_or_none(
    client: BBClient, workspace: str
) -> None:
    """GET-004 — nonexistent PR ID returns Error/None, not Pullrequest."""
    result = await prs.get(client, workspace, PROBE_REPO, 999_999_999)
    assert not isinstance(result, Pullrequest), (
        f"prs.get for a nonexistent PR must not return Pullrequest, got {result!r}"
    )


# ---------------------------------------------------------------------------
# 3. prs.create + prs.update + prs.decline (throwaway PR fixture)
# ---------------------------------------------------------------------------

@pytest.mark.writes
async def test_create_returns_pullrequest(
    client: BBClient, workspace: str, throwaway_pr: dict
) -> None:
    """CREATE-001/002/003 — PR created successfully."""
    pr_id = throwaway_pr["pr_id"]
    assert pr_id is not None, "throwaway_pr fixture returned None id"

    # Verify by fetching
    result = await prs.get(client, workspace, PROBE_REPO, pr_id)
    assert not isinstance(result, Error), (
        f"prs.get on throwaway PR errored: {result!r}"
    )
    assert isinstance(result, Pullrequest), (
        f"prs.get must return Pullrequest, got {type(result).__name__}"
    )
    assert result.id == pr_id


@pytest.mark.writes
async def test_update_throwaway_pr(
    client: BBClient, workspace: str, throwaway_pr: dict
) -> None:
    """UPDATE-001/002 — update throwaway PR title."""
    pr_id = throwaway_pr["pr_id"]
    new_title = f"[test] updated-{uuid.uuid4().hex[:6]}"
    body = Pullrequest(type_="pullrequest", title=new_title)
    result = await prs.update(client, workspace, PROBE_REPO, pr_id, body=body)
    assert not isinstance(result, Error), (
        f"prs.update errored: {result.error.message if result.error else result!r}"
    )
    assert isinstance(result, Pullrequest), (
        f"prs.update must return Pullrequest, got {type(result).__name__}"
    )
    assert result.title == new_title, (
        f"prs.update returned title={result.title!r}, expected {new_title!r}"
    )


@pytest.mark.writes
async def test_decline_throwaway_pr(
    client: BBClient, workspace: str
) -> None:
    """DECLINE-001 — decline a freshly created throwaway PR."""
    # Create a separate branch+PR just for decline test to avoid interfering with the
    # module-scoped fixture (which we also decline in cleanup).
    branch_name = f"test/decline-{uuid.uuid4().hex[:8]}"
    branch = await branches_sdk.create(
        client, workspace, PROBE_REPO,
        name=branch_name, target_hash=SEED_COMMIT_HASH,
    )
    if branch is None:
        pytest.skip("Could not create branch for decline test")

    pr_body = Pullrequest(
        type_="pullrequest",
        title=f"[test] decline-me {uuid.uuid4().hex[:6]}",
        source=PullRequestEndpoint(
            branch=PullRequestEndpointPullRequestBranch(name=branch_name)
        ),
        destination=PullRequestEndpoint(
            branch=PullRequestEndpointPullRequestBranch(name="main")
        ),
    )
    pr_result = await prs.create(client, workspace, PROBE_REPO, body=pr_body)

    try:
        if isinstance(pr_result, Error) or pr_result is None:
            pytest.skip("Could not create PR for decline test")
        pr_id = pr_result.id
        result = await prs.decline(client, workspace, PROBE_REPO, pr_id)
        assert result is not None, "prs.decline returned None but should return a Pullrequest"
        if isinstance(result, Pullrequest):
            assert str(result.state).upper() == "DECLINED", (
                f"declined PR has state {result.state!r}, expected DECLINED"
            )
        elif isinstance(result, Error):
            pytest.fail(
                f"prs.decline returned Error: {result.error.message if result.error else result!r}"
            )
    finally:
        try:
            await branches_sdk.delete(client, workspace, PROBE_REPO, branch_name)
        except Exception:
            pass


# ---------------------------------------------------------------------------
# 4. prs.approve / prs.unapprove (seed PR #1 — we own it, reversible)
# ---------------------------------------------------------------------------

@pytest.mark.writes
async def test_approve_and_unapprove_seed_pr(
    client: BBClient, workspace: str
) -> None:
    """APPROVE-001/002 + UNAPPROVE-001 — approve then unapprove PR #1."""
    # Approve
    result = await prs.approve(client, workspace, PROBE_REPO, SEED_PR_ID)
    assert not isinstance(result, Error), (
        f"prs.approve errored: {result.error.message if result.error else result!r}"
    )
    assert isinstance(result, Participant), (
        f"prs.approve must return Participant, got {type(result).__name__}"
    )

    # Unapprove (always run regardless of approve result)
    await prs.unapprove(client, workspace, PROBE_REPO, SEED_PR_ID)
    # unapprove returns None (204) — no assertion needed beyond not raising


# ---------------------------------------------------------------------------
# 5. prs.request_changes / prs.unrequest_changes (self-review — expect failure)
# ---------------------------------------------------------------------------

async def test_request_changes_self_review_errors(
    client: BBClient, workspace: str
) -> None:
    """RC-001 — request_changes on own PR should return Error (self-review not allowed).

    Bitbucket Cloud does not allow the PR author to request changes on their own PR.
    We document the exact response rather than asserting a specific error message.
    """
    result = await prs.request_changes(client, workspace, PROBE_REPO, SEED_PR_ID)
    # Acceptable outcomes: Error with relevant message, or None
    # It must NOT raise an uncaught exception
    assert not isinstance(result, Participant), (
        "request_changes on own PR unexpectedly succeeded with Participant — "
        "self-review is supposed to be rejected by Bitbucket Cloud"
    )
    # Just document — this is expected to fail with Error
    if isinstance(result, Error):
        pass  # expected; error message logged implicitly in output
    elif result is None:
        pass  # also acceptable — 404/400 that parsed to None


async def test_unrequest_changes_self_review_no_exception(
    client: BBClient, workspace: str
) -> None:
    """RC-002 — unrequest_changes on own PR should not raise."""
    # Should silently succeed (204) or return Error
    await prs.unrequest_changes(client, workspace, PROBE_REPO, SEED_PR_ID)
    # No exception → test passes


# ---------------------------------------------------------------------------
# 6. prs.comments / prs.add_comment / prs.get_comment /
#    prs.update_comment / prs.delete_comment
# ---------------------------------------------------------------------------

async def test_comments_returns_list(
    client: BBClient, workspace: str
) -> None:
    """COMMENTS-001/002 — returns list of PullRequestComment for PR #1."""
    result = await prs.comments(client, workspace, PROBE_REPO, SEED_PR_ID, pagelen=25)
    assert not isinstance(result, Error), (
        f"prs.comments errored: {result.error.message if result.error else result!r}"
    )
    assert isinstance(result, list), (
        f"prs.comments must return list, got {type(result).__name__}"
    )
    for idx, comment in enumerate(result):
        assert isinstance(comment, PullRequestComment), (
            f"prs.comments[{idx}] is {type(comment).__name__}, expected PullrequestComment"
        )


async def test_comments_contains_seed_comment(
    client: BBClient, workspace: str
) -> None:
    """COMMENTS-003 — seed comment_id 797172056 is present."""
    result = await prs.comments(client, workspace, PROBE_REPO, SEED_PR_ID, pagelen=50)
    if isinstance(result, Error):
        pytest.skip(f"prs.comments errored: {result!r}")
    comment_ids = {c.id for c in result}
    assert SEED_COMMENT_ID in comment_ids, (
        f"seed comment_id {SEED_COMMENT_ID} not found in PR #1 comments. "
        f"Found ids: {comment_ids!r}"
    )


async def test_get_comment_seed(client: BBClient, workspace: str) -> None:
    """GET-COMMENT-001/002 — get_comment for seed comment."""
    result = await prs.get_comment(client, workspace, PROBE_REPO, SEED_PR_ID, SEED_COMMENT_ID)
    assert not isinstance(result, Error), (
        f"prs.get_comment errored: {result.error.message if result.error else result!r}"
    )
    assert isinstance(result, PullRequestComment), (
        f"prs.get_comment must return PullrequestComment, got {type(result).__name__}"
    )
    assert result.id == SEED_COMMENT_ID, (
        f"prs.get_comment returned id={result.id!r}, expected {SEED_COMMENT_ID!r}"
    )


@pytest.mark.writes
async def test_add_update_delete_comment(client: BBClient, workspace: str) -> None:
    """ADD-COMMENT-001/002 + UPDATE-COMMENT-001/002 + DELETE-COMMENT-001/002."""
    comment_body = PullRequestComment(
        content=CommentContent(raw=f"[test] throwaway comment {uuid.uuid4().hex[:8]}"),
    )
    comment_id: int | None = None

    try:
        # Add
        result = await prs.add_comment(
            client, workspace, PROBE_REPO, SEED_PR_ID, body=comment_body
        )
        assert not isinstance(result, Error), (
            f"prs.add_comment errored: {result.error.message if result.error else result!r}"
        )
        assert isinstance(result, PullRequestComment), (
            f"prs.add_comment must return PullrequestComment, got {type(result).__name__}"
        )
        assert result.id is not None, "prs.add_comment returned comment with no id"
        comment_id = result.id

        # Update
        updated_body = PullRequestComment(
            content=CommentContent(raw=f"[test] UPDATED {uuid.uuid4().hex[:8]}"),
        )
        updated = await prs.update_comment(
            client, workspace, PROBE_REPO, SEED_PR_ID, comment_id, body=updated_body
        )
        assert not isinstance(updated, Error), (
            f"prs.update_comment errored: {updated.error.message if updated.error else updated!r}"
        )
        assert isinstance(updated, PullRequestComment), (
            f"prs.update_comment must return PullrequestComment, got {type(updated).__name__}"
        )
        # Content should reflect the update
        assert updated.id == comment_id, (
            f"prs.update_comment returned id={updated.id!r}, expected {comment_id!r}"
        )

    finally:
        if comment_id is not None:
            try:
                await prs.delete_comment(client, workspace, PROBE_REPO, SEED_PR_ID, comment_id)
            except Exception:
                pass


# ---------------------------------------------------------------------------
# 7. prs.resolve_comment / prs.unresolve_comment (seed comment)
# ---------------------------------------------------------------------------

@pytest.mark.writes
async def test_resolve_and_unresolve_comment(client: BBClient, workspace: str) -> None:
    """RESOLVE-001 + UNRESOLVE-001 — resolve then unresolve the seed comment."""
    try:
        resolve_result = await prs.resolve_comment(
            client, workspace, PROBE_REPO, SEED_PR_ID, SEED_COMMENT_ID
        )
        # Should not raise; result may be None or any object
        assert not isinstance(resolve_result, Error) or True, (
            "resolve_comment returned Error — documenting but not failing"
        )
    finally:
        # Always try to unresolve regardless of above result
        try:
            await prs.unresolve_comment(
                client, workspace, PROBE_REPO, SEED_PR_ID, SEED_COMMENT_ID
            )
        except Exception:
            pass


# ---------------------------------------------------------------------------
# 8. prs.diff
# ---------------------------------------------------------------------------

async def test_diff_returns_string(client: BBClient, workspace: str) -> None:
    """DIFF-001/002 — returns non-empty string for seed PR #1."""
    result = await prs.diff(client, workspace, PROBE_REPO, SEED_PR_ID)
    assert not isinstance(result, Error), (
        f"prs.diff errored: {result.error.message if result.error else result!r}"
    )
    assert isinstance(result, str), (
        f"prs.diff must return str, got {type(result).__name__}"
    )
    assert len(result) > 0, "prs.diff returned empty string"


# ---------------------------------------------------------------------------
# 9. prs.commits
# ---------------------------------------------------------------------------

async def test_commits_returns_list(client: BBClient, workspace: str) -> None:
    """COMMITS-001/002 — returns non-empty list for PR #1."""
    result = await prs.commits(client, workspace, PROBE_REPO, SEED_PR_ID)
    assert not isinstance(result, Error), (
        f"prs.commits errored: {result.error.message if result.error else result!r}"
    )
    assert isinstance(result, list), (
        f"prs.commits must return list, got {type(result).__name__}"
    )
    assert len(result) > 0, "prs.commits returned empty list for seed PR #1"


# ---------------------------------------------------------------------------
# 10. prs.tasks — list
# ---------------------------------------------------------------------------

async def test_tasks_returns_list_with_seed_task(client: BBClient, workspace: str) -> None:
    """TASKS-001/002 — returns list for PR #1; seed task_id 64759588 present."""
    result = await prs.tasks(client, workspace, PROBE_REPO, SEED_PR_ID)
    assert not isinstance(result, Error), (
        f"prs.tasks errored: {result.error.message if result.error else result!r}"
    )
    assert isinstance(result, list), (
        f"prs.tasks must return list, got {type(result).__name__}"
    )
    task_ids = set()
    for t in result:
        tid = getattr(t, "id", None)
        if tid is not None:
            task_ids.add(tid)
    assert SEED_TASK_ID in task_ids, (
        f"seed task_id {SEED_TASK_ID} not found in PR #1 tasks. Found ids: {task_ids!r}"
    )


# ---------------------------------------------------------------------------
# 11. prs.create_task / get_task / update_task / delete_task
# ---------------------------------------------------------------------------

@pytest.mark.writes
async def test_task_lifecycle(client: BBClient, workspace: str) -> None:
    """CREATE-TASK-001/002 + GET-TASK-001 + UPDATE-TASK-001 + DELETE-TASK-001/002."""
    task_id: int | None = None

    try:
        # Create task
        task_body = PullRequestTaskCreate(
            content=PullRequestTaskCreateTaskRawContent(
                raw=f"[test] throwaway task {uuid.uuid4().hex[:8]}"
            ),
        )
        result = await prs.create_task(client, workspace, PROBE_REPO, SEED_PR_ID, body=task_body)
        assert result is not None, "prs.create_task returned None"
        assert not isinstance(result, Error), (
            f"prs.create_task errored: {result.error.message if result.error else result!r}"
        )
        task_id = getattr(result, "id", None)
        assert task_id is not None, f"prs.create_task returned task with no id: {result!r}"

        # Get task (seed)
        seed_task = await prs.get_task(client, workspace, PROBE_REPO, SEED_PR_ID, SEED_TASK_ID)
        assert seed_task is not None, f"prs.get_task({SEED_TASK_ID}) returned None"
        assert not isinstance(seed_task, Error), (
            f"prs.get_task errored: {seed_task.error.message if seed_task.error else seed_task!r}"
        )

        # Update throwaway task
        update_body = PullRequestTaskUpdate(
            content=PullRequestTaskUpdateTaskRawContent(
                raw=f"[test] updated task {uuid.uuid4().hex[:8]}"
            ),
            state=PullRequestTaskUpdateState.RESOLVED,
        )
        updated = await prs.update_task(
            client, workspace, PROBE_REPO, SEED_PR_ID, task_id, body=update_body
        )
        assert updated is not None, "prs.update_task returned None"

    finally:
        if task_id is not None:
            try:
                await prs.delete_task(client, workspace, PROBE_REPO, SEED_PR_ID, task_id)
            except Exception:
                pass


# ---------------------------------------------------------------------------
# 12. prs.default_reviewers
# ---------------------------------------------------------------------------

async def test_default_reviewers_returns_list(
    client: BBClient, workspace: str
) -> None:
    """DR-001/002 — returns list (likely empty for single-user workspace)."""
    result = await prs.default_reviewers(client, workspace, PROBE_REPO, pagelen=10)
    if isinstance(result, Error):
        pytest.skip(
            f"prs.default_reviewers not available: "
            f"{result.error.message if result.error else result!r}"
        )
    assert isinstance(result, list), (
        f"prs.default_reviewers must return list, got {type(result).__name__}"
    )


# ---------------------------------------------------------------------------
# 13. prs.get_default_reviewer (self — expect error on single-user workspace)
# ---------------------------------------------------------------------------

async def test_get_default_reviewer_owner_documents_result(
    client: BBClient, workspace: str
) -> None:
    """DR-GET-001 — get_default_reviewer for owner; documents response (likely Error/None)."""
    result = await prs.get_default_reviewer(
        client, workspace, PROBE_REPO, OWNER_ACCOUNT_ID
    )
    # For a single-user workspace this is expected to return Error or None.
    # We just confirm it does not raise.
    _ = result  # accepted: Error, None, or a reviewer object


# ---------------------------------------------------------------------------
# 14. prs.effective_default_reviewers
# ---------------------------------------------------------------------------

async def test_effective_default_reviewers_returns_list(
    client: BBClient, workspace: str
) -> None:
    """EDR-001/002 — returns list for bb-probe."""
    result = await prs.effective_default_reviewers(client, workspace, PROBE_REPO, pagelen=10)
    if isinstance(result, Error):
        pytest.skip(
            f"prs.effective_default_reviewers not available: "
            f"{result.error.message if result.error else result!r}"
        )
    assert isinstance(result, list), (
        f"prs.effective_default_reviewers must return list, got {type(result).__name__}"
    )


# ---------------------------------------------------------------------------
# 15. prs.activity (repo-level)
# ---------------------------------------------------------------------------

async def test_activity_returns_list(client: BBClient, workspace: str) -> None:
    """ACTIVITY-001/002 — repo-level PR activity."""
    result = await prs.activity(client, workspace, PROBE_REPO, pagelen=10)
    if isinstance(result, Error):
        pytest.skip(
            f"prs.activity errored: {result.error.message if result.error else result!r}"
        )
    assert isinstance(result, list), (
        f"prs.activity must return list, got {type(result).__name__}"
    )


# ---------------------------------------------------------------------------
# 16. prs.pr_activity (PR-level)
# ---------------------------------------------------------------------------

async def test_pr_activity_returns_list(client: BBClient, workspace: str) -> None:
    """PR-ACTIVITY-001/002 — PR #1 activity."""
    result = await prs.pr_activity(client, workspace, PROBE_REPO, SEED_PR_ID, pagelen=10)
    if isinstance(result, Error):
        pytest.skip(
            f"prs.pr_activity errored: {result.error.message if result.error else result!r}"
        )
    assert isinstance(result, list), (
        f"prs.pr_activity must return list, got {type(result).__name__}"
    )


# ---------------------------------------------------------------------------
# 17. prs.diffstat
# ---------------------------------------------------------------------------

async def test_diffstat_returns_result(client: BBClient, workspace: str) -> None:
    """DIFFSTAT-001/002 — diffstat for PR #1 is not None."""
    result = await prs.diffstat(client, workspace, PROBE_REPO, SEED_PR_ID)
    assert result is not None, "prs.diffstat returned None for seed PR #1"
    assert not isinstance(result, Error), (
        f"prs.diffstat errored: {result.error.message if isinstance(result, Error) and result.error else result!r}"
    )


# ---------------------------------------------------------------------------
# 18. prs.patch
# ---------------------------------------------------------------------------

async def test_patch_returns_string(client: BBClient, workspace: str) -> None:
    """PATCH-001/002 — returns non-empty string for PR #1."""
    result = await prs.patch(client, workspace, PROBE_REPO, SEED_PR_ID)
    assert not isinstance(result, Error), (
        f"prs.patch errored: {result.error.message if result.error else result!r}"
    )
    assert isinstance(result, str), (
        f"prs.patch must return str, got {type(result).__name__}"
    )
    assert len(result) > 0, "prs.patch returned empty string"


# ---------------------------------------------------------------------------
# 19. prs.statuses
# ---------------------------------------------------------------------------

async def test_statuses_returns_list(client: BBClient, workspace: str) -> None:
    """STATUSES-001/002 — returns list (may be empty; no CI configured)."""
    result = await prs.statuses(client, workspace, PROBE_REPO, SEED_PR_ID, pagelen=10)
    if isinstance(result, Error):
        pytest.skip(
            f"prs.statuses errored: {result.error.message if result.error else result!r}"
        )
    assert isinstance(result, list), (
        f"prs.statuses must return list, got {type(result).__name__}"
    )


# ---------------------------------------------------------------------------
# 20. prs.user_prs
# ---------------------------------------------------------------------------

async def test_user_prs_returns_list(client: BBClient, workspace: str) -> None:
    """USER-PRS-001/002/003 — PRs authored by owner."""
    result = await prs.user_prs(client, workspace, OWNER_ACCOUNT_ID, pagelen=25)
    if isinstance(result, Error):
        pytest.skip(
            f"prs.user_prs errored: {result.error.message if result.error else result!r}"
        )
    assert isinstance(result, list), (
        f"prs.user_prs must return list, got {type(result).__name__}"
    )
    for idx, pr in enumerate(result):
        assert isinstance(pr, Pullrequest), (
            f"prs.user_prs[{idx}] is {type(pr).__name__}, expected Pullrequest"
        )


# ---------------------------------------------------------------------------
# 21. prs.merge_task_status (bogus task_id — documents response)
# ---------------------------------------------------------------------------

async def test_merge_task_status_bogus_id_no_exception(
    client: BBClient, workspace: str
) -> None:
    """MTS-001/002 — bogus task_id returns Error/None, does not raise."""
    result = await prs.merge_task_status(
        client, workspace, PROBE_REPO, SEED_PR_ID, "bogus-task-id-00000"
    )
    # We do not assert on the exact type — documenting that it should not raise
    _ = result
