# Stage 1–2 Public-Prompt Reproduction Trial — October 24, 2026 (historical R2)

**Newer follow-up:** [R3 security hardening and 63-test results](LOCAL_STAGE2_R3_SECURITY_REVIEW_20261024.md). This page intentionally preserves the historical 57-test R2 run and the original model-generated Stage 1 fingerprint; R3 changes are documented separately.

**Status: partial model-generated reproduction; supervised local prototype; NOT a software release or security certification.**

This trial tested whether an AI could follow the public [Stage 1](../prompts/stages/01_OFFLINE_CORE.md) and [Stage 2](../prompts/stages/02_TASKS_EVIDENCE_RECOVERY.md) educational prompts to produce working Python/SQLite continuity software. It is a separate experiment from the earlier [v0.4 R1 synthetic reference](LOCAL_REFERENCE_R1_HARDENING_20261024.md). **No private Seraph source, services, datasets, machine identifiers, credentials or model weights were imported or distributed.**

## What actually happened

| Attempt | Source and process | Observed outcome |
| --- | --- | --- |
| Stage 1 fresh local coding-model generation | Public Stage 1 instructions; original direct local coding-model call | First generated program had a Python syntax error. A separately retained, model-generated repair produced a working CLI; **8/8 external synthetic acceptance tests PASS**. |
| Stage 2 initial model generation | Public Stage 2 requirements plus the generated Stage 1 source | **REJECTED BEFORE EXECUTION**: incompatible schema migration, raw claim-token exposure in proposed CLI, and incomplete journal verification. |
| Stage 2 larger-model attempt | Preinstalled local coding model, same public synthetic scope | **NO VALID SOURCE OUTPUT**; inference attempt ended without creating usable runtime code. Not counted as a pass. |
| Stage 2 narrowly scoped model generation | Direct local coding-model call; public Stage 2 plus generated Stage 1 | **8 PASS / 5 FAIL out of 13 tests**. Important failures: direct task alteration, evidence alteration, event-history corruption, and missing task-detail visibility. |
| Stage 2 supervised correction | Newly written local Python/SQLite code after the rejected model output was preserved | **57/57 first-party synthetic tests PASS** on each of two macOS computers; further details below. **This was not an independent model-generated Stage 2 build.** |

The original Stage 1 source remained byte-for-byte unchanged; its exact SHA-256 is retained in the owner-controlled private evidence manifest and not published here.

## What the supervised Stage 2 implements

The local experimental program now has explicit database migration, durable tasks/dependencies, a deterministic event journal and replay-to-projection checks, expiring fenced task claims, synthetic completion evidence, preserved first-failure records, private claim files, redacted pseudonymous handoff references, and SQLite backup/restore into new folders. A command-line demonstration confirms restart persistence and refusal of a mutation without a fresh **synthetic** approval flag.

The program uses Python standard-library modules and SQLite, not a hosted model or remote agent. No executable, installer, remote callback, private account connector or source-data archive was added to the public repository.

## Measured synthetic verification

| Actual check | Result |
| --- | --- |
| Migration, journal integrity and source tampering suite | **13/13 PASS** |
| Claims, dependencies, failure handling and handoff suite | **15/15 PASS** |
| CLI, local claim-file handling, SQLite backup/restore suite | **15/15 PASS** |
| Additional adversarial checks including race conditions, aliases and authority limits | **14/14 PASS** |
| Combined suite, Python 3.9, 3.12, 3.14 on one Mac | **57/57 per interpreter** |
| Combined suite on a second Mac, clean ZIP extraction and independent file-manifest/checksum verification | **57/57 PASS**, Python 3.9 |
| macOS process sandbox denying network access on both Macs | **57/57 PASS** per machine; separate blocked-connect control verified network denial |
| Focused Ruff S/B source checks | **PASS**, no findings in the selected rules |
| Short synthetic local-process continuity demonstration | **PASS** on both Macs |
| Fresh browser-chat reconstruction of full Stage 2 with real AI tool access | **NOT VERIFIED** |
| Independent human code/security review | **NOT PERFORMED** |
| Windows/Linux qualification and real-data retention/deletion evaluation | **NOT RUN** |

Developer-run tests and a second computer do **not** equal an independent security audit. Synthetic event consistency does **not** mean verified external truth. The test suite includes a deliberate demonstration that a coordinated local attacker can rewrite the entire event history and still pass structural checks: the journal is **not tamper-proof or independently authenticated**.

The supervised local Stage 2 engine and review ZIP SHA-256 values are retained in the owner-controlled private evidence manifest and not published here. These hashes identify reviewed bytes but are not proof of safety, authorship, or ownership. **The ZIP is deliberately not publicly downloadable.**

## What this teaches about the free builder guide

The Stage 1 prompt can generate a working small project using a direct local coding model, after a real syntax repair and real tests. Stage 2 is **substantially harder**: even plausible source code can omit the very security properties that make the system useful. Splitting the project into stages helps, but every stage still needs explicit independent negative tests before the owner calls it finished.

A beginner-friendly next iteration should provide a short, executable *self-check harness* for each stage and clearly state that the model must run the actual tests. A fluent explanation of fencing, journal replay, backup or privacy is not proof those behaviors exist.

## Release decision

**HOLD the executable.** Rights-holder licensing decisions, source-code ownership review, independent security assessment, authenticated history, real-data privacy controls, fresh-chat recovery qualification, and Windows/Linux testing remain outstanding. Public GitHub continues to distribute **educational text, generic schemas, synthetic examples and documented evidence**, not the executable.

Related: [Verification Status](VERIFICATION_STATUS.md), [Release Gate](PRIVACY_IP_AND_RELEASE_GATE.md), [License Decision Brief](LICENSE_DECISION_BRIEF.md), and [Staged Builder Path](STAGED_BUILD_PATH.md).
