"""Live tests for ``bb.cloud.sdk.prs``."""

from __future__ import annotations

import pytest

from bb.cloud.models.error import Error
from bb.cloud.models.pullrequest import Pullrequest
from bb.cloud.sdk import prs
from bb.cloud.sdk._client import BBClient

pytestmark = pytest.mark.live


async def test_list_returns_pullrequests(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
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


@pytest.mark.parametrize("state", [prs.PullrequestState.OPEN, prs.PullrequestState.MERGED,
                                    prs.PullrequestState.DECLINED, prs.PullrequestState.SUPERSEDED])
async def test_list_filter_by_state(
    client: BBClient,
    workspace: str,
    probe_repo_slug: str,
    state: prs.PullrequestState,
) -> None:
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
        # When filtered, every returned PR should carry the matching state.
        assert pr.state is None or str(pr.state).upper() == state.value.upper(), (
            f"prs.list(state={state.value!r})[{idx}] has wrong state: {pr.state!r}"
        )


async def test_get_returns_pullrequest(
    client: BBClient,
    workspace: str,
    probe_repo_slug: str,
    probe_pr_id: int,
) -> None:
    result = await prs.get(client, workspace, probe_repo_slug, probe_pr_id)
    assert not isinstance(result, Error), (
        f"prs.get({probe_pr_id}) errored: "
        f"{result.error.message if result.error else result!r}"
    )
    assert isinstance(result, Pullrequest), (
        f"prs.get must return Pullrequest, got {type(result).__name__}"
    )
    assert result.id == probe_pr_id, (
        f"prs.get returned id={result.id!r}, expected {probe_pr_id!r}"
    )


async def test_get_missing_pullrequest_is_error_or_none(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    result = await prs.get(client, workspace, probe_repo_slug, 999_999_999)
    assert not isinstance(result, Pullrequest), (
        f"prs.get for a nonexistent PR must not return Pullrequest, got {result!r}"
    )


async def test_default_reviewers_returns_list(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    result = await prs.default_reviewers(client, workspace, probe_repo_slug, pagelen=10)
    if isinstance(result, Error):
        pytest.skip(
            f"prs.default_reviewers not available: "
            f"{result.error.message if result.error else result!r}"
        )
    assert isinstance(result, list), (
        f"prs.default_reviewers must return list, got {type(result).__name__}"
    )


async def test_effective_default_reviewers_returns_list(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    result = await prs.effective_default_reviewers(client, workspace, probe_repo_slug, pagelen=10)
    if isinstance(result, Error):
        pytest.skip(
            f"prs.effective_default_reviewers not available: "
            f"{result.error.message if result.error else result!r}"
        )
    assert isinstance(result, list), (
        f"prs.effective_default_reviewers must return list, got {type(result).__name__}"
    )
