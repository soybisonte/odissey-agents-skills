"""Build safe, deterministic Odissey distributions from canonical skills."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import os
from pathlib import Path
import shutil
import tempfile
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


@dataclass(frozen=True)
class PlannedOutput:
    """Fully rendered contents for one atomically replaceable output subtree."""

    relative_path: Path
    files: tuple[tuple[Path, str], ...]


def _managed_path(root: Path, relative_path: Path) -> Path:
    """Resolve a declared output subtree without granting parent-directory ownership."""
    if relative_path not in _MANAGED_SUBTREES:
        raise BuildSafetyError(f"not a managed output subtree: {relative_path}")
    target = root
    for component in relative_path.parts:
        target = target / component
        if target.is_symlink():
            raise BuildSafetyError(f"managed output contains a symlink: {target}")
    return root / relative_path


def _owned_skill_text(source: Path, text: str) -> str:
    """Insert the ownership marker after frontmatter so generated skills stay valid."""
    lines = normalize_newlines(text).splitlines(keepends=True)
    delimiters = [index for index, line in enumerate(lines) if line.rstrip("\n") == "---"]
    if len(delimiters) < 2:  # Validation is completed before this function is reached.
        raise BuildValidationError(f"cannot add ownership header to invalid skill: {source}")
    insert_at = delimiters[1] + 1
    return "".join([*lines[:insert_at], f"{OWNERSHIP_HEADER}\n", *lines[insert_at:]])


def _cursor_rule_text(source_skill: Path) -> str:
    """Produce a minimal owned Cursor rule; richer platform rendering is deferred."""
    metadata, body = parse_frontmatter(source_skill / "SKILL.md")
    return (
        "---\n"
        f"description: {metadata['description']}\n"
        "alwaysApply: false\n"
        "---\n"
        f"{OWNERSHIP_HEADER}\n"
        f"{normalize_newlines(body)}"
    )


def _validate_sources(root: Path) -> list[Path]:
    catalog_root = root / _CANONICAL_SKILLS
    result = validate_catalog(catalog_root)
    errors = [issue for issue in result.issues if issue.severity == "error"]
    if errors:
        diagnostics = "\n".join(str(issue) for issue in errors)
        raise BuildValidationError(f"canonical catalog validation failed:\n{diagnostics}")
    return sorted(catalog_root.rglob("SKILL.md"))


def _read_skill_tree(source_skill: Path) -> tuple[tuple[Path, str], ...]:
    """Pre-read every file the build will render before changing an output tree."""
    files: list[tuple[Path, str]] = []
    for source in sorted(source_skill.rglob("*")):
        if not source.is_file():
            continue
        try:
            text = source.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as error:
            raise BuildValidationError(f"cannot read source file {source}: {error}") from error
        files.append((source.relative_to(source_skill), text))
    return tuple(files)


def _plan_outputs(skill_paths: list[Path]) -> tuple[PlannedOutput, ...]:
    """Read and render all generated content before staging begins."""
    planned_files: dict[Path, list[tuple[Path, str]]] = {
        relative_path: [] for relative_path in _MANAGED_SUBTREES
    }
    for source_skill_file in skill_paths:
        source_skill = source_skill_file.parent
        name = source_skill.name
        for relative_file, text in _read_skill_tree(source_skill):
            content = (
                _owned_skill_text(source_skill / relative_file, text)
                if relative_file == Path("SKILL.md")
                else f"{OWNERSHIP_HEADER}\n{normalize_newlines(text)}"
            )
            planned_files[Path("generated-skills")].append((Path(name) / relative_file, content))
            planned_files[Path("plugins/bbva-odissey/skills")].append(
                (Path(name) / relative_file, content)
            )
        planned_files[Path(".cursor/rules")].append(
            (Path(f"{name}.mdc"), _cursor_rule_text(source_skill))
        )
    return tuple(
        PlannedOutput(relative_path, tuple(sorted(files)))
        for relative_path, files in planned_files.items()
    )


def _stage_outputs(
    root: Path, planned_outputs: tuple[PlannedOutput, ...]
) -> tuple[Path, tuple[Path, ...]]:
    """Write complete replacement trees without disturbing live distributions."""
    stage_root = Path(tempfile.mkdtemp(prefix=".odissey-build-", dir=root))
    staged_paths: list[Path] = []
    try:
        for index, output in enumerate(planned_outputs):
            stage_path = stage_root / f"output-{index}"
            stage_path.mkdir()
            for relative_file, content in output.files:
                atomic_write_text(stage_path / relative_file, content)
            staged_paths.append(stage_path)
    except BaseException:
        shutil.rmtree(stage_root, ignore_errors=True)
        raise
    return stage_root, tuple(staged_paths)


def _remove_staged_or_live_tree(path: Path) -> None:
    """Remove a directory created by this build while rolling back a failed swap."""
    if path.exists():
        shutil.rmtree(path)


def _replace_staged_outputs(
    root: Path,
    stage_root: Path,
    planned_outputs: tuple[PlannedOutput, ...],
    staged_paths: tuple[Path, ...],
) -> None:
    """Swap staged directories into place and restore all prior trees on failure."""
    backup_root = stage_root / "previous"
    backup_root.mkdir()
    completed: list[tuple[Path, Path | None]] = []
    try:
        for index, (output, staged_path) in enumerate(
            zip(planned_outputs, staged_paths, strict=True)
        ):
            target = _managed_path(root, output.relative_path)
            target.parent.mkdir(parents=True, exist_ok=True)
            backup_path = backup_root / f"output-{index}"
            had_previous = target.exists()
            if had_previous:
                os.replace(target, backup_path)
            try:
                os.replace(staged_path, target)
            except BaseException:
                if had_previous:
                    os.replace(backup_path, target)
                raise
            completed.append((target, backup_path if had_previous else None))
    except BaseException:
        for target, backup_path in reversed(completed):
            _remove_staged_or_live_tree(target)
            if backup_path is not None and backup_path.exists():
                os.replace(backup_path, target)
        raise
    finally:
        shutil.rmtree(stage_root, ignore_errors=True)


def build_repository(root: Path) -> BuildResult:
    """Validate canonical sources, then regenerate only declared output subtrees."""
    root = Path(root).resolve()
    skill_paths = _validate_sources(root)
    for relative_path in _MANAGED_SUBTREES:
        _managed_path(root, relative_path)
    planned_outputs = _plan_outputs(skill_paths)
    stage_root, staged_paths = _stage_outputs(root, planned_outputs)
    _replace_staged_outputs(root, stage_root, planned_outputs, staged_paths)

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
