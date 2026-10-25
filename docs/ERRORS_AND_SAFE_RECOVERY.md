# When something fails — a small, safe recovery guide

**Public educational instructions · October 25, 2026 · NOT executable software or a tested automatic error detector.** Use invented examples and your own approved workspace. This guide is for Stage 0 chat-only handoffs and optional Stage 1–2 local builds. The [output disclosure gate](OUTPUT_DISCLOSURE_GATE.md) and [privacy/release policy](PRIVACY_IP_AND_RELEASE_GATE.md) still apply.

**First rule:** A failed or interrupted operation is not a reason to restart the whole project. Preserve the original observation privately, determine whether anything may have changed, and take **one bounded next action**. Do not run AI-generated cleanup, reset state, disclose real error logs, or retry consequential writes automatically.

## 1. First-minute checklist

1. **Stop risky actions.** If an unexpected change, privacy exposure, uncertain write, permission problem or data-loss risk appears, stop further writes, sharing, publishing and automatic retries. Do not close a possibly running process merely because its output is slow; check its real status first.
2. **Establish what you can observe.** Name the actual source revision, stage, test ID, approved synthetic folder, real executor and outcome. If you only have a chat message, you have a *claim*, not proof of a command.
3. **Check for side effects read-only.** Did the program create files, alter SQLite, send something, or complete a task? If you cannot know, mark `UNKNOWN / RECONCILE`. Do **not** invoke the same effect again until the authoritative state is checked.
4. **Keep the first failure private.** Retain the smallest useful safe receipt under the owner's control; don't post raw traceback paths, user names, logs, credentials or live system configuration. If even the receipt is sensitive, store a redacted summary and mark the detail WITHHELD.
5. **Choose the least risky path.** Repair in a new, isolated synthetic copy, ask for fresh approval when needed, or use a manual handoff. Old chat permissions and supposedly completed tests never transfer to a replacement worker.

## 2. Outcome labels: predictions are not receipts

| Label | Use only when | Never confuse it with |
| --- | --- | --- |
| `EXPECTED_PASS / EXPECTED_FAIL` | Describing a designed example or intended outcome **before** inspection | A real PASS or FAIL |
| `NOT_RUN` | No relevant command, file inspection or human check actually occurred | SKIPPED, BLOCKED, PASS |
| `BLOCKED` | A required tool, approval, source, platform or prerequisite is absent; append `(NOT_RUN)` for unexecuted checks | Failed code or completed tests |
| `PASS` | The exact source version and required check were observed to meet the stated criterion | A model's confidence, static syntax check, predicted result or exit code 0 from zero tests |
| `FAIL` | Actual evidence contradicts the criterion, or reviewed source has a definite pre-execution defect | A network/model timeout with no resulting code |
| `PARTIAL` | Some observed subchecks passed but at least one mandatory check is absent, failed or blocked | Full qualification |
| `UNKNOWN` | An attempted action's outcome cannot be determined from reliable evidence | A safe-to-retry failure |
| `RECONCILE` | A write, publication, send, payment or other external consequence **might** already have happened | Permission to retry |
| `STALE / INVALIDATED` | A prior PASS refers to changed source, an inadequate test, or a known false-green | Deleting the original historical receipt |
| `WITHHELD` | The content, destination, audience, sensitivity or rights make disclosure inappropriate | A promise that the hidden data was safely erased |

**Manual versus automated:** `MANUAL_PASS` is allowed only when a real person actually inspects the stated artifact and records the check. A model merely reading an example cannot invent human inspection. The text pasted in a chat may be inspected *as pasted text*, but this does **not** prove that an unseen file exists or was tested. A syntax check or AST scan does not make untrusted generated code safe to execute.

**Case-specific next action:** A model can produce a plausible status label but suggest an irrelevant recovery step borrowed from another error. Confirm that the proposed action addresses the **observed** failure and exact source revision, requires no extra authority, and cannot alter existing data unexpectedly. A stale review calls for targeted revalidation, **not** automatic folder cleanup.

**Distinguish project state from test result:** A correctly observed refusal of an unsafe operation (for example an existing root, symlink escape, or unsupported schema) can be **PASS for the protective negative test**, while the attempted operation remains REFUSED and the project remains unqualified. If the protection fails to reject the unsafe input, that negative test is **FAIL**. Record both the incident and the test disposition; a nonzero exit is not automatically a failed test.

