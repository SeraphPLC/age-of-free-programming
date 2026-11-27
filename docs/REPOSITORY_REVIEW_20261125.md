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

## Bounded Mac Studio local-model advisory receipts

Two installed Ollama models were **actually invoked against the same five excerpted public files**, not against the complete 101-file repository: `README.md`, `docs/VERIFICATION_STATUS.md`, `docs/START_HERE.md`, `docs/SHARING_AND_LICENSE_STATUS.md`, and `prompts/stages/00_CHAT_ONLY_CONTINUITY.md`. The local private receipt file is `/tmp/seraph-public-audit-20261125/local_review_receipts.json` on the authorized Studio (a temporary audit folder, not a durable canonical evidence store).

- `gpt-oss:20b`: completed at the model endpoint after 134.5 seconds but returned an **empty response**. Reviewer finding count: zero; qualification: **UNUSABLE RESPONSE**. Do not count it as independent agreement or a successful review.
- `qwen2.5-coder:7b`: returned a bounded advisory response after 51.5 seconds. It suggested more explicit warnings about security qualification and executable status in README/START_HERE/VERIFICATION_STATUS; **direct source comparison shows these caveats are already explicitly present** (for example README's “What is real today?” warning and the verification ledger's NOT VERIFIED entries). Its suggestions are therefore **ALREADY COVERED**, not confirmed new defects, and should not justify duplicative additions without stronger evidence. Its last item was cut off at the token limit and is **INCOMPLETE**.

**Independence and qualification:** Both attempts used different local model names through the same installed Ollama service and the same coordinating session; these are **not provider-independent frontier reviews**, no external cloud service was invoked, and they do **not** satisfy the five-provider Advanced AI Council quorum. Neither model performed security tests, fresh-chat reproduction or rights clearance. The source quotes and recommendations are advisory, not dispositive.


## Source-pinned open-PR overlap review (2026-11-25)

After the initial audit, the private Mac Studio maintenance checker queried **all 14 open GitHub pull requests** using the actual `headRefOid` and changed-file manifests returned by the public GitHub API. The comparison recorded **37 PR pairs with at least one shared changed file**. The total is a file-level overlap count, **not 37 confirmed Git merge conflicts**, 37 defects, or 37 required manual merges. Actual patch semantics and branch freshness still need review.

