# SHA-256, saved memory, and safe recovery — a beginner's guide

**Public educational guide · 2026-10-25 · Documentation and synthetic example only. No installed AI OS, implemented security boundary, independent test pass, or production guarantee is provided here.**

**Start here:** [Stage 1 offline core](../prompts/stages/01_OFFLINE_CORE.md) → [Stage 2 tasks and recovery](../prompts/stages/02_TASKS_EVIDENCE_RECOVERY.md) → [Stage 3 memory fidelity](../prompts/stages/03_MEMORY_FIDELITY.md). The [current advanced builder prompt](../prompts/BUILD_YOUR_OWN_AI_OS_v0.5_LIVING_CANDIDATE.md) includes the corresponding implementation requirements.

## In one minute: where does the information go?

Your AI does **not** save project history merely because you ask it to "remember." You must actually save it somewhere that a new process or chat can read.

| Part | What it does | What it does **not** do |
| --- | --- | --- |
| **A manual handoff card (Stage 0)** | Gives you a text record to save and paste into a new chat | Automatically create durable storage, prove a fact, or preserve permissions |
| **SQLite (Stages 1–3)** | Holds actual mission/task/evidence/event data in a file you control | Authenticate a claim just because it appears in a table |
| **Application event journal (Stage 2+)** | Preserves an ordered history of changes and corrections | Automatically provide an independent trusted witness |
| **SHA-256 fingerprints (Stage 2+)** | Detects changes to bytes when compared with a trusted expected fingerprint | Encrypt data, back it up, prove authorship, or guarantee factual truth |
| **Linked event fingerprints (Stage 2+)** | Reveal certain missing, changed, duplicated, or reordered events during verification | Defeat an attacker who rewrites the whole chain and its local checkpoint |
| **SQLite backup + mission binder (Stage 2+)** | Provides restorable copies when built and checked correctly | Automatically make the separate \`MISSION.md\` consistent with a database snapshot |
| **Git (optional)** | Preserves selected *source/document* revisions and commit identities | Store a private database safely by default, or prove a project is correct |
| **GET SERAPHED packet** | Carries a sanitized verified-state summary to the next AI | Grant authority, transport confidential records safely by itself, or provide the missing original evidence |

**Short version:** SQLite stores the information. Events record changes. SHA-256 detects certain inconsistencies. Verified backups provide a way to recover. A new AI reconstructs the state from those records, not from its own confidence.

## 1. What exactly is SHA-256?

SHA-256 is a cryptographic *hash function*: you put bytes into it and get a 256-bit output, usually shown as **64 hexadecimal characters**. This output is a **fingerprint** of the exact input bytes.

If the bytes change, the fingerprint will almost certainly change. But the fingerprint is not the file, and you cannot restore the file from its fingerprint.

A hash is **not encryption**. A person holding the stored mission or database can read its contents unless a separate encryption/access-control mechanism protects them.

A hash also does **not authenticate its creator**. If someone can rewrite the project database and its locally stored hashes, they may be able to create a self-consistent false history. Verification is stronger only when the expected checkpoint is protected independently (for example, a separately trusted signed or access-controlled record).

## 2. What is a linked event journal?

Imagine a completely fictional greenhouse project:

1. **Event 1** establishes the mission: "Grow three seedlings."
2. **Event 2** records a task: "Measure the soil."
3. **Event 3** records a *correction*: "The first measurement was wrong; corrected from a second source."

Store the actual records in SQLite. Each event has a sequence, unique ID, type, source reference, and synthetic payload. Use one documented, stable encoding rule to turn the exact event into bytes, then calculate:

\`\`\`text
digest_1 = SHA256(version_marker || genesis_digest || canonical(event_1))
digest_2 = SHA256(version_marker || digest_1       || canonical(event_2))
digest_3 = SHA256(version_marker || digest_2       || canonical(event_3))
\`\`\`

Here \`||\` means *combine bytes in a well-defined way*, not text concatenation with ambiguous separators. Keep the algorithm/version explicit and the prior digest fixed-length. An actual implementation stores the previous digest and resulting digest along with each event.

On restart, \`doctor\` should verify the SQLite database, replay events in order, check unique IDs and valid parent/sequence relationships, recompute every digest, and compare the reconstructed project state with the saved task/evidence projection. Check the final digest against a **separately trusted checkpoint when available**.

If a past measurement was incorrect, **append a correction event** rather than silently changing its historical event. Retain the original failure where policy permits; do not treat hash preservation as an exemption from legitimate privacy deletion.

## 3. Tiny synthetic SHA-256 illustration — no files or network

The following Python 3 standard-library example computes a linked chain **in memory only** using invented events. It neither writes a database nor proves an installed Seraph system. Review the code and run it only in a suitable local learning environment.

\`\`\`python
import hashlib
import json

def canonical_bytes(event):
    return json.dumps(
        event, sort_keys=True, separators=(",", ":"),
        ensure_ascii=False, allow_nan=False
    ).encode("utf-8")

def fingerprint(previous_hex, event):
    previous = bytes.fromhex(previous_hex)  # 32 fixed bytes
    if len(previous) != 32:
        raise ValueError("Expected a 32-byte prior digest")
    return hashlib.sha256(
        b"AIOS-event-v1\x00" + previous + canonical_bytes(event)
    ).hexdigest()

events = [
    {"seq": 1, "id": "fictional-001", "kind": "MISSION",
     "text": "Grow three seedlings"},
    {"seq": 2, "id": "fictional-002", "kind": "TASK",
     "text": "Measure soil"},
    {"seq": 3, "id": "fictional-003", "kind": "CORRECTION",
     "text": "Correct first measurement"}
]
tip = "00" * 32  # documented synthetic genesis marker
for event in events:
    tip = fingerprint(tip, event)
    print(event["id"], tip[:16] + "...")

# A changed input should give a different final fingerprint.
altered = [dict(item) for item in events]
altered[1]["text"] = "Measure soil twice"
changed_tip = "00" * 32
for event in altered:
    changed_tip = fingerprint(changed_tip, event)
assert changed_tip != tip
print("Synthetic alteration detected by differing chain tips")
\`\`\`

This is an **illustration**, not a security-hardened journal. It does not implement persistent storage, authorization, event uniqueness checks, replay validation, independent checkpoint protection, backup, or privacy-safe deletion. Tests of any actual Stage 2 program must examine those separately.

Do not store secrets in the public demonstration or publish digests of unreleased sensitive files. Even a digest can enable correlation or confirmation of protected material. See the [public output disclosure policy](OUTPUT_DISCLOSURE_GATE.md).

## 4. Git hashes and SHA-256 are related, but different

Git identifies versions of files, trees, and commits with **Git object IDs** (many current repositories use SHA-1 object IDs; Git also supports SHA-256-formatted repositories). A Git commit ID is **not automatically the SHA-256 of your SQLite database or its event chain**.

Use Git for versions of deliberately selected, rights-cleared source code and documentation. Do **not** commit a private SQLite database, raw conversations, secrets, personal data, local backups, or internal Seraph implementation to a public repository.

A Git commit can help identify exactly which *code revision* was tested. It does not by itself prove that a tool ran, that the resulting behavior is correct, or that a private database was backed up.

## 5. What must a verified backup protect?

SQLite's standard-library \`sqlite3.Connection.backup()\` can produce a consistent snapshot **of the database**. The mission file, local metadata, directory permissions, and other external artifacts are **separate**.

A proper implementation needs a documented generation/snapshot protocol that proves the saved \`MISSION.md\` and SQLite records belong to the **same consistent state**. A manifest can record the schema, mission-file digest, event count, event tip, and snapshot identity, but a manifest stored beside editable files is not independent proof against malicious rewriting.

A safe restore should:
- Refuse symlinks, traversal, and any existing destination; use a different authorized empty target.
- Check file and database integrity, mission consistency, event history, permissions, schema and expected snapshot generation.
- Rebuild and compare projected state, tasks, evidence references, corrections, and first failures.
- Stop as \`UNKNOWN / RECONCILE\` when a timed-out write or mismatched snapshot cannot be resolved safely; do not blindly retry.
- Account for authorized retention and deletion obligations across the database, derived indexes and reachable backups.

## 6. Minimum synthetic negative tests before claiming memory integrity

Run these on the **actual generated program**, using only fictitious records and an isolated test folder:

| Test | Expected result |
| --- | --- |
| Change one event without updating its digest | \`doctor\` reports an integrity discrepancy |
| Delete, reorder, or duplicate an event | Sequence/lineage validation rejects or reports inconsistency |
| Alter task/evidence projection without corresponding events | Replay comparison detects inconsistency |
| Rewrite all events *and* local hashes coherently | Do **not** falsely claim authentication; compare a separate trusted anchor if one exists |
| Restore a snapshot with mismatched \`MISSION.md\` or generation | Reject the restore; preserve the original |
| Simulate interrupted write/uncertain result | Reconcile read-only before any consequential retry |
| New AI reads a sanitized handoff | Verifies real sources; inherits **no** permissions |
| Delete an approved private record | Enforce scoped retention/erasure, including derived stores; disclose backup limitations honestly |

A written test list is **NOT RUN**, not PASS. A hash match means certain bytes agree; it does not prove that the information is true, that an external reviewer checked it, or that the system is secure.

## 7. What to request from your builder AI

Copy this requirement into [Stage 2](../prompts/stages/02_TASKS_EVIDENCE_RECOVERY.md) or the [advanced v0.5 master prompt](../prompts/BUILD_YOUR_OWN_AI_OS_v0.5_LIVING_CANDIDATE.md):

> Implement a versioned SQLite application-event journal with documented canonical record serialization and SHA-256 linked digests. Store actual events and evidence in the database; never treat hashes as the stored facts. On \`doctor\` or a cold restart, independently recompute the chain, check event order/IDs, verify source-bound task/evidence projections and original mission files, and reconcile against a separately trusted chain-tip checkpoint when available. Make consistent SQLite backups plus the required mission binder, restore only into a new approved destination, test deliberate tampering and interrupted writes, and preserve corrections and first failures subject to authorized deletion. Hashes do not provide encryption, authorship proof, independent audit, or automatic safe AI handoff. Report actual test receipts or NOT RUN.

The complete public guide remains educational. **No production memory-integrity gate, runnable app, independently reviewed security boundary or universal recovery guarantee is created by publishing these instructions.**

**Continue:** [Full staged build guide](STAGED_BUILD_PATH.md) · [Safe error recovery](ERRORS_AND_SAFE_RECOVERY.md) · [Memory-fidelity acceptance tests](MEMORY_FIDELITY_ACCEPTANCE_V1.md) · [Verification ledger](VERIFICATION_STATUS.md).
