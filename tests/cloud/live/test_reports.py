"""Live tests for ``bb.cloud.sdk.reports``.

Seed data (never mutate):
- workspace:     beaverish
- repo:          bb-probe
- commit hash:   84952fad87fb39e3c6d61811a93769378dd4fad7
- report_id:     bb-probe-report (type: TEST)
- annotation_id: bb-probe-ann-001 on bb-probe-report

Spec / generator risk:
- PUT /reports/{reportId}       → spec says 200; if API returns 201 the generated
  _parse_response raises UnexpectedStatus (201 is not handled).
- PUT /annotations/{annotationId} → same risk.
  Tests will xfail with explanation if UnexpectedStatus is raised.
"""

from __future__ import annotations

import uuid

import pytest

from bb.cloud.errors import UnexpectedStatus
from bb.cloud.models.error import Error
from bb.cloud.models.report import Report
from bb.cloud.models.report_annotation import ReportAnnotation
from bb.cloud.models.report_annotation_annotation_type import ReportAnnotationAnnotationType
from bb.cloud.models.report_annotation_result import ReportAnnotationResult
from bb.cloud.models.report_annotation_severity import ReportAnnotationSeverity
from bb.cloud.models.report_report_type import ReportReportType
from bb.cloud.models.report_result import ReportResult
from bb.cloud.sdk import reports
from bb.cloud.sdk._client import BBClient

pytestmark = pytest.mark.live

# ---------------------------------------------------------------------------
# Seed constants
# ---------------------------------------------------------------------------
SEED_COMMIT = "84952fad87fb39e3c6d61811a93769378dd4fad7"
SEED_REPO = "bb-probe"
SEED_REPORT_ID = "bb-probe-report"
SEED_ANNOTATION_ID = "bb-probe-ann-001"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _err(result: object) -> str:
    if isinstance(result, Error):
        return result.error.message if getattr(result, "error", None) else repr(result)
    return repr(result)


def _make_report(report_id: str, result: ReportResult = ReportResult.PENDING) -> Report:
    return Report(
        type_="report",
        external_id=report_id,
        title="bb-sdk live test report",
        details="Throwaway report created by bb SDK live tests",
        report_type=ReportReportType.TEST,
        result=result,
        reporter="bb-sdk-live-tests",
        link="https://example.com/report",
    )


def _make_annotation(annotation_id: str) -> ReportAnnotation:
    return ReportAnnotation(
        type_="report_annotation",
        external_id=annotation_id,
        annotation_type=ReportAnnotationAnnotationType.BUG,
        summary="Throwaway annotation from bb SDK live tests",
        details="This annotation was created automatically and should be deleted.",
        result=ReportAnnotationResult.FAILED,
        severity=ReportAnnotationSeverity.LOW,
        path="README.md",
        line=1,
        link="https://example.com/annotation",
    )


# ---------------------------------------------------------------------------
# TC-REP-001: list
# ---------------------------------------------------------------------------


async def test_list_reports_for_seed_commit(
    client: BBClient,
    workspace: str,
) -> None:
    """TC-REP-001: list returns a list containing the seeded report."""
    result = await reports.list(client, workspace, SEED_REPO, SEED_COMMIT)
    assert not isinstance(result, Error), (
        f"reports.list errored: {_err(result)}"
    )
    assert isinstance(result, list), (
        f"reports.list must return list, got {type(result).__name__}"
    )
    assert result, (
        f"reports.list returned empty list for commit {SEED_COMMIT!r}"
    )
    for idx, report in enumerate(result):
        assert isinstance(report, Report), (
            f"reports.list[{idx}] is {type(report).__name__}, expected Report"
        )

    external_ids = {r.external_id for r in result}
    assert SEED_REPORT_ID in external_ids, (
        f"Expected seed report {SEED_REPORT_ID!r} in reports list, got: {external_ids!r}"
    )


