#!/usr/bin/env python3
"""Apply deprecated_endpoint decorators to generated Bitbucket Data Center API modules.

This hook mutates the freshly generated package in the temp output tree when
invoked by ``openapi-python-client``.  Falling back to the checked-in source
tree is supported for manual repair workflows.

Unlike the Cloud script, Bitbucket Data Center does not publish scheduled
removal dates, so all generated deprecated endpoints receive
``@deprecated_endpoint(None)`` (unconditional warning, no date-based blocking).

DC generated file names are derived from the ``operationId`` (camelCase →
snake_case) and the endpoint may appear in multiple tag directories (the
generator creates one file per tag).  The script patches every copy.
"""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Project / API directory discovery
# ---------------------------------------------------------------------------


def find_project_root() -> Path:
    """Find the project root directory.

    Resolution order:
    1. ``BB_PROJECT_ROOT`` environment variable (set by the generation workflow).
    2. Directory containing this script (``scripts/`` lives at project root).
    3. Current working directory.

    Raises :class:`RuntimeError` if ``bb_datacenter.openapi.json`` is not found.
    """
    candidates: list[Path] = []

    env_root = os.environ.get("BB_PROJECT_ROOT")
    if env_root:
        candidates.append(Path(env_root))

    candidates.append(Path(__file__).resolve().parent.parent)
    candidates.append(Path.cwd())

    for candidate in candidates:
        if (candidate / "bb_datacenter_fixed.openapi.json").exists():
            return candidate

    searched = ", ".join(str(p) for p in candidates)
    raise RuntimeError(
        "Cannot locate project root (bb_datacenter_fixed.openapi.json not found).\n"
        f"Searched: {searched}\n"
        "Set BB_PROJECT_ROOT to the project directory and retry."
    )


PROJECT_ROOT = find_project_root()
SPEC_FILE = PROJECT_ROOT / "bb_datacenter_fixed.openapi.json"


def find_api_dir() -> Path | None:
    """Find the DC API directory to modify.

    Checks the generated temp-dir layout first, then falls back to the
    project's checked-in source tree.
    """
    # openapi-python-client places the generated package at <cwd>/bb/api/
    generated_pkg_api = Path.cwd() / "bb" / "api"
    if generated_pkg_api.exists() and (generated_pkg_api / "deprecated").exists():
        return generated_pkg_api

    # Alternate: api/ directly from cwd
    cwd_api = Path.cwd() / "api"
    if cwd_api.exists() and (cwd_api / "deprecated").exists():
        return cwd_api

    # Fallback: project source tree
    project_api = PROJECT_ROOT / "src" / "bb" / "datacenter" / "api"
    if project_api.exists():
        return project_api

    return None


API_DIR = find_api_dir()


# ---------------------------------------------------------------------------
# Naming helpers
# ---------------------------------------------------------------------------


def operation_id_to_filename(operation_id: str) -> str:
    """Convert a camelCase ``operationId`` to a snake_case module filename.

    Examples::

        approve              → approve.py
        withdrawApproval     → withdraw_approval.py
        getDefaultBranch_1   → get_default_branch_1.py
        addUserToGroup       → add_user_to_group.py
    """
    # Handle sequences of uppercase letters followed by a capital+lower pair
    s = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", operation_id)
    # Insert underscore before each uppercase letter preceded by lowercase/digit
    s = re.sub(r"([a-z\d])([A-Z])", r"\1_\2", s)
    return s.lower() + ".py"


def tag_to_dirname(tag: str) -> str:
    """Convert an OpenAPI tag string to the generator's directory name.

    Examples::

        "Pull Requests"       → pull_requests
        "Deprecated"          → deprecated
        "Permission Management" → permission_management
    """
    return tag.lower().replace(" ", "_").replace("-", "_")


# ---------------------------------------------------------------------------
# File content manipulation
# ---------------------------------------------------------------------------


