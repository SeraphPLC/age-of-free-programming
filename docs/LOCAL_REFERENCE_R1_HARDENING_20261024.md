# R1 Local Reference Hardening — October 24, 2026

**PUBLIC-SAFE RESULTS ONLY · EXPERIMENTAL · NO EXECUTABLE RELEASE OR LICENSE GRANT**

This updates the [initial R0 synthetic trial](LOCAL_REFERENCE_TRIAL_20261024.md). An original, separately stored Python/SQLite continuity prototype was developed against the frozen public [v0.4 builder specification](../prompts/BUILD_YOUR_OWN_AI_OS_v0.4_MEMORY_FIDELITY_CANDIDATE.md). The executable remains **local** for review, not downloadable through this repository. Nothing requires, uses, or connects to private Seraph code, credentials, accounts, or infrastructure. Only fictional task/memory data were used.

## What the R1 review verified

| Scope | Actually observed |
| --- | --- |
| First-party regression tests | **31/31 PASS** on two separate Macs after R1 hardening |
| Interpreter coverage on one Mac | Python **3.9, 3.12, 3.14** each passed the same 31-test suite |
| Clean ZIP on second Mac | SHA-256 and all manifest file hashes matched; extracted code passed **31/31** with Python 3.9 |
| Network-denied macOS sandbox | **31/31 PASS** on both machines; separate socket-connection controls showed the sandbox denied network access |
| Fixed fictional memory benchmark | **20/20** exact expected synthetic records; **3/3** corrections and **2/2** contradictions |
| Public JSON Schema compatibility | **7/7** valid/invalid cases met expectations using an already installed offline Draft 2020-12 validator with format checks |
| Runtime source audit | No network-client or shell-execution imports identified; selected **Ruff S/B** checks reported no findings |
| Owner-controlled sensitive data | **Real personal data not tested or approved**; current fixtures are invented |
| Public executable source | **NOT PUBLISHED**; source and raw logs remain local |
| Software distribution license | **NOT SELECTED** |

R1 repairs defects discovered during negative testing: a restart packet that did not match the published timestamp/property contract, non-finite clock values, malformed untrusted handoffs, over-capacity handoff lists, and overly broad SQL construction in a fixed internal maintenance path. Tests were added before requalification. These were errors in the experimental implementation, **not evidence that the public educational prompt itself was an executable product**.

## Two real local model observations (not a simulated council)

A separate, entirely fictional source-evidence question was submitted to two installed local models in fresh, independent inference calls. This was **outside the Python continuity program**, with no cloud-model API or private source material.

- **Qwen 2.5 7B:** 7/7 expected typed answer fields.
- **Llama 3.2 3B:** 5/7 fields on the first call. Its two errors were strings representing `false` rather than actual JSON booleans in authority-related answers.
- **Second Llama call with a typed-output contract:** 7/7. Both the original 5/7 result and the improved 7/7 result remain preserved in private evidence.

**Interpretation:** a model's intended answer is not equivalent to a correctly typed, verified application response. Use strict output validation and fail closed on malformed authority values. These calls show **limited independent local-model evidence handling**, not genuine multi-provider security review or long-term memory certification.

## Acceptance-map honesty

- **M01, M03–M18, M20–M21:** 19 synthetic cases PASS as originally scoped.
- **M02: PARTIAL.** A genuinely fresh Python process and separate local-model prompts were tested; a new cloud/browser AI chat receiving a full sanitized project packet and reconstructing verified state was not.
- **M19: PARTIAL in the formal test rubric**, supplemented by two OS-level deny-network sandbox passes. This does not certify every possible network path on every computer.
- **M22: PARTIAL.** Two genuinely separate local models returned recorded results, but full cross-model state reconstruction, independently checked source access, and cross-provider qualification remain outstanding.
- **Windows and Linux:** NOT RUN. No additional VM with broader access to unrelated local files was started for this experiment.
- **Legal/privacy/independent security approval:** NOT PERFORMED.

## Outstanding release gates

An independent reviewer must inspect the actual withheld source and raw failures. Ownership, legal distribution terms, backup-erasure semantics, trusted history anchoring, real-data consent and authentication, portability, and complete fresh-chat/cross-model reconstruction must be resolved before calling the executable public AI OS 1.0. Historical internal Seraph results cannot be substituted for these independent checks.

**Distribution posture unchanged:** Share the free prompts and safety guidance. Do not publish the experimental executable, its local database, private raw logs, model sessions or unrelated files as a general-purpose product.

See [Verification Status](VERIFICATION_STATUS.md), [Release Gate](PRIVACY_IP_AND_RELEASE_GATE.md), and [License Decision Brief](LICENSE_DECISION_BRIEF.md).
