# Standalone Independence & No-Backlink Boundary V1

The free AI OS educational materials must be reproducible **without access to any specific private project, machine, account, identity, service, API key, developer billing account, or unpublished technology**. This file is intentionally generic and contains no private platform pointers.

**This is a requirement on software that a reader may build, not a claim that a secure application has already been shipped.** The public repository holds only educational documentation, optional JSON schemas, and synthetic example data.

## Threats to avoid

- **Outbound callbacks:** no telemetry beacons, webhooks, hidden HTTP clients, DNS lookups, model-cloud proxy, installation tracking, crash reporting, analytics, remote update checks, or other requests to a publisher or third party in the offline baseline.
- **Private access inheritance:** no bundled credentials, tokens, OAuth scopes, SSH config, session cookies, personal account references, internal URLs or private software dependencies. A memory packet must not contain a host address or account connection token.
- **Permission inheritance:** no past chat, saved memory, archived approval, uploaded instruction, retrieved wiki page or model output authorizes a new action.
- **User-data extraction:** no automatic folder scanning, chat exporting, account lookup, browser history reading, remote backup, embedding of personal records or credential capture.
- **License mistakes:** no redistribution of full third-party archives, code, model weights or scraped datasets without documented rights for the specific use.
- **Misleading assurance:** no statements that local-first guarantees privacy, that a hash authenticates history, or that the proposed software has completed security certification.

## Rules for independent beginner builds

1. Build a deterministic Python/SQLite CLI that works with the network disconnected and with no external dependencies beyond standard-library modules.
2. Use a newly approved folder and **synthetic** project data. Do not touch another directory or existing project until separately authorized.
3. Store project memory locally by default; do not send a restart packet to an AI vendor without a separate owner-approved redaction step.
4. Model selection, hosted AI adapters, retrieval add-ons, downloaded archives and user-supplied endpoints are optional and disabled until explicitly chosen, reviewed and tested.
5. Never hard-code private entity references, IP addresses, account IDs, author email addresses, paths, domains, event collection endpoints or branded API URLs.
6. Record optional third-party dependencies, network destinations, exact model revisions, licenses, data-processing behavior and stop controls **before** any enablement.
7. Ship no background daemon, privileged launcher, installer, GitHub Actions workflow, remote bridge, cloud database or automatic updater in the baseline.
8. Preserve owner-authorized deletion capability for private local data; explain backup, index and exported-copy limitations.

## Publication safety checklist

- [ ] Only original, rights-cleared generic text and public standards are included
- [ ] No private code, internal docs, source-tree paths, account emails, secrets, links, hostnames or device IDs
- [ ] No binary/model weights, downloaded books, noncommercial third-party archives, tracking pixels or service endpoints
- [ ] No executable callbacks, scripts that silently install packages, or networked build steps
- [ ] JSON Schema identifiers are local URNs; the only schema dialect URL identifies a public standard, not a callback
- [ ] Tests use fabricated example data and publish no real-state receipts
- [ ] No instruction to contact a publisher, grant permanent authority or buy an API
- [ ] Public review uses the repository's established pull-request protection; confidential vulnerabilities use private security reporting

**A public hyperlink to a reference standard is not a callback, but a program that resolves it over the network would be a separate optional behavior.** In the offline baseline, no network resolution is needed to parse the included JSON files.

Before claiming a program is independent, actually inspect code and processes, run an offline test, and check that no outbound calls occur under the tested configuration. A documentation-only compliance checklist is not evidence of that execution.
