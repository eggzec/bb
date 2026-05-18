"""Tests for bb.cloud.sdk.branching_model."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from bb.cloud.models.branching_model import BranchingModel
from bb.cloud.models.branching_model_settings import BranchingModelSettings
from bb.cloud.models.effective_repo_branching_model import EffectiveRepoBranchingModel
from bb.cloud.sdk import branching_model
from bb.cloud.sdk._errors import AuthenticationError

_API = "bb.cloud.api.branching_model"


async def test_get_returns_model(mock_client):
    model = MagicMock(spec=BranchingModel)
    with patch(
        f"{_API}.get_repositories_workspace_repo_slug_branching_model.asyncio", new=AsyncMock(return_value=model)
    ):
        result = await branching_model.get(mock_client, "ws", "slug")
    assert result is model


async def test_get_returns_none(mock_client):
    with patch(
        f"{_API}.get_repositories_workspace_repo_slug_branching_model.asyncio", new=AsyncMock(return_value=None)
    ):
        result = await branching_model.get(mock_client, "ws", "slug")
    assert result is None


async def test_effective_returns_model(mock_client):
    model = MagicMock(spec=EffectiveRepoBranchingModel)
    with patch(
        f"{_API}.get_repositories_workspace_repo_slug_effective_branching_model.asyncio",
        new=AsyncMock(return_value=model),
    ):
        result = await branching_model.effective(mock_client, "ws", "slug")
    assert result is model


async def test_settings_returns_settings(mock_client):
    settings = MagicMock(spec=BranchingModelSettings)
    with patch(
        f"{_API}.get_repositories_workspace_repo_slug_branching_model_settings.asyncio",
        new=AsyncMock(return_value=settings),
    ):
        result = await branching_model.settings(mock_client, "ws", "slug")
    assert result is settings


async def test_update_settings_returns_settings(mock_client):
    settings = MagicMock(spec=BranchingModelSettings)
    with patch(
        f"{_API}.put_repositories_workspace_repo_slug_branching_model_settings.asyncio",
        new=AsyncMock(return_value=settings),
    ):
        result = await branching_model.update_settings(mock_client, "ws", "slug", body=MagicMock(spec=BranchingModelSettings))
    assert result is settings


async def test_project_get_returns_model(mock_client):
    model = MagicMock(spec=BranchingModel)
    with patch(
        f"{_API}.get_workspaces_workspace_projects_project_key_branching_model.asyncio",
        new=AsyncMock(return_value=model),
    ):
        result = await branching_model.project_get(mock_client, "ws", "PROJ")
    assert result is model


async def test_project_settings_returns_settings(mock_client):
    settings = MagicMock(spec=BranchingModelSettings)
    with patch(
        f"{_API}.get_workspaces_workspace_projects_project_key_branching_model_settings.asyncio",
        new=AsyncMock(return_value=settings),
    ):
        result = await branching_model.project_settings(mock_client, "ws", "PROJ")
    assert result is settings


async def test_update_project_settings_returns_settings(mock_client):
    settings = MagicMock(spec=BranchingModelSettings)
    with patch(
        f"{_API}.put_workspaces_workspace_projects_project_key_branching_model_settings.asyncio",
        new=AsyncMock(return_value=settings),
    ):
        result = await branching_model.update_project_settings(mock_client, "ws", "PROJ", body=MagicMock(spec=BranchingModelSettings))
    assert result is settings


async def test_get_raises_on_bad_auth(bad_auth_client):
    with pytest.raises(AuthenticationError):
        await branching_model.get(bad_auth_client, "ws", "slug")
