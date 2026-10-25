# Offline reconciliation: two copies, one honest history

**Fictional, manual-first exercise. NOT an installed syncing tool or live Seraph Mesh implementation.** No remote connection, credentials, shared account or background sync is needed.

The public [Governed Continuity Beyond the Cluster](https://docs.google.com/document/d/1mvNSlFk8k5UDSYbz5-DfykakSIYQRFi7cj-jY5WRdRw/edit) paper uses fleet management as an analogy for reconciling desired and observed state. This lab adapts the idea with ordinary, user-controlled fictional records. It does not reproduce internal Seraph protocols, clocks, fencing or conflict algorithms.

## Mission and permissions

An imaginary neighborhood workshop has a paper schedule. Two copies of the schedule are edited while disconnected.

- **Baseline `R0`**: `TASK-A: Saturday 10:00 room A`; `TASK-B: print two flyers`.
- **Local A, `R1-A`**: changes `TASK-A` to 11:00 with a note from fictitious coordinator Alex.
- **Local B, `R1-B`**: changes `TASK-A` to 09:00 with a different note from fictitious coordinator Blair; marks `TASK-B` as "flyers printed", without a receipt.
- **Human authority:** Only the fictitious real-world coordinator may choose a final workshop time in this story. A model cannot infer a winner based on the timestamp or apparent confidence.

The copies can be represented as two separately named notes in a new, safe folder. If using a tool, ask permission before file creation. **No real calendar, mail, account or cloud sync.**

## Expected reconciliation

| Item | What the learner must show | What would fail |
| --- | --- | --- |
| Common ancestry | Both edits derive from `R0` | Claim B supersedes A without a source |
| Conflict | Two incompatible proposed times for `TASK-A` | Silently accept last writer |
| Evidence | Alex and Blair notes are reports, not authoritative verified decisions | Treat a role name as permission |
| Incomplete task | B's "printed" claim is unverified until actual evidence exists | Convert claimed completion to verified |
| Durable merge | Preserve `R0`, `R1-A`, `R1-B` plus conflict record | Erase conflicting branch to make history tidy |
| Human gate | Outcome `NEEDS_COORDINATOR_DECISION` | Quietly publish new event time |
| Recovery | A fresh worker sees the unresolved conflict and safe next action | Announces reconciliation success without a decision |

## Four steps

1. **Freeze `R0`:** mark the common baseline and its source ID. If there is no real file, use `ILLUSTRATION_ONLY`.
2. **Create divergent notes:** introduce the A and B changes independently. Do not claim one remote worker actually ran unless a real provider returned a response.
3. **Reconcile without inventing truth:** report proposed states, source strengths and open conflict; preserve an immutable-looking history as a **teaching record**, not a cryptographic audit system.
4. **Obtain explicit resolution (optional):** only if a participating human really chooses a time for the fictional exercise, record `D-01` as a decision scoped to that exercise. It is not authentication or authority for real calendars.

**Example of safe final report (an illustration):**

```text
BASE: R0 (fictional)
BRANCHES: R1-A and R1-B retained
TASK-A: CONFLICT; 11:00 and 09:00 are incompatible proposals
TASK-B: CLAIMED_COMPLETE / NOT_VERIFIED
SOURCE_STRENGTH: reporter notes only; actual coordinator decision absent
MERGE: HELD
ACTION_AUTHORITY: NONE
NEXT: ask the human coordinator to resolve the fictional conflict
```

## Negative tests

- **Changed source after earlier PASS:** ensure old conclusions refer to their original revisions.
- **Offline during a needed real call:** stop with `NOT_AVAILABLE`; do not fabricate a provider message.
- **Duplicate side effect uncertain:** do not blindly retry "publish" or "send" when prior success is unknown.
- **One copy missing:** retain absence as a provenance gap; do not infer the missing copy's contents.
- **New session has old permission note:** read as historical context; authority is not inherited.
- **Reconciliation not performed:** report `NOT_RUN`, even if the illustrative desired result is obvious.

For real systems, correctness, atomicity, provenance security, tamper resistance, conflict resolution, deletion semantics and concurrency require implementation-specific engineering and testing. This document does not provide such a product.

Related: [handoff and recovery](../learning-routes/04_HANDOFF_EVIDENCE_AND_RECOVERY.md), [qualification rewind](QUALIFICATION_REWIND.md), [privacy/IP policy](../PRIVACY_IP_AND_RELEASE_GATE.md).