"""Live tests for Bitbucket Data Center projects API."""
from __future__ import annotations

import pytest

from bb.datacenter.sdk import BBDCClient

pytestmark = pytest.mark.live


def test_list_projects(dc_client: BBDCClient) -> None:
    """Test listing projects returns a list."""
    projects = dc_client.projects.list()
    assert isinstance(projects, list)
    assert len(projects) > 0, "At least one project should exist for testing"


def test_get_project(dc_client: BBDCClient, dc_project_key: str) -> None:
    """Test getting a project by key."""
    proj = dc_client.projects.get(dc_project_key)
    assert proj is not None
    assert proj.key == dc_project_key
