"""Pure parsing and link-validation helpers for Odissey artifacts."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Mapping
from urllib.parse import unquote, urlsplit


_ALLOWED_FIELDS = {"name", "description"}
_FRONTMATTER_FIELD = re.compile(r"(?P<key>[A-Za-z][A-Za-z0-9_-]*):(?: (?P<value>.*))?$")
_MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]*\]\((?P<target>[^)\s]+)(?:\s+[^)]*)?\)")


@dataclass(frozen=True)
class ValidationIssue:
    """An actionable validation problem tied to a source location."""

    path: Path
    line: int
    message: str

    def __str__(self) -> str:
        return f"{self.path}:{self.line}: {self.message}"


def _error(path: Path, line: int, message: str) -> ValueError:
    return ValueError(f"{path}:{line}: {message}")


def parse_frontmatter(path: Path) -> tuple[dict[str, str], str]:
    """Return supported SKILL.md metadata and its remaining Markdown body.

    The intentionally small YAML subset accepts scalar values and the folded
    ``>`` form for descriptions.  Every malformed construct identifies its
    source file and line.
    """
    path = Path(path)
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    if not lines or lines[0].rstrip("\r\n") != "---":
        raise _error(path, 1, "frontmatter must start with a delimiter")

    metadata: dict[str, str] = {}
    index = 1
    while index < len(lines):
        raw_line = lines[index]
        line = raw_line.rstrip("\r\n")
        line_number = index + 1
        if line == "---":
            missing = _ALLOWED_FIELDS - set(metadata)
            if missing:
                raise _error(
                    path,
                    line_number,
                    f"missing frontmatter fields: {', '.join(sorted(missing))}",
                )
            return metadata, "".join(lines[index + 1 :])

        field = _FRONTMATTER_FIELD.fullmatch(line)
        if field is None:
            raise _error(path, line_number, "unsupported frontmatter syntax")
        key = field.group("key")
        value = field.group("value")
        if key not in _ALLOWED_FIELDS:
            raise _error(path, line_number, f"unsupported frontmatter field '{key}'")
        if key in metadata:
            raise _error(path, line_number, f"duplicate frontmatter field '{key}'")
        if value is None or value == "":
            raise _error(path, line_number, f"missing value for '{key}'")

        if value == ">":
            if key != "description":
                raise _error(path, line_number, "only description may use folded text")
            folded_lines: list[str] = []
            index += 1
            while index < len(lines):
                folded_line = lines[index].rstrip("\r\n")
                if folded_line == "---":
                    break
                if not folded_line.startswith((" ", "\t")):
                    raise _error(path, index + 1, "folded text must be indented")
                folded_lines.append(folded_line.strip())
                index += 1
            if not folded_lines:
                raise _error(path, line_number, "folded description must not be empty")
            metadata[key] = " ".join(folded_lines)
            continue

        metadata[key] = value
        index += 1

    raise _error(path, len(lines), "frontmatter is missing its closing delimiter")


def render_frontmatter(metadata: Mapping[str, str], body: str) -> str:
    """Render the repository's supported metadata subset and Markdown body."""
    keys = set(metadata)
    unsupported = keys - _ALLOWED_FIELDS
    if unsupported:
        raise ValueError(f"unsupported frontmatter field '{sorted(unsupported)[0]}'")
    missing = _ALLOWED_FIELDS - keys
    if missing:
        raise ValueError(f"missing frontmatter field '{sorted(missing)[0]}'")
    if any("\n" in str(metadata[key]) for key in _ALLOWED_FIELDS):
        raise ValueError("rendered frontmatter values must be scalar")
    return (
        "---\n"
        f"name: {metadata['name']}\n"
        f"description: {metadata['description']}\n"
        "---\n"
        f"{body}"
    )


def _relative_target(target: str) -> str | None:
    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc or target.startswith(("/", "#")):
        return None
    if not parsed.path:
        return None
    return unquote(parsed.path)


def relative_markdown_links(path: Path, body: str) -> list[tuple[int, Path]]:
    """Resolve local Markdown link targets relative to ``path``'s directory."""
    path = Path(path)
    links: list[tuple[int, Path]] = []
    for line_number, line in enumerate(body.splitlines(), start=1):
        for match in _MARKDOWN_LINK.finditer(line):
            target = _relative_target(match.group("target"))
            if target is not None:
                links.append((line_number, path.parent / target))
    return links


def validate_relative_links(path: Path, body: str) -> list[ValidationIssue]:
    """Report Markdown links whose local target does not exist."""
    issues: list[ValidationIssue] = []
    for line_number, target in relative_markdown_links(path, body):
        if not target.exists():
            issues.append(
                ValidationIssue(path, line_number, f"relative link does not exist: {target}")
            )
    return issues
