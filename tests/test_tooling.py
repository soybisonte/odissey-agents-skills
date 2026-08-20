"""Contract tests for the dependency-free tooling primitives."""

from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from scripts.build import (
    OWNERSHIP_HEADER,
    BuildSafetyError,
    BuildValidationError,
    build_repository,
)
from scripts.odissey_tooling import (
    ValidationIssue,
    parse_frontmatter,
    relative_markdown_links,
    render_frontmatter,
    validate_relative_links,
)
from scripts.validate import validate_catalog, validate_skill


class FrontmatterTests(unittest.TestCase):
    """Frontmatter parsing and relative Markdown link contracts."""

    def write_skill(self, directory: Path, content: str) -> Path:
        skill_path = directory / "example" / "SKILL.md"
        skill_path.parent.mkdir()
        skill_path.write_text(content, encoding="utf-8")
        return skill_path

    def test_parses_valid_skill_metadata_and_body(self) -> None:
        """Removing a supported metadata field must make this test fail."""
        with TemporaryDirectory() as temporary_directory:
            skill_path = self.write_skill(
                Path(temporary_directory),
                "---\nname: example\ndescription: A valid skill.\n---\n\n# Body\n",
            )

            metadata, body = parse_frontmatter(skill_path)

        self.assertEqual(
            {"name": "example", "description": "A valid skill."}, metadata
        )
        self.assertEqual("\n# Body\n", body)

    def test_rejects_frontmatter_without_closing_delimiter(self) -> None:
        """Accepting an unterminated header would make this test fail."""
        with TemporaryDirectory() as temporary_directory:
            skill_path = self.write_skill(
                Path(temporary_directory), "---\nname: example\ndescription: Missing end\n"
            )

            with self.assertRaisesRegex(ValueError, r"SKILL\.md:3:.*delimiter"):
                parse_frontmatter(skill_path)

    def test_rejects_unsupported_frontmatter_fields(self) -> None:
        """Silently accepting arbitrary metadata would make this test fail."""
        with TemporaryDirectory() as temporary_directory:
            skill_path = self.write_skill(
                Path(temporary_directory),
                "---\nname: example\ndescription: Valid\nlicense: MIT\n---\n",
            )

            with self.assertRaisesRegex(ValueError, r"SKILL\.md:4:.*license"):
                parse_frontmatter(skill_path)

    def test_rejects_frontmatter_without_name(self) -> None:
        """Accepting metadata without a skill name would make this test fail."""
        with TemporaryDirectory() as temporary_directory:
            skill_path = self.write_skill(
                Path(temporary_directory), "---\ndescription: Valid\n---\n"
            )

            with self.assertRaisesRegex(ValueError, r"SKILL\.md:3:.*name"):
                parse_frontmatter(skill_path)

    def test_rejects_frontmatter_without_description(self) -> None:
        """Accepting metadata without a description would make this test fail."""
        with TemporaryDirectory() as temporary_directory:
            skill_path = self.write_skill(Path(temporary_directory), "---\nname: example\n---\n")

            with self.assertRaisesRegex(ValueError, r"SKILL\.md:3:.*description"):
                parse_frontmatter(skill_path)

    def test_rejects_whitespace_only_description(self) -> None:
        """Treating whitespace as a description would make invalid metadata pass."""
        with TemporaryDirectory() as temporary_directory:
            skill_path = self.write_skill(
                Path(temporary_directory), "---\nname: example\ndescription:   \n---\n"
            )

            with self.assertRaisesRegex(ValueError, r"SKILL\.md:3:.*description"):
                parse_frontmatter(skill_path)

    def test_rejects_empty_frontmatter(self) -> None:
        """Accepting an empty metadata block would make this test fail."""
        with TemporaryDirectory() as temporary_directory:
            skill_path = self.write_skill(Path(temporary_directory), "---\n---\n")

            with self.assertRaisesRegex(ValueError, r"SKILL\.md:2:.*name"):
                parse_frontmatter(skill_path)

    def test_parses_scalar_and_folded_descriptions(self) -> None:
        """Ignoring a supported YAML description shape would make this test fail."""
        with TemporaryDirectory() as temporary_directory:
            directory = Path(temporary_directory)
            scalar_path = self.write_skill(
                directory,
                "---\nname: example\ndescription: Scalar description\n---\n",
            )
            folded_path = directory / "folded" / "SKILL.md"
            folded_path.parent.mkdir()
            folded_path.write_text(
                "---\nname: folded\ndescription: >\n  First line\n  second line\n---\n",
                encoding="utf-8",
            )

            scalar_metadata, _ = parse_frontmatter(scalar_path)
            folded_metadata, _ = parse_frontmatter(folded_path)

        self.assertEqual("Scalar description", scalar_metadata["description"])
        self.assertEqual("First line second line", folded_metadata["description"])

    def test_resolves_relative_markdown_links_and_reports_broken_ones(self) -> None:
        """Resolving links from another directory or hiding failures breaks this test."""
        with TemporaryDirectory() as temporary_directory:
            directory = Path(temporary_directory)
            skill_path = self.write_skill(directory, "---\nname: example\ndescription: Valid\n---\n")
            reference = skill_path.parent / "references" / "guide.md"
            reference.parent.mkdir()
            reference.write_text("Guide", encoding="utf-8")
            body = "[guide](references/guide.md)\n[missing](references/missing.md)\n[web](https://example.com)\n"

            links = relative_markdown_links(skill_path, body)
            issues = validate_relative_links(skill_path, body)

        self.assertEqual(
            [
                (1, reference),
                (2, skill_path.parent / "references" / "missing.md"),
            ],
            links,
        )
        self.assertEqual(1, len(issues))
        self.assertIsInstance(issues[0], ValidationIssue)
        self.assertEqual(skill_path, issues[0].path)
        self.assertEqual(2, issues[0].line)
        self.assertIn("references/missing.md", issues[0].message)

    def test_renders_supported_metadata_as_frontmatter(self) -> None:
        """Omitting a field or delimiter from rendered frontmatter breaks this test."""
        rendered = render_frontmatter(
            {"name": "example", "description": "A valid skill."}, "# Body\n"
        )

        self.assertEqual(
            "---\nname: example\ndescription: A valid skill.\n---\n# Body\n", rendered
        )


