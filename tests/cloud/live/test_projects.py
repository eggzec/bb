"""Live tests for ``bb.cloud.sdk.projects``."""

from __future__ import annotations

import pytest

from bb.cloud.models.error import Error
from bb.cloud.models.project import Project
from bb.cloud.sdk import projects
from bb.cloud.sdk._client import BBClient

pytestmark = pytest.mark.live


async def test_list_returns_projects(client: BBClient, workspace: str) -> None:
    result = await projects.list(client, workspace, pagelen=10)
    assert not isinstance(result, Error), (
        f"projects.list errored: {result.error.message if result.error else result!r}"
    )
    assert isinstance(result, list), f"projects.list must return list, got {type(result).__name__}"
    for idx, project in enumerate(result):
        assert isinstance(project, Project), (
            f"projects.list[{idx}] is {type(project).__name__}, expected Project"
        )
        assert project.key, f"projects.list[{idx}] has empty key: {project!r}"


async def test_get_returns_project(client: BBClient, workspace: str, probe_project_key: str) -> None:
    result = await projects.get(client, workspace, probe_project_key)
    assert not isinstance(result, Error), (
        f"projects.get({probe_project_key!r}) errored: "
        f"{result.error.message if result.error else result!r}"
    )
    assert isinstance(result, Project), (
        f"projects.get must return Project, got {type(result).__name__}"
    )
    assert result.key == probe_project_key, (
        f"returned project key {result.key!r} does not match requested {probe_project_key!r}"
    )


async def test_get_missing_project_is_error_or_none(client: BBClient, workspace: str) -> None:
    result = await projects.get(client, workspace, "ZZZNOPE")
    assert not isinstance(result, Project), (
        f"projects.get for a nonexistent key must not return Project, got {result!r}"
    )


async def test_default_reviewers_returns_list(
    client: BBClient, workspace: str, probe_project_key: str
) -> None:
    result = await projects.default_reviewers(client, workspace, probe_project_key, pagelen=10)
    if isinstance(result, Error):
        pytest.skip(
            f"projects.default_reviewers not available: "
            f"{result.error.message if result.error else result!r}"
        )
    assert isinstance(result, list), (
        f"projects.default_reviewers must return list, got {type(result).__name__}"
    )
