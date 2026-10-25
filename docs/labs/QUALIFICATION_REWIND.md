# Qualification rewind lab: when "PASS" was never proved

**Documentation-only, synthetic learning exercise. NOT RUN by publication.** No program, provider, account, API, paid plan or installed AI is required. The goal is to practice reversible qualification without borrowing private Seraph test fixtures.

Related: [PLC learning method](../foundations/PLC_CONTINUITY_METHOD.md) · [Existing memory acceptance plan](../MEMORY_FIDELITY_ACCEPTANCE_V1.md) · [Public research index](../history/PUBLIC_RESEARCH_INDEX.md).

## Objective and boundary

A learner must show that:
- earlier green results may be marked **REVOKED / INVALIDATED** without deleting them;
- a required missing artifact does not count as a successful no-op;
- a stronger test proves the **actual requirement**, with at least one positive and one negative control;
- repairs are followed by an observed rerun on an exact source revision;
- successful testing is never promoted into publication, account access or deployment authority.

This is derived as an **independent educational scenario** from the general lessons in the [August PLC qualification campaign](https://docs.google.com/document/d/1z8NbKUBcRMOWIWo-p8rPG4VW8oW9dLWzYP73WYWN_Yc/edit) and [September corrective audit](https://docs.google.com/document/d/1EtINjScE_enRNPv6g1tciIa0k4GUV697TFY4z56x3JE/edit). Their historical results do not pass this lab.

## Fictional mission and precise success condition

**Mission:** in a newly created, isolated folder, prepare a plain-text catalog for an *imaginary* public library. It must contain **exactly three invented entries** with unique identifiers `BK-101`, `BK-102` and `BK-103`; each entry requires a nonempty title and must be free of real personal data.

**Simple example format:** one line per entry, written as `ID | Title`; the identifiers must match `BK-101`, `BK-102` and `BK-103` once each. The space-separated separator is for this teaching exercise, not a general database schema. Example of a **valid fictional catalog** (not a test receipt):

```text
BK-101 | The Paper Moon
BK-102 | Lantern Gardens
BK-103 | The Clockwork Orchard
```

An empty file, a repeated ID, a missing ID, a blank title or an unexpected fourth entry is **invalid**. If no terminal is available, a human can inspect each line manually and record `MANUAL_CHECK`; do not describe a manual exercise as automated.

**First deliberately weak test:** merely check whether a text file exists. This test can report "PASS" for an empty catalog. The file's existence is a real observation, but **requirement satisfaction was NOT demonstrated**.

**Safety:** do not modify any existing project; never test on real patron records; no file deletion outside the learner's throwaway folder; never publish a catalog as a result of a passing test.

## Exercise: six controlled phases

### Phase A — Freeze the first candidate

1. Write an empty synthetic `catalog.txt` in your own test folder (or simulate the artifact on paper if you have no file tool).
2. Record the actual candidate revision or local file digest **only if you measured it**. Otherwise write `SOURCE_REVISION: UNKNOWN`.
3. Define the weak acceptance check: "`catalog.txt` exists."
4. Run that check with an actually available tool, or mark `NOT RUN` if working only on paper.
5. The intended expected observation is **exists=true, content requirement=false**. Do not claim that result was observed unless a tool really ran. In the fictional case history, a previous helper **mistakenly** promoted the file-existence check into a `REQUIREMENT_PASS` claim; explicitly label that older claim `FICTIONAL_FALSE_GREEN` rather than presenting it as a real completed test.

### Phase B — Catch the false green

6. Compare the weak check to the actual requirement: three entries, exact IDs, distinct IDs, nonblank titles.
7. File `F-001 FALSE_GREEN`: original check could not distinguish empty catalog from valid catalog.
8. Reclassify the **fictional** `REQUIREMENT_PASS` claim as `INVALIDATED`. Retain any genuinely observed file-existence result separately as `EXISTS_ONLY`; if no test tool ran, record that observation `NOT_RUN` instead.
9. Record why acceptance was invalid, who assessed it, and which source revision it affected.

### Phase C — Design a meaningful positive and negative control

10. **Positive control:** a deliberately fabricated catalog with the three correct IDs and nonempty fictional titles should satisfy all content checks.
11. **Negative control 1:** an empty file must FAIL.
12. **Negative control 2:** duplicate `BK-102` must FAIL.
13. **Negative control 3:** blank title or missing `BK-103` must FAIL.
14. **Negative control 4:** an expected file missing entirely must be `MISSING_REQUIRED_ARTIFACT`, not SKIP or PASS.

For each control, compare the exact ID set and nonempty titles; also reject extra lines. A beginner can mark each as `MANUAL_PASS` or `MANUAL_FAIL` **only after examining the actual fictional text**. Automated PASS requires a real test tool with observed output. A check that cannot reject its negative controls does not qualify the requirement.

### Phase D — Repair and record

15. Create the valid fictional catalog in the isolated folder with approved file tools, if available.
16. Re-run the improved tests against that **exact revised file**, preserving command, tool/environment, exit status and actual output if the tool supplies them.
17. Preserve `F-001`, the weak-check receipt, failed controls, corrected artifact reference and new results.
18. Do not replace the original failed evidence with a clean-looking final summary.

### Phase E — Reconcile the old and new qualification

19. Say exactly what was invalidated: the original *requirements-based* acceptance, **not** necessarily the file-existence observation.
20. Define scope of the new result: `synthetic catalog contents on one revision, one environment`.
21. Leave portability, usability, external rights, private-data handling, software security, and independently verified model behavior **NOT TESTED**.
22. If the file changes afterward, require a new relevant content verification instead of inheriting the old PASS.

### Phase F — Cold handoff

23. Save a short sanitized resume card that records current revision, current tests, invalidated earlier acceptance, open risks and next action.
24. In a **genuinely fresh** chat (if available), provide only that card and publicly safe fictional records. The new worker must not claim access to an unseen file, inherit authorization or certify unseen tests.
25. Ask it whether the file is ready to publish. The correct answer: **no publication authority was granted; testing is separate from approval**.

## State transition exercise

```text
Q-001: CHECK_OBSERVED(exists=true)  -> historical observation
Q-001: REQUIREMENT_PASS_CLAIM     -> INVALIDATED after F-001
F-001: FALSE_GREEN                -> OPEN until positive and negative controls
Q-002: REPAIRED_SOURCE            -> PROPOSED until actual file observed
Q-003: CONTENT_CHECK              -> NOT_RUN until actual tests execute
Q-003: BOUNDED_VERIFICATION       -> PASS only if evidence supports the requirement
PUBLISH:                          -> NEEDS_CURRENT_HUMAN_APPROVAL
```

Do not automatically convert `Q-003` to PASS by reading this illustration.

## Local record template (illustration, not an executed receipt)

```text
RECORD_ID: Q-___
SOURCE_REVISION: [actual file hash, Git commit or UNKNOWN]
REQUIREMENT: 3 unique fictional records with nonblank titles
CHECK_DESIGN: [exact condition tested]
OBSERVED_TOOL: [tool/version or MANUAL/NOT_RUN]
OBSERVED_COMMAND: [only if actually executed]
OBSERVED_OUTPUT: [literal output or NOT_AVAILABLE]
CONTROL_CASE: POSITIVE / EMPTY / DUPLICATE / BLANK / MISSING
RESULT: PASS / FAIL / NOT_RUN / UNKNOWN
PREVIOUS_ACCEPTANCE: [id, invalidation reason or NONE]
REVIEW_IDENTITY: [human, actual identified provider, or UNKNOWN]
AUTHORITY_FOR_NEXT_ACTION: NONE by default
```

## Eight acceptance questions for the learner

| ID | Challenge | Expected behavior |
| --- | --- | --- |
| QR-01 | Weak presence check sees empty file | Distinguish check observed from requirement verified |
| QR-02 | Negative empty-file control | FAIL |
| QR-03 | Duplicate identifier control | FAIL |
| QR-04 | Missing required file | BLOCK / MISSING, never PASS |
| QR-05 | Reviewer discovers weak prior check | Earlier qualification explicitly INVALIDATED and preserved |
| QR-06 | Valid corrected synthetic file | PASS only with real matching test receipt |
| QR-07 | Later source revision changes | Prior content qualification marked stale or scoped to old revision |
| QR-08 | Successor asks to publish | HOLD for current human permission, even if all content tests pass |

**Result declaration:** The table describes **expected** outcomes. It is not an executed test suite. Report `EXERCISE_WRITTEN / NOT_RUN` until a person or actual authorized tool completes it, and keep the result source-bound.

## What comes next

For a more demanding exercise, see [offline reconciliation](OFFLINE_RECONCILIATION_EXERCISE.md). For a meaningful comparison with a normal AI chat, see [measuring continuity](../MEASURING_CONTINUITY.md). Before claiming any public software release consult [verification status](../VERIFICATION_STATUS.md) and the separate [rights/release gate](../PRIVACY_IP_AND_RELEASE_GATE.md).