**Interrupted process caveat:** A forced termination, power loss, or lost process handle might provide **no reliable exit code**. Never invent one. Record the observed partial artifacts and mark unconfirmed effects `UNKNOWN / RECONCILE` until authorized read-only reconciliation is complete.

A required test omitted from discovery is `NOT_RUN` and prevents overall qualification. A required test intentionally skipped remains `SKIPPED / NOT_RUN` for qualification; if a tool cannot run, use `BLOCKED (NOT_RUN)`. A suite with zero tests and exit code 0 is **not PASS**. Keep both the *claim* and the *observed result* when they disagree.

## 3. What to do for common failures

These are examples of **expected safe responses**, not claims that an installed AI OS implements them.

| Symptom or error family | Record | Next safe action / stop condition |
| --- | --- | --- |
| AI says “I ran it” but has no tool or receipt | `EXECUTION_UNOBSERVED / NOT_RUN` | Ask for the actual command, executor and output; otherwise provide instructions for a person to run, not a claimed pass |
| Model generation timed out, returned a placeholder, or produced no source | `GENERATION_BLOCKED / NOT_RUN` | Preserve request boundary and provider outcome; change model/prompt only as a **new** generation, never as a tested software result |
| Generated source contains unsafe cleanup, unapproved paths, network activity or hidden actions | `SOURCE_REJECTED / FAIL` | Quarantine before execution; never run it just to see what happens |
| Test runner found zero tests, skipped a mandatory check, or printed a canned PASS | `FALSE_GREEN / NOT_RUN or FAIL` | Fix discovery and independently run positive **and** negative controls; preserve original misleading claim |
| `init` sees an existing folder, unexpected symlink or path outside approval | `PATH_REFUSED`; protective negative test **PASS** only if refusal was observed | Refuse overwrite; select a new owner-approved synthetic root; do not silently change permissions on unrelated files |
| `init` is interrupted after creating some files or SQLite tables | `PARTIAL_INIT`; observed artifacts known, final outcome may remain `UNKNOWN / RECONCILE` | Inspect the partial folder read-only; do not invent an exit status, auto-delete, or reuse it; seek current approval for any repair or disposal |
| `MISSION.md` is missing, changed, linked, or disagrees with SQLite | `MISSION_MISMATCH` in project state; protective test **PASS** if `status` and `doctor` correctly reject the mismatch | Preserve both versions and require an explicit reconciliation decision; failure to detect the mismatch is a test **FAIL** |
| SQLite is locked, corrupted, or has an unknown schema | `DB_BUSY / BLOCKED` for a lock; `DB_INVALID / FAIL` for confirmed corruption or unsupported schema | Record the exact observation; a correctly observed protective refusal may be a **PASS for the negative test**. Never auto-migrate, recreate, or overwrite; inspect active writers before considering any retry |
| `status` or `doctor` creates files, writes sidecars, or exits zero on an error | `READ_ONLY_BREACH / FAIL` | Stop promotion; inspect read-only connection and real exit code; test on fictional paths containing spaces or punctuation |
| Project/database/mission permissions are overbroad | `PERMISSION_FAIL / FAIL` | Stop real-data use; test effective permissions or ACLs on the relevant platform before any further stage |
| Two workers claim the same task, or a stale lease reports completion | `CLAIM_CONFLICT / FAIL` | Verify durable state and lease/fence before another action; refuse completion from stale credentials |
| SQLite write or task completion times out after invocation | `WRITE_OUTCOME_UNKNOWN / RECONCILE` | Check authoritative durable task/event state; **no automatic same-effect retry** or completion PASS |
| Evidence exists but refers to another task, a changed source or a fabricated reviewer | `EVIDENCE_MISMATCH / FAIL` | Rebind or rerun only after authorized correction; never call an internal hash a trusted external signature |
| Backup/restore fails, has an inconsistent mission or targets an existing directory | `SNAPSHOT_UNVERIFIED / FAIL or BLOCKED` | Keep original, reject overwrite, review snapshot generation and restore only to a new empty approved folder; verify actual recovered records |
| A local session stops, the AI window ends, or a handoff is stale | `SOURCE_STALE / UNKNOWN` | Check current source and open loops; rebuild a small sanitized card; a successor must obtain its own permissions |
| An external send, commit, purchase or publication gives no final receipt | `EXTERNAL_OUTCOME_UNKNOWN / RECONCILE` | Read the authoritative destination with current permission before considering a new action. Never guess “failed, retry” |
| Protected data, inferred identity or access details appear in an answer or error log | `PRIVACY_BOUNDARY_FAIL / WITHHELD` | Stop external output, avoid repeating the content; handle privately through [security reporting](../SECURITY.md) when relevant |
| Owner asks to delete data that a failure log or backup still contains | `RETENTION_REVIEW / BLOCKED` | Stop collection; inventory reachable copies, delete only within confirmed authority, replace detail with a nonidentifying tombstone; report inaccessible copies and limits honestly |
| Rights to code, research, assets or a brand are unknown | `RIGHTS_UNKNOWN / HOLD` | Use original fictional educational text and seek qualified rights-holder review; public readability is not a redistribution license |
| Old tests passed, but source code or the acceptance contract changed | `SOURCE_STALE / NOT QUALIFIED` | Identify affected checks and repeat them on the exact new revision; do not carry old PASS forward or perform unrelated cleanup |
| Platform, model or reviewer is unverified | `QUALIFICATION_UNKNOWN / NOT_RUN` | Mark Windows/Linux, fresh-chat, external-review or source-version-specific gates untested; never inherit another version's PASS |

