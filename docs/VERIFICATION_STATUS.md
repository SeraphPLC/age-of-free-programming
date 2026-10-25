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
| Separate local executable prototype guided by public v0.4 | **26/26 FIRST-PARTY TESTS PASSED ON TWO MACS (19/21 fully covered)** | Developer-authored synthetic code, **not publicly released**; M02 and M19 have scope limits. [Trial details](LOCAL_REFERENCE_TRIAL_20261024.md) |\n| Independent fresh-chat full v0.4 build / M01–M21 acceptance | **NOT VERIFIED** | A new Python process is not a genuinely fresh AI chat or independent code reviewer |
| M22 cross-model cold restart | **NOT RUN** | A single chat role-play does not establish independently reproduced state |
| Mac/Windows/Linux general compatibility | **NOT VERIFIED ACROSS ALL CLAIMED PLATFORMS** | A different historical Linux prototype pass is not universal portability |
| Independent legal/security or multi-provider council review | **NOT PERFORMED FOR THIS RELEASE** | Model-generated agreement is not independent review |
| Formal whole-repository content/software license | **NOT SELECTED** | See [license discussion](LICENSE_DECISION_BRIEF.md) and [sharing status](SHARING_AND_LICENSE_STATUS.md) |
| Public Git history email privacy | **NOREPLY ON AUDITED REACHABLE COMMITS** | All commits checked on 2026-10-24 used noreply; the count changes when new commits land. Older detached commits and caches **may still be reachable** and require GitHub-side follow-up. |
| Public Issues / private vulnerability reporting | **Issues disabled / private reporting enabled** | No build reports are requested from users |
| Public content audit | **STATIC TEXT/JSON ONLY AS CHECKED** | Pattern checks and review do not prove absence of every privacy, security or legal issue |

## October 24 experimental candidate — evidence boundary\n\nA separate **new local Python/SQLite implementation** now exists. Its first-party suite passed 26/26 tests on macOS 26.6 and macOS 27.0; both machines also passed when a macOS sandbox denied network access. Fixed fictional memory records were reconstructed 20/20. These are **synthetic, developer-run tests** on a withheld local candidate—not proof that a fresh AI chat independently generated the same code, performed a review, or met production security/privacy requirements. The actual code is not a public download and no distribution license has been chosen. Full scope, fingerprints, failures and limitations: [Local Reference Trial](LOCAL_REFERENCE_TRIAL_20261024.md).\n\n## Main unresolved verification gap

A capable AI might build strong Python/SQLite continuity software from the specification, but **that has not yet been established by a clean-room, fresh-chat build of the public prompt**. Reproducing Stage 1 is not equivalent to passing all memory-fidelity cases. A JSON Schema validator checking example files is not evidence of working encryption, consent, retention, protected actions, durable service operation, or semantic memory accuracy.

**Highest-value remaining experiments:** independent reviewer inspection of the separate local reference code and its failure receipts; a genuinely **fresh AI chat** that builds or reconstructs state from a frozen packet; actual cross-model M22 with provenance; Windows/Linux test environments; stronger privacy deletion and trusted history anchors. A test run by the authoring AI is not independent review. Keep failures as evidence and never silently upgrade NOT RUN or PARTIAL to PASS.

## Historical privacy clarification

Main branch history was rewritten to use a GitHub `noreply` commit identity. At the latest 2026-10-24 audit, **all commits then reachable in main's current history used noreply**; their number changes with future commits. This **does not guarantee deletion of old detached commit objects**, API lookups, forks, external clones or search caches. Do not publish the historical email address or describe complete removal until GitHub can confirm relevant purge behavior. Avoid another uncoordinated force-push; the default branch is protected.

See [privacy and release gate](PRIVACY_IP_AND_RELEASE_GATE.md), [private safety reporting](../SECURITY.md), and the [private self-check](BUILD_REPORT_TEMPLATE_OFFLINE.md).
