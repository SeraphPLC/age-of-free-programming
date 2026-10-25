# Council feedback → practical public AI OS hardening (R1 candidate)

**Status: PUBLIC-SAFE EDUCATIONAL DRAFT · SPECIFICATION ONLY · NOT RUN · NOT APPROVED FOR RELEASE.**

This document turns external adversarial feedback on the frozen **v0.4 memory-fidelity prompt** into original, testable requirements for future community builders. Its presence does **not** establish a new council seat, an independently verified model identity, a safe executable or approval of the newer v0.5 Living prompt. The private reviewer transcripts and account sessions remain outside this repository. For the actual current builder entry point, use [Stages 0–4](STAGED_BUILD_PATH.md), not a large design document as your first step.

**Exact-version warning:** the archived v0.4 file in the current public tree was later prefixed with a safety warning. Its original underlying prompt body is unchanged, but the full file bytes and hash now differ from the frozen review artifact. Treat prior reviews as addressing that *historical body*, not as cryptographic receipts for the full newer file or any v0.5 material.

## Evidence boundary and order of operations

A candidate written by an AI is not an implementation. Source code must exist, pass a separately observed test process, and be inspected for destructive operations, network access, permission escalation, false output and untrusted dependencies. Even then, a functional test is not an independent security audit.

Use a **synthetic project and isolated, user-approved folder**. Enforce these rules at the test runner and filesystem layer; statements in a prompt or JSON schema alone are not controls. Never ship this educational exercise with private Seraph assets, real customer or personal records, private credentials or hidden infrastructure. The [output disclosure gate](OUTPUT_DISCLOSURE_GATE.md) is mandatory and already has observed black-box failures: prompt-only confidentiality is **not** an adequate security barrier.

Do not promote a fix directly because a model confidently calls it safe. The execution phases are: **PENDING → IMPLEMENTED (files exist) → TESTED (actual bounded run) → REVIEWED (qualified independent review) → OWNER-APPROVED**. The transitions are distinct; UNKNOWN, FAIL, BLOCKED, PARTIAL and NOT_RUN never silently become PASS.

## H01 — A test's existence is not evidence that it ran

**Risk:** an assistant reports “all tests green” when it generated a result string, executed only part of a suite, skipped expected failures, or ran on its own sandbox instead of the owner's approved machine.

**Required behavior:** for each required test ID record source revision, target platform, approved workspace, exact invocation, process start/finish, **observed exit code**, discovery/enumeration of expected tests, pass/fail/error/skip counts, and a locally retained synthetic output receipt. Distinguish `test_result=OBSERVED_PASS` from an AI's `claimed_result=PASS`. A complete report must list every required ID, including missing IDs as NOT_RUN. Exit code 0 from an empty test discovery is **not PASS**. Do not infer real Mac/Windows/Linux execution from a model's statement.

**Negative control:** deliberately make one synthetic test undiscoverable, one fail, and another skip. The gate must identify all three and block global VERIFIED despite a plausible success sentence. Repeat from a new process, not by recycling an earlier result.

## H02 — Deletion outranks immutable failure retention for private content

**Risk:** removing a record from the current view leaves its invented sensitive canary in SQLite pages, WAL/SHM, FTS indexes, caches, exports, attachments, snapshots or archived logs; preserving “original failure output forever” may directly conflict with user deletion.

**Required behavior:** design scoped deletion **before** collecting real data. Keep a versioned storage-location inventory and ask the owner what is in scope. Stop collection, invalidate active search/query outputs, remove permitted local copies from each named store, rebuild indexes/snapshots as supported, and replace retained failure details with a nonidentifying tombstone. Report every **unavailable, retained, exported, synced or unverified** copy. SQLite `DELETE` alone is not erasure; `VACUUM` alone is not a universal guarantee, particularly on SSDs or when backups exist. No promise of physical secure erase or recall of external copies is permitted.

**Negative control:** seed an entirely fictional marker into each created storage layer, request deletion, inspect the supported live tables, index and accessible files for that marker, then verify the report explicitly marks inaccessible backups and any physical-erasure limitation UNKNOWN. Never paste a real marker or raw database into an online AI chat.

## H03 — Local hash chains do not authenticate a coordinated rewrite

**Risk:** a malicious or mistaken writer changes the event log and recomputes the chain; a self-contained checksum can still look internally consistent.

**Required behavior:** state a threat model with separate levels: (A) detect accidental/local corruption, (B) compare against an **independently held** earlier reference, (C) attribute authorship. A bare SHA-256 or linked event hash only helps with A. An optional owner-held offline commitment can store event count, revision and tip digest outside the working directory, with separate authorization before write. Even with a commitment, identity/authenticity claims need an appropriate trusted mechanism.

**Negative control:** reconstruct a synthetic event chain after altering an entry. Local integrity alone must not call it authenticated; where an owner-held earlier commitment exists, the changed tip must be reported as a conflict, not silently updated.

## H04 — A handoff packet needs allowlisted fields and an independent export gate

**Risk:** `private_data_included=false` is a self-description rather than a scanner; free-text mission/task notes, paths, source URLs, errors, Git metadata or file names reveal private identities, routes or access details.