# ---------------------------------------------------------------------------
# TC-REP-002 / TC-REP-003: get
# ---------------------------------------------------------------------------


async def test_get_seed_report(
    client: BBClient,
    workspace: str,
) -> None:
    """TC-REP-002: get the seeded report by ID and verify type=TEST."""
    result = await reports.get(client, workspace, SEED_REPO, SEED_COMMIT, SEED_REPORT_ID)
    assert not isinstance(result, Error), (
        f"reports.get({SEED_REPORT_ID!r}) errored: {_err(result)}"
    )
    assert isinstance(result, Report), (
        f"reports.get must return Report, got {type(result).__name__}"
    )
    assert result.report_type == ReportReportType.TEST, (
        f"report_type mismatch: got {result.report_type!r}, expected TEST"
    )


async def test_get_missing_report_is_error_or_none(
    client: BBClient,
    workspace: str,
) -> None:
    """TC-REP-003: get with a nonexistent report_id returns Error or None."""
    result = await reports.get(
        client, workspace, SEED_REPO, SEED_COMMIT, "report-that-does-not-exist-xyz"
    )
    assert not isinstance(result, Report), (
        f"reports.get for missing id must not return Report, got {result!r}"
    )


# ---------------------------------------------------------------------------
# TC-REP-004 / TC-REP-005 / TC-REP-006: create_or_update + delete
# ---------------------------------------------------------------------------


async def test_create_throwaway_report(
    client: BBClient,
    workspace: str,
) -> None:
    """TC-REP-004: create (PUT) a new report; cleanup via delete.

    SPEC NOTE: PUT /reports/{reportId} is documented as returning 200.
    The generated _parse_response handles 200 → Report.
    If the live API returns 201 instead, an UnexpectedStatus is raised.
    This test catches that with pytest.xfail and documents it as BUG-COMMITS-002.
    """
    throwaway_id = f"bb-test-report-{uuid.uuid4().hex[:8]}"
    try:
        result = await reports.create_or_update(
            client,
            workspace,
            SEED_REPO,
            SEED_COMMIT,
            throwaway_id,
            body=_make_report(throwaway_id),
        )
        assert result is not None, (
            f"reports.create_or_update returned None for {throwaway_id!r}"
        )
        assert not isinstance(result, Error), (
            f"reports.create_or_update errored: {_err(result)}"
        )
        assert isinstance(result, Report), (
            f"reports.create_or_update must return Report, got {type(result).__name__}"
        )
        assert result.report_type == ReportReportType.TEST, (
            f"report_type mismatch: got {result.report_type!r}, expected TEST"
        )
    except UnexpectedStatus as exc:
        pytest.xfail(
            f"reports.create_or_update raised UnexpectedStatus({exc.status_code}) — "
            f"likely API returned 201 but generated parser only handles 200. "
            f"See BUG-COMMITS-002."
        )
    finally:
        # Best-effort delete — ignore errors.
        try:
            await reports.delete(client, workspace, SEED_REPO, SEED_COMMIT, throwaway_id)
        except Exception:
            pass


async def test_update_throwaway_report(
    client: BBClient,
    workspace: str,
) -> None:
    """TC-REP-005: create then update the report result to PASSED."""
    throwaway_id = f"bb-test-report-{uuid.uuid4().hex[:8]}"
    try:
        create_result = await reports.create_or_update(
            client,
            workspace,
            SEED_REPO,
            SEED_COMMIT,
            throwaway_id,
            body=_make_report(throwaway_id, ReportResult.PENDING),
        )
        if create_result is None or isinstance(create_result, Error):
            pytest.skip(
                f"Skipping update test: create failed ({_err(create_result)!r})"
            )

        # Update to PASSED.
        updated = await reports.create_or_update(
            client,
            workspace,
            SEED_REPO,
            SEED_COMMIT,
            throwaway_id,
            body=_make_report(throwaway_id, ReportResult.PASSED),
        )
        assert not isinstance(updated, Error), (
            f"reports.create_or_update (update) errored: {_err(updated)}"
        )
        assert isinstance(updated, Report), (
            f"reports.create_or_update (update) must return Report, got {type(updated).__name__}"
        )
        assert updated.result == ReportResult.PASSED, (
            f"result mismatch after update: got {updated.result!r}, expected PASSED"
        )
    except UnexpectedStatus as exc:
        pytest.xfail(
            f"reports.create_or_update raised UnexpectedStatus({exc.status_code}) — "
            f"likely API returned 201 but generated parser only handles 200. "
            f"See BUG-COMMITS-002."
        )
    finally:
        try:
            await reports.delete(client, workspace, SEED_REPO, SEED_COMMIT, throwaway_id)
        except Exception:
            pass


