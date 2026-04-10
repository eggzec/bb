#!/usr/bin/env python3
"""Apply deprecated endpoint decorators to generated API modules.

This hook must mutate the freshly generated package in the temp output tree
when invoked by ``openapi-python-client``. Falling back to the checked-in
source tree is only for manual repair workflows.
"""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path


# Find project root by looking for bb_cloud_fixed.openapi.json
def find_project_root() -> Path:
    """Find the project root directory.

    Resolution order:
    1. BB_PROJECT_ROOT environment variable (set by the generation workflow).
    2. The directory containing this script (scripts/ lives at project root).
    3. Current working directory, when the script is run directly from the root.

    Raises RuntimeError if the OpenAPI spec is not found in any candidate.
    """
    candidates: list[Path] = []

    env_root = os.environ.get("BB_PROJECT_ROOT")
    if env_root:
        candidates.append(Path(env_root))

    # __file__ is an absolute path when invoked via post-hook, so this is reliable.
    candidates.append(Path(__file__).resolve().parent.parent)

    candidates.append(Path.cwd())

    for candidate in candidates:
        if (candidate / "bb_cloud_fixed.openapi.json").exists():
            return candidate

    searched = ", ".join(str(p) for p in candidates)
    raise RuntimeError(
        "Cannot locate project root (bb_cloud_fixed.openapi.json not found).\n"
        f"Searched: {searched}\n"
        "Set BB_PROJECT_ROOT to the project directory and retry."
    )


PROJECT_ROOT = find_project_root()
SPEC_FILE = PROJECT_ROOT / "bb_cloud_fixed.openapi.json"


# Determine target API directory - could be in generated temp dir or project dir
def find_api_dir() -> Path | None:
    """Find the API directory to modify."""
    # Newer openapi-python-client layouts place the generated package at
    # <cwd>/bb/api/ when post-hooks run.
    generated_pkg_api = Path.cwd() / "bb" / "api"
    if generated_pkg_api.exists() and (generated_pkg_api / "addon").exists():
        return generated_pkg_api

    # Older or alternate layouts may expose api/ directly from the cwd.
    cwd_api = Path.cwd() / "api"
    if cwd_api.exists() and (cwd_api / "addon").exists():
        return cwd_api

    # Otherwise use project's API directory.
    project_api = PROJECT_ROOT / "src" / "bb" / "cloud" / "api"
    if project_api.exists():
        return project_api

    return None


API_DIR = find_api_dir()

DATE_PATTERNS = [
    re.compile(
        r"(?P<month>January|February|March|April|May|June|July|August|September|October|November|December)\s+(?P<day>\d{1,2}),?\s+(?P<year>\d{4})",
        re.IGNORECASE,
    ),
    re.compile(
        r"(?P<month>January|February|March|April|May|June|July|August|September|October|November|December)\s+(?P<year>\d{4})",
        re.IGNORECASE,
    ),
]


def path_to_module_name(path: str, method: str) -> str:
    """Convert OpenAPI path + method to module filename."""
    path = path.strip("/")
    path = re.sub(r"\{[^}]+\}", lambda m: m.group(0)[1:-1], path)
    path = path.replace("/", "_").replace("-", "_")
    method = method.lower()
    return f"{method}_{path}.py"


def find_module_file(name: str) -> Path | None:
    """Search API directory recursively for a module file."""
    if API_DIR is None:
        return None

    for api_file in API_DIR.rglob(name):
        return api_file
    return None


def has_deprecated_decorator(content: str) -> bool:
    """Check if content already has @deprecated_endpoint decorator."""
    return "@deprecated_endpoint" in content