class CatalogValidationTests(unittest.TestCase):
    """Contracts for validating a canonical skill catalog."""

    def write_skill(self, root: Path, directory_name: str, metadata: str, body: str = "") -> Path:
        skill_path = root / directory_name / "SKILL.md"
        skill_path.parent.mkdir(parents=True)
        skill_path.write_text(f"---\n{metadata}---\n{body}", encoding="utf-8")
        return skill_path

    def issues_for(self, skill_path: Path) -> list[ValidationIssue]:
        return validate_skill(skill_path).issues

    def test_requires_directory_to_match_skill_name(self) -> None:
        """Dropping the folder/name comparison would let misplaced skills pass."""
        with TemporaryDirectory() as temporary_directory:
            skill_path = self.write_skill(
                Path(temporary_directory), "different-folder", "name: actual-name\ndescription: Valid\n"
            )

            issues = self.issues_for(skill_path)

        self.assertTrue(any(issue.rule == "directory-name" for issue in issues))
        issue = next(issue for issue in issues if issue.rule == "directory-name")
        self.assertEqual(skill_path, issue.path)
        self.assertIn("actual-name", issue.message)
        self.assertIn("different-folder", issue.remediation)

    def test_requires_lowercase_hyphenated_skill_names(self) -> None:
        """Allowing uppercase letters or underscores would make invalid IDs pass."""
        with TemporaryDirectory() as temporary_directory:
            skill_path = self.write_skill(
                Path(temporary_directory), "Bad_Name", "name: Bad_Name\ndescription: Valid\n"
            )

            issues = self.issues_for(skill_path)

        self.assertTrue(any(issue.rule == "skill-name-format" for issue in issues))

    def test_enforces_description_length_and_reports_long_description_warning(self) -> None:
        """Removing either description boundary would hide an authoring error or warning."""
        with TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            warning_path = self.write_skill(
                root, "warning", f"name: warning\ndescription: {'a' * 501}\n"
            )
            error_path = self.write_skill(
                root, "error", f"name: error\ndescription: {'b' * 1025}\n"
            )

            warning_issues = self.issues_for(warning_path)
            error_issues = self.issues_for(error_path)

        self.assertTrue(
            any(
                issue.rule == "description-length" and issue.severity == "warning"
                for issue in warning_issues
            )
        )
        self.assertTrue(
            any(
                issue.rule == "description-length" and issue.severity == "error"
                for issue in error_issues
            )
        )

    def test_rejects_empty_descriptions_and_extra_frontmatter_fields(self) -> None:
        """Accepting empty descriptions or arbitrary metadata would corrupt the manifest."""
        with TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            empty_path = self.write_skill(root, "empty", "name: empty\ndescription: \n")
            extra_path = self.write_skill(
                root, "extra", "name: extra\ndescription: Valid\nlicense: MIT\n"
            )

            empty_issues = self.issues_for(empty_path)
            extra_issues = self.issues_for(extra_path)

        self.assertTrue(any(issue.rule == "description-required" for issue in empty_issues))
        self.assertTrue(any(issue.rule == "frontmatter-fields" for issue in extra_issues))

    def test_reports_broken_relative_links_with_remediation(self) -> None:
        """Ignoring local Markdown targets would let broken skill references ship."""
        with TemporaryDirectory() as temporary_directory:
            skill_path = self.write_skill(
                Path(temporary_directory),
                "links",
                "name: links\ndescription: Valid\n",
                "Read [the guide](references/missing.md).\n",
            )

            issues = self.issues_for(skill_path)

        issue = next(issue for issue in issues if issue.rule == "relative-link")
        self.assertEqual(1, issue.line)
        self.assertIn("references/missing.md", issue.message)
        self.assertIn("Create", issue.remediation)

    def test_rejects_nonportable_source_references_and_commands(self) -> None:
        """Removing portability checks would allow host-specific source coupling."""
        with TemporaryDirectory() as temporary_directory:
            skill_path = self.write_skill(
                Path(temporary_directory),
                "portable",
                "name: portable\ndescription: Valid\n",
                ".github/copilot/skills\nmcp__claude\nmcp__figma\nmcp__pencil\n/strategy\n/research\n/blueprint\n/journey\n/organizar\n/articular\n/evaluar\n/robustecer\n/incluir\n/trasponer\n/localizar\n/medir\n/idear\n/spec\n/storytelling\n/odissey\n",
            )

            issues = self.issues_for(skill_path)

        rules = {issue.rule for issue in issues}
        self.assertEqual(
            {"copilot-source", "mcp-name", "legacy-command"}, rules
        )
        self.assertTrue(all(issue.remediation for issue in issues))

    def test_reports_aggregate_description_budget_for_catalog(self) -> None:
        """Omitting the aggregate would hide catalog-level metadata growth."""
        with TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            self.write_skill(root, "first", "name: first\ndescription: alpha\n")
            self.write_skill(root, "second", "name: second\ndescription: bravo\n")

            result = validate_catalog(root)

        self.assertEqual(2, result.skill_count)
        self.assertEqual(10, result.description_characters)
        self.assertEqual([], result.issues)

    def test_cli_reports_a_missing_catalog_root_as_an_error(self) -> None:
        """Treating a missing root as an empty catalog would hide a broken invocation."""
        with TemporaryDirectory() as temporary_directory:
            missing_root = Path(temporary_directory) / "missing-catalog"
            completed = subprocess.run(
                [
                    sys.executable,
                    "scripts/validate.py",
                    "--root",
                    str(missing_root),
                    "--format",
                    "json",
                ],
                cwd=Path(__file__).parents[1],
                check=False,
                capture_output=True,
                text=True,
            )

        self.assertEqual(1, completed.returncode)
        self.assertIn('"rule": "catalog-root"', completed.stdout)
        self.assertIn(str(missing_root), completed.stdout)

    def test_cli_supports_json_and_treats_warnings_as_errors_on_request(self) -> None:
        """Ignoring CLI format or warning policy would make automation unreliable."""
        with TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            self.write_skill(root, "warning", f"name: warning\ndescription: {'a' * 501}\n")

            command = [
                sys.executable,
                "scripts/validate.py",
                "--root",
                str(root),
                "--format",
                "json",
                "--warnings-as-errors",
            ]
            completed = subprocess.run(
                command,
                cwd=Path(__file__).parents[1],
                check=False,
                capture_output=True,
                text=True,
            )

        self.assertEqual(1, completed.returncode)
        self.assertIn('"description_characters": 501', completed.stdout)
        self.assertIn('"severity": "warning"', completed.stdout)


