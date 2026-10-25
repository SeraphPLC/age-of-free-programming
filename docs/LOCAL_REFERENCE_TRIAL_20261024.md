# Local experimental reference trial — 2026-10-24

**Status: developer-run synthetic trial, NOT a public code release or independent security certification.**

A new, original Python/SQLite local continuity prototype was authored from the public [v0.4 educational specification](../prompts/BUILD_YOUR_OWN_AI_OS_v0.4_MEMORY_FIDELITY_CANDIDATE.md) frozen at Git commit `c50781ff459e41f7c42a9da91cb55a98194b1632`. The experimental prototype was written in a new isolated local workspace using **only synthetic data**. No private Seraph source code, private account integrations, archived datasets, model weights, or external endpoints were imported.

## Test results actually observed

| Test scope | Observed result |
| --- | --- |
| First-party Python `unittest` regressions | **26/26 passed** on macOS 26.6 (one Mac) |
| Repeated tests on Python 3.12.13 and Python 3.14.6 | **26/26 passed** for each interpreter on that Mac |
| Clean ZIP extraction and test on a different Mac, macOS 27.0 / Python 3.9.6 | **26/26 passed** |
| macOS process sandbox with network access denied | **26/26 passed** on both Macs; a separate socket connection attempt was blocked by the OS sandbox |
| Reconstructed fixed synthetic facts | **20/20**, each with source ID and a separate fictional evidence receipt |
| Synthetic corrections | **3/3** correctly applied |
| Synthetic contradiction pairs | **2/2** correctly detected |
| M01–M21 classification | **19 PASS**, **M02 PARTIAL** (fresh process, not a fresh AI chat), **M19 PARTIAL** in the original runner (network source/in-process checks; supplemented by both OS sandbox runs) |
| M22 genuine cross-model comparison | **NOT RUN** |
| Executable released to public GitHub | **NO; locally retained review candidate only** |

The initial developer run failed **one** duplicate-record error-handling check. That defect was corrected and the original failure was retained in private test evidence; the full suite was rerun after the correction. This is **not** a claim of bug-free or formally audited software.

The implementation and tests were authored in the same AI-assisted work session. **They are not independently reproduced from a fresh AI chat or independently security reviewed**, notwithstanding successful execution on two machines.

## Fingerprints for future reproducibility

The following fingerprints identify the tested original local source files; the files themselves have not been publicly released pending rights and security review:

- Core Python implementation SHA-256: `62792b76332fca80d34ee2aaa3e875d9476037eb6ddde28a13d5701aa64d53b6`.
- Main acceptance test source SHA-256: `8d13df0f28790c3f454fdf88b87a0484a8d6a83f146f48f11fb90243ddb445d1`.
- Review-only ZIP SHA-256: `0497f6f384fc4a450160dcd070c4034a69b3831f2011d682b60fcfac4dfa97e4`.

The ZIP is **not** publicly downloadable. These hashes document byte identity only, not code safety, authorship, legal ownership, or historical authenticity.

## Known unsolved problems

1. **A same-user attacker who controls the entire local database can coherently rewrite the event chain and its projections.** The M12 test demonstrates that a local hash chain is not tamper-proof; the program explicitly warns about absent independent historical authentication.
2. The current synthetic approval flags, owner labels, and private claim files are not multi-user authentication. Do not rely on them to perform real sensitive account or system actions.
3. The memory deletion exercise verifies active record/index removal with synthetic strings. Existing backups, journal metadata/digests, filesystem traces, exports and cloud copies are **not** guaranteed erased.
4. A real second AI conversation has **not** rebuilt the project state from the handoff. Fresh process reconstruction does not count as full fresh-chat semantic fidelity.
5. No Windows/Linux portability, model-to-model correctness, production privacy/retention compliance, or independent legal/security review is established.
6. No source-code distribution license has been selected, and third-party/open-data/model license rights have not been approved for a bundled release.

## What is and is not available now

The **public educational prompts, static schemas, staged builder path and test requirements** remain freely readable. A separate **local executable candidate and private test receipts** exist for rights-holder and independent reviewer evaluation, but are intentionally held from GitHub distribution.

**Next release gates:** confirm ownership and licensing scope; obtain independent code/security review; run a genuine fresh-AI clean-room build and cross-model M22 where permitted; expand erasure/retention testing; qualify more operating systems. The project cannot honestly claim "AI OS 1.0 shipped" from this trial alone.

See [Verification Status](VERIFICATION_STATUS.md), [License Decision Brief](LICENSE_DECISION_BRIEF.md) and [Privacy/IP Release Gate](PRIVACY_IP_AND_RELEASE_GATE.md).
