# Research without manufacturing discoveries

**Original public, educational research discipline. NOT a claim of novel science, AGI, autonomous research certification or validated multi-model evaluation.** A model may propose a hypothesis; a real source and real experiment determine what survives.

Earlier public Seraph papers, including [Chromatic Lensing Inference](https://docs.google.com/document/d/1MUufrzOFrc4Hp2KRGrXrwsdUDLkajXx6XBSbRO78Mbw/edit) and the [PLC × Seraph Horsepower paper](https://docs.google.com/document/d/1rLElYJjZKSlXMzykkLampptXc4l2I9FVd_z5SC-PgpE/edit), make a useful distinction between *surprising synthesis* and *tested discovery*. The [SAGE public research](https://docs.google.com/document/d/1O6dWvoRLZFt939kxW1_SgkoDMkuIb3TiMUSHEmqYkNU/edit) illustrates committing evaluation rules before seeing favorable results. This guide is a new community method, not a replica of their specific research programs.

## Eight phases of an evidence-bounded project

| Phase | What to do | Evidence to keep | Stop condition |
| --- | --- | --- | --- |
| 1. Observation | State exactly what was seen, by whom, when and through which source | Original data or attribution | Observation source missing |
| 2. Question | Narrow the question to one falsifiable claim | Question and scope | It cannot be contradicted by any possible result |
| 3. Hypothesis | Generate candidate mechanisms, including null and competing explanations | Explicit assumptions and alternatives | Hypothesis is mislabeled established fact |
| 4. Prior art | Search relevant original literature, standards and earlier techniques | Bibliography, dates, actual retrieval records | Alleged novelty depends on unsearched prior work |
| 5. Prediction | Specify a measurable result and a control where hypotheses disagree | Fixed rule, outcomes, failure thresholds | Predictions rewritten after seeing test data |
| 6. Execution | Obtain approved real observation or run tests on fictional/safe inputs | Commands, environment, outputs or real research records | No authorized tool, inappropriate risk or no ground truth |
| 7. Independent criticism | Obtain actual identified critiques and evaluate alternatives | Verbatim critiques, reviewer identities, independence and source versions | Unqualified/unknown reviewers are counted as independent |
| 8. Qualification | State supported, refuted, inconclusive and still unknown claims | Exact version-scoped decision and unresolved issues | Serious BLOCKER/HIGH findings unresolved or rights not cleared |

Research should be able to fail safely. A good project sometimes ends with `NOT SUPPORTED`.

## Teach the method with an entirely fictional software question

**Observation:** A pretend museum catalog takes longer to load after adding a second search filter. We want to know whether **string normalization** causes the slowdown.

**Candidate explanations:**
- H1: repeated normalization inside the search loop raises work per record.
- H2: the catalog was simply doubled in size.
- H0: there is no reproducible slowdown; the first observation was noisy.
- H3: unrelated file access or different test hardware caused the difference.

**Discriminating design:** Generate fixed fictional entries; compare baseline and changed code on **the same** dataset, environment and measurement procedure, varying one factor at a time. Reserve held-out test cases. If timings are noisy, repeat or conclude inconclusive rather than selectively reporting the fastest run.

**Prior-art check:** Compare to established software profiling and normalization guidance before claiming a new algorithm. Do not send private profiling logs, proprietary code or real users' data to an unapproved model.

**Expected publication:** A small claim table: observation, competing explanations, real measurements if run, constraints, negative outcomes, and next experiment. Never write "optimized by X%" without the underlying before/after measurements and conditions.

## Four evidence labels

- `SUPPORTED_IN_THIS_TEST`: exact observation and controls support a limited claim.
- `REFUTED_IN_THIS_TEST`: controlled evidence contradicts the claim for that scope.
- `INCONCLUSIVE`: insufficient or conflicting evidence, invalid test, or uncontrolled confounder.
- `NOT_RUN`: plans or model suggestions with no actual experiment.

`NOVELTY_UNKNOWN` is separate from all four: even a correctly functioning technique may be prior art. Likewise, a researcher's theory may be scientifically meaningful without qualifying a software release.

## A real multi-model review receipt is more than agreement

A qualified independent reviewer must receive the same frozen, minimized source packet and return an **actual** response. Log date, exact packet version/digest, channel, known model/provider, known uncertainty, genuine separation from other reviewer outputs, and verbatim criticism. A response read aloud by the coordinating model does not become independently returned evidence.

If an exact release demands five distinct qualified frontier model/providers, then **five independent source-bound receipts** are needed; five role names, a list of possible model brands, mock outputs, the older Core PR #951 or an older research council are **zero transferable approvals**. High-severity findings need documented fixes and exact-version re-review before any publication recommendation.

## Adversarial questions

1. Is the conclusion simply repeating the original instruction as if it were a test?
2. Could the observed result occur under a simpler or null explanation?
3. What earlier work solves the same problem? Is the bibliography current?
4. What evidence would make us abandon the hypothesis?
5. Have source revisions or environment changes invalidated an earlier result?
6. Does the sample contain invented measurements or unsourced citations?
7. Is reviewer diversity actual and documented, or a prompt pretending to have a council?
8. Were costs, data destinations and human authority admitted before any tool call?
9. Are negative, null and dropped cases retained in the report?

## A tiny student research card

```text
QUESTION: [one falsifiable, bounded question]
SOURCE_REVISION: [actual source id or UNKNOWN]
OBSERVATION: [direct measurement / attributed report / UNVERIFIED]
HYPOTHESES: [H0, H1, H2 ...]
PRIOR_ART: [actual sources reviewed and dates, or NOT_SEARCHED]
CONTROL: [what could show our favored idea is wrong]
TEST_PLAN: [specific inputs, outcome rule, permitted tools]
ACTUAL_TEST: NOT_RUN by default
REVIEW: [verbatim actual source or NO_REVIEW]
FINDINGS: INCONCLUSIVE until evidence supports a claim
NOVELTY: UNKNOWN until meaningful prior-art review
NEXT_SAFE_ACTION: [one bounded step with human approval if needed]
```

This is complementary to [memory fidelity](MEMORY_FIDELITY_V1.md), [model routing](learning-routes/README.md) and [the historical research bibliography](history/PUBLIC_RESEARCH_INDEX.md); it is not a new executable workflow or a guarantee of frontier research performance.
