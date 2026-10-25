# Private offline AI OS build self-check

Keep this on your own computer. Do not upload it to GitHub, social media, or a public AI chat.

No account details, registration, analytics, or report submission required.

## Setup (generic only)
Prompt version:
Operating system family:
Python major/minor version:
Execution mode:

## Outcome (mark each test separately, not a single global PASS)
- [ ] NOT RUN — no observed check
- [ ] Stage 1: init/status/doctor observed for an exact source revision
- [ ] Stage 2: tasks, claims, handoff **and separate-directory backup/restore** checked
- [ ] Stage 3: source-backed facts, corrections and memory-fidelity checks observed
- [ ] PASS / FAIL / PARTIAL / BLOCKED / UNKNOWN / NOT RUN — choose per required check

**Never score a hypothetical example or a skipped mandatory test as PASS.** See [error labels and recovery](ERRORS_AND_SAFE_RECOVERY.md). Previous passing tests may be STALE when source or acceptance rules change. A first-party local PASS is not independent security qualification.

### BUILT
Functions created using synthetic tasks.

### VERIFIED
Non-secret command and exit code summaries; keep real logs private.

### FAILED, BLOCKED, OR UNKNOWN
Keep the first failure privately with the smallest useful, nonidentifying evidence. Do not copy personal machine paths, live logs or secrets into this form if it could leave your computer. A timed-out attempted write may have happened: mark `RECONCILE` and check authoritative state **before** a same-effect retry. Never delete partially created files to make a report look clean.

## Minimal per-check receipt (fictional labels only)

| Test ID | Expected | Observed executor/action | Observed exit or artifact | Result | Source revision | Retry / next action |
| --- | --- | --- | --- | --- | --- | --- |
| Example only: S1-01 | New folder | NO_TOOL / NOT_RUN | NOT_AVAILABLE | NOT_RUN | UNKNOWN | Approve a synthetic folder before testing |

Replace the example row only after an actual action; **do not prefill PASS**. Preserve a separate observed failure and any later repair receipt. Report skipped/undiscovered required tests as NOT_RUN. Use `MANUAL_PASS` only for a person who inspected the actual supplied artifact. If deletion is requested, preserve only permissible nonidentifying failure history and report unknown backup copies.

### NEXT SAFE ACTION
One bounded next step and permission needed.

## Privacy check
- [ ] No names, email, contact, government or account identifiers
- [ ] No username, private paths, hostnames, IP or screenshots
- [ ] No keys, tokens, cookies, passwords, banking data
- [ ] No medical, school, employment, family or personal records
- [ ] No real databases, backups, chat transcripts or private files

This is a self-check, not certification. For vulnerabilities in these public educational prompts see the repository SECURITY.md and use private reporting.
