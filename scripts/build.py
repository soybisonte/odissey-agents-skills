"""Build safe, deterministic Odissey distributions from canonical skills."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import shutil
from typing import Sequence

if __package__:
    from scripts.odissey_tooling import (
        OWNERSHIP_HEADER,
        atomic_write_text,
        normalize_newlines,
        parse_frontmatter,
    )
    from scripts.validate import validate_catalog
else:  # pragma: no cover - exercised by the build.sh wrapper.
    from odissey_tooling import OWNERSHIP_HEADER, atomic_write_text, normalize_newlines, parse_frontmatter
    from validate import validate_catalog


_CANONICAL_SKILLS = Path(".agents/skills")
_MANAGED_SUBTREES = (
    Path(".codex/agents"),
    Path(".github/agents"),
    Path("generated-skills"),
    Path("plugins/bbva-odissey/skills"),
    Path(".cursor/rules"),
)


class BuildValidationError(ValueError):
    """Raised before any output write when canonical source validation fails."""


class BuildSafetyError(ValueError):
    """Raised when a managed output is not safe to replace."""


@dataclass(frozen=True)
class BuildResult:
    """Stable summary of one successful build."""

    root: Path
    skill_count: int


def _is_within(path: Path, ancestor: Path) -> bool:
    try:
        path.relative_to(ancestor)
    except ValueError:
        return False
    return True


def _managed_path(root: Path, relative_path: Path) -> Path:
    """Resolve a declared output subtree without granting parent-directory ownership."""
    if relative_path not in _MANAGED_SUBTREES:
        raise BuildSafetyError(f"not a managed output subtree: {relative_path}")
    target = root / relative_path
    if target.is_symlink():
        raise BuildSafetyError(f"managed output must not be a symlink: {target}")
    return target


def _clear_managed_subtree(root: Path, relative_path: Path) -> None:
    """Delete only a declared fully managed subtree, never one of its parents."""
    target = _managed_path(root, relative_path)
    if target.exists():
        if not target.is_dir():
            raise BuildSafetyError(f"managed output must be a directory: {target}")
        shutil.rmtree(target)
    target.mkdir(parents=True)


def _owned_skill_text(source: Path) -> str:
    """Insert the ownership marker after frontmatter so generated skills stay valid."""
    text = normalize_newlines(source.read_text(encoding="utf-8"))
    lines = text.splitlines(keepends=True)
    delimiters = [index for index, line in enumerate(lines) if line.rstrip("\n") == "---"]
    if len(delimiters) < 2:  # Validation is completed before this function is reached.
        raise BuildValidationError(f"cannot add ownership header to invalid skill: {source}")
    insert_at = delimiters[1] + 1
    return "".join([*lines[:insert_at], f"{OWNERSHIP_HEADER}\n", *lines[insert_at:]])


def _copy_skill_tree(source_skill: Path, destination_skill: Path) -> None:
    """Copy one validated skill tree using atomic, normalized writes in stable order."""
    for source in sorted(source_skill.rglob("*")):
        if not source.is_file():
            continue
        destination = destination_skill / source.relative_to(source_skill)
        if source.name == "SKILL.md":
            content = _owned_skill_text(source)
        else:
            content = f"{OWNERSHIP_HEADER}\n{normalize_newlines(source.read_text(encoding='utf-8'))}"
        atomic_write_text(destination, content)


def _write_cursor_rule(source_skill: Path, destination: Path) -> None:
    """Produce a minimal owned Cursor rule; richer platform rendering is deferred."""
    metadata, body = parse_frontmatter(source_skill / "SKILL.md")
    content = (
        "---\n"
        f"description: {metadata['description']}\n"
        "alwaysApply: false\n"
        "---\n"
        f"{OWNERSHIP_HEADER}\n"
        f"{normalize_newlines(body)}"
    )
    atomic_write_text(destination, content)


def _validate_sources(root: Path) -> list[Path]:
    catalog_root = root / _CANONICAL_SKILLS
    result = validate_catalog(catalog_root)
    errors = [issue for issue in result.issues if issue.severity == "error"]
    if errors:
        diagnostics = "\n".join(str(issue) for issue in errors)
        raise BuildValidationError(f"canonical catalog validation failed:\n{diagnostics}")
    return sorted(catalog_root.rglob("SKILL.md"))


def build_repository(root: Path) -> BuildResult:
    """Validate canonical sources, then regenerate only declared output subtrees."""
    root = Path(root).resolve()
    skill_paths = _validate_sources(root)

    for relative_path in _MANAGED_SUBTREES:
        _clear_managed_subtree(root, relative_path)

    for source_skill_file in skill_paths:
        source_skill = source_skill_file.parent
        name = source_skill.name
        _copy_skill_tree(source_skill, root / "generated-skills" / name)
        _copy_skill_tree(source_skill, root / "plugins/bbva-odissey/skills" / name)
        _write_cursor_rule(source_skill, root / ".cursor/rules" / f"{name}.mdc")

    return BuildResult(root=root, skill_count=len(skill_paths))


def main(arguments: Sequence[str] | None = None) -> int:
    """Run the portable build CLI."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).parents[1])
    options = parser.parse_args(arguments)
    try:
        result = build_repository(options.root)
    except (BuildSafetyError, BuildValidationError) as error:
        print(error)
        return 1
    print(f"Built {result.skill_count} skills from {result.root / _CANONICAL_SKILLS}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
