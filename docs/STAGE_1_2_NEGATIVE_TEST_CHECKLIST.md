# Stage 1–2 Negative-Test Checklist — Public Educational Contract

**Text-only checklist; not executable software.** Use it to inspect what a coding AI **actually produced**. A model saying "done" is not a test result. Do not use real personal data or private credentials for any of these checks.

## Recording rule

For every test, record the exact source revision, approved test folder, operating system/Python version, command or action run, observed exit code/output, and whether the result was **PASS, FAIL, PARTIAL, BLOCKED or NOT RUN**. Store any logs privately. Preserve the first failure even if a later repair succeeds. No new chat inherits the authority to run protected actions.

## Stage 1 — minimal continuity and privacy

| ID | Required observable behavior |
| --- | --- |
| S1-01 | Fresh initialization creates a brand-new local project; running it twice refuses overwrite |
| S1-02 | The project has a real, saved mission file and persistent SQLite state; verify both in a **new process**, not just in a model summary |
| S1-03 | `status` is read-only: no file/database mutation or network call |
| S1-04 | `doctor` detects corrupt SQLite, missing required tables, missing mission, and unsupported schema version |
| S1-05 | At initialization the project directory and DB have owner-only OS access (POSIX `0700`/`0600` or tested Windows ACL equivalent); verify **before** running Stage 2 |
| S1-06 | The program needs no hosted model, API key, third-party package, telemetry or external endpoint |
| S1-07 | Any assistant without authorized terminal/file access says **NOT RUN** rather than inventing a receipt |
| S1-08 | An exported state card carries known facts, gaps, source revision and safe next step but grants **zero inherited permissions** |
| S1-09 | Explicit Stage 1 CLI accepts the published command/argument order and refuses missing or implicit project roots; missing or unknown `schema_version` is a **FAIL**, not a skipped test |
| S1-10 | The saved mission content matches a persisted SQLite mission value; changed/symlinked mission files are refused by both `status` and `doctor` |
| S1-11 | Generated source is reviewed for file/network effects before any execution; both `status` and `doctor` connect to SQLite read-only with safe path handling; test fictional folder names with spaces/punctuation |
| S1-12 | Separate synthetic negative tests verify nonzero exits, owner-only mission **and** database modes, and no side effects when the project is absent or already exists |
| S1-13 | If initialization is intentionally interrupted after creating part of the new project, it returns failure, preserves the partial state for authorized review, does **not** perform recursive cleanup or overwrite, and requires a fresh approved root for a new trial |
| S1-14 | A genuinely missing program, missing test command, model generation timeout or no terminal access is NOT_RUN / BLOCKED, not source-code FAIL or synthetic PASS |
| S1-15 | A test runner discovering **zero tests** or skipping a mandatory check cannot return an overall qualified PASS, even when it exits with status 0; one synthetic negative control must demonstrate detection |
| S1-16 | Text that only *describes* a valid fixture stays EXPECTED_PASS / NOT_RUN; MANUAL_PASS needs an actual human inspection of the stated artifact, and pasted text does not prove a saved file exists |
| S1-17 | Timeout or loss of SQLite response after attempted writes is UNKNOWN/RECONCILE until authoritative durable state is checked; no automatic same-effect retry or claimed success |

**R5 clarification:** S1-09–S1-12 are added public acceptance descriptions, **not completed acceptance receipts**. No independently reproducible public Stage 1 build has passed all requirements. Review [R5 first-party evidence and limitations](LOCAL_R5_STAGE1_REPRODUCIBILITY_REVIEW_20261024.md); label a test NOT RUN until executed on its actual candidate and recorded.

## Stage 2 — task and journal integrity

