"""Live tests for addon.py — all skipped (requires Bitbucket Connect app).

Addon endpoints require an installed Bitbucket Connect app with a valid descriptor.
These stubs document the coverage gap and provide a clear skip reason.
See: https://developer.atlassian.com/cloud/bitbucket/app-descriptor/
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.live


async def test_delete_addon() -> None:
    """Test uninstalling the addon."""
    pytest.skip("requires a Bitbucket Connect app installation — see https://developer.atlassian.com/cloud/bitbucket/app-descriptor/")


async def test_update_addon() -> None:
    """Test updating the addon descriptor."""
    pytest.skip("requires a Bitbucket Connect app installation — see https://developer.atlassian.com/cloud/bitbucket/app-descriptor/")


async def test_list_linkers() -> None:
    """Test listing all addon linkers."""
    pytest.skip("requires a Bitbucket Connect app installation — see https://developer.atlassian.com/cloud/bitbucket/app-descriptor/")


async def test_get_linker() -> None:
    """Test fetching a specific addon linker."""
    pytest.skip("requires a Bitbucket Connect app installation — see https://developer.atlassian.com/cloud/bitbucket/app-descriptor/")


async def test_list_linker_values() -> None:
    """Test listing all values for an addon linker."""
    pytest.skip("requires a Bitbucket Connect app installation — see https://developer.atlassian.com/cloud/bitbucket/app-descriptor/")


async def test_get_linker_value() -> None:
    """Test fetching a specific value for an addon linker."""
    pytest.skip("requires a Bitbucket Connect app installation — see https://developer.atlassian.com/cloud/bitbucket/app-descriptor/")


async def test_create_linker_value() -> None:
    """Test creating a new value for an addon linker."""
    pytest.skip("requires a Bitbucket Connect app installation — see https://developer.atlassian.com/cloud/bitbucket/app-descriptor/")


async def test_set_linker_values() -> None:
    """Test setting (replacing) all values for an addon linker."""
    pytest.skip("requires a Bitbucket Connect app installation — see https://developer.atlassian.com/cloud/bitbucket/app-descriptor/")


async def test_clear_linker_values() -> None:
    """Test clearing (deleting) all values for an addon linker."""
    pytest.skip("requires a Bitbucket Connect app installation — see https://developer.atlassian.com/cloud/bitbucket/app-descriptor/")


async def test_delete_linker_value() -> None:
    """Test deleting a specific value from an addon linker."""
    pytest.skip("requires a Bitbucket Connect app installation — see https://developer.atlassian.com/cloud/bitbucket/app-descriptor/")
