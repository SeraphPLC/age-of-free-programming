#!/usr/bin/env python3
"""Offline public-doc external URL inventory. Zero network or credential access.

The result gives counts and categories only: it NEVER logs a URL, query value,
username or token. This is not a reachability test, service-terms check,
accessibility certification, security scan or publication approval.
"""
import argparse
from collections import Counter
import ipaddress
import json
from pathlib import Path
import re
from urllib.parse import parse_qsl, urlsplit

try:
    from .check_repo import without_fenced_code
except ImportError:
    from check_repo import without_fenced_code

DEFAULT_ROOT = Path(__file__).resolve().parents[1]
URL = re.compile(r"""(?i)(?<![a-z0-9+.-])https?://[^\s<>"'\]\)]+""")
PRIVATE_SUFFIXES = (".local", ".internal", ".lan", ".test", ".invalid")
SECRET_KEYS = {"access_token", "token", "api_key", "apikey", "password",
               "secret", "auth", "authorization", "session", "credential", "code"}


def private_host(host):
    if not host:
        return True
    host = host.rstrip(".").lower()
    if host in {"localhost", "metadata.google.internal"}:
        return True
    if host.endswith(PRIVATE_SUFFIXES):
        return True
    try:
        address = ipaddress.ip_address(host)
        return not address.is_global
    except ValueError:
        pass
    # Dotless hostnames generally do not identify a public DNS destination.
    return "." not in host


def classify(raw):
    """Return flags only; never include the raw address or its components."""
    flags = set()
    try:
        parts = urlsplit(raw)
        host = parts.hostname
        # Accessing port can raise ValueError for malformed URLs.
        _ = parts.port
        if parts.scheme.lower() != "https":
            flags.add("HTTP_NOT_HTTPS")
        if parts.username is not None or parts.password is not None:
            flags.add("USERINFO_PRESENT")
        if private_host(host):
            flags.add("NON_PUBLIC_DESTINATION")
        if parts.query:
            flags.add("QUERY_NEEDS_CONTEXT_REVIEW")
            keys = {key.casefold() for key, _ in parse_qsl(
                parts.query, keep_blank_values=True, max_num_fields=100)}
            if any(k in SECRET_KEYS for k in keys):
                flags.add("POTENTIAL_SECRET_QUERY_KEY")
    except (ValueError, UnicodeError):
        flags.add("MALFORMED_EXTERNAL_URL")
    return flags


def inventory(root):
    """Read only source Markdown, with literal fenced examples excluded."""
    root = Path(root)
    totals = Counter()
    unsafe_documents = set()
    query_documents = set()
    unique_host_count = set()
    for file in sorted(root.rglob("*.md")):
        if ".git" in file.parts:
            continue
        if file.is_symlink() or not file.is_file():
            totals["UNTRUSTED_MARKDOWN_FILE"] += 1
            unsafe_documents.add(file.relative_to(root).as_posix())
            continue
        try:
            text = without_fenced_code(file.read_text(encoding="utf-8"))
        except (OSError, UnicodeError):
            totals["UNREADABLE_MARKDOWN_FILE"] += 1
            unsafe_documents.add(file.relative_to(root).as_posix())
            continue
        totals["markdown_files_scanned"] += 1
        for match in URL.finditer(text):
            uri = match.group().rstrip(".,;:")
            totals["url_occurrences"] += 1
            try:
                host = urlsplit(uri).hostname
                if host:
                    unique_host_count.add(host.casefold())
            except ValueError:
                pass
            flags = classify(uri)
            for flag in flags:
                totals[flag] += 1
            if "QUERY_NEEDS_CONTEXT_REVIEW" in flags:
                query_documents.add(file.relative_to(root).as_posix())
            if any(flag in flags for flag in (
                "HTTP_NOT_HTTPS", "USERINFO_PRESENT", "NON_PUBLIC_DESTINATION",
                "MALFORMED_EXTERNAL_URL", "UNTRUSTED_MARKDOWN_FILE",
                "UNREADABLE_MARKDOWN_FILE")):
                unsafe_documents.add(file.relative_to(root).as_posix())
    fatal = ("HTTP_NOT_HTTPS", "USERINFO_PRESENT", "NON_PUBLIC_DESTINATION",
             "MALFORMED_EXTERNAL_URL", "UNTRUSTED_MARKDOWN_FILE",
             "UNREADABLE_MARKDOWN_FILE")
    return {
        "scope": "OFFLINE_STATIC_URL_INVENTORY_NOT_REMOTE_VALIDATION",
        "network_requests": 0,
        "files_scanned": totals["markdown_files_scanned"],
        "url_occurrences": totals["url_occurrences"],
        "unique_hostnames": len(unique_host_count),
        "insecure_http": totals["HTTP_NOT_HTTPS"],
        "userinfo": totals["USERINFO_PRESENT"],
        "non_public_destinations": totals["NON_PUBLIC_DESTINATION"],
        "malformed": totals["MALFORMED_EXTERNAL_URL"],
        "query_occurrences_to_review": totals["QUERY_NEEDS_CONTEXT_REVIEW"],
        "potential_secret_query_keys": totals["POTENTIAL_SECRET_QUERY_KEY"],
        "query_documents_to_review": len(query_documents),
        "unsafe_document_count": len(unsafe_documents),
        "disposition": "STOP_AND_REVIEW" if any(totals[k] for k in fatal)
                       else "STATIC_PASS_REACHABILITY_UNTESTED",
        "independent_release_evidence": False,
    }


def main():
    parser = argparse.ArgumentParser(description="No-network public URL inventory")
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    args = parser.parse_args()
    report = inventory(args.root)
    print(json.dumps(report, sort_keys=True, indent=2))
    return 1 if report["disposition"] == "STOP_AND_REVIEW" else 0


if __name__ == "__main__":
    raise SystemExit(main())
