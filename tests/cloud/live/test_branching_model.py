"""Live tests for ``bb.cloud.sdk.branching_model``."""

from __future__ import annotations

import pytest

from bb.cloud.models.branching_model import BranchingModel
from bb.cloud.models.branching_model_settings import BranchingModelSettings
from bb.cloud.models.effective_repo_branching_model import EffectiveRepoBranchingModel
from bb.cloud.sdk import branching_model
from bb.cloud.sdk._client import BBClient

pytestmark = pytest.mark.live


async def test_get_returns_branching_model(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    result = await branching_model.get(client, workspace, probe_repo_slug)
    if result is None:
        pytest.skip(f"branching_model.get returned None for {probe_repo_slug!r}")
    assert isinstance(result, BranchingModel), (
        f"branching_model.get must return BranchingModel, got {type(result).__name__}"
    )


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
