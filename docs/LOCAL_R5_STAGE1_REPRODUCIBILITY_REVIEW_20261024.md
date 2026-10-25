# R5 Stage 1 reproduction and qualification — October 24, 2026

**Public-safe, documentation-only synthesis · Educational candidate · Executable release HOLD**

This review follows the [R4 mission/evidence report](LOCAL_R4_MISSION_EVIDENCE_REVIEW_20261024.md) and should be read with the [Stage 1 prompt](../prompts/stages/01_OFFLINE_CORE.md) and [verification ledger](VERIFICATION_STATUS.md). It describes only scoped first-party synthetic testing. No raw model replies, privately held executable, account information, local-machine identifiers, internal infrastructure, or sensitive private findings are distributed.

## What was tested

| Workstream | Actual observed result | Qualification |
| --- | --- | --- |
| Prior supervised R4 Stage 2 candidate | 78/78 first-party synthetic cases passed on two Macs, as previously reported | NOT an independent generated/released program |
| R5 local full-source model generation/repair series | 16 distinct generation/repair attempts under mixed prompt conditions; sources and first failures preserved privately | Independent public-prompt-only Stage 1 NOT QUALIFIED |
| Model-generated Stage 1 repair | 14/14 first-party synthetic behavior checks passed on two Macs, but an additional read-only database requirement **failed** | NOT QUALIFIED |
| Separate supervised Stage 1 correction | 14/14 first-party synthetic tests passed on two Macs (three Python versions on one); extra fictional path-name scenarios passed | SUPERVISED, first-party experimental result only |
| Later local model given the frozen **public Stage 1 prompt only** | Generation timed out after 300 seconds, without producing usable source | GENERATION BLOCKED; executable tests NOT RUN |
| R5 independent Stage 2 from a qualified public-only Stage 1 | NOT RUN | BLOCKED by the Stage 1 prerequisite |
| Independent human security audit, Windows/Linux qualification, production identity, secure deletion/retention and explicit rights clearance | NOT VERIFIED | Release HOLD |

These observations have different provenance. Some R5 model trials were given an **unpublished, proposed Stage 1 clarification** as well as the frozen public instructions; repairs sometimes received their own earlier generated code. Neither those runs nor supervised corrections prove the exact current public prompt can be independently reproduced by an ordinary new AI chat. A local model inference session is not a fresh browser chat.

## What the failures teach

- **Start small and specify observable interfaces.** Ambiguous command order, version metadata and saved mission behavior can yield non-interoperable but syntactically valid programs.
- **Save the real mission twice, consistently.** Merely creating a Markdown mission file or placing a version key in SQLite does not prove that the persisted mission is bound to its database record.
- **Test owner-only filesystem permissions and real read-only behavior.** A successful startup message or unchanged database after one read is insufficient.
- **Check filesystem edge cases before declaring completion.** Supplemental tests found that a prior supervised copy behaved differently for some ordinary folder names. A new supervised copy passed the additional synthetic checks. This is a functional lesson, not a disclosure of private systems.
- **Inspect generated source before running it.** Some attempts produced unsafe or incomplete cleanup, misleading success status, or unintended file behavior. Such candidates were rejected or quarantined; a syntax check is not authorization to execute.
- **Never promote timeouts or skipped tests to passes.** Preserve first failures, model-generated repairs and supervised edits under distinct labels.

## Minimum usable Stage 1 gate

A beginner should obtain a complete reviewed Python/SQLite CLI with `init`, `status`, `doctor`, a separately saved `MISSION.md`, versioned SQLite metadata, owner-only initial permissions, refusal to overwrite existing folders, and observed negative tests. Tests must use fictional tasks in a new approved directory, with genuine command outputs and nonzero failures. [Use the updated public Stage 1 contract](../prompts/stages/01_OFFLINE_CORE.md) and [negative-test checklist](STAGE_1_2_NEGATIVE_TEST_CHECKLIST.md), whose additional R5 checks remain unqualified for a public independent build.

**Do not begin Stage 2 until Stage 1 qualifies on its actual source revision.** A new chat inherits no previous permission. The public project remains educational: it does not contain a downloadable executable, a qualified confidentiality filter, a selected general software redistribution license, or an independently authenticated history mechanism.

## Status and next action

**Decision: HOLD.** The next high-value trial is a genuinely fresh public-prompt-only reproduction against the precise published contract, followed by a separate source review and observable tests. Independent review, cross-platform qualification, rights/licensing, and genuine fresh-chat recovery remain necessary before any runnable public release. See the [privacy/IP/release gate](PRIVACY_IP_AND_RELEASE_GATE.md).

This summary is an educational description of privately recorded first-party results. It is not a certification, a private artifact map, or authorization to release the underlying code.
