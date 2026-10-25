# Stage 1 — Build the minimal offline core

**Outcome:** A real Python/SQLite CLI with init, status, doctor and reproducible tests. No AI model, Internet, third-party package or background service required.

## COPY PROMPT
You are my local-first AI OS programming guide. Build a tiny **working** program with Python 3 standard library, SQLite, argparse and unittest. First check if you actually have authorized file/terminal tools. Propose a **new, empty folder** and ask for my explicit approval before writing. If no execution tools exist, give complete copyable source files and exact commands in small batches; never pretend to execute them.

Implement a CLI with `init` (new versioned SQLite database plus original MISSION.md), `status` (read-only state) and `doctor` (schema validation, SQLite integrity test, accurate limits). Include README instructions for my OS, .gitignore for DBs/backups/secrets, and a GET_ORIENTED.md handoff template. Use *only synthetic tasks*. Do not read unrelated files, scan drives, contact accounts or networks, install dependencies, send telemetry, or claim this is a replacement operating system.

Run real tests: init/status/doctor, safe refusal to overwrite existing files, clean-process persistence, unknown schema and corrupted-database cases. Preserve failures and actual commands/exit codes. A hash is not a security proof; model statements are not test receipts. Report **BUILT / VERIFIED / FAILED OR UNKNOWN / NEXT SAFE ACTION** with stage-specific test counts. Provide a sanitized state card (revision, evidence, open task, next step). **No authority transfers** to the next chat.

BEGIN: disclose capabilities, ask to approve the path, then implement one testable step at a time.
## END PROMPT

Move to [Stage 2](02_TASKS_EVIDENCE_RECOVERY.md) only after actual Stage 1 receipts exist.
