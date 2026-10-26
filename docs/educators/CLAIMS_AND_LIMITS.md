# Claims and evidence: what faculty can responsibly say

**Source-bound educational claims matrix | Checked against public `main` 41343168a52b5b9e9fd5cd8d796eb88c1ed515a5 | 2026-10-26**

| Statement | Disposition | Evidence or limit |
| --- | --- | --- |
| The project shares free educational prompts and documentation | Supported within published invitation | [README](../../README.md), [sharing terms](../SHARING_AND_LICENSE_STATUS.md) |
| Community R1 Living is the current beginner prompt | Supported | [Community R1](../../prompts/GET_SERAPHED_COMMUNITY_R1_LIVING.md), [verification ledger](../VERIFICATION_STATUS.md) |
| Stage 0 can be practiced without any installed software | Supported as instruction | Learner saves and checks the card; no automatic persistence is implied |
| Optional offline core specifies standard-library Python 3 and SQLite | Supported as design | [Stage 1](../../prompts/stages/01_OFFLINE_CORE.md); this does not mean a qualified executable is released |
| The public Mesh educational architecture has 115 topics in 11 chapters | Supported as documentation | [Architecture index](../architecture/README.md) |
| The routing atlas describes an 18-port conceptual flow and test specifications | Supported as documentation | [Learning routes](../learning-routes/README.md); no private routing implementation is disclosed |
| A reference code candidate passed 31/31 first-party checks on two Macs | Historical, bounded first-party observation | [R1 report](../LOCAL_REFERENCE_R1_HARDENING_20261024.md); not a public clean-room executable |
| Supervised derivatives passed 57/57, 63/63 and 78/78 synthetic checks | Historical, version-specific first-party observations | [R2](../STAGE2_PUBLIC_PROMPT_TRIAL_20261024.md), [R3](../LOCAL_STAGE2_R3_SECURITY_REVIEW_20261024.md), [R4](../LOCAL_R4_MISSION_EVIDENCE_REVIEW_20261024.md); do not add scores across suites |
| Clean public-prompt reproduction of Stage 1 and Stage 2 is qualified | **Not established** | [R5](../LOCAL_R5_STAGE1_REPRODUCIBILITY_REVIEW_20261024.md): independent Stage 1 remains unqualified; Stage 2 NOT RUN |
| Prompt-only confidentiality controls are reliable | **Contradicted by observed negative tests** | [Black-box trial](../LLM_DISCLOSURE_BLACKBOX_TRIAL_20261024.md): 19 exact echoes in 24 synthetic privacy challenges; no real secrets used |
| SHA-256 journal and safe backup are deployed as public software | **Not established** | [Integrity guide](../SHA256_MEMORY_INTEGRITY_AND_RECOVERY.md) is instruction and illustration, not a tested installed implementation |
| An approved downloadable AI operating system exists in the repository | **False for this checked revision** | [README](../../README.md) explicitly says no released executable |
| No repository-wide open-source license has been selected | **Supported as a current rights limitation** | [Sharing and license status](../SHARING_AND_LICENSE_STATUS.md) explicitly withholds a blanket license |
| Universities have endorsed or adopted the curriculum | **Not established** | Treat any proposed outreach or academic pilot as pending until real replies or approvals are recorded |
| A particular university is definitively a top-10 AI school | **Do not assert from this project** | Rankings depend on year and method; not needed for faculty-fit outreach |

## First-party research pending separate release review

Unmerged [PR #29](https://github.com/SeraphPLC/age-of-free-programming/pull/29) includes a **fictional, time-compressed** 25-year tabletop reporting 12,000/12,000 source-scripted fact reconstruction and the same result from a conventional complete event log. This is a **PR claim under human review**, not material already accepted on `main`, real decades of reliability, comparative superiority or a public application release. Do not use these numbers in an outreach headline before the PR is independently reviewed and approved.

## Safe one-sentence description

> The Age of Free Programming offers free-to-read, public instructions and synthetic exercises for learning AI project continuity, verification, and local-first Python/SQLite design; it does not distribute a certified AI operating system or guarantee safe handling of private data.

## Red-flag claims to remove from faculty messages

Avoid: "open-source product" (no blanket license); "$0 total cost to every user" (hardware/provider differences); "Grade A university readiness" (not independently scored); "already adopted by colleges" (no evidence); "fully automated cross-model memory" (not an installed public capability); or "no security risk" (known prompt-only failures).

**Rule:** A new GitHub commit, tool, model output or review changes only the claims its actual evidence supports. Update the source revision after publication; do not carry historical test counts as a new release qualification.
