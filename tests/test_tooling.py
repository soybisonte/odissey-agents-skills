"""Contract tests for the dependency-free tooling primitives."""

from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from scripts.odissey_tooling import (
    ValidationIssue,
    parse_frontmatter,
    relative_markdown_links,
    render_frontmatter,
    validate_relative_links,
)


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
