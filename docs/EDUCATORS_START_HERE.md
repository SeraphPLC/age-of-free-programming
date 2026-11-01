# Educators: evaluate The Age of Free Programming

**Independent educational material | Review candidate dated 2026-10-26 | No university endorsement or executable release**

The Age of Free Programming is a free-to-read collection of prompts, learning routes and local-first software-design exercises. It teaches how to preserve a project's mission, tasks, evidence, decisions, failures and next actions when an AI chat or model changes. The public repository does **not** supply a completed AI operating system, an installed Seraph agent or access to private Seraph services.

The intended entry-level activity does not require paid API calls or programming. Optional computer-based labs use Python 3 and SQLite from the standard library, but a student's computer, AI provider, accessibility requirements and optional services may involve separate costs. The publisher has not independently qualified all builds or operating systems.

## Pick one teaching route

| Format | Suggested time (not a promise) | Learning outcome | Start |
| --- | --- | --- | --- |
| Chat-only workshop | 20-30 minutes | Distinguish a saved project record from a model's unsupported recollection | [Lab 1: handoff and source fidelity](educators/LAB01_MANUAL_HANDOFF.md) |
| Optional programming lab | 60-90 minutes for a scoped introduction; longer builds may be needed | Examine file persistence, read-only checks and failures in a Python/SQLite design | [Lab 2: offline core](educators/LAB02_OFFLINE_CORE.md) |
| Faculty study or capstone design | Instructor-defined | Design falsifiable evaluation with fair baselines and traceable evidence | [Pilot protocol](educators/ACADEMIC_PILOT_PROTOCOL.md) |

## Faculty materials

- [One-page faculty overview](educators/FACULTY_BRIEF.md)
- [Lab 1 instructor key](educators/LAB01_INSTRUCTOR_KEY.md) -- keep outside the model's evaluation input
- [Assessment rubric](educators/ASSESSMENT_RUBRIC.md)
- [Claims, evidence and limitations](educators/CLAIMS_AND_LIMITS.md)
- [Faculty feedback worksheet](educators/FACULTY_FEEDBACK.md) -- save locally, no collection endpoint

## What to use today

Begin with the [current Community R1 Living prompt](../prompts/GET_SERAPHED_COMMUNITY_R1_LIVING.md), or the shorter [Stage 0 chat-only activity](../prompts/stages/00_CHAT_ONLY_CONTINUITY.md). Historical Community R0 is archived and is **not** the current recommended starter. See the [staged guide](STAGED_BUILD_PATH.md), [safe error recovery](ERRORS_AND_SAFE_RECOVERY.md), and [verification ledger](VERIFICATION_STATUS.md) before attempting software construction.

## Safety and reuse boundaries

Use invented projects only. Do not submit students' real records, credentials, private conversations, research data, repository secrets or local logs to an AI service or public issue. A model's disclosure promise is not an enforced privacy boundary; actual synthetic model-output tests found confidentiality failures. Never pass an old chat's claimed permission to a successor.

This material is free to read, and the repository expressly invites copying its identified prompts for personal learning and sharing its link. **No repository-wide open-source redistribution license is currently granted.** Obtain rights review before broad adaptation, commercial redistribution or bundling external sources. Review the [sharing and licensing status](SHARING_AND_LICENSE_STATUS.md) and [public disclosure gate](OUTPUT_DISCLOSURE_GATE.md).

**Instructor standard:** A plausible response is not a verified result. Mark actual observations, failed checks, partial outcomes and NOT RUN separately. A course exercise is not security certification or academic endorsement.