def has_deprecated_decorator(content: str) -> bool:
    """Return True if the file already carries a ``@deprecated_endpoint`` call."""
    return "@deprecated_endpoint" in content


def inject_deprecated_import(content: str) -> str:
    """Ensure ``from ...deprecation import deprecated_endpoint`` is present."""
    target = "from ...deprecation import deprecated_endpoint"
    if target in content:
        return content

    # Insert before the first ``from ... import`` statement
    pattern = re.search(r"^from \.\.\. import", content, re.MULTILINE)
    if pattern:
        return content[: pattern.start()] + target + "\n" + content[pattern.start() :]

    # Fallback: prepend after the first import block
    import_block = re.search(r"^((?:from .* import .*\n|import .*\n)+)", content, re.MULTILINE)
    if import_block:
        end = import_block.end()
        return content[:end] + target + "\n" + content[end:]

    # Last resort: prepend before the first function definition
    return re.sub(
        r"^((?:async\s+)?def )",
        target + "\n\n\n\\1",
        content,
        count=1,
        flags=re.MULTILINE,
    )


def apply_decorator_to_function(content: str, func_name: str) -> str:
    """Prepend ``@deprecated_endpoint(None)`` to *func_name* in *content*."""
    pattern = rf"^(?P<indent>[ ]*)(?:async\s+)?def {re.escape(func_name)}\("
    match = re.search(pattern, content, re.MULTILINE)
    if not match:
        return content

    indent = match.group("indent")
    decorator = f"{indent}@deprecated_endpoint(None)\n"

    def _replacer(m: re.Match) -> str:
        return decorator + m.group(0)

    return re.sub(pattern, _replacer, content, count=1, flags=re.MULTILINE)


def process_deprecated_endpoint(module_file: Path) -> bool:
    """Apply ``@deprecated_endpoint(None)`` to all generated functions in
    *module_file*.

    Returns ``True`` if the file was modified, ``False`` if it was already
    decorated or does not exist.
    """
    if not module_file.exists():
        return False

    content = module_file.read_text()

    if has_deprecated_decorator(content):
        return False  # Already decorated (idempotent)

    content = inject_deprecated_import(content)

    for func_name in ("sync_detailed", "sync", "asyncio_detailed", "asyncio"):
        if re.search(rf"(?:async\s+)?def {re.escape(func_name)}\(", content):
            content = apply_decorator_to_function(content, func_name)

    module_file.write_text(content)
    return True


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
    """Apply deprecation decorators to all deprecated DC endpoint modules."""
    if not SPEC_FILE.exists():
        print(f"ERROR: spec not found: {SPEC_FILE}", file=sys.stderr)
        return 1

    if API_DIR is None or not API_DIR.exists():
        print("ERROR: cannot locate DC API directory", file=sys.stderr)
        return 1

    with open(SPEC_FILE) as f:
        spec = json.load(f)

    http_methods = {"get", "post", "put", "delete", "patch", "options", "head"}
    modified_count = 0

    for _path, path_item in spec.get("paths", {}).items():
        for method, operation in path_item.items():
            if method.lower() not in http_methods:
                continue
            if not isinstance(operation, dict) or not operation.get("deprecated"):
                continue

            operation_id = operation.get("operationId")
            if not operation_id:
                continue

            filename = operation_id_to_filename(operation_id)
            tags = operation.get("tags", [])

            # The generator creates one file per tag directory.  Patch every copy.
            candidate_dirs: list[Path] = []
            for tag in tags:
                candidate_dirs.append(API_DIR / tag_to_dirname(tag))

            # Also search the whole API tree in case the naming is unusual.
            if not any(d.exists() for d in candidate_dirs):
                for api_file in API_DIR.rglob(filename):
                    candidate_dirs.append(api_file.parent)

            seen: set[Path] = set()
            for tag_dir in candidate_dirs:
                module_file = tag_dir / filename
                if module_file in seen:
                    continue
                seen.add(module_file)
                if process_deprecated_endpoint(module_file):
                    modified_count += 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
