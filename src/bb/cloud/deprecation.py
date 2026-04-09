"""Custom deprecation handling for Bitbucket Cloud API endpoints.

The ``deprecated_endpoint`` decorator accepts an optional date string and emits
generic warnings/errors that include the endpoint function identity.
"""

import re
import warnings
from collections.abc import Callable
from datetime import datetime
from functools import wraps
from typing import Any, TypeVar

try:
    from .errors import UnexpectedStatus
except ImportError:
    # Fallback for testing
    from bb.cloud.errors import UnexpectedStatus

F = TypeVar("F", bound=Callable[..., Any])

# Month name to number mapping
MONTH_MAP = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12,
}


def parse_deprecation_date(date_text: str | None) -> datetime | None:
    """Extract deprecation date from text like 'May 2026' or 'May 31, 2026'."""
    if not date_text:
        return None

    # Try to find "Month YYYY" or "Month DD, YYYY" patterns
    patterns = [
        r"(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{1,2}),?\s+(\d{4})",
        r"(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{4})",
    ]

    for pattern in patterns:
        match = re.search(pattern, date_text, re.IGNORECASE)
        if match:
            groups = match.groups()
            month_str = groups[0].lower()

            if len(groups) == 3:  # Month DD, YYYY
                month = MONTH_MAP.get(month_str, 1)
                day = int(groups[1])
                year = int(groups[2])
                return datetime(year, month, day)
            else:  # Month YYYY
                month = MONTH_MAP.get(month_str, 1)
                year = int(groups[1])
                return datetime(year, month, 1)

    return None


def _endpoint_name(func: Callable[..., Any]) -> str:
    return f"{func.__module__}.{func.__name__}"


def deprecated_endpoint(removal_date: str | None) -> Callable[[F], F]:
    """Decorator for deprecated endpoints with date-based HTTP error handling.

    Args:
        removal_date: Optional removal date (e.g., 'May 2026' or 'May 31, 2026')

    Returns:
        Decorator function

    Raises:
        UnexpectedStatus: With 410 (Gone) if deprecation date has not passed
    """
    deprecation_date = parse_deprecation_date(removal_date)

    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            endpoint = _endpoint_name(func)
            if deprecation_date:
                has_passed = deprecation_date <= datetime.now()
                if has_passed:
                    # Date has passed - emit warning but allow call
                    warnings.warn(
                        (
                            f"Endpoint '{endpoint}' is deprecated. "
                            f"Removal date was {deprecation_date.strftime('%B %d, %Y')} and has passed."
                        ),
                        DeprecationWarning,
                        stacklevel=2,
                    )
                else:
                    # Date has not passed - raise 410 Gone error
                    content = (
                        f"Endpoint '{endpoint}' is deprecated and unavailable until removal window. "
                        f"Removal date: {deprecation_date.strftime('%B %d, %Y')}."
                    )
                    raise UnexpectedStatus(
                        status_code=410,
                        content=content.encode(),
                    )
            else:
                warnings.warn(
                    f"Endpoint '{endpoint}' is deprecated.",
                    DeprecationWarning,
                    stacklevel=2,
                )

            return func(*args, **kwargs)

        return wrapper  # type: ignore

    return decorator