async def test_delete_throwaway_report(
    client: BBClient,
    workspace: str,
) -> None:
    """TC-REP-006: delete a report and confirm it is gone."""
    throwaway_id = f"bb-test-report-{uuid.uuid4().hex[:8]}"
    try:
        create_result = await reports.create_or_update(
            client,
            workspace,
            SEED_REPO,
            SEED_COMMIT,
            throwaway_id,
            body=_make_report(throwaway_id),
        )
        if create_result is None or isinstance(create_result, Error):
            pytest.skip(
                f"Skipping delete test: create failed ({_err(create_result)!r})"
            )
    except UnexpectedStatus as exc:
        pytest.xfail(
            f"reports.create_or_update raised UnexpectedStatus({exc.status_code}) — "
            f"cannot test delete without a successfully created report. See BUG-COMMITS-002."
        )

    # Delete.
    await reports.delete(client, workspace, SEED_REPO, SEED_COMMIT, throwaway_id)

    # Confirm it is gone.
    gone = await reports.get(client, workspace, SEED_REPO, SEED_COMMIT, throwaway_id)
    assert not isinstance(gone, Report), (
        f"reports.get after delete must not return Report, got {gone!r}"
    )


# ---------------------------------------------------------------------------
# TC-REP-007 / TC-REP-008 / TC-REP-009: annotations list + get
# ---------------------------------------------------------------------------


async def test_list_annotations_for_seed_report(
    client: BBClient,
    workspace: str,
) -> None:
    """TC-REP-007: annotations returns a list containing the seeded annotation."""
    result = await reports.annotations(
        client, workspace, SEED_REPO, SEED_COMMIT, SEED_REPORT_ID
    )
    assert not isinstance(result, Error), (
        f"reports.annotations errored: {_err(result)}"
    )
    assert isinstance(result, list), (
        f"reports.annotations must return list, got {type(result).__name__}"
    )
    for idx, ann in enumerate(result):
        assert isinstance(ann, ReportAnnotation), (
            f"reports.annotations[{idx}] is {type(ann).__name__}, expected ReportAnnotation"
        )

    external_ids = {a.external_id for a in result}
    assert SEED_ANNOTATION_ID in external_ids, (
        f"Expected seed annotation {SEED_ANNOTATION_ID!r} in annotations list, "
        f"got: {external_ids!r}"
    )


async def test_get_seed_annotation(
    client: BBClient,
    workspace: str,
) -> None:
    """TC-REP-008: get the seeded annotation by ID."""
    result = await reports.get_annotation(
        client, workspace, SEED_REPO, SEED_COMMIT, SEED_REPORT_ID, SEED_ANNOTATION_ID
    )
    assert not isinstance(result, Error), (
        f"reports.get_annotation({SEED_ANNOTATION_ID!r}) errored: {_err(result)}"
    )
    assert isinstance(result, ReportAnnotation), (
        f"reports.get_annotation must return ReportAnnotation, got {type(result).__name__}"
    )
    assert result.external_id == SEED_ANNOTATION_ID, (
        f"external_id mismatch: got {result.external_id!r}, expected {SEED_ANNOTATION_ID!r}"
    )


