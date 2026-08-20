"""Validate a portable, canonical Odissey skill catalog."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
from typing import Sequence

if __package__:
    from scripts.odissey_tooling import (
        CatalogValidationResult,
        SkillValidationResult,
        ValidationIssue,
        parse_frontmatter,
        validate_relative_links,
    )
else:  # pragma: no cover - exercised by the direct CLI invocation.
    from odissey_tooling import (
        CatalogValidationResult,
        SkillValidationResult,
        ValidationIssue,
        parse_frontmatter,
        validate_relative_links,
    )


_SKILL_NAME = re.compile(r"^[a-z0-9-]+$")
_MCP_NAMES = ("mcp__claude", "mcp__figma", "mcp__pencil")
_LEGACY_COMMANDS = (
    "strategy",
    "research",
    "blueprint",
    "journey",
    "organizar",
    "articular",
    "evaluar",
    "robustecer",
    "incluir",
    "trasponer",
    "localizar",
    "medir",
    "idear",
    "spec",
    "storytelling",
    "odissey",
)
_LEGACY_COMMAND = re.compile(r"(?<![A-Za-z0-9_])/(?:" + "|".join(_LEGACY_COMMANDS) + r")\b")
_ERROR_DESCRIPTION_LIMIT = 1024
_WARNING_DESCRIPTION_LIMIT = 500


def _issue(
    path: Path,
    line: int,
    message: str,
    *,
    rule: str,
    remediation: str,
    severity: str = "error",
) -> ValidationIssue:
    return ValidationIssue(
        path=path,
        line=line,
        message=message,
        severity=severity,
        rule=rule,
        remediation=remediation,
    )


def _error_line(error: ValueError) -> int:
    match = re.search(r":(\d+):", str(error))
    return int(match.group(1)) if match else 1


def _frontmatter_issue(path: Path, error: ValueError) -> ValidationIssue:
    message = str(error).rsplit(": ", maxsplit=1)[-1]
    if "description" in message:
        rule = "description-required"
        remediation = "Add a non-empty description field to the frontmatter."
    elif "unsupported frontmatter field" in message:
        rule = "frontmatter-fields"
        remediation = "Keep only the name and description frontmatter fields."
    else:
        rule = "frontmatter"
        remediation = "Use a complete frontmatter block with name and description fields."
    return _issue(path, _error_line(error), message, rule=rule, remediation=remediation)


def _source_portability_issues(path: Path) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if ".github/copilot/skills" in line:
            issues.append(
                _issue(
                    path,
                    line_number,
                    "canonical sources must not reference .github/copilot/skills",
                    rule="copilot-source",
                    remediation="Replace the Copilot-specific path with a portable local reference.",
                )
            )
        for name in _MCP_NAMES:
            if name in line:
                issues.append(
                    _issue(
                        path,
                        line_number,
                        f"canonical sources must not reference MCP name '{name}'",
                        rule="mcp-name",
                        remediation="Remove the host-specific MCP name or describe the capability generically.",
                    )
                )
        for match in _LEGACY_COMMAND.finditer(line):
            issues.append(
                _issue(
                    path,
                    line_number,
                    f"canonical sources must not invoke legacy command '{match.group(0)}'",
                    rule="legacy-command",
                    remediation="Replace the slash command with a portable skill reference or plain-language instruction.",
                )
            )
    return issues


def validate_skill(path: Path) -> SkillValidationResult:
    """Validate one skill source and return all actionable diagnostics."""
    path = Path(path)
    try:
        metadata, body = parse_frontmatter(path)
    except ValueError as error:
        return SkillValidationResult(
            path=path,
            description_characters=0,
            issues=[_frontmatter_issue(path, error), *_source_portability_issues(path)],
        )

    issues: list[ValidationIssue] = _source_portability_issues(path)
    name = metadata["name"]
    description = metadata["description"]
    if path.parent.name != name:
        issues.append(
            _issue(
                path,
                2,
                f"skill name '{name}' must match directory '{path.parent.name}'",
                rule="directory-name",
                remediation=f"Rename the directory to '{name}' or set name to '{path.parent.name}'.",
            )
        )
    if not _SKILL_NAME.fullmatch(name):
        issues.append(
            _issue(
                path,
                2,
                f"skill name '{name}' must use only lowercase letters, digits, and hyphens",
                rule="skill-name-format",
                remediation="Use a lowercase, hyphen-separated skill name.",
            )
        )

    description_length = len(description)
    if description_length > _ERROR_DESCRIPTION_LIMIT:
        issues.append(
            _issue(
                path,
                3,
                f"description is {description_length} characters; maximum is {_ERROR_DESCRIPTION_LIMIT}",
                rule="description-length",
                remediation=f"Shorten the description to at most {_ERROR_DESCRIPTION_LIMIT} characters.",
            )
        )
    elif description_length > _WARNING_DESCRIPTION_LIMIT:
        issues.append(
            _issue(
                path,
                3,
                f"description is {description_length} characters; consider staying at or below {_WARNING_DESCRIPTION_LIMIT}",
                severity="warning",
                rule="description-length",
                remediation="Shorten the description to reduce the catalog metadata budget.",
            )
        )

    for link_issue in validate_relative_links(path, body):
        issues.append(
            _issue(
                path,
                link_issue.line,
                link_issue.message,
                rule="relative-link",
                remediation="Create the target file or update the link to an existing relative target.",
            )
        )
    return SkillValidationResult(path, description_length, issues)


def validate_catalog(root: Path) -> CatalogValidationResult:
    """Validate every ``SKILL.md`` under a catalog root."""
    root = Path(root)
    if not root.is_dir():
        message = (
            f"catalog root does not exist: {root}"
            if not root.exists()
            else f"catalog root is not a directory: {root}"
        )
        return CatalogValidationResult(
            root=root,
            skill_count=0,
            description_characters=0,
            issues=[
                _issue(
                    root,
                    1,
                    message,
                    rule="catalog-root",
                    remediation="Create the canonical catalog directory or pass an existing directory with --root.",
                )
            ],
        )

    skill_paths = sorted(root.rglob("SKILL.md"))
    results = [validate_skill(path) for path in skill_paths]
    return CatalogValidationResult(
        root=root,
        skill_count=len(results),
        description_characters=sum(result.description_characters for result in results),
        issues=[issue for result in results for issue in result.issues],
    )


def _result_data(result: CatalogValidationResult) -> dict[str, object]:
    return {
        "root": str(result.root),
        "skill_count": result.skill_count,
        "description_characters": result.description_characters,
        "issues": [
            {
                "path": str(issue.path),
                "line": issue.line,
                "severity": issue.severity,
                "rule": issue.rule,
                "message": issue.message,
                "remediation": issue.remediation,
            }
            for issue in result.issues
        ],
    }


def _text_result(result: CatalogValidationResult) -> str:
    lines = [str(issue) for issue in result.issues]
    lines.append(
        f"Description budget: {result.description_characters} characters across {result.skill_count} skills."
    )
    return "\n".join(lines)


def main(arguments: Sequence[str] | None = None) -> int:
    """Run catalog validation and return a shell-compatible status code."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(".agents/skills"))
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--warnings-as-errors", action="store_true")
    options = parser.parse_args(arguments)

    result = validate_catalog(options.root)
    if options.format == "json":
        print(json.dumps(_result_data(result), indent=2, sort_keys=True))
    else:
        print(_text_result(result))

    has_error = any(issue.severity == "error" for issue in result.issues)
    has_warning = any(issue.severity == "warning" for issue in result.issues)
    return int(has_error or (options.warnings_as_errors and has_warning))


if __name__ == "__main__":
    raise SystemExit(main())