| PR pair | Shared changed files | Review implication |
| --- | ---: | --- |
| [#33](https://github.com/SeraphPLC/age-of-free-programming/pull/33) and [#40](https://github.com/SeraphPLC/age-of-free-programming/pull/40) | 7 | Beginner routes, README, changelog, and Community R1 overlap; compare source texts before deciding which is authoritative |
| [#32](https://github.com/SeraphPLC/age-of-free-programming/pull/32) and #40 | 4 | Affirmative transparency edits intentionally overlap; avoid two competing versions of the same wording |
| [#10](https://github.com/SeraphPLC/age-of-free-programming/pull/10) and #40 | 4 | Documentation/navigation overlap; separately review research content |
| [#37](https://github.com/SeraphPLC/age-of-free-programming/pull/37) and #40 | 4 | README and public positioning overlap; preserve owner branding/rights decisions |
| [#10](https://github.com/SeraphPLC/age-of-free-programming/pull/10) and [#20](https://github.com/SeraphPLC/age-of-free-programming/pull/20) | 3 | Changelog/README/builder guidance overlap; evidence restrictions must not be weakened |
| [#26](https://github.com/SeraphPLC/age-of-free-programming/pull/26) and #40 | 1 | Stage 0 successor prompt overlap; preserve earlier failed synthetic trials |

**Controlling observed refs for this comparison:** main `56f74ebeb9748b27e927a4391762a8169987ece3`, #40 `f3156a36c51260d202d4038ea09ee92f950c935f`, #32 `ff0d1f75973ffeb28d57b96854ddb393fdbf0bb9`, #26 `9fbee50b29f534d8835b17d3b7490cc45dfce616`. The result becomes stale as soon as any relevant PR head changes.

**Next safe action:** Keep #39 and #40 as separate draft, unmerged review candidates. Reconcile #12/#26/#27/#32/#33 before attempting an owner-reviewed merge. Repeat exact-source Stage 0 synthetic negative controls and independently qualified beginner testing, and separate optional support/branding changes from evidence and privacy work. No older PR approval or synthetic-model success counts as current release clearance.


## Checker blind-spot regression coverage — 2026-11-25

Source-pinned checker review uncovered two independent structural-audit blind spots: links shown as literal Markdown in fenced code examples were incorrectly treated as live targets, and links pointing to headings in the **same document** were entirely skipped rather than checked. Neither finding by itself establishes a problem in the published content; they are weaknesses in the validator.

The revised checker in `scripts/check_repo.py` and its standard-library-only synthetic regression suite `scripts/test_check_repo.py` are at exact draft PR #39 commit `a441fd4c8f6d6c546b9c4ae78c51a35fb74bd840`. **7/7 synthetic tests passed**, exercising code-fence exclusion, simple same-page and cross-file heading anchors, duplicated headings, percent-encoded relative names, missing/escaping paths, and malformed JSON. `git diff --check` passed in the source-pinned isolated checkout.

The enhanced offline checker returned **PASS: 83 Markdown documents, 493 local references and four JSON files**, with zero findings against the current public-main baseline in that checkout. It also returned zero findings when pointed at the separate draft PR #40 checkout (87 Markdown documents, 514 relative references, four JSON files). The static checker cannot validate external URL availability, accessibility, security, provider entitlements, AI instruction efficacy, compiled software, or independent release requirements. Both PRs remain **draft and unmerged**.

For independent reproducibility on a Python 3.9+ environment after checking out this exact PR #39 branch:

```sh
python3 -m unittest -v scripts.test_check_repo
python3 scripts/check_repo.py
```

No GitHub Actions workflow, paid external API, deployment, installer, or unreviewed execution service was created.


## Offline external-link inventory and safer outbound URL classification

This audit added a separate **read-only / no-network** public-doc inventory at `scripts/audit_external_links.py` with a six-case synthetic fixture suite `scripts/test_external_links.py`. The script parses HTTPS/HTTP URLs found in Markdown outside literal fenced code, checks the syntax of the destination host and URL and **only prints aggregate counts**. It never prints usernames, payment query values, token-like parameters or complete URL strings; it never contacts a provider or performs a redirect.

**Pinned working draft #39** at `7a9b5f60b925bca60d8537db3b776d004faddf3d`: all **13** synthetic checker tests passed (7 original structural-link fixtures plus 6 new external-link safety fixtures). Running the inventory against that draft source found **176 URL occurrences**, **96 distinct hostnames** across 83 Markdown files. **0** plain-HTTP, userinfo, non-public/private-network destination or malformed URL findings. **4** query-bearing URLs appear in **2** public support/payment-related files; whether their payment parameters are appropriate, privacy-cleared, and stable is a separate contextual review, **not a reason to silently remove donation functionality**.

Running the **same** tested scanner against draft PR #40 at source head `acdf997fa067b5e4487d7b94cc0ecfa6d0229640` found **173 URL occurrences**, **96 hostnames** across 87 Markdown files. Its findings were the same: **0** insecure/private destination indicators, **4** query-bearing URLs in **2** files, and no URL content printed. All four query strings were excluded from the printed report. Some were observed in public support/payment documentation; no payment transaction or connection was attempted.

**Critical limitation:** `STATIC_PASS_REACHABILITY_UNTESTED` is **not** confirmation that a link works, that a third-party plan is currently free, that an account or donation address is the rightful owner's, that external text or assets have distribution rights, or that linked services provide authorized API access. These must be checked separately under owner rights, cost and publication policies. The public prompts are not running AI OS software. All owner release gates remain HOLD.

Reproduce on an isolated checkout of the current draft #39:

```sh
python3 -m unittest -v scripts.test_check_repo scripts.test_external_links
python3 scripts/check_repo.py
python3 scripts/audit_external_links.py
```

No external HTTP requests, new standing CI workers, service registrations, model-provider requests, payments or release actions were made.


## Markdown accessibility hygiene follow-up — 2026-11-27

A source-pinned, **offline** Markdown accessibility hygiene audit at `scripts/audit_accessibility.py` now checks for skipped heading levels, empty image alternative text, unlabelled generic Markdown links, and missing/empty `<img>` alt attributes. Six standard-library-only synthetic regression fixtures were added at `scripts/test_accessibility.py`. Fenced code examples are deliberately excluded. This is a **conservative authoring check**, not an assistive-technology test, independent beginner evaluation, WCAG compliance certification or privacy/security audit.

At original public `main` `56f74ebeb9748b27e927a4391762a8169987ece3` and at unchanged draft PR #40 `acdf997fa067b5e4487d7b94cc0ecfa6d0229640`, the checker found **one** source-specific hierarchy issue: `docs/SHARING_AND_LICENSE_STATUS.md` line 5 jumped from an H1 heading to H3. The two affected headings were changed from `###` to `##` **in draft PR #39 only**. Their wording, licensing choices and document substance remain unchanged; this is **not** an owner's license selection.

At verified draft PR #39 commit `2d860c44b6d767865ef29dfe5fa8994c37cf80e5`, all **19/19** public standard-library tests passed (seven structural-link tests, six external URL tests, six Markdown accessibility tests). The corrected draft #39 has **zero** findings from the narrow static accessibility audit across **83 Markdown documents**. Its other checks also reported zero broken local structural references and zero unsafe external URL syntax indicators. Actual rendering with screen readers, keyboard navigation, independent novice testing, accessible QR-code payment use, external HTTP link availability, provider cost terms and release rights are **NOT VERIFIED**.

To reproduce from a pinned, isolated copy of draft PR #39:

```sh
python3 -m unittest -v scripts.test_check_repo scripts.test_external_links scripts.test_accessibility
python3 scripts/check_repo.py
python3 scripts/audit_external_links.py
python3 scripts/audit_accessibility.py
```

The Mac Studio private tasker separately tracks the same **unmerged** main-branch heading defect in W13 as `STATIC_ACCESSIBILITY_REVIEW_REQUIRED`; the public draft PR #39 is a proposed fix, **not proof the default branch was updated**. No merges, public release, third-party account requests, external model invocations or payments occurred.


### Inline-code false-positive correction — 2026-11-27

The first accessibility checker run on its **own** audit report generated a **false positive**: the report's inline-code example `<img>` was mistaken for a live unlabelled image. This is an auditor defect, not an accessibility fault in that report. Its literal Markdown heading/alt checks, the single H1-to-H3 source finding, and all original receipts were retained.

The checker and fixture were updated at exact source commit `470dfd3f60bc9d7065b4f584d832ec3ed66fa0c6` to exclude **inline code as well as fenced code** before checking actual images and links. The new test explicitly covers backtick-quoted HTML and image Markdown. The resulting **20/20 public offline tests passed** (seven structural link, six outbound URL, seven accessibility cases). The revised PR #39 audit now reports **zero narrow static Markdown accessibility findings** across 83 Markdown files, with no external network requests. The separate PR #40 draft remains an independent, unmerged candidate with the original heading issue.

These static checks do **not** establish WCAG conformance, keyboard or screen-reader operation, actual payment-QR accessibility, provider licensing or a final public release approval.