class BuildTests(unittest.TestCase):
    """Filesystem contracts for the safe, deterministic catalog build."""

    def write_skill(self, root: Path, name: str, body: str = "# Skill\n") -> Path:
        """Create one valid canonical source skill with deliberately mixed newlines."""
        skill_path = root / ".agents" / "skills" / name / "SKILL.md"
        skill_path.parent.mkdir(parents=True)
        skill_path.write_bytes(
            f"---\r\nname: {name}\r\ndescription: {name} description\r\n---\r\n{body}".encode(
                "utf-8"
            )
        )
        return skill_path

    def snapshot(self, root: Path) -> dict[Path, bytes]:
        """Read all generated files so idempotence is tested as bytes on disk."""
        output_roots = (
            root / ".codex" / "agents",
            root / ".github" / "agents",
            root / "generated-skills",
            root / "plugins" / "bbva-odissey" / "skills",
            root / ".cursor" / "rules",
        )
        return {
            path.relative_to(root): path.read_bytes()
            for output_root in output_roots
            if output_root.exists()
            for path in sorted(output_root.rglob("*"))
            if path.is_file()
        }

    def test_build_preserves_unmanaged_github_files_and_creates_output_roots(self) -> None:
        """Deleting .github or skipping an output root would make this test fail."""
        with TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            self.write_skill(root, "alpha")
            workflow = root / ".github" / "workflows" / "ci.yml"
            keep = root / ".github" / "keep.md"
            workflow.parent.mkdir(parents=True)
            workflow.write_text("name: CI\n", encoding="utf-8")
            keep.write_text("keep me\n", encoding="utf-8")

            build_repository(root)

            self.assertEqual("name: CI\n", workflow.read_text(encoding="utf-8"))
            self.assertEqual("keep me\n", keep.read_text(encoding="utf-8"))
            for relative_path in (
                ".codex/agents",
                ".github/agents",
                "generated-skills",
                "plugins/bbva-odissey/skills",
                ".cursor/rules",
            ):
                self.assertTrue((root / relative_path).is_dir(), relative_path)
            self.assertTrue((root / "generated-skills" / "alpha" / "SKILL.md").is_file())
            self.assertTrue(
                (root / "plugins" / "bbva-odissey" / "skills" / "alpha" / "SKILL.md").is_file()
            )

    def test_build_is_byte_idempotent_and_normalizes_newlines(self) -> None:
        """Nondeterministic ordering or newline preservation would make this test fail."""
        with TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            self.write_skill(root, "zeta")
            self.write_skill(root, "alpha", "# Alpha\r\n")

            build_repository(root)
            first = self.snapshot(root)
            build_repository(root)
            second = self.snapshot(root)

            self.assertEqual(first, second)
            generated = second[Path("generated-skills/alpha/SKILL.md")]
            self.assertNotIn(b"\r", generated)
            self.assertIn(OWNERSHIP_HEADER.encode("utf-8"), generated)

    def test_validation_failure_leaves_existing_outputs_unchanged(self) -> None:
        """Writing before validation completes would make this test fail."""
        with TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            self.write_skill(root, "valid")
            build_repository(root)
            before = self.snapshot(root)
            invalid = root / ".agents" / "skills" / "invalid" / "SKILL.md"
            invalid.parent.mkdir()
            invalid.write_text("---\nname: invalid\n---\n", encoding="utf-8")

            with self.assertRaises(BuildValidationError):
                build_repository(root)

            self.assertEqual(before, self.snapshot(root))

    def test_build_removes_only_managed_subtree_contents(self) -> None:
        """Removing an unowned sibling would make this ownership-safety test fail."""
        with TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            self.write_skill(root, "alpha")
            unmanaged = root / ".github" / "keep.md"
            managed_stale = root / ".github" / "agents" / "stale.agent.md"
            header_owned = root / ".github" / "obsolete.md"
            unmanaged.parent.mkdir(parents=True)
            managed_stale.parent.mkdir()
            unmanaged.write_text("user owned\n", encoding="utf-8")
            managed_stale.write_text("user content in managed subtree\n", encoding="utf-8")
            header_owned.write_text(f"{OWNERSHIP_HEADER}\nold output\n", encoding="utf-8")

            build_repository(root)

            self.assertTrue(unmanaged.exists())
            self.assertFalse(managed_stale.exists())
            self.assertTrue(header_owned.exists())

    def test_build_rejects_symlinked_managed_output_parent_without_touching_target(self) -> None:
        """Following a symlinked .github parent would make this test fail."""
        with TemporaryDirectory() as repository_directory, TemporaryDirectory() as target_directory:
            root = Path(repository_directory)
            external_target = Path(target_directory)
            self.write_skill(root, "alpha")
            sentinel = external_target / "agents" / "preserve.txt"
            sentinel.parent.mkdir()
            sentinel.write_text("external user data\n", encoding="utf-8")
            (root / ".github").symlink_to(external_target, target_is_directory=True)

            with self.assertRaises(BuildSafetyError):
                build_repository(root)

            self.assertEqual("external user data\n", sentinel.read_text(encoding="utf-8"))
            self.assertFalse((root / ".codex" / "agents").exists())

    def test_invalid_utf8_auxiliary_source_leaves_outputs_unchanged(self) -> None:
        """Decoding an auxiliary file after cleanup would make this test fail."""
        with TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            skill = self.write_skill(root, "alpha")
            build_repository(root)
            before = self.snapshot(root)
            auxiliary = skill.parent / "references" / "broken.md"
            auxiliary.parent.mkdir()
            auxiliary.write_bytes(b"\xff\xfe")

            with self.assertRaises(BuildValidationError):
                build_repository(root)

            self.assertEqual(before, self.snapshot(root))

    def test_operational_write_failure_leaves_previous_distribution_unchanged(self) -> None:
        """Replacing outputs before a write completes would make this test fail."""
        with TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            self.write_skill(root, "alpha")
            build_repository(root)
            before = self.snapshot(root)

            with patch("scripts.build.atomic_write_text", side_effect=OSError("disk full")):
                with self.assertRaisesRegex(OSError, "disk full"):
                    build_repository(root)

            self.assertEqual(before, self.snapshot(root))
