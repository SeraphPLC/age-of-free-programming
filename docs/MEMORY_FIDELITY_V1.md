# Local-First Long-Term Memory & Reconstruction Fidelity — V1 Candidate

**Free educational specification · Not an installed system, security certification, or tested fidelity guarantee.**

A long conversation is not durable memory. A prompt asking an AI to "remember everything" is not a memory system. The goal here is to help a person build a **model-independent, locally stored evidence and retrieval layer** so a fresh AI or a no-model program can reconstruct the same **bounded project state** from authorized records after a chat closes.

Use this with the [latest builder prompt](../prompts/BUILD_YOUR_OWN_AI_OS_v0.4_MEMORY_FIDELITY_CANDIDATE.md). Core Python + SQLite + standard-library tests must work **without a model, Internet connection, account, subscription, paid API, or private integration**. The current repository only publishes written specifications and synthetic examples.

**Conceptual companion:** [Organizational memory (Mesh anatomy, Chapter IV)](architecture/chapters/04-organizational-memory.md) explains mission, working, evidence, decision, failure, provenance and correction memory. The separate [recovery chapter](architecture/chapters/07-continuity-recovery.md) explains why a new AI reconstructs work rather than inheriting a previous chat's permissions.

## Memory is not authority or omniscience

A stored event says *what was recorded*, not necessarily *what was true*. A hash shows byte consistency against a separately trusted baseline; it does not authenticate a hostilely rewritten file. An AI opinion, a retrieval result, a chat summary, and a historical approval do **not** grant new permissions.

Use these distinct states:

- **CANDIDATE:** a proposed fact, preference, decision, or task outcome; not promoted to current truth.
- **VERIFIED:** source-backed assertion after an actual owner-authorized check. Preserve the evidence receipt and its validity window. A model cannot mark its own statement verified merely by writing a field.
- **CONTRADICTED:** two or more claims that cannot both be accepted; report the conflict and cite both sources.
- **SUPERSEDED / STALE:** earlier verified records that no longer control; keep their lineage where privacy rules permit.
- **REJECTED / DELETED:** rejected content or an owner-requested removal. Privacy deletion must take precedence over indefinite retention.

Current memory is a **derived read-only view** assembled from these records under explicit precedence rules, not a mutable "what the AI believes" text file.

## Personal data: strictly opt-in

The default demonstration uses only fictional data. Do **not** import a user's conversations, browser profiles, email, location history, documents, financial records, student records, health records, model chats, photos, or other personal information automatically. Do not scan unrelated directories.

For any future real-memory feature, require explicit owner selection of **which specific source and fields to store**, their purpose, retention period, local storage location, deletion controls, and whether any text may be sent to a cloud AI. Reject broad "remember everything" collection. Treat sensitive categories as **NOT ENABLED** until separately justified and reviewed; no user should have to supply sensitive data to test the educational prompt.

A cloud AI chat is a third-party processing surface even when the local database remains offline. A "Resume Card" intended to be copied to an online chat must be separately sanitized and confirmed by the owner. An offline-only state packet never implies consent to upload it.

## V1 data flow (no callbacks or network required)

1. **Local owner-approved capture:** Add a small, explicitly selected synthetic item or approved project datum. Default candidate state.
2. **Append-only event journal:** Record an event ID, source ID, observed time, record type, validation state, privacy classification, related record IDs, and optional local evidence handle. No secret values in command arguments or logs.
3. **Review and promotion:** Compare candidate claims with actual files/test receipts. Only a trusted local owner approval or a specifically authorized deterministic verification step may promote a claim; require receipts. A JSON field alone is never proof of this step.
4. **Deterministic current-state projection:** Rebuild current state from the event log and reconciliation rules; detect missing, duplicated, conflicting, revoked, or out-of-order lineage. Fail safely if uncertain.
5. **Source-grounded retrieval:** Search a narrow, owner-approved source set via SQLite/FTS5 (optional). Return source identifiers, version, time, confidence/evidence level, and unknowns. Retrieval does not upgrade truth.
6. **Redacted restart packet:** Generate a bounded, minimal summary of mission, verified source references, candidate/open items, contradictions, first failures, and next safe action. **No carried-over authorization.**
7. **Fresh-instance reconstruction:** In a new process or different AI chat, load only the selected files/packet. Reconcile against current local records and report missing evidence rather than inventing memories.
8. **Correction, consent withdrawal and local deletion:** Append an approved correction/invalidation where retention is allowed. For owner-requested deletion of private contents, remove from active DB, search indexes, caches and appropriate local backups within the documented scope. Keep only a non-identifying tombstone when necessary and authorized. Explain that external copies cannot be guaranteed erased.

