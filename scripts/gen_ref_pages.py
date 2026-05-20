"""Generate API reference pages from hand-written SDK modules at build time.

This script is executed by mkdocs-gen-files during `mkdocs build` / `mkdocs serve`.
It walks src/bb/cloud/sdk/ and src/bb/datacenter/sdk/, creates one virtual .md page
per module (with a single ::: autodoc directive), and writes a SUMMARY.md for
literate-nav. Generated api/ directories under src/ are never included.
"""

from pathlib import Path

import mkdocs_gen_files

SRC = Path(__file__).parent.parent / "src"

# ── display names ──────────────────────────────────────────────────────────────

_NAMES: dict[str, str] = {
    "_auth": "Authentication",
    "_auth_validation": "Auth Validation",
    "_client": "Client",
    "_errors": "Errors",
    "_pagination": "Pagination",
    "addon": "Add-ons",
    "branch_restrictions": "Branch Restrictions",
    "branches": "Branches",
    "branching_model": "Branching Model",
    "builds": "Builds",
    "commit_statuses": "Commit Statuses",
    "commits": "Commits",
    "deployments": "Deployments",
    "downloads": "Downloads",
    "issues": "Issues",
    "pipelines": "Pipelines",
    "projects": "Projects",
    "properties": "Properties",
    "prs": "Pull Requests",
    "repos": "Repositories",
    "reports": "Reports",
    "search": "Search",
    "security": "Security",
    "snippets": "Snippets",
    "source": "Source",
    "users": "Users",
    "webhooks": "Webhooks",
    "workspaces": "Workspaces",
}


def _display(name: str) -> str:
    return _NAMES.get(name, name.lstrip("_").replace("_", " ").title())


# ── module lists ───────────────────────────────────────────────────────────────

CLOUD_CORE = ["_client", "_auth", "_auth_validation", "_pagination", "_errors"]
CLOUD_RESOURCES = [
    "addon",
    "branch_restrictions",
    "branches",
    "branching_model",
    "commit_statuses",
    "commits",
    "deployments",
    "downloads",
    "issues",
    "pipelines",
    "projects",
    "properties",
    "prs",
    "reports",
    "repos",
    "search",
    "snippets",
    "source",
    "users",
    "webhooks",
    "workspaces",
]

DC_CORE = ["_client", "_auth", "_auth_validation", "_pagination", "_errors"]
DC_RESOURCES = ["branches", "builds", "commits", "projects", "prs", "repos", "security"]


# ── generator ─────────────────────────────────────────────────────────────────

def _generate(
    sdk_pkg: str,          # e.g. "cloud.sdk" or "datacenter.sdk"
    sdk_dir: Path,         # e.g. SRC / "bb/cloud/sdk"
    core: list[str],
    resources: list[str],
    docs_prefix: str,      # e.g. "cloud" or "datacenter"
) -> None:
    nav = mkdocs_gen_files.Nav()

    groups = [("Core", core), ("Resources", resources)]
    for section, modules in groups:
        for name in modules:
            src_file = sdk_dir / f"{name}.py"
            if not src_file.exists():
                continue

            import_path = f"bb.{sdk_pkg}.{name}"
            doc_path = f"{docs_prefix}/api/{name}.md"
            display = _display(name)

            nav[section, display] = f"{name}.md"

            with mkdocs_gen_files.open(doc_path, "w") as fh:
                fh.write(f"# {display}\n\n")
                fh.write(f"::: {import_path}\n")

            mkdocs_gen_files.set_edit_path(
                doc_path,
                src_file.relative_to(SRC.parent),
            )

    with mkdocs_gen_files.open(f"{docs_prefix}/api/SUMMARY.md", "w") as fh:
        fh.writelines(nav.build_literate_nav())


_generate(
    sdk_pkg="cloud.sdk",
    sdk_dir=SRC / "bb" / "cloud" / "sdk",
    core=CLOUD_CORE,
    resources=CLOUD_RESOURCES,
    docs_prefix="cloud",
)

_generate(
    sdk_pkg="datacenter.sdk",
    sdk_dir=SRC / "bb" / "datacenter" / "sdk",
    core=DC_CORE,
    resources=DC_RESOURCES,
    docs_prefix="datacenter",
)
