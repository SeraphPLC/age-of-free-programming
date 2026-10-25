# Tell us whether it worked

**Public visibility warning:** GitHub Issues are public and may be indexed, copied or archived. Do not upload full real logs, project archives, screenshots containing identifiers, email/phone/address, account details or personal case history. Security vulnerabilities belong in [private reporting](../SECURITY.md), never in a public Build Report.

This free community project measures **reproducible builds**, not impressions or claims about AI autonomy.

**[Create a new Build Report](https://github.com/SeraphPLC/age-of-free-programming/issues/new?template=build-report.md)**

Please report (only if you wish): your operating system, Python major/minor version, model/chat provider, which prompt version you used, and how far you got.

## Outcome definitions

- **Stage 0 / NOT STARTED:** Prompt read, no commands executed.
- **Stage 1 / INIT + STATUS:** A new project initialized, status and doctor were executed with visible receipts.
- **Stage 2 / TASKS + HANDOFF:** A task was created, safely claimed, checked, and resumed from a new process or chat.
- **Stage 3 / BACKUP + RESTORE:** A SQLite backup restored into a different, empty directory and matched expected records.
- **PARTIAL / BLOCKED:** The build stopped for missing tools, permission, errors, or unsupported steps.

Do not claim a stage PASSED unless you can identify commands that ran and what they returned. A self-report is not a third-party verification.

## Keep your report safe

No names of family members, identifying task content, full file paths containing personal names, addresses, account emails, private IP addresses, authentication tokens, actual databases, raw private logs, or real Resume Cards. Replace sensitive material with `[redacted]`. Use synthetic examples only.

When something fails, share a **sanitized** error and exact *non-secret* command. Reporting a failure is useful progress.

**Reviewers:** label outcomes `SELF-REPORTED`, `REPRODUCED`, or `INDEPENDENTLY REVIEWED` only when corresponding evidence exists. Never upgrade a claim because an AI says it reviewed its own output.
