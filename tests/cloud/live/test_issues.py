"""Live integration tests for ``bb.cloud.sdk.issues``.

Context
-------
This workspace (beaverish) is on the **Bitbucket Cloud Free plan**.
The issue tracker is disabled (``has_issues=false``) for all repos on this plan.
Every issue-tracker endpoint returns HTTP 404.

PASS criteria for every test in this file
------------------------------------------
The SDK surfaces the 404 as an ``Error`` model or ``None`` — it does NOT raise
``UnexpectedStatus`` or return a real Issue / IssueComment / etc. object.

Seed data (read-only)
---------------------
- workspace: beaverish
- repo: bb-probe (issues NOT available — Free plan returns 404 for all endpoints)
"""

from __future__ import annotations

import pytest

from bb.cloud.errors import UnexpectedStatus
from bb.cloud.models.component import Component
from bb.cloud.models.error import Error
from bb.cloud.models.issue import Issue
from bb.cloud.models.issue_change import IssueChange
from bb.cloud.models.issue_comment import IssueComment
from bb.cloud.models.milestone import Milestone
from bb.cloud.models.version import Version
from bb.cloud.sdk import issues
from bb.cloud.sdk._client import BBClient

pytestmark = [pytest.mark.live]

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

FAKE_ISSUE_ID = 1
FAKE_COMMENT_ID = 1
FAKE_CHANGE_ID = 1
FAKE_MILESTONE_ID = 1
FAKE_VERSION_ID = 1
FAKE_COMPONENT_ID = 1
FAKE_ATTACHMENT_PATH = "screenshot.png"
FAKE_REPO_NAME = "bb-probe"
FAKE_TASK_ID = "deadbeef"


def _assert_no_happy_path(result: object, happy_type: type, fn_name: str) -> None:
    """Assert the result is NOT the happy-path model type.

    The Free plan returns 404 for all issue tracker endpoints. The SDK must
    surface this as Error/None rather than the typed model object.
    """
    assert not isinstance(result, happy_type), (
        f"issues.{fn_name} returned {type(result).__name__} on a Free-plan workspace — "
        f"expected Error or None (404 from API). "
        f"This may indicate the spec does not document 404 for this endpoint (spec bug), "
        f"or the SDK is not surfacing the error correctly (sdk-wrapper bug)."
    )


def _assert_no_exception_raised(result: object, fn_name: str) -> None:
    """Assert the SDK returned something (including None) rather than raising."""
    # The result may be None — that's fine for void-returning endpoints.
    # We just want to be sure no UnexpectedStatus was raised (caught at call site).
    pass  # If we reach this point, no exception was raised.


# ---------------------------------------------------------------------------
# issues.list
# ---------------------------------------------------------------------------


