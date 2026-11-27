#!/usr/bin/env python3
"""Synthetic no-network external-link audit fixtures."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from scripts import audit_external_links as audit


class ExternalLinkSafetyTests(unittest.TestCase):
    def inventory(self, pages):
        with tempfile.TemporaryDirectory() as location:
            root = Path(location)
            for rel, content in pages.items():
                file = root / rel
                file.parent.mkdir(parents=True, exist_ok=True)
                file.write_text(content, encoding="utf-8")
            with patch.object(audit, "urlsplit", wraps=audit.urlsplit) as parser:
                r = audit.inventory(root)
                self.assertEqual(r["network_requests"], 0)
                self.assertEqual(parser.call_count, 2 * r["url_occurrences"]
                                 if r["url_occurrences"] else 0)
            return r

    def test_secure_link_and_code_examples_are_not_real_urls(self):
        r = self.inventory({"README.md":
            "# Synthetic\n[Public](https://example.org/guide)\n"
            "~~~markdown\n[Example only](http://127.0.0.1/private)\n~~~\n"})
        self.assertEqual(r["url_occurrences"], 1)
        self.assertEqual(r["insecure_http"], 0)
        self.assertEqual(r["non_public_destinations"], 0)
        self.assertEqual(r["disposition"], "STATIC_PASS_REACHABILITY_UNTESTED")

    def test_non_https_and_localhost_are_blocking_not_auto_fixes(self):
        r=self.inventory({"docs/links.md":
          "http://example.org/fake\nhttps://localhost/release\n"
          "https://192.168.0.2/path\n"})
        self.assertEqual(r["url_occurrences"], 3)
        self.assertEqual(r["insecure_http"], 1)
        self.assertEqual(r["non_public_destinations"], 2)
        self.assertEqual(r["unsafe_document_count"], 1)
        self.assertEqual(r["disposition"], "STOP_AND_REVIEW")

    def test_userinfo_and_query_value_never_appear_in_report(self):
        text=("https://synthetic-user:NOT_A_REAL_PASSWORD@example.org/path\n"
              "https://payment.example.org/donate?token=NEVER_ECHO_00001&foo=bar\n")
        r=self.inventory({"SUPPORT.md":text})
        serialized=json.dumps(r)
        self.assertEqual(r["userinfo"],1)
        self.assertEqual(r["query_occurrences_to_review"],1)
        self.assertEqual(r["potential_secret_query_keys"],1)
        self.assertNotIn("NOT_A_REAL_PASSWORD",serialized)
        self.assertNotIn("NEVER_ECHO_00001",serialized)
        self.assertNotIn("synthetic-user",serialized)
        self.assertEqual(r["disposition"],"STOP_AND_REVIEW")

    def test_normal_query_is_review_not_automatic_removal(self):
        r=self.inventory({"README.md":
          "https://cash.example.org/pay?amount=10\n"
          "https://cash.example.org/pay?amount=10\n"})
        self.assertEqual(r["query_occurrences_to_review"],2)
        self.assertEqual(r["potential_secret_query_keys"],0)
        self.assertEqual(r["query_documents_to_review"],1)
        self.assertEqual(r["unique_hostnames"],1)
        self.assertEqual(r["disposition"],"STATIC_PASS_REACHABILITY_UNTESTED")

    def test_local_non_public_and_invalid_urls_are_not_passed(self):
        self.assertIn("NON_PUBLIC_DESTINATION",
                      audit.classify("https://metadata.google.internal/"))
        self.assertIn("NON_PUBLIC_DESTINATION",
                      audit.classify("https://127.0.0.1/"))
        self.assertIn("MALFORMED_EXTERNAL_URL",
                      audit.classify("https://[broken_ipv6_address/"))
        self.assertNotIn("NON_PUBLIC_DESTINATION",
                         audit.classify("https://www.github.com/project"))

    def test_untrusted_markdown_symlink_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder)
            original=root/"original.txt"
            original.write_text("Synthetic hidden content")
            (root/"linked.md").symlink_to(original)
            result=audit.inventory(root)
            self.assertEqual(result["unsafe_document_count"],1)
            self.assertEqual(result["disposition"],"STOP_AND_REVIEW")


if __name__ == "__main__":
    unittest.main()
