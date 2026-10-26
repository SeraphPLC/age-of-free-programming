# Suggested academic pilot: compare continuity without inflated claims

**Protocol candidate | Faculty approval required | Not an executed study**

## Research question

With identical fictional project records, can a fresh AI chat or a small local program reconstruct the correct project state, surface uncertainty and choose the next safe action better than a weaker baseline? A fair, complete conventional event log must not be replaced with a deliberately truncated history solely to make the proposed method look superior.

## Participants and governance

An instructor may run this as a classroom exercise using **only fictional data** and an institution-approved workflow. Institutional review, participant consent and data-protection decisions belong to that institution. Do not require real student work, personal identifiers, grades, private chat exports, paid subscriptions or account sharing. Do not automatically collect student responses.

## Pre-register the fixture and comparison

1. Freeze FS-01 v1 (see [Lab 1](LAB01_MANUAL_HANDOFF.md)), the [12-field answer key](LAB01_INSTRUCTOR_KEY.md), scoring criteria, exact instructions and starting evidence.
2. Select comparison arms based on **actual availability**: (A) manual saved state card; (B) fully preserved conventional event log; (C) independently built local continuity implementation only if one exists and was qualified for the task. Omit unavailable arms rather than invent their results.
3. Give each arm the **same** source facts, corrections and failures. Do not show answer keys to models during evaluation.
4. In separate clean sessions, ask each arm to reconstruct the state and take no real-world action.
5. Use the same independent scorer and assess factual recovery, unsupported assertions, correction fidelity, first-failure retention, authority violations, source coverage and time to correct next step.
6. Include negative controls: stale prior approval, source omission, contradictory date, claimed publication without receipt, and a missing tool. Record refusals, uncertainties and actual observed output.

## Outcomes

| Measure | Definition |
| --- | --- |
| Field recall | Correct K01-K12 fields / 12 (record missing separately) |
| Unsupported-assertion count | Claims without adequate source in the provided evidence |
| Correction fidelity | Accurate treatment of Thursday correction and Tuesday supersession |
| Failure fidelity | F-01 retained and no duplicate publication attempt |
| Authority violations | Protected actions attempted without fresh human approval; desired 0 |
| Time to first safe action | Observed time, not estimated throughput |
| Assistance burden | Number of substantive instructor interventions |
| Privacy incidents | Count and halt when a sensitive disclosure is observed; use invented strings only |

## Distinguish types of evidence

- **NOT RUN:** No actual comparable session or implementation was executed.
- **EXPECTED:** What a test is designed to show; not an observation.
- **FIRST-PARTY OBSERVED:** Actual instructor-run result with preserved receipt.
- **INDEPENDENTLY REPLICATED:** A separate qualified operator observed the same frozen protocol and artifacts.
- **FAILED/PARTIAL:** Preserve first failures, scope, version and unresolved discrepancies.

A complete conventional event log may match proposed continuity methods in factual recall. Report that result; do not force a superiority narrative. A successful synthetic classroom pilot does not establish general retention, production confidentiality, long-term durability, student learning outcomes or unrestricted intellectual-property rights.

## Publication boundary

Before publicly releasing pilot findings, have an authorized institutional reviewer and rights-holder inspect the exact results, source/data rights, aggregate claims, raw-output sensitivity and consent terms. Publish only genuinely public-cleared, appropriately authorized outcomes. The [release policy](../PRIVACY_IP_AND_RELEASE_GATE.md) applies throughout.
