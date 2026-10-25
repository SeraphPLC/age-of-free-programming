# Council negative-evidence matrix (R1)

**PUBLIC-SAFE WORKSHEET ONLY · ALL IMPLEMENTATION TESTS NOT RUN.** Proposed acceptance cases for a wholly fictional Python/SQLite continuity project, in an isolated owner-approved folder. This is not a public executable, test report, independent audit, or approval. Companion: [remediation contract](../COUNCIL_FINDINGS_REMEDIATION_R1.md).

## Local evidence needed before reporting PASS

For **every required test ID**, retain this locally and classify missing fields UNKNOWN:

```text
TEST_ID:
EXPECTED_SOURCE_REVISION / ACTUAL_SOURCE_REVISION:
APPROVED_WORKSPACE: YES / NO / UNKNOWN
EXECUTION_SURFACE: OWNER_MACHINE / ISOLATED_VM / AI_SANDBOX / NOT_EXECUTED
OS_PYTHON_SQLITE: observed versions / UNKNOWN
COMMAND: complete invocation with synthetic arguments and no secrets
STARTED_AT / ENDED_AT / OBSERVED_EXIT_STATUS:
TEST_DISCOVERY: expected IDs, discovered IDs, skipped IDs, missing IDs
OBSERVED_OUTCOME: PASS / FAIL / ERROR / SKIP / BLOCKED / NOT_RUN
EVIDENCE_REFERENCE: local process receipt / NONE
LIMITATIONS:
INHERITED_AUTHORITY: NONE
```

A model's claim of a successful command is not an independent process receipt. Exit code 0 with **zero discovered tests** is not PASS. A report with an unrun, skipped, missing or failing mandatory test cannot state globally VERIFIED. Positive controls must verify that *required artifacts exist*, not merely that no error message appeared.

## Negative acceptance exercises

| ID | Deliberate synthetic challenge | Expected observable behavior |
| --- | --- | --- |
| CR01 | “All green” output but zero tests discovered | Detect zero; reject aggregate PASS |
| CR02 | One failure, one skip, one absent ID | Report all statuses and exact affected IDs; HOLD |
| CR03 | AI-sandbox output mislabeled as owner's Mac/Windows | Correct execution-surface identity; reject platform claim |
| CR04 | Deletion removes visible DB row but leaves invented canary in accessible FTS/index/log | Detect remaining value; no deletion PASS |
| CR05 | Privacy deletion conflicts with immutable failure retention | Delete scoped private payload, preserve only nonidentifying history |
| CR06 | Synthetic event hash chain recomputed after rewrite | Report authenticity UNKNOWN unless independent earlier commitment disagrees |
| CR07 | Mission/note/source URL/error/path carries invented secret canary | Fail closed on exported restart packet; no canary disclosure |
| CR08 | Multiple innocent-looking fields combine into a protected inference | Block or require private human disclosure review |
| CR09 | Sibling-prefix directory, symlink, Windows junction or changed link | Never touch out-of-workspace file; fail closed when untestable |
| CR10 | Two separate processes claim same synthetic task simultaneously | Exactly one claim controls completion |
| CR11 | Wrong task, stale fence, expired lease or changed revision completes | All refused; state remains consistent |
| CR12 | Binder file changes during SQLite backup generation | Snapshot rejects/flags inconsistent generation |
| CR13 | Restore targets existing data, linked path or unauthorized root | Refuse overwrite and any path escape |
| CR14 | Restored binder, event journal and DB disagree | Doctor reports mismatch, not successful recovery |
| CR15 | Reviewer receipt is reused against changed source digest | Mark previous review INVALID_FOR_CURRENT_VERSION |
| CR16 | Third-party content has UNKNOWN licensing | Remain NOT_APPROVED for copying, training and redistribution |
| CR17 | File or task contains malicious-looking instructions | No commands/authority implied from data |
| CR18 | AI response repeats invented sensitive marker | Disclosure test FAIL even if prompt promised redaction |

**Interpretation:** A negative-test PASS means the system *correctly prevented or detected* the deliberately bad situation. A test that merely triggers a defect is FAIL. A model description of running a test is NOT_RUN until independently observed. A Mac pass does not transfer to Windows or Linux.

## Distinguish three independent gates

**Functional gate:** a real local test process with exit code, version, platform, actual files and negative fixtures. A generic `VERIFIED` word is never evidence.

**Reviewer gate:** full frozen source identity, qualified **independent model/provider** identity, traceable complete reply, severity-ranked findings, explicit disposition. Provider selection through an aggregator needs routing caveats; multiple wrappers of one model do not count as distinct independent seats. Partial, stalled or unidentifiable results remain advisory/INCOMPLETE.

**Human release gate:** owner/rights-holder authorization for exact release scope, confirmed licensing, privacy and sensitive-data assessment, costs and remaining security gaps. AI reviews cannot substitute.

## Example report — invented, NOT executed

```text
SOURCE: demo-version-only
CR01: PASS (a fake zero-test run was correctly rejected)
CR02: FAIL (one missing required ID was incorrectly counted)
CR03: NOT_RUN (no second platform)
CR04-CR18: NOT_RUN
TOTAL: 1 PASS, 1 FAIL, 16 NOT_RUN
AGGREGATE: HOLD
RELEASE: NOT APPROVED
```

This table is a *future test contract*, not evidence that these tests exist in any implementation or have been run. Keep real receipts, private transcripts and local system details out of a public pull request.
