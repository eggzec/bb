"""Live tests for Bitbucket Data Center repositories API."""
from __future__ import annotations

import pytest

from bb.datacenter.sdk import BBDCClient

pytestmark = pytest.mark.live


def test_list_repos(dc_client: BBDCClient, dc_project_key: str) -> None:
    """Test listing repositories in a project."""
    repos = dc_client.repos.list(dc_project_key)
    assert isinstance(repos, list)
    assert len(repos) > 0, f"Project {dc_project_key} should have at least one repo for testing"


def test_get_repo(dc_client: BBDCClient, dc_project_key: str, dc_repo_slug: str) -> None:
    """Test getting a repository by key and slug."""
    repo = dc_client.repos.get(dc_project_key, dc_repo_slug)
    assert repo is not None
    assert repo.slug == dc_repo_slug


def test_list_all_repos(dc_client: BBDCClient) -> None:
    """Test listing all repositories across all projects."""
    repos = dc_client.repos.list_all()
    assert isinstance(repos, list)
    # At least one repo should exist for testing
    assert len(repos) > 0, "At least one repository should exist for testing"
