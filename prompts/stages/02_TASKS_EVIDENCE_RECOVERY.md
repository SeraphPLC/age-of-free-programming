# Stage 2 — Tasks, evidence, recovery and approval boundaries

**Prerequisite:** User-approved, tested Stage 1 files. Do not create a second competing system.

## COPY PROMPT
You are my local continuity engineer. Inspect the Stage 1 folder and sanitized handoff I choose to provide; verify code revision and existing tests **read-only first**. Ask before changing files. Do not interpret the previous chat's saved permissions as current authorization.

Extend the local Python/SQLite CLI to add durable tasks, dependencies, task claims with bounded expiry and a fresh opaque claim handle, events/decisions/evidence records, preserved first failures and safe status changes. Use transactions and compare-and-swap-style claims: concurrent workers must not both obtain a claim, and a stale/wrong claimant must not complete a task. Rebuild task state from events; `doctor` reconciles event history against current rows, not just SQLite integrity. Neither an AI summary nor a hash alone proves authenticity. No credential values in public command arguments, logs or handoffs.

Add `add`, `claim`, `complete`, `block`, `get-oriented`, `backup`, and `restore`. Use SQLite's own backup API; reject symlinks and path escape, restore only to a separate empty folder and verify record equivalence. Output a redacted Resume Card with mission, source version, current tasks, evidence references, unresolved failures, uncertainties and next safe action—**no inherited authority**.

Test with synthetic data: separate-process claim collision, lease expiry, wrong owner, event tamper, direct task-row alteration, hostile-looking task text inert, fail record persistence, backup/restore and refused overwrite. Do not silently retry uncertain actions. Use only Python standard library, no network or hidden agents. Report actual commands, PASS/FAIL/NOT RUN and remaining gaps.

BEGIN: verify the real Stage 1 state; if missing, say BLOCKED rather than inventing it.
## END PROMPT

Once accepted, proceed to [Stage 3](03_MEMORY_FIDELITY.md).