**Required behavior:** default to no cloud export. For a manually approved public-safe restart card, assemble output from a small **explicit allowlist of typed fields** (synthetic project label, opaque public record IDs, status, revision class, evidence availability and next non-sensitive action). Do not serialize raw database rows, command output, local absolute paths, private URLs, secrets or sensitive task text. Display the exact outgoing text to the owner and record an explicit approval for the destination and the **one** transfer. Use deterministic deny checks for known structured sensitive classes, plus human review and a fail-closed UNKNOWN; do not claim automatic redaction catches inference or all PII.

**Negative control:** plant fabricated high-risk strings into each input field and a combination of harmless-looking clues across fields; verify the packet withholds the affected fields or fails closed. A passed synthetic test does not establish real-data safety. The previous v0.5 black-box disclosure failures remain applicable until independently mitigated.

## H05 — Workspace boundaries must be checked on actual handles

**Risk:** simple string-prefix tests can confuse sibling directories; path traversal, symlinks or platform-specific reparse points can redirect a read or restore.

**Required behavior:** identify the approved workspace using resolved paths and actual opened handles, refuse ambiguous links and unexpected file types, and avoid time-of-check/time-of-use gaps wherever platform facilities permit. On POSIX, evaluate safe directory-relative opening and no-follow behavior; on Windows, verify handle-resolved paths and junction/reparse semantics. Python `Path.resolve()` and a prefix check alone are **not** a complete race-safe containment proof. Fail closed when equivalent safety is unavailable. Generated code may not recursively clean unapproved paths.

**Negative control:** try invented file references to a sibling folder, a symlink in the synthetic workspace and a changed link during a bounded test. No outside file may be accessed or modified. If a platform cannot be tested, mark that platform NOT_RUN.

## H06 — Task leases need atomic fencing, not optimistic labels

**Risk:** two real processes accept the same task, or a stale worker writes a result after its lease expires.

**Required behavior:** transactionally compare task state and active lease token, create a fresh unguessable fencing value per grant, bind completion/evidence to that grant and the task's current revision, and reject stale/wrong completions. SQLite transactions must serialize the competing claim; record conflicts explicitly. A human-readable worker name is **not** authentication. Define expiry with a documented clock policy; clock rollback/suspension and cross-device time cannot silently revalidate a stale lease.

**Negative control:** launch two separate synthetic processes behind a start barrier against the same test database and inspect committed state. Exactly one valid claim may control completion. Repeat and test stale token, wrong task, expired lease and changed task revision. Do not equate two thread calls in one process with the separate-process gate.

## H07 — Backup is a consistent state generation, not a bag of hashes

**Risk:** the SQLite snapshot, binder Markdown, event tip and evidence pointers are collected at different revisions; they all have valid hashes but do not describe the same committed state.

**Required behavior:** define an authorized generation boundary, capture SQLite with the backup API, bind included source/binder files to the same recorded generation, use a minimal explicit manifest, and detect any file that changes during capture. Restore only to a different, verified-empty test folder. Reconcile the replayed event count and task/evidence/mission state; a checksum match by itself does not prove a meaningful restore. Exclude linked files and other unapproved content.

**Negative control:** modify the synthetic binder while a backup is being formed. The operation must fail or clearly report an inconsistent snapshot. Also test missing files, wrong manifest generation and refused overwrite of existing content.

## H08 — Make the first ten minutes smaller and less ambiguous

Begin with [Stage 0](../prompts/stages/00_CHAT_ONLY_CONTINUITY.md) if there is no authorized computer access, or the [Stage 1](../prompts/stages/01_OFFLINE_CORE.md) minimal CLI with three commands and a **short list of acceptance tests**. Do **not** ask a beginner to paste an entire advanced specification and expect an instant secure “AI OS.” Keep Stages 2–4 optional and qualify each separately. The large v0.5 Living prompt remains a **reference candidate**, not a binary, privacy barrier or integrated release.

## H09 — Rights and approval are separate from technical readiness

Do not import proprietary studies, private AI model routing, personal research archives, official content without lawful reuse rights, or unapproved third-party packages. “Publicly accessible” does not mean “licensed for redistribution or training.” The software distribution license remains undecided. A completed council tally cannot override owner/rights-holder review, historical Git metadata exposure, release review, or the observed model disclosure failures.

## Definition of done for any future candidate

The next revised **exact source** must have its own SHA-256, synthetic test IDs with genuine command receipts and independent, identifiable reviewer acknowledgements. Reviews of historical v0.4 do not automatically qualify changed v0.5 or a future version. Maintain a private evidence store for raw browser transcripts, host/account details and sensitive failure traces; publish only a privacy-safe aggregate with uncertainties. Preserve failures, partial returns, tool blocks and source mismatches without inventing reviewer votes.

**Current status:** this is a proposed remediation contract; the negative cases above are **NOT RUN** against a newly generated release candidate. No approval, executable test pass or council qualification is asserted here. The companion [review receipt and negative-test matrix](labs/COUNCIL_NEGATIVE_EVIDENCE_MATRIX_R1.md) is a worksheet, not an automated test runner.
