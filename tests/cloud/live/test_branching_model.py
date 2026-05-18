"""Live integration tests for ``bb.cloud.sdk.branching_model``.

Seed data (read-only):
- workspace:    beaverish
- repo:         bb-probe
- branch:       main  (development branch)

The update_settings test reads current settings and PUT-s them back unchanged
to verify the round-trip without mutating data.
"""

from __future__ import annotations

import pytest

from bb.cloud.models.branching_model import BranchingModel
from bb.cloud.models.branching_model_settings import BranchingModelSettings
from bb.cloud.models.effective_repo_branching_model import EffectiveRepoBranchingModel
from bb.cloud.sdk import branching_model
from bb.cloud.sdk._client import BBClient

pytestmark = [pytest.mark.live]

SEED_DEV_BRANCH = "main"


# ---------------------------------------------------------------------------
# branching_model.get
# ---------------------------------------------------------------------------


async def test_get_returns_branching_model(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    result = await branching_model.get(client, workspace, probe_repo_slug)
    if result is None:
        pytest.skip(f"branching_model.get returned None for {probe_repo_slug!r} — may not be configured")
    assert isinstance(result, BranchingModel), (
        f"branching_model.get must return BranchingModel, got {type(result).__name__}"
    )
    # type_ should be populated
    assert result.type_, f"BranchingModel.type_ is empty: {result!r}"


# ---------------------------------------------------------------------------
# branching_model.effective
# ---------------------------------------------------------------------------


async def test_effective_returns_model(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    result = await branching_model.effective(client, workspace, probe_repo_slug)
    if result is None:
        pytest.skip(f"branching_model.effective returned None for {probe_repo_slug!r}")
    assert isinstance(result, EffectiveRepoBranchingModel), (
        f"branching_model.effective must return EffectiveRepoBranchingModel, "
        f"got {type(result).__name__}"
    )


async def test_effective_development_branch_is_main(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """The bb-probe repo has 'main' as its development branch."""
    from bb.cloud.types import Unset

    result = await branching_model.effective(client, workspace, probe_repo_slug)
    if result is None:
        pytest.skip(f"branching_model.effective returned None for {probe_repo_slug!r}")
    assert isinstance(result, EffectiveRepoBranchingModel)

    dev = result.development
    if isinstance(dev, Unset) or dev is None:
        pytest.skip("effective branching model has no development branch configured")

    # Either use_mainbranch is True (tracking main) OR name is "main"
    is_main_branch = dev.use_mainbranch or dev.name == SEED_DEV_BRANCH
    assert is_main_branch, (
        f"Expected development branch to be {SEED_DEV_BRANCH!r} or use_mainbranch=True, "
        f"got name={dev.name!r}, use_mainbranch={dev.use_mainbranch!r}"
    )


async def test_effective_has_development_field(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    from bb.cloud.types import Unset

    result = await branching_model.effective(client, workspace, probe_repo_slug)
    if result is None:
        pytest.skip(f"branching_model.effective returned None for {probe_repo_slug!r}")
    assert isinstance(result, EffectiveRepoBranchingModel)
    # development field must be present (not Unset) for a seeded repo
    assert not isinstance(result.development, Unset), (
        "EffectiveRepoBranchingModel.development should not be UNSET for bb-probe"
    )


# ---------------------------------------------------------------------------
# branching_model.settings
# ---------------------------------------------------------------------------


async def test_settings_returns_model(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    result = await branching_model.settings(client, workspace, probe_repo_slug)
    if result is None:
        pytest.skip(f"branching_model.settings returned None for {probe_repo_slug!r}")
    assert isinstance(result, BranchingModelSettings), (
        f"branching_model.settings must return BranchingModelSettings, "
        f"got {type(result).__name__}"
    )
    assert result.type_, f"BranchingModelSettings.type_ is empty: {result!r}"


async def test_settings_has_type_field(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    result = await branching_model.settings(client, workspace, probe_repo_slug)
    if result is None:
        pytest.skip(f"branching_model.settings returned None for {probe_repo_slug!r}")
    assert isinstance(result, BranchingModelSettings)
    assert result.type_ == "branching_model_settings", (
        f"Expected type_='branching_model_settings', got {result.type_!r}"
    )


# ---------------------------------------------------------------------------
# branching_model.update_settings  (safe round-trip — PUT back same payload)
# ---------------------------------------------------------------------------


async def test_update_settings_roundtrip(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """Read current settings and PUT them back unchanged. Verifies the endpoint
    is reachable and returns BranchingModelSettings without mutating data."""
    current = await branching_model.settings(client, workspace, probe_repo_slug)
    if current is None:
        pytest.skip(f"branching_model.settings returned None for {probe_repo_slug!r}")
    assert isinstance(current, BranchingModelSettings)

    updated = await branching_model.update_settings(
        client, workspace, probe_repo_slug, body=current
    )
    if updated is None:
        pytest.skip("branching_model.update_settings returned None — may require write permission")
    assert isinstance(updated, BranchingModelSettings), (
        f"branching_model.update_settings must return BranchingModelSettings, "
        f"got {type(updated).__name__}"
    )
    # type_ must be preserved
    assert updated.type_ == current.type_, (
        f"type_ changed after update: {current.type_!r} → {updated.type_!r}"
    )


# ---------------------------------------------------------------------------
# branching_model.project_get / project_settings
# ---------------------------------------------------------------------------


async def test_project_get_returns_model_or_none(
    client: BBClient, workspace: str, probe_project_key: str
) -> None:
    result = await branching_model.project_get(client, workspace, probe_project_key)
    # May legitimately return None if the project has no branching model set
    assert result is None or isinstance(result, BranchingModel), (
        f"branching_model.project_get must return BranchingModel or None, "
        f"got {type(result).__name__}: {result!r}"
    )


async def test_project_settings_returns_model_or_none(
    client: BBClient, workspace: str, probe_project_key: str
) -> None:
    result = await branching_model.project_settings(client, workspace, probe_project_key)
    assert result is None or isinstance(result, BranchingModelSettings), (
        f"branching_model.project_settings must return BranchingModelSettings or None, "
        f"got {type(result).__name__}: {result!r}"
    )
