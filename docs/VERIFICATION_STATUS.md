# Verification status
**2026-10-24 snapshot — educational public prompts, NOT executable software certification**

| Claim | Status |
| --- | --- |
| Archived v0.1 prompt | PUBLISHED, EDUCATIONAL |
| Hardened v0.2 | PUBLISHED CANDIDATE, NOT INDEPENDENTLY BUILT FROM FRESH CHAT |
| Expanded v0.3 | PUBLISHED CANDIDATE, NOT INDEPENDENTLY REPRODUCED |
| Isolated Linux synthetic reference implementation | INTERNAL 30/30 AUTOMATED TESTS PASS AFTER FIXES; this is NOT the public prompt build |
| Public downloadable reference executable | HELD / NOT RELEASED |
| Windows/macOS fresh build compatibility | NOT VERIFIED |
| Actual continuous autonomous agents or multi-model handoff | NOT VERIFIED |
| Independent five-seat frontier Council/security review | NOT PERFORMED ON THIS PUBLIC PROMPT RELEASE |
| Formal public software/data license | NOT SELECTED; see [license status](SHARING_AND_LICENSE_STATUS.md) |
| Public repository current content scan | TEXT-ONLY WITH NO OBVIOUS SECRET IN DOCUMENT CONTENT; NOT A COMPLETE SECURITY AUDIT |
| Public historical commit email privacy | PERSONAL AUTHOR EMAIL EXPOSED; NOT REMOVED; FUTURE NOREPLY AUTHOR IS BEING USED |

Early prototype negative tests found and corrected a task/event integrity mismatch and a symlink path-escape backup flaw. This does **not** prove resistance to an active attacker who rewrites all local evidence or that the educational prompt yields equivalent results with any AI.

Actual test counts and user reports must not be elevated to independent certification. See [release and legal gate](PRIVACY_IP_AND_RELEASE_GATE.md), [private security reporting](../SECURITY.md) and [build report](BUILD_REPORT.md).