async def test_get_missing_annotation_is_error_or_none(
    client: BBClient,
    workspace: str,
) -> None:
    """TC-REP-009: get_annotation with a nonexistent ID returns Error or None."""
    result = await reports.get_annotation(
        client,
        workspace,
        SEED_REPO,
        SEED_COMMIT,
        SEED_REPORT_ID,
        "annotation-that-does-not-exist-xyz",
    )
    assert not isinstance(result, ReportAnnotation), (
        f"reports.get_annotation for missing id must not return ReportAnnotation, got {result!r}"
    )


# ---------------------------------------------------------------------------
# TC-REP-010 / TC-REP-011: create_annotation + delete_annotation
# ---------------------------------------------------------------------------


async def test_create_throwaway_annotation(
    client: BBClient,
    workspace: str,
) -> None:
    """TC-REP-010: create an annotation on the seeded report; cleanup via delete.

    SPEC NOTE: PUT /annotations/{annotationId} is documented as returning 200.
    The generated _parse_response handles 200 → ReportAnnotation.
    If the live API returns 201 instead, UnexpectedStatus is raised.
    """
    throwaway_ann_id = f"bb-test-ann-{uuid.uuid4().hex[:8]}"
    try:
        result = await reports.create_annotation(
            client,
            workspace,
            SEED_REPO,
            SEED_COMMIT,
            SEED_REPORT_ID,
            throwaway_ann_id,
            body=_make_annotation(throwaway_ann_id),
        )
        assert result is not None, (
            f"reports.create_annotation returned None for {throwaway_ann_id!r}"
        )
        assert not isinstance(result, Error), (
            f"reports.create_annotation errored: {_err(result)}"
        )
        assert isinstance(result, ReportAnnotation), (
            f"reports.create_annotation must return ReportAnnotation, "
            f"got {type(result).__name__}"
        )
        assert result.external_id == throwaway_ann_id, (
            f"external_id mismatch: got {result.external_id!r}, expected {throwaway_ann_id!r}"
        )
    except UnexpectedStatus as exc:
        pytest.xfail(
            f"reports.create_annotation raised UnexpectedStatus({exc.status_code}) — "
            f"likely API returned 201 but generated parser only handles 200. "
            f"See BUG-COMMITS-003."
        )
    finally:
        try:
            await reports.delete_annotation(
                client, workspace, SEED_REPO, SEED_COMMIT, SEED_REPORT_ID, throwaway_ann_id
            )
        except Exception:
            pass


async def test_delete_throwaway_annotation(
    client: BBClient,
    workspace: str,
) -> None:
    """TC-REP-011: create an annotation, delete it, confirm it is gone."""
    throwaway_ann_id = f"bb-test-ann-{uuid.uuid4().hex[:8]}"
    try:
        create_result = await reports.create_annotation(
            client,
            workspace,
            SEED_REPO,
            SEED_COMMIT,
            SEED_REPORT_ID,
            throwaway_ann_id,
            body=_make_annotation(throwaway_ann_id),
        )
        if create_result is None or isinstance(create_result, Error):
            pytest.skip(
                f"Skipping annotation delete test: create failed ({_err(create_result)!r})"
            )
    except UnexpectedStatus as exc:
        pytest.xfail(
            f"reports.create_annotation raised UnexpectedStatus({exc.status_code}) — "
            f"cannot test delete_annotation without a successfully created annotation. "
            f"See BUG-COMMITS-003."
        )

    # Delete.
    await reports.delete_annotation(
        client, workspace, SEED_REPO, SEED_COMMIT, SEED_REPORT_ID, throwaway_ann_id
    )

    # Confirm it is gone.
    gone = await reports.get_annotation(
        client, workspace, SEED_REPO, SEED_COMMIT, SEED_REPORT_ID, throwaway_ann_id
    )
    assert not isinstance(gone, ReportAnnotation), (
        f"reports.get_annotation after delete must not return ReportAnnotation, got {gone!r}"
    )
