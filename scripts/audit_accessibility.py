#!/usr/bin/env python3
"""Offline, conservative Markdown accessibility hygiene checks.

This does NOT claim WCAG conformance or replace assistive-technology/user
testing. It reads Markdown only; no browsing, downloads, network or model calls.
"""
import argparse
from collections import Counter
import json
from pathlib import Path
import re

try:
    from .check_repo import without_fenced_code
except ImportError:
    from check_repo import without_fenced_code

HEADING = re.compile(r"^\s{0,3}(#{1,6})[ \t]+(.+)$")
MD_IMAGE = re.compile(r"!\[([^\]]*)\]\(([^)]*)\)")
MD_LINK = re.compile(r"(?<!!)\[([^\]]*)\]\(([^)]*)\)")
HTML_IMG = re.compile(r"<img\b[^>]*>", re.I | re.S)
HTML_ALT = re.compile(r"\balt\s*=\s*(['\"])(.*?)\1", re.I | re.S)
WEAK_LINK_TEXT = {"here", "click here", "read more", "link", "this link"}
DEFAULT_ROOT = Path(__file__).resolve().parents[1]


def checks_for_text(text):
    clean = without_fenced_code(text)
    problems = []
    last_level = None
    for line_number, line in enumerate(clean.splitlines(), start=1):
        heading = HEADING.match(line)
        if heading:
            level = len(heading.group(1))
            if last_level is not None and level > last_level + 1:
                problems.append((line_number, "SKIPPED_HEADING_LEVEL"))
            last_level = level
        for match in MD_IMAGE.finditer(line):
            if not match.group(1).strip():
                problems.append((line_number, "EMPTY_MARKDOWN_IMAGE_ALT_NEEDS_REVIEW"))
        for match in MD_LINK.finditer(line):
            label = " ".join(match.group(1).split()).casefold()
            if not label:
                problems.append((line_number, "EMPTY_MARKDOWN_LINK_LABEL"))
            elif label in WEAK_LINK_TEXT:
                problems.append((line_number, "GENERIC_LINK_LABEL_NEEDS_REVIEW"))
        for match in HTML_IMG.finditer(line):
            alt = HTML_ALT.search(match.group())
            if alt is None:
                problems.append((line_number, "HTML_IMAGE_ALT_MISSING_NEEDS_REVIEW"))
            elif not alt.group(2).strip():
                problems.append((line_number, "HTML_IMAGE_ALT_EMPTY_NEEDS_REVIEW"))
    return problems


def inventory(root):
    """Return counts and public-relative source locations, never link URLs."""
    root = Path(root)
    tally = Counter()
    reviewed = []
    for file in sorted(root.rglob("*.md")):
        if ".git" in file.parts:
            continue
        if file.is_symlink() or not file.is_file():
            tally["UNTRUSTED_MARKDOWN_SOURCE"] += 1
            continue
        try:
            content = file.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            tally["UNREADABLE_MARKDOWN_SOURCE"] += 1
            continue
        tally["markdown_files_checked"] += 1
        findings = checks_for_text(content)
        if findings:
            tally["files_with_findings"] += 1
        for lineno, kind in findings:
            tally[kind] += 1
            # Paths are public source locations, NOT outbound links.
            reviewed.append({"source_file":file.relative_to(root).as_posix(),
                             "line":lineno, "check":kind})
    blocking = {"SKIPPED_HEADING_LEVEL", "EMPTY_MARKDOWN_IMAGE_ALT_NEEDS_REVIEW",
                "EMPTY_MARKDOWN_LINK_LABEL", "GENERIC_LINK_LABEL_NEEDS_REVIEW",
                "HTML_IMAGE_ALT_MISSING_NEEDS_REVIEW",
                "HTML_IMAGE_ALT_EMPTY_NEEDS_REVIEW",
                "UNTRUSTED_MARKDOWN_SOURCE", "UNREADABLE_MARKDOWN_SOURCE"}
    return {
        "scope": "STATIC_MARKDOWN_HYGIENE_NOT_WCAG_CERTIFICATION",
        "network_requests": 0,
        "markdown_files_checked": tally["markdown_files_checked"],
        "files_with_findings": tally["files_with_findings"],
        "finding_counts": {k:tally[k] for k in sorted(blocking) if tally[k]},
        "findings": reviewed,
        "disposition": "REVIEW_REQUIRED" if any(tally[k] for k in blocking)
                       else "STATIC_HYGIENE_PASS_ASSISTIVE_TECH_NOT_TESTED",
        "independent_accessibility_verification": False,
        "qualified_release_evidence": False
    }


def main():
    parser=argparse.ArgumentParser(description="No-network Markdown accessibility hygiene")
    parser.add_argument("--root",type=Path,default=DEFAULT_ROOT)
    args=parser.parse_args()
    report=inventory(args.root)
    print(json.dumps(report,indent=2,sort_keys=True))
    return 1 if report["disposition"] == "REVIEW_REQUIRED" else 0


if __name__=="__main__":
    raise SystemExit(main())