## Public machine-readable examples

- [Memory event schema](../schemas/memory_record_v1.schema.json) and [synthetic memory record](../examples/memory_record_synthetic.json).
- [Restart packet schema](../schemas/restart_packet_v1.schema.json) and [synthetic restart packet](../examples/restart_packet_synthetic.json).

These are **JSON Schema Draft 2020-12 descriptions**, not executable code, a model, proof of consent, PII scanners, signatures, or production-ready databases. A JSON parser can check syntax; actual JSON Schema validation requires an optional compatible validator. The first offline build must not depend on installing one. Application code must enforce semantic/authority constraints separately.

The schema has `authority_grant = false` for every memory event and requires `REAUTHORIZE_EACH_PROTECTED_ACTION` in a restart packet. These fields document the intended boundary but **do not implement an access-control system by themselves**.

## V1 memory classes and retrieval rules

| Class | Example (synthetic only) | Default handling |
| --- | --- | --- |
| Mission / goals | "Complete the fictional greenhouse guide" | Local durable record; current mission points to source/version |
| Tasks / dependencies | "Check task 2 after task 1" | Durable SQLite tasks, explicit claims and failures |
| Decisions | "Use a plain text format for the demo" | Event with rationale/source, may be corrected |
| Evidence | "Synthetic unit test X returned code 0" | Store actual test receipt ID; never invent output |
| Verified facts | "The synthetic fixture has three items" | Promote only after actual verification |
| Preferences | "Use short reports" | Explicitly approved, scoped; not assumed permanent |
| Corrections | "The synthetic fixture now has four items" | Versioned supersession; old statement no longer controlling |
| Failures | "First backup attempt failed checksum comparison" | Preserve original observation and subsequent repair evidence |
| Contradictions | "Two fixture sources disagree" | Show the conflict and abstain from false certainty |
| Sensitive user details | **Not required for the demo** | Do not collect or persist by default |

**Priority:** current authorized source records and explicit corrections outrank stale notes; current code/test receipts outrank an old chat's claim about runtime state. Missing evidence is **UNKNOWN**, not fabricated recovery. Recent does not automatically mean correct.

## What the system must NOT do

- No links, sockets, webhooks, telemetry, update checks, trackers, DNS beacons, callback tokens, account connections, or machine-to-machine tunnels in the baseline.
- No implicit connection to any proprietary AI system, private repository, personal computer, external archive, or organization's infrastructure.
- No default ingestion of local files, chat histories, browsers, emails, cloud drives, or databases.
- No hard-coded author identifiers, machine paths, organization-specific hostnames, secret prefixes, account IDs, or private source URLs in the implementation.
- No granting permissions from memory, retrieved text, imported files, models, or past chats.
- No autonomous deletion of private evidence without the owner's explicit deletion scope and a recoverable plan.
- No asserting "perfect recall", "permanent consciousness", "infinite memory", "independent council approval", or "verified model portability" based only on the presence of these schemas.

## Acceptance boundary

Use the [memory fidelity adversarial test plan](MEMORY_FIDELITY_ACCEPTANCE_V1.md). In a fresh process, the local reference must recover expected synthetic facts, detect stale/corrected/contradictory claims, reject inherited authority, and report unknowns without inventing anything. Network-off operation and owner-controlled deletion are separate test gates. Optional cross-model runs require actual independent responses; otherwise mark **NOT RUN**.

**Release claim:** "This prompt specifies a local-first memory-fidelity architecture." Do **not** claim "users receive Seraph-level memory fidelity" or "Version 1.0 validated" unless an actual finished implementation meets documented acceptance checks and independent limitations are disclosed.