def inject_deprecated_import(content: str) -> str:
    """Ensure deprecated_endpoint import is present."""
    if "from ...deprecation import deprecated_endpoint" in content:
        return content

    # Find where to insert - right after first third-party import but with other related imports
    # Look for "from ...errors import" as a reference point
    errors_import = content.find("from ... import errors")
    if errors_import != -1:
        # Insert before it, on the same line level
        return (
            content[:errors_import]
            + "from ...deprecation import deprecated_endpoint\nfrom ... import errors"
            + content[errors_import + len("from ... import errors") :]
        )

    # Look for any "from ..." import
    relative_import_pattern = re.search(r"^from \.\.\. import", content, re.MULTILINE)
    if relative_import_pattern:
        insert_pos = relative_import_pattern.start()
        return content[:insert_pos] + "from ...deprecation import deprecated_endpoint\n" + content[insert_pos:]

    # Fallback - add after all imports
    import_section = re.search(r"^((?:from .* import .*\n|import .*\n)+)", content, re.MULTILINE)
    if import_section:
        end_pos = import_section.end()
        return content[:end_pos] + "from ...deprecation import deprecated_endpoint\n" + content[end_pos:]

    # Last resort
    return re.sub(
        r"^(def |async def )",
        "from ...deprecation import deprecated_endpoint\n\n\1",
        content,
        count=1,
        flags=re.MULTILINE,
    )


def extract_deprecation_date(text: str) -> str | None:
    """Extract and normalize a deprecation date string from operation text."""
    for pattern in DATE_PATTERNS:
        match = pattern.search(text)
        if not match:
            continue

        month = match.group("month").title()
        year = match.group("year")
        day = match.groupdict().get("day")
        if day:
            return f"{month} {int(day)}, {year}"
        return f"{month} {year}"

    return None


def apply_decorator_to_function(content: str, func_name: str, deprecation_date: str | None) -> str:
    """Apply @deprecated_endpoint decorator to a specific function."""
    pattern = rf"^(?P<indent>[ ]*)(?:async\s+)?def {func_name}\("
    match = re.search(pattern, content, re.MULTILINE)

    if not match:
        return content

    indent = match.group("indent")
    if deprecation_date is None:
        decorator = f"{indent}@deprecated_endpoint(None)\n"
    else:
        escaped_date = deprecation_date.replace("\\", "\\\\").replace("'", "\\'")
        decorator = f"{indent}@deprecated_endpoint('{escaped_date}')\n"

    # Use a replacement function to avoid re.sub interpreting escape sequences
    def replacer(m):
        return decorator + m.group(0)

    return re.sub(
        pattern,
        replacer,
        content,
        count=1,
        flags=re.MULTILINE,
    )


def process_deprecated_endpoint(module_file: Path, deprecation_date: str | None) -> bool:
    """Apply @deprecated decorator to all functions in a module."""
    if not module_file.exists():
        return False

    content = module_file.read_text()

    if has_deprecated_decorator(content):
        return False

    content = inject_deprecated_import(content)

    for func_name in ["sync_detailed", "sync", "asyncio_detailed", "asyncio"]:
        if re.search(rf"(?:async\s+)?def {func_name}\(", content):
            content = apply_decorator_to_function(content, func_name, deprecation_date)

    module_file.write_text(content)
    return True


def main() -> int:
    """Main entry point."""
    if not SPEC_FILE.exists() or API_DIR is None or not API_DIR.exists():
        return 1

    with open(SPEC_FILE) as f:
        spec = json.load(f)

    modified_count = 0

    for path, path_item in spec.get("paths", {}).items():
        for method, operation in path_item.items():
            if method.lower() not in ["get", "post", "put", "delete", "patch", "options", "head"]:
                continue

            if not isinstance(operation, dict) or not operation.get("deprecated"):
                continue

            summary = operation.get("summary", "")
            description = operation.get("description", "")
            combined_text = f"{summary}\n{description}".strip()
            deprecation_date = extract_deprecation_date(combined_text)

            module_name = path_to_module_name(path, method)
            module_file = find_module_file(module_name)

            if not module_file:
                tags = operation.get("tags", [])
                if tags:
                    tag_dir = API_DIR / tags[0].lower().replace(" ", "_")
                    if tag_dir.exists():
                        alt_file = tag_dir / module_name
                        if alt_file.exists():
                            module_file = alt_file

            if module_file and process_deprecated_endpoint(module_file, deprecation_date):
                modified_count += 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
