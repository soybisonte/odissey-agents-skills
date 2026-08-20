"""Quality contracts for the canonical Odissey reference guides."""

from pathlib import Path
import re
import unicodedata
import unittest


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
REFERENCE_DIRECTORY = REPOSITORY_ROOT / ".agents" / "skills" / "odissey" / "references"

EXPECTED_GUIDES = (
    "arquitectura-informacion.md",
    "diseno-etico.md",
    "diseno-servicios.md",
    "estrategia-contenido.md",
    "fundamentos-accesibilidad.md",
    "marcos-medicion.md",
    "metodos-investigacion.md",
    "patrones-interaccion.md",
)

CORRUPTED_SUBSTITUTION_TOKEN = re.compile(
    r"\b(?:"
    r"mesgalileos?|"
    r"medirments?|"
    r"organizards?|"
    r"odisseyionals?|"
    r"rempathfindereds?|"
    r"ugalileos?"
    r")\b",
    re.IGNORECASE,
)

# Exact headings observed in the baseline. Exact matching keeps this conservative:
# it catches the known untranslated prose without guessing from product names,
# standards, acronyms, or citations that may legitimately remain in English.
KNOWN_ENGLISH_HEADINGS = {
    "A/B Test Design",
    "Accessibility Foundations",
    "Addictive Design → Respectful Engagement",
    "Affinity Mapping",
    "Aging",
    "Anti-Pattern Remediation Guide",
    "Anti-Patterns in Progressive Disclosure",
    "Applied Mental Model Theory",
    "Applying HEART by Feature Type",
    "Assistive Technology Landscape",
    "Bias Avoidance in Research",
    "Building a Terminology Glossary",
    "Button States",
    "Card Sort and Tree Test Methodology",
    "Channel Orchestration",
    "Cognitive Accessibility",
    "Common Communication Failures",
    "Common GSM Mistakes",
    "Common consent failures",
    "Communicating Findings",
    "Confidence Intervals",
    "Consent Design Patterns",
    "Consent interface patterns",
    "Consistent Patterns",
    "Content Modeling",
    "Content Reuse",
    "Content Strategy",
    "Core Wayfinding Principles",
    "Cross-Channel Consistency",
    "Dashboard",
    "Deceptive Patterns → Honest Alternatives",
    "Default Manipulation → Respectful Defaults",
    "Design Ethics Frameworks",
    "Design Principles for Undo",
    "Designing for Moments of Truth",
    "Destructive Action Safeguards",
    "Don't-Know-What-I-Don't-Know",
    "Effect Size",
    "Empty States",
    "Engagement vs. Wellbeing",
    "Error Prevention",
    "Ethical Design",
    "Ethical Measurement",
    "Ethical Measurement Principles",
    "Evaluative Methods (Is this working?)",
    "Evidence Strength Indicators",
    "Exploratory Search",
    "Faceted",
    "Fail Point Categories",
    "Fail Point Identification and Recovery Design",
    "Feedback Loops",
    "Field Grouping",
    "Findings Format",
    "Flat",
    "Focus Management",
    "Form Design Principles",
    "Form Field States",
    "Friction Hierarchy",
    "GSM Example: Search Feature",
    "Generative Methods (What should we build?)",
    "Goal-Signal-Metric (GSM) Mapping",
    "HEART Framework",
    "Hierarchical (Tree)",
    "Hub-and-Spoke",
    "Hypothesis Structure",
    "Identifying Moments of Truth",
    "Implementation Approaches",
    "In analysis",
    "In question design",
    "In sampling",
    "Inclusive Design Beyond Disability",
    "Information Architecture",
    "Inline Validation Timing",
    "Interaction Patterns",
    "Jargon Management",
    "Journey-Based Synthesis",
    "Keyboard Navigation Design",
    "Keyboard Patterns for Custom Components",
    "Known-Item Search",
    "Landmarks",
    "Live Regions",
    "Localization-Ready Content",
    "Low Literacy",
    "Lynch's Spatial Elements",
    "MECE Principle",
    "Magnification",
    "Measurement Frameworks",
    "Mental Models",
    "Method Selection Matrix",
    "Microcopy Pattern Library",
    "Minimum Detectable Effect (MDE)",
    "Modern Blueprint Layers",
    "Moment-of-Truth Analysis",
    "Moment-of-Truth Categories",
    "Naming Conventions",
    "Navigation Patterns",
    "Older Devices and Low Bandwidth",
    "One Thing Per Page",
    "Operable",
    "Optimistic UI",
    "Orchestration Design Principles",
    "Orchestration Patterns",
    "Patterns",
    "Perceivable",
    "Placeholder Text",
    "Plain Language",
    "Plain Language Principles",
    "Polyhierarchy",
    "Principles of meaningful consent",
    "Progress Indicators",
    "Progressive Disclosure",
    "Re-finding",
    "Readability Scoring",
    "Readability and Plain Language",
    "Reading Order",
    "Recovery Design Principles",
    "Regulatory Landscape",
    "Research Methods",
    "Robust",
    "Running a Card Sort",
    "Running a Tree Test",
    "Safeguard Design Principles",
    "Sample Size",
    "Screen Reader Flow Design",
    "Screen Readers",
    "Search Behavior Models",
    "Service Blueprinting Methodology",
    "Service Design",
    "Simplify Processes",
    "Situational Impairment",
    "Skeleton Screens",
    "Smart Defaults",
    "State Machines for UI",
    "Statistical Literacy for Designers",
    "Statistical Significance",
    "Step 1: Brand Attribute Identification",
    "Step 2: Voice Principles",
    "Step 3: Tone Spectrum",
    "Step 4: Writing Guidelines",
    "Structural Methods (How should we organizar this?)",
    "Structured Content",
    "Switch Access",
    "Synthesis Techniques",
    "Tab Order",
    "Taxonomy Design",
    "Terminology Governance",
    "Test Duration",
    "The Five Dimensions",
    "The Lines",
    "The Three Layers",
    "Tone Matrix",
    "Tooltips",
    "Top-Down vs. Bottom-Up",
    "Touchpoint Evaluation Matrix",
    "Touchpoint Inventory",
    "Touchpoint Mapping",
    "Undo/Redo Patterns",
    "Understandable",
    "Universal Component States",
    "Urgency Fabrication → Honest Scarcity",
    "Validation Patterns",
    "Voice Control",
    "Voice Framework Methodology",
    "WCAG 2.2 for Designers",
    "Wayfinding",
    "What A/B Tests Cannot Tell You",
    "When Metrics Incentivize Bad UX",
    "When to Validate",
}

HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$", re.MULTILINE)
LOCAL_MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(#[^)]+\)")


def normalized(text: str) -> str:
    """Return accent-insensitive lowercase text for prose-level assertions."""
    decomposed = unicodedata.normalize("NFKD", text)
    return "".join(
        character
        for character in decomposed
        if unicodedata.category(character) != "Mn"
    ).casefold()


class ReferenceQualityTests(unittest.TestCase):
    """Editorial and source-quality contracts for Odissey references."""

    def read_guide(self, filename: str) -> str:
        guide_path = REFERENCE_DIRECTORY / filename
        self.assertTrue(
            guide_path.is_file(),
            f"{filename}: required canonical reference guide is missing",
        )
        return guide_path.read_text(encoding="utf-8")

    def test_canonical_reference_inventory_is_exact(self) -> None:
        """Adding, removing, or renaming a canonical guide must fail discovery."""
        actual_guides = tuple(
            sorted(path.name for path in REFERENCE_DIRECTORY.glob("*.md"))
        )

        self.assertEqual(
            EXPECTED_GUIDES,
            actual_guides,
            ".agents/skills/odissey/references: expected exactly the eight "
            "canonical reference guides",
        )

    def test_long_guides_include_a_nearby_local_index(self) -> None:
        """Removing a long guide's early local index must fail navigation quality."""
        for filename in EXPECTED_GUIDES:
            with self.subTest(guide=filename):
                lines = self.read_guide(filename).splitlines()
                if len(lines) <= 100:
                    continue

                index_lines = [
                    line_number
                    for line_number, line in enumerate(lines)
                    if line.strip() == "## Índice"
                ]
                self.assertEqual(
                    1,
                    len(index_lines),
                    f"{filename}: guides longer than 100 lines must contain "
                    "exactly one '## Índice' section",
                )
                index_line = index_lines[0]
                self.assertLess(
                    index_line,
                    40,
                    f"{filename}: '## Índice' must appear within the first 40 lines",
                )

                next_section = next(
                    (
                        line_number
                        for line_number in range(index_line + 1, len(lines))
                        if lines[line_number].startswith("## ")
                    ),
                    len(lines),
                )
                index_body = "\n".join(lines[index_line + 1 : next_section])
                local_links = LOCAL_MARKDOWN_LINK.findall(index_body)
                self.assertGreaterEqual(
                    len(local_links),
                    3,
                    f"{filename}: '## Índice' must contain at least three "
                    "local Markdown links",
                )

    def test_guides_do_not_contain_corrupted_substitution_tokens(self) -> None:
        """Reintroducing any known corrupted token family must fail quality checks."""
        for filename in EXPECTED_GUIDES:
            with self.subTest(guide=filename):
                matches = sorted(
                    {
                        match.group(0)
                        for match in CORRUPTED_SUBSTITUTION_TOKEN.finditer(
                            self.read_guide(filename)
                        )
                    },
                    key=str.casefold,
                )
                self.assertEqual(
                    [],
                    matches,
                    f"{filename}: contains corrupted substitution tokens: {matches}",
                )

    def test_guides_do_not_use_known_english_section_headings(self) -> None:
        """Leaving a known English heading in a localized guide must fail."""
        for filename in EXPECTED_GUIDES:
            with self.subTest(guide=filename):
                headings = HEADING.findall(self.read_guide(filename))
                english_headings = sorted(
                    heading
                    for heading in headings
                    if heading in KNOWN_ENGLISH_HEADINGS
                )
                self.assertEqual(
                    [],
                    english_headings,
                    f"{filename}: contains known English section headings: "
                    f"{english_headings}",
                )

    def test_ethical_guide_has_dated_verification_marker(self) -> None:
        """Removing the legal-source verification date must fail."""
        filename = "diseno-etico.md"
        text = self.read_guide(filename)

        self.assertTrue(
            "Última verificación: 2026-08-20" in text,
            f"{filename}: must include 'Última verificación: 2026-08-20'",
        )

    def test_ethical_guide_states_scope_and_jurisdiction(self) -> None:
        """Presenting UX guidance as legal advice must fail the scope contract."""
        filename = "diseno-etico.md"
        text = normalized(self.read_guide(filename))

        self.assertIsNotNone(
            re.search(
                r"(?:guia|orientacion)[^.\n]{0,80}\bux\b"
                r"|\bux\b[^.\n]{0,80}(?:guia|orientacion)",
                text,
            ),
            f"{filename}: must identify the document as UX guidance",
        )
        self.assertIsNotNone(
            re.search(
                r"\bno\b[^.\n]{0,60}(?:asesoramiento|consejo|asesoria)\s+legal",
                text,
            ),
            f"{filename}: must state that it is not legal advice",
        )
        self.assertIsNotNone(
            re.search(
                r"verific\w*[^.\n]{0,100}(?:ley|legislacion|normativa|derecho)"
                r"[^.\n]{0,100}jurisdic\w*"
                r"|verific\w*[^.\n]{0,100}jurisdic\w*"
                r"[^.\n]{0,100}(?:ley|legislacion|normativa|derecho)",
                text,
            ),
            f"{filename}: must require verification of applicable law by jurisdiction",
        )

    def test_ethical_guide_links_official_regulatory_sources(self) -> None:
        """Replacing an official regulatory source with an unsupported claim must fail."""
        filename = "diseno-etico.md"
        text = self.read_guide(filename)
        official_sources = {
            "GDPR": r"https://eur-lex\.europa\.eu/eli/reg/2016/679(?:/[^\s)>]*)?",
            "FTC negative-option material": (
                r"https://(?:www\.)?ftc\.gov/[^\s)>]*negative-option[^\s)>]*"
            ),
            "CCPA/CPRA": r"https://cppa\.ca\.gov(?:/[^\s)>]*)?",
            "EU Digital Services Act": (
                r"https://eur-lex\.europa\.eu/eli/reg/2022/2065(?:/[^\s)>]*)?"
            ),
        }

        for source, url_pattern in official_sources.items():
            with self.subTest(source=source):
                self.assertIsNotNone(
                    re.search(url_pattern, text),
                    f"{filename}: must link to an official {source} source",
                )

    def test_ethical_guide_correctly_describes_click_to_cancel_status(self) -> None:
        """Treating the vacated amendment as an active mandate must fail."""
        filename = "diseno-etico.md"
        text = normalized(self.read_guide(filename))

        self.assertIsNotNone(
            re.search(r"click[- ]to[- ]cancel", text),
            f"{filename}: must discuss the FTC Click-to-Cancel amendment",
        )
        self.assertIsNotNone(
            re.search(
                r"\b2024\b[^.\n]{0,180}(?:anulad\w*|vacat\w*|dej\w+\s+sin\s+efecto)"
                r"|(?:anulad\w*|vacat\w*|dej\w+\s+sin\s+efecto)"
                r"[^.\n]{0,180}\b2024\b",
                text,
            ),
            f"{filename}: must say the 2024 Click-to-Cancel amendment was vacated",
        )
        self.assertIsNotNone(
            re.search(
                r"\bno\b[^.\n]{0,120}(?:mandato|exigencia|requisito)"
                r"[^.\n]{0,100}(?:nacional|federal|todo\s+estados\s+unidos)",
                text,
            ),
            f"{filename}: must say the amendment is not an active nationwide mandate",
        )
        self.assertIsNotNone(
            re.search(
                r"\b1973\b[^.\n]{0,160}(?:vigente|en\s+vigor|actual)"
                r"|(?:vigente|en\s+vigor|actual)[^.\n]{0,160}\b1973\b",
                text,
            ),
            f"{filename}: must distinguish the still-current 1973 rule",
        )
        self.assertIsNotNone(
            re.search(
                r"(?:otras|demas)\s+(?:leyes|normas)[^.\n]{0,80}(?:aplicables|vigentes)"
                r"|(?:leyes|normas)\s+aplicables",
                text,
            ),
            f"{filename}: must distinguish other applicable laws",
        )

    def test_accessibility_guide_identifies_official_wcag_22_recommendation(self) -> None:
        """Removing the normative WCAG source or its status must fail."""
        filename = "fundamentos-accesibilidad.md"
        text = self.read_guide(filename)
        normalized_text = normalized(text)

        self.assertTrue(
            "https://www.w3.org/TR/WCAG22/" in text,
            f"{filename}: must link to the official WCAG 2.2 Recommendation",
        )
        self.assertIsNotNone(
            re.search(r"wcag\s+2\.2", normalized_text),
            f"{filename}: must identify WCAG 2.2 by version",
        )
        self.assertIsNotNone(
            re.search(
                r"recomendacion[^.\n]{0,80}w3c|w3c[^.\n]{0,80}recomendacion",
                normalized_text,
            ),
            f"{filename}: must identify WCAG 2.2 as a W3C Recommendation",
        )


if __name__ == "__main__":
    unittest.main()
