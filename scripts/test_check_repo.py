#!/usr/bin/env python3
"""Synthetic tests for the repo's stdlib-only Markdown/JSON structure checker."""
import contextlib
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from scripts import check_repo as target


class PublicCheckerTests(unittest.TestCase):
    def check(self, files):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            for rel, data in files.items():
                path = root / rel
                path.parent.mkdir(exist_ok=True, parents=True)
                path.write_text(data, encoding="utf-8")
            stdout = io.StringIO()
            with patch.object(target, "ROOT", root), contextlib.redirect_stdout(stdout):
                status = target.main()
            return status, stdout.getvalue()

    def test_valid_relative_link_and_percent_encoded_file(self):
        code, log = self.check({"README.md": "# Hello\n[one](Guide%20One.md#details)\n",
                                "Guide One.md": "# Details\n"})
        self.assertEqual(code, 0, log)

    def test_fenced_code_links_are_examples_not_real_references(self):
        # Examples in code blocks do not imply actual files need to exist.
        code, log = self.check({
            "README.md": "# Valid\n~~~markdown\n[Literal](fake-missing.md)\n"
                         "~~~\n~~~md\n![Example](example-fake.png)\n~~~\n"
        })
        self.assertEqual(code, 0, log)

    def test_current_document_anchor_is_checked(self):
        code, log = self.check({
            "README.md": "# Existing\n[Valid](#existing)\n[Broken](#not-a-heading)\n"
        })
        self.assertEqual(code, 1, log)
        self.assertIn("not-a-heading", log)

    def test_duplicate_simple_heading_slugs(self):
        code, log = self.check({
            "README.md": "# Topic\n# Topic\n[Second](#topic-1)\n"
        })
        self.assertEqual(code, 0, log)

    def test_missing_file_and_escape_fail_closed(self):
        code, log = self.check({
            "docs/start.md": "[Missing](absent.md)\n[Escape](../../outside.md)\n"
        })
        self.assertEqual(code, 1, log)
        self.assertIn("missing target", log)
        self.assertIn("escapes repo", log)

    def test_malformed_json_detected(self):
        code, log = self.check({"README.md":"# Safe\n","bad.json":"{oops"})
        self.assertEqual(code, 1, log)
        self.assertIn("invalid JSON", log)

    def test_header_inside_fenced_code_is_not_anchor(self):
        code, log = self.check({
            "README.md": "# Real\n~~~text\n# Fabricated\n~~~\n[bad](#fabricated)\n"
        })
        self.assertEqual(code, 1, log)
        self.assertIn("unresolved simple anchor", log)


if __name__ == "__main__":
    unittest.main()
