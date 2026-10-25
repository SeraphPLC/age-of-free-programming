# R3 Local Security Review — October 24, 2026

**Experimental synthetic evidence only. Executable withheld; no software license or production security certification granted.**

This is a follow-on to the [historical Stage 1–2 model reproduction trial](STAGE2_PUBLIC_PROMPT_TRIAL_20261024.md). The prior model-generated Stage 2 failed five of thirteen negative checks; a separate supervised local version subsequently passed 57 first-party synthetic tests. **R3 is a further supervised hardening iteration**, not independent model reproduction.

## Three reproduced defects, before and after

| Negative test | Prior build behavior | R3 correction |
| --- | --- | --- |
| Local project permissions | Default newly initialized directory `0755`, SQLite database `0644`; retained after Stage 2 migration | Stage 1 now creates owner-only folder/file access (`0700`/`0600` on tested macOS); migration also restricts previously broad access |
| Task chronology | A synthetic completion could have a timestamp earlier than its own active claim and still be accepted | Event replay rejects completion **or blocking** earlier than the corresponding claim's start |
| Long task identifiers | A documented valid long task ID could create an oversized failure-record ID, preventing first-failure recording | Failure records use bounded deterministic IDs that remain valid at maximum supported task length |

These failures were **observed before the corrections**. Targeted tests were added, and the corrected behavior was observed afterward. The previous R2 ZIP and logs remain preserved separately.

## Actual R3 receipts

| Scope | Result |
| --- | --- |
| Supervised Python/SQLite test suite on first Mac, Python 3.9, 3.12 and 3.14 | **63/63 PASS** on each interpreter |
| Fresh R3 ZIP extraction on a second Mac, independent SHA-256 and per-file manifest verification | **63/63 PASS**, Python 3.9 |
| macOS deny-network process sandbox on both machines | **63/63 PASS** on each; an independent socket-control attempt confirmed networking was blocked |
| Focused Ruff security/bug-risk source rules | **PASS** under the selected S/B rules |
| Local synthetic continuity demo | **PASS** on both machines |
| Fresh AI chat independently building complete Stage 2 from public prompts | **NOT VERIFIED** |
| Independent professional security review | **NOT PERFORMED** |
| Windows/Linux portability | **NOT TESTED** on this R3 candidate |
| Personal-data retention/erasure/security certification | **NOT PERFORMED** |

The R3 package manifest identifies its 17 tracked source, test and documentation files plus a manifest. The package excludes private raw logs, model sessions, real account identifiers, network callbacks, external AI connectors and unrelated material.

**Byte-identification fingerprints:** Exact SHA-256 values for the R3 supervised Stage 1 source, Stage 2 engine and private review ZIP are retained in the owner-controlled private evidence manifest, not published here. Hashes are not proof of independent authorship, ownership or security.

The historical independently model-generated Stage 1 was originally preserved unmodified; **R3's Stage 1 has now been supervised-edited specifically to harden file permissions**. Do not attribute its R3 test result entirely to the original model-generated source.

## What these tests do not prove

A local hash chain **cannot authenticate history against someone who coherently rewrites the database and its hashes**. The CLI's synthetic approval flag and owner labels are not secure real-world authorization. File permissions cannot defend against privileged or same-user malicious processes. Evidence IDs can refer to unrelated or fabricated observations; a receipt is not an independent determination of truth or completion quality. Local backup files, journal remnants and exports are not covered by a validated deletion or retention program.

Separate-process recovery is **not** a fresh-chat or long-term AI memory test. Running a suite on two Macs is not Windows/Linux qualification. A first-party regression suite, even with adversarial tests, is not an independent security audit.

## Actionable changes for public builders

The [Stage 1 prompt](../prompts/stages/01_OFFLINE_CORE.md) now requests owner-only access **immediately after initialization**, checks that the actual mission file exists, and refuses personal data when access restrictions cannot be enforced. The [Stage 2 prompt](../prompts/stages/02_TASKS_EVIDENCE_RECOVERY.md) now specifies temporal ordering, maximum task-ID failure preservation, repeat-migration permissions and distinct journal/projection corruption tests.

Use the [public negative-test checklist](STAGE_1_2_NEGATIVE_TEST_CHECKLIST.md) as a human-readable acceptance contract; it is **not executable code** and no model's unsupported PASS assertion should be accepted.

**Release gate unchanged:** executable held privately pending explicit software licensing, genuine independent code/security review, trustworthy authority and source provenance, personal-data privacy safeguards, true fresh-chat reconstruction, and Windows/Linux portability checks.