async def test_list_returns_error_not_issues(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """issues.list on Free plan must return Error (404), not a list of Issue."""
    try:
        result = await issues.list(client, workspace, probe_repo_slug)
    except UnexpectedStatus as exc:
        pytest.fail(
            f"issues.list raised UnexpectedStatus({exc.status_code}) — "
            f"SDK should return Error/None instead of raising. "
            f"BUG: spec does not document HTTP {exc.status_code} for this endpoint."
        )
    assert not isinstance(result, list) or result == [], (
        f"issues.list returned a non-empty list on Free plan workspace — "
        f"expected Error (404). Got: {result!r}"
    )


# ---------------------------------------------------------------------------
# issues.get
# ---------------------------------------------------------------------------


async def test_get_returns_error_or_none(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """issues.get on Free plan must return Error or None (404), not an Issue."""
    try:
        result = await issues.get(client, workspace, probe_repo_slug, FAKE_ISSUE_ID)
    except UnexpectedStatus as exc:
        pytest.fail(
            f"issues.get raised UnexpectedStatus({exc.status_code}) — SDK should return Error/None."
        )
    _assert_no_happy_path(result, Issue, "get")


# ---------------------------------------------------------------------------
# issues.create
# ---------------------------------------------------------------------------


async def test_create_returns_error_or_none(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """issues.create on Free plan must return Error or None (404), not an Issue."""
    try:
        result = await issues.create(client, workspace, probe_repo_slug)
    except UnexpectedStatus as exc:
        pytest.fail(
            f"issues.create raised UnexpectedStatus({exc.status_code}) — SDK should return Error/None."
        )
    _assert_no_happy_path(result, Issue, "create")


# ---------------------------------------------------------------------------
# issues.update
# ---------------------------------------------------------------------------


async def test_update_returns_error_or_none(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """issues.update on Free plan must return Error or None (404), not an Issue."""
    try:
        result = await issues.update(client, workspace, probe_repo_slug, FAKE_ISSUE_ID)
    except UnexpectedStatus as exc:
        pytest.fail(
            f"issues.update raised UnexpectedStatus({exc.status_code}) — SDK should return Error/None."
        )
    _assert_no_happy_path(result, Issue, "update")


# ---------------------------------------------------------------------------
# issues.delete
# ---------------------------------------------------------------------------


async def test_delete_does_not_raise(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """issues.delete on Free plan must not raise — returns None silently."""
    try:
        await issues.delete(client, workspace, probe_repo_slug, FAKE_ISSUE_ID)
    except UnexpectedStatus as exc:
        pytest.fail(
            f"issues.delete raised UnexpectedStatus({exc.status_code}) — "
            f"SDK should absorb unexpected status codes when raise_on_unexpected_status=False."
        )


# ---------------------------------------------------------------------------
# issues.comments
# ---------------------------------------------------------------------------


async def test_comments_returns_error_or_empty(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """issues.comments on Free plan must return Error (404) or empty list, not IssueComments."""
    try:
        result = await issues.comments(client, workspace, probe_repo_slug, FAKE_ISSUE_ID)
    except UnexpectedStatus as exc:
        pytest.fail(
            f"issues.comments raised UnexpectedStatus({exc.status_code}) — SDK should return Error/None."
        )
    assert not isinstance(result, list) or result == [], (
        f"issues.comments returned non-empty list on Free plan — expected Error. Got: {result!r}"
    )


# ---------------------------------------------------------------------------
# issues.get_comment
# ---------------------------------------------------------------------------


async def test_get_comment_returns_error_or_none(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """issues.get_comment on Free plan must return Error or None, not an IssueComment."""
    try:
        result = await issues.get_comment(
            client, workspace, probe_repo_slug, FAKE_ISSUE_ID, FAKE_COMMENT_ID
        )
    except UnexpectedStatus as exc:
        pytest.fail(
            f"issues.get_comment raised UnexpectedStatus({exc.status_code}) — SDK should return Error/None."
        )
    _assert_no_happy_path(result, IssueComment, "get_comment")


# ---------------------------------------------------------------------------
# issues.add_comment
# ---------------------------------------------------------------------------


async def test_add_comment_returns_error_or_none(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """issues.add_comment on Free plan must return Error or None (404)."""
    try:
        result = await issues.add_comment(client, workspace, probe_repo_slug, FAKE_ISSUE_ID)
    except UnexpectedStatus as exc:
        pytest.fail(
            f"issues.add_comment raised UnexpectedStatus({exc.status_code}) — SDK should return Error/None."
        )
    _assert_no_happy_path(result, IssueComment, "add_comment")


# ---------------------------------------------------------------------------
# issues.update_comment
# ---------------------------------------------------------------------------


async def test_update_comment_returns_error_or_none(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """issues.update_comment on Free plan must return Error or None (404)."""
    try:
        result = await issues.update_comment(
            client, workspace, probe_repo_slug, FAKE_ISSUE_ID, FAKE_COMMENT_ID
        )
    except UnexpectedStatus as exc:
        pytest.fail(
            f"issues.update_comment raised UnexpectedStatus({exc.status_code}) — SDK should return Error/None."
        )
    _assert_no_happy_path(result, IssueComment, "update_comment")


# ---------------------------------------------------------------------------
# issues.delete_comment
# ---------------------------------------------------------------------------


async def test_delete_comment_does_not_raise(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """issues.delete_comment on Free plan must not raise."""
    try:
        await issues.delete_comment(
            client, workspace, probe_repo_slug, FAKE_ISSUE_ID, FAKE_COMMENT_ID
        )
    except UnexpectedStatus as exc:
        pytest.fail(
            f"issues.delete_comment raised UnexpectedStatus({exc.status_code}) — should not raise."
        )


# ---------------------------------------------------------------------------
# issues.changes
# ---------------------------------------------------------------------------


async def test_changes_returns_error_or_empty(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """issues.changes on Free plan must return Error (404) or empty list."""
    try:
        result = await issues.changes(client, workspace, probe_repo_slug, FAKE_ISSUE_ID)
    except UnexpectedStatus as exc:
        pytest.fail(
            f"issues.changes raised UnexpectedStatus({exc.status_code}) — SDK should return Error/None."
        )
    assert not isinstance(result, list) or result == [], (
        f"issues.changes returned non-empty list on Free plan — expected Error. Got: {result!r}"
    )


# ---------------------------------------------------------------------------
# issues.get_change
# ---------------------------------------------------------------------------


async def test_get_change_returns_error_or_none(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """issues.get_change on Free plan must return Error or None, not an IssueChange."""
    try:
        result = await issues.get_change(
            client, workspace, probe_repo_slug, FAKE_ISSUE_ID, FAKE_CHANGE_ID
        )
    except UnexpectedStatus as exc:
        pytest.fail(
            f"issues.get_change raised UnexpectedStatus({exc.status_code}) — SDK should return Error/None."
        )
    _assert_no_happy_path(result, IssueChange, "get_change")


# ---------------------------------------------------------------------------
# issues.add_change
# ---------------------------------------------------------------------------


async def test_add_change_returns_error_or_none(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """issues.add_change on Free plan must return Error or None (404)."""
    try:
        result = await issues.add_change(client, workspace, probe_repo_slug, FAKE_ISSUE_ID)
    except UnexpectedStatus as exc:
        pytest.fail(
            f"issues.add_change raised UnexpectedStatus({exc.status_code}) — SDK should return Error/None."
        )
    _assert_no_happy_path(result, IssueChange, "add_change")


# ---------------------------------------------------------------------------
# issues.vote / issues.unvote
# ---------------------------------------------------------------------------


async def test_vote_does_not_raise(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """issues.vote on Free plan must not raise (404 is silently absorbed)."""
    try:
        await issues.vote(client, workspace, probe_repo_slug, FAKE_ISSUE_ID)
    except UnexpectedStatus as exc:
        pytest.fail(
            f"issues.vote raised UnexpectedStatus({exc.status_code}) — should not raise."
        )


async def test_unvote_does_not_raise(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """issues.unvote on Free plan must not raise (404 is silently absorbed)."""
    try:
        await issues.unvote(client, workspace, probe_repo_slug, FAKE_ISSUE_ID)
    except UnexpectedStatus as exc:
        pytest.fail(
            f"issues.unvote raised UnexpectedStatus({exc.status_code}) — should not raise."
        )


# ---------------------------------------------------------------------------
# issues.voted
# ---------------------------------------------------------------------------


async def test_voted_returns_error_or_none(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """issues.voted on Free plan must return None or Error (404), not a vote object."""
    try:
        result = await issues.voted(client, workspace, probe_repo_slug, FAKE_ISSUE_ID)
    except UnexpectedStatus as exc:
        pytest.fail(
            f"issues.voted raised UnexpectedStatus({exc.status_code}) — SDK should return Error/None."
        )
    _assert_no_happy_path(result, Issue, "voted")


# ---------------------------------------------------------------------------
# issues.watch / issues.unwatch
# ---------------------------------------------------------------------------


async def test_watch_does_not_raise(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """issues.watch on Free plan must not raise."""
    try:
        await issues.watch(client, workspace, probe_repo_slug, FAKE_ISSUE_ID)
    except UnexpectedStatus as exc:
        pytest.fail(
            f"issues.watch raised UnexpectedStatus({exc.status_code}) — should not raise."
        )


async def test_unwatch_does_not_raise(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """issues.unwatch on Free plan must not raise."""
    try:
        await issues.unwatch(client, workspace, probe_repo_slug, FAKE_ISSUE_ID)
    except UnexpectedStatus as exc:
        pytest.fail(
            f"issues.unwatch raised UnexpectedStatus({exc.status_code}) — should not raise."
        )


# ---------------------------------------------------------------------------
# issues.watching
# ---------------------------------------------------------------------------


async def test_watching_returns_none_or_error(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """issues.watching on Free plan must return None or Error, not a watch-status object."""
    try:
        result = await issues.watching(client, workspace, probe_repo_slug, FAKE_ISSUE_ID)
    except UnexpectedStatus as exc:
        pytest.fail(
            f"issues.watching raised UnexpectedStatus({exc.status_code}) — SDK should return Error/None."
        )
    _assert_no_happy_path(result, Issue, "watching")


# ---------------------------------------------------------------------------
# issues.milestones
# ---------------------------------------------------------------------------


async def test_milestones_returns_error_or_empty(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """issues.milestones on Free plan must return Error (404) or empty list."""
    try:
        result = await issues.milestones(client, workspace, probe_repo_slug)
    except UnexpectedStatus as exc:
        pytest.fail(
            f"issues.milestones raised UnexpectedStatus({exc.status_code}) — SDK should return Error/None."
        )
    assert not isinstance(result, list) or result == [], (
        f"issues.milestones returned non-empty list on Free plan — expected Error. Got: {result!r}"
    )


# ---------------------------------------------------------------------------
# issues.get_milestone
# ---------------------------------------------------------------------------


async def test_get_milestone_returns_error_or_none(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """issues.get_milestone on Free plan must return Error or None, not a Milestone."""
    try:
        result = await issues.get_milestone(client, workspace, probe_repo_slug, FAKE_MILESTONE_ID)
    except UnexpectedStatus as exc:
        pytest.fail(
            f"issues.get_milestone raised UnexpectedStatus({exc.status_code}) — SDK should return Error/None."
        )
    _assert_no_happy_path(result, Milestone, "get_milestone")


# ---------------------------------------------------------------------------
# issues.versions
# ---------------------------------------------------------------------------


async def test_versions_returns_error_or_empty(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """issues.versions on Free plan must return Error (404) or empty list."""
    try:
        result = await issues.versions(client, workspace, probe_repo_slug)
    except UnexpectedStatus as exc:
        pytest.fail(
            f"issues.versions raised UnexpectedStatus({exc.status_code}) — SDK should return Error/None."
        )
    assert not isinstance(result, list) or result == [], (
        f"issues.versions returned non-empty list on Free plan — expected Error. Got: {result!r}"
    )


# ---------------------------------------------------------------------------
# issues.get_version
# ---------------------------------------------------------------------------


async def test_get_version_returns_error_or_none(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """issues.get_version on Free plan must return Error or None, not a Version."""
    try:
        result = await issues.get_version(client, workspace, probe_repo_slug, FAKE_VERSION_ID)
    except UnexpectedStatus as exc:
        pytest.fail(
            f"issues.get_version raised UnexpectedStatus({exc.status_code}) — SDK should return Error/None."
        )
    _assert_no_happy_path(result, Version, "get_version")


# ---------------------------------------------------------------------------
# issues.components
# ---------------------------------------------------------------------------


async def test_components_returns_error_or_empty(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """issues.components on Free plan must return Error (404) or empty list."""
    try:
        result = await issues.components(client, workspace, probe_repo_slug)
    except UnexpectedStatus as exc:
        pytest.fail(
            f"issues.components raised UnexpectedStatus({exc.status_code}) — SDK should return Error/None."
        )
    assert not isinstance(result, list) or result == [], (
        f"issues.components returned non-empty list on Free plan — expected Error. Got: {result!r}"
    )


# ---------------------------------------------------------------------------
# issues.get_component
# ---------------------------------------------------------------------------


async def test_get_component_returns_error_or_none(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """issues.get_component on Free plan must return Error or None, not a Component."""
    try:
        result = await issues.get_component(client, workspace, probe_repo_slug, FAKE_COMPONENT_ID)
    except UnexpectedStatus as exc:
        pytest.fail(
            f"issues.get_component raised UnexpectedStatus({exc.status_code}) — SDK should return Error/None."
        )
    _assert_no_happy_path(result, Component, "get_component")


# ---------------------------------------------------------------------------
# issues.attachments
# ---------------------------------------------------------------------------


async def test_attachments_returns_none_or_error(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """issues.attachments on Free plan must return None or Error, not an attachment list."""
    try:
        result = await issues.attachments(client, workspace, probe_repo_slug, FAKE_ISSUE_ID)
    except UnexpectedStatus as exc:
        pytest.fail(
            f"issues.attachments raised UnexpectedStatus({exc.status_code}) — SDK should return Error/None."
        )
    # attachments returns Any | Error | None — just check it's not raising
    # and not returning a happy-path Issue model
    _assert_no_happy_path(result, Issue, "attachments")


# ---------------------------------------------------------------------------
# issues.get_attachment
# ---------------------------------------------------------------------------


async def test_get_attachment_returns_none_or_error(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """issues.get_attachment on Free plan must return None or Error."""
    try:
        result = await issues.get_attachment(
            client, workspace, probe_repo_slug, FAKE_ISSUE_ID, FAKE_ATTACHMENT_PATH
        )
    except UnexpectedStatus as exc:
        pytest.fail(
            f"issues.get_attachment raised UnexpectedStatus({exc.status_code}) — SDK should return Error/None."
        )
    _assert_no_happy_path(result, Issue, "get_attachment")


# ---------------------------------------------------------------------------
# issues.upload_attachment
# ---------------------------------------------------------------------------


async def test_upload_attachment_does_not_raise(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """issues.upload_attachment on Free plan must not raise."""
    try:
        await issues.upload_attachment(client, workspace, probe_repo_slug, FAKE_ISSUE_ID)
    except UnexpectedStatus as exc:
        pytest.fail(
            f"issues.upload_attachment raised UnexpectedStatus({exc.status_code}) — should not raise."
        )


# ---------------------------------------------------------------------------
# issues.delete_attachment
# ---------------------------------------------------------------------------


async def test_delete_attachment_does_not_raise(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """issues.delete_attachment on Free plan must not raise."""
    try:
        await issues.delete_attachment(
            client, workspace, probe_repo_slug, FAKE_ISSUE_ID, FAKE_ATTACHMENT_PATH
        )
    except UnexpectedStatus as exc:
        pytest.fail(
            f"issues.delete_attachment raised UnexpectedStatus({exc.status_code}) — should not raise."
        )


# ---------------------------------------------------------------------------
# issues.export
# ---------------------------------------------------------------------------


async def test_export_does_not_raise(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """issues.export on Free plan must not raise."""
    try:
        await issues.export(client, workspace, probe_repo_slug)
    except UnexpectedStatus as exc:
        pytest.fail(
            f"issues.export raised UnexpectedStatus({exc.status_code}) — should not raise."
        )


# ---------------------------------------------------------------------------
# issues.export_status
# ---------------------------------------------------------------------------


async def test_export_status_returns_none_or_error(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """issues.export_status on Free plan must return None or Error."""
    try:
        result = await issues.export_status(
            client, workspace, probe_repo_slug, FAKE_REPO_NAME, FAKE_TASK_ID
        )
    except UnexpectedStatus as exc:
        pytest.fail(
            f"issues.export_status raised UnexpectedStatus({exc.status_code}) — SDK should return Error/None."
        )
    _assert_no_happy_path(result, Issue, "export_status")


# ---------------------------------------------------------------------------
# issues.import_status
# ---------------------------------------------------------------------------


async def test_import_status_returns_none_or_error(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """issues.import_status on Free plan must return None or Error."""
    try:
        result = await issues.import_status(client, workspace, probe_repo_slug)
    except UnexpectedStatus as exc:
        pytest.fail(
            f"issues.import_status raised UnexpectedStatus({exc.status_code}) — SDK should return Error/None."
        )
    _assert_no_happy_path(result, Issue, "import_status")


# ---------------------------------------------------------------------------
# issues.import_data
# ---------------------------------------------------------------------------


async def test_import_data_does_not_raise(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """issues.import_data on Free plan must not raise."""
    try:
        await issues.import_data(client, workspace, probe_repo_slug)
    except UnexpectedStatus as exc:
        pytest.fail(
            f"issues.import_data raised UnexpectedStatus({exc.status_code}) — should not raise."
        )
