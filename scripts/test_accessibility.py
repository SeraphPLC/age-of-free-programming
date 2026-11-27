#!/usr/bin/env python3
"""Synthetic no-network tests of Markdown accessibility hygiene."""
from pathlib import Path
import tempfile
import unittest
from scripts import audit_accessibility as audit


class MarkdownAccessibilityTests(unittest.TestCase):
    def test_heading_skip_fails_without_claiming_wcag_certificate(self):
        data = "# Heading\n\n### Skipped to level three\n"
        self.assertEqual(audit.checks_for_text(data),
                         [(3,"SKIPPED_HEADING_LEVEL")])
        self.assertEqual(audit.checks_for_text(
            "# Heading\n\n## Section\n\n### Detail\n"),[])

    def test_fenced_examples_are_not_scanned(self):
        text = ("# Actual heading\n"
                "~~~markdown\n### Fenced title\n![bad]()\n[here](https://example.org)\n~~~\n"
                "## Real section\n")
        self.assertEqual(audit.checks_for_text(text),[])

    def test_inline_code_is_example_not_live_html_or_image(self):
        raw = ("# Real title\n"
               "The syntax `<img>` is shown as inline code.\n"
               "Use `![alt](path.png)` as an example.\n"
               "The inert literal `<img src='x.png'>` should not count.\n")
        self.assertEqual(audit.checks_for_text(raw), [])

    def test_image_alts_and_html_figure_alts(self):
        t=("# Heading\n![descriptive](img.png)\n"
           "![  ](img2.png)\n"
           "<img src='image.png' width='20'>\n"
           "<img src='image2.png' alt=''>\n"
           "<img src='image3.png' alt='descriptive'>\n")
        codes=[kind for _,kind in audit.checks_for_text(t)]
        self.assertEqual(codes, [
            "EMPTY_MARKDOWN_IMAGE_ALT_NEEDS_REVIEW",
            "HTML_IMAGE_ALT_MISSING_NEEDS_REVIEW",
            "HTML_IMAGE_ALT_EMPTY_NEEDS_REVIEW"])

    def test_weak_markdown_label_is_review_not_link_validation(self):
        t="# Heading\n[here](https://example.org?a=b)\n[This link](page.md)\n[An informative label](page.md)\n"
        r=audit.checks_for_text(t)
        self.assertEqual(r,[(2,"GENERIC_LINK_LABEL_NEEDS_REVIEW"),
                            (3,"GENERIC_LINK_LABEL_NEEDS_REVIEW")])

    def test_offline_inventory_preserves_only_public_file_and_line(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            (root/"README.md").write_text("# A\n\n### B\n")
            (root/"GOOD.md").write_text("# B\n## C\n![Descriptive alt](https://example.org/?SECRET=not-to-show)\n")
            result=audit.inventory(root)
            self.assertEqual(result["network_requests"],0)
            self.assertEqual(result["markdown_files_checked"],2)
            self.assertEqual(result["files_with_findings"],1)
            self.assertEqual(result["finding_counts"]["SKIPPED_HEADING_LEVEL"],1)
            self.assertEqual(result["findings"][0]["source_file"],"README.md")
            self.assertNotIn("SECRET",str(result))
            self.assertEqual(result["disposition"],"REVIEW_REQUIRED")

    def test_symlink_markdown_is_not_read(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            (root/"original.txt").write_text("Confidential synthetic fixture")
            (root/"linked.md").symlink_to(root/"original.txt")
            result=audit.inventory(root)
            self.assertIn("UNTRUSTED_MARKDOWN_SOURCE",result["finding_counts"])
            self.assertEqual(result["disposition"],"REVIEW_REQUIRED")
            self.assertNotIn("Confidential synthetic",str(result))


if __name__ == "__main__":
    unittest.main()
