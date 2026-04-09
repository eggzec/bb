"""Tests for the custom deprecation module."""

from __future__ import annotations

import warnings

import pytest

from bb.cloud.deprecation import deprecated_endpoint, parse_deprecation_date
from bb.cloud.errors import UnexpectedStatus


@pytest.mark.parametrize(
    ("message", "expected"),
    [
        pytest.param("May 2026", (2026, 5, 1), id="month-year"),
        pytest.param(
            "This endpoint is deprecated and will be removed by May 2026.",
            (2026, 5, 1),
            id="month-year-embedded",
        ),
        pytest.param("May 31, 2026", (2026, 5, 31), id="full-date"),
        pytest.param("January 1, 2025", (2025, 1, 1), id="another-full-date"),
        pytest.param("December 2027", (2027, 12, 1), id="another-month-year"),
    ],
)
def test_parse_deprecation_date(message: str, expected: tuple[int, int, int]) -> None:
    parsed = parse_deprecation_date(message)

    assert parsed is not None
    assert (parsed.year, parsed.month, parsed.day) == expected


def test_past_deprecation_emits_warning_and_allows_execution() -> None:
    @deprecated_endpoint("January 2025")
    def old_endpoint() -> dict[str, str]:
        return {"status": "ok"}

    with warnings.catch_warnings(record=True) as captured:
        warnings.simplefilter("always")
        result = old_endpoint()

    assert result == {"status": "ok"}
    assert len(captured) == 1
    assert issubclass(captured[0].category, DeprecationWarning)
    msg = str(captured[0].message)
    assert "old_endpoint" in msg
    assert "Removal date was January 01, 2025" in msg


def test_future_deprecation_raises_http_410() -> None:
    @deprecated_endpoint("December 2026")
    def future_endpoint() -> dict[str, str]:
        return {"status": "ok"}

    with pytest.raises(UnexpectedStatus) as exc_info:
        future_endpoint()

    assert exc_info.value.status_code == 410
    assert "future_endpoint" in exc_info.value.content.decode()


@pytest.mark.asyncio
async def test_async_functions_are_also_guarded() -> None:
    @deprecated_endpoint("December 2026")
    async def future_async_endpoint() -> str:
        return "ok"

    with pytest.raises(UnexpectedStatus) as exc_info:
        await future_async_endpoint()

    assert exc_info.value.status_code == 410


def test_unknown_deprecation_date_emits_generic_warning() -> None:
    @deprecated_endpoint(None)
    def endpoint_without_date() -> str:
        return "ok"

    with warnings.catch_warnings(record=True) as captured:
        warnings.simplefilter("always")
        result = endpoint_without_date()

    assert result == "ok"
    assert len(captured) == 1
    assert issubclass(captured[0].category, DeprecationWarning)
    assert "endpoint_without_date" in str(captured[0].message)
