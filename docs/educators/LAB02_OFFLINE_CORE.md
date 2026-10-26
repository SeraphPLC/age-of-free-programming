# Lab 2: inspect and test an offline Python/SQLite continuity core

**Optional advanced lab | Target 60-90 minutes for introduction; actual build may exceed that | NOT RUN as a student lab**

This is a supervised teaching **plan**, not a distributed executable. The public project provides [Stage 1 requirements](../../prompts/stages/01_OFFLINE_CORE.md), not a certified `ai_os.py` download. Do not make students run unknown AI-generated code without source inspection and an approved isolated test environment.

## Learning objectives

1. Design actual persistence rather than telling a chat to remember.
2. Explain how SQLite differs from an integrity fingerprint and an external source-of-truth receipt.
3. Review generated source **before** execution.
4. Demonstrate expected negative outcomes with real commands, nonzero exits and preserved failures.
5. Explain why a verified program still does not inherit authorization across chats.

## Prerequisites and safety

- Python 3 and its standard-library `sqlite3`, `argparse`, and `unittest` modules.
- A restricted disposable account, VM, container or other authorized isolated environment; no unrelated filesystem access.
- A new, owner-approved empty parent location. The `init` target itself **must not exist**, even if empty.
- Wholly invented mission and task records. No real students, confidential data, API keys, browser profiles or private projects.
- Review all imports, filesystem side effects, network calls, shell calls, cleanup paths, symlink handling and entrypoints before running generated source or tests.

If safe execution is unavailable, perform a code-review worksheet only and mark execution `BLOCKED (NOT RUN)`.

## Student task: Stage 1 design

Starting from the public [current Stage 1 prompt](../../prompts/stages/01_OFFLINE_CORE.md), design a program with:

- `init`: creates the previously nonexistent project directory, restrictive owner-only files and `MISSION.md` plus SQLite `ai_os.db` with consistent mission content.
- `status`: uses a read-only database connection and refuses missing or mismatched mission state.
- `doctor`: checks real SQLite integrity, schema, mission agreement and failure conditions without altering data.
- Tests: `unittest` discovery that includes positive **and** negative cases and does not treat zero tests as success.

Do **not** advance to Stage 2 claims, leases or event-hash journals unless Stage 1 is genuinely qualified first. The [SHA-256 memory guide](../SHA256_MEMORY_INTEGRITY_AND_RECOVERY.md) describes **requirements**, not proof of an implemented journal.

## Conditional command sequence

The commands below are examples **only after** the student has reviewed the generated program and explicitly selected an approved empty target. They have **NOT** been run by this educational page.

```sh
python3 --version
python3 ai_os.py --root ./fictional-library-r01 init
python3 ai_os.py --root ./fictional-library-r01 status
python3 ai_os.py --root ./fictional-library-r01 doctor
python3 -m unittest discover -s tests -v
```

These command names are specified in the public guide; they do not imply the files exist. On Windows, use the appropriate Python launcher and explicitly validate Windows ACLs instead of treating POSIX permission bits as meaningful.

## Required observed outcomes

| Test | Expected result | Actual status until performed |
| --- | --- | --- |
| New-root initialization | Real mission file and database contain the same versioned mission | NOT RUN |
| Repeat init on existing root | Refused without overwrite | NOT RUN |
| `status` with missing/modified mission file | Nonzero failure, no new files | NOT RUN |
| `doctor` with unsupported schema | Nonzero failure, no silent migration | NOT RUN |
| Read-only `status` and `doctor` | No database, journal or file changes | NOT RUN |
| Permissions after init | Owner-only directory/mission/database or platform ACL equivalent | NOT RUN |
| Clean-process persistence | Mission survives a separate Python process | NOT RUN |
| Zero-test or omitted-test control | Must **not** be recorded as full PASS | NOT RUN |
| Unexpected symlink/path | Refused; no out-of-root access | NOT RUN |

## Instructor check

Collect only sanitized test IDs, exact source revision, command name, observed exit status, positive/negative outputs and any first failure. The instructor should compare observations with the [Stage 1-2 negative checklist](../STAGE_1_2_NEGATIVE_TEST_CHECKLIST.md) and [error recovery rules](../ERRORS_AND_SAFE_RECOVERY.md).

Do not mistake `exit 0` from a zero-test runner, a successful Python syntax check or a locally supervised repair for a qualifying independent build. If an `init` attempt is interrupted, inspect the possible partial target **read-only**; never blindly delete or retry it. A genuine failed case can be a useful learning result.

**Release boundary:** This classroom activity does not authorize publishing a downloadable executable or submitting real records. Read [verification status](../VERIFICATION_STATUS.md) and [release policy](../PRIVACY_IP_AND_RELEASE_GATE.md).
