# PR #10 — research-integration source review packet

**Status: DRAFT / REVIEW REQUEST / NOT APPROVED.** Prepared 2026-10-24 for [PR #10](https://github.com/SeraphPLC/age-of-free-programming/pull/10) in the independent public education repository. This packet is **not** an external review or a license grant.

## Target and freeze discipline

- Review **the exact immutable commit SHA** recorded in PR #10's GitHub review thread. Do not substitute a later `main`, local files, a changed Google Doc or another prompt candidate.
- This PR changes educational Markdown only: eight new guides and six documentation/navigation files, plus this review packet. No original v0.1–v0.4 master prompt, executable software, JSON schema, or private Seraph component is being approved here.
- Source bibliography: [public research index](../history/PUBLIC_RESEARCH_INDEX.md). Open each linked historical paper directly to confirm public visibility and accuracy **at your review date**. Public readability is not a copyright license.
- **Review scope differs from release scope:** admission of this documentation PR does **not** satisfy the exact-hash five-provider Advanced AI Council rule for any v0.3/v0.4 public master prompt. The executable starter is a **separate** release with code/security and platform testing gates.

## Author/editor checks already performed — limited evidence

| Check | Observed result | Limitation |
| --- | --- | --- |
| Public bibliography visibility | 14/14 linked Google Docs had Drive `anyone:reader` permissions on 2026-10-24 | Anyone-reader does not establish third-party rights, external availability in all regions or legal redistribution clearance |
| Repository relative links | 182 relative Markdown links in the 14 changed files resolved against the branch tree; 0 missing paths (author/editor check) | Not a rendered-link or browser-usability test |
| Historical verbatim reuse screen | No 12-word contiguous overlap found across eight new guides versus six major historical source bodies in an author/editor token-sequence comparison | Not a plagiarism opinion, complete corpus search, legal audit or semantic derivation test |
| Sensitive content spot scan | No obvious password/key assignment, private user-directory path, internal Seraph route token or secret markers in changed Markdown | Not a certified privacy/security review; Git history and private content beyond PR not audited |
| Synthetic catalog sanity | 7/7 expected cases matched a **first-party throwaway Python check** on Linux Python 3.13.5: one valid, six rejected variants | No public program is shipped; this is not independent user testing, a clean-machine qualification or completion of the documented full lab |
| GitHub CI | No commit status checks or workflow runs returned at this review snapshot | **No CI pass to claim** |
| Independent reviews | **0 qualified independent review receipts observed** before this packet | Author/editor review is not a council seat |

The seven synthetic content-check cases comprised: valid, empty, duplicate ID, blank title, missing required ID, extra entry, and missing file. A weak "file exists" check accepted some invalid cases, illustrating the documented false-green failure. The test code and input were temporary, **not a published public software artifact**. All exercise documents remain `NOT RUN` as integrated beginner and cross-model acceptance campaigns.

## Findings, correction and open gates

| ID | Severity/status | Finding or required evidence |
| --- | --- | --- |
| EDIT-01 | **CORRECTED in branch** | Fictional source card mistakenly referenced an unverified email instead of the actual human confirmation receipt as the controlling anchor. Changed to `E-01`; source still needs verification in real use |
| EDIT-02 | **CORRECTED in branch** | Qualification rewind lab lacked an explicit small valid example and an unambiguous distinction between a fictional false-green story and a test actually run. Added exact three-entry example, controls and manual-vs-automated labels |
| EDIT-03 | **CORRECTED in branch** | Measurement protocol needed a no-tools novice rehearsal before a full A/B/C benchmark. Added a paper-only dry run with explicit `DRY_RUN_ONLY` labeling |
| EDIT-04 | **CORRECTED in branch** | New Markdown files lacked final newline; append a single EOF newline for consistency |
| GATE-01 | **HOLD — rights and brand review** | The appropriate rights-holder/qualified rights reviewer must verify independent adaptation, attribution, permitted use of historical concepts, branding, and whether public visible research may be linked or excerpted |
| GATE-02 | **HOLD — independent content and usability** | No independent human beginner has completed the full synthetic exercise. Require a novice read-through with errors, time, confusion and data privacy notes recorded; correct any HIGH/BLOCKER findings |
| GATE-03 | **HOLD — independent quality findings** | Request qualified external content/technical review on this exact frozen head; preserve verbatim outcomes, actual reviewer identities, method and adverse findings. No fake AI Council roles |
| GATE-04 | **SEPARATE RELEASE HOLD** | Master prompt five-provider exact-hash Advanced AI Council approval, owner publication decision, and executable software audits cannot be inferred from this documentation PR |

## Exact-source reviewer response form

```text
REVIEW_TARGET: PR #10
COMMIT_SHA_REVIEWED: [exact 40-hex SHA actually read]
REVIEW_DATE: [observed date]
REVIEWER_IDENTITY_OR_PROVIDER: [verified actual identity/provider or UNKNOWN]
MODEL_ID_IF_APPLICABLE: [actual exposed version, or UNKNOWN]
METHOD: [direct file read, independent provider return, human user trial, or UNKNOWN]
INDEPENDENCE: [how separation from author/other reviewers was established, or UNKNOWN]
REVIEW_SCOPE: [which files, source references and tasks were checked]
VERBATIM_FINDINGS: [actual returned text, or private safe pointer to a sensitive receipt]
SEVERITY: BLOCKER / HIGH / MEDIUM / LOW / NONE (with justification)
RIGHTS_AND_DISCLOSURE: PASS / HOLD / UNKNOWN, with evidence
BEGINNER_USABILITY: PASS / FAIL / NOT_TESTED, with actual observed outcomes
OUTCOME: ACCEPT / CHANGES_REQUESTED / REJECT / INCONCLUSIVE
NEXT_ACTION: [specific bounded correction, no inherited authorization]
```

If the reviewer reports a sensitive credential, personal identifier or exploitable security flaw, **do not post it in a public PR**. Use the repository's [private vulnerability channel](../../SECURITY.md). A model reporting that it has reviewed a file is **not** evidence that it actually had source access.

## Reviewer tasks

1. Read the frozen GitHub diff and eight new guides in context. Distinguish fictional worked examples from observed results and optional dependencies from required ones.
2. Check that each historical claim is source-grounded and time-scoped. Specifically challenge study results, AGI terminology, productivity estimates and statements about cloud-model access.
3. Evaluate whether the learner can complete the [qualification rewind](../labs/QUALIFICATION_REWIND.md) manually without coding, and with actual offline tooling after specific permission.
4. Check the [continuity measurement protocol](../MEASURING_CONTINUITY.md) for fairness, contamination, missing denominators and time/cost accounting.
5. Verify that the [casebook](../examples/CONTINUITY_CASEBOOK.md) avoids real confidential data, illegal account access and delegation of medical/legal/financial authority.
6. Document every BLOCKER/HIGH issue, the exact revision affected, a defensible fix and whether targeted re-review is still outstanding.
7. Record separate **owner merge decision** only after this documentation branch's own rights and review gates. Do not transfer approval to the AI OS master prompt or software.

**Disposition:** `REVIEW-PACKET-PREPARED / PR-STAYS-DRAFT / OWNER-MERGE-APPROVAL-NOT-REQUESTED`. No independent content, legal or usability reviewer has been simulated or counted.