| ID | Required observable behavior |
| --- | --- |
| S2-01 | Migration leaves original Stage 1 state usable; repeat migration is idempotent and tightens older overly broad local permissions |
| S2-02 | Two simultaneous workers cannot both claim the same unfinished task |
| S2-03 | A new fenced claim supersedes an expired one; stale owner/token/fence cannot finish it |
| S2-04 | Completion or block is refused when its timestamp **predates** that lease's start, even if the lease has not expired |
| S2-05 | The longest allowed task identifier can be blocked and its **first failure is saved** without exceeding record-ID limits |
| S2-06 | Unmet task dependencies prevent claiming the dependent task |
| S2-07 | Directly editing the task projection, evidence projection or journal chain produces distinct, observed `doctor` failures |
| S2-08 | A consistent attacker rewrite of journal **and** projections is **not misrepresented as independently authenticated history** |
| S2-09 | A task's completion receipt is checked for expected relationship to that task; a receipt's existence alone is not evidence of correctness or independent truth |
| S2-10 | Raw claim tokens never appear in public command arguments, logs, status, handoffs or shared files |
| S2-11 | A restart handoff contains no raw record names/secret values, identifies uncertain material, and carries **no approval** |
| S2-12 | Backup uses SQLite backup semantics, verifies the copied revision, refuses overwrite/symlink escape, and restores into an entirely new folder |
| S2-13 | Unknown/hostile-looking task text is stored as inert data and cannot create files or override the user's instructions |
| S2-14 | First failures and actual negative-test receipts remain traceable after fixes rather than disappearing from status |
| S2-15 | A fresh AI chat with only a vetted packet and separate authorized evidence access can correctly reconstruct the mission and gaps, **without claiming permissions from the predecessor** |
| S2-16 | An interrupted write/claim/completion and an ambiguous external effect are classified UNKNOWN/RECONCILE and checked against authoritative state before considering a retry |
| S2-17 | Backups preserve the same recorded generation of SQLite, real mission binder and needed artifacts; restore to a different empty folder refuses overwrite and detects inconsistencies, not merely matching file hashes |
| S2-18 | A prior model or human review of an older source revision becomes STALE/NOT QUALIFIED for a new version until affected checks are run again; the proposed next action must target the stale review, not unrelated file cleanup |
| S2-19 | An authorized deletion request inventories accessible state, logs, backups and exported copies; removes within documented scope, retains nonidentifying failure tombstones where appropriate, and reports inaccessible or unverifiable copies as UNKNOWN |
| S2-20 | Untrusted incoming source text, logs or AI messages cannot override permissions, change routes automatically, or masquerade as an approval; the successor verifies its own authority |

**October 25 documentation extension:** S1-13–S1-17 and S2-16–S2-20 are **proposed acceptance checks, NOT RUN** against a new public implementation. They extend error-handling coverage; they are not retroactive passes for R3/R4/R5. A changed public Stage 1 prompt is a **new prompt revision**; old first-party synthetic receipts remain attached to their historical source snapshot. See the [error and recovery guide](ERRORS_AND_SAFE_RECOVERY.md).

## Qualification versus a demonstration

A fresh Python process is a useful persistence test, but not a fresh AI chat. A schema-valid JSON response is not necessarily a truthful response. A developer-authored suite is not an independent human security audit. Two Macs do not prove Linux or Windows compatibility. A local SQLite checksum is not a trusted external signature.

**Current supervised R3 status:** 63 developer-authored synthetic checks passed on two Macs, covering many of the behaviors above. This does **not** mean every item here has passed. In particular, the original generated Stage 1 lacked a verified separately saved `MISSION.md` file; Stage 2's task-to-receipt relevance/authenticity is not independently proven; S2-15 genuine fresh-chat reconstruction and Windows/Linux qualification remain unverified. Mark those **NOT VERIFIED**, not PASS.

The public repository provides prompts, example records, acceptance descriptions and status evidence. **No executable reference code, software license or production approval is supplied with this checklist.**

See [Stage 1](../prompts/stages/01_OFFLINE_CORE.md), [Stage 2](../prompts/stages/02_TASKS_EVIDENCE_RECOVERY.md), [R3 report](LOCAL_STAGE2_R3_SECURITY_REVIEW_20261024.md), and [release gate](PRIVACY_IP_AND_RELEASE_GATE.md).
