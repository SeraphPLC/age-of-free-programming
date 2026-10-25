# Verification status — educational project, not a software certification

**Checked 2026-10-24 against current public GitHub history and documentation.** Test outcomes are version- and scope-specific. No completed public executable, independent security audit or guaranteed memory fidelity is claimed.

| Item | Status | Meaning |
| --- | --- | --- |
| Get Seraphed Community | **PUBLISHED — manual chat workflow** | Works as copyable instructions; does not install persistent memory or automatically access old chats |
| Original v0.1, v0.2, v0.3, v0.4 | **PUBLISHED EDUCATIONAL PROMPTS** | Plans/instructions, not ready-to-run software |
| New staged prompts 0–4 | **DOCUMENTARY CANDIDATES** | Narrower steps and handoffs; full clean-room build from them **NOT RUN** |
| Separate withheld synthetic Linux reference | **30/30 TESTS PASSED AFTER FIXES (historical)** | Tests were on a different internal program, **not** a public-prompt-generated build or independent release certification |
| Public downloadable reference implementation | **NOT RELEASED** | Source ownership, portability, vulnerability/rights review and repeatable test receipts remain gated |
| Memory schema & synthetic examples | **STATIC JSON DOCUMENTS** | Their syntax/shape can be checked, but no application-level guarantees follow from schema conformity |
| Full v0.4 / M01–M21 working implementation | **NOT RUN / NOT VERIFIED** | No completed public code run from the prompt has been independently reproduced |
| M22 cross-model cold restart | **NOT RUN** | A single chat role-play does not establish independently reproduced state |
| Mac/Windows/Linux general compatibility | **NOT VERIFIED ACROSS ALL CLAIMED PLATFORMS** | A different historical Linux prototype pass is not universal portability |
| Independent legal/security or multi-provider council review | **NOT PERFORMED FOR THIS RELEASE** | Model-generated agreement is not independent review |
| Formal whole-repository content/software license | **NOT SELECTED** | See [license discussion](LICENSE_DECISION_BRIEF.md) and [sharing status](SHARING_AND_LICENSE_STATUS.md) |
| Current public Git history email | **24/24 visible commits use GitHub noreply** | Verified on current reachable main history; older detached commits and caches **may still be reachable** and require GitHub-side follow-up |
| Public Issues / private vulnerability reporting | **Issues disabled / private reporting enabled** | No build reports are requested from users |
| Public content audit | **STATIC TEXT/JSON ONLY AS CHECKED** | Pattern checks and review do not prove absence of every privacy, security or legal issue |

## Main unresolved verification gap

A capable AI might build strong Python/SQLite continuity software from the specification, but **that has not yet been established by a clean-room, fresh-chat build of the public prompt**. Reproducing Stage 1 is not equivalent to passing all memory-fidelity cases. A JSON Schema validator checking example files is not evidence of working encryption, consent, retention, protected actions, durable service operation, or semantic memory accuracy.

**Highest-value experiments:** a clean-room Stage 1 program with genuine command receipts; repeat Stage 2 claims and backup tests; implement and run the M01–M21 synthetic suite on the generated program; then compare two genuinely separate fresh observers under source/permission controls. Keep failures as evidence, never silently upgrade NOT RUN to PASS.

## Historical privacy clarification

Main branch history was rewritten to use a GitHub `noreply` commit identity. All **24 current visible commits** inspected today use that identity; this **does not guarantee deletion of old commit objects**, API lookups, forks, external clones or search caches. Do not publish the historical email address or describe complete removal until GitHub can confirm relevant purge behavior. Avoid another uncoordinated force-push; the default branch is protected.

See [privacy and release gate](PRIVACY_IP_AND_RELEASE_GATE.md), [private safety reporting](../SECURITY.md), and the [private self-check](BUILD_REPORT_TEMPLATE_OFFLINE.md).
