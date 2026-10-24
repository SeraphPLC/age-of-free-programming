# Software Inventory & Exposure Boundaries
**The Age of Free Programming — public community preview | 2026-10-24**

## Scope and honest status
This inventory covers **the public copy-and-paste AI OS prompt repository**, not all Seraph development infrastructure or anything running on a contributor's computer. At publication, the public GitHub tree contained only Markdown text: README, prompts, guidance, a changelog, and an issue template. **It contained no executable program, installer, hosted service, model weights, dependency manifest, workflow, or GitHub Actions configuration.** That is a snapshot of the checked default branch, **not** an assurance about future commits, the private Seraph estate, or every copy made by readers.

**Safety objective:** no mandatory paid service, AI API key, extra package installer, public port, cloud database, telemetry, private Seraph source, or autonomous background worker for the intended offline baseline. This is a design constraint for software readers may choose to generate, **not** a claim that the prompt has already met an independent security audit.

## Inventory: required, optional, excluded

| Component | Why it appears | Deployment classification | Licensing / exposure notes |
| --- | --- | --- | --- |
| **Python 3** | Language for a user-created local CLI | **Specified for offline build**; not distributed by this repository | Python is available under the PSF License; users should install supported Python from a trusted source. Generated Python can still be unsafe. |
| **SQLite / Python's `sqlite3`** | Durable local task, event, evidence records | **Specified for offline build**; no separate database server needed | SQLite core is public domain. Local DB files must not enter a public repository or a chat. |
| **Python `unittest`** | Built-in repeatable tests | **Specified for offline build** | Part of Python standard library; no `pip install` necessary. Test output must be genuinely observed, not fabricated. |
| **Other Python standard modules** | File paths, CLI, transactions, data serialization, hashes, backups | **Allowed when justified** (e.g. `argparse`, `pathlib`, `json`, `hashlib`, `os`, `time`) | Built in. Modules that can launch processes or open sockets still need explicit authorization and careful implementation. |
| **GitHub** | Public, versioned Markdown prompt and voluntary user feedback | **Publisher-side service**; not needed to operate a local AI OS | This repository and public issues are visible to anyone. Never post secrets, private DBs, Resume Cards, or identifiable logs. |
| **ChatGPT or another AI chat** | Optional interactive code-building assistant | **Chosen by user**, not a runtime dependency | Text pasted into an online AI chat may leave the user's computer and is subject to that provider's terms and privacy controls. Use synthetic examples; strip identifiers from handoffs. |
| **Ollama / local model** | Optional local-model adapter after offline tests | **Deferred; not installed/distributed** | Local inference may run an HTTP server, commonly on localhost. Do not expose it to a LAN/Internet, enable cloud routing, or download unreviewed model weights without specific consent. Model licenses vary. |
| **Read-only local dashboard** | Optional browser display of status | **Deferred; not distributed** | Bind only to 127.0.0.1, deny writes, validate Host, escape user text, use a restrictive CSP, and provide a stop control. Loopback alone does not eliminate all risk. |
| **Git / private repo** | Optional user-selected version control | **Deferred** | Exclude DBs, backups, logs, tokens and personal records; user decides whether to connect to any remote. |
| **Multi-device networking / cloud adapters** | Possible future expansion | **Not approved for baseline** | Requires separate testing, privacy review, and explicit per-capability authorization. |

Official licensing references: [Python license](https://docs.python.org/3/license.html), [SQLite public domain](https://www.sqlite.org/copyright.html). Optional technology reference: [Ollama documentation](https://docs.ollama.com/).

## What we deliberately do NOT include
- Private Seraph source, data, repository access, keys, models, infrastructure, special Mesh services, or privileged connectors.
- An installed agent, scheduler, daemon, background job, remote execution bridge, hosted database, account-management automation, payment processing, or web service.
- Mandatory external `pip` packages, a `requirements.txt` that pulls unknown packages, plugins, Docker, telemetry, analytics SDKs, cloud APIs, or auto-updaters.
- Publicly reachable listeners, reverse proxies, network tunnels, unattended installers, dynamic execution of imported task text, or GitHub Actions workflows.
- Any permission to publish, message others, use credentials, edit an existing project, buy things, or deploy code merely because a model requests it.

## The real risk boundaries
1. **Code execution:** the greatest practical risk occurs **after someone follows the prompt** and executes AI-generated Python or shell commands. Every command should be inspected, permission-scoped, and tested in a new isolated folder first. Never presume generated code is secure.
2. **Personal data:** public GitHub issues and cloud-model chats are not private workspaces. Use synthetic examples. Resume Cards must omit secret and identifying content; database files and backups stay local.
3. **Local integrity:** SQLite transactions do not independently establish history authenticity. `doctor` should reconcile events against state; backups should check paths and reject symlinks. A locally edited hash chain can also be rewritten by an attacker with sufficient access.
4. **Local networking:** `127.0.0.1` is safer than a public bind but is not an authentication mechanism. Optional dashboards and local-model servers introduce new surfaces and need separate tests and supervision.
5. **IP and licensing:** publishing a public prompt and inviting users to copy it does **not** grant permission to access or reproduce private Seraph IP. The repository currently does not ship third-party executable source. The public text permits personal copying and sharing as stated in its README, but no comprehensive open-source software license for a future code package has been selected. Obtain a release/license review before publishing executable code or adopting third-party dependencies.
6. **Reliance and reputation:** the prompt is a learning tool, not a tested security product or guarantee of autonomous operation. Do not advertise independently verified portability, safety, or cross-model builds without evidence.

## Mandatory release gate for ANY future software distribution
Before adding an executable, dependency, dashboard, or service:
- Inventory every direct and transitive dependency, pinned version, source, and license; publish a software bill of materials (SBOM) if code is actually distributed.
- Check known security advisories for the selected versions and document updates; review OS-specific behavior.
- Search code, test artifacts, repository history, and build outputs for secrets, private paths, credentials, sensitive data, and unapproved Seraph materials.
- Run negative security tests including path traversal/symlinks, concurrency and lease fencing, event/state tampering, hostile task text, bad restore destinations, localhost HTTP checks if used, and offline behavior.
- Confirm tests were really executed and retain reproducible sanitized receipts; run clean-room builds on the platforms claimed.
- Require explicit human owner approval for any new public code, external connection, telemetry, protected capability, branding or license grant.
- Keep a way to stop or undo optional components. Do **not** turn on remote features by default.

**Bottom line:** the current publicly shared material is a **text-only educational prompt** with a minimal proposed Python/SQLite stack. This minimizes exposure. **It does not make future AI-generated code, third-party services, or users' private data automatically safe.**