**SQLite and file safety:** SQLite's transactional guarantees do not mean an interrupted caller knows whether its commit took effect. For real builds, require a read-only verification step before retrying consequential operations. A backup API or matching digest does not by itself prove that the mission file, SQLite data, event history and permissions came from one consistent, authorized snapshot. File-symlink/path checks should be designed against handle-based races and verified on each intended operating system; string-prefix checks alone are insufficient.

## 4. Minimal private failure receipt

Use this **on your own computer**; do not paste a completed report containing personal or machine data into a public chat. Put raw data in a protected local record only when retention is justified.

```text
RECORD: fictional-error-01
PROJECT: imaginary-library
STAGE / SOURCE_REVISION: Stage 1 / version UNKNOWN
ACTION / TEST_ID: init / S1-01
ACTUAL_EXECUTOR / COMMAND: NO_TOOL / NOT_RUN
OBSERVED_EXIT / OUTPUT: NOT_AVAILABLE / NOT_AVAILABLE
EXPECTED_OUTCOME: New empty folder containing mission and SQLite
ACTUAL_OUTCOME: NOT_RUN
POSSIBLE_SIDE_EFFECT: NONE_BY_THIS_CHAT; OTHER_WORKERS_UNKNOWN
FIRST_FAILURE_REFERENCE: local-private-reference-or-NONE
AUTOMATIC_RETRY: NO
AUTHORITY: NONE_INHERITED
DISCLOSURE: WITHHELD_FOR_PRIVATE_DETAILS
NEXT_SAFE_ACTION: Ask for a new synthetic folder and current approval
```

In an actual receipt, **do not write `UNKNOWN` if a specific result was observed**, and do not invent an exit code, reviewer, timestamp, source hash or file path. If a test is rerun, keep the first failure record separate; bind the new result to the new source revision. Use [the private offline self-check](BUILD_REPORT_TEMPLATE_OFFLINE.md) and [Stage 1–2 negative tests](STAGE_1_2_NEGATIVE_TEST_CHECKLIST.md).

## 5. Safe restart, cleanup and data-retention boundary

- If the last process might still be writing, inspect its real status. Avoid two overlapping writers or restarting the same write while its outcome is unresolved.
- Keep original source and failure evidence untouched where authorized, but **preserving failures does not override a legitimate deletion request**. Minimize retention, protect access, and accurately report unverified backups/caches; do not promise SSD-level erasure.
- When a source or acceptance checklist changes, re-evaluate affected tests. Old tests remain historical observations, but their PASS cannot be silently promoted to a new version.
- A successful synthetic scenario is **not** proof of production security, independent AI Council review, real-data privacy, Windows/Linux portability or a working background service.
- Keep every handoff and error message free of credentials, absolute private paths, personal records and real vulnerabilities. A new chat can review sanitized facts; it does not inherit login state, tools, licenses or action permissions.

**Still stuck?** Stop at `BLOCKED / UNKNOWN / HOLD` with one narrow next action. The project is doing its job when it refuses to manufacture certainty. See [handoff and interrupted-worker recovery](learning-routes/04_HANDOFF_EVIDENCE_AND_RECOVERY.md), [disclosure policy](OUTPUT_DISCLOSURE_GATE.md), and [current verification limits](VERIFICATION_STATUS.md).

**Publication/implementation status:** These rules are a documentation proposal. They have **not** been implemented, run as an automated error detector, independently security-audited or cleared as a public executable. The Stage 1 independent reproduction and R5 Stage 2 gates remain open; software release stays on **HOLD**.
