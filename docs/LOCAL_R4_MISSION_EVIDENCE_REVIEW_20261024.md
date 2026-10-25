# R4 Mission, Evidence and Clean-Room Review — October 24, 2026

**PUBLIC-SAFE DOCUMENTATION ONLY · EXECUTABLE RELEASE HELD · NO NEW LICENSE**

R4 continues the [historical R3 security review](LOCAL_STAGE2_R3_SECURITY_REVIEW_20261024.md) for the separate experimental Python/SQLite continuity candidate. The real source, test data and failure logs remain on privately controlled local machines. **No Seraph private code, connector credentials, cloud API, personal records, machine identifiers, model weights or remote callbacks were included.** The candidate is a supervised, developer-authored continuation, not an independently model-generated Stage 2.

## Defects observed before correction

| Defect | Actual negative finding | R4 correction |
| --- | --- | --- |
| Durable mission | Stage 1 reported successful initialization without creating the required real `MISSION.md` | Create the file and bind its exact contents to the SQLite mission and local digest; `doctor` refuses missing, modified or symlinked binder |
| Task evidence | A receipt about fictional Task B could complete Task A, while the consistency checker still reported healthy | Bind self-reported synthetic observations to a specific task and task-description digest; mismatched or tampered binding cannot complete another task |
| Backup completeness | Prior backup format contained SQLite but not a separately verified mission file | Include `MISSION.md` in backup, manifest and new-folder restore checks |
| Concurrent read/write | A repeat race test encountered an intermittent SQLite write error; a single prior pass was insufficient | Use consistent read snapshots and treat uncertain write failures as **UNVERIFIED**, without automatic retry |

These were first observed on a separate copy; the R3 package and its original logs remain unchanged.

## Verified R4 synthetic results

| Scope | Observed |
| --- | --- |
| First-party automated suite, Python 3.9, 3.12 and 3.14 on one Mac | **78/78 PASS per interpreter** |
| Fresh ZIP transfer/extraction and hash/manifest verification on a second Mac | **78/78 PASS**, Python 3.9 |
| Operating-system network-denied sandbox, both Macs | **78/78 PASS** per Mac; blocked-connect control independently confirmed denial |
| Focused source lint (Ruff S/B) | **PASS** under those selected rules |
| Repeated competing-worker completion test | **10/10 runs PASS** after read/write consistency correction |
| Synthetic local-process continuity demonstration | **PASS** on both Macs |
| Qualified independent human security audit | **NOT RUN** |
| Genuine fresh browser AI-chat Stage 1–2 recreation | **NOT QUALIFIED** |
| Windows/Linux qualified portability | **NOT RUN for R4** |

The R4 ZIP has a different fingerprint from R3, is private, and is not a public download. Its exact review-only SHA-256 is retained in the owner-controlled private evidence manifest, not published here. Hashes document byte identity, not code safety or legal ownership.

**Historical visibility:** Earlier public Git commits and pull-request diffs still expose the previously published fingerprints; forks and caches may retain them. This edit does not erase historical exposure.

## Independent public-prompt reproduction: negative receipts

Separate direct local coding-model calls received the frozen **public Stage 1 prompt**, not the supervised R4 source. Models had no terminal tools; a distinct harness tested their generated source. No Codex was used.

- **First Devstral generation:** **1 of 12** synthetic Stage 1 acceptance checks passed. Initialization failed; an additional pre-execution inspection found an unsafe, destructive cleanup pattern and duplicate executable entry point. The source was quarantined rather than accepted.
- **First Qwen coding-model generation:** syntax/static import checks passed, but Stage 1 initialization failed and only **1 of 12** tests passed.
- **First Qwen model-generated repair:** **10 of 12** tests passed under a strengthened harness. It still failed owner-only file permissions and lacked the required versioned SQLite schema.
- **Second Qwen repair:** failed syntax validation (placeholder response rather than executable source). No code was accepted or run.
- **Fresh GPT-OSS model generation:** a separate direct local inference attempt using only the public Stage 1 prompt **timed out after 180 seconds without producing source code**. No acceptance tests were run for that model; its build is **NOT QUALIFIED**, not PASS. The timeout is preserved in private evidence.

A fresh local inference session is not the same as a genuinely fresh browser AI chat with independent source retrieval and current authority. Model-generated programs are not self-certifying. The experiments demonstrate the value of **source inspection before running and stage-specific negative tests**, not successful independent Stage 2 reproduction.

## Important scope and release boundaries

- Stage 1 still uses SQLite schema 1. R4 uses Stage 2 schema **2** to record task-specific evidence; the earlier R3 Stage 2 schema 1 is deliberately **not upgraded automatically**. Do not point R4 at an existing real R3 database or claim a migration path.
- Every task-specific observation in this educational candidate is **self-reported synthetic evidence**, not independent verification that an action truly happened.
- Local event hashes can be coherently rewritten by a local attacker controlling all stored history. There is no independently anchored authentication of the record.
- Owner labels and a synthetic confirmation flag are not verified identity or production authorization. Local backups and exports do not have certified privacy erasure.
- No real medical, academic, banking, family, account or organizational information is authorized for this experimental build.
- Ownership/licensing clearance, independent human audit, Windows/Linux testing, cross-model long-term fidelity, and genuine fresh-chat recovery remain unfulfilled.

**Release decision: HOLD.** The public repository continues to provide educational prompts, schemas, safety gates and sanitized test methodology, not the executable or private infrastructure.

See [Stage 1 public builder](../prompts/stages/01_OFFLINE_CORE.md), [Stage 2 public builder](../prompts/stages/02_TASKS_EVIDENCE_RECOVERY.md), [Negative-test checklist](STAGE_1_2_NEGATIVE_TEST_CHECKLIST.md), and [Verification Status](VERIFICATION_STATUS.md).
