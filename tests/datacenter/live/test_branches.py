"""Live tests for Bitbucket Data Center branches API."""
from __future__ import annotations

import pytest

from bb.datacenter.sdk import BBDCClient

pytestmark = pytest.mark.live


def test_list_branches(dc_client: BBDCClient, dc_project_key: str, dc_repo_slug: str) -> None:
    """Test listing branches in a repository."""
    branches = dc_client.branches.list(dc_project_key, dc_repo_slug)
    assert isinstance(branches, list)
    assert len(branches) > 0, "Repository should have at least one branch"


def test_get_default_branch(dc_client: BBDCClient, dc_project_key: str, dc_repo_slug: str) -> None:
    """Test getting the default branch of a repository."""
    branch = dc_client.branches.get_default(dc_project_key, dc_repo_slug)
    assert branch is not None
    assert branch.display_id is not None


def test_get_branch_by_name(
    dc_client: BBDCClient, dc_project_key: str, dc_repo_slug: str, dc_branch_name: str
) -> None:
    """Test that the known branch exists in the branch list."""
    branches = dc_client.branches.list(dc_project_key, dc_repo_slug)
    branch_names = [b.display_id for b in branches]
    assert dc_branch_name in branch_names, f"Branch {dc_branch_name} should exist"
