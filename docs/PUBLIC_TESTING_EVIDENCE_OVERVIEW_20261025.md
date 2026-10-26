# What has actually been tested? — Public evidence overview

**The Age of Free Programming · Public-safe research summary · 2026-10-25**

> **Scope:** This is a summary of *bounded, first-party* educational tests and their limits. It is **not** a complete benchmark database, a new executable release, a comparative AI ranking, or independent security certification.

## How to read a result

- **Tested:** Code or model output was actually exercised under a specified fixture, version and environment.
- **Designed / NOT RUN:** A benchmark, test plan or implementation idea exists, but the particular result has not been measured.
- **FAIL:** The observed behavior did not meet a stated condition. Retain the failure, even after a later correction.
- **Supervised:** An engineer or reviewer modified/generated the code; it was not independently built solely from the public prompt.
- **Independent:** Requires a separately executed, traceable reproduction, not the same AI role-playing as multiple reviewers.
- **Public release:** Needs a separately reviewed license, privacy, security and deployment decision. A passing unit test is not that decision.

Test counts from different revisions, languages, machines or suites **must not be added together** as unique cases.

## Publicly documented test outcomes

| Workstream | Recorded result | What it does **not** prove | Public evidence |
| --- | --- | --- | --- |
| Guided local reference | 31/31 first-party tests on two Macs; coverage incomplete on two of 21 requirements | Clean-room construction solely from the public prompt, security certification, or cross-platform support | [Reference review](LOCAL_REFERENCE_R1_HARDENING_20261024.md) |
| Direct AI-generated Stage 1/2 | Stage 1 8/8 **after a repair**; a later direct Stage 2 trial failed 5 of 13 checks | That an AI can reliably generate complete working software from the instructions | [Preserved model trial](STAGE2_PUBLIC_PROMPT_TRIAL_20261024.md) |
| Separate supervised Stage 2 code | 57/57 first-party synthetic checks on two Macs | Independent model-built implementation or released executable | [Trial and limitations](STAGE2_PUBLIC_PROMPT_TRIAL_20261024.md) |
| Supervised hardening | R3 63/63 and R4 78/78 first-party synthetic checks in their respective versions | That all versions are interchangeable, audited or portable | [R3](LOCAL_STAGE2_R3_SECURITY_REVIEW_20261024.md), [R4](LOCAL_R4_MISSION_EVIDENCE_REVIEW_20261024.md) |
| R5 direct build reproducibility | A model repair passed 14/14 listed checks but missed a supplemental requirement; clean public-prompt-only generation timed out; full R5 Stage 2 NOT RUN | Independent end-to-end reproducibility | [R5 negative gate](LOCAL_R5_STAGE1_REPRODUCIBILITY_REVIEW_20261024.md) |
| Output-disclosure fixture | 18/18 defined first-party checks PASS, yet an additional context-sensitive case went **false-green** | That any prompt or detector safely filters all confidential material | [Synthetic disclosure trial](OUTPUT_DISCLOSURE_SYNTHETIC_TRIAL_20261024.md) |
| Actual local-model confidentiality probe | **FAIL:** 19 exact echoes of invented protected markers in 24 privacy challenges | A trustworthy privacy-enforcement service; no real secret was involved | [Black-box trial](LLM_DISCLOSURE_BLACKBOX_TRIAL_20261024.md) |

The public guide remains educational. It does **not** provide a full independently qualified AI OS, make a new AI chat inherit permissions, or establish the security of any user's future implementation.

## Long-term memory: simulated years, not demonstrated years

A separate **offline, fictional continuity experiment** explored memory reconstruction over timestamps spanning 25 years. It is summarized in the [time-compressed tabletop report](LONGEVITY_TABLETOP_R0_PUBLIC_SUMMARY_20261025.md).

The exercise reported 12,000/12,000 expected current facts recovered from 13,500 generated events, with an ordinary complete event-log comparison producing the same result. This illustrates the value of retaining full evidence and correction history, **not** a superiority claim, years of actual operation, or a test of a system built from the public prompt.

The linked report offers conclusions and limitations without publishing its experimental software or raw lab materials.

## What remains unqualified

- An end-to-end fresh-chat build of the current public v0.5 instructions, independently reproduced by an outside beginner.
- Real years of operation, model/provider succession, major future format migrations, and physical storage aging.
- A qualifying standardized memory benchmark against fair baselines, independently executed holdouts and uncertainty estimates.
- Independent security review, model-independent output controls, genuine rights review and published executable licensing.
- Windows and Linux acceptance of a public downloadable implementation.
- Use of real personal/private records, autonomous computer access or unattended data collection.

**Safe next step:** use fictional tasks, verify exact source versions, preserve failed outputs, run the staged [negative-test checklist](STAGE_1_2_NEGATIVE_TEST_CHECKLIST.md), and clearly distinguish BUILD / PASS / FAIL / NOT RUN. The [verification ledger](VERIFICATION_STATUS.md) remains the controlling public status, and the [privacy/release gate](PRIVACY_IP_AND_RELEASE_GATE.md) applies to every publication.

**The mission outlives the model. Passed requires proof.**
