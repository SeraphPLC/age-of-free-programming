# Public beginner/continuity PR reconciliation — November 25, 2026

**Status: reviewable consolidation map; NOT an approval to merge, close other PRs, publish a prompt, or release software.**

## Controlling references

- Public default branch observed at `56f74ebeb9748b27e927a4391762a8169987ece3`.
- Consolidated source candidate: [draft PR #40](https://github.com/SeraphPLC/age-of-free-programming/pull/40); the candidate is **mutable** until frozen and reviewed. Recheck its actual Git head before relying on this file.
- Earlier drafts reviewed: [#12](https://github.com/SeraphPLC/age-of-free-programming/pull/12) `e4f3486a92e49f2dcc9f49cd32a208929c0dc1e4`, [#26](https://github.com/SeraphPLC/age-of-free-programming/pull/26) `9fbee50b29f534d8835b17d3b7490cc45dfce616`, [#27](https://github.com/SeraphPLC/age-of-free-programming/pull/27) `a6105e3278d04b775c33a915dea69ab19ac1a4ed`, [#32](https://github.com/SeraphPLC/age-of-free-programming/pull/32) `ff0d1f75973ffeb28d57b96854ddb393fdbf0bb9`, [#33](https://github.com/SeraphPLC/age-of-free-programming/pull/33) `cbf85aaa7265d745faf18d284691c56390e43c20`.
- This reconciliation is about **changed public educational files and observed scope**, not the owners' private release ledgers or exact-source five-provider frontier votes.

## Disposition of older work

| Earlier PR | What was verified | Treatment in #40 | Outstanding |
| --- | --- | --- | --- |
| **#12 — Stage 0 first-party trials** | Source-scoped **failures** in model-produced cards and partial successes when given manually checked inputs; separate local browser profiles did not establish independent human/provider acceptance | Preserve [October 24 report](STAGE0_LOCAL_HANDOFF_TRIAL_20261024.md) **byte-for-byte** from the older draft: original Git blob `0dcb1011c702cb97959f683072c81931a178612a`; do not silently upgrade historical FAILs | Actual beginner observation, source-specific final revised prompt test and independent qualification remain missing |
| **#26 — two-chat procedure** | Contains an early first/successor split, canonical synthetic IDs, no inherited authority | Incorporate into updated [Stage 0](../../prompts/stages/00_CHAT_ONLY_CONTINUITY.md); include the later trial-informed distinctions and explicit task direction | Revalidate every changed prompt version; no old acceptance carries forward |
| **#27 — gentle handoff** | Complete `docs/GENTLE_CHAT_HANDOFF.md` on #27 and #40 has **identical Git blob** `6f6671de0f38c8882778296915079891ea860bbe` | Preserve full guide unchanged; adapt README/Start Here references to current beginner routing | Independent usability observation and actual linked-source freshness |
| **#32 — transparent AI instructions** | Four focused changes replace potentially misleading “do not tell the user” language with explicit reporting of generic starter limits and failed adapters | All four affected paths are updated in #40; do not ship a second conflicting wording variant | New prompt file bytes mean old version/test approval cannot be assumed |
| **#33 — R1 starter navigation** | Current R1 links, fresh-chat memory-isolation warning and proposed README reordering | Four R0→R1 starter-link fixes and memory-isolation guidance incorporated; the already-live beginner-first public README layout remains authoritative | Donation/branding layout is **separate owner-positioning work** and not an automatic acceptance criterion for Stage 0 |

## New exact-source findings that #40 must preserve

- The November 25 test report records **13 local first-party stateless inference calls** across three prompt revisions using two installed model tags. These exposed ambiguous completion labels, missing real-test fields, insufficient explicit approval rejection, reversed dependencies and malformed field formatting. Treat all adverse evidence as historical, not "fixed forever" by a later string change.
- The source card used in the consolidated Stage 0 candidate at commit `c5acc7bc4b5b235282531311d01f6d315e74e548` initially **failed its own stricter deterministic validator** because its story-only completion and T-02 next action were implicit. The corrected canonical card at `18a01330befc5a77a67344b18bffad933a467295` passed the validator's structural check; this is **not** observed independent AI fidelity.
- A [separate beginner acceptance kit](STAGE0_BEGINNER_ACCEPTANCE_KIT_20261125.md) now specifies how an independent novice/facilitator could test this exact version using fictional data. Its status is **NOT RUN**, not human-usability PASS.

## Pull-request management recommendations

**Do not close #12/#26/#27/#32/#33 as superseded yet.** They are original dated evidence and source proposals, not interchangeable release approvals. Before changing their state: compare live heads again, verify review comments, trace unique requirements and source hashes, obtain owner decisions, and ensure all originally recorded failures remain accessible. A shared file path indicates a possible editorial collision, not necessarily a line-level merge conflict.

Other public research, architecture, positioning, licensing and optional support drafts (including #10, #20, #25, #29, #31, #37 and #38) have distinct editorial or owner-governed decisions. They are not bundled into this beginner-continuity consolidation. [Draft audit #39](https://github.com/SeraphPLC/age-of-free-programming/pull/39) remains a separate source-pinned structural-check/report proposal.

## Release boundaries

- Chat-only prompts are educational instructions, **not** running code, continuous memory, independently audited security, actual private Seraph architecture, or permission to access machines.
- Any runnable starter requires its **separate** clean-machine OS tests, code/security audits and licensing decision.
- Community branding, current optional provider entitlements/cost, source disclosure rights, exact-source five distinct qualified frontier-review receipts, closure of BLOCKER/HIGH findings and final owner publication decision remain their **own** gates.
- **No merge, release, user notification requesting owner go/no-go, payment, connected account change, or external AI dispatch** is authorized by this document.


## 2026-11-27 cross-draft accessibility correction

The exact H1→H3 document-heading defect in the unmerged public `main` is now corrected in **both open drafts #39 and #40**, with no change to rights or licensing claims. The entire `docs/SHARING_AND_LICENSE_STATUS.md` file has the identical Git blob `127ba7be31a3af698b732d24379fc2475355edbe` in both drafts. Only its two section-heading markers differ from main (H3→H2). A same-file overlap is **intentional duplicate proposed coverage**, not proof that either proposal is already published.

At draft #40 commit `43aa4447db0a455884bad4c85ff86c5f588fd227` (before this documentation-only note), the enhanced independent draft #39 checker found **87 Markdown documents, 515 internal references, four JSON files, zero broken structural references**. The separate no-network accessibility hygiene audit found **zero** narrow Markdown findings in the #40 draft. Its outbound URL inventory found **173 URLs / 96 distinct hosts**, no insecure/private destination syntax flags, and four query-bearing support/payment URLs still requiring contextual review. `git diff --check` passed. Stage 0's unchanged SHA-256 remained `eb4e741cbe3356ad78c38d3b605a86bc992f1ba853c7fbd2ba8a202c24a8e38b`.

The Mac Studio operator tasker was updated to verify the **exact PR #39 and #40 Git head and this two-heading-only content change** against the pinned unmerged main source. It caches exact-source evidence by PR head, reports `FIX_PROPOSED_BOTH_DRAFTS_UNMERGED`, and refuses to treat that as a completed main-branch fix, new license, independent accessibility test or owner-approved release. A changed/unknown head cannot inherit approval from a cached older version.

Neither draft has been merged or released. The separate educational prompt's five-provider independent review, owner rights, beginner usability, optional service cost, BLOCKER/HIGH closure, and executable starter audits remain unverified and cannot be satisfied by these documentation checks.
