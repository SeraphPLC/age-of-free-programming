# Repository-wide public education audit — 2026-11-25

**Status:** Reviewable maintenance candidate. **Not** executable AI OS release approval, independent security certification, software license, or five-provider frontier review.

## Exact public source and coverage

- Repository: `SeraphPLC/age-of-free-programming` (public), default branch `main`.
- Baseline commit: `56f74ebeb9748b27e927a4391762a8169987ece3`; baseline tree: `49637f8e013f5d369414ce8715de9884990caea2`.
- GitHub tree API reported `truncated=false`: **101 tracked files** (82 Markdown, 4 JSON, 14 PNG/SVG assets and 1 `.gitignore`).
- A separate shallow clone on an authorized Mac Studio corroborated the exact baseline commit and tracked-file count.
- Structural inspection covered all 82 Markdown files and four JSON files; local static checker examined **493 relative Markdown/HTML references** and four JSON files with **zero reported failures**. This is an *observed static check*, not an external link crawl, semantic link check for every complex GitHub anchor, schema conformance proof, security audit, or runnable AI OS test.
- Read manually: README, START_HERE, SIMPLEST_VALID_PATH, Stage 0, verification ledger, license status, Desktop Commander setup and representative public architecture/routing and safety sections. Remaining long-form files received structural coverage, not paragraph-by-paragraph independent expert review.
- All conclusions pertain to the baseline above. Re-run against a new head before promoting any claim.

## Findings and prioritized actions

| ID | Priority | Observed evidence | Corrective action / status |
| --- | --- | --- | --- |
| A01 | HIGH — user workflow correctness | Stage 0 currently instructs readers to paste the same startup prompt and a saved state card; a successor can restart an invented exercise rather than reliably recover the previous state. | Reuse and reconcile existing drafts [#26](https://github.com/SeraphPLC/age-of-free-programming/pull/26), [#12](https://github.com/SeraphPLC/age-of-free-programming/pull/12), and [#33](https://github.com/SeraphPLC/age-of-free-programming/pull/33). Choose one minimal tested approach. Test with distinct cold-start chat sessions and synthetic ground truth. **OPEN; no merge.** |
| A02 | HIGH — misleading instruction wording | Three archived advanced prompts and the route map contain `do not tell the user` constructions that a simplistic scanner can misclassify; the route-map wording also fails to explicitly require reporting the failed connector. | Existing [#32](https://github.com/SeraphPLC/age-of-free-programming/pull/32) rewrites the instructions affirmatively to report real failures and limitations. Review diff and preserve exact-source version attribution. **OPEN; no merge.** |
| A03 | HIGH — release-evidence provenance | Public verification ledger distinguishes supervised derivatives, model-generated failures, and unreleased binaries. First-party test counts cannot prove the current prompt independently builds a safe executable. | Retain exact source identifiers and historical fail receipts. Keep prompt, code, security, license, rights, and owner publication gates separate. Never promote an archived test to current approval. **HOLD unchanged.** |
| A04 | HIGH — confidentiality | Public verification ledger reports **19/24 exact synthetic canary echoes** from historical first-party local model tests; prompt-only privacy instructions are not a technical guard. | Keep fictional data as the entry point, prohibit real secrets in experiments, and require a separately enforced/tested disclosure boundary for any future sensitive-data product. **Unresolved for executable release.** |
| A05 | MEDIUM — rights and claims | `docs/SHARING_AND_LICENSE_STATUS.md` explicitly says there is no repository-wide license selected. The README makes an educational-use invitation, which does not imply blanket commercial reuse. | Rights-holder chooses a license separately; do not add a LICENSE automatically. Ensure public calls-to-action accurately say link-sharing/prompt use is invited, broad redistribution remains unlicensed. |
| A06 | MEDIUM — maintenance drift | Multiple open drafts cover overlapping beginner, handoff, release evidence, visual positioning and model routing topics. One GitHub listing showed 12 open PRs at the baseline review. | Review dependencies, retire superseded proposals only after owner decision, and avoid merging overlapping edits without fresh main-branch comparison. |
| A07 | MEDIUM — repeatability | The repo is educational Markdown with static JSON examples, but previously lacked an included one-command structural reference check. | Added `scripts/check_repo.py` in this branch: Python standard library only. **PASS on baseline clone: 82 Markdown files, 493 references, 4 JSON files; 0 failures.** This does not execute the AI OS. |
| A08 | MEDIUM — external change | Optional provider access, cost, model names, third-party setup guides and policies can change over time. The 2026 setup guides already state that entitlements/pricing must be verified per account. | Verify vendor terms and pricing against authoritative current pages before publishing updated claims. Do not turn historical advertised prices into guarantees. **NOT RUN in this structural pass.** |

## Open PR triage, not automatic approvals

- **Workflow collision:** #12, #26, #27, #33 all address parts of Stage 0/handoff/beginner clarity; choose a single compatible fix after comparing with current README.
- **Transparency:** #32 is the already-prepared disclosure wording improvement. Avoid independently duplicating it here.
- **Evidence and research:** #10, #20, #25, #29 and #31 add distinct educational/review content, but must remain correctly source-scoped and cannot imply external security certification.
- **Public presentation:** #37 and #38 involve branding/donations; approve exact assets and text separately from core technical/release gates.

## Ordered review plan

1. **Reproduce baseline**: pin commit/tree, complete static check, inventory open PRs and historical evidence. Status: completed as specified above.
2. **Independent review workstreams**: beginner experience, technical correctness, model/provider routing, privacy and prompt injection, rights/branding, and scientific/research claim qualification. Each must record the exact text/version reviewed, tool/model identity, verbatim observations, conflicts, and any unknowns. Local Ollama advice is *not* a five-frontier-provider quorum. Do not infer independence from different prompts or aliases.
3. **Resolve high-severity reader defects**: test a genuinely fresh-chat handoff; ensure failure messages are reported honestly; add negative controls and measure actual results against synthetic answer keys.
4. **Reconcile PR backlog**: compare every candidate against the latest `main`; do not merge incompatible stale changes. Use fresh isolated branches for corrective changes and preserve original findings.
5. **External verification**: re-check live vendor pricing/capabilities/terms, accessibility of published assets and links, copyright/brand rights, and human beginner usability. Mark any skipped review `NOT_RUN`.
6. **Release decisions remain separated**: educational prompt/text, executable starter, sensitive-data automation, and any branded product each require their own proof and owner consent.

## Strict limits

The checker does not parse AI instruction semantics or prove confidentiality. No executable starter was built, installed, audited, or released as a result of this maintenance pass. Do not count local or mediated-model opinions as five genuinely independent direct frontier-provider reviews. No new license, publication approval, external spending, connection permission or merge is authorized by this audit. Private Seraph Core records, credentials, internal infrastructure and protected code are out of scope.

## Reproduction

```sh
python3 scripts/check_repo.py
```

Run from an authorized local checkout. Report its actual exit code and output; the checker returns nonzero on detected broken local targets or invalid JSON. External URLs and semantic verification require other tools and human review.
