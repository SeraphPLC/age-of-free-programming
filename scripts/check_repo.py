#!/usr/bin/env python3
"""Offline, standard-library-only structural check for this educational repository.

Checks relative Markdown links, local HTML href/src targets, and JSON syntax.
Does NOT validate external URLs, interpret prompt safety, run the AI OS,
validate JSON Schema semantics, or certify publication readiness.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"(?<!!)\[[^\]]*\]\((?:<([^>]+)>|([^\s)]+))(?:\s+[^)]*)?\)")
IMAGE = re.compile(r"!\[[^\]]*\]\((?:<([^>]+)>|([^\s)]+))(?:\s+[^)]*)?\)")
HTML = re.compile(r"\b(?:href|src)\s*=\s*[\"']([^\"']+)[\"']", re.I)
HEADING = re.compile(r"^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$")
CODE_FENCE = re.compile(r"^\s*(`{3,}|~{3,})")


def slug(text: str) -> str:
    text = re.sub(r"<[^>]*>", "", text).strip().lower()
    text = re.sub(r"[^\w\- ]", "", text, flags=re.UNICODE)
    return re.sub(r"\s+", "-", text)


def anchors(path: Path) -> set[str]:
    seen: dict[str, int] = {}
    result: set[str] = set()
    fenced = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if CODE_FENCE.match(line):
            fenced = not fenced
            continue
        if fenced:
            continue
        match = HEADING.match(line)
        if match:
            base = slug(match.group(1))
            idx = seen.get(base, 0)
            result.add(base if not idx else f"{base}-{idx}")
            seen[base] = idx + 1
    return result


def main() -> int:
    failures: list[str] = []
    markdown = sorted(ROOT.rglob("*.md"))
    json_files = sorted(ROOT.rglob("*.json"))
    refs = 0
    for path in markdown:
        raw = path.read_text(encoding="utf-8")
        for match in list(LINK.finditer(raw)) + list(IMAGE.finditer(raw)) + list(HTML.finditer(raw)):
            value = next((g for g in match.groups() if g is not None), "")
            if not value or value.startswith(("#", "mailto:", "data:")):
                continue
            parts = urlsplit(value)
            if parts.scheme or parts.netloc:
                continue  # External sites not requested or verified by this offline check.
            target = (path.parent / unquote(parts.path)).resolve()
            refs += 1
            if not target.is_relative_to(ROOT.resolve()):
                failures.append(f"{path.relative_to(ROOT)}: link escapes repo: {value}")
            elif not target.exists():
                failures.append(f"{path.relative_to(ROOT)}: missing target: {value}")
            elif parts.fragment and target.suffix.lower() == ".md":
                # GitHub slugging differs for complex Unicode/HTML; check only simple slugs.
                fragment = unquote(parts.fragment).lower()
                if re.fullmatch(r"[a-z0-9_-]+", fragment) and fragment not in anchors(target):
                    failures.append(f"{path.relative_to(ROOT)}: unresolved simple anchor: {value}")
    for path in json_files:
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (ValueError, UnicodeError) as exc:
            failures.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
    print(f"Checked {len(markdown)} Markdown files, {refs} local references, {len(json_files)} JSON files")
    print("Scope: static relative references and JSON syntax only; NOT AI OS tests or security audit")
    for failure in failures:
        print("FAIL:", failure)
    print(f"Result: {'FAIL' if failures else 'PASS'} ({len(failures)} issues)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
