# Faculty brief: source-backed AI project continuity

**The Age of Free Programming | Proposed classroom evaluation | 2026-10-26**

## The teaching problem

Students can ask a chat model to generate code or plans, yet lose track of the real project state when a chat ends. A fluent summary may confuse a reported task with a completed task, overlook a failed test or carry forward an expired approval. This project makes those distinctions teachable and falsifiable.

## What is available

- **Chat-only exercise:** A student creates a fictional project record, saves a minimal handoff, opens a different chat, and checks which facts and constraints are recovered.
- **Local-first software-design path:** Public Python 3/SQLite requirements for an offline CLI with mission persistence, `init`, `status`, `doctor` and negative tests; later stages cover task/evidence ledgers, recovery and source-backed memory.
- **Public architecture reading:** An 11-chapter, 115-topic conceptual library and a routing atlas for how workers, tools, memory, privacy and human approval fit together.

The content is educational instructions and specifications, **not** an independently certified or downloadable AI OS. The baseline Stage 0 does not require programming, a publisher account or paid API usage. Optional model access, hardware, support or provider tiers may cost money.

## Suggested 20-minute introduction

1. **4 min:** Discuss the difference among a chat claim, a saved source, a real tool receipt and authority.
2. **5 min:** Give students the fictional scenario in [Lab 1](LAB01_MANUAL_HANDOFF.md) and ask for a sanitized state card.
3. **5 min:** Start a fresh chat with only that card and the successor prompt. No historic conversation or old permissions are supplied.
4. **4 min:** Compare the successor to the [instructor key](LAB01_INSTRUCTOR_KEY.md): errors, missing fields, false certainty and unauthorized next steps.
5. **2 min:** Discuss limitations, including confidentiality, independent verification and retention.

## Evidence rather than endorsements

Published first-party tests have identified both functioning supervised prototypes and real failures. Fresh-chat independent reproduction of a complete public executable remains unqualified; actual privacy challenges caused synthetic protected values to be echoed by local models. These outcomes are deliberately preserved. Read the [claims matrix](CLAIMS_AND_LIMITS.md) and [verification ledger](../VERIFICATION_STATUS.md) rather than extrapolating from test totals.

## Educational fit

Relevant topics include software verification, database persistence, systems engineering, computer security, human-computer interaction, research methods and AI literacy. No college has been verified to endorse, adopt or certify this material. An instructor may critique it without installing software or providing real student data.

## Boundaries and rights

Use only fictional or properly cleared materials. No installed automatic confidentiality filter is supplied. Local terminal tools should run only in an isolated, authorized learning environment. The repository is free educational guidance, **not yet licensed as a repository-wide open-source package**; any reuse beyond the published invitation needs a separate rights check. See [sharing status](../SHARING_AND_LICENSE_STATUS.md) and [output disclosure rules](../OUTPUT_DISCLOSURE_GATE.md).

**Invitation:** Evaluate the lesson for pedagogical usefulness and falsifiability. Feedback can be written in the [offline worksheet](FACULTY_FEEDBACK.md); there is no automatic upload or requirement to identify students.
